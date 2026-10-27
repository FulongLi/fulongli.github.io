---
layout: research
research_area: microgrids
parent:
  title: "DC microgrid control"
  url: /research/dcmg/
title: "Rule-Based EMS and Hierarchical DC Microgrid Operation"
permalink: /research/dcmg/rule-based-ems/
excerpt: "The thesis system demonstration: rule-based power management, six-bit bus commands, plug-and-play batteries and PV surplus limitation."
---

<h2 id="overview">Bringing the Three Control Layers Together</h2>

**Chapter 6 of my PhD thesis** combines passive converter control, droop-based bus coordination and dual-window DBI signalling in a household-scale DC microgrid study. Operating rules and a finite-state machine determine which converter regulates the bus, which battery charges or discharges, and when PV generation must be curtailed.

**My contribution:** I integrated the three control layers, defined the operating rules and six-bit signalling scheme, analysed terminal admittance for the operating modes, and demonstrated source connection, battery coordination, planned grid/island transitions and surplus-PV limitation on the bench.

<nav class="project-contents" aria-label="Project contents">
  <p><strong>On this page</strong></p>
  <ul>
    <li><a href="#overview">System overview</a></li>
    <li><a href="#operating-rules">Operating rules</a></li>
    <li><a href="#six-bit-commands">Six-bit commands</a></li>
    <li><a href="#state-machine">Converter state machine</a></li>
    <li><a href="#experimental-validation">Experimental evidence</a></li>
    <li><a href="#project-resources">Sources and related work</a></li>
  </ul>
</nav>

<h2 id="operating-rules">Rules for Grid-Connected and Islanded Operation</h2>

The bench uses four interface converters: **IC1** represents the grid connection, **IC2 and IC3** connect battery banks, and **IC4** interfaces emulated PV generation. Electronic and resistive loads provide demand. Grid power export is emulated using a resistor to absorb surplus power.

<div class="project-table-scroll" role="region" aria-label="Thesis rule-based power management" tabindex="0" markdown="1">

| Operating condition | Rule in the thesis demonstration |
|---|---|
| Grid connected | IC1 regulates the bus; storage receives charging commands, with the first connected module given priority and delays between interactions |
| Surplus PV while grid connected | Surplus power can flow to the emulated grid interface |
| Islanded load support | The assigned battery regulates the bus and can command another storage interface to supply the load |
| Surplus PV while islanded | The bus-regulating battery has priority to absorb surplus; another available battery can then be enabled |
| Storage fully charged while islanded | Limit PV output to maintain power balance |
| Planned grid disconnection/reconnection | Signal the transfer of bus-regulation responsibility between grid and battery interfaces |

</div>

These rules form a **rule-based EMS** for the study. Chapter 6 leaves optimisation of system operation outside its scope. Later battery-degradation-aware energy management is linked under [Energy Management Systems](/research/ems/).

<h2 id="six-bit-commands">Six-Bit Commands Over the DC Bus</h2>

The [dual-window DBI method](/research/dcmg/dc-bus-signalling/) carries the commands. Table 6-1 assigns the bits as follows; the sender and system state determine the meaning of the complete sequence.

<div class="project-table-scroll" role="region" aria-label="Six-bit command fields from thesis Table 6-1" tabindex="0" markdown="1">

| Bit | Function | Encoding in the demonstration |
|---|---|---|
| 1 | Start | 1 marks the beginning of signalling |
| 2 | Converter state | 1: ON; 0: OFF |
| 3 | Battery-interface identity | 0: IC2; 1: IC3 |
| 4 | Operating mode | 1: droop mode; 0: power mode |
| 5 | Charging/discharging state | 1: discharge; 0: charge |
| 6 | Current selection | 0: 1 A; 1: 2 A |

</div>

The experiment uses a **50 V upper working reference**, **52.5 V signalling level** and **100 ms bit duration**. The example **110100** identifies IC2 as ON in droop mode; Appendix A6 gives the sender-dependent command explanations.

<h2 id="state-machine">From a Received Signal to a Converter State</h2>

The first state-machine level handles initialisation, transmission, normal monitoring and reception. Within normal operation, the second level selects **sleep mode**, **droop mode** or **power mode**. Power mode uses the command and battery state to determine the current reference; droop mode gives a converter its bus-regulation role.

For islanded PV operation, the modified MPPT algorithm monitors bus voltage. If storage cannot absorb the surplus and the bus reaches the study's **51 V power-limitation threshold**, the PV operating point moves away from maximum power. The 51 V limit belongs to surplus-power logic; the separate 52.5 V level identifies signalling.

<h2 id="experimental-validation">What the Laboratory Demonstration Shows</h2>

The experiment exercises battery plug-in, command exchange, changing PV generation and load demand, and grid/island transitions. Passive stabilisation remains part of local control, with terminal-admittance and minor-loop-gain analysis supporting the studied modes.

<figure>
  <a href="/images/research/dc-microgrid-control/planned-islanding-result.png" target="_blank" rel="noopener" aria-label="View original: planned grid-to-island transition"><img src="/images/research/dc-microgrid-control/planned-islanding-result.png" alt="Original bus voltage and grid and battery current traces during a signalled handover from grid-connected to islanded operation" width="1293" height="852" loading="lazy"></a>
  <figcaption><strong>Planned transfer to islanded operation.</strong> A signal assigns bus regulation to IC2 before IC1 is mechanically disconnected. The trace includes droop-based current sharing. <span class="figure-source">PhD thesis, Figure 6.21, p. 134.</span></figcaption>
</figure>

This transfer is coordinated in advance. As discussed on p. 133, an abrupt grid-converter failure without the handover signal does not provide the same active power coordination. The seamless transition applies to the demonstrated signalled sequence.

<figure>
  <a href="/images/research/dc-microgrid-control/pv-curtailment-result.png" target="_blank" rel="noopener" aria-label="View original: islanded PV power limitation"><img src="/images/research/dc-microgrid-control/pv-curtailment-result.png" alt="Original traces of bus voltage, battery current and PV power showing curtailment near 51 V when storage is full" width="1293" height="783" loading="lazy"></a>
  <figcaption><strong>PV power limitation with storage at full charge.</strong> The PV operating point shifts away from maximum power as the system limits surplus generation. <span class="figure-source">PhD thesis, Figure 6.26, p. 137.</span></figcaption>
</figure>

The laboratory sequence shortens charging to **10 seconds using an internal timer** to demonstrate state transitions (p. 129). These waveforms establish control-sequence behaviour rather than full-duration battery charging or long-term scheduling performance.

<h2 id="project-resources">Sources and Related Work</h2>

- **Main source:** [Control Strategies for Low Voltage DC Microgrids](https://publications.aston.ac.uk/id/eprint/46135/), PhD thesis, **Chapter 6, pp. 108–138**, Table 6-1 and Appendix A6.
- **Signalling method:** [A Dual-Window DC Bus Interacting Method for DC Microgrids Hierarchical Control Scheme](https://ieeexplore.ieee.org/document/8645723), IEEE Transactions on Sustainable Energy, 2020.
- **Related later work:** [Energy Management System for DC Microgrids Considering Battery Degradation](https://ieeexplore.ieee.org/document/9281580), IEEE PESGM, 2020.

[Previous: Dual-Window DC Bus Signalling](/research/dcmg/dc-bus-signalling/) · [DC Microgrid Control Strategies](/research/dcmg/) · [Microgrid Energy Management](/research/mgapp/) · [All publications](/publications/)
