---
layout: single
title: "Electrical Characterization"
permalink: /research/electrical-characterization/
author_profile: true
body_class: device-project-page
project_stylesheet: /assets/css/marine-project.css
project_contents: true
mathjax: true
excerpt: "A jointly built double-pulse test platform, device measurement campaign and waveform analysis for switching-loss data."
---

I jointly built a double-pulse test (DPT) platform, modified its test board and carried out a SiC device measurement campaign, with waveform post-processing that turns recorded switching events into loss data for converter design.

<h2 id="double-pulse-testing">How Double-Pulse Testing Works</h2>

Converter loss models need to know how much energy a power device dissipates each time it switches, across the voltages, currents, temperatures and gate resistances it will meet in operation. A double-pulse test measures this directly under controlled conditions.

The device under test switches an inductive load supplied from a charged DC-link capacitor bank. The first pulse builds current in the load inductor to the chosen value; the device then turns off, and the second pulse turns it on again at that current before a final turn-off. Recording the drain voltage and current through these transitions gives the turn-on and turn-off energies:

<div class="math-display">\[E = \int v(t)\,i(t)\,dt.\]</div>

Static I–V and C–V measurements complement the switching characteristics with the device's conduction and capacitance characteristics.

<h2 id="dpt-platform">Test Platform and Measurement Campaign</h2>

I jointly assembled the platform and modified the original test board. The rig combines a 2.12 mF capacitor bank and a 52.8 µH load inductor with laminated busbars, a gate driver and a heated device mounting, so that switching conditions can be repeated at controlled temperatures.

<figure>
  <a href="/images/research/device-characterization/dpt-test-platform.png" target="_blank" rel="noopener"><img src="/images/research/device-characterization/dpt-test-platform.png" alt="Double-pulse test platform with capacitor bank, laminated busbars, load inductor, gate driver and heated device mounting" width="1500" height="836" fetchpriority="high"></a>
  <figcaption>Double-pulse test platform with capacitor bank, laminated busbars, load inductor and heated device mounting.</figcaption>
</figure>

The campaign covered more than 450 test points, varying DC-link voltage, load current and gate resistance at 25 °C, 75 °C and 125 °C. Static characteristics were measured with a Keysight B1505A. Acquisition was manual; post-processing was automated. It aligns the voltage and current channels, corrects offsets, integrates instantaneous power over the switching window and extracts current and voltage slew rates and reverse-recovery quantities.

The resulting datasets supply the switching-loss inputs for [device modelling](/research/mosfet_ann_modelling/). The waveform post-processing is continued in the public [DPT Automation](https://github.com/FulongLi/DPT_Automation) repository.

[Thermal Characterization](/research/thermal-characterization/) · [Power Device Characterization](/research/switching_devices/) · [Back to Research](/research/)
