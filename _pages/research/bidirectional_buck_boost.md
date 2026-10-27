---
layout: single
title: "Bidirectional Buck–Boost Converter"
permalink: /research/nonisolated-converters/bidirectional-buck-boost/
author_profile: true
body_class: microgrid-project-page
project_stylesheet: /assets/css/marine-project.css
project_contents: true
---

## Role in the Microgrid

The bidirectional half-bridge converter is a building block of the low-voltage DC microgrid testbed. It links a lower-voltage battery bank to the common DC bus: Boost operation delivers stored energy to the bus, while Buck operation charges the battery. The same modular interface can also support a PV source or grid emulator with the appropriate control.

## Power and Control Architecture

<figure>
  <a href="/images/research/experimental-platforms/aston-converter-architecture.png" target="_blank" rel="noopener"><img src="/images/research/experimental-platforms/aston-converter-architecture.png" alt="Bidirectional interface converter with inductor, switches, voltage and current transducers, isolated sampling, gate drive and TMS320F28335 control board" width="1206" height="1017" loading="lazy"></a>
  <figcaption>Interface converter power stage, sensing and digital control.</figcaption>
</figure>

The power stage combines an inductor, switching devices and input/output capacitors. Voltage and current transducers feed conditioned measurements to the control board, while isolated gate drives apply its switching commands. The **TMS320F28335 DSP** runs the local control and operating logic. Depending on the source, the controller can implement voltage or current regulation, battery charging, PV maximum-power-point tracking and DC bus signalling.

## Prototype Ratings and System Use

The Aston PhD prototype is rated at **250 W per interface**, with a 240 µH inductor and 470 µF input and output capacitors. Two 12 V batteries in series form each 24 V battery bank. Four interfaces connect the grid emulator, two battery banks and PV emulator; the latter operates in the Boost direction. A separate, later converter version documented in the Loughborough test-bench repository is rated at **500 W per converter**.

The converter supports the wider hierarchy: local regulation shapes its response, droop control shares power between sources, and supervisory rules assign operating roles. [Read the DC microgrid control study](/research/dcmg/).

[PhD thesis, Chapter 3](https://publications.aston.ac.uk/id/eprint/46135/) · [Aston testbed](/research/experimental-platforms/aston/) · [Loughborough testbed](/research/experimental-platforms/loughborough/) · [Non-isolated converters](/research/nonisolated_converters/)
