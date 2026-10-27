---
layout: single
title: "SinO-OFH: WP4.1 Thermal Evaluation"
permalink: /research/sino-ofh/
author_profile: true
body_class: marine-project-page
project_stylesheet: /assets/css/marine-project.css
excerpt: "Enclosure thermal modelling and ventilation behaviour across North Sea, Persian Gulf and Singapore climate scenarios."
---

<h2 id="overview">The Thermal Environment Around a Marine Powertrain</h2>
<span id="sino-ofh-wp41-thermal-evaluation"></span>

Fuel-cell and converter equipment must operate inside an enclosure whose temperature depends on the equipment, construction and outdoor climate. I led **WP4.1, Thermal Evaluation, within SinO-OFH in 2024**, developing a room-temperature model to examine those interactions.

This work followed the [3MW marine powertrain study](/research/3mw-marine-fuel-cell/). My contribution covered requirements, enclosure modelling and scenario assessment, connecting the equipment's thermal conditions to ventilation needs.

<h2 id="model-development">Modelling the Enclosure and Ventilation</h2>

The model represents internal air thermal capacity, heat transfer through the enclosure, equipment heat input and fan-driven air exchange. Sensitivity studies of enclosure resistance and airflow informed an updated **6 m × 2.4 m × 3.5 m** enclosure model.

The climate comparison uses equipment surface temperatures of **45°C and 60°C** and a **25°C room-temperature reference**. The representative plots below show the 60°C case under the updated enclosure assumptions.

<h2 id="climate-scenarios">One Enclosure, Three Climates</h2>

<span id="north-sea"></span>
<figure>
  <a href="/images/research/marine-fuel-cell/sino-north-sea-60c.png" target="_blank" rel="noopener"><img src="/images/research/marine-fuel-cell/sino-north-sea-60c.png" alt="North Sea room temperature and fan state with 60 degree equipment surface temperature" width="875" height="645" fetchpriority="high"></a>
  <figcaption><strong>North Sea: fan off.</strong> Cool ambient conditions keep the simulated room below the 25°C reference. <span class="figure-source">SinO-OFH WP4.1, slide 15.</span></figcaption>
</figure>

<span id="persian-gulf"></span>
<figure>
  <a href="/images/research/marine-fuel-cell/sino-persian-gulf-60c.png" target="_blank" rel="noopener"><img src="/images/research/marine-fuel-cell/sino-persian-gulf-60c.png" alt="Persian Gulf room temperature and fan state with 60 degree equipment surface temperature" width="875" height="645" loading="lazy"></a>
  <figcaption><strong>Persian Gulf: ventilation during hot periods.</strong> The room exceeds the reference as outdoor air becomes hotter. <span class="figure-source">SinO-OFH WP4.1, slide 15.</span></figcaption>
</figure>

<span id="singapore"></span>
<figure>
  <a href="/images/research/marine-fuel-cell/sino-singapore-60c.png" target="_blank" rel="noopener"><img src="/images/research/marine-fuel-cell/sino-singapore-60c.png" alt="Singapore room temperature and continuous fan operation with 60 degree equipment surface temperature" width="875" height="645" loading="lazy"></a>
  <figcaption><strong>Singapore: continuous fan operation.</strong> Sustained warm conditions keep the room above the reference for much of the simulation. <span class="figure-source">SinO-OFH WP4.1, slide 15.</span></figcaption>
</figure>

Both equipment-temperature cases show the same broad difference in ventilation duty between regions. Ambient-air ventilation is constrained by the outdoor temperature; achieving one room-temperature target across these climates requires assessment beyond fan capacity alone.

<h2 id="outcomes">Implications for System Integration</h2>

The study provided a basis for reviewing enclosure construction, insulation and airflow alongside equipment temperature. Its results are conditional on the modelled heat transfer and operating scenarios, and help identify the thermal assumptions that need attention before equipment integration.

[Figure sources](/files/research/marine-fuel-cell/sino-ofh-figure-sources.json) · [3MW Marine Fuel-Cell Project](/research/3mw-marine-fuel-cell/) · [Microgrid Energy Management](/research/mgapp/) · [Back to Research](/research/)
