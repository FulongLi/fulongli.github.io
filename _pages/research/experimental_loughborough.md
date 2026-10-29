---
layout: single
title: "Loughborough University DC Microgrid Testbed"
permalink: /research/experimental-platforms/loughborough/
author_profile: true
excerpt: "A modular low-voltage DC microgrid test bench and its successive interface-converter prototypes."
body_class: microgrid-project-page
project_stylesheet: /assets/css/marine-project.css
project_contents: true
---

A low-voltage DC microgrid test bench was built at Loughborough University around modular interface converters, supporting grid-connected and islanded operation so that converter control and system-level power management can be studied together.

## A Modular Test Bench

The test bench follows the same four-interface structure as the earlier PhD microgrid: a grid emulator, two battery banks and a PV emulator connect to the DC bus through interface converters, alongside electronic and resistive loads. A DC supply and soaking resistor emulate the grid, and a computer and instruments monitor the system.

<figure>
  <a href="/images/research/experimental-platforms/aston-system-architecture.png" target="_blank" rel="noopener"><img src="/images/research/experimental-platforms/aston-system-architecture.png" alt="Schematic showing grid, photovoltaic and battery interfaces connected to a common DC bus with loads" width="990" height="645" loading="lazy"></a>
  <figcaption>Four-interface DC microgrid configuration shared with the earlier thesis platform; a system-level reference, not a wiring diagram of this prototype.</figcaption>
</figure>

## Converter Development

The first interface converter was a **100 W** bidirectional Boost converter on a 48 V bus. A second version rated at **500 W per converter** followed, improving gate drive and sensing, reducing switching ringing and adding wireless communication support. Stacked power and control boards provide voltage and current sensing, gate drive and DSP-based control.

<figure>
  <a href="/images/research/experimental-platforms/loughborough-v2.png" target="_blank" rel="noopener"><img src="/images/research/experimental-platforms/loughborough-v2.png" alt="Second-version interface converter with stacked power and control boards and a group of converter modules" width="602" height="302" loading="lazy"></a>
  <figcaption>Second-version interface converter with stacked power and control boards, and a group of assembled modules.</figcaption>
</figure>

The converters implement current and voltage regulation, battery charging, droop control and PV maximum-power-point tracking.

## The Completed Setup

<figure>
  <a href="/images/research/experimental-platforms/loughborough-setup.png" target="_blank" rel="noopener"><img src="/images/research/experimental-platforms/loughborough-setup.png" alt="Low-voltage DC microgrid experimental bench with modular converters, batteries, instruments and computer" width="602" height="425" loading="lazy"></a>
  <figcaption>The complete test bench with modular converters, batteries, instruments and monitoring computer.</figcaption>
</figure>

Hardware designs and schematics are available in the [DC Microgrid Test Bench repository](https://github.com/FulongLi/DCMicrogridTestBench).

[Bidirectional Buck–Boost converter](/research/nonisolated-converters/bidirectional-buck-boost/) · [All experimental platforms](/research/experimental_platforms/) · [Back to Research](/research/)
