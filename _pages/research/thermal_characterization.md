---
layout: single
title: "Thermal Characterization"
permalink: /research/thermal-characterization/
author_profile: true
body_class: device-project-page
project_stylesheet: /assets/css/marine-project.css
project_contents: true
mathjax: true
excerpt: "Thermal resistance of a packaged GaN power device from an on-chip temperature-sensing resistance, and transient thermal impedance of a SiC MOSFET."
---

I characterise how heat leaves power devices. For the P3EP project, I built a thermal-resistance measurement for a GaN power device in an embedded package, using a temperature-dependent resistance on the chip as its thermometer; earlier, I measured the transient thermal impedance of a SiC MOSFET.

<h2 id="thermal-impedance">How Thermal Resistance Is Measured</h2>

A power device's junction temperature cannot be measured directly, yet it sets the device's losses, lifetime and safe operating limits. Thermal characterisation links the power a device dissipates to the temperature rise from its junction to a reference point, such as the case or the cooling plate:

<div class="math-display">\[R_{th}=\frac{T_j-T_c}{P},\qquad Z_{th}(t)=\frac{\Delta T_j(t)}{P}.\]</div>

The steady-state thermal resistance <i>R</i><sub>th</sub> describes the heat path once temperatures settle; the transient thermal impedance <i>Z</i><sub>th</sub>(<i>t</i>) describes how it builds up. In both cases the device itself serves as the thermometer: a temperature-sensitive electrical parameter is first calibrated against temperature on a controlled plate, then read while the device dissipates power.

<h2 id="gan-thermal-resistance">Thermal Resistance of a Packaged GaN Device</h2>

The device is a GaN power transistor embedded in a compact package, with drain and source pads, a gate pin and numbered sense pins. A resistance on the chip changes with temperature, which provides the junction-temperature reading.

<figure>
  <a href="/images/research/gan-characterization/gan-package.jpg" target="_blank" rel="noopener"><img src="/images/research/gan-characterization/gan-package.jpg" alt="Packaged GaN power device with large drain and source pads, a gate pin marked 4G and numbered sense pins" width="700" height="881" fetchpriority="high"></a>
  <figcaption>The packaged GaN device used in the thermal-resistance and current-capability tests.</figcaption>
</figure>

### Test Setup

I designed a base cooling plate with six seats, each a 1 mm-deep pocket for the 1.685 mm-thick package, so several devices can be prepared and tested in turn. A Peltier module sets the plate temperature, both for calibration and for temperature cycling. The bench combines a precision power analyser, a dual DC power supply, a data-acquisition unit and a thermocouple logger, recorded from a laptop.

<figure class="half">
  <a href="/images/research/gan-characterization/cooling-plate.png" target="_blank" rel="noopener"><img src="/images/research/gan-characterization/cooling-plate.png" alt="CAD model of the base cooling plate with six device seats and mounting holes" width="1200" height="779" loading="lazy"></a>
  <a href="/images/research/gan-characterization/test-bench.jpg" target="_blank" rel="noopener"><img src="/images/research/gan-characterization/test-bench.jpg" alt="Laboratory bench with the cooling plate, devices under test, power analyser, power supplies, data-acquisition unit and logging computers" width="1400" height="1050" loading="lazy"></a>
  <figcaption>Base cooling plate with six device seats (left) and the measurement bench (right).</figcaption>
</figure>

### Procedure

1. **Calibrate:** with the device unpowered, step the plate temperature and map the on-chip resistance against temperature.
2. **Heat:** switch the device on and apply power between drain and source to heat the chip.
3. **Measure:** at each power level, record the dissipated power, the junction temperature from the calibrated resistance, and the temperature at the bottom of the package.
4. **Recalibrate:** repeat the calibration to confirm that the mapping has not drifted.
5. **Evaluate:** calculate the thermal resistance from the temperature difference and the power.

### Results

The on-chip resistance rises linearly with temperature over the calibration range, giving a mapping of <i>T</i> ≈ 0.107 <i>R</i> − 81.2 °C with <i>R</i> in ohms.

<figure>
  <a href="/images/research/gan-characterization/thermal-calibration.svg" target="_blank" rel="noopener"><img src="/images/research/gan-characterization/thermal-calibration.svg" alt="Calibration points of temperature against sensing resistance from about 20 degrees C at 956 ohms to 61 degrees C at 1332 ohms, with a linear fit" width="760" height="420" loading="lazy"></a>
  <figcaption>Calibration of the on-chip sensing resistance against temperature, with its linear fit.</figcaption>
</figure>

With this mapping, the junction-to-package-bottom thermal resistance of the device came out at **about 0.2 K/W**. The readings at the lowest power levels scatter widely, because their temperature rise is small compared with the resolution of the measurement.

<h2 id="measurement">Transient Thermal Impedance of a SiC MOSFET</h2>

For a C2M0080120D SiC MOSFET, I used a PWT2400 power tester, the T3STER transient measurement system and a temperature-controlled cooling circuit. I calibrated the forward voltage at a 10 mA sensing current, heated the device to equilibrium, and recorded its cooling transient. Repeating the measurement with a dry and a greased mounting interface changes only the outer part of the heat path, so comparing the two structure functions locates the junction-to-case boundary. Structure-function analysis then extracts a Cauer thermal network for the device.

The extracted network feeds the thermal branch of the [SiC static ANN model](/research/semiconductor-device-modelling/static-ann/#thermal-modelling) and its converter-level temperature estimates. Automation of the measurement workflow continues in the public [TIM Automation](https://github.com/FulongLi/TIM_Automation) repository.

[GaN Current Capability Test](/research/gan-current-capability/) · [Electrical Characterization](/research/electrical-characterization/) · [Power Device Characterization](/research/switching_devices/) · [Back to Research](/research/)
