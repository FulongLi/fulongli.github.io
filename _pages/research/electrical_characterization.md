---
layout: single
title: "Electrical Characterization"
permalink: /research/electrical-characterization/
author_profile: true
body_class: device-project-page
project_stylesheet: /assets/css/marine-project.css
project_contents: true
excerpt: "A jointly built double-pulse test platform, device measurement campaign and waveform analysis for switching-loss data."
---

<h2 id="overview">Turning Switching Waveforms into Device Data</h2>

Electrical characterisation connects device behaviour to converter design. I jointly built a **double-pulse test (DPT) platform**, modified the original board and carried out device testing, with waveform post-processing to extract switching characteristics.

<figure>
  <a href="/images/research/device-characterization/dpt-test-platform.png" target="_blank" rel="noopener"><img src="/images/research/device-characterization/dpt-test-platform.png" alt="Double-pulse test platform with capacitor bank, laminated busbars, load inductor, gate driver and heated device mounting" width="1500" height="836" fetchpriority="high"></a>
  <figcaption><strong>The jointly assembled test platform.</strong> Power circuitry, instrumentation and temperature control establish repeatable switching conditions. <span class="figure-source">DPT report, p. 20.</span></figcaption>
</figure>

<h2 id="dpt-platform">Capturing the Switching Event</h2>

The platform establishes DC-link voltage and load current before capturing turn-on and turn-off transients. The reported campaign spans **more than 450 test points**, varying voltage, current, gate resistance and temperature. Static I–V and C–V measurements with the **Keysight B1505A** complement the dynamic tests.

The first pulse builds current in the load inductor, and the second produces a turn-on event at the chosen current followed by turn-off. The rig includes a 2.12 mF capacitor bank and 52.8 µH inductor. The reported campaign measures at 25°C, 75°C and 125°C, with voltage, current and gate resistance varied across the test matrix.

Post-processing aligns voltage and current channels, corrects offsets and integrates instantaneous power to obtain switching energy, **E = ∫ v(t)i(t) dt**. It also extracts current and voltage slew rates and reverse-recovery quantities. Measurement quality and integration-window selection are central to interpreting the results.

<h2 id="switching-results">Representative Switching Results</h2>

<figure>
  <a href="/images/research/device-characterization/sic-switching-transients.png" target="_blank" rel="noopener"><img src="/images/research/device-characterization/sic-switching-transients.png" alt="SiC turn-on and turn-off waveforms at 600 V, 150 A, 125 degrees Celsius and 2.9 ohm gate resistance" width="1700" height="636" loading="lazy"></a>
  <figcaption><strong>A traceable switching-energy result.</strong> The report gives E<sub>on</sub> = 2.56 mJ and E<sub>off</sub> = 1.94 mJ at this operating point. <span class="figure-source">DPT report, p. 28.</span></figcaption>
</figure>

<figure>
  <a href="/images/research/device-characterization/sic-switching-energy.png" target="_blank" rel="noopener"><img src="/images/research/device-characterization/sic-switching-energy.png" alt="SiC switching energies against current at 600 V, 25 degrees Celsius and 2.9 ohm gate resistance" width="1210" height="770" loading="lazy"></a>
  <figcaption><strong>From individual events to device characteristics.</strong> A current sweep supplies switching-energy data for loss models. <span class="figure-source">DPT report, p. 29.</span></figcaption>
</figure>

<h2 id="outcomes">Supporting Loss and Thermal Modelling</h2>

The work connected platform construction, device testing and analysis into a practical characterisation workflow. Acquisition in this campaign was manual, with automated post-processing. The related public DPT software supports further automation work.

Figures: <em>Double Pulse Test: Fundamentals, Tips and Tricks</em>, Izgun Gunsal and Gerardo Calderon-Lopez, 12 October 2023. [Figure sources](/files/research/device-characterization/figure-sources.json) · [DPT Automation](https://github.com/FulongLi/DPT_Automation)

[Thermal Characterization](/research/thermal-characterization/) · [Device Modelling](/research/mosfet_ann_modelling/) · [Back to Research](/research/)
