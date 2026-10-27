---
layout: research
research_area: microgrids
title: "Energy Management for DC Microgrids"
permalink: /research/ems/
excerpt: "GAMS-based DC microgrid energy management with battery degradation cost, and how it relates to rule-based and marine energy-management work."
---

## Engineering problem

An energy management system (EMS) decides how generation, storage and grid exchange are scheduled over hours to days. In a DC microgrid the battery frequently holds the bus voltage, so an EMS that treats battery energy as free cycles it more than necessary and shortens its life. The question was how to include battery wear in the scheduling objective without losing the ability to maintain the bus.

## Objective and scope

Formulate and solve a scheduling model for a building DC microgrid that includes a battery degradation cost. This was done as a visiting PhD student at the University of Waterloo (April–July 2019), supervised by Prof. Claudio Cañizares.

## My contribution

I developed the EMS optimisation model in GAMS and improved the battery degradation model within it.

## Results and evidence

The model was applied in simulation to the DC microgrid of a building at Xiamen University. Accounting for the battery degradation cost avoided frequent charging and discharging while maintaining the required DC bus voltage. The method and case study are published at the IEEE PES General Meeting 2020.

## Limitations

The results are simulation results for one building case study. The EMS was not deployed on hardware in this work.

## How this relates to my other energy-management work

| Work | Type of EMS | Where |
|---|---|---|
| Waterloo (this page) | Optimisation-based scheduling with degradation cost | Simulation case study |
| [Rule-based EMS](/research/dcmg/rule-based-ems/) | Finite-state rules carried by DC bus signals | Laboratory DC microgrid (PhD thesis) |
| [3 MW marine powertrain](/research/3mw-marine-fuel-cell/) | Rule-based dispatch of fuel cells and batteries | System simulation (industrial project) |

## References

<ol class="references">
<li>F. Li, C. A. Cañizares, Z. Lin, “<a href="https://doi.org/10.1109/PESGM41954.2020.9281580">Energy Management System for DC Microgrids Considering Battery Degradation</a>,” IEEE PES General Meeting, 2020. <a href="/files/PES2020_slides.pdf">Presentation slides (PDF)</a>.</li>
</ol>
