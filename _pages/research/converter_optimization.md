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

<h2 id="overview">Balancing Converter Performance and Size</h2>

Converter design involves coupled choices: reducing component size can increase loss, and the resulting heat changes the cooling requirement. I proposed an integrated framework to compare **loss, mass and cost** using consistent component data and electrical and thermal models.

My contribution was the overall architecture and the early and intermediate research and planning. I later continued the broader framework independently through **AIPE**.

<h2 id="design-framework">From Component Evidence to Design Decisions</h2>

<figure class="project-blueprint">
  <a href="/images/research/converter-optimization/proposed-design-framework.png" target="_blank" rel="noopener"><img src="/images/research/converter-optimization/proposed-design-framework.png" alt="Proposed converter optimisation framework linking component databases, characterisation, loss and thermal models, optimisation and engineering review" width="657" height="477" fetchpriority="high"></a>
  <figcaption>The proposed design framework.</figcaption>
</figure>

Requirements and component evidence feed models, candidate designs and engineering review.

The framework brings together **semiconductors, magnetics, capacitors and cooling**. Manufacturer data and characterisation results support reusable models, allowing candidate designs to be evaluated under the same operating conditions. The [SiC device-modelling project](/research/mosfet_ann_modelling/) demonstrates one part of this approach by connecting ANN loss models to converter experiments.

The diagram uses a buck converter to illustrate the workflow and outlines wider converter applications. It records the proposed architecture; implementation of every branch remains outside the demonstrated scope.

<h2 id="component-models">Design Variables, Models and Constraints</h2>

The proposed workflow turns converter requirements into a design vector and evaluates the associated component losses, mass and thermal requirements. Semiconductor characteristics include conduction, switching and diode behaviour; magnetic models connect core and winding choices to loss and mass; cooling models relate dissipation to thermal resistance and cooling mass. Capacitor models complete the component assessment.

Candidate designs are compared against performance, thermal and geometric constraints. The architecture considers weighted objectives and multi-objective methods such as GA and NSGA-II. These are choices in the proposed optimisation layer, rather than a claim that every algorithm in the diagram was implemented.

The public implementation is a narrower example: a nominal 1 kW, 430 V / 230 V buck-type inverter calculation varies switch area, switching frequency, current ripple and junction-temperature rise, using a weighted loss–volume objective and an SLSQP solver. Its thermal treatment is simplified and component volume excludes the heat sink, so it illustrates the design calculation within those assumptions.

<h2 id="aipe-continuation">Research Direction and Open Tools</h2>

The original architecture remains a proposed framework. My subsequent AIPE work connects component calculations to a focused optimisation implementation and neural-network surrogate modelling.

The value of the approach is a design process in which assumptions and trade-offs can be inspected together. The public repository provides a focused implementation example and supports further development of engineering design tools.

[Public converter optimisation code](https://github.com/FulongLi/AIPE-Converter-Optimisation-Agent) · [AIPE](https://aipel.co.uk/) · [Passive Components](/research/passive_components/) · [Back to Research](/research/)
