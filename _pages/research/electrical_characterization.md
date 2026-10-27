---
layout: single
title: "Electrical Characterization"
permalink: /research/electrical-characterization/
author_profile: true
body_class: device-project-page
project_stylesheet: /assets/css/marine-project.css
project_script: /assets/js/marine-project.js
excerpt: "Power-device test equipment, a jointly built double-pulse test platform for Siemens project work, and switching-waveform analysis."
---

<h2 id="overview">Overview</h2>

Electrical characterization establishes how a power device conducts and switches under defined conditions. My work combines **double-pulse testing (DPT)** for dynamic behaviour with the laboratory equipment used for static current–voltage and capacitance–voltage measurements.

**My contribution:** I worked with a colleague on the Siemens project to build the DPT platform, modify the original test board and carry out device testing. My contribution also included waveform post-processing. The group's DPT report explicitly identifies Fulong and Jixuan as contacts for the MATLAB analysis script.

**Test evidence:** The report documents the physical platform, a measurement campaign spanning voltage, current, gate resistance and temperature, and examples of extracted switching energy. These results show the measurement workflow used by the team.

<figure>
  <a href="/images/research/device-characterization/dpt-test-platform.png" target="_blank" rel="noopener"><img src="/images/research/device-characterization/dpt-test-platform.png" alt="Annotated double-pulse test platform with capacitor bank, laminated busbars, load inductor, gate driver, DUT, hot plate and discharge resistors" width="1500" height="836" fetchpriority="high"></a>
  <figcaption><strong>The double-pulse test platform.</strong> The DC-link capacitor bank supplies the switching event, the inductor sets the test current, and the heated DUT mounting supports temperature-dependent measurements. Original equipment annotations are retained. <span class="figure-source">DPT report, page 20.</span></figcaption>
</figure>

<nav class="project-contents" aria-label="Project contents">
  <p><strong>On this page</strong></p>
  <ul>
    <li><a href="#overview">Overview and contribution</a></li>
    <li><a href="#equipment">Test equipment</a></li>
    <li><a href="#static-measurements">Static I–V and C–V tests</a></li>
    <li><a href="#dpt-platform">DPT platform and test method</a></li>
    <li><a href="#measurement-analysis">Measurement and analysis</a></li>
    <li><a href="#switching-results">Switching results</a></li>
    <li><a href="#outcomes">Outcomes and scope</a></li>
    <li><a href="#resources">Resources and sources</a></li>
  </ul>
</nav>

<h2 id="equipment">Test equipment and its role</h2>

The static analyzer and the DPT rig answer different measurement questions. The analyzer applies controlled voltage or current sweeps. The DPT rig captures a switching event at a selected DC-link voltage and load current.

<div class="project-table-scroll" role="region" aria-label="Electrical characterization equipment" tabindex="0" markdown="1">

| Equipment | Measurement role | Main setup considerations |
|---|---|---|
| Keysight B1505A and EasyEXPERT | Static I–V and C–V characterization | Assign the source/monitor units, set sweep ranges and compliance, and select the correct test configuration |
| N1265A fixture/expander | Connect packaged devices and route measurement resources | Device pinout, force/sense connections and measurement-specific cabling |
| Semi-automated probe station | Contact die-level devices | Chuck positioning, microscope alignment and probe contact |
| DPT power circuit and gate driver | Establish the switching operating point | DC-link voltage, pulse timing, load inductance and gate resistance |
| Tektronix oscilloscope and voltage/current probes | Capture gate voltage, device voltage and current | Bandwidth, sensor range, offsets, probe placement and channel deskew |
| Heated DUT mounting and temperature measurement | Repeat measurements at different temperatures | Temperature stabilisation and recording the temperature with each test point |

</div>

<h2 id="static-measurements">Static I–V and C–V measurements</h2>

The B1505A training materials describe packaged TO-247 SiC MOSFET measurements and measurements on a SiC MOSFET die. The work starts with the physical connections and the source/monitor unit assignments in EasyEXPERT. Forward output curves, reverse conduction, gate-transfer characteristics and capacitances each require an appropriate setup.

<figure>
  <a href="/images/research/device-characterization/packaged-iv-connections.png" target="_blank" rel="noopener"><img src="/images/research/device-characterization/packaged-iv-connections.png" alt="B1505A and N1265A packaged-device I–V diagram showing source and monitor units, resource routing and the device socket connections" width="2013" height="983" loading="lazy"></a>
  <figcaption><strong>Packaged-device measurement connections.</strong> The analyzer, expander and socket form the measurement path. The training material consolidates the connections needed for the laboratory's configuration. <span class="figure-source">Electrical training, slide 17.</span></figcaption>
</figure>

Force and sense connections meet close to the DUT for Kelvin measurements, reducing the contribution of cable resistance. Guarded triaxial connections support low-current measurements. Source compliance and pulsed sweeps help control device stress and self-heating. For capacitance measurements, the C<sub>iss</sub>, C<sub>oss</sub> and C<sub>rss</sub> configurations require separate resource routing.

<details>
  <summary>Probe-station setup and an example output characteristic</summary>
  <p>The on-wafer workflow adds die loading, chuck alignment, micropositioner placement and probe contact under the microscope. The electrical measurement software follows the same principle as the packaged-device tests once the contacts are established.</p>
  <figure>
    <a href="/images/research/device-characterization/wafer-probe-station.jpg" target="_blank" rel="noopener"><img src="/images/research/device-characterization/wafer-probe-station.jpg" alt="Semi-automated wafer probe station and microscope used for die-level characterization" width="4032" height="2268" loading="lazy"></a>
    <figcaption><strong>Die-level measurement equipment.</strong> <span class="figure-source">Electrical training, slide 25.</span></figcaption>
  </figure>
  <figure>
    <a href="/images/research/device-characterization/sic-output-characteristics.png" target="_blank" rel="noopener"><img src="/images/research/device-characterization/sic-output-characteristics.png" alt="Measured SiC MOSFET drain-current versus drain-source-voltage curves at several gate voltages" width="3216" height="2461" loading="lazy"></a>
    <figcaption><strong>Static output-characteristic example.</strong> The training example sweeps drain–source voltage at several gate voltages. <span class="figure-source">Electrical training, slide 20.</span></figcaption>
  </figure>
</details>

<h2 id="dpt-platform">DPT platform and test method</h2>

The Siemens project work used a platform that my colleague and I built together, including modifications to the original test board. The group report shows how the DUT, gate driver, capacitor bank and load inductor were integrated with the measurement equipment. The emphasis was on making the test circuit and its instrumentation work together for repeated device measurements.

The documented rig includes a **2.12 mF capacitor bank**, **laminated busbars**, a **52.8 µH load inductor**, high-voltage contactors and discharge resistors. The platform slide is labelled **750 V, 450 A, 150°C**. The reported measurement matrix uses **25°C, 75°C and 125°C**, so the platform label and the temperatures used in the campaign describe different things.

The first gate pulse ramps the inductor current towards the selected test current. During the pause, current commutates through the freewheeling path. The second pulse provides a turn-on event at approximately that current, followed by another turn-off. For an idealised current ramp, the first-pulse duration is approximately **t₁ = L × I<sub>test</sub> / V<sub>DC</sub>**. Actual timing must account for the test circuit and the recorded waveform.

The report describes more than **450 test points**, covering four voltages, up to nine peak currents, two gate resistances, both devices in each module and two modules, at the three temperatures above. Acquisition was manual, making consistent test settings and data organisation a substantial part of the work.

<h2 id="measurement-analysis">Measurement quality and waveform analysis</h2>

The useful result depends on the measurement chain as well as the power circuit. Voltage and current channels must be aligned before calculating instantaneous power. Probe offset, sensor range and clipping can otherwise produce plausible-looking waveforms with incorrect energy estimates. The report includes both successful captures and examples rejected because of clipping or poor current-sensor sensitivity.

The analysis workflow imports the oscilloscope CSV files, identifies the signals, corrects zero offsets and aligns the channels. It locates the switching events and integrates device voltage multiplied by current over the selected event window:

**E<sub>event</sub> = ∫ v<sub>device</sub>(t) × i<sub>device</sub>(t) dt.**

The MATLAB workflow described in the report extracts **E<sub>on</sub>**, **E<sub>off</sub>**, total event energy, **di/dt**, **dv/dt**, reverse-recovery charge and recovery time, then writes the results to CSV. Integration thresholds and the chosen event window remain part of the measurement definition, especially when comparing IGBT tail current with SiC switching transients.

<h2 id="switching-results">Switching transients and extracted results</h2>

The report's low-side SiC example at **600 V, 150 A, 2.9 Ω gate resistance and 125°C** gives **E<sub>on</sub> = 2.56 mJ** and **E<sub>off</sub> = 1.94 mJ**. The waveforms retain the original voltage/current traces and ringing, making the result traceable to an individual switching event.

<figure>
  <a href="/images/research/device-characterization/sic-switching-transients.png" target="_blank" rel="noopener"><img src="/images/research/device-characterization/sic-switching-transients.png" alt="Turn-on and turn-off voltage and current waveforms for a SiC device at 600 V and 150 A, with event energies of 2.56 and 1.94 millijoules" width="1700" height="636" loading="lazy"></a>
  <figcaption><strong>SiC switching-event example.</strong> Turn-on and turn-off at 125°C with 2.9 Ω gate resistance. <span class="figure-source">DPT report, page 28.</span></figcaption>
</figure>

<figure>
  <a href="/images/research/device-characterization/sic-switching-energy.png" target="_blank" rel="noopener"><img src="/images/research/device-characterization/sic-switching-energy.png" alt="SiC turn-on, turn-off and total switching energy plotted against current at 600 V, 25 degrees Celsius and 2.9 ohms gate resistance" width="1210" height="770" loading="lazy"></a>
  <figcaption><strong>Switching energy over a current sweep.</strong> The plotted event energies show the current dependence at 600 V, 25°C and 2.9 Ω. <span class="figure-source">DPT report, page 29.</span></figcaption>
</figure>

<details>
  <summary>Temperature comparison and interpretation</summary>
  <figure>
    <a href="/images/research/device-characterization/temperature-switching-energy.png" target="_blank" rel="noopener"><img src="/images/research/device-characterization/temperature-switching-energy.png" alt="Original high-side SiC turn-on and turn-off energy curves comparing temperature conditions at 600 V and 2.9 ohms gate resistance" width="1830" height="680" loading="lazy"></a>
    <figcaption><strong>Temperature-dependent switching-energy curves.</strong> The source compares the high-side SiC device at 600 V and 2.9 Ω. Curve colours and axes are preserved. <span class="figure-source">DPT report, page 32.</span></figcaption>
  </figure>
  <p>The report also gives an IGBT example at 540 V, 120 A, 10 Ω and 125°C, with turn-on/off energies of 10.08/9.24 mJ. Its different device, gate resistance and operating point prevent a direct technology ranking against the SiC example above.</p>
</details>

<h2 id="outcomes">Outcomes and engineering scope</h2>

This work connected laboratory equipment and a jointly assembled DPT platform to a repeatable device-characterization workflow. My contribution covered platform construction and board modifications with a colleague, device testing for the Siemens project and waveform analysis. The report records the equipment, operating conditions and examples of the resulting switching data.

The public [DPT Automation repository](https://github.com/FulongLi/DPT_Automation) is a related software resource. The measurement campaign described here used manual acquisition and substantial automated post-processing; the report identifies full acquisition automation as subsequent work.

<h2 id="resources">Resources and figure sources</h2>

The equipment context comes from **Keysight B1505A Power Device Analyzer/Curve Tracer: Training Outcomes**, by **Alejandro Villarruel-Parra and Konstantinos Floros** (30 April 2021, from the supplied filename). Dynamic-test figures and examples come from **Double Pulse Test: Fundamentals, Tips and Tricks**, by **Izgun Gunsal and Gerardo Calderon-Lopez**, dated **12 October 2023**.

Figure captions identify the source slide or PDF page. Select a figure to open the extracted source image. Original plot colours and proportions are preserved.

[Figure sources and extraction details](/files/research/device-characterization/figure-sources.json) · [DPT Automation](https://github.com/FulongLi/DPT_Automation)

[Thermal Characterization](/research/thermal-characterization/) · [Power Device Characterization](/research/switching_devices/) · [Semiconductor Device Modelling](/research/mosfet_ann_modelling/) · [Back to Research](/research/)
