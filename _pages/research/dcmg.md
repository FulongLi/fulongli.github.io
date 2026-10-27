---
layout: single
title: "DC Microgrid Control Strategies"
permalink: /research/dcmg/
author_profile: true
body_class: microgrid-project-page
project_stylesheet: /assets/css/marine-project.css
project_script: /assets/js/marine-project.js
excerpt: "Passive converter control, dual-window DC bus signalling and rule-based energy management within a three-layer DC microgrid hierarchy."
---

<h2 id="overview">Control Strategies for Low Voltage DC Microgrids</h2>

How can a DC microgrid coordinate renewable generation and battery storage while keeping its converters stable and allowing sources to connect and disconnect? My doctoral research at **Aston University** addressed this question through a modified hierarchical control scheme, connecting converter dynamics, DC bus signalling and system operating rules.

**My contribution:** I developed a passive stabiliser for interface converters and a dual-window DC bus interacting method, then combined them with droop control and rule-based power management on a low-voltage DC microgrid bench. The work examined plug-and-play operation, battery charging and discharging, planned grid/island transitions and surplus PV power limitation.

<figure>
  <a href="/images/research/dc-microgrid-control/laboratory-bench.png" target="_blank" rel="noopener" aria-label="View original: low-voltage DC microgrid bench"><img src="/images/research/dc-microgrid-control/laboratory-bench.png" alt="Original thesis photograph of the laboratory bench with interface converters, PV emulator, electronic load and oscilloscope" width="1212" height="915" fetchpriority="high"></a>
  <figcaption><strong>The experimental foundation.</strong> The bench connects source emulation, battery storage and loads through controlled interface converters. <span class="figure-source">PhD thesis, Figure 3.1, p. 63.</span></figcaption>
</figure>

<nav class="project-contents" aria-label="Project contents">
  <p><strong>On this page</strong></p>
  <ul>
    <li><a href="#overview">Research overview</a></li>
    <li><a href="#hierarchical-control">Three-layer control framework</a></li>
    <li><a href="#passive-control">Passive control</a></li>
    <li><a href="#dc-bus-signalling">Dual-window DC bus signalling</a></li>
    <li><a href="#rule-based-ems">Rule-based EMS</a></li>
    <li><a href="#droop-control-and-power-sharing">Related power-sharing research</a></li>
    <li><a href="#project-resources">Thesis and publications</a></li>
  </ul>
</nav>

<h2 id="hierarchical-control">A Three-Layer Control Framework</h2>
<span id="hierarchical-control-and-dc-bus-signalling"></span>

The layer names below follow **the modified hierarchy used in my thesis**: primary current/voltage control, secondary droop control and tertiary power-flow control.

<figure>
  <a href="/images/research/dc-microgrid-control/control-hierarchy.png" target="_blank" rel="noopener" aria-label="View original: thesis control hierarchy"><img src="/images/research/dc-microgrid-control/control-hierarchy.png" alt="Thesis hierarchy: primary current and voltage control, secondary droop control, tertiary power-flow control and sharing" width="900" height="396" loading="lazy"></a>
  <figcaption><strong>From converter regulation to coordinated power flow.</strong> The passive stabiliser supports primary control; droop behaviour enables bus interaction; decoded signals determine operating states and current references. <span class="figure-source">PhD thesis, Figure 6.1, p. 109.</span></figcaption>
</figure>

<div class="project-table-scroll" role="region" aria-label="Three-layer control framework" tabindex="0" markdown="1">

| Control layer | Main task | Method in this research | Read more |
|---|---|---|---|
| Primary: converter control | Stable local current and voltage regulation | Inner/outer control loops with a passive stabiliser | [Passive Control](/research/dcmg/passive-control/) |
| Secondary: bus coordination | Droop behaviour and plug-and-play bus interaction | Separate working and signalling voltage windows | [Dual-Window DC Bus Signalling](/research/dcmg/dc-bus-signalling/) |
| Tertiary: power management | Select modes, charging/discharging and power-flow commands | Rule-based logic carried by six-bit DBI signals | [Rule-Based EMS](/research/dcmg/rule-based-ems/) |

</div>

The dual-window method connects the layers: controlled changes in bus voltage exchange low-bandwidth commands, while operating rules determine their meaning for each source or storage unit.

<h2 id="passive-control">1. Passive Control</h2>
<span id="primary-converter-control-and-stability-analysis"></span>

Boost-converter non-minimum-phase dynamics can limit stable voltage regulation. I developed a feedforward passive stabiliser and a high-pass-filter modification to improve local dynamics while avoiding the steady-state voltage shift introduced by constant-gain compensation. Chapter 5 provides the design and laboratory evidence, including operation with a reduced terminal capacitor.

[Explore passive control: converter model, stabiliser design and experimental waveforms](/research/dcmg/passive-control/)

<h2 id="dc-bus-signalling">2. Dual-Window DC Bus Signalling</h2>

The **dual-window DC bus interacting (DBI) method** separates normal droop operation from signalling. Interface converters briefly manipulate the bus voltage to send a command, then return to their assigned voltage- or current-control role. The method supports source registration and power coordination without a separate communication link.

[Explore DC bus signalling: dual-window droop curves, signal design and converter interaction](/research/dcmg/dc-bus-signalling/)

<h2 id="rule-based-ems">3. Rule-Based EMS and Hierarchical Operation</h2>
<span id="source-and-storage-coordination"></span>

Chapter 6 brings the methods together. A finite-state machine coordinates the grid interface, two battery interfaces and PV generation. Explicit rules govern charging priority, support for islanded loads, planned grid/island transitions and PV curtailment when storage cannot absorb the surplus. The experiments connect local converter stability to source and storage coordination.

[Explore rule-based EMS: operating rules, six-bit commands and system experiments](/research/dcmg/rule-based-ems/)

<h2 id="droop-control-and-power-sharing">Related Research: Droop Control and Power Sharing</h2>

My related work examines bus-voltage variation, line-resistance effects and current-sharing accuracy. These studies complement the thesis framework and the work under [Battery Energy Storage Systems](/research/battery_storage/) and [Non-Isolated / Bidirectional DC–DC Converters](/research/nonisolated_converters/).

- [A Low-pass Filter Method to Suppress the Voltage Variations Caused by Introducing Droop Control in DC Microgrids](https://ieeexplore.ieee.org/document/8557455), IEEE ECCE, 2018.
- [Virtual Negative Cable Resistance for Power Sharing Accuracy Enhancement in DC Microgrids](https://ieeexplore.ieee.org/document/8781426), IEEE ISIE, 2019.
- [Terminal Capacitor Compensation Based Stability Design for DC Microgrids](https://ieeexplore.ieee.org/document/9232923), IEEE ICDCM, 2019.
- [Comprehensive local control design for eliminating line resistance effect on power sharing degradation in DC microgrids](https://ietresearch.onlinelibrary.wiley.com/doi/epdf/10.1049/pel2.12208), IET Power Electronics, 2022.

<h2 id="project-resources">Thesis and Publications</h2>

- **PhD thesis:** [Control Strategies for Low Voltage DC Microgrids](https://publications.aston.ac.uk/id/eprint/46135/), Aston University. The manuscript is dated July 2019; the university record lists the award in 2020. Chapters 4–6 are the main sources for these pages.
- **Passive control:** [Novel Passive Controller Design for Enhancing Boost Converter Stability in DC Microgrid Applications](https://ieeexplore.ieee.org/document/9391691), IEEE JESTPE, 9(6), 6901–6911, 2021.
- **Dual-window DBI:** [A Dual-Window DC Bus Interacting Method for DC Microgrids Hierarchical Control Scheme](https://ieeexplore.ieee.org/document/8645723), IEEE Transactions on Sustainable Energy, 11(2), 652–661, 2020.
- **Earlier signalling work:** [Active DC bus signaling control method for coordinating multiple energy storage devices in DC microgrid](https://ieeexplore.ieee.org/document/8001048), IEEE ICDCM, 2017.
- **Review:** [Review of DC Bus Signalling Control Methods in DC Microgrids](https://ieeexplore.ieee.org/document/9959577), IEEE PEAC, 2022.

Figures are reproduced from my thesis with their original colours and proportions; captions identify the source figure and page.

[All publications](/publications/) · [PV Battery System](/research/pv_systems/) · [Experimental Platforms](/research/experimental_platforms/) · [Microgrid Energy Management](/research/mgapp/) · [DC Safety & Protection](/research/dc_safety/) · [Back to Research](/research/)
