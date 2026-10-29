---
layout: single
title: "Non-Isolated Converters"
permalink: /research/nonisolated_converters/
author_profile: true
excerpt: "Non-isolated converters for DC microgrids: bidirectional battery interfaces and Boost-converter stabilisation."
---

Non-isolated converters connect sources, storage and the grid to a DC microgrid bus without a transformer, so their control directly shapes the stability and coordination of the whole network. Work in this area links converter-level control to microgrid operation.

<h2 id="bidirectional-buck-boost-converter">Bidirectional Half-Bridge Buck–Boost Converter</h2>
<span id="bidirectional-half-bridge-buckboost-converter"></span>

A modular half-bridge converter charges and discharges a battery from the DC bus, combining a power stage, isolated sensing and gate drives and DSP control. It is the interface converter of the laboratory microgrids.

[Read the bidirectional converter project](/research/nonisolated-converters/bidirectional-buck-boost/)

## Buck / Boost Converter Control

A passive stabiliser was developed for Boost interface converters. A high-pass-filtered feedforward path suppresses oscillation without the steady-state voltage shift of constant-gain compensation.

[Read the passive-control study](/research/dcmg/passive-control/) · [IEEE JESTPE 2021 paper](https://ieeexplore.ieee.org/document/9391691) · [Public Buck and Boost converter resources](https://github.com/FulongLi/NonisolatedCoverters)

[DC Microgrid Control Strategies](/research/dcmg/) · [Back to Research](/research/)
