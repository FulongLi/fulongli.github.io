---
layout: single
title: "PV Battery System"
permalink: /research/pv_systems/
author_profile: true
excerpt: "A modified MPPT algorithm that combines solar power tracking with battery charging limits in one converter controller."
body_class: microgrid-project-page
project_stylesheet: /assets/css/marine-project.css
project_contents: true
---

Early PhD work developed a modified maximum power point tracking (MPPT) algorithm that lets a single PV converter switch smoothly between harvesting the maximum solar power and limiting generation to protect the battery.

<h2 id="overview">Tracking Solar Power Within Battery Limits</h2>

A PV panel delivers its maximum power at one operating point on its current–voltage curve, which moves with irradiance and temperature. An MPPT algorithm such as perturb-and-observe (P&O) finds that point by repeatedly nudging the operating voltage and keeping the direction that increases power.

In an off-grid PV-battery system, maximum power is not always wanted. Once the battery approaches full charge, its charging voltage and current must be limited, so the PV converter must reduce its output below the maximum. The same reduced power can be reached on either side of the maximum power point, and the two choices respond differently when irradiance changes.

<span id="operating-points"></span>
<figure>
  <a href="/images/research/pv-battery/two-operating-points.png" target="_blank" rel="noopener"><img src="/images/research/pv-battery/two-operating-points.png" alt="Left and right reduced-power operating points on either side of the PV maximum power point" width="781" height="494" loading="lazy"></a>
  <figcaption>The same reduced PV power can be reached at a left or a right operating point on either side of the maximum power point.</figcaption>
</figure>

<h2 id="modified-mppt-and-integrated-active-power-control">Modified MPPT with Integrated Power Control</h2>

MPPT and battery charging limits are combined in one modified P&O controller, so that the same Boost converter moves between maximum-power operation and reduced generation during bulk and absorption charging.

<figure>
  <a href="/images/research/pv-battery/system-architecture.png" target="_blank" rel="noopener"><img src="/images/research/pv-battery/system-architecture.png" alt="PV source and boost converter connected to batteries with shared MPPT and charging feedback" width="651" height="371" fetchpriority="high"></a>
  <figcaption>PV source, Boost converter and battery, with PV measurements guiding tracking and battery feedback setting the power limit.</figcaption>
</figure>

At each 100 ms update, the controller samples PV voltage and current and battery charging voltage and current, calculates PV power and updates the perturbation direction from the change in power. If the charging voltage or current exceeds its reference, it redirects the perturbation towards reduced PV power.

The controller was implemented on a **TMS320F28335** DSP driving a **200 W Boost converter**, which charges four 12 V VRLA batteries from a PV emulator. The same power-limitation idea supports the wider [DC microgrid energy management](/research/dcmg/rule-based-ems/).

<span id="pv-integration-into-dc-microgrids"></span>
[A modified MPPT algorithm with integrated active power control for PV-battery systems](https://ieeexplore.ieee.org/document/7884432), ICRERA 2016, pp. 742–746.

[DC Microgrid Control Strategies](/research/dcmg/) · [Back to Research](/research/)
