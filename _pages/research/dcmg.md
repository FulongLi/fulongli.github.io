---
layout: single
title: "DC Microgrid Control Strategies"
permalink: /research/dcmg/
author_profile: true
body_class: microgrid-project-page
project_stylesheet: /assets/css/marine-project.css
excerpt: "Passive converter control, DC bus signalling and rule-based energy management demonstrated on a laboratory microgrid."
---

<h2 id="overview">Stable Converters, Coordinated Energy Sources</h2>

A DC microgrid needs stable local control and a way for sources and storage to agree on operating roles. My PhD research connects those tasks through **passive converter control**, **dual-window DC bus signalling** and **rule-based power management**.

I developed the stabiliser and signalling method, then integrated them with droop control on a low-voltage laboratory microgrid. The study covers battery coordination, source connection, planned grid/island transitions and surplus PV limitation.

<h2 id="hierarchical-control">A Three-Layer Control Framework</h2>

<figure>
  <a href="/images/research/dc-microgrid-control/control-hierarchy.png" target="_blank" rel="noopener"><img src="/images/research/dc-microgrid-control/control-hierarchy.png" alt="Primary current and voltage control, secondary droop coordination and tertiary power-flow management" width="900" height="396" fetchpriority="high"></a>
  <figcaption><strong>From local regulation to system operation.</strong> Each layer provides the behaviour needed by the next. <span class="figure-source">PhD thesis, Figure 6.1, p. 109.</span></figcaption>
</figure>

<span id="passive-control"></span>
**[Passive control](/research/dcmg/passive-control/)** stabilises Boost interface converters. A high-pass-filtered compensator suppresses oscillation while avoiding the steady-state voltage shift of constant-gain compensation.

<span id="dc-bus-signalling"></span>
**[Dual-window bus signalling](/research/dcmg/dc-bus-signalling/)** separates normal droop operation from intentional voltage messages, allowing converters to exchange coordination commands through the power bus.

<span id="rule-based-ems"></span>
**[Rule-based EMS](/research/dcmg/rule-based-ems/)** assigns bus regulation, charging and discharging roles and limits PV output when storage cannot absorb the surplus.

<h2 id="experimental-validation">A Laboratory Demonstration</h2>

<figure>
  <a href="/images/research/dc-microgrid-control/laboratory-bench.png" target="_blank" rel="noopener"><img src="/images/research/dc-microgrid-control/laboratory-bench.png" alt="Low-voltage DC microgrid bench with source emulation, battery interfaces, loads and measurement equipment" width="1212" height="915" loading="lazy"></a>
  <figcaption><strong>The experimental system.</strong> Controlled interface converters connect emulated generation, storage and loads. <span class="figure-source">PhD thesis, Figure 3.1, p. 63.</span></figcaption>
</figure>

The experiments connect converter stability to coordinated source behaviour, including a signalled handover of bus regulation before planned grid disconnection. The result establishes the control sequence for the tested conditions; abrupt grid failure without that signal is a separate case.

<h2 id="droop-control-and-power-sharing">Wider Research and Significance</h2>

Related work examines voltage variation and line-resistance effects on power sharing, extending the same question: how can local converter behaviour support reliable operation of the network?

[PhD thesis: Control Strategies for Low Voltage DC Microgrids](https://publications.aston.ac.uk/id/eprint/46135/), Chapters 4–6. · [Passive-control paper](https://ieeexplore.ieee.org/document/9391691) · [Dual-window signalling paper](https://ieeexplore.ieee.org/document/8645723) · [Figure sources](/files/research/dc-microgrid-control/figure-sources.json)

[Battery Energy Storage](/research/battery_storage/) · [PV Battery System](/research/pv_systems/) · [All publications](/publications/) · [Back to Research](/research/)
