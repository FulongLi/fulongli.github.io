---
layout: single
title: "Rule-Based EMS and Hierarchical DC Microgrid Operation"
permalink: /research/dcmg/rule-based-ems/
author_profile: true
body_class: microgrid-project-page
project_stylesheet: /assets/css/marine-project.css
project_contents: true
excerpt: "Rule-based power management for a DC microgrid: six-bit bus commands, two-level state machines, battery coordination and PV surplus limitation."
---

My PhD system study brings **passive control, droop coordination and dual-window bus signalling** together under a rule-based energy management system (EMS). I integrated the control layers, defined the operating rules and six-bit signalling scheme, and analysed terminal admittance.

<h2 id="overview">Who Regulates the Bus?</h2>

A DC microgrid must continually decide which converter regulates the bus voltage, when batteries charge or discharge, and what happens when PV generation exceeds demand and storage is full. A rule-based EMS answers these questions with explicit operating rules tied to the system state. Compared with optimisation-based scheduling, it is transparent and simple to implement on the converters' own controllers.

<h2 id="system-configuration">The Microgrid System</h2>

The scheme is designed for a household-scale DC microgrid in which four interface converters share a DC bus held between 45 and 52.5 V. IC1 connects the 220 V AC grid through a rectifier, with a soaking resistor to absorb surplus power; IC2 and IC3 connect two 24 V battery banks; IC4 connects the PV panels with maximum-power-point tracking and power limitation. Electronic and resistive loads draw from the bus.

<figure class="project-blueprint">
  <a href="/images/research/dc-microgrid-control/system-control-configuration.png" target="_blank" rel="noopener"><img src="/images/research/dc-microgrid-control/system-control-configuration.png" alt="DC microgrid with grid, two battery and PV interface converters on a 45 to 52.5 V DC bus with loads; each grid and battery converter has droop, passive stabiliser, voltage and current loops and a state machine driven by bus signal series" width="1947" height="1170" fetchpriority="high"></a>
  <figcaption>System control configuration: grid (IC1), battery (IC2, IC3) and PV (IC4) interface converters on the DC bus, with each converter's control loops and state machine.</figcaption>
</figure>

Each grid and battery converter combines the layers of the hierarchy: droop and the passive stabiliser set the voltage reference, voltage and current loops regulate the converter, and a state machine reads the signal series on the bus and sets the converter's operating role.

<h2 id="operating-rules">Operating Rules and State Machines</h2>

Grid-connected operation gives bus regulation to the grid interface; planned disconnection transfers it to a battery. The power-management logic curtails surplus PV near **51 V**, distinct from the **52.5 V signalling level**. Commands travel through the [dual-window bus signalling method](/research/dcmg/dc-bus-signalling/) as **six bits at 100 ms per bit**, identifying the start, converter state, battery-interface identity, droop or power mode, charge or discharge state and current selection.

Each converter turns received commands into an operating role through a two-level finite-state machine.

<h3 id="signal-state-machine">First Level: Sending and Receiving Signals</h3>

<figure>
  <a href="/images/research/dc-microgrid-control/signal-state-machine.png" target="_blank" rel="noopener"><img src="/images/research/dc-microgrid-control/signal-state-machine.png" alt="First-level signal state machine: initialisation, sending, normal operation and receiving, with transitions based on converter type, signalling voltage and completion flags" width="930" height="555" loading="lazy"></a>
  <figcaption>First-level state machine for signal handling; state III contains the operating-mode controller.</figcaption>
</figure>

- **I — initialisation:** determine the interface role. The grid converter enters normal operation directly; another converter first enters the sending state.
- **II — sending:** transmit the signal sequence, then return to normal operation. Sending can also be triggered during normal operation.
- **III — normal operation:** monitor the bus, run the operating-mode state machine and initiate signalling when another source needs to be switched.
- **IV — receiving:** detect and decode a signal, then return to normal operation, applying current compensation while another interface drives the signal.

<h3 id="mode-state-machine">Second Level: Sleep, Droop and Power Modes</h3>

<figure>
  <a href="/images/research/dc-microgrid-control/mode-state-machine.png" target="_blank" rel="noopener"><img src="/images/research/dc-microgrid-control/mode-state-machine.png" alt="Second-level state machine with sleep, droop and power modes, showing transitions controlled by received state and mode bits" width="720" height="615" loading="lazy"></a>
  <figcaption>Second-level state machine selecting sleep, droop or power mode from the received command bits.</figcaption>
</figure>

In **sleep mode**, the interface monitors the bus and waits for a command. An ON command selects **droop mode**, in which the converter helps regulate the bus, or **power mode**, in which it follows a commanded charge or discharge current while considering battery state of charge. A change in the mode bit switches between them; an OFF command, or a fully charged battery, returns the interface to sleep. The grid interface starts in droop mode, and other converters start in sleep after their signalling exchange.

The EMS defines rule-based operating sequences for source connection, battery coordination and planned handover of bus regulation, rather than optimal long-term scheduling.

[PhD thesis: Control Strategies for Low Voltage DC Microgrids](https://publications.aston.ac.uk/id/eprint/46135/), Chapter 6. · [Dual-window signalling paper](https://ieeexplore.ieee.org/document/8645723)

[DC Microgrid Control Strategies](/research/dcmg/) · [Energy Management Systems](/research/ems/) · [Back to Research](/research/)
