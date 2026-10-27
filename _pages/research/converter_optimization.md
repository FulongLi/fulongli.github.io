---
layout: single
title: "Converter Design Optimisation"
permalink: /research/converter_optimization/
author_profile: true
body_class: marine-project-page converter-project-page
project_stylesheet: /assets/css/marine-project.css
excerpt: "An integrated converter design framework connecting component evidence, electrical and thermal models, and engineering trade-offs."
---

<h2 id="overview">Balancing Converter Performance and Size</h2>

Converter design involves coupled choices: reducing component size can increase loss, and the resulting heat changes the cooling requirement. I proposed an integrated framework to compare **loss, mass and cost** using consistent component data and electrical and thermal models.

The concept grew out of research and planning with **Cardiff University**. My contribution was the overall architecture and the early and intermediate planning; I later continued the broader framework independently through **AIPE**.

<h2 id="design-framework">From Component Evidence to Design Decisions</h2>

<figure class="project-blueprint">
  <a href="/images/research/converter-optimization/proposed-design-framework.png" target="_blank" rel="noopener"><img src="/images/research/converter-optimization/proposed-design-framework.png" alt="Proposed converter optimisation framework linking component databases, characterisation, loss and thermal models, optimisation and engineering review" width="657" height="477" fetchpriority="high"></a>
  <figcaption><strong>The proposed design framework.</strong> Requirements and component evidence feed models, candidate designs and engineering review. <span class="figure-source">Original framework supplied by Fulong Li.</span></figcaption>
</figure>

The framework brings together **semiconductors, magnetics, capacitors and cooling**. Manufacturer data and characterisation results support reusable models, allowing candidate designs to be evaluated under the same operating conditions. The [SiC device-modelling project](/research/mosfet_ann_modelling/) demonstrates one part of this approach by connecting ANN loss models to converter experiments.

The diagram uses a buck converter to illustrate the workflow and outlines wider converter applications. It records the proposed architecture; implementation of every branch remains outside the demonstrated scope.

<h2 id="aipe-continuation">Research Direction and Open Tools</h2>

Within the Cardiff collaboration, the team pursued a narrower software-based optimisation route under another colleague's lead. My subsequent AIPE work continued the integrated concept, connecting component calculations, optimisation and data-based surrogate models.

The value of the approach is a design process in which assumptions and trade-offs can be inspected together. The public repository provides a focused implementation example and supports further development of engineering design tools.

[Public converter optimisation code](https://github.com/FulongLi/AIPE-Converter-Optimisation-Agent) · [AIPE](/research/aipe/) · [Passive Components](/research/passive_components/) · [Back to Research](/research/)
