---
layout: single
title: "Thermal Evaluation"
permalink: /research/sino-ofh/
author_profile: true
body_class: marine-project-page
project_stylesheet: /assets/css/marine-project.css
project_contents: true
excerpt: "Enclosure thermal modelling and ventilation behaviour across North Sea, Persian Gulf and Singapore climate scenarios."
---

The thermal evaluation, led by the author in 2024, followed the [3 MW marine powertrain study](/research/3mw-marine-fuel-cell/). It developed a room-temperature model of the equipment enclosure and assessed its ventilation needs across three climates, covering the requirements, enclosure modelling and scenario assessment.

<h2 id="overview">The Thermal Environment Around a Marine Powertrain</h2>
<span id="sino-ofh-wp41-thermal-evaluation"></span>

Fuel-cell and converter equipment operates inside an enclosure whose air temperature depends on the heat the equipment releases, how well the walls conduct heat away and the outdoor climate. If the room becomes too hot, equipment performance and lifetime suffer. Ventilation with outdoor air removes heat, but only while the outdoor air is cooler than the room, so the same enclosure can behave very differently in a cold sea and a hot gulf.

<h2 id="model-development">Enclosure and Ventilation Model</h2>

The model represents the thermal capacity of the internal air, heat transfer through the enclosure, equipment heat input and fan-driven air exchange. Sensitivity studies of enclosure resistance and fan capacity tested those parts of the model separately and informed an updated **6 m × 2.4 m × 3.5 m** enclosure with 5 mm aluminium walls and door, insulation, no windows and a 50% air-filled fraction.

The climate scenarios use ambient ranges of 6–14 °C for the North Sea, 14–46.6 °C for the Persian Gulf and 24.3–32.4 °C for Singapore, with equipment surface temperatures of **45 °C and 60 °C** and a **25 °C room-temperature reference**.

<h2 id="climate-scenarios">One Enclosure, Three Climates</h2>
<span id="north-sea"></span>
<span id="persian-gulf"></span>
<span id="singapore"></span>

The plots below show the 60 °C equipment case under the updated enclosure assumptions. In the North Sea, cool ambient air keeps the room below the reference with the fan off.

<figure>
  <a href="/images/research/marine-fuel-cell/sino-north-sea-60c.png" target="_blank" rel="noopener"><img src="/images/research/marine-fuel-cell/sino-north-sea-60c.png" alt="North Sea room temperature and fan state with 60 degree equipment surface temperature" width="875" height="645" fetchpriority="high"></a>
  <figcaption>North Sea: room temperature and fan state with 60 °C equipment; the fan stays off.</figcaption>
</figure>

In the Persian Gulf, the room exceeds the reference as the outdoor air heats up, and the fan runs during hot periods.

<figure>
  <a href="/images/research/marine-fuel-cell/sino-persian-gulf-60c.png" target="_blank" rel="noopener"><img src="/images/research/marine-fuel-cell/sino-persian-gulf-60c.png" alt="Persian Gulf room temperature and fan state with 60 degree equipment surface temperature" width="875" height="645" loading="lazy"></a>
  <figcaption>Persian Gulf: room temperature and fan state with 60 °C equipment; ventilation runs during hot periods.</figcaption>
</figure>

In Singapore, sustained warm conditions keep the room above the reference for much of the day, with the fan running continuously.

<figure>
  <a href="/images/research/marine-fuel-cell/sino-singapore-60c.png" target="_blank" rel="noopener"><img src="/images/research/marine-fuel-cell/sino-singapore-60c.png" alt="Singapore room temperature and continuous fan operation with 60 degree equipment surface temperature" width="875" height="645" loading="lazy"></a>
  <figcaption>Singapore: room temperature and fan state with 60 °C equipment; the fan runs continuously.</figcaption>
</figure>

<h2 id="outcomes">Implications for System Integration</h2>

Both equipment-temperature cases show the same difference in ventilation duty between regions. Because ambient-air ventilation is limited by the outdoor temperature, holding one room-temperature target across these climates needs more than fan capacity alone. The study provided a basis for reviewing enclosure construction, insulation and airflow alongside equipment temperature before integration; its results depend on the modelled heat transfer and operating scenarios.

[3 MW Marine Fuel-Cell Project](/research/3mw-marine-fuel-cell/) · [Microgrid Energy Management](/research/mgapp/) · [Back to Research](/research/)
