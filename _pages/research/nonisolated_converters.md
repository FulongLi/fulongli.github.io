---
layout: research
research_area: converters
title: "Non-Isolated and Grid-Interface Converters"
permalink: /research/nonisolated_converters/
excerpt: "Bidirectional buck–boost interface converters for a laboratory DC microgrid, boost converter control, and work with a three-phase VSC on a 50 kW DC microgrid platform."
---

These converters were not designed as standalone products. They are the interface converters of DC microgrid research, so their requirements come from the system: regulating a shared DC bus, sharing current under droop control, and remaining stable when sources and loads connect and disconnect.

## Bidirectional half-bridge buck–boost converter {#bidirectional-half-bridge-buckboost-converter}

**Problem.** A battery on a DC microgrid must both charge from and discharge into the bus, and a PV source or grid emulator must be interfaced to the same bus with a common control structure.

**My contribution.** During my PhD at Aston University and at Loughborough University I built the bench converters for the [laboratory DC microgrid](/research/experimental_platforms/) and implemented their DSP-based control: double-loop voltage and current control, feedforward compensation for transient response, MPPT for the PV interface, and state-of-charge-based control for the battery units.

**Hardware.** Each interface is a half-bridge bidirectional buck–boost (bidirectional boost) converter with a TMS320F28335 DSP control card. The public design repository lists a 240 µH inductor and 470 µF input and output capacitors, and documents a second bench version with a higher power rating and improved gate drive and sensing.

**Evidence.** The converters are the hardware used for the experiments in my [PhD thesis](https://publications.aston.ac.uk/id/eprint/46135/); the bench and its configuration are described in the thesis and in the public repository.

## Boost converter stability by passive control

The boost converter's right-half-plane zero (non-minimum-phase behaviour) limits how fast its voltage loop can be made, and a microgrid interface converter is exposed to constant-power loads and changes in terminal capacitance. I developed a feedforward passive stabiliser with a high-pass filter that damps the resulting oscillation without shifting the steady-state bus voltage, and validated it experimentally. The method, equations and measured waveforms are on the [passive control page](/research/dcmg/passive-control/); the work is published in IEEE JESTPE (2021).

## AC–DC converter interface: three-phase VSC {#acdc-converter-interfaces}

During a visiting period at Zhejiang University (March–April 2018) I tested and operated an existing **50 kW DC microgrid platform** whose grid interface was a three-phase voltage-source converter (VSC), and modified primary control strategies to improve stability and dynamic response. The VSC was part of the platform; I did not design or build it. Details of the tests are not yet documented here.

## References and resources

- F. Li, Z. Lin, “[Novel Passive Controller Design for Enhancing Boost Converter Stability in DC Microgrid Applications](https://doi.org/10.1109/JESTPE.2021.3070234),” *IEEE JESTPE*, 9(6), 6901–6911, 2021.
- [DCMicrogridTestBench (GitHub, CC BY 4.0)](https://github.com/FulongLi/DCMicrogridTestBench): power and control board description of the bench converters.
- [NonisolatedCoverters (GitHub, CC BY 4.0)](https://github.com/FulongLi/NonisolatedCoverters): boost control design scripts and Simulink models.
- Related: [Battery storage control](/research/battery_storage/) · [DC microgrid control strategies](/research/dcmg/)
