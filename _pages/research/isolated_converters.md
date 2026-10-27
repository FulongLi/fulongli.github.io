---
layout: research
research_area: converters
title: "10 kW LLC and Dual Active Bridge Converters"
permalink: /research/isolated_converters/
excerpt: "Design and simulation of 10 kW LLC resonant and dual active bridge DC–DC converters for liquid-cooled data-centre power supplies."
---

## Engineering problem

Data-centre power supplies need an isolated DC–DC stage that is efficient across a wide load range and compact enough for high power density, in this case within a liquid-cooled supply. The two leading candidates make different trade-offs. The **LLC resonant converter** achieves soft switching through its resonant tank and regulates by varying switching frequency, which suits a largely unidirectional, narrow-range conversion. The **dual active bridge (DAB)** controls power through the phase shift between two active bridges, which gives bidirectional power flow but requires attention to the soft-switching range at light load.

## Objective and scope

Design and simulate a 10 kW LLC converter and a 10 kW DAB converter for the **ELIPS** (Enhanced Liquid-cooled Power Supplies) project at CSA Catapult, so that the two topologies could be compared for the application. The scope was converter design and simulation. Hardware construction and measured efficiency are outside what this page reports.

## My contribution

I designed and simulated both converters in MATLAB/Simulink.

## Method

- **LLC:** a MATLAB design script for the resonant tank and a Simulink switching model of the converter.
- **DAB:** a Simulink model of the phase-shift-controlled converter.

Both are in the public repository listed below.

The [PCB current sensors](/research/sensing_devices/) developed in the same project address current measurement in the fast-switching SiC stages.

## Results and evidence

The outcome was a pair of simulated 10 kW designs. Simulation models and design scripts are available in a public repository. The project's detailed specifications and results are internal and not reproduced here.

## Limitations

- Simulation only: no measured efficiency, thermal or EMI results are claimed.
- Performance figures in the public repository's description are generic targets, not results of this project.

## References and resources

- [IsolatedCoverters (GitHub, CC BY 4.0)](https://github.com/FulongLi/IsolatedCoverters): LLC design script and Simulink model; DAB simulation files.
- Related: [Converter design optimisation](/research/converter_optimization/) · [Solid-state transformer assessment](/research/sst/)
