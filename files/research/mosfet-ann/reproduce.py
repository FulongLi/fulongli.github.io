"""Re-run the MOSFET ANN training and export the website results.

Checkout AIPE-MOSFET-ANN-Modelling at 720575683673259a6ddcd29a6c69771e43b6d17a.
Install torch, numpy, pandas, scikit-learn, joblib, matplotlib, openpyxl and plotly.
Run: python reproduce.py --source /path/to/repo --output-dir /path/to/results
Uses the original training architecture, 2,000 epochs, Adam lr=0.01 and seed 42.
The upstream interactive main is bypassed and the actual JSON filename is supplied.
"""
import argparse
import csv
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import platform
import time

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--source', type=Path, required=True)
parser.add_argument('--output-dir', type=Path, required=True)
args = parser.parse_args()
source = args.source.resolve()
out = args.output_dir.resolve()
out.mkdir(parents=True, exist_ok=True)
os.environ['MPLBACKEND'] = 'Agg'

import numpy as np
import pandas as pd
import torch
import sklearn
import matplotlib
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from plotly.offline import get_plotlyjs

torch.set_num_threads(4)
spec = importlib.util.spec_from_file_location('mosfet_upstream', source/'C2MSeries_ANN_full_model.py')
upstream = importlib.util.module_from_spec(spec)
spec.loader.exec_module(upstream)
data = upstream.load_json_data(str(source/'C2M0080120D.json'))
tx, ty = upstream.load_excel_data(str(source/'C2M0040120D_Thermal_Impedance_Data.xlsx'))

# Save newly trained files separately; never overwrite the repository's checkpoint.
run_dir = out/'trained-model'
run_dir.mkdir(exist_ok=True)
previous_dir = Path.cwd()
os.chdir(run_dir)
start = time.perf_counter()
try:
    result = upstream.process_and_train_combined_model(data, tx, ty)
finally:
    os.chdir(previous_dir)
elapsed = time.perf_counter() - start
(model, switching_scaler, mosfet_scaler, diode_scaler,
 mosfet_df, mosfet_test_x, mosfet_test_y,
 diode_df, diode_test_x, diode_test_y, _, _) = result
model.eval()

def predict(x, task, scaler=None):
    x = scaler.transform(x) if scaler is not None else x
    with torch.no_grad():
        return model(torch.tensor(x, dtype=torch.float32), task=task).numpy().ravel()

def metrics(actual, predicted):
    assert np.isfinite(predicted).all()
    return {'mae': float(mean_absolute_error(actual, predicted)),
            'rmse': float(np.sqrt(mean_squared_error(actual, predicted))),
            'r2': float(r2_score(actual, predicted)), 'n': int(len(actual))}

scores = {}
surfaces = {}
test_rows = []
fig, axes = plt.subplots(1, 2, figsize=(9, 4.3), layout='constrained')
for ax, key, title, frame, scaler, test_x, test_y in zip(
        axes, ['conduction_mosfet', 'conduction_diode'], ['MOSFET channel', 'Body diode'],
        [mosfet_df, diode_df], [mosfet_scaler, diode_scaler],
        [mosfet_test_x, diode_test_x], [mosfet_test_y, diode_test_y]):
    predicted = predict(test_x, key, scaler)
    scores[key] = {**metrics(test_y, predicted), 'unit':'V', 'evaluation':'held-out reference table rows',
                   'train_n':len(frame)-len(test_y), 'total_n':len(frame)}
    held = {tuple(row) for row in test_x.tolist()}
    all_x = frame[['Ids','Temperature']].to_numpy()
    assert len(held) == len(test_x) and len({tuple(row) for row in all_x.tolist()}) == len(frame)
    is_test = [tuple(row) in held for row in all_x.tolist()]
    assert sum(is_test) == len(test_y)
    current = np.linspace(frame.Ids.min(), frame.Ids.max(), 41)
    temperature = np.linspace(frame.Temperature.min(), frame.Temperature.max(), 41)
    xx, yy = np.meshgrid(current, temperature)
    zz = predict(np.column_stack([xx.ravel(),yy.ravel()]), key, scaler).reshape(xx.shape)
    assert np.isfinite(zz).all()
    surfaces[key] = {'title':title, 'current':current.tolist(), 'temperature':temperature.tolist(),
                     'voltage':zz.tolist(), 'reference':{
                         'current':frame.Ids.tolist(), 'temperature':frame.Temperature.tolist(),
                         'voltage':frame.Vds.tolist(), 'held_out':is_test}}
    for (current_value,temp), actual, pred in zip(test_x, test_y, predicted):
        test_rows.append({'task':key, 'current_A':float(current_value), 'temperature_C':float(temp),
                          'reference_V':float(actual), 'predicted_V':float(pred),
                          'error_V':float(pred-actual)})
    ax.scatter(test_y, predicted, s=36, color='#008da0', edgecolors='white', linewidths=0.5, zorder=3)
    low, high = min(test_y.min(), predicted.min()), max(test_y.max(), predicted.max())
    ax.plot([low,high], [low,high], '--', color='#89939c', linewidth=1.2, label='Ideal agreement')
    ax.set(xlabel='Reference voltage (V)', ylabel='ANN prediction (V)', title=title)
    ax.text(0.05,0.94,f"{len(test_y)} held-out points\nRMSE {scores[key]['rmse']:.3f} V",transform=ax.transAxes,va='top')
    ax.grid(alpha=0.15)
    ax.spines[['top','right']].set_visible(False)
fig.savefig(out/'held-out-validation.png',dpi=180)
plt.close(fig)

# These switching tests contain resistance-scaled variants of source rows.
# They are interpolation checks, not independent switching experiments.
for key, label, json_key in [('switching_on','TurnOnEnergy','TurnOnLoss'),
                              ('switching_off','TurnOffEnergy','TurnOffLoss')]:
    frame = upstream.generate_switching_loss_data(data['SemiconductorData'][json_key], label,
                                                  np.arange(1,31),np.arange(1,31))
    datasets, scaler, raw_x, raw_y = upstream.prepare_data(
        frame,['Current','Voltage','Temperature','Rgon','Rgoff'],label)
    scores[key] = {**metrics(raw_y,predict(raw_x,key,scaler)), 'unit':'microjoule',
                   'evaluation':'held-out augmented rows; source conditions overlap training',
                   'total_n':len(frame), 'train_n':len(frame)-len(raw_y)}
scores['thermal'] = {**metrics(ty.ravel(),predict(tx,'thermal')), 'unit':'K/W',
                     'evaluation':'training fit only; no held-out thermal data'}

# Check that serialisation preserves the fresh model predictions.
restored = upstream.CombinedANNModel()
restored.load_state_dict(torch.load(run_dir/'c2m0080120d_ANN_Trainned_Model.pth',map_location='cpu',weights_only=True))
restored.eval()
probe = torch.tensor(mosfet_scaler.transform(mosfet_test_x),dtype=torch.float32)
with torch.no_grad():
    assert torch.equal(model(probe,task='conduction_mosfet'),restored(probe,task='conduction_mosfet'))

with (out/'test-predictions.csv').open('w',newline='',encoding='utf-8') as f:
    writer=csv.DictWriter(f,fieldnames=test_rows[0].keys())
    writer.writeheader();writer.writerows(test_rows)
(out/'surfaces.json').write_text(json.dumps(surfaces,allow_nan=False),encoding='utf-8')
(out/'plotly.min.js').write_text(get_plotlyjs(),encoding='utf-8')
metadata = {
    'source':'https://github.com/FulongLi/AIPE-MOSFET-ANN-Modelling',
    'revision':'720575683673259a6ddcd29a6c69771e43b6d17a',
    'device':'C2M0080120D', 'training_seconds':elapsed,
    'method':{'seed':42,'epochs':2000,'optimizer':'Adam','learning_rate':0.01,
              'split':'80/20 random rows, random_state=42; thermal uses all rows',
              'scaling':'StandardScaler fitted on training inputs; targets unscaled',
              'architecture':{'switching':'5-32-32, shared layers with separate on/off outputs',
                              'mosfet':'2-32-32-1','diode':'2-32-32-1','thermal':'1-64-64-1'},
              'loss':'sum of five MSE losses','activation':'ReLU','cpu_threads':4},
    'versions':{'python':platform.python_version(),'torch':torch.__version__,
                'numpy':np.__version__,'pandas':pd.__version__,
                'scikit-learn':sklearn.__version__,'matplotlib':matplotlib.__version__},
    'input_sha256':{name:hashlib.sha256((source/name).read_bytes()).hexdigest() for name in
                    ['C2MSeries_ANN_full_model.py','C2M0080120D.json','C2M0040120D_Thermal_Impedance_Data.xlsx']},
    'metrics':scores,
    'checks':{'finite_predictions':True,'unique_disjoint_conduction_split':True,
               'checkpoint_round_trip':True},
    'limitations':[
        'Reference tables in the repository; their measurement provenance is not established here.',
        'Static conduction held-out rows test interpolation, not a new device or new measurement campaign.',
        'Switching data includes a 900 C table entry and resistance-scaled augmentation; no claim of physical validity there.',
        'Thermal input is named C2M0040120D, not C2M0080120D; device correspondence is unconfirmed.',
        'Upstream test/app network widths differ from training. This run uses the training architecture throughout.',
        'No constraints enforce zero-current voltage, passivity or monotonicity; low-current error should be checked.',
    ],
}
(out/'run-metadata.json').write_text(json.dumps(metadata,indent=2,allow_nan=False),encoding='utf-8')
print(json.dumps({'training_seconds':elapsed,'metrics':scores,'checks':metadata['checks']},indent=2),flush=True)
