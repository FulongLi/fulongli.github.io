---
layout: research
research_area: converters
title: "Multi-Objective Converter Design Optimisation"
permalink: /research/converter_optimization/
excerpt: "Loss–volume trade-off study for a 1 kW single-phase buck-type inverter, with a neural-network surrogate, reproduced in public Python code."
---

## Engineering problem

Making a converter smaller usually costs efficiency: a higher switching frequency shrinks the passive components but raises switching loss, and a smaller semiconductor area raises conduction loss and temperature. The design variables interact, so a designer needs to see the whole loss–volume trade-off rather than optimise one component at a time.

## Objective and scope

Build a component-level loss and volume model of a converter, explore its loss–volume trade-off, and train a neural-network surrogate on the computed designs. The benchmark is a **single-phase buck-type voltage-source inverter, nominally 1 kW, 430 V DC to 230 V AC**. The work was done at CSA Catapult in collaboration with Cardiff University.

## My contribution

Within the project I reviewed passive components and switching devices, built the transistor loss models, defined the objective function and trained the AI-assisted surrogate. I then wrote the public Python reconstruction that produces the results below.

## Method

- **Component models:** semiconductor, inductor and capacitor loss and volume as functions of four decision variables: switch area *A*<sub>sw</sub>, switching frequency *f*<sub>sw</sub>, current ripple *I*<sub>ripple</sub> and junction-temperature rise Δ*T*<sub>j</sub>.
- **Trade-off exploration:** a weighted-sum objective of normalised loss and volume, solved with SciPy SLSQP for 21 weightings.
- **Surrogate:** a small multilayer perceptron trained on the computed designs to predict loss and volume from the decision variables.

## Results from the public Python model

An illustrative run on **26 October 2026** evaluated the 21 loss–volume weightings. Weighting low loss produced larger, more efficient designs; weighting compactness increased loss.

![Modelled efficiency versus power density for 21 design weightings, highlighting volume-focused, equal-weight and loss-focused designs.](/files/research/converter-optimization/design-tradeoff.png)

| Design emphasis | Component volume | Modelled efficiency |
|---|---:|---:|
| Compactness | 146.7 cm³ | 96.51 % |
| Equal loss–volume weighting | 181.3 cm³ | 97.98 % |
| Low loss | 205.7 cm³ | 98.04 % |

At equal weighting the model attributes most of the loss to the semiconductors, while volume is shared more evenly between switches, inductors and capacitors, which in this model makes the semiconductor choice the first lever on efficiency.

<details>
  <summary>Component breakdown and calculation details</summary>
  <p><img src="/files/research/converter-optimization/component-breakdown.png" alt="Component volume and loss contributions for the equal-weight design, showing semiconductors dominate the modelled losses." loading="lazy"></p>
  <p>All 21 SLSQP runs reported success, but switching frequency stayed near its 175 kHz starting value, so these points do not establish a globally optimal Pareto front. Junction-temperature rise is an independent bounded input rather than a coupled thermal solution, and volume excludes the heat sink.</p>
  <p>Efficiency is 100 × (1,000 W − modelled loss) / 1,000 W. The surrogate training also ran on the 21 designs; its accuracy on independent designs has not been established.</p>
  <p><a href="/files/research/converter-optimization/design-sweep.csv">All design results (CSV)</a> · <a href="/files/research/converter-optimization/run-metadata.json">Run details and assumptions</a> · <a href="/files/research/converter-optimization/reproduce.py">Reproduce the figures (Python)</a></p>
</details>

## Limitations

- These are calculated results from the public Python reconstruction, not hardware measurements, and not a reproduction of the original MATLAB results: the original convex-optimisation scripts were not available to port, and component volumes are calibrated.
- The optimiser did not move switching frequency far from its initial value, so the trade-off curve should be read as indicative.

## References and resources

- T. Jin, Z. Feng, J. Liang, R. Navaratne, F. Li, S. Wang, “[Explainable Multi-Objective Optimization for Data-Driven Design: Application to Power Converters](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7021149),” SSRN preprint, 2026. Related preprint by the collaboration; not peer reviewed.
- [AIPE-Converter-Optimisation-Agent (GitHub)](https://github.com/FulongLi/AIPE-Converter-Optimisation-Agent): Python reconstruction, Pareto sweep and surrogate training.
- Related: [ANN-based device modelling](/research/mosfet_ann_modelling/) · [AIPE](/research/aipe/)
