---
layout: single
title: "10 kW LLC Resonant Converter"
permalink: /research/isolated-converters/llc/
author_profile: true
excerpt: "Resonant-tank design and closed-loop control of a 10 kW, 750 V to 50 V LLC converter for data-centre power."
body_class: microgrid-project-page
project_stylesheet: /assets/css/marine-project.css
project_contents: true
---

I studied an isolated 10 kW LLC resonant converter for a data-centre power application, from resonant-tank design calculations to closed-loop control.

## How an LLC Converter Regulates Its Output

An LLC converter places a resonant tank between a switching bridge and an isolating transformer. The tank is formed by a resonant capacitor, a resonant inductor and the transformer's magnetising inductance. The voltage gain of the tank depends on the switching frequency, so the controller regulates the output by varying frequency as the input voltage and load change. Operating near resonance allows soft switching, which keeps losses low at high frequency.

<figure>
  <a href="/images/research/llc-converter/llc-circuit.png" target="_blank" rel="noopener"><img src="/images/research/llc-converter/llc-circuit.png" alt="Full-bridge LLC converter with resonant capacitor and inductor, transformer, diode rectifier and output filter" width="784" height="366"></a>
  <figcaption>Full-bridge LLC power stage with resonant tank, transformer, secondary rectifier and output filter.</figcaption>
</figure>

## Resonant-Tank Design

The design had to supply a regulated 50 V output across a wide input range:

| Design target | Value |
| --- | --- |
| Input voltage | 750 V nominal; 675–825 V range |
| Output voltage | 50 V |
| Maximum output power | 10 kW |
| Target operating frequency | 200 kHz |

I swept the quality factor <i>Q</i> and inductance ratio <i>m</i> to examine the gain available across the input range. One initial design uses <i>Q</i> = 0.4 and <i>m</i> = 10 with a 15:1 transformer turns ratio, giving these calculated tank values:

| Parameter | Initial calculated value |
| --- | --- |
| Resonant inductance | 14.51 µH |
| Resonant capacitance | 43.6 nF |
| Magnetising inductance | 130.62 µH |
| Transformer turns ratio | 15:1 |

The sweep also considered reducing <i>m</i> to 9 or 8 to increase the maximum gain, and a later alternative investigated <i>Q</i> = 0.9 with a changed turns ratio and a 100 kHz resonant frequency. These are design alternatives, not measured component values or a final hardware specification.

## Closed-Loop Control

A PI controller regulates the output voltage by adjusting the switching frequency, holding 50 V as the input voltage moves across its 675–825 V range and the load changes. The low-frequency end of that range, where the tank must provide its highest gain, sets the tightest margin and drives the choice of <i>Q</i> and <i>m</i>.

[Isolated Converters](/research/isolated_converters/) · [Converter Design Optimisation](/research/converter_optimization/) · [Back to Research](/research/)
