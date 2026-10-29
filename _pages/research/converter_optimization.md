---
layout: single
title: "Converter Design Optimisation"
permalink: /research/converter_optimization/
author_profile: true
body_class: marine-project-page converter-project-page
project_stylesheet: /assets/css/marine-project.css
project_contents: true
excerpt: "Multi-objective converter design: the optimal design process, an integrated framework for loss, volume and cost, and a Pareto study of a 1 kW buck-type inverter."
---

This work proposed an integrated framework for comparing power converter designs by **loss, mass and cost**, using consistent component data and electrical and thermal models. The author defined its overall architecture, led its early and intermediate research and planning, and later continued the approach independently through [AIPE](/research/aipe/).

<h2 id="overview">Why Converter Design Is a Trade-Off</h2>

Converter design involves coupled choices. Raising the switching frequency shrinks the magnetic components but increases switching loss; that extra heat in turn demands a larger heat sink, which adds mass and cost. Each component is usually designed with its own tools and assumptions, so these interactions are hard to see. Comparing candidate designs fairly requires evaluating all components with consistent data under the same operating conditions.

There is rarely a single best design. Improving one objective, such as efficiency, usually costs another, such as power density. Optimal design therefore looks for the set of designs in which no objective can improve without another getting worse, the **Pareto front**, and then chooses a point on it from the project's priorities.

<h2 id="design-process">The Optimal Design Process</h2>

<figure class="project-blueprint">
  <a href="/images/research/converter-optimization/design-process.svg" target="_blank" rel="noopener"><img src="/images/research/converter-optimization/design-process.svg" alt="Eight-step optimal converter design process from specification, design variables and constraints through component models, multi-objective search and the Pareto front to design selection and verification, with verified data fed back into the models" width="760" height="676" fetchpriority="high"></a>
  <figcaption>The optimal design process; steps 4 to 6 form the optimisation loop.</figcaption>
</figure>

1. **Specification.** Fix the ratings, voltages and operating range, and the limits on efficiency, temperature, volume and cost.
2. **Design variables.** Choose the quantities the optimiser may change, such as switch die area, switching frequency, current ripple and junction temperature rise, each within physical bounds.
3. **Constraints.** State what every design must satisfy: junction temperature, output ripple, core saturation, current density, clearance and insulation.
4. **Component models.** Express each component's loss and size as functions of the design variables, using consistent data for semiconductors, magnetics, capacitors and cooling.
5. **Multi-objective search.** Explore the design space by weighted-sum scalarisation, by genetic algorithms such as NSGA-II, or by sampling.
6. **Pareto front.** Keep only the non-dominated designs.
7. **Design selection.** Choose a point on the front, comparing candidates across efficiency, power density and component sizes.
8. **Verification.** Check the chosen design with detailed simulation and a prototype, and feed the verified data back into the models.

<h2 id="design-framework">The Proposed Design Framework</h2>

<figure class="project-blueprint">
  <a href="/images/research/converter-optimization/proposed-design-framework.png" target="_blank" rel="noopener"><img src="/images/research/converter-optimization/proposed-design-framework.png" alt="Proposed converter optimisation framework linking component databases, characterisation, loss and thermal models, optimisation and engineering review" width="657" height="477" loading="lazy"></a>
  <figcaption>Proposed design framework, from requirements and component evidence to candidate designs and engineering review.</figcaption>
</figure>

The framework brings together **semiconductors, magnetics, capacitors and cooling**. Manufacturer data and characterisation results support reusable component models, so candidate designs can be evaluated under the same operating conditions. The diagram uses a buck converter to illustrate the workflow and outlines wider converter applications.

<h2 id="example">Example: A 1 kW Buck-Type Inverter</h2>

The [optimisation code](https://github.com/FulongLi/AIPE-Converter-Optimisation-Agent) applies the process to a single-phase buck-type voltage-source inverter: 430 V to 230 V at a nominal 1 kW and 4.35 A. It reconstructs in Python a MATLAB design workflow from a collaboration with Cardiff University, with explicit physics-based loss and volume models.

| Design variable | Range |
| --- | --- |
| Switch die area | 0.35 to 4.5 times a 45.6 mm² reference die |
| Switching frequency | 50 to 300 kHz |
| Inductor current ripple | 10% to 50% of the output current |
| Junction temperature rise | up to 75 K above a 25 °C ambient |

For each design, the models sum the semiconductor loss (conduction, switching, output capacitance, reverse recovery and gate drive), the inductor loss and the capacitor loss, and the volumes of the switches, inductor and capacitor. The heat sink is not included in the volume. The objectives are efficiency and power density.

### Pareto Front

Sampling 60,000 designs across these ranges with the code's models shows the trade-off clearly. Along the front, efficiency falls from about 98.9% at 1.6 kW/dm³ to 96.2% at 9.7 kW/dm³. Moving along it, the switching frequency rises from 50 to 300 kHz and the die area shrinks: the passive components get smaller, while switching and conduction losses grow.

<figure class="project-blueprint">
  <a href="/images/research/converter-optimization/pareto-front.svg" target="_blank" rel="noopener"><img src="/images/research/converter-optimization/pareto-front.svg" alt="Efficiency against power density for 60,000 sampled designs, with the Pareto front from about 98.9% at 1.6 kW/dm³ to 96.2% at 9.7 kW/dm³ and three marked designs A, B and C" width="760" height="430" loading="lazy"></a>
  <figcaption>Efficiency against power density for 60,000 sampled designs, with the Pareto front and three selected designs.</figcaption>
</figure>

### Comparing Designs on the Front

Three designs on the front show what the choice involves. Each axis of the radar chart is scaled across the front, with outward always better, so a design's shape shows where it gains and what it gives up.

<figure class="project-blueprint">
  <a href="/images/research/converter-optimization/design-tradeoff-radar.svg" target="_blank" rel="noopener"><img src="/images/research/converter-optimization/design-tradeoff-radar.svg" alt="Radar chart of designs A, B and C on efficiency, power density, semiconductor loss and switch, inductor and capacitor volume" width="760" height="440" loading="lazy"></a>
  <figcaption>Trade-offs between the three selected designs; outward is better on every axis.</figcaption>
</figure>

| | A: High efficiency | B: Balanced | C: High power density |
| --- | --- | --- | --- |
| Efficiency | 98.8% | 97.6% | 96.9% |
| Power density | 2.2 kW/dm³ | 6.8 kW/dm³ | 8.8 kW/dm³ |
| Switching frequency | 62 kHz | 220 kHz | 289 kHz |
| Switch die area | 62 mm² | 30 mm² | 23 mm² |
| Semiconductor loss | 10.7 W | 23.2 W | 30.5 W |
| Switch / inductor / capacitor volume | 101 / 145 / 200 cm³ | 48 / 49 / 47 cm³ | 37 / 37 / 36 cm³ |

Design A uses large dies at low frequency, so it has the lowest loss but the largest inductor and capacitor. Design C switches nearly five times faster with smaller dies, shrinking the inductor and capacitor to between a quarter and a fifth of A's size at almost three times the semiconductor loss. Design B, at the knee of the front, keeps most of C's size reduction for a smaller loss penalty.

These are model results for comparing designs, not measured performance. The models simplify the thermal path and leave out the heat sink, which would penalise the high-loss designs further.

<h2 id="aipe-continuation">Implementation and Continuation</h2>

Parts of the framework have been implemented. The [SiC device-modelling project](/research/mosfet_ann_modelling/) demonstrates the semiconductor branch, connecting ANN loss models to converter loss calculations, and the optimisation code above trains a neural-network surrogate on its Pareto designs for fast evaluation.

The complete architecture remains a proposed framework. Subsequent AIPE work builds on it, connecting component calculations to optimisation and neural-network surrogate modelling within a wider design workflow.

[AIPE](/research/aipe/) · [Back to Research](/research/)
