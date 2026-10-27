---
layout: research
research_area: microgrids
parent:
  title: "Microgrid energy management"
  url: /research/mgapp/
title: "3 MW Marine Fuel-Cell Hybrid Powertrain"
permalink: /research/3mw-marine-fuel-cell/
excerpt: "Technical lead for a 3 MW marine fuel-cell hybrid powertrain study: system architecture, component modelling and a rule-based energy management strategy."
---

## Engineering problem

An offshore vessel's working day mixes high-power transit, low-power manoeuvring, intermittent operation on site and idle periods. A fuel-cell and battery powertrain has to meet that profile while respecting the fuel cells' preferred operating range and the battery's capacity and state-of-charge limits. The battery size that is adequate depends on the dispatch policy: how much of the day the battery is asked to carry, and when it can be recharged. The fuel cells also produce heat comparable to their electrical output, which has to be managed on board.

## Objective and scope

Develop a system model and energy management strategy for the **3 MW Marinised Fuel Cell System and Powertrain** project at CSA Catapult (2023), and use it to assess how the powertrain would operate over representative vessel duty cycles. The scope was system-level modelling and simulation. Converter-level control and hardware were outside it.

## My contribution

I was technical lead for the project, responsible for:

- defining the system architecture and comparing central and distributed arrangements of fuel cells and batteries;
- building the component and vessel load models in MATLAB/Simulink from partner equipment data and operating profiles;
- developing the rule-based energy management strategy; and
- running and documenting the scenario assessment and handing the model over in a form that could be rerun with revised inputs.

## Method

Time-varying propulsion and auxiliary (hotel) load profiles represent each phase of the working day. A central rule-based EMS decides at each step how fuel cells and batteries share the demand. Fuel-cell and battery models then return voltage, current, state of charge, efficiency and generated heat. Running the same model over several duty cycles makes the consequences of battery capacity and dispatch rules explicit.

## Results and evidence

The study showed that the battery capacity required was governed by the dispatch policy. An early policy that asked the batteries to carry electric manoeuvring and auxiliary loads could not be met by the smaller battery case. Revising the rule so that fuel cells supply demand while running, and batteries supply it while the fuel cells are off, made the smaller battery cases workable in the model. The released model produced daily power schedules, component states and fuel-cell heat for several vessel profiles, and the heat results became the starting point for the [SinO-OFH thermal evaluation](/research/sino-ofh/).

Equipment data, vessel profiles and numerical results belong to the project partners and are documented in internal reports; they are not reproduced here.

## Limitations

- Simulation results for assumed and partner-supplied profiles; no measured vessel data.
- The auxiliary load profile was an assumption to be refined.
- Converter behaviour was represented in simplified form; hierarchical converter control was identified as further work.

## Related pages

[SinO-OFH WP4.1 thermal evaluation](/research/sino-ofh/) · [Energy management](/research/ems/) · [Microgrid energy management projects](/research/mgapp/)
