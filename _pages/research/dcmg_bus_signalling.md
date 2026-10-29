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

I developed the **dual-window DC bus interacting (DBI) method**, which lets sources and storage in a DC microgrid exchange operating commands through the DC bus voltage itself, without a separate communication link. I designed the voltage windows, signal sequences and converter-control modifications.

<h2 id="overview">Coordinating Converters Through the Bus Voltage</h2>

In a DC microgrid, droop control lets several converters share load without communication: each converter lowers its output voltage as its current rises, so the bus voltage itself indicates loading. Higher-level coordination, such as switching a battery on or handing bus regulation from one source to another, normally needs a separate communication network.

Bus signalling removes that network by also using the bus voltage to carry deliberate messages. The difficulty is keeping messages distinct from the ordinary voltage changes caused by droop control.

<h2 id="dual-window-principle">Working and Signalling Voltage Windows</h2>

My method separates the two functions into distinct voltage ranges. Normal droop operation stays within a working window, while deliberate signalling uses a level outside it. My design uses a **45–50 V working window** and a **52.5 V signalling level**.

<figure>
  <a href="/images/research/dc-microgrid-control/dual-window-droop.png" target="_blank" rel="noopener"><img src="/images/research/dc-microgrid-control/dual-window-droop.png" alt="Droop curves with separate working and signalling voltage windows" width="1095" height="693" fetchpriority="high"></a>
  <figcaption>Droop characteristics with separate working and signalling voltage windows.</figcaption>
</figure>

To send a message, one converter temporarily drives the bus voltage through a sequence while the others decode it, then returns to its assigned power-control role. As the bus rises during reception, the receiving converters' outer voltage loops would otherwise demand unwanted negative current. I isolated that loop during reception and applied a positive or zero current reference, limiting the extra power the signalling converter must supply. Each converter returns to its normal control mode after the sequence.

<h2 id="signal-design">System Commands</h2>

The simplest messages switch a converter on or off. The integrated system extends the method to **six-bit commands at 100 ms per bit**, selecting converter identity, operating mode, charging or discharging and current reference.

These commands carry the [rule-based EMS](/research/dcmg/rule-based-ems/): one interface regulates the bus, and explicit signals hand that role to another. Using the bus for both power and information simplifies the communication arrangement, at the cost of low bandwidth, deliberate voltage excursions and settling intervals that must suit the connected loads and the required coordination speed.

[A Dual-Window DC Bus Interacting Method for DC Microgrids Hierarchical Control Scheme](https://ieeexplore.ieee.org/document/8645723), IEEE Transactions on Sustainable Energy, 2020. · [PhD thesis](https://publications.aston.ac.uk/id/eprint/46135/), Chapters 4 and 6.

[Passive Control](/research/dcmg/passive-control/) · [Rule-Based EMS](/research/dcmg/rule-based-ems/) · [Back to Research](/research/)
