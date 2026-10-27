---
layout: single
title: "10 kW LLC Resonant Converter"
permalink: /research/isolated-converters/llc/
author_profile: true
body_class: microgrid-project-page
project_stylesheet: /assets/css/marine-project.css
project_contents: true
---

## Design Objective

I studied an isolated LLC converter for a data-centre power application, using resonant-tank design calculations and closed-loop simulation. The work remained at the simulation stage; no hardware prototype was built or tested.

| Design target | Value |
| --- | --- |
| Input voltage | 750 V nominal; 675–825 V range |
| Output voltage | 50 V |
| Maximum output power | 10 kW |
| Target operating frequency | 200 kHz |

## Power Stage

<figure>
  <a href="/images/research/llc-converter/llc-circuit.png" target="_blank" rel="noopener"><img src="/images/research/llc-converter/llc-circuit.png" alt="Full-bridge LLC converter with resonant capacitor and inductor, transformer, diode rectifier and output filter" width="784" height="366"></a>
  <figcaption>LLC converter power stage.</figcaption>
</figure>

A full switching bridge drives the resonant capacitor and inductor. The transformer's magnetising inductance forms the third resonant element; an isolated secondary rectifier and output capacitor supply the load. Frequency variation changes the tank gain to regulate the output as input voltage and load change.

## Resonant-Tank Design

The study sweeps the quality factor <i>Q</i> and inductance ratio <i>m</i> to examine the available gain across the input range. One initial design uses <i>Q</i> = 0.4 and <i>m</i> = 10, with a 15:1 primary-to-secondary transformer turns ratio. The corresponding calculated tank values are:

| Parameter | Initial calculated value |
| --- | --- |
| Resonant inductance | 14.51 µH |
| Resonant capacitance | 43.6 nF |
| Magnetising inductance | 130.62 µH |
| Transformer turns ratio | 15:1 |

The sweep also considers reducing <i>m</i> to 9 or 8 to increase maximum gain. A later alternative investigates <i>Q</i> = 0.9 with a changed turns ratio and a 100 kHz resonant frequency. These are design alternatives explored in the study, not measured component values or a final hardware specification.

## Closed-Loop Simulation

A PI controller regulates the output while the model applies input-voltage and load changes. In the illustrated simulation, the output voltage dips when the input falls from 825 V to 675 V, then returns towards 50 V. A subsequent load reduction produces a smaller transient. The study notes that the operating margin is tight at low frequency, motivating further resonant-tank exploration.

<figure>
  <a href="/images/research/llc-converter/llc-output-transient.png" target="_blank" rel="noopener"><img src="/images/research/llc-converter/llc-output-transient.png" alt="Simulated LLC output voltage and output power during changes in input voltage and load" width="644" height="274" loading="lazy"></a>
  <figcaption>Simulated output voltage and power response.</figcaption>
</figure>

The response illustrates the simulated control behaviour under the chosen conditions. Switching performance, losses, thermal behaviour and manufacturability would require further design and experimental verification.

[Isolated Converters](/research/isolated_converters/) · [Converter Design Optimisation](/research/converter_optimization/) · [Back to Research](/research/)
