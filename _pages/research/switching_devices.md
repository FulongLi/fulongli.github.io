---
layout: single
title: "Switching Devices"
permalink: /research/switching_devices/
author_profile: true
---

## Overview

Switching devices are the cornerstone of modern power electronics. They determine the performance, efficiency, and compactness of power conversion systems. Key technologies include:

- IGBTs for medium- to high-voltage applications  
- SiC MOSFETs for high-efficiency, high-frequency systems  
- GaN HEMTs for ultra-fast switching and compact converter designs

---

## Device Comparison

| Device Type | Switching Speed | Voltage Rating | Efficiency | Typical Use Case |
|-------------|------------------|----------------|------------|------------------|
| IGBT        | Medium           | 600–1700 V     | Moderate   | Inverters, motor drives |
| SiC MOSFET  | High             | 650–3300 V     | High       | EV traction, DC–DC, PV |
| GaN HEMT    | Very High        | 100–650 V      | Very High  | Fast chargers, telecom, server PSU |

---

## Testing and Measurement

### 1) Power-Loss Characterisation
- Double-Pulse Test (DPT) for switching loss (E_on, E_off, E_rec)  
- Conduction loss from I–V/R_DS(on)/V_CE(sat) vs T_j curves  
- High-bandwidth voltage/current probes, low-inductance fixtures, controlled gate drive

### 2) Thermal Modelling
- Thermal impedance Z_th extraction (step response / structure function)  
- Cauer/Foster network fitting for transient thermal simulation  
- Layout/gate-loop parasitics and dead-time impacts on junction heating

---

## AI-Assisted Device Modelling (ANN)

To accelerate converter design and optimisation, we develop neural-network models that predict device losses and dynamics directly from operating conditions.

### A) Static Loss Modelling (Conduction) — using ANN
Goal: Predict conduction losses (P_cond) across operating points without exhaustive interpolation of datasheet curves.

- Inputs: device type, I, T_j, V_GS/V_GE, conduction mode (uni/bi-directional), package  
- Targets: R_DS(on)(T_j) or V_CE(sat)(I,T_j) and resulting P_cond = I^2R (MOSFET) / I × V_CE(sat) (IGBT)  
- Training data: digitised datasheets + bench DC sweeps (optional)  
- Validation: MAE/RMSE vs held-out curves; sanity checks against physics

Planned GitHub:  
- `/ann-static-loss/` — data loader, curve digitiser, training scripts, ONNX export

### B) Dynamic Loss Modelling (Switching) — using ANN
Goal: Predict E_on, E_off, diode E_rec vs V_DC, I, T_j, R_g, dv/dt, di/dt to speed up topology-level optimisation.

- Inputs: V_DC, load I, T_j, external R_g, stray L, gate voltage, package parasitics  
- Targets: E_on/off, peak overshoot, ringing metrics  
- Training data: curated DPT sweeps across the above variables (SiC/GaN/IGBT)  
- Model notes: use monotonic constraints or physics-informed loss terms  
- Validation: compare predicted loss maps to measured maps; cross-device generalisation

Planned GitHub:  
- `/ann-dynamic-loss/` — dataset schema, training notebooks, evaluation, exportable inference API

---

## DPT Automation (Measurement Pipeline)

A robust automated double-pulse testing stack to generate high-quality datasets for ANN training and verification.

Hardware
- Low-inductance DPT board (Kelvin source, tight gate loop), configurable R_g, external snubbers  
- High-BW probes (HV diff voltage probe, wide-band current shunt or Rogowski), isolated scopes  
- Temperature control (hotplate/chamber) for T_j sweeps; programmable DC source and electronic load

Software
- Instrument control (e.g., PyVISA) for supply, scope, load, chamber  
- Test matrices covering V_DC, I, T_j, R_g, repeatability passes  
- Auto-extraction of E_on/off, overshoot, ringing, and CSV/Parquet export with metadata

Safety and Data Quality
- Interlocks (over-voltage/current/temperature), soft-start sequencing  
- Fixture-level de-skew/calibration, uncertainty budgets, outlier detection  
- Versioned datasets for traceability

Planned GitHub:  
- `/dpt-automation/` — hardware docs, Python control scripts, feature extraction, dataset versioning

---

## Integration into Converter Design

- Plug ANN models into buck, DAB, LLC design flows to get instant loss/thermal estimates, enabling multi-objective optimisation (efficiency, mass, cost)  
- Export compact models (ONNX) for use in Python/Matlab design tools or C++/embedded evaluators

---

## Collaborations and Data

Have measured DPT datasets or want to validate a device family?  
Contact: [fulong.li@ieee.org](mailto:fulong.li@ieee.org)

Roadmap: open-source static/dynamic ANN models, DPT automation toolkit, and reference integration with buck, DAB, LLC workflows.
