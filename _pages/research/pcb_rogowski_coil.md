---
layout: single
title: "PCB Rogowski Coil Current Sensing"
permalink: /research/pcb-rogowski-coil/
author_profile: true
excerpt: "PCB Rogowski coils and signal-conditioning circuits for measuring fast current transients in power converters."
body_class: microgrid-project-page
project_stylesheet: /assets/css/marine-project.css
project_contents: true
mathjax: true
---

I designed PCB Rogowski coils and their signal-conditioning circuits for measuring fast current transients in power converters, then tested the complete sensing chain against a commercial Rogowski coil.

## How a Rogowski Coil Measures Current

A Rogowski coil is an air-cored winding placed around the conductor carrying the current to be measured. The changing magnetic field of that current induces a voltage in the winding proportional to the rate of change of current:

<div class="math-display">\[v_{\mathrm{coil}}(t)=M\frac{di(t)}{dt},\]</div>

where <i>M</i> is the mutual inductance between the conductor and the coil. An integrator in the signal-conditioning circuit converts this voltage back into a signal proportional to the current. Because there is no magnetic core to saturate, the coil suits large, fast-changing currents such as the switching transients of SiC converters; it does not measure steady DC current.

Building the winding on a PCB makes the coil compact, repeatable and easy to place close to power devices. Its geometry, return path and shielding set the sensitivity and the rejection of interference, and the conditioning circuit must manage gain, bandwidth and integrator offset.

## Coil and Signal-Conditioning Design

Starting from a review of existing coil designs and commercial specifications, I designed several PCB winding layouts and the amplification and integration circuitry that follows them. Each board places the coil and its conditioning electronics together, so the sensing element and output circuit can be assessed as one measurement chain.

<figure>
  <a href="/images/research/pcb-rogowski/circular-coil-pcb.png" target="_blank" rel="noopener"><img src="/images/research/pcb-rogowski/circular-coil-pcb.png" alt="PCB Rogowski coil design with a circular winding and integrated signal-conditioning circuitry" width="602" height="432"></a>
  <figcaption>Circular PCB winding with on-board amplification and integration stages.</figcaption>
</figure>

An alternative layout uses a rectangular winding around the aperture with the same conditioning chain.

<figure>
  <a href="/images/research/pcb-rogowski/rectangular-coil-pcb.png" target="_blank" rel="noopener"><img src="/images/research/pcb-rogowski/rectangular-coil-pcb.png" alt="PCB Rogowski sensor design with a rectangular winding and signal-conditioning components" width="602" height="457" loading="lazy"></a>
  <figcaption>Rectangular PCB winding with the same signal-conditioning chain.</figcaption>
</figure>

## Comparison with a Commercial Coil

I tested the designed sensing chain alongside a commercial Rogowski coil measuring the same current. The prototype's measured response was broadly in line with the commercial reference in these project tests. The comparison is qualitative: numerical error, bandwidth and measurement uncertainty for the prototype were not established in the published summary.

The design files are available in the [PCB Rogowski coil repository](https://github.com/FulongLi/PCB-Rogowski-Coil).

[PCB Current Transformer](/research/pcb-current-transformer/) · [Current Sensing](/research/sensing_devices/) · [Back to Research](/research/)
