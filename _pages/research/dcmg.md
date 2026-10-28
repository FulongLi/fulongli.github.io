---
layout: single
title: "DC Microgrid Control Strategies"
permalink: /research/dcmg/
author_profile: true
body_class: microgrid-project-page
project_stylesheet: /assets/css/marine-project.css
project_contents: true
excerpt: "Passive converter control, DC bus signalling and rule-based energy management demonstrated on a laboratory microgrid."
---

My PhD research developed a hierarchical control scheme for low-voltage DC microgrids, connecting **passive converter control**, **dual-window DC bus signalling** and **rule-based power management**. I developed the stabiliser and signalling method, integrated them with droop control and demonstrated the complete scheme on a laboratory microgrid.

<h2 id="overview">Stable Converters, Coordinated Sources</h2>

A DC microgrid connects generation, storage and loads to a common DC bus through power converters. Running it reliably requires two things at once: each converter must remain stable as converters interact on the bus, and the sources and storage must agree on operating roles, such as which one regulates the bus voltage and when batteries charge. Hierarchical control addresses these at different time scales, from fast local current and voltage loops, through droop-based power sharing, to supervisory power management.

<h2 id="hierarchical-control">A Three-Layer Control Framework</h2>

<figure>
  <a href="/images/research/dc-microgrid-control/control-hierarchy.png" target="_blank" rel="noopener"><img src="/images/research/dc-microgrid-control/control-hierarchy.png" alt="Primary current and voltage control, secondary droop coordination and tertiary power-flow management" width="900" height="396" fetchpriority="high"></a>
  <figcaption>Primary current and voltage control, secondary droop coordination and tertiary power-flow management.</figcaption>
</figure>

<span id="passive-control"></span>
**[Passive control for Boost converters](/research/dcmg/passive-control/)** stabilises the interface converters. A high-pass-filtered compensator suppresses oscillation without the steady-state voltage shift of constant-gain compensation.

<span id="dc-bus-signalling"></span>
**[Dual-window bus signalling](/research/dcmg/dc-bus-signalling/)** separates normal droop operation from deliberate voltage messages, so converters can exchange coordination commands through the power bus.

<span id="rule-based-ems"></span>
**[Rule-based EMS](/research/dcmg/rule-based-ems/)** assigns bus regulation, charging and discharging roles, and limits PV output when storage cannot absorb the surplus.

<h2 id="experimental-validation">Laboratory Demonstration</h2>

I demonstrated the scheme on a low-voltage laboratory microgrid in which interface converters connect emulated generation, battery storage and loads. The experiments link converter stability to coordinated source behaviour, including a signalled handover of bus regulation before planned grid disconnection and the limitation of surplus PV generation.

<figure>
  <a href="/images/research/dc-microgrid-control/laboratory-bench.png" target="_blank" rel="noopener"><img src="/images/research/dc-microgrid-control/laboratory-bench.png" alt="Low-voltage DC microgrid bench with source emulation, battery interfaces, loads and measurement equipment" width="1212" height="915" loading="lazy"></a>
  <figcaption>Low-voltage DC microgrid bench with source emulation, battery interfaces, loads and measurement equipment.</figcaption>
</figure>

<span id="droop-control-and-power-sharing"></span>
Related work examines how voltage variation and line resistance affect droop power sharing, extending the same question: how local converter behaviour can support reliable operation of the network.

[PhD thesis: Control Strategies for Low Voltage DC Microgrids](https://publications.aston.ac.uk/id/eprint/46135/), Chapters 4–6. · [Passive-control paper](https://ieeexplore.ieee.org/document/9391691) · [Dual-window signalling paper](https://ieeexplore.ieee.org/document/8645723)

[Battery Energy Storage](/research/battery_storage/) · [PV Battery System](/research/pv_systems/) · [All publications](/publications/) · [Back to Research](/research/)
