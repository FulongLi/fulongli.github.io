---
layout: single
title: "Sensing Devices"
permalink: /research/sensing_devices/
author_profile: true
---

## Overview

Accurate **current sensing** is essential for **closed-loop control**, **fault protection**, and **efficiency optimization** in power electronic converters.  
Recent developments in **PCB-based magnetic sensors** enable compact, low-cost, and wide-bandwidth current measurement.

This section highlights two key technologies:

- **PCB Rogowski Coils (PCB-RC)**  
- **Embedded-Core PCB Current Transformers (PCB-CT)**  

---

## PCB Rogowski Coil (PCB-RC)

PCB Rogowski coils are air-cored current sensors printed directly onto a PCB.

**Key Features**
- Wide bandwidth and excellent linearity — ideal for fast switching (SiC device).
- No magnetic core → minimal saturation risk and wide dynamic range.
- Flexible form factor — easily integrated into power modules or busbars.
- Requires external integrator circuit to recover current signal.

**Design Considerations**
- **Winding geometry** (spiral, meander, differential pairs) affects mutual inductance and noise immunity.
- **Shielding and return paths** reduce EMI coupling.
- **Integrator circuit**: high-quality op-amp, RC time constant tuned for switching frequency.

**Prototype Example**

<img src="/images/research/Rogcoil/RogT2_d.png" width="300" />
<img src="/images/research/Rogcoil/RogT4_d.png" width="300" />

Full Details: [GitHub — PCB Rogowski Coil Design](https://github.com/FulongLi/Magnetics-PCBRogowskiCoil)

---

## Embedded-Core PCB Current Transformer (PCB-CT)

PCB-CT integrates a **ferromagnetic core** into the PCB stack-up, forming a compact, isolated current transformer.

**Key Features**
- Galvanic isolation and low insertion loss.
- High sensitivity at lower frequencies compared to air-cored sensors.
- Robust against external EMI due to magnetic core.

**Design Considerations**
- **Core material and geometry** — ferrite vs. nanocrystalline; cut core vs. planar core.
- **Turns ratio** — primary busbar vs. multiple secondary PCB turns.
- **Bandwidth trade-off** — core size, leakage inductance, and winding parasitics.
- **Thermal stability** — embedded cores affect PCB lamination and soldering processes.

**Prototype Example**

<img src="/images/research/CT/CT1_d.png" width="300" />

Full Details: [GitHub — PCB Current Transformer Design](https://github.com/FulongLi/Magnetics-PCBCurrentTransformerTransducer)

---

**Feel free to reach out** via [email](mailto:fulong.li@ieee.org).
