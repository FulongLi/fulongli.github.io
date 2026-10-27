---
layout: single
title: "Semiconductor Device Modelling"
permalink: /research/mosfet_ann_modelling/
author_profile: true
body_class: device-project-page
project_stylesheet: /assets/css/marine-project.css
excerpt: "ANN-based SiC MOSFET loss and thermal modelling, assessed against buck-converter experiments up to 3 kW."
---

<h2 id="overview">From Device Characteristics to Converter Losses</h2>

Can a model built from SiC MOSFET characteristics predict the losses of a working converter? I led this collaboration at **CSA Catapult** with **Cardiff University** and **Sumitomo Heavy Industries, Japan**, connecting artificial neural network (ANN) device models with a laboratory buck-converter experiment.

The aim was to make conduction, switching and thermal behaviour usable in converter design. As technical lead, I brought the experimental platform, model development and converter-level comparison into a common assessment.

<figure>
  <a class="device-experiment-rotation" href="/images/research/sumitomo-device-modelling/buck-thermal-test.jpeg" target="_blank" rel="noopener"><img src="/images/research/sumitomo-device-modelling/buck-thermal-test.jpeg" alt="Heatsink-mounted buck-converter power module and temperature measurement equipment, shown rotated clockwise by 90 degrees" width="3301" height="2474" fetchpriority="high"></a>
  <figcaption><strong>The experimental check.</strong> A heatsink-mounted SiC power module connects device loss predictions to temperature-rise measurements. <span class="figure-source">WP3, slide 4.</span></figcaption>
</figure>

<h2 id="device-loss-models">An Electrical and Thermal Model</h2>

For the **Wolfspeed C2M0080120D**, ANN models represent conduction voltage as a function of current and temperature, switching energy across electrical operating points, and the transient thermal response. These models link the device operating point to power loss and junction-temperature rise.

<figure>
  <a href="/images/research/sumitomo-device-modelling/ann-conduction-characteristic.png" target="_blank" rel="noopener"><img src="/images/research/sumitomo-device-modelling/ann-conduction-characteristic.png" alt="ANN drain-source voltage surface versus current and temperature with reference points" width="1490" height="850" loading="lazy"></a>
  <figcaption><strong>Learning the device characteristic.</strong> The ANN represents the temperature-dependent voltage drop used in conduction-loss calculations. <span class="figure-source">WP2, slide 7.</span></figcaption>
</figure>

<span id="thermal-modelling"></span>
Device measurements complemented the fitted characteristics. Thermal-response testing produced a four-section Cauer network with a junction-to-case resistance of approximately **0.762 K/W**. This connects electrical loss estimates to the heat path through the device.

<h2 id="experimental-validation">Comparison with a Working Converter</h2>

The buck-converter study operated at approximately **400 V input, 200 V output and up to 3 kW**, with **20 kHz switching** and **2.5 Ω gate resistances**. Losses inferred from heatsink temperature rise were compared with ANN predictions over a load sweep.

<figure>
  <a href="/images/research/sumitomo-device-modelling/measured-vs-ann-loss.png" target="_blank" rel="noopener"><img src="/images/research/sumitomo-device-modelling/measured-vs-ann-loss.png" alt="Thermally inferred and ANN-predicted total power loss across the experimental current sweep" width="947" height="593" loading="lazy"></a>
  <figcaption><strong>Predicted and experimental loss trends.</strong> The two traces follow a similar trend as load current increases. <span class="figure-source">WP3, slide 7.</span></figcaption>
</figure>

The project summary reports **about 10% variation against a 20% target**. This is the report's stated outcome for the tested conditions; the percentage metric is not defined as a maximum error at every point. Experimental losses were inferred thermally, and the displayed MOSFET predictions cover conduction and switching loss.

<h2 id="outcomes">What This Enables</h2>

The study connects device-level modelling to converter-level evidence, providing a basis for loss estimation, thermal assessment and [converter design optimisation](/research/converter_optimization/). Further applications require device data and experimental checks suited to their gate drive, cooling and operating conditions.

Figures: my 2024–2025 project reports. [Figure sources](/files/research/sumitomo-device-modelling/figure-sources.json) · [Public ANN code](https://github.com/FulongLi/AIPE-MOSFET-ANN-Modelling)

[Device Characterization](/research/switching_devices/) · [AIPE](/research/aipe/) · [Back to Research](/research/)
