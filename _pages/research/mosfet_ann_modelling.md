---
layout: single
title: "Semiconductor Device Modelling"
permalink: /research/mosfet_ann_modelling/
author_profile: true
body_class: device-project-page
project_stylesheet: /assets/css/marine-project.css
project_contents: true
excerpt: "Semiconductor modelling for power conversion, with a SiC static ANN model for conduction, switching energy and thermal response."
---

<h2 id="overview">Device Models for Converter Simulation</h2>

Semiconductor models connect device characteristics to converter loss and temperature calculations. My work in this area uses measured and reference data to build models that can be evaluated across electrical operating points.

The current case study concerns **SiC power devices and static ANN modelling**: neural networks fit characteristic data, supplying continuous voltage-drop, switching-energy and thermal-response functions for higher-level calculations.

<h2 id="static-ann-modelling">SiC Power Devices — Static ANN Modelling</h2>
<span id="device-loss-models"></span>

The C2M0080120D case separates MOSFET-channel conduction, body-diode conduction, turn-on energy, turn-off energy and thermal impedance. Each function has defined inputs and outputs; together they support a loss-model workflow comparable in purpose to a PLECS thermal description.

The case study explains the neural-network branches, training and scaling, loss calculation, thermal measurements and a buck-converter comparison at approximately 400 V / 200 V and up to 3 kW.

[Read the static ANN modelling study](/research/semiconductor-device-modelling/static-ann/)

<h2 id="scope">Model Scope and Related Measurements</h2>
<span id="thermal-modelling"></span>
<span id="experimental-validation"></span>
<span id="outcomes"></span>

The current models map operating conditions to characteristic values or event energies. Electrical switching-transient modelling remains outside this case study. [Electrical characterisation](/research/electrical-characterization/) supplies static and switching data, while [thermal characterisation](/research/thermal-characterization/) identifies the heat path needed for temperature estimation.

[Converter Design Optimisation](/research/converter_optimization/) · [AIPE](https://aipel.co.uk/) · [Back to Research](/research/)
