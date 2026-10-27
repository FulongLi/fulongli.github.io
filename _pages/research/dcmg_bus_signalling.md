---
layout: single
title: "Dual-Window DC Bus Signalling"
permalink: /research/dcmg/dc-bus-signalling/
author_profile: true
body_class: microgrid-project-page
project_stylesheet: /assets/css/marine-project.css
project_contents: true
excerpt: "The dual-window DC bus interacting method: working and signalling voltage windows for coordination of sources and storage."
---

<h2 id="overview">Using the Power Bus to Coordinate Converters</h2>

My **dual-window DC bus interacting (DBI) method** combines droop control with intentional voltage signalling. It gives sources and storage a way to exchange operating commands through the DC bus, without a separate communication link for those commands.

I developed the voltage-window mechanism, signal sequences and converter-control modifications, and evaluated them on a laboratory DC microgrid.

<h2 id="dual-window-principle">Separate Windows for Power and Information</h2>

<figure>
  <a href="/images/research/dc-microgrid-control/dual-window-droop.png" target="_blank" rel="noopener"><img src="/images/research/dc-microgrid-control/dual-window-droop.png" alt="Droop curves with separate working and signalling voltage windows" width="1095" height="693" fetchpriority="high"></a>
  <figcaption>The dual-window principle.</figcaption>
</figure>

Normal power delivery and deliberate signalling occupy distinct voltage ranges.

The demonstration uses a **45–50 V working window** and a **52.5 V signalling level**. A converter temporarily controls the voltage sequence while the others decode it, then returns to its assigned power-control role. During reception, the active outer voltage loop can otherwise demand unwanted negative interacting current as the bus rises. Isolating that loop and applying a positive or zero current reference limits the extra power burden on the signalling converter. The source returns to its normal assigned control mode after the signal sequence.

<h2 id="signal-design">From Source Connection to Power Management</h2>

Bench tests demonstrate converter ON/OFF coordination and interacting-current compensation. The integrated system extends the approach to **six-bit commands**, with **100 ms per bit**, selecting converter identity, mode, charging or discharging, and current reference.

The method connects plug-and-play source interaction to the [rule-based EMS](/research/dcmg/rule-based-ems/). One interface maintains bus regulation, with explicit signalling used to hand that role to another.

<h2 id="scope">Implications for Distributed Coordination</h2>

Using the bus for both power and information simplifies the demonstrated communication arrangement. Its low bandwidth, deliberate voltage excursions and settling intervals must be considered alongside load compatibility and required coordination speed.

[A Dual-Window DC Bus Interacting Method for DC Microgrids Hierarchical Control Scheme](https://ieeexplore.ieee.org/document/8645723), IEEE Transactions on Sustainable Energy, 2020. · [PhD thesis](https://publications.aston.ac.uk/id/eprint/46135/), Chapters 4 and 6.

[Passive Control](/research/dcmg/passive-control/) · [Rule-Based EMS](/research/dcmg/rule-based-ems/) · [Back to Research](/research/)
