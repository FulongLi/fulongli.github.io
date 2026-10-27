---
layout: research
research_area: components
parent:
  title: "Device characterisation"
  url: /research/switching_devices/
title: "Electrical Characterisation: Double-Pulse Testing"
permalink: /research/electrical-characterization/
excerpt: "Double-pulse switching measurements of power modules, including IGBT modules, to build switching-energy datasets for device modelling."
---

## Engineering problem

Switching loss is the event energy *E*<sub>on</sub> or *E*<sub>off</sub> multiplied by switching frequency, and those energies depend on DC-link voltage, load current, gate resistance and junction temperature. Datasheets give a few curves at fixed conditions. A converter loss model, and in particular a data-driven one, needs a denser and consistent set of measurements across the operating range actually used.

## Objective and scope

Produce switching-energy datasets for power modules, including IGBT modules in an industry-funded characterisation project, as training and validation data for ANN-based device modelling. The scope was the measurement platform, the test campaign and the waveform post-processing; the downstream models are described under [device modelling](/research/mosfet_ann_modelling/).

## My contribution

- Built the double-pulse test platform with a colleague, including modifications to the original test board, as part of a test rig I designed and commissioned for SiC and GaN device characterisation.
- Carried out a large double-pulse test campaign on IGBT modules across voltage, current, gate-resistance and temperature conditions.
- Post-processed the recorded waveforms to extract switching energies and transient parameters.

## Method

The double-pulse test applies two gate pulses to the device under test in a half-bridge with an inductive load. The first pulse ramps the inductor current to the target value, approximately *I* = *V*<sub>DC</sub>*t*<sub>1</sub>/*L*. The turn-off at the end of the first pulse and the turn-on at the start of the second occur at that current, while the short test keeps the junction near the set temperature. Each event energy is the integral of device voltage multiplied by device current over a defined event window:

<p class="equation"><em>E</em> = ∫ <em>v</em><sub>DS/CE</sub>(<em>t</em>) <em>i</em><sub>D/C</sub>(<em>t</em>) d<em>t</em></p>

Three measurement decisions dominate the result, and the post-processing was built around them:

1. **Channel alignment.** A few nanoseconds of skew between voltage and current probes changes the integrated energy, so channels were deskewed and zero offsets removed before multiplication.
2. **Event window.** Integration limits defined by voltage and current thresholds must be applied consistently, particularly when comparing IGBT tail current with fast SiC transitions.
3. **Data quality.** Captures with clipping or insufficient current-sensor resolution were identified and excluded rather than averaged into the dataset.

## Results and evidence

The campaign produced a switching-energy dataset across the planned voltage, current, gate-resistance and temperature matrix, with turn-on and turn-off energies and transient parameters extracted per event. These data and the platform documentation are held in internal project reports and are not reproduced here.

## Limitations

- Acquisition was manual; consistent settings and file organisation were a significant part of the effort. Automated acquisition was identified as follow-on work.
- Double-pulse results describe single switching events in the test fixture. Applying them to a converter requires accounting for its own layout parasitics and gate drive.

## Related pages

[Thermal characterisation](/research/thermal-characterization/) · [Reliability testing](/research/reliability_testing/) · [ANN-based device modelling](/research/mosfet_ann_modelling/)
