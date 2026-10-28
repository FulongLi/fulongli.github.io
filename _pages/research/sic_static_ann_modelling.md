---
layout: single
title: "SiC Power Devices — Static ANN Modelling"
permalink: /research/semiconductor-device-modelling/static-ann/
author_profile: true
body_class: device-project-page
project_stylesheet: /assets/css/marine-project.css
project_contents: true
excerpt: "Neural-network models of SiC conduction, switching energy and thermal response, assessed against a buck converter up to 3 kW."
---

I led the development and experimental assessment of a data-based model of the **C2M0080120D SiC MOSFET** for converter loss and temperature calculations. Neural networks fit the device's conduction, switching-energy and thermal characteristics, and a buck-converter load sweep tests the resulting loss predictions.

<h2 id="overview">Device Characteristics for Loss Models</h2>

A converter-level loss model treats each switch as a set of characteristic functions rather than simulating every switching waveform. Three are needed: the conduction voltage as a function of current and junction temperature, the energy lost at each turn-on and turn-off as a function of voltage, current, temperature and gate resistance, and the thermal impedance that turns dissipated power into temperature rise. Circuit simulators with thermal models use the same description while keeping the electrical switching ideal.

These characteristics come as tables from datasheets, manufacturer models and measurements. An artificial neural network (ANN) can learn each table as a continuous function, so the loss model can be evaluated smoothly at any operating point within the data. The model represents characteristic surfaces; it does not resolve the electrical waveform during a switching transition.

<h2 id="data-and-model-functions">Building the ANN Model</h2>

<h3 id="network-structure">Model Branches</h3>

I organised the reference data as current–temperature–voltage samples for conduction and as event energies at specified voltage, current and temperature for switching, treating the body diode separately from the MOSFET channel. The public training implementation uses fully connected feedforward networks with ReLU hidden layers and linear outputs:

<div class="project-table-scroll" role="region" aria-label="Static ANN branches and layer structures" tabindex="0" markdown="1">

| Model branch | Inputs | Hidden layers | Output |
|---|---|---|---|
| MOSFET conduction | I<sub>DS</sub>, T<sub>j</sub> | 32 → 32 | V<sub>DS</sub> |
| Body-diode conduction | I<sub>D</sub>, T<sub>j</sub> | Separate 32 → 32 | V<sub>F</sub> |
| Turn-on / turn-off energy | I, V, T<sub>j</sub>, R<sub>g,on</sub>, R<sub>g,off</sub> | Shared 32 → 32 | Separate E<sub>on</sub> and E<sub>off</sub> heads |
| Thermal response | Time | Separate 64 → 64 | Z<sub>th</sub>(t) |

</div>

Separate conduction networks let the channel and diode characteristics be fitted independently, while the two switching outputs share one hidden representation.

<h3 id="network-training">Training</h3>

Electrical inputs are standardised with the training-set mean and standard deviation, and the same scaler is saved with the weights for later queries. Training holds out 20% of the electrical samples and minimises the sum of the five branch mean-square errors with the Adam optimiser at a 0.01 learning rate over 2,000 epochs. The hold-out split checks interpolation within the tables; the converter experiment below provides the independent test of loss prediction.

<figure>
  <a href="/images/research/sumitomo-device-modelling/ann-conduction-characteristic.png" target="_blank" rel="noopener"><img src="/images/research/sumitomo-device-modelling/ann-conduction-characteristic.png" alt="ANN conduction-voltage surface versus current and temperature with reference samples" width="1490" height="850" loading="lazy"></a>
  <figcaption>Fitted conduction-voltage surface against current and junction temperature, with the reference samples.</figcaption>
</figure>

<figure class="half">
  <a href="/images/research/sumitomo-device-modelling/ann-turn-on-energy.png" target="_blank" rel="noopener"><img src="/images/research/sumitomo-device-modelling/ann-turn-on-energy.png" alt="Fitted turn-on energy surface against voltage and current" width="1149" height="931" loading="lazy"></a>
  <a href="/images/research/sumitomo-device-modelling/ann-turn-off-energy.png" target="_blank" rel="noopener"><img src="/images/research/sumitomo-device-modelling/ann-turn-off-energy.png" alt="Fitted turn-off energy surface against voltage and current" width="1137" height="923" loading="lazy"></a>
  <figcaption>Fitted turn-on (left) and turn-off (right) energy surfaces against voltage and current.</figcaption>
</figure>

The public implementation extends the gate-resistance dependence with fitted scaling relations; those generated samples extend the data representation and are not independent double-pulse measurements.

<h3 id="loss-model">Loss Calculation</h3>

A Python loss workflow evaluates the fitted functions at the converter operating point. For a buck converter with duty ratio <i>D</i> and switching frequency <i>f</i><sub>sw</sub>:

- **Conduction:** P<sub>cond</sub> = V<sub>DS</sub>(I, T<sub>j</sub>) × I × D.
- **Switching:** P<sub>sw</sub> = [E<sub>on</sub> + E<sub>off</sub>] × f<sub>sw</sub>.

<h3 id="thermal-modelling">Thermal Response</h3>

An ANN branch fits the transient thermal impedance of the manufacturer's Cauer model, giving a response function from dissipated power to temperature rise.

<figure>
  <a href="/images/research/sumitomo-device-modelling/ann-thermal-impedance-fit.png" target="_blank" rel="noopener"><img src="/images/research/sumitomo-device-modelling/ann-thermal-impedance-fit.png" alt="Reference thermal impedance and ANN fit on linear and logarithmic time axes" width="1920" height="980" loading="lazy"></a>
  <figcaption>Reference thermal impedance and its ANN fit on linear and logarithmic time axes.</figcaption>
</figure>

I also measured the device's thermal path directly, calibrating its temperature-sensitive electrical parameter at 10 mA and comparing dry and wet interfaces. Structure-function analysis gives a four-section Cauer network with **R<sub>th,jc</sub> ≈ 0.762 K/W**. The measured response differs from the manufacturer model across the transient, so the chosen thermal representation affects the estimated junction temperature. [Thermal characterization](/research/thermal-characterization/) describes this measurement.

<h2 id="experimental-validation">Buck-Converter Assessment</h2>

I tested the model against a buck converter operating at about **400 V input, 200 V output and up to 3 kW**, with 20 kHz switching, D = 0.5 and 2.5 Ω turn-on and turn-off gate resistances. Heatsink and ambient temperatures give a thermally inferred loss, P = (T<sub>hs</sub> − T<sub>amb</sub>) / R<sub>th,hs</sub>, and the estimated junction temperature sets the ANN operating point.

<figure>
  <a class="device-experiment-rotation" href="/images/research/sumitomo-device-modelling/buck-thermal-test.jpeg" target="_blank" rel="noopener"><img src="/images/research/sumitomo-device-modelling/buck-thermal-test.jpeg" alt="Heatsink-mounted SiC buck-converter module and temperature-measurement equipment" width="3301" height="2474" loading="lazy"></a>
  <figcaption>Heatsink-mounted SiC buck-converter module with temperature measurement.</figcaption>
</figure>

Over the load-current sweep, the ANN-predicted losses and the thermally inferred losses follow a similar trend, with about **10% variation against a 20% target**. The loss breakdown includes MOSFET conduction and switching and excludes body-diode loss.

<figure>
  <a href="/images/research/sumitomo-device-modelling/measured-vs-ann-loss.png" target="_blank" rel="noopener"><img src="/images/research/sumitomo-device-modelling/measured-vs-ann-loss.png" alt="Thermally inferred and ANN-predicted total loss over the load-current sweep" width="947" height="593" loading="lazy"></a>
  <figcaption>Thermally inferred and ANN-predicted total loss over the load-current sweep.</figcaption>
</figure>

The model applies within the ranges of its reference data and characterised gate-drive conditions. The networks are unconstrained, so they do not enforce zero-current behaviour or monotonicity outside those ranges. The [public training implementation](https://github.com/FulongLi/AIPE-MOSFET-ANN-Modelling/blob/720575683673259a6ddcd29a6c69771e43b6d17a/C2MSeries_ANN_full_model.py) is a reference implementation; its input tables should be reviewed before it is used as a validated C2M0080120D model.

[Semiconductor Device Modelling](/research/mosfet_ann_modelling/) · [Electrical Characterization](/research/electrical-characterization/) · [Converter Design Optimisation](/research/converter_optimization/) · [Back to Research](/research/)
