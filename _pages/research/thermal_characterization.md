---
layout: single
title: "Thermal Characterization"
permalink: /research/thermal-characterization/
author_profile: true
body_class: device-project-page
project_stylesheet: /assets/css/marine-project.css
project_contents: true
excerpt: "Thermal-resistance testing connects electrical temperature sensing, cooling transients and device thermal models."
---

<h2 id="overview">Measuring the Heat Path Through a Power Device</h2>

Thermal characterisation links power dissipation to junction-temperature rise. My work focuses on operating the characterisation equipment and carrying out thermal-resistance testing, providing measurements that support device and converter models.

The laboratory method uses the **PWT2400 power tester**, **T3STER** transient measurement and analysis, and a temperature-controlled cooling circuit. The figures below illustrate the method through the group's training examples.

<h2 id="thermal-transient">From Electrical Temperature Sensing to Thermal Response</h2>

<figure>
  <a href="/images/research/device-characterization/thermal-test-connections.png" target="_blank" rel="noopener"><img src="/images/research/device-characterization/thermal-test-connections.png" alt="Device heating and electrical temperature-sensing circuits connected to a temperature-controlled fixture" width="1144" height="721" fetchpriority="high"></a>
  <figcaption><strong>A controlled heating and cooling experiment.</strong> The same device is heated electrically and then monitored using a small sensing current. <span class="figure-source">Thermal training, slide 18.</span></figcaption>
</figure>

The module training example calibrates forward voltage at 500 mA sensing current from 20°C to 80°C in 5°C steps. With the cooling boundary held constant, an 80 A heating stage establishes the temperature rise before switching to the calibrated sensing current. These are example settings for that device and fixture.

A calibrated temperature-sensitive electrical parameter converts the cooling waveform into junction temperature. The transient response is then evaluated to obtain thermal impedance and a thermal-network representation.

<h2 id="thermal-resistance">Identifying Junction-to-Case Resistance</h2>

The response is evaluated as **Z<sub>th</sub>(t) = ΔT<sub>j</sub>(t) / P**, with the reference boundary defined by the fixture. Paired dry and wet measurements in the module example use 200 s heating and 400 s cooling. Dry and greased mounting interfaces change the later part of the heat path. Comparing their structure functions helps locate the shared junction-to-case boundary.

<figure>
  <a href="/images/research/device-characterization/to247-structure-functions.png" target="_blank" rel="noopener"><img src="/images/research/device-characterization/to247-structure-functions.png" alt="TO-247 device structure functions under dry, greased and additional interface conditions" width="768" height="751" loading="lazy"></a>
  <figcaption><strong>Separating device and interface behaviour.</strong> Changes in mounting conditions reveal where the measured thermal paths diverge. <span class="figure-source">Thermal training, slide 33.</span></figcaption>
</figure>

The training summary reports **0.05 K/W** for a CAS300M17BM2 module diode and **2.58 K/W** for a C3M0280090D SiC MOSFET. These are attributed worked examples from the training report. The separate [SiC ANN-modelling project](/research/semiconductor-device-modelling/static-ann/#thermal-modelling) includes later C2M0080120D measurements.

<h2 id="outcomes">Connecting Measurement and Modelling</h2>

The outputs—transient thermal impedance, thermal resistance and Cauer networks—provide a link between loss calculations and temperature prediction. Useful results depend on calibration, stable cooling conditions and an appropriate sensing current for the device.

Figures and worked examples: <em>Thermal Characterisation: Training Outcomes</em>, Usman Nasir, 25 June 2021. [Figure sources](/files/research/device-characterization/figure-sources.json) · [TIM Automation](https://github.com/FulongLi/TIM_Automation)

[Electrical Characterization](/research/electrical-characterization/) · [Power Device Characterization](/research/switching_devices/) · [Back to Research](/research/)
