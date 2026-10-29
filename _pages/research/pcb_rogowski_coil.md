---
layout: single
title: "PCB Rogowski Coil Current Sensing"
permalink: /research/pcb-rogowski-coil/
author_profile: true
excerpt: "A review of PCB Rogowski coil winding shapes and their trade-offs, and five coil designs with on-board signal conditioning for fast current transients in power converters."
body_class: microgrid-project-page
project_stylesheet: /assets/css/marine-project.css
project_contents: true
mathjax: true
---

I reviewed how PCB Rogowski coils have developed and how their winding shape affects sensing, then designed a family of five PCB coils, each with its own signal-conditioning circuit, for measuring fast current transients in power converters.

## How a Rogowski Coil Measures Current

A Rogowski coil is an air-cored winding placed around the conductor carrying the current to be measured. The changing magnetic field of that current induces a voltage in the winding proportional to the rate of change of current:

<div class="math-display">\[v_{\mathrm{coil}}(t)=M\frac{di(t)}{dt},\]</div>

where <i>M</i> is the mutual inductance between the conductor and the coil. Because there is no magnetic core to saturate, the coil suits large, fast-changing currents such as the switching transients of SiC converters; it does not measure steady DC current.

On a PCB, the winding is formed by traces on the top and bottom layers joined by vias, so each turn has a rectangular cross-section set by the board thickness <i>h</i> and the inner and outer radii <i>a</i> and <i>b</i>. For <i>N</i> evenly spaced turns:

<div class="math-display">\[M=\frac{\mu_0 N h}{2\pi}\ln\frac{b}{a}.\]</div>

More turns, a thicker board or a wider winding raise the sensitivity. An integrator then recovers a signal proportional to the current, with gain set by its time constant τ:

<div class="math-display">\[v_{\mathrm{out}}(t)=\frac{1}{\tau}\int v_{\mathrm{coil}}\,dt=\frac{M}{\tau}\,i(t).\]</div>

The integrator's gain, bandwidth and offset drift therefore matter as much as the coil itself.

## Winding Shapes and Their Trade-Offs

My review traced three development paths: coils wound on flexible formers, rigid windings on PCB, and windings on flexible PCB. It compared literature and commercial designs by winding shape and size, current range, sensitivity, bandwidth and external circuitry. On a rigid PCB, the winding shape is the main design choice, and four features recur.

<figure class="project-blueprint">
  <a href="/images/research/pcb-rogowski/winding-shapes.svg" target="_blank" rel="noopener"><img src="/images/research/pcb-rogowski/winding-shapes.svg" alt="Schematic top views of a radial sawtooth winding, a square fishbone winding, a radial winding with a return line along its mean path, and a square winding with a cutout" width="760" height="290" fetchpriority="high"></a>
  <figcaption>PCB winding shapes: radial sawtooth, square fishbone, a return line along the mean path, and a cutout that opens the coil.</figcaption>
</figure>

| Shape or feature | Advantages | Limitations |
| --- | --- | --- |
| Radial, sawtooth traces | Uniform turn density around the aperture, so the output depends little on the conductor's position; symmetric and simple to lay out | Turn count limited by the via pitch on the inner circle; board area grows with the aperture; a poor fit around rectangular busbars |
| Square, fishbone traces | Straight, parallel turns use board area efficiently and suit rectangular conductors and busbars | Turn density changes at the corners, so the output is more sensitive to conductor position and nearby conductors |
| Without return line | Simplest routing, with the fewest layers and vias | A winding that advances once around the aperture also forms one large turn in the board plane, which picks up fields perpendicular to the board |
| With return line | A conductor brought back along the mean path cancels that turn, improving rejection of external fields | Needs an extra trace or layer, and the return path must follow the winding's mean path closely |
| Split or cutout | Fits around an existing conductor without disconnecting it | The gap breaks the closed path, adding position sensitivity and pickup from external fields; alignment at the gap matters |
| Flexible former or flexible PCB | Wraps conductors of different shapes and sizes | Turn spacing and cross-section are less repeatable than on a rigid PCB, and the output varies with bending and placement |

## My Coil Designs

From the review, I designed five PCB coils in July 2024 that vary one feature at a time: the winding shape, the return line and the cutout. Each board places the coil beside the same signal-conditioning chain, with amplification and integration stages and coaxial connectors for the raw coil output and the final output, so the coil designs can be assessed with identical electronics.

| Design | Winding | Return line | Shape |
| --- | --- | --- | --- |
| Type 1 | Sawtooth | No | Radial |
| Type 2 | Sawtooth | Yes | Radial |
| Type 3 | Fishbone | No | Square |
| Type 4 | Fishbone | Yes | Square |
| Type 5 | Fishbone | Yes | Square with cutout |

### Radial Sawtooth Coil

Type 1 uses the circular, radial winding: traces run outwards on one layer and step back at an angle on the other, giving the sawtooth pattern and an even turn density around the aperture. Type 2 adds the return line to the same winding.

<figure>
  <a href="/images/research/pcb-rogowski/circular-coil-pcb.png" target="_blank" rel="noopener"><img src="/images/research/pcb-rogowski/circular-coil-pcb.png" alt="Type 1 PCB Rogowski coil board with a radial sawtooth winding beside its signal-conditioning circuit" width="602" height="432" loading="lazy"></a>
  <figcaption>Type 1: radial sawtooth winding without return line, beside the signal-conditioning chain.</figcaption>
</figure>

### Square Fishbone Coil with Cutout

Type 5 uses the square fishbone winding with a return line, and a cutout from the aperture to the board edge, so the board can be slid around a conductor that is already in place.

<figure>
  <a href="/images/research/pcb-rogowski/square-cutout-coil-pcb.png" target="_blank" rel="noopener"><img src="/images/research/pcb-rogowski/square-cutout-coil-pcb.png" alt="Type 5 PCB Rogowski coil board with a square fishbone winding, return line and a cutout from the aperture to the board edge" width="602" height="462" loading="lazy"></a>
  <figcaption>Type 5: square fishbone winding with return line and cutout.</figcaption>
</figure>

The board renders and design files of all five coils are in the [PCB Rogowski coil repository](https://github.com/FulongLi/PCB-Rogowski-Coil).

[PCB Current Transformer](/research/pcb-current-transformer/) · [Current Sensing](/research/sensing_devices/) · [Back to Research](/research/)
