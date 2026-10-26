---
layout: single
title: "Converter Optimization"
permalink: /research/converter_optimization/
author_profile: true
excerpt: "Multi-objective converter design and neural-network modelling, from a collaboration with Cardiff University."
---

## Overview

**Overview:** Multi-objective converter optimisation connecting semiconductor loss modelling, passive component selection, and loss–volume and efficiency trade-offs.

**My contribution:** Developed a component-modelling and optimisation workflow through collaboration with Cardiff University, including AI-assisted modelling.

**Outcome / evidence:** Calculated results, reproducibility resources, and model limitations are retained below. See also [AIPE](/research/aipe/) and [Semiconductor Device Modelling](/research/mosfet_ann_modelling/).

Developed through my collaboration with **Cardiff University**, this project explores a practical design question: **how can a power converter become more compact without sacrificing efficiency?**

The case study is a **single-phase buck-type voltage-source inverter**, using a nominal **1 kW, 430 V / 230 V** benchmark. The workflow connects component models, multi-objective optimisation, and a neural-network surrogate to support design decisions.

## What the Project Does

- **Models the components:** estimates semiconductor, inductor, and capacitor losses and volumes.
- **Explores design trade-offs:** varies switch area, switching frequency, current ripple, and junction-temperature rise, balancing total loss against component volume.
- **Builds a learning model:** trains a small neural network on the computed designs to predict loss and volume from design parameters.

The aim is to make the relationship between component choices and converter performance visible, so designers can compare alternatives before committing to hardware.

## Results from the Python Model

An illustrative run on **26 October 2026** evaluated **21 loss–volume weightings**. Giving more weight to low loss produced larger, more efficient designs; prioritising compactness increased loss.

![Modelled efficiency versus power density for 21 design weightings, highlighting volume-focused, equal-weight, and loss-focused designs.](/files/research/converter-optimization/design-tradeoff.png)

| Design emphasis | Component volume | Modelled efficiency |
|---|---:|---:|
| Compactness | 146.7 cm³ | 96.51% |
| Equal loss–volume weighting | 181.3 cm³ | 97.98% |
| Low loss | 205.7 cm³ | 98.04% |

At equal weighting, the model attributes most losses to the semiconductors, while volume is shared more evenly between switches, inductors, and capacitors. This helps identify which component choices deserve closer attention.

*These are calculated results from the public Python reconstruction, not hardware measurements or a reproduction of the original MATLAB results. The model uses calibrated component volumes and simplified thermal assumptions.*

<details>
  <summary>Component breakdown and calculation details</summary>
  <p><img src="/files/research/converter-optimization/component-breakdown.png" alt="Component volume and loss contributions for the equal-weight design, showing semiconductors dominate the modelled losses." loading="lazy"></p>
  <p>The unmodified implementation uses a weighted loss–volume objective and an SLSQP solver. All 21 runs reported success, but switching frequency remained near its 175 kHz starting value; these points do not establish a globally optimal Pareto front. Junction-temperature rise is an independent bounded input rather than a coupled thermal solution. Volume excludes the heat sink.</p>
  <p>Efficiency follows the repository's convention: 100 × (1,000 W − modelled loss) / 1,000 W. The neural-network training pipeline also ran on the 21 designs; prediction accuracy on independent designs has not been established.</p>
  <p><a href="/files/research/converter-optimization/design-sweep.csv">Download all design results (CSV)</a> · <a href="/files/research/converter-optimization/run-metadata.json">Run details and assumptions</a> · <a href="/files/research/converter-optimization/reproduce.py">Reproduce the figures (Python)</a></p>
</details>

## Project Resources

[View the project on GitHub](https://github.com/FulongLi/AIPE-Converter-Optimisation-Agent) · [Back to Research](/research/)
