---
layout: research
research_area: components
title: "Supporting Work: Inductor Design"
permalink: /research/passive_components/
excerpt: "Planar inductor designs and drawings prepared as supporting work for converter design."
---

## Context

Magnetic components set much of a converter's volume and a significant share of its loss, and at high switching frequency the winding loss depends strongly on layout. Planar inductors with PCB windings make that layout explicit and repeatable. This page records supporting design work rather than a standalone research project.

## What was done

I prepared inductor designs and their documentation: winding layouts, mechanical drawings and PDF design files for three inductors, published in a public repository. Inductor 1, shown below, uses a PCB winding through a pair of cores.

<figure>
  <a href="/images/research/magnetics/inductor1_d.png" target="_blank" rel="noopener"><img src="/images/research/magnetics/inductor1_d.png" alt="3D CAD render of a planar inductor: a PCB winding passing through two stacked rectangular cores" width="602" height="467" loading="lazy"></a>
  <figcaption><span class="figure-kind">Design render</span><strong>Planar inductor with a PCB winding.</strong> CAD render, not a photograph of tested hardware. <span class="figure-source">Public repository, inductor 1.</span></figcaption>
</figure>

## Evidence and limitations

The public material consists of drawings and design documents. Measured inductance, loss or temperature rise is not published, so no performance claims are made.

## Resources

- [Inductor design examples (GitHub, CC BY 4.0)](https://github.com/FulongLi/AIPE-Magnetics-Agnet-Inductor-Design-Example)
- [Converter design optimisation](/research/converter_optimization/) covers how passive-component volume and loss enter the converter design trade-off.
