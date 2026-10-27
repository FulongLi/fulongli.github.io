---
layout: single
title: "Semiconductor Device Modelling"
permalink: /research/mosfet_ann_modelling/
author_profile: true
body_class: device-project-page
project_stylesheet: /assets/css/marine-project.css
project_script: /assets/js/marine-project.js
excerpt: "Technical leadership of the Sumitomo Heavy Industries collaboration: ANN-based SiC MOSFET loss and thermal models, compared with buck-converter experiments up to 3 kW."
---

<h2 id="overview">ANN-Based SiC MOSFET Modelling</h2>

I led this project as **Technical Lead at Compound Semiconductor Applications (CSA) Catapult**, working with **Cardiff University** and **Sumitomo Heavy Industries, Japan**. The aim was to predict SiC MOSFET losses and temperature rise well enough to support converter design, using artificial neural networks (ANNs) to represent device behaviour across operating conditions.

The engineering question was straightforward: **can device-characteristic models predict the losses observed in a working converter?** We connected conduction and switching-energy models to thermal behaviour, then compared the predictions with a laboratory buck converter operating at approximately **400 V input, 200 V output and up to 3 kW**.

**My role:** Technical lead for the project, connecting the experimental platform, device-modelling workflow and model-to-experiment assessment across the three work packages. I authored the WP1 setup report, WP2 loss and thermal modelling summary, and WP3 experimental comparison.

**Principal results:** WP2 produced ANN representations of conduction, switching energy and transient thermal impedance, alongside a measured junction-to-case thermal resistance of approximately **0.762 K/W** for the C2M0080120D. WP3 compared predicted and thermally inferred power loss over a load sweep. Its summary reports **about 10% variation against a 20% target** for the comparison; the test conditions and limits are explained below.

<figure>
  <a href="/images/research/sumitomo-device-modelling/buck-thermal-test.jpeg" target="_blank" rel="noopener" aria-label="View original: Buck-converter thermal experiment"><img src="/images/research/sumitomo-device-modelling/buck-thermal-test.jpeg" alt="Laboratory buck-converter power module with a clamped heatsink and temperature-measurement equipment" width="3301" height="2474" fetchpriority="high"></a>
  <figcaption><strong>The experimental check.</strong> The heatsink-mounted power module used to compare the ANN loss predictions with losses inferred from temperature rise. <span class="figure-source">WP3, slide 4.</span></figcaption>
</figure>

<nav class="project-contents" aria-label="Project contents">
  <p><strong>On this page</strong></p>
  <ul>
    <li><a href="#overview">Project overview</a></li>
    <li><a href="#work-packages">Work packages</a></li>
    <li><a href="#experimental-platform">WP1: experimental platform</a></li>
    <li><a href="#device-loss-models">WP2: device loss models</a></li>
    <li><a href="#thermal-modelling">WP2: thermal modelling</a></li>
    <li><a href="#experimental-validation">WP3: experimental comparison</a></li>
    <li><a href="#outcomes">Outcomes and scope</a></li>
    <li><a href="#public-model">Public model and interactive results</a></li>
    <li><a href="#project-resources">Project resources</a></li>
  </ul>
</nav>

<h2 id="work-packages">The project workflow</h2>

The work linked device data to converter operation. WP1 established the test platform. WP2 supplied the electrical and thermal models. WP3 brought them together under a common set of operating conditions so that predicted losses could be checked against experimental evidence.

<div class="project-table-scroll" role="region" aria-label="Work-package summary" tabindex="0" markdown="1">

| Work package | Engineering work | Result |
|---|---|---|
| WP1: platform setup | Configure the Imperix B-Box RCP controller, MATLAB/Simulink model, SiC half-bridge and measurement channels | A documented buck-converter platform for the subsequent experiments |
| WP2: loss and thermal modelling | Fit conduction characteristics, turn-on/off energy and thermal impedance; characterise the device's thermal response | Device models for calculating losses and linking them to junction temperature |
| WP3: experimental comparison | Run the buck converter across a load sweep and compare ANN predictions with thermally inferred losses | A converter-level comparison under defined voltage, frequency, duty-cycle and gate-resistance conditions |

</div>

The source reports span **December 2024 to June 2025**. The project fits into the wider [converter design optimisation](/research/converter_optimization/) workflow: device losses and thermal limits become inputs to design decisions. The results here concern the device models and their experimental assessment.

<h2 id="experimental-platform">WP1: establishing the experimental platform</h2>

The platform used an **Imperix B-Box RCP** and a **PEB8038 SiC half-bridge**, with a **2.5 mH inductor** and **3 mF output capacitor**. WP1 documented the control and hardware configuration, sensor scaling, PWM assignment and MATLAB/Simulink code-generation workflow. Its test envelope was **500 W–3 kW**, with approximately **400 V input and 200 V output**.

<figure>
  <a href="/images/research/sumitomo-device-modelling/buck-test-platform.png" target="_blank" rel="noopener" aria-label="View original: Imperix buck-converter platform"><img src="/images/research/sumitomo-device-modelling/buck-test-platform.png" alt="Buck-converter schematic showing the B-Box RCP controller, complementary PWM, SiC half-bridge, inductor, output capacitor and voltage/current feedback" width="1551" height="739" loading="lazy"></a>
  <figcaption><strong>Buck-converter test platform.</strong> The controller and measurement paths connect the physical converter with its Simulink representation. WP1 also shows an operating reference at approximately 1.3 kW. <span class="figure-source">WP1, slides 3 and 15.</span></figcaption>
</figure>

<h2 id="device-loss-models">WP2: device characteristics and loss prediction</h2>

WP2 developed a modelling workflow around the **Wolfspeed C2M0080120D SiC MOSFET**. Conduction loss depends on the voltage drop at the operating current and junction temperature. Switching loss depends on turn-on and turn-off energy at the relevant electrical and gate-drive conditions. The ANN models represent these dependencies continuously between the available reference points.

The workflow treated MOSFET-channel conduction and body-diode conduction separately, then added switching-energy and thermal-impedance models. It organised the resulting models for reuse by higher-level converter calculations.

<figure>
  <a href="/images/research/sumitomo-device-modelling/ann-conduction-characteristic.png" target="_blank" rel="noopener" aria-label="View original: ANN conduction characteristic"><img src="/images/research/sumitomo-device-modelling/ann-conduction-characteristic.png" alt="ANN surface and reference points for MOSFET drain-source voltage versus current and temperature, with the original temperature colour scale" width="1490" height="850" loading="lazy"></a>
  <figcaption><strong>Temperature-dependent conduction characteristic.</strong> The network predicts the drain–source voltage drop from current and temperature. The surface and reference points retain the original report's colour scale. <span class="figure-source">WP2, slide 7.</span></figcaption>
</figure>

<figure class="half">
  <a href="/images/research/sumitomo-device-modelling/ann-turn-on-energy.png" target="_blank" rel="noopener" aria-label="View original: ANN turn-on energy"><img src="/images/research/sumitomo-device-modelling/ann-turn-on-energy.png" alt="ANN turn-on energy surface versus drain-source voltage and current, with reference points and energy in microjoules" width="1149" height="931" loading="lazy"></a>
  <a href="/images/research/sumitomo-device-modelling/ann-turn-off-energy.png" target="_blank" rel="noopener" aria-label="View original: ANN turn-off energy"><img src="/images/research/sumitomo-device-modelling/ann-turn-off-energy.png" alt="ANN turn-off energy surface versus drain-source voltage and current, with reference points and energy in microjoules" width="1137" height="923" loading="lazy"></a>
  <figcaption><strong>Turn-on and turn-off energy models.</strong> These surfaces provide energy per switching event. Multiplying their sum by switching frequency gives the switching-power contribution. <span class="figure-source">WP2, slide 7.</span></figcaption>
</figure>

For the simplified operating-point calculation used in the reports, the principal terms are:

- **Conduction power:** P<sub>cond</sub> = V<sub>DS</sub>(I, T<sub>j</sub>) × I × D.
- **Switching power:** P<sub>sw</sub> = (E<sub>on</sub> + E<sub>off</sub>) × f<sub>sw</sub>, with event energies expressed in joules.

Gate-drive settings matter when applying these models. WP3 fixed the duty ratio at 0.5 and both gate resistances at 2.5 Ω. Its displayed loss breakdowns include MOSFET conduction and switching loss and explicitly exclude body-diode loss.

<h2 id="thermal-modelling">WP2: thermal impedance and device measurements</h2>

Electrical losses must connect to a thermal model to estimate junction temperature. WP2 examined the manufacturer's PLECS Cauer RC representation and fitted its transient thermal-impedance response with an ANN. It also measured the C2M0080120D's thermal response, using a temperature-sensitive electrical parameter to relate the device's electrical response to junction temperature.

<figure>
  <a href="/images/research/sumitomo-device-modelling/ann-thermal-impedance-fit.png" target="_blank" rel="noopener" aria-label="View original: ANN thermal-impedance fit"><img src="/images/research/sumitomo-device-modelling/ann-thermal-impedance-fit.png" alt="Reference thermal impedance and ANN fit shown on both linear and logarithmic time axes" width="1920" height="980" loading="lazy"></a>
  <figcaption><strong>ANN fit to the thermal response.</strong> Linear and logarithmic time views show the original data and the fitted response. This demonstrates fitting of the manufacturer-model response; the separate device measurements below provide an additional comparison. <span class="figure-source">WP2, slides 8–9.</span></figcaption>
</figure>

The measurement sequence included **calibration at 10 mA**, heating and cooling tests under dry and wet interface conditions, and structure-function analysis. The report derived a **four-section Cauer network** with a total junction-to-case thermal resistance of approximately **0.762 K/W**.

<figure class="half">
  <a href="/images/research/sumitomo-device-modelling/measured-thermal-impedance.png" target="_blank" rel="noopener" aria-label="View original: Measured junction-to-case thermal impedance"><img src="/images/research/sumitomo-device-modelling/measured-thermal-impedance.png" alt="Measured transient junction-to-case thermal impedance approaching 0.762 K/W" width="1003" height="813" loading="lazy"></a>
  <a href="/images/research/sumitomo-device-modelling/thermal-impedance-comparison.png" target="_blank" rel="noopener" aria-label="View original: Measured and PLECS thermal impedance"><img src="/images/research/sumitomo-device-modelling/thermal-impedance-comparison.png" alt="Comparison of measured and manufacturer PLECS-model transient thermal impedance on logarithmic axes" width="1003" height="813" loading="lazy"></a>
  <figcaption><strong>Measured thermal response and model comparison.</strong> The measured response approaches 0.762 K/W. The measured and PLECS curves differ over the transient, making the thermal-model choice relevant to temperature prediction. <span class="figure-source">WP2, slides 14–15. Original vector plots rasterised for browser display.</span></figcaption>
</figure>

<h2 id="experimental-validation">WP3: comparing predictions with the working converter</h2>

WP3 tested the connection between the device models and converter operation. The experiment measured heatsink and ambient temperatures together with electrical operating variables. It used heatsink thermal resistance to infer power loss, estimated junction temperature, and supplied the operating point to the ANN loss model.

| Test parameter | Reported condition |
|---|---|
| Converter | Buck converter with heatsink, up to 3 kW |
| Input / output voltage | Approximately 400 V / 200 V |
| Switching frequency | 20 kHz |
| Duty ratio | 0.5 |
| Turn-on / turn-off gate resistance | 2.5 Ω / 2.5 Ω |
| Component assumption | Identical MOSFETs and heatsinks share the same thermal properties |

The comparison followed the thermal calculation **P = (T<sub>hs</sub> − T<sub>amb</sub>) / R<sub>th,hs</sub>**, then **T<sub>j</sub> = T<sub>hs</sub> + P × R<sub>th,MOSFET</sub>**. This makes the experimental loss estimate dependent on the thermal resistances and heat-flow assumptions used in the test. It is an indirect thermal estimate, rather than a direct measurement of switching-event energy.

<figure>
  <a href="/images/research/sumitomo-device-modelling/measured-vs-ann-loss.png" target="_blank" rel="noopener" aria-label="View original: Experimental and ANN loss comparison"><img src="/images/research/sumitomo-device-modelling/measured-vs-ann-loss.png" alt="Original WP3 comparison of thermally inferred power loss and ANN-predicted total power loss across a current sweep" width="947" height="593" loading="lazy"></a>
  <figcaption><strong>Power-loss comparison across the load sweep.</strong> The report's experimentally inferred and ANN-predicted total-loss traces follow a similar trend as current increases. The source labels the experimental trace “Measured power loss”. <span class="figure-source">WP3, slide 7.</span></figcaption>
</figure>

The WP3 summary states **“within 20% variance (10% in actual)”**. This is the report's stated comparison outcome under the conditions above. The supplied deck does not include the underlying experimental data table or a definition of that percentage metric, so it does not establish a maximum error bound at every point, particularly at low losses.

<details>
  <summary>Operating-current definition and per-device loss breakdown</summary>
  <p>WP3 defines MOSFET current using the average inductor current during the conducting half-cycle, aligned with the oscilloscope interpretation. Its waveform example illustrates the distinction between pulsed device current and continuous inductor current.</p>
  <figure>
    <a href="/images/research/sumitomo-device-modelling/mosfet-current-waveforms.png" target="_blank" rel="noopener" aria-label="View original: MOSFET and inductor currents"><img src="/images/research/sumitomo-device-modelling/mosfet-current-waveforms.png" alt="Simulated pulsed currents in the two MOSFETs and the continuous triangular inductor-current waveform" width="875" height="619" loading="lazy"></a>
    <figcaption><strong>Current interpretation used in the model comparison.</strong> <span class="figure-source">WP3, slide 3.</span></figcaption>
  </figure>
  <p>The following values transcribe the six single-device prediction examples from WP3, slide 6. They exclude body-diode loss and are separate from the aggregate total-loss comparison above. The source's displayed rounding is retained.</p>
  <div class="project-table-scroll" role="region" aria-label="Per-device ANN loss predictions" tabindex="0">
    <table>
      <thead><tr><th scope="col">Current (A)</th><th scope="col">Conduction (W)</th><th scope="col">Switching (W)</th><th scope="col">Total (W)</th></tr></thead>
      <tbody>
        <tr><td>0.8</td><td>0.027</td><td>0.643</td><td>0.670</td></tr>
        <tr><td>2.0</td><td>0.170</td><td>0.938</td><td>1.109</td></tr>
        <tr><td>5.5</td><td>1.301</td><td>1.600</td><td>2.901</td></tr>
        <tr><td>7.2</td><td>2.249</td><td>1.924</td><td>4.173</td></tr>
        <tr><td>10.8</td><td>5.629</td><td>2.401</td><td>8.030</td></tr>
        <tr><td>13.4</td><td>9.312</td><td>3.091</td><td>12.403</td></tr>
      </tbody>
    </table>
  </div>
  <p><a href="/files/research/sumitomo-device-modelling/wp3-per-device-predictions.csv">Download the per-device predictions (CSV)</a></p>
</details>

<h2 id="outcomes">Outcomes and engineering scope</h2>

The project established a documented route from device characteristics to converter loss assessment. WP2 supplied electrical and thermal representations, including a measured thermal network. WP3 exercised the models against a working converter, showing how predicted loss changed with operating current and where thermal assumptions entered the comparison.

As Technical Lead, I connected the work-package activities around this engineering question: whether the device models were useful when applied to the converter. The reports bring the model-development results and experimental assessment into a common workflow for subsequent design and optimisation work.

The demonstrated scope is the reported SiC device and buck-converter test conditions. The simplified loss breakdown covers MOSFET conduction and switching. Applying it to other gate-drive settings, cooling arrangements or converter topologies requires suitable device data and a further check against those conditions.

<h2 id="public-model">Public model and interactive results</h2>

The related public **Python/PyTorch** example provides an inspectable implementation and reproducible static-characteristic results. It predicts **drain–source voltage from current and temperature**, with separate MOSFET-channel and body-diode networks. These public-code results were regenerated separately from the 2025 project experiments and have their own evaluation scope.

Rotate and zoom the surface, or switch between conduction modes. Grey points are training references and orange points were held out for testing. The surface interpolates between the available temperature curves.

<iframe class="device-ann-interactive" src="/files/research/mosfet-ann/interactive.html" title="Interactive 3D MOSFET and body-diode ANN characteristics" width="100%" height="640" loading="lazy" allowfullscreen></iframe>

[Open the interactive plot in a full window](/files/research/mosfet-ann/interactive.html)

The full training workflow was rerun on **26 October 2026**. Static conduction was evaluated on **21 MOSFET** and **8 body-diode** reference-table points excluded from training.

| Model | Test points | MAE (V) | RMSE (V) |
|---|---:|---:|---:|
| MOSFET | 21 | 0.094 | 0.293 |
| Body diode | 8 | 0.096 | 0.136 |

<figure>
  <a href="/files/research/mosfet-ann/held-out-validation.png" target="_blank" rel="noopener"><img src="/files/research/mosfet-ann/held-out-validation.png" alt="ANN voltage predictions against held-out reference voltages for the MOSFET and body diode, with a dashed ideal-agreement line" loading="lazy"></a>
  <figcaption><strong>Public-code static-characteristic check.</strong> These results test interpolation of the repository's reference tables. The plots show a freshly retrained model. They are separate from the WP3 converter experiment.</figcaption>
</figure>

<details>
  <summary>Public-code scope and reproducibility</summary>
  <p>The workflow uses standardised current and temperature inputs, with separate MOSFET and diode networks containing two 32-neuron hidden layers and ReLU activations. The full five-output training workflow was rerun with seed 42, 2,000 epochs and Adam (learning rate 0.01). The current training-script architecture was used throughout: the older test script and web app specify different network widths.</p>
  <p>The public switching branch uses gate-resistance-scaled data, including a 900 °C table entry whose physical interpretation is unconfirmed. Its random-row test is not independent experimental validation. The thermal source file is named C2M0040120D rather than C2M0080120D and uses all points for training; it is not presented here as validated thermal behaviour for this device. These limitations apply to the public-code reproduction and should not be confused with the separate WP2 device measurements.</p>
  <p>The static networks do not enforce physical constraints such as zero-current behaviour or monotonicity. Results should be used within the reference-data ranges, with particular care near zero current.</p>
  <p><a href="/files/research/mosfet-ann/test-predictions.csv">Held-out predictions (CSV)</a> · <a href="/files/research/mosfet-ann/run-metadata.json">Run settings and metrics</a> · <a href="/files/research/mosfet-ann/reproduce.py">Reproduction script</a></p>
</details>

<h2 id="project-resources">Project resources and figure sources</h2>

The project figures come from my **WP1 setup report** (9 December 2024), **WP2 loss and thermal modelling summary** (updated 15 April 2025) and **WP3 modelling/experiment comparison** (updated 9 June 2025). Captions identify the work package and slide number. Select a figure to open the original extracted image or the browser-compatible rendering of the source figure.

[Figure sources and slide numbers](/files/research/sumitomo-device-modelling/figure-sources.json) · [WP3 per-device predictions (CSV)](/files/research/sumitomo-device-modelling/wp3-per-device-predictions.csv) · [Related public ANN code](https://github.com/FulongLi/AIPE-MOSFET-ANN-Modelling)

Related work: [Device characterisation](/research/switching_devices/) · [Converter Design Optimisation](/research/converter_optimization/) · [AIPE](/research/aipe/) · [Back to Research](/research/)
