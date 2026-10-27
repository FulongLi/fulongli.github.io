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

<h2 id="signal-state-machine">First Level: Signal Sending and Receiving</h2>

The first state-machine level manages communication and contains the normal-operation controller. The original diagram uses four states:

<figure>
  <a href="/images/research/dc-microgrid-control/signal-state-machine.png" target="_blank" rel="noopener"><img src="/images/research/dc-microgrid-control/signal-state-machine.png" alt="First-level signal state machine: initialisation, sending, normal operation and receiving, with transitions based on converter type, signalling voltage and completion flags" width="930" height="555" loading="lazy"></a>
  <figcaption><strong>Signal-handling state machine.</strong> State III monitors the bus and contains the second-level operating-mode controller. <span class="figure-source">PhD thesis, Figure 6.14, p. 126.</span></figcaption>
</figure>

- **I — initialisation:** determine the interface role. The grid converter enters normal operation directly; another converter first enters the sending state.
- **II — sending:** transmit the signal sequence, then return to normal operation. Sending can also be triggered by a request arising during normal operation.
- **III — normal operation:** monitor the DC bus, run the operating-mode state machine and initiate signalling when another source needs to be switched.
- **IV — receiving:** detect and decode a signal, then return to normal operation. Current compensation is applied during reception while another interface regulates the bus for signalling.

<h2 id="mode-state-machine">Second Level: Sleep, Droop and Power Modes</h2>

The second level sits inside state III. It changes the local converter's operating mode according to the received command and battery condition:

<figure>
  <a href="/images/research/dc-microgrid-control/mode-state-machine.png" target="_blank" rel="noopener"><img src="/images/research/dc-microgrid-control/mode-state-machine.png" alt="Second-level state machine with sleep, droop and power modes, showing transitions controlled by received state and mode bits" width="720" height="615" loading="lazy"></a>
  <figcaption><strong>Operating-mode state machine.</strong> The thesis labels the received signal fields with zero-based indices: <code>ss[1]</code> controls ON/OFF and <code>ss[3]</code> selects droop or power mode. <span class="figure-source">PhD thesis, Figure 6.15, p. 127.</span></figcaption>
</figure>

In **sleep mode**, the interface monitors the bus and waits for a command. An ON command selects **droop mode** when the mode bit is 1, or **power mode** when it is 0. Droop mode allows an assigned converter to regulate the bus; power mode follows the commanded charge or discharge current while considering battery state of charge. A change in the mode bit switches between droop and power; an OFF command returns the interface to sleep. A fully charged battery also leaves power mode for sleep.

The grid interface starts in droop mode. Other converters initially enter sleep after their signalling interaction. The two levels therefore connect the bus-voltage message to the local control mode: receive and decode the command first, then select the appropriate controller and current reference.

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
