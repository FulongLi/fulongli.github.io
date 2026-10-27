---
layout: research
research_area: aipe
title: "AIPE: AI for Power Engineering"
permalink: /research/aipe/
excerpt: "Data-driven device models, surrogate-based converter optimisation and open engineering tools for power electronics."
lede: "AIPE groups the parts of my work where data-driven models replace or speed up conventional engineering calculations, together with the open code that makes them inspectable."
---

## Scope

Power electronics design repeatedly evaluates the same physical relationships: device loss as a function of operating point, junction temperature as a function of dissipated power, converter loss and volume as functions of design variables. Where those relationships come from measurements or expensive models, a trained surrogate can make them fast enough to use inside optimisation loops. The engineering value depends on the quality of the underlying data and on testing the surrogate against independent evidence, so each project below states what has and has not been validated.

## Projects

| Project | What the model does | How it is checked |
|---|---|---|
| [ANN-based SiC MOSFET modelling](/research/mosfet_ann_modelling/) | Conduction, switching-energy and thermal-impedance models for converter loss calculation | Comparison with a laboratory buck converter (industrial project); held-out reference points (public model) |
| [Multi-objective converter optimisation](/research/converter_optimization/) | Loss–volume trade-off of a 1 kW inverter and a surrogate trained on computed designs | Public reproducible calculation; surrogate accuracy on independent designs not yet established |

## Open-source engineering tools and resources {#open-source-engineering-tools-and-resources}

The public repositories are the inspectable part of this work. Their descriptions are documentation, not measured results.

- [AIPE-MOSFET-ANN-Modelling](https://github.com/FulongLi/AIPE-MOSFET-ANN-Modelling): device loss and thermal models with a web interface.
- [AIPE-Converter-Optimisation-Agent](https://github.com/FulongLi/AIPE-Converter-Optimisation-Agent): converter loss–volume optimisation in Python.
- [Spirit Connect AIPE Labs](https://github.com/FulongLi/Spirit-Connect-AIPE-Labs): index of the AIPE repositories.
- AIPE web resources: [Academy](https://aipel.co.uk/academy/) (engineering knowledge), [Hub](https://aipel.co.uk/hub/) (data, models and tools), [Frontiers](https://aipel.co.uk/frontiers/) (open research).
