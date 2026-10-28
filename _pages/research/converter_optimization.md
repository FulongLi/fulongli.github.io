---
layout: single
title: "Converter Design Optimisation"
permalink: /research/converter_optimization/
author_profile: true
body_class: marine-project-page converter-project-page
project_stylesheet: /assets/css/marine-project.css
project_contents: true
excerpt: "An integrated converter design framework connecting component evidence, electrical and thermal models, and engineering trade-offs."
---

I proposed an integrated framework for comparing power converter designs by **loss, mass and cost**, using consistent component data and electrical and thermal models. I defined its overall architecture and led its early and intermediate research and planning, and later continued the approach independently through [AIPE](/research/aipe/).

<h2 id="overview">Why Converter Design Is a Trade-Off</h2>

Converter design involves coupled choices. Raising the switching frequency shrinks the magnetic components but increases switching loss; that extra heat in turn demands a larger heat sink, which adds mass and cost. Each component is usually designed with its own tools and assumptions, so these interactions are hard to see. Comparing candidate designs fairly requires evaluating all components with consistent data under the same operating conditions.

<h2 id="design-framework">The Proposed Design Framework</h2>

<figure class="project-blueprint">
  <a href="/images/research/converter-optimization/proposed-design-framework.png" target="_blank" rel="noopener"><img src="/images/research/converter-optimization/proposed-design-framework.png" alt="Proposed converter optimisation framework linking component databases, characterisation, loss and thermal models, optimisation and engineering review" width="657" height="477" fetchpriority="high"></a>
  <figcaption>Proposed design framework, from requirements and component evidence to candidate designs and engineering review.</figcaption>
</figure>

The framework brings together **semiconductors, magnetics, capacitors and cooling**. Manufacturer data and characterisation results support reusable component models, so candidate designs can be evaluated under the same operating conditions. The diagram uses a buck converter to illustrate the workflow and outlines wider converter applications.

<h3 id="component-models">Design Variables, Models and Constraints</h3>

The workflow turns converter requirements into a design vector and evaluates the resulting component losses, mass and thermal requirements. Semiconductor models cover conduction, switching and diode behaviour; magnetic models connect core and winding choices to loss and mass; cooling models relate dissipation to thermal resistance and heat-sink mass; capacitor models complete the assessment. Candidate designs are compared against performance, thermal and geometric constraints, using weighted objectives or multi-objective methods such as GA and NSGA-II in the optimisation layer.

<h2 id="aipe-continuation">Implementation and Continuation</h2>

Parts of the framework have been implemented. The [SiC device-modelling project](/research/mosfet_ann_modelling/) demonstrates the semiconductor branch, connecting ANN loss models to converter experiments. The [public optimisation code](https://github.com/FulongLi/AIPE-Converter-Optimisation-Agent) implements a focused example: a nominal 1 kW, 430 V / 230 V buck-type inverter whose switch area, switching frequency, current ripple and junction-temperature rise are optimised for a weighted loss–volume objective with an SLSQP solver. Its thermal treatment is simplified and its component volume excludes the heat sink.

The complete architecture remains a proposed framework. My subsequent AIPE work builds on it, connecting component calculations to optimisation and neural-network surrogate modelling within a wider design workflow.

[AIPE](/research/aipe/) · [Back to Research](/research/)
