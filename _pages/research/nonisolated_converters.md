---
layout: single
title: "Non-Isolated Converters"
permalink: /research/nonisolated_converters/
author_profile: true
excerpt: "Non-isolated converters for DC microgrids: bidirectional battery interfaces, Boost-converter stabilisation and AC–DC interfaces."
---

Non-isolated converters connect sources, storage and the grid to a DC microgrid bus without a transformer, so their control directly shapes the stability and coordination of the whole network. My work in this area links converter-level control to microgrid operation.

<h2 id="bidirectional-buck-boost-converter">Bidirectional Half-Bridge Buck–Boost Converter</h2>
<span id="bidirectional-half-bridge-buckboost-converter"></span>

I developed a modular half-bridge converter that charges and discharges a battery from the DC bus, combining a power stage, isolated sensing and gate drives and DSP control. It is the interface converter of my laboratory microgrids.

[Read the bidirectional converter project](/research/nonisolated-converters/bidirectional-buck-boost/)

## Buck / Boost Converter Control

I developed a passive stabiliser for Boost interface converters. A high-pass-filtered feedforward path suppresses oscillation without the steady-state voltage shift of constant-gain compensation.

[Read the passive-control study](/research/dcmg/passive-control/) · [IEEE JESTPE 2021 paper](https://ieeexplore.ieee.org/document/9391691) · [Public Buck and Boost converter resources](https://github.com/FulongLi/NonisolatedCoverters)

<h2 id="acdc-converter-interfaces">AC–DC Converter Interfaces</h2>

During visiting research at Zhejiang University, I worked with the three-phase voltage-source converter interface of an existing 50 kW DC microgrid platform.

[Zhejiang University platform](/research/experimental-platforms/zhejiang/)

[DC Microgrid Control Strategies](/research/dcmg/) · [Back to Research](/research/)
