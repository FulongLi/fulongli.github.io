---
layout: single
title: "Passive Control for DC Microgrid Interface Converters"
permalink: /research/dcmg/passive-control/
author_profile: true
body_class: microgrid-project-page
project_stylesheet: /assets/css/marine-project.css
project_contents: true
excerpt: "Passivity-based Boost converter stabilisation: feedforward compensation, high-pass filtering and experimental stability assessment."
---

<h2 id="overview">Suppressing Oscillation Without Shifting the Operating Point</h2>

Boost converters can exhibit non-minimum-phase dynamics that limit voltage regulation. My PhD research developed a **feedforward passive stabiliser** for these interface converters, then added a high-pass filter to retain dynamic compensation without changing the steady-state operating point.

<h2 id="stabiliser-design">A Filtered Passive Stabiliser</h2>

<figure>
  <a href="/images/research/dc-microgrid-control/passive-control-block.png" target="_blank" rel="noopener"><img src="/images/research/dc-microgrid-control/passive-control-block.png" alt="Droop, voltage and current control loops with an additional passive stabiliser" width="1248" height="543" fetchpriority="high"></a>
  <figcaption><strong>The compensator within the local controller.</strong> The added stabiliser supports the existing current and voltage loops. <span class="figure-source">PhD thesis, Figure 5.9, p. 100.</span></figcaption>
</figure>

The compensator **G<sub>p</sub>(s) = Ks / (s + δ)** tends to zero at DC and to gain K at high frequency. This retains the stabilising action while removing the constant-gain contribution at the quiescent operating point. Positive-realness and frequency-response analysis guide the design. The model separates the inner current loop from the outer voltage loop; the feedforward term compensates the outer-loop plant. High-pass filtering removes the compensator’s DC contribution while preserving its higher-frequency action. The corner frequency δ and gain K therefore belong to the analysed converter design.

<h2 id="experimental-validation">Experimental Result</h2>

The experiment reduced terminal capacitance from **470 µF to 100 µF** to expose oscillation. Constant-gain compensation suppressed it but introduced a voltage drop; the filtered stabiliser suppressed it without that steady-state shift.

<figure>
  <a href="/images/research/dc-microgrid-control/passive-hpf-result.png" target="_blank" rel="noopener"><img src="/images/research/dc-microgrid-control/passive-hpf-result.png" alt="DC bus voltage oscillation suppressed when high-pass-filtered passive control is enabled" width="1293" height="444" loading="lazy"></a>
  <figcaption><strong>Filtered compensation, K = 1.9.</strong> The recorded bus voltage settles when the stabiliser is enabled. <span class="figure-source">PhD thesis, Figure 5.14, p. 105.</span></figcaption>
</figure>

<h2 id="system-integration">From Converter Dynamics to Microgrid Control</h2>

Further tests examined parallel converters with droop current sharing. The stabiliser became the primary layer of the [integrated DC microgrid framework](/research/dcmg/#hierarchical-control). Its gain and capacitor requirements remain specific to the converter and operating conditions assessed.

[Novel Passive Controller Design for Enhancing Boost Converter Stability in DC Microgrid Applications](https://ieeexplore.ieee.org/document/9391691), IEEE JESTPE, 2021. · [PhD thesis](https://publications.aston.ac.uk/id/eprint/46135/), Chapter 5. · [Figure sources](/files/research/dc-microgrid-control/figure-sources.json)

[Dual-Window DC Bus Signalling](/research/dcmg/dc-bus-signalling/) · [DC Microgrid Control Strategies](/research/dcmg/) · [Back to Research](/research/)
