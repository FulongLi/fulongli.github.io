---
layout: single
title: "Passive Control for DC Microgrid Interface Converters"
permalink: /research/dcmg/passive-control/
author_profile: true
body_class: microgrid-project-page
project_stylesheet: /assets/css/marine-project.css
project_script: /assets/js/marine-project.js
excerpt: "Passivity-based Boost converter stabilisation: feedforward compensation, high-pass filtering and experimental stability assessment."
---

<h2 id="overview">Primary Control: Stable Converter Dynamics</h2>

The primary layer must regulate converter current and voltage before a microgrid can coordinate its sources. My work addressed the **non-minimum-phase dynamics of Boost interface converters**, which can restrict voltage regulation and lead to oscillation under demanding load or terminal-capacitance conditions.

**My contribution:** I developed a feedforward passive stabiliser, then modified it with a high-pass filter to retain its stabilising action while avoiding the steady-state voltage shift of a constant feedforward gain. The design and experiments appear in **Chapter 5 of my PhD thesis**, with a related journal publication in **IEEE JESTPE (2021)**.

<nav class="project-contents" aria-label="Project contents">
  <p><strong>On this page</strong></p>
  <ul>
    <li><a href="#overview">Research overview</a></li>
    <li><a href="#stabiliser-design">Passive stabiliser design</a></li>
    <li><a href="#experimental-validation">Experimental evidence</a></li>
    <li><a href="#system-integration">Microgrid integration</a></li>
    <li><a href="#project-resources">Sources and publications</a></li>
  </ul>
</nav>

<h2 id="stabiliser-design">From Feedforward Compensation to a Passive Stabiliser</h2>

The thesis models the inner current loop and outer voltage loop, then uses positive-realness analysis to guide compensation of the outer-loop plant. Constant feedforward gain **K** compensates the unfavourable dynamics, but also changes the low-frequency gain and shifts the quiescent operating point.

The modified compensator introduces a high-pass filter:

**G<sub>p</sub>(s) = Ks / (s + δ)**

Here, **K** sets the compensation gain and **δ** is the filter corner frequency. The compensator tends to zero at DC and to K at high frequency, retaining dynamic compensation while removing its constant-gain contribution at the steady operating point. The thesis derives the design requirements from the converter model and its Nyquist response.

<figure>
  <a href="/images/research/dc-microgrid-control/passive-control-block.png" target="_blank" rel="noopener" aria-label="View original: passive converter control block"><img src="/images/research/dc-microgrid-control/passive-control-block.png" alt="Original converter diagram with droop control, outer voltage loop, inner current loop and additional passive stabiliser Gp" width="1248" height="543" loading="lazy"></a>
  <figcaption><strong>The stabiliser within the converter controller.</strong> G<sub>p</sub> supplements the existing current/voltage control structure. The complete design also considers controller discretisation. <span class="figure-source">PhD thesis, Figure 5.9, p. 100.</span></figcaption>
</figure>

<h2 id="experimental-validation">Experimental Evidence</h2>

The Chapter 5 experiment reduced the terminal capacitor from **470 µF to 100 µF** to expose an oscillatory case. Constant-gain compensation suppressed the oscillation, accompanied by the predicted voltage drop. The high-pass-filtered stabiliser suppressed it without that steady-state shift in the reported test.

<figure>
  <a href="/images/research/dc-microgrid-control/passive-constant-gain-result.png" target="_blank" rel="noopener" aria-label="View original: constant-gain passive control result"><img src="/images/research/dc-microgrid-control/passive-constant-gain-result.png" alt="Oscilloscope trace showing oscillation suppression and a voltage drop when constant-gain passive control is switched on" width="1293" height="444" loading="lazy"></a>
  <figcaption><strong>Constant-gain compensation.</strong> The oscillation is suppressed, but the DC bus voltage shifts when passive control is enabled. <span class="figure-source">PhD thesis, Figure 5.13, p. 105.</span></figcaption>
</figure>

<figure>
  <a href="/images/research/dc-microgrid-control/passive-hpf-result.png" target="_blank" rel="noopener" aria-label="View original: high-pass-filtered passive control result"><img src="/images/research/dc-microgrid-control/passive-hpf-result.png" alt="Original DC bus voltage trace with oscillations suppressed after enabling high-pass-filtered passive control at K equals 1.9" width="1293" height="444" loading="lazy"></a>
  <figcaption><strong>High-pass-filtered compensation, K = 1.9.</strong> The modified stabiliser suppresses oscillation while avoiding the voltage shift of the constant-gain test. Both original traces retain their voltage and time scales. <span class="figure-source">PhD thesis, Figure 5.14, p. 105.</span></figcaption>
</figure>

Further tests cover **K = 2.5** and two parallel converters with droop current sharing. Removing the stabilisers from the parallel-converter test produces oscillation, connecting the local design to operation with multiple converters.

<h2 id="system-integration">Connecting Local Stability to the Microgrid</h2>

The stabiliser forms part of the **primary layer** of the [three-layer framework](/research/dcmg/#hierarchical-control). Chapter 6 examines terminal admittance and minor-loop gain for the integrated system's operating modes.

The compensation is designed for the analysed converter and operating conditions. Chapter 6 identifies a trade-off between compensating non-minimum-phase behaviour and terminal impedance when supplying constant-power loads. The experiments establish behaviour in the tested cases; gain and capacitor selection remain part of the converter design.

<h2 id="project-resources">Sources and Publications</h2>

- [Control Strategies for Low Voltage DC Microgrids](https://publications.aston.ac.uk/id/eprint/46135/), PhD thesis, **Chapter 5, pp. 88–107**, and Chapter 6 terminal-admittance analysis.
- F. Li and Z. Lin, [Novel Passive Controller Design for Enhancing Boost Converter Stability in DC Microgrid Applications](https://ieeexplore.ieee.org/document/9391691), **IEEE Journal of Emerging and Selected Topics in Power Electronics**, 9(6), 6901–6911, December 2021.
- Related work: [Terminal Capacitor Compensation Based Stability Design for DC Microgrids](https://ieeexplore.ieee.org/document/9232923), IEEE ICDCM, 2019.

[Next: Dual-Window DC Bus Signalling](/research/dcmg/dc-bus-signalling/) · [DC Microgrid Control Strategies](/research/dcmg/) · [All publications](/publications/)
