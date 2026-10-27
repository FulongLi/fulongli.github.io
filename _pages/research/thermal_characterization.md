---
layout: single
title: "Thermal Characterization"
permalink: /research/thermal-characterization/
author_profile: true
body_class: device-project-page
project_stylesheet: /assets/css/marine-project.css
project_script: /assets/js/marine-project.js
excerpt: "Power-device thermal resistance testing with the PWT2400, T3STER and temperature-control equipment: calibration, cooling transients and thermal networks."
---

<h2 id="overview">Overview</h2>

Thermal characterization measures the path that carries heat from a semiconductor junction to its cooling arrangement. The central task is to relate an accessible electrical measurement to **junction temperature**, then use a controlled heating and cooling experiment to obtain **transient thermal impedance** and **thermal resistance**.

**My work:** Operating the device-characterization equipment and carrying out thermal-resistance testing. The emphasis is on understanding the setup, selecting appropriate measurement conditions and interpreting the thermal response for subsequent device and converter modelling.

The equipment and method below are illustrated with the group's 2021 thermal-characterization training materials. Their SiC module and TO-247 case studies provide worked examples of the procedure and its outputs.

<figure class="half">
  <a href="/images/research/device-characterization/power-tester-rack.jpeg" target="_blank" rel="noopener"><img src="/images/research/device-characterization/power-tester-rack.jpeg" alt="PWT2400 power tester rack with measurement equipment, power supplies and control screen" width="770" height="1027" fetchpriority="high"></a>
  <a href="/images/research/device-characterization/temperature-control-unit.jpeg" target="_blank" rel="noopener"><img src="/images/research/device-characterization/temperature-control-unit.jpeg" alt="Julabo Presto W55 temperature-control unit for the thermal characterization cooling circuit" width="518" height="691" loading="lazy"></a>
  <figcaption><strong>Thermal-characterization equipment.</strong> The PWT2400 test rack provides the electrical heating and measurement functions. The Julabo Presto W55 controls the coolant temperature at the test fixture. <span class="figure-source">Thermal training, slides 18 and 13.</span></figcaption>
</figure>

<nav class="project-contents" aria-label="Project contents">
  <p><strong>On this page</strong></p>
  <ul>
    <li><a href="#overview">Overview and contribution</a></li>
    <li><a href="#equipment">Test equipment</a></li>
    <li><a href="#calibration">Temperature calibration</a></li>
    <li><a href="#thermal-transient">Heating and cooling tests</a></li>
    <li><a href="#thermal-resistance">Thermal resistance extraction</a></li>
    <li><a href="#case-studies">Training case studies</a></li>
    <li><a href="#outcomes">Application to device models</a></li>
    <li><a href="#resources">Resources and sources</a></li>
  </ul>
</nav>

<h2 id="equipment">Test equipment and connections</h2>

The setup combines a **PWT2400 16c Power Tester**, **T3STER** transient measurement and analysis, and a **Julabo Presto W55** temperature-control unit. The training rack includes output-stage control units for sensing current and the temperature-sensitive signal, heating-current terminals, DC power supplies, an HMI and the control/safety modules.

<div class="project-table-scroll" role="region" aria-label="Thermal characterization equipment" tabindex="0" markdown="1">

| Equipment or connection | Role in the measurement | What needs to be established |
|---|---|---|
| Power tester and heating-current supplies | Apply electrical power to heat the DUT | Heating current, dissipated power and sufficient heating duration |
| Output-stage control and sensing connections | Apply a small measurement current and acquire the temperature-sensitive signal | Device configuration, sensing current and signal quality |
| T3STER and T3STER Master | Record and process the cooling response | Calibration, transient correction and structure-function evaluation |
| Temperature-control unit and cooled fixture | Set the thermal boundary condition | Stable coolant temperature, mounting and interface condition |
| Thermocouple and temperature inputs | Record the fixture or reference temperature | Sensor position and the temperature represented by each channel |

</div>

<figure>
  <a href="/images/research/device-characterization/thermal-test-connections.png" target="_blank" rel="noopener"><img src="/images/research/device-characterization/thermal-test-connections.png" alt="Thermal test connection diagram showing DUT heating and sensing circuits, heatsink temperature measurement and temperature-control unit" width="1144" height="721" loading="lazy"></a>
  <figcaption><strong>Measurement and cooling connections.</strong> The heating-current path and the electrical temperature-sensing path connect to the same DUT, while the cooled fixture sets the reference thermal condition. <span class="figure-source">Thermal training, slide 18.</span></figcaption>
</figure>

<h2 id="calibration">Calibrating the temperature-sensitive electrical parameter</h2>

The first step is to identify a **temperature-sensitive electrical parameter (TSEP)** suitable for the device and its connection. The training examples use a forward-voltage measurement at a fixed sensing current. Calibration establishes how that voltage changes with temperature before it is used to interpret the cooling transient.

For the SiC module example, the training procedure calibrates from **20°C to 80°C in 5°C steps**, using **500 mA** sensing current. The temperature is allowed to stabilise at each step and the corresponding voltage is recorded. The cooling measurement then uses the same sensing current, so that the recorded voltage can be converted back to temperature through the calibration relation.

<figure>
  <a href="/images/research/device-characterization/tsep-calibration.png" target="_blank" rel="noopener"><img src="/images/research/device-characterization/tsep-calibration.png" alt="Calibration software showing the relation between forward voltage and temperature at 500 milliamps sensing current" width="854" height="487" loading="lazy"></a>
  <figcaption><strong>TSEP calibration example.</strong> Forward voltage is related to temperature at a fixed sensing current. This calibration is the basis of the inferred junction-temperature trace. <span class="figure-source">Thermal training, slides 19–20.</span></figcaption>
</figure>

Sensing current involves a measurement tradeoff. A current that is too small can give a noisy signal, while a large current can heat the device during sensing. The appropriate setting depends on the device and the available temperature sensitivity. It must be established for the test rather than copied unchanged from another device.

<h2 id="thermal-transient">Heating, cooling and transient thermal impedance</h2>

At a fixed cooling condition, the tester applies a larger heating current until the required thermal state is reached. It then switches to the calibrated sensing current and records the cooling response. The module example uses **80 A heating current** and includes a response recorded with the reference temperature at **25°C**.

T3STER Master converts the electrical response to temperature and processes the transient. For a power step and a defined reference boundary, thermal impedance relates temperature rise to heating power:

**Z<sub>th</sub>(t) = ΔT<sub>j</sub>(t) / P.**

The cooling record is evaluated to recover the thermal response associated with the preceding heating. Heating power comes from the electrical conditions during heating. The resulting junction-to-heatsink response includes the device, mounting interface and cooling path represented by that test arrangement.

<figure>
  <a href="/images/research/device-characterization/junction-heatsink-impedance.png" target="_blank" rel="noopener"><img src="/images/research/device-characterization/junction-heatsink-impedance.png" alt="T3STER junction-to-heatsink transient thermal impedance curve on a logarithmic time axis" width="921" height="925" loading="lazy"></a>
  <figcaption><strong>Transient thermal-impedance output.</strong> The evaluated response approaches its steady-state thermal resistance as time increases. The boundary here is junction to heatsink. <span class="figure-source">Thermal training, slide 24.</span></figcaption>
</figure>

<h2 id="thermal-resistance">Junction-to-case thermal resistance</h2>

To identify the device's junction-to-case thermal resistance, the training procedure compares two mounting interfaces: a **dry test** and a **wet test with thermal grease**. Changing the case-to-heatsink interface changes the later part of the heat path. Comparing their structure functions helps identify the boundary of the shared junction-to-case path.

The tests need consistent heating and cooling durations for comparison. In the module example, the paired tests use **200 s heating** and **400 s cooling**. The software then evaluates the structure-function and derivative-delta results to identify the junction-to-case resistance.

<figure class="half">
  <a href="/images/research/device-characterization/to247-dry-test.png" target="_blank" rel="noopener"><img src="/images/research/device-characterization/to247-dry-test.png" alt="TO-247 SiC MOSFET mounted for a dry-interface thermal test" width="570" height="268" loading="lazy"></a>
  <a href="/images/research/device-characterization/to247-wet-test.png" target="_blank" rel="noopener"><img src="/images/research/device-characterization/to247-wet-test.png" alt="TO-247 SiC MOSFET thermal test with grease at the case-to-heatsink interface" width="518" height="395" loading="lazy"></a>
  <figcaption><strong>Dry and wet mounting examples.</strong> The TO-247 case study illustrates the two interface conditions used in the thermal-resistance comparison. <span class="figure-source">Thermal training, slide 31.</span></figcaption>
</figure>

<figure>
  <a href="/images/research/device-characterization/to247-structure-functions.png" target="_blank" rel="noopener"><img src="/images/research/device-characterization/to247-structure-functions.png" alt="Cumulative structure functions comparing dry, wet and additional thermal-interface layers for the TO-247 device" width="768" height="751" loading="lazy"></a>
  <figcaption><strong>Structure functions under different interface conditions.</strong> The curves show where changes in the mounting interface affect the measured heat path. Original labels and colours are retained. <span class="figure-source">Thermal training, slide 33.</span></figcaption>
</figure>

<h2 id="case-studies">Worked examples from the training materials</h2>

The training report demonstrates the complete procedure on a **CAS300M17BM2 module diode** and a **C3M0280090D SiC MOSFET in a TO-247 package**. The summary records the following junction-to-case resistances:

<div class="project-table-scroll" role="region" aria-label="Thermal training case-study results" tabindex="0" markdown="1">

| Training example | Manufacturer value quoted in the training | Experimental value selected in the training |
|---|---:|---:|
| CAS300M17BM2 module diode | 0.06 K/W | 0.05 K/W |
| C3M0280090D SiC MOSFET | 2.3 K/W | 2.58 K/W |

</div>

*Source: thermal training, slide 35. These are the report's worked-example values, including its manufacturer references. They are distinct from the later C2M0080120D measurements on the [Semiconductor Device Modelling page](/research/mosfet_ann_modelling/#thermal-modelling).*

<details>
  <summary>Extraction choices and measurement sensitivity</summary>
  <p>For the module example, the structure-delta and derivative-delta methods give 0.029 K/W and 0.05 K/W respectively. The training selects 0.05 K/W. The TO-247 example gives 2.58 K/W from structure delta and 2.52 K/W from derivative delta, with 2.58 K/W retained in the summary. The extraction method therefore matters when quoting a result.</p>
  <p>The training also compares heating duration and sensing current. Short heating can give an insufficient temperature change, and low sensing current can produce a noisy response. Stable thermal conditions and a usable calibration are necessary before interpreting the extracted network.</p>
</details>

<h2 id="outcomes">Application to device and converter models</h2>

The equipment workflow produces a calibrated temperature response, transient thermal impedance and an identified junction-to-case resistance. The training examples also extract **six-stage Cauer thermal networks**, connecting the measurement to an RC representation that can be used in thermal simulation.

For my device-characterization work, the practical focus is operating this equipment and obtaining interpretable thermal-resistance measurements. These measurements support temperature estimation when combined with electrical loss calculations. The later [ANN-based SiC device-modelling project](/research/mosfet_ann_modelling/#thermal-modelling) provides a separate example of measured thermal behaviour entering a device-modelling workflow.

The related [TIM Automation repository](https://github.com/FulongLi/TIM_Automation) is retained as a software resource alongside the laboratory method.

<h2 id="resources">Resources and figure sources</h2>

Equipment photographs, procedures and worked examples come from **Thermal Characterisation: Training Outcomes**, by **Usman Nasir** (25 June 2021, from the supplied filename). The report documents the group's equipment and training cases. The numerical examples above retain that attribution.

Figure captions identify the source slide. Select a figure to open its original extracted image. The source photographs, diagram colours and plot proportions are preserved.

[Figure sources and extraction details](/files/research/device-characterization/figure-sources.json) · [TIM Automation](https://github.com/FulongLi/TIM_Automation)

[Electrical Characterization](/research/electrical-characterization/) · [Power Device Characterization](/research/switching_devices/) · [Semiconductor Device Modelling](/research/mosfet_ann_modelling/) · [Back to Research](/research/)
