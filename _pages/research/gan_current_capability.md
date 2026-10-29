---
layout: single
title: "GaN Current Capability Test"
permalink: /research/gan-current-capability/
author_profile: true
body_class: device-project-page
project_stylesheet: /assets/css/marine-project.css
project_contents: true
excerpt: "Current capability of a packaged GaN power device, tracked through the junction temperature read from an on-chip sensing resistance."
---

For the P3EP project, I tested how much current a packaged GaN power device can carry, by stepping its drain current and tracking its junction temperature through a temperature-dependent resistance on the chip. The test uses the same packaged device as the [thermal-resistance measurement](/research/thermal-characterization/#gan-thermal-resistance).

## What Limits the Current

A power device's current rating is set less by the semiconductor than by heat: the conduction loss grows with the square of the current, and the junction temperature rises with that loss through the device's thermal resistance. The usable current is therefore the current at which the junction reaches its temperature limit in a given package and cooling arrangement. Measuring it directly needs a reliable reading of junction temperature while the device conducts.

<figure>
  <a href="/images/research/gan-characterization/gan-package.jpg" target="_blank" rel="noopener"><img src="/images/research/gan-characterization/gan-package.jpg" alt="Packaged GaN power device with large drain and source pads, a gate pin marked 4G and numbered sense pins" width="700" height="881" fetchpriority="high"></a>
  <figcaption>The packaged GaN device under test.</figcaption>
</figure>

## Test Method

The device sits in an enclosure with its gate on. A supply steps the drain current, and the on-chip sensing resistance is read alongside it as the junction thermometer.

<figure class="project-blueprint">
  <a href="/images/research/gan-characterization/current-test-circuit.svg" target="_blank" rel="noopener"><img src="/images/research/gan-characterization/current-test-circuit.svg" alt="Current-capability test circuit: a supply steps the drain current through the GaN device with its gate on inside an enclosure while an ohmmeter reads the on-chip sensing resistance; illustrative traces of drain current steps with rests and the junction temperature rising to a higher plateau at each step" width="760" height="262" loading="lazy"></a>
  <figcaption>Current-capability test circuit, with illustrative traces of the stepped drain current and the junction temperature it produces.</figcaption>
</figure>

1. **Calibrate:** map the sensing resistance against temperature, with the gate both off and on, because driving the gate shifts the reading.
2. **Step the current:** drive the drain current through a series of increasing steps, each held long enough for the temperature to settle.
3. **Track the temperature:** convert the sensing resistance to junction temperature with the gate-on calibration at each step.

## Calibration

In both gate states, the sensing resistance rises linearly with temperature; across the two, the readings span about 0.94 to 1.38 kΩ over 25 to 67 °C. The gate-on curve is offset from the gate-off curve, so each state needs its own mapping; the gate-on fit, about 116 °C per kΩ, is the one used during the current test. The gate-off data combine two calibration runs.

<figure>
  <a href="/images/research/gan-characterization/current-calibration.svg" target="_blank" rel="noopener"><img src="/images/research/gan-characterization/current-calibration.svg" alt="Calibration points and linear fits of temperature against sensing resistance with the gate off and with the gate on, the gate-on line offset to lower resistance" width="760" height="420" loading="lazy"></a>
  <figcaption>Calibration of the sensing resistance against temperature with the gate off and on, with linear fits.</figcaption>
</figure>

## Stepped Current Test

During the test, the sensing resistance steps up with each increase in drain current and settles at a higher level, then falls back towards its starting value between steps. Over the sequence it rises from about 940 Ω to about 1150 Ω, which the gate-on calibration places at roughly 25 °C and 50 °C.

<figure>
  <a href="/images/research/gan-characterization/current-test-resistance.png" target="_blank" rel="noopener"><img src="/images/research/gan-characterization/current-test-resistance.png" alt="Sensing resistance over the test, rising in successive steps from about 940 ohms to about 1150 ohms and returning to its baseline between steps" width="1256" height="942" loading="lazy"></a>
  <figcaption>Sensing resistance (Ω) logged through the stepped current test, against logging time.</figcaption>
</figure>

Extending the steps until the junction reaches its limit gives the device's current capability in this package and cooling arrangement, and the same data show how quickly the junction settles after each step.

[Thermal Characterization](/research/thermal-characterization/) · [Power Device Characterization](/research/switching_devices/) · [Back to Research](/research/)
