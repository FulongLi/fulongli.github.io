---
layout: single
title: "Power Device Characterization"
permalink: /research/switching_devices/
author_profile: true
excerpt: "Electrical and thermal characterization of SiC and GaN power devices: double-pulse testing, thermal resistance and impedance, and current capability."
---

Converter design depends on device data that datasheets do not fully provide: how much energy each switching event costs under real operating conditions, and how quickly that heat reaches the cooling system. Device characterisation produces both, from configuring the laboratory equipment and test conditions to turning recorded signals into device data.

<h2 id="electrical-characterization">Double Pulse Test</h2>

A jointly built double-pulse test platform, with a modified test board, carried a SiC measurement campaign of more than 450 test points across voltage, current, gate resistance and temperature. Waveform post-processing extracts turn-on and turn-off energies, slew rates and reverse-recovery quantities, complemented by static I–V and C–V measurements. For GaN devices, a half-bridge double-pulse test board was designed.

[Read the double pulse test project](/research/electrical-characterization/)

<h2 id="thermal-characterization">Thermal Characterization</h2>

The thermal resistance of a packaged GaN device, about 0.2 K/W, was measured using a temperature-dependent resistance on the chip as its thermometer and a purpose-designed six-seat cooling plate. Earlier work measured the transient thermal impedance of a SiC MOSFET and extracted its Cauer thermal network.

[Read the thermal characterization project](/research/thermal-characterization/)

<h2 id="gan-current-capability">GaN Current Capability</h2>

The same packaged GaN device was tested for current capability by stepping the drain current and tracking the junction temperature through the calibrated on-chip resistance, with separate calibrations for the gate off and on.

[Read the GaN current capability test](/research/gan-current-capability/)

The measured characteristics feed [Semiconductor Device Modelling](/research/mosfet_ann_modelling/) and [Converter Design Optimisation](/research/converter_optimization/). [Power Device Reliability Testing](/research/reliability_testing/) is a separate area of work.

[Back to Research](/research/)
