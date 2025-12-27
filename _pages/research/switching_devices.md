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

### 1. Electrical Characterisation

- Double-Pulse Test (DPT) for switching loss (E_on, E_off, E_rec)  

Full Details: [Github - DPT Automation](https://github.com/FulongLi/DPT_Automation)


- Conduction loss from I–V/R_DS(on)/V_CE(sat) vs T_j curves  


### 2. Thermal Characterisation
- Thermal impedance Z_th extraction (TO-247-3 Package) 

<img src="/images/research/characterisation/TIM.png" width="300" />

Full Details: [Github - TIM Automation](https://github.com/FulongLi/TIM_Automation)

- Cauer/Foster network fitting for transient thermal simulation  

- Layout/gate-loop parasitics and dead-time impacts on junction heating


---

## Electrical Modelling

To accelerate converter design and optimisation, we develop neural-network models that predict device losses and dynamics directly from operating conditions.

### 1. Static Modelling — using ANN
Goal: Predict losses across operating points without exhaustive interpolation of datasheet curves.

<img src="/images/research/characterisation/fig1.png" width="600" />
<img src="/images/research/characterisation/fig1-1.png" width="300" />
<img src="/images/research/characterisation/fig1-2.png" width="300" />

### 2. Dynamic Modelling (Switching) — using ANN

## Thermal Modelling

### 1. Static Modelling


### 2. Dynamic Modelling



Full Details: [Github: Transistor-MOSFETLibraryANN](https://github.com/FulongLi/Transistor-MOSFETLibraryANN)

---


## Integration into Converter Optimisaiton Design

- Plug ANN models into buck, DAB, LLC design flows to get instant loss/thermal estimates, enabling multi-objective optimisation (efficiency, mass, cost)  

<img src="/images/research/characterisation/optimisationstructure.png" width="600" />

Full Details: [Github: Converter Optimisaiton Design](https://github.com/FulongLi/BuckConverterOptimisation)

---

**Feel free to reach out** via [email](mailto:fulong.li@ieee.org).
