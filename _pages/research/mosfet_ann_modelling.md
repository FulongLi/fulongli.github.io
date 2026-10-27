---
layout: research
research_area: components
title: "ANN-Based SiC MOSFET Loss and Thermal Modelling"
permalink: /research/mosfet_ann_modelling/
excerpt: "Technical lead for an ANN-based SiC MOSFET loss and thermal modelling project with Cardiff University and Sumitomo Heavy Industries, plus a public, reproducible model of static device characteristics."
---

<nav class="project-contents" aria-label="Project contents">
  <p><strong>On this page</strong></p>
  <ul>
    <li><a href="#problem">Engineering problem</a></li>
    <li><a href="#contribution">My contribution</a></li>
    <li><a href="#method">Method</a></li>
    <li><a href="#evidence">Results and evidence</a></li>
    <li><a href="#public-model">Public model and results</a></li>
    <li><a href="#limitations">Limitations</a></li>
    <li><a href="#project-resources">References</a></li>
  </ul>
</nav>

<h2 id="problem">Engineering problem</h2>

Converter design needs device losses at operating points the datasheet does not tabulate: conduction voltage as a function of current and junction temperature, and switching energy as a function of voltage, current and gate resistance. Interpolating between a handful of datasheet curves becomes unreliable as the number of variables grows. A compact, differentiable model that reproduces measured characteristics across the operating range can sit directly inside loss calculations and design optimisation.

The project asked a practical question: **can neural-network device models predict the losses observed in a working converter well enough to support design decisions?**

<h2 id="contribution">My contribution</h2>

I was technical lead of the joint development between CSA Catapult, Cardiff University and Sumitomo Heavy Industries (2024–2025). I coordinated dataset creation, feature extraction and the model-training pipelines; set up the converter test platform; and led the comparison between model predictions and converter measurements. I authored the project's work-package reports.

<h2 id="method">Method</h2>

The work was organised in three stages:

| Stage | Engineering work |
|---|---|
| Platform | A laboratory SiC half-bridge buck converter under rapid-control-prototyping control, with documented sensing and code generation from MATLAB/Simulink |
| Device models | Separate neural networks for MOSFET-channel and body-diode conduction, turn-on and turn-off energy, and transient thermal impedance; device thermal measurements by the method on the [thermal characterisation](/research/thermal-characterization/) page |
| Converter comparison | Load sweep of the buck converter at fixed voltage, frequency, duty ratio and gate resistance, comparing predicted losses with losses inferred from measured temperatures |

For an operating point, the models give the principal loss terms

<p class="equation"><em>P</em><sub>cond</sub> = <em>V</em><sub>DS</sub>(<em>I</em>, <em>T</em><sub>j</sub>) · <em>I</em> · <em>D</em>, &nbsp;&nbsp; <em>P</em><sub>sw</sub> = [<em>E</em><sub>on</sub>(<em>V</em>, <em>I</em>, <em>R</em><sub>g</sub>) + <em>E</em><sub>off</sub>(<em>V</em>, <em>I</em>, <em>R</em><sub>g</sub>)] · <em>f</em><sub>sw</sub></p>

and the thermal-impedance model links that power to junction temperature. In the converter test, loss was inferred thermally: heatsink-to-ambient temperature rise divided by the heatsink thermal resistance. This is an indirect estimate whose accuracy depends on the thermal resistances and the assumption that all device loss flows through the measured path; it is not a direct measurement of switching energy.

<h2 id="evidence">Results and evidence</h2>

- **Device models:** neural-network representations of conduction, switching energy and thermal impedance, together with a measured junction-to-case thermal network for the test device.
- **Converter comparison:** predicted and thermally inferred losses followed the same trend across the load sweep. The project reports state the agreement quantitatively; because those reports are internal, the figures are not reproduced here.

The publicly checkable part of this work is the open model described next.

<h2 id="public-model">Public model and reproducible results</h2>

The related public **Python/PyTorch** repository provides an inspectable implementation for the Wolfspeed C2M0080120D, trained on reference tables included in the repository. It predicts **drain–source voltage from current and temperature**, with separate MOSFET-channel and body-diode networks. These results were regenerated independently of the industrial project and have their own scope.

Rotate and zoom the surface, or switch between conduction modes. Grey points are training references and orange points were held out for testing. The surface interpolates between the available temperature curves.

<iframe class="device-ann-interactive" src="/files/research/mosfet-ann/interactive.html" title="Interactive 3D MOSFET and body-diode ANN characteristics" width="100%" height="640" loading="lazy" allowfullscreen></iframe>

[Open the interactive plot in a full window](/files/research/mosfet-ann/interactive.html)

The full training workflow was rerun on **26 October 2026**. Static conduction was evaluated on **21 MOSFET** and **8 body-diode** reference-table points excluded from training.

<div class="project-table-scroll" role="region" aria-label="Held-out validation of the public model" tabindex="0" markdown="1">

| Model | Held-out points | MAE (V) | RMSE (V) |
|---|---:|---:|---:|
| MOSFET channel | 21 | 0.094 | 0.293 |
| Body diode | 8 | 0.096 | 0.136 |

</div>

<figure>
  <a href="/files/research/mosfet-ann/held-out-validation.png" target="_blank" rel="noopener"><img src="/files/research/mosfet-ann/held-out-validation.png" alt="ANN voltage predictions against held-out reference voltages for the MOSFET and body diode, with a dashed ideal-agreement line" loading="lazy"></a>
  <figcaption><span class="figure-kind">Computed result</span><strong>Held-out check of the public static-characteristic model.</strong> Predictions against reference-table voltages excluded from training. This tests interpolation of the repository's reference tables, not agreement with converter measurements. <span class="figure-source">Generated with reproduce.py from the public repository.</span></figcaption>
</figure>

<details>
  <summary>Public-code scope and reproducibility</summary>
  <p>The workflow uses standardised current and temperature inputs, with separate MOSFET and diode networks containing two 32-neuron hidden layers and ReLU activations. The five-output training workflow was rerun with seed 42, 2,000 epochs and Adam (learning rate 0.01). The current training-script architecture was used throughout; the older test script and web app specify different network widths.</p>
  <p>The public switching branch uses gate-resistance-scaled data, including a 900 °C table entry whose physical meaning is unconfirmed, and its random-row test is not independent experimental validation. The thermal source file is named C2M0040120D rather than C2M0080120D and uses all points for training, so it is not presented as validated thermal behaviour for this device.</p>
  <p><a href="/files/research/mosfet-ann/test-predictions.csv">Held-out predictions (CSV)</a> · <a href="/files/research/mosfet-ann/run-metadata.json">Run settings and metrics</a> · <a href="/files/research/mosfet-ann/reproduce.py">Reproduction script</a></p>
</details>

<h2 id="limitations">Limitations</h2>

- The converter comparison covers one SiC device, one buck-converter configuration and fixed gate-drive conditions. Other gate resistances, cooling arrangements or topologies need their own device data and check.
- The simplified loss breakdown covers MOSFET conduction and switching and excludes body-diode loss.
- The static networks in the public model do not enforce physical constraints such as zero voltage at zero current or monotonicity, so they should be used within the reference-data ranges.

<h2 id="project-resources">References</h2>

- [AIPE-MOSFET-ANN-Modelling (GitHub)](https://github.com/FulongLi/AIPE-MOSFET-ANN-Modelling): public model, training scripts and web interface.
- Related pages: [Thermal characterisation](/research/thermal-characterization/) · [Electrical characterisation](/research/electrical-characterization/) · [Converter design optimisation](/research/converter_optimization/)
