---
layout: single
title: "3 MW Marine Fuel-Cell Hybrid Powertrain"
permalink: /research/mgapp/
author_profile: true
body_class: marine-project-page
project_stylesheet: /assets/css/marine-project.css
project_script: /assets/js/marine-project.js
excerpt: "A complete project case study: leading the 3MW marine powertrain project, followed by SinO-OFH WP4.1 thermal evaluation."
---

## Overview

I led the 3MW marine fuel-cell hybrid powertrain project, developing a system modelling and operating-strategy workflow that connected vessel requirements to fuel-cell and battery behaviour. The subsequent SinO-OFH project extended this work into the equipment’s thermal environment, where I led Work Package 4.1.

The engineering problem covered a complete working day at sea: leaving port, travelling to a wind farm, transferring personnel and equipment, waiting onsite, and returning to shore. Each activity places different demands on the propulsion system. The project examined how fuel cells and batteries could meet those demands, what storage and operating assumptions were needed, and how much heat the fuel cells would generate.

**My role, 3MW (2023):** Lead for the whole project, covering system architecture, component and vessel models, central energy management, scenario assessment and model handover.

**My role, SinO-OFH (2024):** WP4.1 lead, covering thermal evaluation of the engine-room enclosure, equipment heat sources and ventilation across different operating climates.

<nav class="project-contents" aria-label="Project contents">
  <p><strong>On this page</strong></p>
  <ul>
    <li><a href="#system-overview">System overview</a></li>
    <li><a href="#vessel-requirements">Vessel requirements</a></li>
    <li><a href="#design-development">Design development</a></li>
    <li><a href="#released-model">Released model</a></li>
    <li><a href="#hst-results">HST results</a></li>
    <li><a href="#bmt-results">BMT results</a></li>
    <li><a href="#sino-ofh-wp41-thermal-evaluation">SinO-OFH WP4.1</a></li>
    <li><a href="#outcomes">Outcomes</a></li>
  </ul>
</nav>

<h2 id="system-overview">The system and the modelling workflow</h2>
<span id="3-mw-marine-fuel-cell-hybrid-powertrain"></span>

The powertrain combined fuel-cell stacks, battery storage and electric propulsion, together with the vessel’s onboard electrical services. My work at Compound Semiconductor Applications Catapult brought partner equipment information and vessel requirements into a common modelling framework, working with Auriga Energy and Deregallera.

<figure class="project-blueprint">
  <a href="/images/research/marine-fuel-cell/3mw-ems-blueprint.png" target="_blank" rel="noopener" aria-label="View original: 3 MW marine powertrain project blueprint"><img src="/images/research/marine-fuel-cell/3mw-ems-blueprint.png" alt="3 MW marine powertrain project blueprint" width="1156" height="644" fetchpriority="high"></a>
  <figcaption><strong>3 MW marine powertrain project blueprint.</strong> Equipment characteristics and vessel load profiles feed component models and a central rule-based EMS. The simulation produces the power schedule, energy estimates and fuel-cell and battery states. <span class="figure-source">Project blueprint supplied by Fulong Li.</span></figcaption>
</figure>

The blueprint shows the complete workflow: capture the equipment data, build the component representations, define the duty cycle, run the operating strategy, and process the results. Fuel-cell heat is assessed alongside electrical power, connecting the powertrain study to the thermal questions addressed in the second phase.

<h2 id="vessel-requirements">1. Turning vessel operations into model inputs</h2>

A single rated power value could not describe the vessel’s daily requirements. I constructed time-varying propulsion and hotel-load inputs so the model could distinguish high-power transit from manoeuvring, intermittent offshore activity and idle periods. Here, “hotel loads” means onboard auxiliary electrical demand.

The study used two partner-provided operating profiles, referred to in the project materials as **HST** and **BMT**. Propulsion maximum continuous rating (MCR) was **2 × 1,081 kW**. The 3MW project name describes the powertrain project; the propulsion MCR is a separate input to the studied scenarios.

<div class="project-figures">
<figure>
  <a href="/images/research/marine-fuel-cell/hst-vessel.png" target="_blank" rel="noopener" aria-label="View original: HST vessel reference"><img src="/images/research/marine-fuel-cell/hst-vessel.png" alt="HST vessel reference" width="1284" height="985" loading="lazy"></a>
  <figcaption><strong>HST vessel reference.</strong> Vessel arrangement used to frame the first operating profile. <span class="figure-source">3MW, slide 54.</span></figcaption>
</figure>
<figure>
  <a href="/images/research/marine-fuel-cell/bmt-vessel.png" target="_blank" rel="noopener" aria-label="View original: BMT vessel reference"><img src="/images/research/marine-fuel-cell/bmt-vessel.png" alt="BMT vessel reference" width="1884" height="1341" loading="lazy"></a>
  <figcaption><strong>BMT vessel reference.</strong> Vessel arrangement associated with the second operating profile. <span class="figure-source">3MW, slide 54.</span></figcaption>
</figure>
</div>

| Operating activity | HST profile | BMT profile |
|---|---|---|
| Departure and return | Approximately 30 minutes of manoeuvring at around 20% MCR, with electric operation considered | Dockside periods bookend the operating day |
| Transit | Approximately 1–2 hours at around 85% MCR in each direction | Transit at approximately 85% MCR |
| Work at the wind farm | Intermittent manoeuvring and transfer activity between 25% and 100% MCR, with idle periods | Repeated low-load movement and high-load transfer activity |
| Scenario coverage | Five variable working-day profiles plus minimum and maximum cases | A distinct daily profile with repeated onsite switching |

<div class="project-figures">
<figure>
  <a href="/images/research/marine-fuel-cell/hst-duty-cycles.png" target="_blank" rel="noopener" aria-label="View original: HST daily duty-cycle scenarios"><img src="/images/research/marine-fuel-cell/hst-duty-cycles.png" alt="HST daily duty-cycle scenarios" width="1085" height="712" loading="lazy"></a>
  <figcaption><strong>HST daily duty-cycle scenarios.</strong> Five variable operating days and their minimum/maximum reference profiles, expressed as a fraction of propulsion MCR. <span class="figure-source">3MW, slide 55.</span></figcaption>
</figure>
<figure>
  <a href="/images/research/marine-fuel-cell/bmt-duty-cycle.png" target="_blank" rel="noopener" aria-label="View original: BMT operating profile"><img src="/images/research/marine-fuel-cell/bmt-duty-cycle.png" alt="BMT operating profile" width="752" height="452" loading="lazy"></a>
  <figcaption><strong>BMT operating profile.</strong> The second duty cycle introduces repeated offshore demand changes rather than reproducing the HST profile. <span class="figure-source">3MW, slide 56.</span></figcaption>
</figure>
</div>

The workflow supported load data at different time resolutions during development. The final daily scheduling results presented below use **15-minute intervals**, with approximately **96 simulation steps covering 24 hours**. Hotel-load demand remained an assumed profile in this release, so its refinement was one of the identified next steps.

<h2 id="design-development">2. Developing the architecture and resolving the battery constraint</h2>

The model evolved as partner discussions clarified the equipment and intended operating modes. I assessed both a combined arrangement, with fuel cells in parallel and central battery storage, and a distributed cabinet arrangement. Within the distributed model, the fuel-cell grouping changed from six to four and then five fuel cells per cabinet as the design inputs were updated.

The central design difficulty was how much battery energy the operating policy actually required. Early cases asked the batteries to support electric departure manoeuvring and hotel loads. Under those assumptions, the smaller HST battery case could not deliver the requested operating mode. A larger battery alone would also have implications for how storage was distributed and how auxiliary loads were supported.

| Development step | What the study revealed | Engineering response |
|---|---|---|
| Initial architecture and component models | Cabinet connections and equipment data determined how power could flow | Compared central and distributed arrangements, then updated the fuel-cell grouping and battery model |
| Electric manoeuvring and auxiliary-load support | The earlier 110 kWh HST case could not satisfy the requested electric-mode operation under that dispatch policy | Examined the energy budget, usable capacity and the effect of assigning hotel loads to particular cabinets |
| Battery allocation and redundancy discussions | Replicating auxiliary-load support across distributed cabinets could greatly increase required storage | Considered grouping battery banks and separating propulsion and hotel-load responsibilities |
| Charging scenarios | Charging location and timing changed battery use over the day | Evaluated onshore and offshore charging options |
| Revised dispatch rule | Reducing the battery’s assigned operating duty made the smaller battery cases usable in the revised model | Fuel cells supply demand while on; batteries supply demand while fuel cells are off |

The energy-budget discussion quantified the challenge. The assumed daily hotel load was **331.695 kWh**. The electric-operation portions considered in the sizing exercise added **432.400 kWh** for HST and **681.030 kWh** for BMT, giving illustrative usable-energy requirements of **764.095 kWh** and **1,012.725 kWh**, respectively. Applying a 50% depth-of-discharge allowance would double the corresponding nominal capacity. These were sizing exercises for the earlier duty allocation, rather than the installed capacities of the released cases.

**The resulting design decision linked battery capacity to the operating policy.** The June update reduced battery use by changing when it supplied the vessel. The final simulations used the project’s **110 kWh HST** and **280 kWh BMT** battery case labels under that revised rule. This does not imply that the earlier electric-mode requirement was achieved with an unchanged operating strategy.

<h2 id="released-model">3. The released model and operating strategy</h2>

The model release on **22 June 2023** brought the work into a repeatable workflow with three steps: initialise the equipment and load inputs, run the operational model, and process the results. I documented the data import, load-profile updates and simulation procedure so the study could be rerun with revised inputs.

The released configuration represented **two propulsion engines**, each associated with **nine cabinets**, with **five fuel cells per cabinet**. The modelling connected a central rule-based algorithm to fuel-cell and battery models and an equivalent engine-load representation. Simplified converter representations supported the system scheduling study.

<figure>
  <a href="/images/research/marine-fuel-cell/cabinet-simulink-model.png" target="_blank" rel="noopener" aria-label="View original: Component-level operational model"><img src="/images/research/marine-fuel-cell/cabinet-simulink-model.png" alt="Component-level operational model" width="1635" height="618" loading="lazy"></a>
  <figcaption><strong>Component-level operational model.</strong> The MATLAB/Simulink representation connects the fuel-cell and battery behaviour with the equivalent load. The central operating logic activates these component models. The project also included a system-level aggregation layer. <span class="figure-source">3MW, slide 57.</span></figcaption>
</figure>

The outputs covered the fuel-cell operating state, battery state and daily energy use. They included voltage and current, battery state of charge (SoC), reactant-flow and stack-efficiency traces, power supplied to the loads, and the calculated fuel-cell heat. These are simulation results for the documented inputs and operating rules.

<h2 id="hst-results">4. HST results: a working day and its operating envelope</h2>

### Representative day: HST Case 2

HST Case 2 shows how the revised strategy responds to the daily vessel schedule. Fuel-cell output rises with propulsion activity, while battery charging and discharging appear in the periods assigned by the operating rule. The separate hotel-load trace retains the assumed auxiliary demand, and the fuel-cell heat trace shows the thermal load associated with electrical generation.

<figure>
  <a href="/images/research/marine-fuel-cell/hst-power-schedule.png" target="_blank" rel="noopener" aria-label="View original: HST Case 2: daily power schedule"><img src="/images/research/marine-fuel-cell/hst-power-schedule.png" alt="HST Case 2: daily power schedule" width="1381" height="956" loading="lazy"></a>
  <figcaption><strong>HST Case 2: daily power schedule.</strong> Battery power, hotel-load demand, fuel-cell electrical output and heat generation, and total propulsion demand are shown together. The horizontal axis uses 15-minute simulation steps. <span class="figure-source">3MW, slide 58.</span></figcaption>
</figure>

<div class="project-figures">
<figure>
  <a href="/images/research/marine-fuel-cell/hst-battery-state.png" target="_blank" rel="noopener" aria-label="View original: HST Case 2: battery state"><img src="/images/research/marine-fuel-cell/hst-battery-state.png" alt="HST Case 2: battery state" width="875" height="619" loading="lazy"></a>
  <figcaption><strong>HST Case 2: battery state.</strong> SoC, current and voltage show the battery’s discharge and subsequent charging. The source case uses 103.680 kWh modelled capacity, labelled 110 kWh, and an initial SoC of 80%. <span class="figure-source">3MW, slide 58.</span></figcaption>
</figure>
<figure>
  <a href="/images/research/marine-fuel-cell/hst-fuel-cell-state.png" target="_blank" rel="noopener" aria-label="View original: HST Case 2: fuel-cell state"><img src="/images/research/marine-fuel-cell/hst-fuel-cell-state.png" alt="HST Case 2: fuel-cell state" width="1167" height="737" loading="lazy"></a>
  <figcaption><strong>HST Case 2: fuel-cell state.</strong> Voltage, current, reactant flows, stack consumption, efficiency and utilisation show how the fuel-cell operating point changes with the schedule. <span class="figure-source">3MW, slide 58.</span></figcaption>
</figure>
</div>

For this case, the deck reports **13.721 MWh of fuel-cell electrical energy** and **17.188 MWh of generated heat**. The reported propulsion energy is **13.503 MWh**, with **331.695 kWh** of assumed hotel-load demand. The heat result made thermal management a significant part of the system discussion, alongside the electrical operating schedule.

### Minimum and maximum demand

I also evaluated bounding HST cases so that the assessment covered a range of daily operations. The minimum case reports **10.7037 MWh** of fuel-cell electrical energy; the maximum case reports **17.1897 MWh**. Their associated heat totals span **12.9681–22.6230 MWh**. The same model can therefore compare the consequences of different vessel schedules without treating one working day as representative of every mission.

<div class="project-figures">
<figure>
  <a href="/images/research/marine-fuel-cell/hst-min-power.png" target="_blank" rel="noopener" aria-label="View original: HST minimum-demand case"><img src="/images/research/marine-fuel-cell/hst-min-power.png" alt="HST minimum-demand case" width="1381" height="956" loading="lazy"></a>
  <figcaption><strong>HST minimum-demand case.</strong> Daily power and heat traces for the minimum reference profile. <span class="figure-source">3MW, slide 60.</span></figcaption>
</figure>
<figure>
  <a href="/images/research/marine-fuel-cell/hst-max-power.png" target="_blank" rel="noopener" aria-label="View original: HST maximum-demand case"><img src="/images/research/marine-fuel-cell/hst-max-power.png" alt="HST maximum-demand case" width="1381" height="956" loading="lazy"></a>
  <figcaption><strong>HST maximum-demand case.</strong> The maximum reference profile requires more fuel-cell electrical energy and generates more heat over the day. <span class="figure-source">3MW, slide 59.</span></figcaption>
</figure>
</div>

### Results across all seven HST scenarios

The complete scenario summary preserves the values reported in the final deck. All cases use the same assumed hotel-load profile of 331.695 kWh and 80% initial battery SoC.

<div class="project-table-scroll" tabindex="0" role="region" aria-label="All HST daily simulation energy results">
<table>
<caption>HST daily simulation results · 3MW overview, slide 61</caption>
<thead><tr><th scope="col">Scenario</th><th scope="col">Fuel-cell electrical energy<br>(MWh)</th><th scope="col">Propulsion energy<br>(MWh)</th><th scope="col">Fuel-cell heat<br>(MWh)</th></tr></thead>
<tbody>
<tr><th scope="row">Minimum</th><td>10.7037</td><td>10.4857</td><td>12.9681</td></tr>
<tr><th scope="row">Case 1</th><td>14.1426</td><td>13.9247</td><td>17.8045</td></tr>
<tr><th scope="row">Case 2</th><td>13.7210</td><td>13.5030</td><td>17.1880</td></tr>
<tr><th scope="row">Case 3</th><td>13.5002</td><td>13.2823</td><td>16.8453</td></tr>
<tr><th scope="row">Case 4</th><td>13.4940</td><td>13.2760</td><td>16.8580</td></tr>
<tr><th scope="row">Case 5</th><td>13.6102</td><td>13.3920</td><td>16.9931</td></tr>
<tr><th scope="row">Maximum</th><td>17.1897</td><td>16.9717</td><td>22.6230</td></tr>
</tbody></table>
</div>

The deck reports a battery-energy entry of **−20.3625 kWh** for each HST scenario. Its sign convention identifies negative values as charged energy in the onshore-charging case. These source totals describe the individual reported outputs; they should not be read as a reconciled vessel-wide energy balance without checking the model’s aggregation boundaries.

<details class="project-appendix">
<summary>Battery and fuel-cell states for the minimum and maximum HST cases</summary>
<div class="project-figures">
<figure>
  <a href="/images/research/marine-fuel-cell/hst-min-battery.png" target="_blank" rel="noopener" aria-label="View original: HST minimum: battery state"><img src="/images/research/marine-fuel-cell/hst-min-battery.png" alt="HST minimum: battery state" width="875" height="619" loading="lazy"></a>
  <figcaption><strong>HST minimum: battery state.</strong> SoC, current and voltage for the minimum-demand profile. <span class="figure-source">3MW, slide 60.</span></figcaption>
</figure>
<figure>
  <a href="/images/research/marine-fuel-cell/hst-min-fuel-cell.png" target="_blank" rel="noopener" aria-label="View original: HST minimum: fuel-cell state"><img src="/images/research/marine-fuel-cell/hst-min-fuel-cell.png" alt="HST minimum: fuel-cell state" width="1167" height="737" loading="lazy"></a>
  <figcaption><strong>HST minimum: fuel-cell state.</strong> The source reports fuel-cell operation at 600–800 V and 170 A for this case. <span class="figure-source">3MW, slide 60.</span></figcaption>
</figure>
<figure>
  <a href="/images/research/marine-fuel-cell/hst-max-battery.png" target="_blank" rel="noopener" aria-label="View original: HST maximum: battery state"><img src="/images/research/marine-fuel-cell/hst-max-battery.png" alt="HST maximum: battery state" width="875" height="619" loading="lazy"></a>
  <figcaption><strong>HST maximum: battery state.</strong> Battery-state traces for the maximum-demand profile. <span class="figure-source">3MW, slide 59.</span></figcaption>
</figure>
<figure>
  <a href="/images/research/marine-fuel-cell/hst-max-fuel-cell.png" target="_blank" rel="noopener" aria-label="View original: HST maximum: fuel-cell state"><img src="/images/research/marine-fuel-cell/hst-max-fuel-cell.png" alt="HST maximum: fuel-cell state" width="1167" height="737" loading="lazy"></a>
  <figcaption><strong>HST maximum: fuel-cell state.</strong> The source reports fuel-cell operation at 600–800 V and 200 A for this case. <span class="figure-source">3MW, slide 59.</span></figcaption>
</figure>
</div>
</details>

<h2 id="bmt-results">5. BMT results: repeated offshore demand changes</h2>

The BMT case tested a different pattern of operation. Repeated offshore activities create a more intermittent demand profile, with the fuel cells switching between operating periods and the batteries supplying their assigned low-demand periods. Comparing this case with HST demonstrates why the duty cycle is an essential design input.

<figure>
  <a href="/images/research/marine-fuel-cell/bmt-power-schedule.png" target="_blank" rel="noopener" aria-label="View original: BMT: daily power schedule"><img src="/images/research/marine-fuel-cell/bmt-power-schedule.png" alt="BMT: daily power schedule" width="1381" height="956" loading="lazy"></a>
  <figcaption><strong>BMT: daily power schedule.</strong> Repeated onsite demand changes create a different fuel-cell and battery schedule from the HST day. Electrical output, hotel-load demand and generated heat remain visible in the same assessment. <span class="figure-source">3MW, slide 62.</span></figcaption>
</figure>

<div class="project-figures">
<figure>
  <a href="/images/research/marine-fuel-cell/bmt-battery-state.png" target="_blank" rel="noopener" aria-label="View original: BMT: battery state"><img src="/images/research/marine-fuel-cell/bmt-battery-state.png" alt="BMT: battery state" width="875" height="619" loading="lazy"></a>
  <figcaption><strong>BMT: battery state.</strong> The model uses 276.480 kWh capacity, labelled 280 kWh, with 80% initial SoC. The traces show battery use and subsequent charging through the day. <span class="figure-source">3MW, slide 62.</span></figcaption>
</figure>
<figure>
  <a href="/images/research/marine-fuel-cell/bmt-fuel-cell-state.png" target="_blank" rel="noopener" aria-label="View original: BMT: fuel-cell state"><img src="/images/research/marine-fuel-cell/bmt-fuel-cell-state.png" alt="BMT: fuel-cell state" width="1167" height="737" loading="lazy"></a>
  <figcaption><strong>BMT: fuel-cell state.</strong> Voltage, current, reactant flows and efficiency track the repeated operating periods. The source reports 600–800 V and a maximum current of 170 A. <span class="figure-source">3MW, slide 62.</span></figcaption>
</figure>
</div>

| BMT daily output | Reported value |
|---|---:|
| Fuel-cell electrical energy | 13.0071 MWh |
| Propulsion energy | 12.7774 MWh |
| Assumed hotel-load energy | 331.695 kWh |
| Fuel-cell heat generated | 16.6033 MWh |
| Battery-energy entry | −53.631 kWh |

*Source: 3MW overview, slide 62. The negative battery-energy entry denotes charging under the deck’s convention. Battery capacities throughout this case study retain the source’s case labels and model values; no vessel-wide installed capacity is inferred from them.*

<h2 id="sino-ofh-wp41-thermal-evaluation">6. SinO-OFH WP4.1: evaluating the thermal environment</h2>

The first project quantified heat generation alongside the electrical schedule. The next phase examined the thermal environment around the equipment: how would the enclosure, equipment surface temperature, outdoor climate and ventilation affect the room temperature?

**I led WP4.1, Thermal Evaluation, within SinO-OFH.** The work package covered requirement capture, construction of the room-temperature model, sensitivity studies and updated operating-condition simulations. My leadership scope here was this work package.

### Requirements and model development

I represented the enclosure through the thermal capacity of its internal air, heat transfer through its boundaries, heat input from the fuel-cell/converter equipment and fan-driven air exchange. Initial studies varied enclosure thermal resistance and fan capacity to understand the model’s response before applying updated project specifications.

The requirements capture identified the information needed to make the assessment meaningful: room dimensions and construction, insulation properties, equipment surface temperatures, fan airflow, target room temperature and external temperature variation. The model then progressed from an initial enclosure description to the July 2024 update with revised aluminium wall and door construction and rock-wool insulation assumptions.

| Updated model input | Study condition |
|---|---|
| Enclosure dimensions | 6 m × 2.4 m × 3.5 m |
| Walls and door | Revised 5 mm aluminium construction with insulation assumptions |
| Door dimensions | 2 m × 0.8 m |
| Windows | None |
| Air-filled fraction | 50% |
| Equipment surface temperatures | 45°C and 60°C |
| Temperature reference in updated plots | 25°C |
| Climate cases | North Sea, Persian Gulf and Singapore |

The equipment surface temperature is a heat-source input to this room model. It is distinct from the total fuel-cell heat-energy outputs in the 3MW study. The work established the connection between electrical operation and enclosure assessment without assuming that every unit of stack heat entered the room air.

<details class="project-appendix">
<summary>Initial sensitivity studies: enclosure resistance and fan size</summary>
<p>The initial model examples use a 35°C reference. They precede the updated project scenarios below, which use 25°C. The plots explore the effect of thermal resistance and airflow rather than establish final equipment specifications.</p>
<div class="project-figures">
<figure>
  <a href="/images/research/marine-fuel-cell/sino-sensitivity-normal-resistance.png" target="_blank" rel="noopener" aria-label="View original: Fan off: reference enclosure resistance"><img src="/images/research/marine-fuel-cell/sino-sensitivity-normal-resistance.png" alt="Fan off: reference enclosure resistance" width="875" height="646" loading="lazy"></a>
  <figcaption><strong>Fan off: reference enclosure resistance.</strong> The initial example shows room temperature rising above the 35°C reference. <span class="figure-source">SinO-OFH WP4.1, slide 6.</span></figcaption>
</figure>
<figure>
  <a href="/images/research/marine-fuel-cell/sino-sensitivity-high-resistance.png" target="_blank" rel="noopener" aria-label="View original: Fan off: high enclosure resistance"><img src="/images/research/marine-fuel-cell/sino-sensitivity-high-resistance.png" alt="Fan off: high enclosure resistance" width="875" height="646" loading="lazy"></a>
  <figcaption><strong>Fan off: high enclosure resistance.</strong> Greater thermal isolation changes the response to heat input and ambient variation. <span class="figure-source">SinO-OFH WP4.1, slide 6.</span></figcaption>
</figure>
<figure>
  <a href="/images/research/marine-fuel-cell/sino-sensitivity-low-resistance.png" target="_blank" rel="noopener" aria-label="View original: Fan off: low enclosure resistance"><img src="/images/research/marine-fuel-cell/sino-sensitivity-low-resistance.png" alt="Fan off: low enclosure resistance" width="875" height="646" loading="lazy"></a>
  <figcaption><strong>Fan off: low enclosure resistance.</strong> With strong heat exchange, the room temperature closely follows the outdoor profile. <span class="figure-source">SinO-OFH WP4.1, slide 6.</span></figcaption>
</figure>
<figure>
  <a href="/images/research/marine-fuel-cell/sino-sensitivity-small-fan.png" target="_blank" rel="noopener" aria-label="View original: Small-fan example"><img src="/images/research/marine-fuel-cell/sino-sensitivity-small-fan.png" alt="Small-fan example" width="875" height="646" loading="lazy"></a>
  <figcaption><strong>Small-fan example.</strong> The fan runs for most of the example cycle and the room still exceeds the reference during parts of the cycle. <span class="figure-source">SinO-OFH WP4.1, slide 6.</span></figcaption>
</figure>
<figure>
  <a href="/images/research/marine-fuel-cell/sino-sensitivity-medium-fan.png" target="_blank" rel="noopener" aria-label="View original: Medium-fan example"><img src="/images/research/marine-fuel-cell/sino-sensitivity-medium-fan.png" alt="Medium-fan example" width="875" height="646" loading="lazy"></a>
  <figcaption><strong>Medium-fan example.</strong> In this example the model switches the fan as the room approaches the reference. <span class="figure-source">SinO-OFH WP4.1, slide 6.</span></figcaption>
</figure>
<figure>
  <a href="/images/research/marine-fuel-cell/sino-sensitivity-large-fan.png" target="_blank" rel="noopener" aria-label="View original: Large-fan example"><img src="/images/research/marine-fuel-cell/sino-sensitivity-large-fan.png" alt="Large-fan example" width="875" height="646" loading="lazy"></a>
  <figcaption><strong>Large-fan example.</strong> Increased airflow changes the temperature response and fan switching pattern. <span class="figure-source">SinO-OFH WP4.1, slide 6.</span></figcaption>
</figure>
</div>
</details>

### Comparing three climates at 45°C and 60°C equipment temperature

The July update compared both equipment-temperature inputs in three operating regions. The climate ranges below are the scenarios specified in the project deck. The thermal-result plots use **time in seconds**, extending to approximately two days.

| Climate case | Ambient-air range | Seawater range recorded in the study |
|---|---:|---:|
| North Sea | 6–14°C | 3.5–11.4°C |
| Persian Gulf | 14–46.6°C | 19.3–34.4°C |
| Singapore | 24.3–32.4°C | 30.5–31°C |

#### North Sea: cooler ambient conditions

For both heat-source temperatures, the simulated room stays below the 25°C reference and the fan remains off. Increasing the equipment surface temperature raises the room-temperature trace, while the cool external conditions continue to influence the enclosure strongly.

<div class="project-figures">
<figure>
  <a href="/images/research/marine-fuel-cell/sino-north-sea-45c.png" target="_blank" rel="noopener" aria-label="View original: North Sea: 45°C heat source"><img src="/images/research/marine-fuel-cell/sino-north-sea-45c.png" alt="North Sea: 45°C heat source" width="875" height="645" loading="lazy"></a>
  <figcaption><strong>North Sea: 45°C heat source.</strong> Room and outdoor temperatures remain below the 25°C reference; the fan stays off. <span class="figure-source">SinO-OFH WP4.1, slide 14.</span></figcaption>
</figure>
<figure>
  <a href="/images/research/marine-fuel-cell/sino-north-sea-60c.png" target="_blank" rel="noopener" aria-label="View original: North Sea: 60°C heat source"><img src="/images/research/marine-fuel-cell/sino-north-sea-60c.png" alt="North Sea: 60°C heat source" width="875" height="645" loading="lazy"></a>
  <figcaption><strong>North Sea: 60°C heat source.</strong> The warmer equipment changes the room response, which remains below the reference in this scenario. <span class="figure-source">SinO-OFH WP4.1, slide 15.</span></figcaption>
</figure>
</div>

#### Persian Gulf: high ambient temperature

The fan switches on during hot periods in both cases. Room temperature nevertheless rises above the 25°C reference as the outdoor air becomes hotter. This result illustrates the constraint on using ambient-air ventilation to achieve a temperature target during hot-weather operation.

<div class="project-figures">
<figure>
  <a href="/images/research/marine-fuel-cell/sino-persian-gulf-45c.png" target="_blank" rel="noopener" aria-label="View original: Persian Gulf: 45°C heat source"><img src="/images/research/marine-fuel-cell/sino-persian-gulf-45c.png" alt="Persian Gulf: 45°C heat source" width="875" height="645" loading="lazy"></a>
  <figcaption><strong>Persian Gulf: 45°C heat source.</strong> Fan operation follows the hotter part of the ambient cycle, while the room exceeds the reference. <span class="figure-source">SinO-OFH WP4.1, slide 14.</span></figcaption>
</figure>
<figure>
  <a href="/images/research/marine-fuel-cell/sino-persian-gulf-60c.png" target="_blank" rel="noopener" aria-label="View original: Persian Gulf: 60°C heat source"><img src="/images/research/marine-fuel-cell/sino-persian-gulf-60c.png" alt="Persian Gulf: 60°C heat source" width="875" height="645" loading="lazy"></a>
  <figcaption><strong>Persian Gulf: 60°C heat source.</strong> The higher source-temperature case retains the strong influence of the outdoor temperature cycle. <span class="figure-source">SinO-OFH WP4.1, slide 15.</span></figcaption>
</figure>
</div>

#### Singapore: sustained warm conditions

The room exceeds the 25°C reference for much of the simulated period and the fan remains on throughout both plotted cases. This contrasts with the North Sea result, showing that the same enclosure and control target lead to different ventilation duties in different climates.

<div class="project-figures">
<figure>
  <a href="/images/research/marine-fuel-cell/sino-singapore-45c.png" target="_blank" rel="noopener" aria-label="View original: Singapore: 45°C heat source"><img src="/images/research/marine-fuel-cell/sino-singapore-45c.png" alt="Singapore: 45°C heat source" width="875" height="645" loading="lazy"></a>
  <figcaption><strong>Singapore: 45°C heat source.</strong> The fan remains on and the room temperature follows the warm ambient cycle. <span class="figure-source">SinO-OFH WP4.1, slide 14.</span></figcaption>
</figure>
<figure>
  <a href="/images/research/marine-fuel-cell/sino-singapore-60c.png" target="_blank" rel="noopener" aria-label="View original: Singapore: 60°C heat source"><img src="/images/research/marine-fuel-cell/sino-singapore-60c.png" alt="Singapore: 60°C heat source" width="875" height="645" loading="lazy"></a>
  <figcaption><strong>Singapore: 60°C heat source.</strong> The higher equipment-temperature input raises the room response while fan operation remains continuous. <span class="figure-source">SinO-OFH WP4.1, slide 15.</span></figcaption>
</figure>
</div>

The thermal study showed why enclosure construction and the operating environment belong in the assessment alongside the heat-source specification. Ventilation duty differed substantially between the three simulated regions. Temperature predictions remain conditional on the enclosure, insulation, heat-transfer and airflow assumptions used in each model version.

<h2 id="outcomes">7. Project outcomes and my contribution</h2>

The 3MW project delivered a documented modelling workflow that allowed the powertrain to be examined over realistic vessel duty cycles. I led the work across the architecture and model revisions, connected partner inputs to the simulation, and used the results to make the consequences of battery capacity and dispatch policy explicit. The final release covered five HST working days, their operating envelope and the BMT duty cycle, with electrical and thermal outputs available for comparison.

The work also exposed the next engineering questions. The assumed hotel-load profile needed refinement, equipment construction details were needed for deeper thermal assessment, and converter-level hierarchical control remained a development opportunity. The original system-level model provided the basis for those discussions.

In SinO-OFH, I carried the thermal assessment forward as WP4.1 lead, developing an enclosure model and comparing heat-source conditions across three climates. Together, the two phases tell a continuous engineering story: **define the vessel’s operating requirements, test the powertrain architecture and operating policy, quantify the resulting electrical and heat behaviour, then assess the environment in which the equipment must operate.**

<h2 id="project-resources">Project evidence and resources</h2>

The figures are extracted from my **3MW overview** presentation and **SinO-OFH WP4.1 progress** presentation, with the separately supplied system blueprint used as the project overview. Select a figure to open its original image. These materials document simulation and design assessment; they do not establish measured vessel performance.

[Daily simulation results (CSV)](/files/research/marine-fuel-cell/daily-energy-results.csv) · [Figure sources and slide numbers](/files/research/marine-fuel-cell/figure-sources.json) · [Related public marine EMS code](https://github.com/FulongLi/MicrogridEnergyManagementSystermDesign)

The public code is a related resource whose scope is narrower than the industrial project described here.

[Back to Research](/research/)
