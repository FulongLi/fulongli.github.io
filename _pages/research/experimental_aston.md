---
layout: single
title: "Aston University DC Microgrid Testbed"
permalink: /research/experimental-platforms/aston/
author_profile: true
body_class: microgrid-project-page
project_stylesheet: /assets/css/marine-project.css
project_contents: true
---

## A Modular Laboratory Microgrid

I built this low-voltage platform to investigate converter stability, coordinated source operation and energy management. Four interface converters connect a grid emulator, a PV emulator and two battery banks to a common DC bus; electronic and resistive loads create controllable demand.

<figure>
  <a href="/images/research/dc-microgrid-control/laboratory-bench.png" target="_blank" rel="noopener"><img src="/images/research/dc-microgrid-control/laboratory-bench.png" alt="Aston DC microgrid bench with interface converters, PV emulator, batteries, loads and measurement equipment" width="1212" height="915"></a>
  <figcaption>The Aston laboratory test bench. <span class="figure-source">PhD thesis, Figure 3.1, p. 63.</span></figcaption>
</figure>

## System Architecture

<figure>
  <a href="/images/research/experimental-platforms/aston-system-architecture.png" target="_blank" rel="noopener"><img src="/images/research/experimental-platforms/aston-system-architecture.png" alt="Schematic showing grid, photovoltaic and battery interfaces connected to a common DC bus with loads" width="990" height="645" loading="lazy"></a>
  <figcaption>DC microgrid configuration. <span class="figure-source">PhD thesis, Figure 3.2, p. 63.</span></figcaption>
</figure>

The grid-side supply and a soaking resistor emulate grid exchange; the resistor dissipates returned power. Each battery bank comprises two 12 V lead-acid batteries in series. The PV emulator supplies up to 150 W. The diagram represents the grid connection conceptually; the experimental grid interface uses the DC supply and soaking resistor.

## Converter and Control

Each interface converter is rated at **250 W**. A TMS320F28335 DSP control board, sensing and isolated gate drives support local regulation and coordination. The battery interfaces operate bidirectionally; the PV interface operates in the Boost direction. This platform supported the studies of [passive control](/research/dcmg/passive-control/), [DC bus signalling](/research/dcmg/dc-bus-signalling/) and [rule-based energy management](/research/dcmg/rule-based-ems/).

[Bidirectional Buck–Boost converter](/research/nonisolated-converters/bidirectional-buck-boost/) · [PhD thesis, Chapter 3](https://publications.aston.ac.uk/id/eprint/46135/) · [Figure sources](/files/research/dc-microgrid-control/figure-sources.json) · [All experimental platforms](/research/experimental_platforms/)
