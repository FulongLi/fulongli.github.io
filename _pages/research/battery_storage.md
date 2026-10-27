---
layout: research
research_area: microgrids
title: "Battery Storage: Converter Control and Energy Management"
permalink: /research/battery_storage/
excerpt: "Battery storage in DC microgrids at two levels: plug-and-play converter control and current sharing, and degradation-aware energy management."
---

Battery storage enters a DC microgrid at two different levels, and the two are kept apart here. At **converter level** the question is how each battery interface regulates the bus and shares current with its peers, on a timescale of milliseconds. At **system level** the question is when to charge and discharge over a day, given prices, demand and the cost of battery wear.

## Converter-level control {#converter-level-control}

### Plug-and-play operation and current sharing {#battery-power-sharing-and-plug-and-play-storage}

**Problem.** Droop control lets battery modules share load without communication, so modules can be added and removed, but it trades away current-sharing accuracy and its coefficients must be chosen carefully: large droop coefficients move the operating point and can cause instability.

**My work.**

- *Multifunctional control for modular plug-and-play storage* (IEEE ISIE 2020) reconfigures the hierarchical control scheme so that an automatic master–slave mechanism in the secondary layer handles cases where communication is absent or the master module fails.
- *Reconstructed droop control* (IEEE ICDCM 2021) realises droop through a reconstructed control block with a natural droop coefficient, avoiding the need to select large coefficients, and provides a variable for integration with the hierarchical scheme.

**Evidence.** Both papers validate the methods in MATLAB/Simulink simulation.

### State-of-charge-based control on hardware

At Loughborough University I implemented state-of-charge-based control for the battery units of the [laboratory DC microgrid](/research/experimental_platforms/) on its DSP-controlled [interface converters](/research/nonisolated_converters/#bidirectional-half-bridge-buckboost-converter). The thesis demonstration of signalled battery charging and discharging is described under [Rule-based EMS](/research/dcmg/rule-based-ems/).

## System-level energy management {#battery-degradation-modelling-and-energy-management-optimisation}

**Problem.** In a DC microgrid the battery often holds the bus voltage, so scheduling that ignores wear cycles it more than necessary.

**My work.** As a visiting PhD student at the University of Waterloo (2019), supervised by Prof. Claudio Cañizares, I developed a GAMS-based energy management model for DC microgrids that includes a battery degradation cost, and improved the degradation modelling within the optimisation.

**Evidence.** The IEEE PES General Meeting 2020 paper applies the model to the DC microgrid of a building at Xiamen University. In simulation, including the degradation cost avoided frequent charge–discharge cycling while maintaining the required bus voltage. See [Energy management](/research/ems/).

## References

<ol class="references">
<li>F. Li, H. Xu, Z. Lin, “<a href="https://doi.org/10.1109/ISIE45063.2020.9152414">Multifunctional Control Design for Modular Plug-and-play Battery Storage in DC Microgrids</a>,” IEEE ISIE, 2020, pp. 1147–1152.</li>
<li>F. Li, H. Xu, Z. Lin, “<a href="https://doi.org/10.1109/ICDCM50975.2021.9504641">Reconstructed Droop Control for Peer Current Sharing of Battery Storage in DC Microgrids</a>,” IEEE ICDCM, 2021.</li>
<li>F. Li, C. A. Cañizares, Z. Lin, “<a href="https://doi.org/10.1109/PESGM41954.2020.9281580">Energy Management System for DC Microgrids Considering Battery Degradation</a>,” IEEE PES General Meeting, 2020.</li>
</ol>
