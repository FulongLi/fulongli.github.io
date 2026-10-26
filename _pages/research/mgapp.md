---
layout: single
title: "Marine Fuel-Cell Hybrid Powertrain"
permalink: /research/mgapp/
author_profile: true
excerpt: "Leading the 3 MW marine powertrain project and the subsequent SinO-OFH WP4.1 thermal evaluation."
---

## Overview

How should a marine powertrain share demand between fuel cells and batteries over a working day, and what thermal conditions will its equipment create inside the vessel? My work addressed these questions across two successive projects at Compound Semiconductor Applications Catapult, working with project partners including Auriga Energy and Deregallera.

**My role:** I led the **3 MW marine fuel-cell hybrid powertrain project**, covering system architecture, modelling and energy management. In the subsequent **SinO-OFH project**, I led **Work Package 4.1 (WP4.1), Thermal Evaluation**, focusing on the engine-room temperature and ventilation model.

| Phase | My responsibility | Main output |
|---|---|---|
| 3MW, 2023 | Lead for the whole project | A MATLAB/Simulink modelling and EMS workflow for vessel duty cycles, component sizing and operating scenarios |
| SinO-OFH WP4.1, 2024 | Work package lead | An enclosure thermal model evaluating temperature and fan operation under different climates and heat-source conditions |

## 3 MW Marine Fuel-Cell Hybrid Powertrain

### System Overview

The 3MW project investigated a hybrid marine powertrain combining fuel-cell stacks, battery banks and electric propulsion. The modelling connected equipment characteristics to vessel operating requirements, including propulsion demand and onboard auxiliary demand, referred to as hotel loads.

<figure>
  <a href="/images/research/marine-fuel-cell/3mw-ems-blueprint.png"><img src="/images/research/marine-fuel-cell/3mw-ems-blueprint.png" alt="3 MW marine EMS blueprint linking fuel cells, batteries, electric motors and vessel loads to component models, a central rule-based algorithm and simulation results." width="1156" height="644"></a>
  <figcaption>The project blueprint: component data and vessel duty cycles feed a central EMS and operational model, followed by analysis of power sharing, energy use and component states. Select any figure to view the original image.</figcaption>
</figure>

### Architecture, Models and Operating Strategy

I led the modelling work through successive design updates, using partner data and discussions to revise the system configuration and operating assumptions.

- **System architecture:** assessed a combined arrangement with central battery storage and a distributed arrangement with fuel-cell and battery cabinets. The released configuration represented two propulsion engines, each associated with nine cabinets containing five fuel cells per cabinet.
- **Component models:** developed fuel-cell and battery models, with equivalent propulsion loads and simplified converter representations suitable for system-level scheduling. The workflow tracked fuel-cell electrical behaviour and heat generation alongside battery state of charge, current and voltage.
- **Vessel duty cycles:** converted the HST and BMT operating profiles into daily demand scenarios, including departure manoeuvring, transit to a wind farm, onsite operations and return to port. HST assessment included five variable working-day scenarios and minimum and maximum cases.
- **Central EMS:** implemented a rule-based strategy to allocate demand between fuel cells and batteries, with operating thresholds and charging options. The released rule assigned demand to the fuel cells while they were on, and to the batteries while the fuel cells were off.
- **Design assessment and handover:** compared battery capacities and onshore/offshore charging scenarios, analysed electrical energy and fuel-cell heat, and documented model initialisation, simulation and data processing for reuse.

A key design issue was the interaction between battery size and the operating policy. Earlier scenarios showed that small batteries could not sustain the requested electric manoeuvring and hotel-load support. Revising the dispatch rule reduced battery use and enabled the model to operate with the 110 kWh HST and 280 kWh BMT battery cases. This made the trade-off between electric operating time, storage capacity and fuel-cell operation explicit.

### Representative Simulation Results

The following figures come from the released-model results in the June 2023 project deck. The daily simulations use **15-minute intervals**. The horizontal axes in these original plots show simulation steps, with approximately 96 steps representing 24 hours.

<figure>
  <a href="/images/research/marine-fuel-cell/hst-power-schedule.png"><img src="/images/research/marine-fuel-cell/hst-power-schedule.png" alt="HST Case 2 daily simulation showing battery power, hotel power, fuel-cell electrical and heat power, and propulsion demand." width="1381" height="956" loading="lazy"></a>
  <figcaption>HST Case 2: the power schedule connects the changing propulsion demand with fuel-cell output, battery use and hotel loads. Fuel-cell heat is evaluated alongside electrical output. Source: 3MW overview, slide 58.</figcaption>
</figure>

<figure>
  <a href="/images/research/marine-fuel-cell/hst-battery-state.png"><img src="/images/research/marine-fuel-cell/hst-battery-state.png" alt="HST Case 2 simulation traces of battery state of charge, current and voltage across a daily operating cycle." width="875" height="619" loading="lazy"></a>
  <figcaption>Battery behaviour for the same HST case, showing discharge during assigned operating periods and subsequent charging. The source labels this as a 110 kWh battery case, with 103.680 kWh modelled capacity and 80% initial state of charge. Source: slide 58.</figcaption>
</figure>

The reported energy totals also show how the vessel duty cycle changes both electrical demand and the thermal burden:

| Simulated daily case | Fuel-cell electrical energy | Fuel-cell heat generated |
|---|---:|---:|
| HST minimum-demand case | 10.704 MWh | 12.968 MWh |
| HST Case 2 | 13.721 MWh | 17.188 MWh |
| HST maximum-demand case | 17.190 MWh | 22.623 MWh |
| BMT duty cycle | 13.007 MWh | 16.603 MWh |

*Rounded values reported in the project deck, slides 58, 61 and 62. These are outputs for the specified model scenarios, rather than measured vessel performance.*

<details>
  <summary>Additional results: fuel-cell operation and the BMT duty cycle</summary>
  <figure>
    <a href="/images/research/marine-fuel-cell/hst-fuel-cell-state.png"><img src="/images/research/marine-fuel-cell/hst-fuel-cell-state.png" alt="HST Case 2 fuel-cell voltage, current, flow rates, stack consumption, efficiency and utilisation traces." width="1167" height="737" loading="lazy"></a>
    <figcaption>HST Case 2 fuel-cell operating states, including voltage and current, reactant flows and stack efficiency. Source: slide 58.</figcaption>
  </figure>
  <figure>
    <a href="/images/research/marine-fuel-cell/bmt-power-schedule.png"><img src="/images/research/marine-fuel-cell/bmt-power-schedule.png" alt="BMT daily power schedule showing repeated fuel-cell operation during onsite propulsion demand." width="1381" height="956" loading="lazy"></a>
    <figcaption>BMT duty cycle: repeated onsite demand produces a different fuel-cell operating schedule from the HST case. Source: slide 62.</figcaption>
  </figure>
  <figure>
    <a href="/images/research/marine-fuel-cell/bmt-battery-state.png"><img src="/images/research/marine-fuel-cell/bmt-battery-state.png" alt="BMT battery state of charge, current and voltage for the 280 kWh simulation case." width="875" height="619" loading="lazy"></a>
    <figcaption>BMT battery response for the 280 kWh case, with 276.480 kWh modelled capacity and 80% initial state of charge. Source: slide 62.</figcaption>
  </figure>
</details>

The project delivered a reusable simulation workflow for comparing configurations and operating policies. It also identified the need for more precise hotel-load profiles and further thermal assessment, providing the engineering context for the subsequent work.

## SinO-OFH: WP4.1 Thermal Evaluation

### Engine-Room Temperature and Ventilation

In the next phase, I led WP4.1 to assess the thermal environment around the fuel-cell and converter equipment. The question shifted from daily electrical dispatch to how equipment heat, enclosure construction and external conditions affect engine-room temperature and ventilation requirements.

I developed a room temperature model combining the thermal capacity of the internal air, heat transfer through the enclosure, equipment heat input and fan-driven air exchange. The work progressed from initial requirement capture and sensitivity studies to updated enclosure specifications and climate scenarios.

The updated July 2024 study represented a **6 m × 2.4 m × 3.5 m enclosure**, with revised aluminium wall and door construction and insulation assumptions. It compared **45°C and 60°C equipment surface temperatures** under ambient profiles for the **North Sea, Persian Gulf and Singapore**.

### Representative Thermal Results

<figure>
  <a href="/images/research/marine-fuel-cell/sino-north-sea-60c.png"><img src="/images/research/marine-fuel-cell/sino-north-sea-60c.png" alt="SinO-OFH North Sea thermal simulation with a 60 degree Celsius heat-source surface temperature, showing fan state and indoor and outdoor temperature traces." width="875" height="645" loading="lazy"></a>
  <figcaption>North Sea case with a 60°C equipment surface temperature: the modelled room temperature stays below the 25°C reference and the fan remains off. The original time axis is in seconds. Source: SinO-OFH WP4.1, slide 15.</figcaption>
</figure>

<figure>
  <a href="/images/research/marine-fuel-cell/sino-persian-gulf-60c.png"><img src="/images/research/marine-fuel-cell/sino-persian-gulf-60c.png" alt="SinO-OFH Persian Gulf thermal simulation at a 60 degree Celsius equipment surface temperature, showing fan switching and room temperature above the reference during hot periods." width="875" height="645" loading="lazy"></a>
  <figcaption>Persian Gulf case with the same 60°C equipment surface temperature: the fan switches on during hotter periods, while room temperature rises above the 25°C reference as outdoor temperature increases. Source: slide 15.</figcaption>
</figure>

<details>
  <summary>Comparison: Persian Gulf case with a 45°C equipment surface temperature</summary>
  <figure>
    <a href="/images/research/marine-fuel-cell/sino-persian-gulf-45c.png"><img src="/images/research/marine-fuel-cell/sino-persian-gulf-45c.png" alt="Persian Gulf thermal model at a 45 degree Celsius equipment surface temperature for comparison with the 60 degree Celsius case." width="875" height="645" loading="lazy"></a>
    <figcaption>The 45°C source-temperature case provides a comparison with the updated 60°C scenario. Source: slide 14.</figcaption>
  </figure>
</details>

These simulations illustrate the influence of ambient climate on the enclosure temperature and the limits of ventilation as a means of reaching the reference temperature during hot conditions. WP4.1 provided a model for comparing enclosure and operating assumptions. Its predictions depend on the specified heat sources, insulation and airflow parameters.

## Project Resources

The narrative and figures are drawn from my **3MW overview** and **SinO-OFH WP4.1 progress** presentations. Original plot images are retained, and the [figure source record](/files/research/marine-fuel-cell/figure-sources.json) identifies their slide numbers.

[Related marine EMS code on GitHub](https://github.com/FulongLi/MicrogridEnergyManagementSystermDesign). This is a related public resource, with a narrower scope than the industrial project described here.

## Related Work

[Energy Management Systems](/research/ems/) · [Battery Energy Storage Systems](/research/battery_storage/).

[Back to Research](/research/)
