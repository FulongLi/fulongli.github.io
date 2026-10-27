---
layout: single
title: "Loughborough University DC Microgrid Testbed"
permalink: /research/experimental-platforms/loughborough/
author_profile: true
body_class: microgrid-project-page
project_stylesheet: /assets/css/marine-project.css
project_contents: true
---

## A Modular Test Bench

I built and developed a low-voltage DC microgrid test bench around modular interface converters. The platform supports grid-connected and islanded operation and allows converter control and system-level power management to be studied together.

<figure>
  <a href="/images/research/experimental-platforms/loughborough-setup.png" target="_blank" rel="noopener"><img src="/images/research/experimental-platforms/loughborough-setup.png" alt="Low-voltage DC microgrid experimental bench with modular converters, batteries, instruments and computer" width="602" height="425" loading="lazy"></a>
  <figcaption>The complete experimental setup. <span class="figure-source"><a href="https://github.com/FulongLi/DCMicrogridTestBench">DC Microgrid Test Bench repository</a>, CC BY 4.0.</span></figcaption>
</figure>

## System Architecture

The documented setup uses four interfaces: a grid emulator, two battery banks and a PV emulator. The converters connect these resources to the DC bus, alongside electronic and resistive loads, with a computer and instruments for monitoring. A DC supply and soaking resistor emulate the grid interface.

<figure>
  <a href="/images/research/experimental-platforms/aston-system-architecture.png" target="_blank" rel="noopener"><img src="/images/research/experimental-platforms/aston-system-architecture.png" alt="Schematic showing grid, photovoltaic and battery interfaces connected to a common DC bus with loads" width="990" height="645" loading="lazy"></a>
  <figcaption>DC microgrid configuration. <span class="figure-source">PhD thesis, Figure 3.2, p. 63.</span></figcaption>
</figure>

This earlier thesis diagram illustrates the same four-interface system configuration described in the test-bench repository; it is a system-level reference, not a wiring diagram of the later prototype.

## Converter Development

<figure>
  <a href="/images/research/experimental-platforms/loughborough-v2.png" target="_blank" rel="noopener"><img src="/images/research/experimental-platforms/loughborough-v2.png" alt="Second-version interface converter with stacked power and control boards and a group of converter modules" width="602" height="302" loading="lazy"></a>
  <figcaption>Second-version converter hardware and assembled modules. <span class="figure-source"><a href="https://github.com/FulongLi/DCMicrogridTestBench">DC Microgrid Test Bench repository</a>, CC BY 4.0.</span></figcaption>
</figure>

The repository describes a first **100 W** bidirectional Boost converter on a 48 V bus, followed by a second version rated at **500 W per converter**. The upgrade improved gate drive and sensing, reduced switching ringing and added wireless communication support. Power and control boards provide voltage and current sensing, gate drive and DSP-based control.

The documented functions include current and voltage regulation, battery charging, droop control and PV maximum-power-point tracking. The repository contains hardware designs and schematics for further detail.

[DC Microgrid Test Bench repository](https://github.com/FulongLi/DCMicrogridTestBench) · [Bidirectional Buck–Boost converter](/research/nonisolated-converters/bidirectional-buck-boost/) · [All experimental platforms](/research/experimental_platforms/)
