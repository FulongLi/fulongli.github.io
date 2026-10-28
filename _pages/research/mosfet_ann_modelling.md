---
layout: single
title: "Semiconductor Device Modelling"
permalink: /research/mosfet_ann_modelling/
author_profile: true
excerpt: "Semiconductor modelling for power conversion, with a SiC static ANN model for conduction, switching energy and thermal response."
---

Semiconductor models connect device characteristics to converter loss and temperature calculations. My work in this area builds models from measured and reference data that can be evaluated at any electrical operating point, so that loss and temperature can be predicted early in converter design.

<h2 id="static-ann-modelling">SiC Power Devices — Static ANN Modelling</h2>
<span id="device-loss-models"></span>
<span id="thermal-modelling"></span>
<span id="experimental-validation"></span>

Neural networks fit the conduction voltage, turn-on and turn-off energy and thermal impedance of the C2M0080120D SiC MOSFET, treating the MOSFET channel and body diode separately. I led the modelling and its assessment against a buck converter at about 400 V / 200 V and up to 3 kW, where predicted and thermally inferred losses showed about 10% variation against a 20% target.

[Read the static ANN modelling study](/research/semiconductor-device-modelling/static-ann/)

<h2 id="scope">Related Measurements</h2>
<span id="outcomes"></span>

The models map operating conditions to characteristic values and event energies; switching-transient waveform modelling is outside their scope. [Electrical characterisation](/research/electrical-characterization/) supplies switching-energy data, and [thermal characterisation](/research/thermal-characterization/) identifies the heat path needed for temperature estimation.

[Converter Design Optimisation](/research/converter_optimization/) · [AIPE](/research/aipe/) · [Back to Research](/research/)
