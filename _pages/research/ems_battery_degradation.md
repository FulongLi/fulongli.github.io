---
layout: single
title: "EMS for DC Microgrids Considering Battery Degradation"
permalink: /research/mgapp/battery-degradation-ems/
author_profile: true
excerpt: "An optimisation-based energy management system for DC microgrids that prices battery wear alongside grid electricity, so the battery can hold the bus voltage without excessive cycling."
body_class: microgrid-project-page
project_stylesheet: /assets/css/marine-project.css
project_contents: true
mathjax: true
---

Research at the University of Waterloo developed an optimisation-based energy management system (EMS) for DC microgrids that prices battery wear alongside grid electricity. The battery holds the DC bus voltage, and the EMS schedules it so that it is not charged and discharged more than the system needs.

## Why Battery Degradation Matters in DC Microgrids

A DC microgrid needs at least one source that regulates its bus voltage. A grid-connected converter can do this while the grid is available, but a battery energy storage system can hold the bus in both grid-connected and islanded operation, which removes the need for a seamless switch between the two modes. Energy management is also simpler than in AC microgrids: with no frequency or reactive power, it reduces to scheduling active power on a two-wire system.

Using the battery this way has a cost. Every charge and discharge cycle wears it, and deep cycles wear it fastest, so an EMS that only minimises electricity cost will cycle the battery heavily and shorten its life. The EMS sits at the top of the [hierarchical control scheme](/research/dcmg/), on a time scale of minutes to days, above the converter and bus-voltage control layers.

## Degradation Cost Model

For a lead-acid battery, the number of cycles to failure falls steeply as the depth of discharge (DoD) increases, while the total energy throughput over the battery's life changes little. Deep discharges therefore consume the battery's life faster for the same energy delivered.

<figure>
  <a href="/images/research/battery-degradation-ems/lead-acid-cycle-life.png" target="_blank" rel="noopener"><img src="/images/research/battery-degradation-ems/lead-acid-cycle-life.png" alt="Cycles to failure falling from about 3,800 at 10% depth of discharge to about 550 at 100%, with calculated lifetime throughput between about 50,000 and 83,000 kWh" width="734" height="429" fetchpriority="high"></a>
  <figcaption>Cycles to failure and lifetime energy throughput against depth of discharge for a lead-acid battery.</figcaption>
</figure>

The degradation cost per kWh of throughput divides the replacement cost by the energy the battery can deliver over its life. With battery unit cost <i>C</i><sub>bu</sub> in $/kWh and cycle life ℒ<sub>b</sub>(DoD):

<div class="math-display">\[\varphi=\frac{C_{rp}}{E_{lc}}=\frac{C_{bu}}{2\,\mathcal{L}_b(\mathrm{DoD})\,\mathrm{DoD}},\]</div>

<div class="math-display">\[\mathcal{C}_{dg}=\sum_{\Delta t}\varphi\,\bigl(P^{dc}_{bat,t}+P^{c}_{bat,t}\bigr)\Delta t,\]</div>

where <i>P</i><sup>dc</sup><sub>bat,t</sub> and <i>P</i><sup>c</sup><sub>bat,t</sub> are the battery's discharging and charging power. Any charging or discharging adds to the cost, so reducing it means using the battery less.

## EMS Formulation

The battery's state of charge follows its charging and discharging power, with efficiencies η<sub>c</sub> and η<sub>d</sub>, and stays between its limits:

<div class="math-display">\[\mathit{SoC}_{t}=\mathit{SoC}_{t-1}+\Bigl(\eta_c P^{c}_{bat,t-1}-\frac{P^{dc}_{bat,t-1}}{\eta_d}\Bigr)\Delta t,\]</div>

<div class="math-display">\[\mathit{SoC}_{\min}\le \mathit{SoC}_{t}\le \mathit{SoC}_{\max}.\]</div>

Charging and discharging powers are bounded, and neither the battery nor the grid connection may charge and discharge at the same time. With no reactive power, the remaining network constraint is the active power balance on the bus:

<div class="math-display">\[P^{dc}_{bat,t}+P^{dc}_{g,t}+P_{PV,t}=P_{load,t}+P^{c}_{bat,t}+P^{c}_{g,t},\]</div>

where the load <i>P</i><sub>load,t</sub> is the sum of the EV charging, air-conditioning and LED lighting demand.

The objective weighs the cost of grid electricity at price ξ<sup>dc</sup><sub>g,t</sub> against the battery degradation cost:

<div class="math-display">\[\mathcal{C}=\min\Bigl[\alpha\sum_{\Delta t}\xi^{dc}_{g,t}P^{dc}_{g,t}\,\Delta t+(1-\alpha)\,\mathcal{C}_{dg}\Bigr].\]</div>

The weighting factor α sets how grid power and battery throughput compete. At α = 1 only the electricity bill counts and the battery is used freely; lowering α gives battery wear more weight, so the schedule leans on the grid and keeps the battery's state of charge steadier.

## Test Microgrid

The EMS is formulated for a model of the DC microgrid of a building at Xiamen University. A 380 V DC bus connects PV generation, a lead-acid battery bank that maintains the bus voltage, and a bidirectional AC/DC converter to the grid, with LED lighting, an EV charging station and air conditioning as loads.

<figure>
  <a href="/images/research/battery-degradation-ems/dc-test-microgrid.png" target="_blank" rel="noopener"><img src="/images/research/battery-degradation-ems/dc-test-microgrid.png" alt="380 V DC test microgrid with a 160 kW grid AC/DC converter, 150 kW PV, a 200 Ah battery, and 20 kW LED, 40 kW EV and 30 kW air-conditioning loads" width="755" height="435" loading="lazy"></a>
  <figcaption>DC test microgrid based on the Xiamen University DC building.</figcaption>
</figure>

| Element | Value |
| --- | --- |
| Generation and grid | 150 kW PV; 160 kW bidirectional AC/DC grid converter |
| Battery | 200 Ah, 336 V lead-acid bank; ±67.2 kW; replacement cost 200 $/kWh |
| Battery limits | Initial SoC 80%; DoD 60%, so SoC between 40% and 95%; η<sub>c</sub> = 95%, η<sub>d</sub> = 90% |
| Loads | 20 kW LED lighting, 40 kW EV charging, 30 kW air conditioning |
| Electricity price | 0.077 $/kWh from 8 am to 10 pm, 0.044 $/kWh otherwise |
| Dispatch interval | 15 minutes |

The PV profile represents a summer day, the EV charging station is used after working hours, and the air conditioning cycles intermittently during working hours.

<figure class="half">
  <a href="/images/research/battery-degradation-ems/pv-generation-profile.png" target="_blank" rel="noopener"><img src="/images/research/battery-degradation-ems/pv-generation-profile.png" alt="Summer PV generation over a day, peaking at about 80 kW around midday" width="751" height="383" loading="lazy"></a>
  <a href="/images/research/battery-degradation-ems/daily-load-profiles.png" target="_blank" rel="noopener"><img src="/images/research/battery-degradation-ems/daily-load-profiles.png" alt="Daily load profiles of the intermittent air conditioning, the evening EV charging and the LED lighting" width="748" height="362" loading="lazy"></a>
  <figcaption>Summer PV generation (left) and daily load profiles of air conditioning, EV charging and LED lighting (right).</figcaption>
</figure>

## Simulation Results

Solving the EMS for different weighting factors shows how pricing battery wear changes the schedule. As α decreases and the degradation cost carries more weight, the battery's state of charge flattens out and its charging and discharging power tends to zero, while the battery still holds the DC bus voltage.

<figure class="half">
  <a href="/images/research/battery-degradation-ems/soc-alpha.png" target="_blank" rel="noopener"><img src="/images/research/battery-degradation-ems/soc-alpha.png" alt="Battery state of charge over a day for alpha from 1 to 0.8, swinging between 40% and 95% at alpha of 1 and staying flat at 80% at alpha of 0.8" width="746" height="415" loading="lazy"></a>
  <a href="/images/research/battery-degradation-ems/battery-power-alpha.png" target="_blank" rel="noopener"><img src="/images/research/battery-degradation-ems/battery-power-alpha.png" alt="Battery power over a day for alpha from 1 to 0.8, with large charge and discharge swings at alpha of 1 and near-zero power at alpha of 0.8" width="746" height="417" loading="lazy"></a>
  <figcaption>Battery state of charge (left) and power (right) over the day for weighting factors from α = 1 to 0.8.</figcaption>
</figure>

The dispatch for two weightings shows the difference. At α = 0.95, part of the surplus PV around midday charges the battery and the battery supports the evening load. At α = 0.8, the battery is barely used: the grid absorbs the PV surplus and supplies the evening EV and air-conditioning demand, so the battery cycles far less and lasts longer.

<figure class="half">
  <a href="/images/research/battery-degradation-ems/dispatch-alpha-095.png" target="_blank" rel="noopener"><img src="/images/research/battery-degradation-ems/dispatch-alpha-095.png" alt="Optimal dispatch at alpha of 0.95 with PV, total load, battery power and grid power over a day" width="754" height="418" loading="lazy"></a>
  <a href="/images/research/battery-degradation-ems/dispatch-alpha-080.png" target="_blank" rel="noopener"><img src="/images/research/battery-degradation-ems/dispatch-alpha-080.png" alt="Optimal dispatch at alpha of 0.8 with PV, total load, near-zero battery power and grid power over a day" width="756" height="419" loading="lazy"></a>
  <figcaption>Optimal dispatch of PV, load, battery and grid power for α = 0.95 (left) and α = 0.8 (right).</figcaption>
</figure>

The weighting factor therefore gives the operator a direct handle on how much the battery contributes to the microgrid against how long it lasts. The air-conditioning and EV loads were treated as non-dispatchable; making them controllable is a natural extension of the model.

[Energy Management System for DC Microgrids Considering Battery Degradation](https://ieeexplore.ieee.org/document/9281580), IEEE PES General Meeting, 2020 · [Accepted manuscript](https://repository.lboro.ac.uk/articles/conference_contribution/Energy_management_system_for_DC_microgrids_considering_battery_degradation/13619312)

[Microgrid Energy Management](/research/mgapp/) · [Energy Management Systems](/research/ems/) · [Back to Research](/research/)
