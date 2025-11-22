---
layout: single
title: "Isolated Converters"
permalink: /research/isolated_converters/
author_profile: true
---

## Overview

This section introduces the **topologies, modelling, and control** of isolated DC–DC converters.  
Unlike non-isolated converters, these topologies use **galvanic isolation** (often with high-frequency transformers) to provide safety, meet regulatory requirements, and allow large step-up or step-down voltage ratios.

---

## Isolated DC–DC Converter Summary

| Topology | Description | GitHub Examples |
|----------|-------------|----------------|
| **Dual Active Bridge (DAB)** | Widely used for high-power bidirectional energy transfer. Achieves soft-switching (ZVS) and high efficiency at medium–high power levels. | [DAB Converter Repo](https://github.com/yourname/dab-converter) |
| **LLC Resonant Converter** | High efficiency and soft-switching over wide load range. Common in server power supplies, EV chargers, and telecom applications. | [LLC Converter Repo](https://github.com/yourname/llc-converter) |
| **Full-Bridge Converter** | Classic isolated topology, robust and suitable for wide input/output ranges. | [Full-Bridge Converter Repo](https://github.com/yourname/fullbridge-converter) |

> *Tip*: Each GitHub repository can include circuit diagrams, design notes, and simulation files.


---

## Applications

- **EV Chargers & Onboard DC/DC** — high efficiency and galvanic isolation for safety.
- **Data Center & Server Power** — LLC and FB converters for dense power supplies.
- **Renewable Energy Systems** — DAB and FB converters in PV and energy storage.
- **Industrial Automation & Robotics** — reliable isolated power for control and drive systems.

---

**Feel free to reach out** via [email](mailto:fulong.li@ieee.org).
