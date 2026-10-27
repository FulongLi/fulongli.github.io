---
layout: single
title: "Dual-Window DC Bus Signalling"
permalink: /research/dcmg/dc-bus-signalling/
author_profile: true
body_class: microgrid-project-page
project_stylesheet: /assets/css/marine-project.css
project_script: /assets/js/marine-project.js
excerpt: "The dual-window DC bus interacting method: working and signalling voltage windows for coordination of sources and storage."
---

<h2 id="overview">Coordinating Sources Through the DC Bus</h2>

DC bus signalling (DBS) uses the electrical bus to convey operating information between converters. My **dual-window DC bus interacting (DBI) method** combines this idea with droop control: converters use one voltage window for normal operation and another for deliberate signalling.

**My contribution:** I developed the dual-window mechanism, signal sequences and converter-control modifications, and evaluated them on a small-scale DC microgrid bench. **Chapter 4 of my PhD thesis** describes the method; **Chapter 6** uses it to carry power-management commands within the complete hierarchical scheme.

<nav class="project-contents" aria-label="Project contents">
  <p><strong>On this page</strong></p>
  <ul>
    <li><a href="#overview">Research overview</a></li>
    <li><a href="#dual-window-principle">The two voltage windows</a></li>
    <li><a href="#converter-interaction">Converter interaction</a></li>
    <li><a href="#signal-design">Signals and experiments</a></li>
    <li><a href="#scope">Design considerations</a></li>
    <li><a href="#project-resources">Sources and publications</a></li>
  </ul>
</nav>

<h2 id="dual-window-principle">A Working Window and a Signalling Window</h2>

The **working window** accommodates normal droop-based power delivery. The **signalling window** is reached deliberately during a signalling period, separating the intended message from normal droop-related voltage variation.

<figure>
  <a href="/images/research/dc-microgrid-control/dual-window-droop.png" target="_blank" rel="noopener" aria-label="View original: dual-window droop curves"><img src="/images/research/dc-microgrid-control/dual-window-droop.png" alt="Original droop diagram showing the working window, signal window, signalling voltage, droop coefficient and interacting current" width="1095" height="693" loading="lazy"></a>
  <figcaption><strong>The dual-window principle.</strong> Normal droop operation and signalling occupy distinct voltage windows. The original coloured curves show how converter interaction moves the bus into the signalling state. <span class="figure-source">PhD thesis, Figure 4.4, p. 77.</span></figcaption>
</figure>

In the Chapter 4 demonstration, the upper working reference is **50 V**, the lower working boundary is **45 V**, and the signalling level is **52.5 V**. Signal amplitude must remain distinguishable from bus disturbances while respecting the connected equipment's voltage requirements.

<h2 id="converter-interaction">Plug, Signal and Return to Power Control</h2>

During the **plug period**, a connecting source uses bus interaction to register with the converter maintaining the bus voltage. During the **play period**, sources follow their assigned roles, including battery current control and PV maximum-power-point tracking. A converter returns to voltage-controlled interaction when it needs to send another signal.

The signalling converter temporarily controls the bus-voltage sequence while the other converters monitor and decode it. At least one interface converter must maintain the bus voltage during operation; the system assigns that role to the grid interface or a battery interface.

Raising the bus into the signalling window can induce unwanted negative interacting current through an active outer voltage loop. Chapter 4 modifies the control during reception: it isolates that loop and applies a positive or zero current reference, reducing the extra power burden on the signalling converter. Local stability is addressed by the [passive stabiliser](/research/dcmg/passive-control/).

<h2 id="signal-design">From Simple Commands to Six-Bit Messages</h2>

Chapter 4 considers pulse-width-based signals and fixed-width binary sequences, then demonstrates converter ON/OFF coordination and interacting-current compensation. Chapter 6 extends the method to **six-bit sequences** for converter identity, operating mode, charging/discharging and current selection.

<div class="project-table-scroll" role="region" aria-label="DC bus signalling demonstration parameters" tabindex="0" markdown="1">

| Parameter | Chapter 4 demonstration | Chapter 6 integrated system |
|---|---|---|
| Upper working reference | 50 V | 50 V |
| Signalling voltage | 52.5 V | 52.5 V |
| Message design | Simple sequences for method validation | Six-bit operating commands |
| Fixed bit interval | Depends on the selected signal design | 100 ms |
| Main purpose | Validate bus interaction and command exchange | Coordinate source/storage states |

</div>

The **100 ms interval** is the implemented Chapter 6 bit duration, distinct from the faster inner converter-control response. The command vocabulary and rules are described in [Rule-Based EMS and Hierarchical Operation](/research/dcmg/rule-based-ems/).

<h2 id="scope">Design Considerations and Scope</h2>

The method removes the need for a separate communication link for the demonstrated commands. It relies on accurate voltage measurement, a detectable signal window and sufficient time to settle and decode each sequence. Chapter 6 includes delays between source interactions.

Information exchange is low bandwidth, and the bus voltage changes during signalling. These characteristics influence connected-load compatibility and coordination speed. The demonstration assigns one converter responsibility for bus regulation and uses an explicit command sequence to hand over that role.

<h2 id="project-resources">Sources and Publications</h2>

- [Control Strategies for Low Voltage DC Microgrids](https://publications.aston.ac.uk/id/eprint/46135/), PhD thesis, **Chapter 4, pp. 72–87**, and Chapter 6.
- F. Li, Z. Lin, Z. Qian, J. Wu and W. Jiang, [A Dual-Window DC Bus Interacting Method for DC Microgrids Hierarchical Control Scheme](https://ieeexplore.ieee.org/document/8645723), **IEEE Transactions on Sustainable Energy**, 11(2), 652–661, April 2020.
- [Active DC bus signaling control method for coordinating multiple energy storage devices in DC microgrid](https://ieeexplore.ieee.org/document/8001048), IEEE ICDCM, 2017.
- [Review of DC Bus Signalling Control Methods in DC Microgrids](https://ieeexplore.ieee.org/document/9959577), IEEE PEAC, 2022.

[Previous: Passive Control](/research/dcmg/passive-control/) · [Next: Rule-Based EMS](/research/dcmg/rule-based-ems/) · [DC Microgrid Control Strategies](/research/dcmg/)
