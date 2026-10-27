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

<h2 id="overview">The Thermal Environment Around a Marine Powertrain</h2>
<span id="sino-ofh-wp41-thermal-evaluation"></span>

Fuel-cell and converter equipment must operate inside an enclosure whose temperature depends on the equipment, construction and outdoor climate. I led the thermal evaluation in 2024, developing a room-temperature model to examine those interactions.

This work followed the [3MW marine powertrain study](/research/3mw-marine-fuel-cell/). My contribution covered requirements, enclosure modelling and scenario assessment, connecting the equipment's thermal conditions to ventilation needs.

<h2 id="model-development">Modelling the Enclosure and Ventilation</h2>

The model represents internal air thermal capacity, heat transfer through the enclosure, equipment heat input and fan-driven air exchange. Sensitivity studies of enclosure resistance and airflow informed an updated **6 m × 2.4 m × 3.5 m** enclosure model.

The enclosure description uses revised 5 mm aluminium walls and door, insulation assumptions, no windows and a 50% air-filled fraction. The air thermal capacity stores heat; boundary heat exchange and fan-driven airflow determine how the room responds to the equipment and outdoor temperature. Changing enclosure resistance and fan capacity tests those parts of the model separately.

The climate scenarios use ambient ranges of 6–14°C for the North Sea, 14–46.6°C for the Persian Gulf and 24.3–32.4°C for Singapore. These are study inputs, with the same enclosure assessed across the three cases.

The climate comparison uses equipment surface temperatures of **45°C and 60°C** and a **25°C room-temperature reference**. The representative plots below show the 60°C case under the updated enclosure assumptions.

<h2 id="climate-scenarios">One Enclosure, Three Climates</h2>

<span id="north-sea"></span>
<figure>
  <a href="/images/research/marine-fuel-cell/sino-north-sea-60c.png" target="_blank" rel="noopener"><img src="/images/research/marine-fuel-cell/sino-north-sea-60c.png" alt="North Sea room temperature and fan state with 60 degree equipment surface temperature" width="875" height="645" fetchpriority="high"></a>
  <figcaption>North Sea: fan off.</figcaption>
</figure>

Cool ambient conditions keep the simulated room below the 25°C reference.

<span id="persian-gulf"></span>
<figure>
  <a href="/images/research/marine-fuel-cell/sino-persian-gulf-60c.png" target="_blank" rel="noopener"><img src="/images/research/marine-fuel-cell/sino-persian-gulf-60c.png" alt="Persian Gulf room temperature and fan state with 60 degree equipment surface temperature" width="875" height="645" loading="lazy"></a>
  <figcaption>Persian Gulf: ventilation during hot periods.</figcaption>
</figure>

The room exceeds the reference as outdoor air becomes hotter.

<span id="singapore"></span>
<figure>
  <a href="/images/research/marine-fuel-cell/sino-singapore-60c.png" target="_blank" rel="noopener"><img src="/images/research/marine-fuel-cell/sino-singapore-60c.png" alt="Singapore room temperature and continuous fan operation with 60 degree equipment surface temperature" width="875" height="645" loading="lazy"></a>
  <figcaption>Singapore: continuous fan operation.</figcaption>
</figure>

Sustained warm conditions keep the room above the reference for much of the simulation.

Both equipment-temperature cases show the same broad difference in ventilation duty between regions. Ambient-air ventilation is constrained by the outdoor temperature; achieving one room-temperature target across these climates requires assessment beyond fan capacity alone.

<h2 id="outcomes">Implications for System Integration</h2>

The study provided a basis for reviewing enclosure construction, insulation and airflow alongside equipment temperature. Its results are conditional on the modelled heat transfer and operating scenarios, and help identify the thermal assumptions that need attention before equipment integration.

[3MW Marine Fuel-Cell Project](/research/3mw-marine-fuel-cell/) · [Microgrid Energy Management](/research/mgapp/) · [Back to Research](/research/)
