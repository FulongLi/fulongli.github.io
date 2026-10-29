---
layout: single
title: "Aston University DC Microgrid Testbed"
permalink: /research/experimental-platforms/aston/
author_profile: true
excerpt: "A modular low-voltage DC microgrid with grid, PV and battery interfaces, built for PhD control experiments."
body_class: microgrid-project-page
project_stylesheet: /assets/css/marine-project.css
project_contents: true
---

This low-voltage DC microgrid was built at Aston University during the PhD research to test converter stability, coordinated source operation and energy management on real hardware.

## A Modular Laboratory Microgrid

A laboratory microgrid reproduces, at low voltage and power, the structure of a real DC network: sources, storage and loads connected to a common bus through power converters. Building it from identical modular interface converters means each control method runs on the same hardware it would use in the field, and sources can be added or reconfigured without redesigning the system.

## System Architecture and Converters

Four interface converters connect a grid emulator, a PV emulator and two battery banks to the common DC bus, and electronic and resistive loads create controllable demand. A DC supply and a soaking resistor emulate grid exchange, with the resistor dissipating returned power. Each battery bank consists of two 12 V lead-acid batteries in series, and the PV emulator supplies up to 150 W.

<figure>
  <a href="/images/research/experimental-platforms/aston-system-architecture.png" target="_blank" rel="noopener"><img src="/images/research/experimental-platforms/aston-system-architecture.png" alt="Schematic showing grid, photovoltaic and battery interfaces connected to a common DC bus with loads" width="990" height="645" loading="lazy"></a>
  <figcaption>Microgrid configuration: grid, PV and battery interfaces on a common DC bus with loads. The grid connection is shown conceptually; the bench emulates it with a DC supply and soaking resistor.</figcaption>
</figure>

Each [bidirectional interface converter](/research/nonisolated-converters/bidirectional-buck-boost/) is rated at **250 W**, with a TMS320F28335 DSP control board, sensing and isolated gate drives for local regulation and coordination. The battery interfaces operate bidirectionally; the PV interface operates in the Boost direction.

## The Completed Testbed

<figure>
  <a href="/images/research/dc-microgrid-control/laboratory-bench.png" target="_blank" rel="noopener"><img src="/images/research/dc-microgrid-control/laboratory-bench.png" alt="Aston DC microgrid bench with interface converters, PV emulator, batteries, loads and measurement equipment" width="1212" height="915" loading="lazy"></a>
  <figcaption>The Aston test bench with interface converters, PV emulator, batteries, loads and measurement equipment.</figcaption>
</figure>

The testbed carried the experimental studies of the PhD research: [passive control](/research/dcmg/passive-control/), [dual-window DC bus signalling](/research/dcmg/dc-bus-signalling/) and [rule-based energy management](/research/dcmg/rule-based-ems/).

[PhD thesis, Chapter 3](https://publications.aston.ac.uk/id/eprint/46135/) · [All experimental platforms](/research/experimental_platforms/) · [Back to Research](/research/)
