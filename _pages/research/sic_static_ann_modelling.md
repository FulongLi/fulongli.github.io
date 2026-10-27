---
layout: single
title: "SiC Power Devices — Static ANN Modelling"
permalink: /research/semiconductor-device-modelling/static-ann/
author_profile: true
body_class: device-project-page
project_stylesheet: /assets/css/marine-project.css
project_contents: true
excerpt: "Static neural-network fitting of SiC conduction and switching-energy characteristics, thermal response and converter-level loss assessment."
---

<h2 id="overview">Static Characteristic Fitting</h2>

This work builds a data-based model of the **C2M0080120D SiC MOSFET** for converter loss and temperature calculations. I led the modelling and experimental assessment, connecting device-characteristic fitting to a buck-converter load sweep.

The ANN learns a mapping between operating conditions and a device quantity: current and temperature determine conduction voltage, while switching conditions determine energy per event. The approach represents the characteristic surfaces needed by a loss model; it does not resolve the electrical waveform during a switching transition.

<h2 id="data-and-model-functions">Data and Model Functions</h2>

The workflow starts with datasheet or semiconductor-model tables, complemented by electrical and thermal characterisation where needed. Conduction data are organised as current–temperature–voltage samples. Switching tables supply event energy at specified voltage, current and temperature. The body diode is treated separately from the MOSFET channel.

The accompanying public training implementation uses fully connected feedforward networks. Its layer structure is:

<div class="project-table-scroll" role="region" aria-label="Static ANN branches and layer structures" tabindex="0" markdown="1">

| Model branch | Inputs | Hidden layers | Output |
|---|---|---|---|
| MOSFET conduction | I<sub>DS</sub>, T<sub>j</sub> | 32 → 32, ReLU | V<sub>DS</sub> |
| Body-diode conduction | I<sub>D</sub>, T<sub>j</sub> | Separate 32 → 32, ReLU | V<sub>F</sub> |
| Turn-on / turn-off energy | I, V, T<sub>j</sub>, R<sub>g,on</sub>, R<sub>g,off</sub> | Shared 32 → 32, ReLU | Separate E<sub>on</sub> and E<sub>off</sub> linear heads |
| Thermal response | Time | Separate 64 → 64, ReLU | Z<sub>th</sub>(t) |

</div>

Each hidden neuron applies a learned weighted sum and bias followed by a ReLU activation; the output layer is linear. Separate conduction networks allow channel and diode characteristics to be fitted independently. The switching branches share their hidden representation and have separate scalar outputs for the two event energies. These widths describe the public training code; the report illustrates the fitted device functions and identifies a two-layer ANN thermal fit.

<h2 id="network-training">Scaling and Network Training</h2>

Electrical inputs are standardised using the training-set mean and standard deviation. The same scaler is retained for prediction. The implementation holds out **20% of electrical samples**, using **seed 42**, and minimises the sum of the five branch mean-square errors with **Adam**, a **0.01 learning rate** and **2,000 epochs**. The thermal branch uses its time/impedance samples without this electrical-input scaling.

The fitting sequence is to organise the reference tables, train the relevant function and compare its predictions with the reference characteristic. The weights and input scalers are saved together for subsequent operating-point queries. The electrical hold-out split checks interpolation of those tables; the converter experiment provides a separate assessment of loss prediction.

<figure>
  <a href="/images/research/sumitomo-device-modelling/ann-conduction-characteristic.png" target="_blank" rel="noopener"><img src="/images/research/sumitomo-device-modelling/ann-conduction-characteristic.png" alt="ANN conduction-voltage surface versus current and temperature with reference samples" width="1490" height="850" loading="lazy"></a>
  <figcaption><strong>Conduction characteristic.</strong> The fitted surface supplies the voltage drop at a selected current and junction temperature. <span class="figure-source">Device loss and thermal modelling report, slide 7.</span></figcaption>
</figure>

<h2 id="loss-model">Loss Calculation and PLECS-Type Use</h2>

PLECS thermal descriptions use conduction characteristics and switching-energy data to calculate dissipation while retaining ideal electrical switching. The ANN functions represent the same kinds of characteristic data for a converter-level loss calculation. The fitted functions are evaluated in a Python loss workflow, with PLECS providing a reference for how the characteristic data are organised. [PLECS thermal modelling reference](https://www.plexim.com/products/plecs/thermal).

For a simplified buck operating point, the model evaluates:

- **Conduction:** P<sub>cond</sub> = V<sub>DS</sub>(I, T<sub>j</sub>) × I × D.
- **Switching:** P<sub>sw</sub> = [E<sub>on</sub> + E<sub>off</sub>] × f<sub>sw</sub>, with energy converted to joules.

<figure class="half">
  <a href="/images/research/sumitomo-device-modelling/ann-turn-on-energy.png" target="_blank" rel="noopener"><img src="/images/research/sumitomo-device-modelling/ann-turn-on-energy.png" alt="Fitted turn-on energy surface against voltage and current" width="1149" height="931" loading="lazy"></a>
  <a href="/images/research/sumitomo-device-modelling/ann-turn-off-energy.png" target="_blank" rel="noopener"><img src="/images/research/sumitomo-device-modelling/ann-turn-off-energy.png" alt="Fitted turn-off energy surface against voltage and current" width="1137" height="923" loading="lazy"></a>
  <figcaption><strong>Switching energy as an operating-point function.</strong> These fits return energy per event, rather than switching-time waveforms. <span class="figure-source">Device loss and thermal modelling report, slide 7.</span></figcaption>
</figure>

The public implementation expands gate-resistance dependence using fitted scaling relations. Those generated samples extend the fitted data representation; they are not independent DPT measurements. The experimental loss breakdown below includes MOSFET conduction and switching and excludes body-diode loss.

<h2 id="thermal-modelling">Thermal Response and Measurement</h2>

The report fits the transient thermal-impedance response of a manufacturer Cauer RC model with an ANN. This supplies a response function linking dissipated power to temperature rise.

<figure>
  <a href="/images/research/sumitomo-device-modelling/ann-thermal-impedance-fit.png" target="_blank" rel="noopener"><img src="/images/research/sumitomo-device-modelling/ann-thermal-impedance-fit.png" alt="Reference thermal impedance and ANN fit on linear and logarithmic time axes" width="1920" height="980" loading="lazy"></a>
  <figcaption><strong>Thermal-response fitting.</strong> Linear and logarithmic views compare the reference response with the ANN representation. <span class="figure-source">Device loss and thermal modelling report, slides 8–9.</span></figcaption>
</figure>

Separate C2M0080120D measurements use **10 mA TSEP calibration**, heating/cooling transients and dry/wet interface comparison. Structure-function analysis gives a four-section Cauer network with total **R<sub>th,jc</sub> ≈ 0.762 K/W**. The measured transient differs from the manufacturer-model response, so the selected thermal representation affects temperature estimation.

<figure>
  <a href="/images/research/sumitomo-device-modelling/thermal-impedance-comparison.png" target="_blank" rel="noopener"><img src="/images/research/sumitomo-device-modelling/thermal-impedance-comparison.png" alt="Measured and manufacturer-model thermal-impedance curves for comparison" width="1003" height="813" loading="lazy"></a>
  <figcaption><strong>Thermal-model comparison.</strong> The measured and PLECS-model responses differ across the transient. <span class="figure-source">Device loss and thermal modelling report, slide 15.</span></figcaption>
</figure>

<h2 id="experimental-validation">Buck-Converter Assessment</h2>

The test operates at approximately **400 V input, 200 V output and up to 3 kW**, with **20 kHz switching**, **D = 0.5** and **2.5 Ω turn-on/off gate resistances**. Heatsink and ambient temperature measurements give a thermal loss estimate, P = (T<sub>hs</sub> − T<sub>amb</sub>) / R<sub>th,hs</sub>. The estimated junction temperature then supplies the ANN operating point.

<figure>
  <a class="device-experiment-rotation" href="/images/research/sumitomo-device-modelling/buck-thermal-test.jpeg" target="_blank" rel="noopener"><img src="/images/research/sumitomo-device-modelling/buck-thermal-test.jpeg" alt="Heatsink-mounted SiC buck-converter module and temperature-measurement equipment" width="3301" height="2474" loading="lazy"></a>
  <figcaption><strong>The experimental check.</strong> A heatsink-mounted power module provides the temperature-rise comparison. <span class="figure-source">Modelling/experiment comparison, slide 4.</span></figcaption>
</figure>

<figure>
  <a href="/images/research/sumitomo-device-modelling/measured-vs-ann-loss.png" target="_blank" rel="noopener"><img src="/images/research/sumitomo-device-modelling/measured-vs-ann-loss.png" alt="Thermally inferred and ANN-predicted total loss over the load-current sweep" width="947" height="593" loading="lazy"></a>
  <figcaption><strong>Loss comparison over the load sweep.</strong> The predictions and thermally inferred losses follow a similar trend. <span class="figure-source">Modelling/experiment comparison, slide 7.</span></figcaption>
</figure>

The report states **about 10% variation against a 20% target**. Its percentage metric is not defined as a maximum pointwise error. The comparison tests the combined loss and thermal assumptions under these operating conditions.

<h2 id="scope-and-sources">Scope and Sources</h2>

The model is intended for the reference-data ranges and characterised gate-drive conditions. The unconstrained networks do not impose zero-current behaviour or monotonicity. In the public repository, the thermal training file is labelled C2M0040120D and a switching table contains an unconfirmed 900°C entry; those inputs require review before using that code as a validated C2M0080120D device model.

[Public training implementation](https://github.com/FulongLi/AIPE-MOSFET-ANN-Modelling/blob/720575683673259a6ddcd29a6c69771e43b6d17a/C2MSeries_ANN_full_model.py) · [Figure sources](/files/research/sumitomo-device-modelling/figure-sources.json)

[Semiconductor Device Modelling](/research/mosfet_ann_modelling/) · [Electrical Characterization](/research/electrical-characterization/) · [Converter Design Optimisation](/research/converter_optimization/) · [Back to Research](/research/)
