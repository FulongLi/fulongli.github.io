---
layout: single
title: "Thermal Characterization"
permalink: /research/thermal-characterization/
author_profile: true
body_class: device-project-page
project_stylesheet: /assets/css/marine-project.css
project_contents: true
mathjax: true
excerpt: "Transient thermal-impedance measurement of SiC power devices, from electrical temperature sensing to the junction-to-case thermal network."
---

I operated the thermal characterisation equipment and carried out transient thermal-impedance measurements of SiC power devices, identifying the junction-to-case thermal path used in device and converter temperature models.

<h2 id="thermal-impedance">How Thermal Impedance Is Measured</h2>

A power device's junction temperature cannot be measured directly, yet it sets the device's losses, lifetime and safe operating limits. Thermal characterisation links the power a device dissipates to the temperature rise at its junction through the transient thermal impedance:

<div class="math-display">\[Z_{th}(t)=\frac{\Delta T_j(t)}{P}.\]</div>

The device itself serves as the thermometer. A temperature-sensitive electrical parameter (TSEP), such as the forward voltage at a small sensing current, is first calibrated against temperature. The device is then heated with a large current until it reaches thermal equilibrium, and switched to the sensing current as it cools; the calibrated TSEP converts the cooling waveform into junction temperature over time.

Repeating the measurement with a dry and a greased mounting interface changes only the outer part of the heat path. Comparing the two structure functions locates where the paths diverge, which identifies the junction-to-case boundary and its thermal resistance R<sub>th,jc</sub>.

<h2 id="measurement">Measurement of a SiC MOSFET</h2>

The measurements use a PWT2400 power tester, the T3STER transient measurement and analysis system and a temperature-controlled cooling circuit. For a C2M0080120D SiC MOSFET, I calibrated the TSEP at a 10 mA sensing current, recorded heating and cooling transients, and compared dry and wet interface conditions. Structure-function analysis then extracts a Cauer thermal network for the device.

The extracted network feeds the thermal branch of the [SiC static ANN model](/research/semiconductor-device-modelling/static-ann/#thermal-modelling) and its converter-level temperature estimates. Automation of the measurement workflow continues in the public [TIM Automation](https://github.com/FulongLi/TIM_Automation) repository.

[Electrical Characterization](/research/electrical-characterization/) · [Power Device Characterization](/research/switching_devices/) · [Back to Research](/research/)
