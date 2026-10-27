---
layout: single
title: "Rule-Based EMS and Hierarchical DC Microgrid Operation"
permalink: /research/dcmg/rule-based-ems/
author_profile: true
body_class: microgrid-project-page
project_stylesheet: /assets/css/marine-project.css
project_contents: true
excerpt: "The thesis system demonstration: rule-based power management, six-bit bus commands, plug-and-play batteries and PV surplus limitation."
---

<h2 id="overview">Coordinating Generation, Storage and Bus Regulation</h2>

A microgrid must decide which converter regulates the bus, when batteries charge or discharge, and what happens when PV generation exceeds demand. My PhD system study brings **passive control, droop coordination and dual-window bus signalling** together under a rule-based EMS.

I integrated the control layers, defined the operating rules and six-bit signalling scheme, analysed terminal admittance, and demonstrated the coordinated sequences on the bench.

<h2 id="operating-rules">Operating Roles Follow the System State</h2>

The experimental system uses a grid interface, two battery interfaces and an emulated PV source. Operating rules assign bus regulation to the grid or a battery and coordinate charging, discharging and PV limitation. A finite-state machine translates received commands into converter roles. Its first level handles initialisation, transmission, monitoring and reception; normal operation then selects sleep, droop or power mode. Droop mode assigns bus regulation, while power mode selects a current reference from the command and battery state.

Messages travel through the [dual-window DBI method](/research/dcmg/dc-bus-signalling/), using **six bits at 100 ms per bit**. The command fields identify the start, converter state, battery-interface identity, droop/power mode, charge/discharge state and current selection. Grid-connected operation gives bus regulation to the grid interface; planned disconnection transfers that responsibility to a battery. The power-management logic curtails surplus PV near **51 V**, distinct from the **52.5 V signalling level**.

<h2 id="experimental-validation">Two Representative System Responses</h2>

<figure>
  <a href="/images/research/dc-microgrid-control/planned-islanding-result.png" target="_blank" rel="noopener"><img src="/images/research/dc-microgrid-control/planned-islanding-result.png" alt="Bus voltage and grid and battery currents during a signalled handover to islanded operation" width="1293" height="852" fetchpriority="high"></a>
  <figcaption><strong>Planned transition to islanded operation.</strong> A command transfers bus regulation to a battery before the grid interface disconnects. <span class="figure-source">PhD thesis, Figure 6.21, p. 134.</span></figcaption>
</figure>

<figure>
  <a href="/images/research/dc-microgrid-control/pv-curtailment-result.png" target="_blank" rel="noopener"><img src="/images/research/dc-microgrid-control/pv-curtailment-result.png" alt="Bus voltage, battery current and PV power during surplus-generation limitation" width="1293" height="783" loading="lazy"></a>
  <figcaption><strong>Power balance when storage is full.</strong> PV generation is reduced when the batteries cannot absorb the surplus. <span class="figure-source">PhD thesis, Figure 6.26, p. 137.</span></figcaption>
</figure>

<h2 id="outcomes">A Demonstration of Coordinated Control</h2>

The experiments show how local stability and bus-borne commands support source connection, battery coordination and planned handover. They demonstrate a rule-based sequence rather than optimal long-term scheduling. Charging stages were shortened with a timer, and the planned transition relies on advance signalling rather than an abrupt grid failure.

[PhD thesis: Control Strategies for Low Voltage DC Microgrids](https://publications.aston.ac.uk/id/eprint/46135/), Chapter 6. · [Dual-window signalling paper](https://ieeexplore.ieee.org/document/8645723) · [Figure sources](/files/research/dc-microgrid-control/figure-sources.json)

[DC Microgrid Control Strategies](/research/dcmg/) · [Energy Management Systems](/research/ems/) · [Back to Research](/research/)
