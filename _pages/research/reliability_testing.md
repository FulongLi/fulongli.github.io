---
layout: single
title: "Power Device Reliability Testing"
permalink: /research/reliability_testing/
author_profile: true
body_class: device-project-page
project_stylesheet: /assets/css/marine-project.css
project_contents: true
excerpt: "Environmental and thermal reliability testing of SiC power modules and GaN devices."
---

My reliability testing work covers environmental and thermal stress tests of SiC power modules and GaN devices, alongside my [electrical and thermal characterisation](/research/switching_devices/) work.

<h2 id="reliability-concept">Why Accelerated Stress Testing</h2>

Power devices are expected to operate for many years, so their weaknesses must be revealed in weeks rather than in service. Accelerated stress tests apply conditions harsher than normal operation and monitor the device for drift or failure. Reverse-bias tests hold a device in its blocking state at high temperature, and with high humidity in H3TRB, to expose degradation of the blocking junction, passivation and package. Thermal cycling repeatedly heats and cools a device, stressing the interfaces between materials with different thermal expansion.

<h2 id="sic-power-module-htrb-h3trb-test">SiC Power Module HTRB / H3TRB Test</h2>

I carried out high-temperature reverse-bias (HTRB) and high-humidity, high-temperature reverse-bias (H3TRB) testing of SiC power modules.

In both tests, the devices are held off, with each gate shorted to its source, while a DC supply applies a high voltage between drain and source. Each device is usually connected through a series resistor, which limits the current if it fails, and its leakage current is recorded throughout the test. A rising leakage current shows the blocking capability degrading.

<figure class="project-blueprint">
  <a href="/images/research/reliability-testing/htrb-h3trb-circuit.svg" target="_blank" rel="noopener"><img src="/images/research/reliability-testing/htrb-h3trb-circuit.svg" alt="HTRB and H3TRB test circuit: a high-voltage DC supply biases several devices in parallel inside a climate chamber, each through a series resistor and a leakage-current meter, with each gate shorted to its source" width="760" height="322" fetchpriority="high"></a>
  <figcaption>HTRB and H3TRB test circuit: devices in a climate chamber held in the blocking state, each with its own leakage-current monitor.</figcaption>
</figure>

For automotive power modules, the AQG 324 qualification guideline sets these conditions for the two tests:

| AQG 324 condition | HTRB | H3TRB |
| --- | --- | --- |
| Drain–source voltage | At least 80% of the rated maximum | 80 V, or 80% of the rated maximum |
| Temperature | Maximum junction temperature | 85 °C |
| Relative humidity | — | 85% |
| Gate–source voltage | 0 V, or the datasheet minimum if 0 V does not fully block the channel | As for HTRB |
| Duration | At least 1000 h | At least 1000 h |
| Failure criterion | Leakage current rises fivefold | Leakage current rises tenfold |

The 80 V option for H3TRB applies only to devices rated above 100 V. In H3TRB, the voltage is limited so that heat from the leakage current does not dry out the humidity around the device.

<h2 id="gan-thermal-cycling">GaN Thermal Cycling</h2>

I tested GaN devices under repeated thermal cycles.

The devices sit unpowered on a cooling plate whose temperature swings between a minimum and a maximum, dwelling at each extreme long enough for the whole device to reach it. For the GaN devices, a Peltier module under the cooling plate from the [thermal-resistance setup](/research/thermal-characterization/#gan-thermal-resistance) sets the temperature. Each cycle stresses the interfaces between the die, its attach and the package, because they expand by different amounts; measuring the devices at intervals, for example their thermal resistance, shows the damage accumulating.

<figure class="project-blueprint">
  <a href="/images/research/reliability-testing/thermal-cycling-setup.svg" target="_blank" rel="noopener"><img src="/images/research/reliability-testing/thermal-cycling-setup.svg" alt="Thermal cycling setup with devices on a cooling plate above a Peltier module and heat sink, a temperature controller and a thermocouple on the plate, beside a temperature profile alternating between a minimum and a maximum with ramps and dwells" width="760" height="262" loading="lazy"></a>
  <figcaption>Thermal cycling setup and temperature profile.</figcaption>
</figure>

For comparison, AQG 324's thermal shock test for power modules cycles between −40 °C and +125 °C, with dwells of more than 15 minutes, for at least 1000 cycles, and counts a 20% rise in thermal resistance as a failure.

[Power Device Characterization](/research/switching_devices/) · [Back to Research](/research/)
