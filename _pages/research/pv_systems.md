---
layout: single
title: "PV Battery System"
permalink: /research/pv_systems/
author_profile: true
body_class: microgrid-project-page
project_stylesheet: /assets/css/marine-project.css
project_contents: true
excerpt: "Integrated MPPT and battery charging limits, with experimental comparison of two reduced-power PV operating points."
---

<h2 id="overview">Harvesting Solar Power Within Battery Limits</h2>

An off-grid PV system should extract the available solar power while the battery can accept it, then reduce generation as charging limits are reached. My early PhD work investigated how to make that transition within a single converter controller.

Our **ICRERA 2016 paper** combines maximum power point tracking (MPPT) with battery current and voltage limits using a modified perturb-and-observe (P&O) algorithm.

<h2 id="modified-mppt-and-integrated-active-power-control">One Controller for Tracking and Power Limitation</h2>

<figure>
  <a href="/images/research/pv-battery/system-architecture.png" target="_blank" rel="noopener"><img src="/images/research/pv-battery/system-architecture.png" alt="PV source and boost converter connected to batteries with shared MPPT and charging feedback" width="651" height="371" fetchpriority="high"></a>
  <figcaption><strong>Integrated PV-battery control.</strong> PV measurements guide power tracking; battery current and voltage determine when generation must be curtailed. <span class="figure-source">ICRERA 2016, Figure 1.</span></figcaption>
</figure>

At each update, the controller samples PV voltage/current and battery charging voltage/current, calculates PV power and updates the perturbation direction from the power change. If charging voltage or current exceeds its reference, it redirects the perturbation toward reduced PV power. The implementation uses a fixed 100 ms P&O update interval. This allows the same boost converter to move between maximum-power operation and reduced generation during bulk and absorption charging.

<span id="operating-points"></span>
<figure>
  <a href="/images/research/pv-battery/two-operating-points.png" target="_blank" rel="noopener"><img src="/images/research/pv-battery/two-operating-points.png" alt="Left and right reduced-power operating points on either side of the PV maximum power point" width="781" height="494" loading="lazy"></a>
  <figcaption><strong>Two ways to reduce PV output.</strong> The same power limit can be reached on either side of the maximum power point, with different transient behaviour. <span class="figure-source">ICRERA 2016, Figure 4.</span></figcaption>
</figure>

<h2 id="experimental-validation">Experimental Comparison</h2>

The algorithm ran on a **TMS320F28335 controller** with a **200 W boost converter**, a PV emulator and four 12 V VRLA batteries. Absorption-stage tests used a **53.3 V charging-voltage limit** and compared the two reduced-power operating points under changing irradiance.

<figure>
  <a href="/images/research/pv-battery/dynamic-response-comparison.png" target="_blank" rel="noopener"><img src="/images/research/pv-battery/dynamic-response-comparison.png" alt="Battery-voltage responses showing a shorter response interval for the right-side operating point" width="571" height="494" loading="lazy"></a>
  <figcaption><strong>Faster response on the right branch in the reported test.</strong> The comparison shows t₂ &lt; t₁ after a rapid irradiance increase. <span class="figure-source">ICRERA 2016, Figure 12.</span></figcaption>
</figure>

With irradiance increasing from **600 to 1,000 W/m² in one second**, the reported right-side operating point responds faster while the controller limits battery voltage. The paper does not tabulate numerical settling times or a percentage improvement.

<h2 id="outcomes">From Energy Harvesting to Coordinated Operation</h2>

The study demonstrates feedback-based coordination between available PV power and battery charging constraints. Its evidence is short-term electrical behaviour; long-term battery-life improvement was not measured. The same power-limitation idea supports wider [DC microgrid energy management](/research/dcmg/rule-based-ems/).

<span id="pv-integration-into-dc-microgrids"></span>
[Paper: A modified MPPT algorithm with integrated active power control for PV-battery systems](https://ieeexplore.ieee.org/document/7884432), ICRERA 2016, pp. 742–746. · [Figure sources](/files/research/pv-battery/figure-sources.json)

[Battery Energy Storage](/research/battery_storage/) · [DC Microgrid Control Strategies](/research/dcmg/) · [Back to Research](/research/)
