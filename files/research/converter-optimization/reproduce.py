"""Reproduce the website's illustrative design sweep using the upstream model.

Install the upstream project's dependencies, then run:
python reproduce.py --source /path/to/AIPE-Converter-Optimisation-Agent --output-dir results

Source revision: 3b682989b7072bbd42497c5432f2df246786a508
The model and solver settings are unchanged. This script adds reporting only.
"""
import argparse
import csv
import json
import platform
import sys
from dataclasses import asdict
from importlib.metadata import version
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--source', type=Path, required=True)
parser.add_argument('--output-dir', type=Path, required=True)
args = parser.parse_args()
sys.path.insert(0, str(args.source.resolve() / 'src'))

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import cardiff_converter_opt.optimization as opt
from cardiff_converter_opt.parameters import DesignParameters

out = args.output_dir
out.mkdir(parents=True, exist_ok=True)
solver_records = []
original_minimize = opt.minimize

def tracked_minimize(*positional, **keywords):
    result = original_minimize(*positional, **keywords)
    solver_records.append({
        'solver_success': bool(result.success),
        'solver_message': str(result.message),
        'solver_iterations': int(result.nit),
    })
    return result

opt.minimize = tracked_minimize
p = DesignParameters()
try:
    points = opt.pareto_sweep(p)
finally:
    opt.minimize = original_minimize

rows = []
for pt, status in zip(points, solver_records):
    eff, density = opt.efficiency_and_power_density(p, pt)
    rows.append({**asdict(pt), 'efficiency_pct': float(eff),
                 'power_density_kw_per_l': float(density), **status})
if len(rows) != 21 or not all(r['solver_success'] for r in rows):
    raise RuntimeError('Incomplete sweep or solver failure; inspect before publishing.')
for r in rows:
    assert np.isfinite([r['p_total'], r['v_total_m3'], r['efficiency_pct']]).all()
    assert np.isclose(r['p_total'], r['p_semiconductor'] + r['p_inductor'] + r['p_capacitor'])
    assert np.isclose(r['v_total_m3'], r['v_switch_m3'] + r['v_inductor_m3'] + r['v_capacitor_m3'])
with (out / 'design-sweep.csv').open('w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11,
                     'axes.spines.top': False, 'axes.spines.right': False,
                     'axes.labelcolor': '#30363d', 'text.color': '#30363d'})
fig, ax = plt.subplots(figsize=(8, 5.2), layout='constrained')
rho = np.array([r['power_density_kw_per_l'] for r in rows])
eff = np.array([r['efficiency_pct'] for r in rows])
ax.plot(rho, eff, color='#008da0', linewidth=1.7, alpha=0.75, zorder=2)
ax.scatter(rho, eff, color='#008da0', s=28, zorder=3)
selected = [0, 10, 20]
labels = ['Volume-focused', 'Equal-weight', 'Loss-focused']
offsets = [(-12, 20), (14, -30), (14, 15)]
for i, label, offset in zip(selected, labels, offsets):
    ax.scatter(rho[i], eff[i], s=70, color='#213c50', zorder=4)
    ax.annotate(label, (rho[i], eff[i]), xytext=offset, textcoords='offset points',
                ha='right' if i == 0 else 'left', fontsize=10,
                bbox={'facecolor':'white','edgecolor':'none','alpha':0.85,'pad':2})
ax.set(xlabel='Modelled power density (kW/L)', ylabel='Modelled efficiency (%)',
       title='Efficiency and compactness: the design trade-off',
       xlim=(4.55, 6.8), ylim=(96.3, 98.3))
ax.grid(alpha=0.18)
fig.savefig(out / 'design-tradeoff.png', dpi=180)
plt.close(fig)

pt = points[10]
volumes = np.array([pt.v_switch_m3, pt.v_inductor_m3, pt.v_capacitor_m3]) * 1e6
losses = np.array([pt.p_semiconductor, pt.p_inductor, pt.p_capacitor])
fig, axes = plt.subplots(2, 1, figsize=(8, 5.5), layout='constrained')
colors = ['#008da0', '#546c91', '#cc8549']
names = ['Semiconductors', 'Inductors', 'Capacitors']
for ax, values, unit, title in zip(axes, [volumes, losses], ['cm³', 'W'],
                                  ['Component volume', 'Component loss']):
    ax.barh(names, values, color=colors, height=0.55)
    ax.invert_yaxis()
    ax.set_xlim(0, max(values) * 1.25)
    ax.set_xlabel(unit)
    ax.set_title(title, loc='left', fontsize=12)
    ax.grid(axis='x', alpha=0.15)
    ax.set_axisbelow(True)
    for i, value in enumerate(values):
        ax.text(value + max(values)*0.02, i, f'{value:.2f}', va='center', fontsize=10)
fig.suptitle('Where volume and losses come from — equal-weight design', fontsize=13)
fig.savefig(out / 'component-breakdown.png', dpi=180)
plt.close(fig)

metadata = {
    'source': 'https://github.com/FulongLi/AIPE-Converter-Optimisation-Agent',
    'revision': '3b682989b7072bbd42497c5432f2df246786a508',
    'parameters': asdict(p),
    'python': platform.python_version(),
    'dependencies': {name: version(name) for name in ['numpy','scipy','matplotlib']},
    'solver_success_count': sum(r['solver_success'] for r in rows),
    'selected_row_indices': selected,
    'conventions': {
        'efficiency_pct': '100 * (1000 - total_loss_W) / 1000; upstream reporting convention',
        'power_density_kw_per_l': '(1000 - total_loss_W) / 1000 / (total_volume_m3 * 1000)',
        'volume': 'Sum of modelled switches, inductors and capacitors; heat sink excluded',
    },
    'limitations': [
        'Python reimplementation with calibrated component volumes, not original MATLAB or hardware results.',
        'SLSQP uses the upstream unscaled variables and warm starts; frequency stays near 175 kHz.',
        'Junction-temperature rise is an independent bounded input, not a coupled thermal solution.',
        'Solver success does not certify a global optimum or a globally Pareto-optimal front.',
    ],
}
(out / 'run-metadata.json').write_text(json.dumps(metadata, indent=2), encoding='utf-8')
print(json.dumps({'selected_designs': [rows[i] for i in selected]}, indent=2))
