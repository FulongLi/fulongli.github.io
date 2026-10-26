---
layout: single
title: "MOSFET ANN Modelling"
permalink: /research/mosfet_ann_modelling/
author_profile: true
excerpt: "Temperature-dependent MOSFET characteristics modelled with neural networks, with interactive 3D results."
---

## Overview

This project grew out of my collaboration with **Cardiff University** and **Sumitomo Heavy Industries, Japan**. It uses artificial neural networks to turn tabulated device characteristics into continuous models for power-electronics design.

The static model predicts **drain–source voltage from current and temperature**, capturing both MOSFET-channel and body-diode conduction. The public example uses **C2M0080120D** data and a Python/PyTorch workflow; the broader framework also includes switching-energy and thermal-impedance models.

## How It Works

- **Learn device behaviour:** standardise current and temperature, then fit separate MOSFET and diode networks with two 32-neuron hidden layers and ReLU activations.
- **Check the predictions:** reserve 20% of the reference-table points for testing, using a fixed random seed.
- **Support loss estimation:** use predicted voltage drops with current and duty cycle to estimate conduction loss across operating conditions.

## Explore the ANN Results

Rotate and zoom the surface, or switch between the two conduction modes. Grey points are training references; orange points were held out for testing. The surface interpolates between the available temperature curves.

<iframe src="/files/research/mosfet-ann/interactive.html" title="Interactive 3D MOSFET and body-diode ANN characteristics" width="100%" height="640" loading="lazy" style="border: 1px solid #dce3e8; border-radius: 6px;" allowfullscreen></iframe>

[Open the interactive plot in a full window](/files/research/mosfet-ann/interactive.html)

## Test Results

The full training workflow was rerun on **26 October 2026**. Static conduction was evaluated on **21 MOSFET** and **8 body-diode** points excluded from training.

| Model | Test points | MAE (V) | RMSE (V) |
|---|---:|---:|---:|
| MOSFET | 21 | 0.094 | 0.293 |
| Body diode | 8 | 0.096 | 0.136 |

![ANN predictions against held-out reference voltages for the MOSFET and body diode; the dashed line represents ideal agreement.](/files/research/mosfet-ann/held-out-validation.png)

*These results test interpolation of the repository's reference tables, rather than a new measurement campaign. The plots show a freshly retrained model, not the repository's saved checkpoint.*

<details>
  <summary>Scope and reproducibility</summary>
  <p>The full five-output training workflow was rerun with seed 42, 2,000 epochs and Adam (learning rate 0.01). The current training-script architecture was used throughout: the older test script and web app specify different network widths.</p>
  <p>The switching branch uses gate-resistance-scaled data, including a 900 °C table entry whose physical interpretation is unconfirmed. Its random-row test is not independent experimental validation. The thermal source file is named C2M0040120D rather than C2M0080120D and uses all points for training; it is not presented here as validated thermal behaviour for this device.</p>
  <p>The static networks do not enforce physical constraints such as zero-current behaviour or monotonicity. Results should be used within the reference-data ranges, with particular care near zero current.</p>
  <p><a href="/files/research/mosfet-ann/test-predictions.csv">Held-out predictions (CSV)</a> · <a href="/files/research/mosfet-ann/run-metadata.json">Run settings and metrics</a> · <a href="/files/research/mosfet-ann/reproduce.py">Reproduction script</a></p>
</details>

## Project Resources

[View the project on GitHub](https://github.com/FulongLi/AIPE-MOSFET-ANN-Modelling) · [Back to Research](/research/)

<!-- Add laboratory setup, measurement and temperature-rise photographs here when supplied, with device and test-condition captions. -->
