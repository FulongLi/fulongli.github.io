---
layout: single
title: "Non-Isolated Converters"
permalink: /research/nonisolated_converters/
author_profile: true
---

## Overview

This section introduces the **topologies, modelling, and control** of both **DC–DC** and **AC–DC** converters used across power electronics applications.

We start with **non-isolated converters** — simple but fundamental building blocks — then move into more advanced **bidirectional** and **AC interface** topologies.

---

## Non-Isolated DC–DC Converters

Non-isolated converters provide direct voltage transformation without galvanic isolation. They are widely used due to simplicity, high efficiency, and compact design.

| Topology | Description | GitHub Examples |
|----------|-------------|----------------|
| **Buck** | Steps down input voltage to a lower output level. Common in point-of-load supplies and embedded systems. | [Buck Converter Repo](https://github.com/yourname/buck-converter) |
| **Boost** | Steps up input voltage to a higher output level. Useful in LED drivers, renewable energy interfaces, and battery applications. | [Boost Converter Repo](https://github.com/yourname/boost-converter) |
| **Buck–Boost** | Provides output voltage that can be higher or lower than input; inverts polarity. | [Buck-Boost Converter Repo](https://github.com/yourname/buckboost-converter) |
| **Ćuk** | Achieves similar function to buck–boost but with reduced ripple on input/output current. | [Ćuk Converter Repo](https://github.com/yourname/cuk-converter) |

> *Tip*: Host each converter’s modelling and control example on GitHub (simulation files, small design notes, or code).

---

## Bidirectional Converters

Designed for **energy storage** and **two-way power flow**, ideal in battery management and DC microgrids.

- **Dual Active Bridge (DAB)** – high power density and soft-switching capability  
- **Non-isolated bidirectional buck-boost** – compact and cost-effective  
- [Example GitHub Repo](https://github.com/yourname/bidirectional-dcdc)

---

## Advanced Research Topics

- **Soft-Switching Techniques**  
  - ZVS / ZCS  
  - Resonant topologies (LLC, Phase-Shift Full Bridge)

- **High-Frequency Design Considerations**  
  - Parasitics and EMI control  
  - Gate driver optimisation and PCB layout

---
