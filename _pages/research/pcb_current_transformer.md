---
layout: single
title: "Embedded-Core PCB Current Transformer"
permalink: /research/pcb-current-transformer/
author_profile: true
excerpt: "A current transformer with a ferrite core embedded in the PCB and a secondary winding formed by traces and vias."
body_class: microgrid-project-page
project_stylesheet: /assets/css/marine-project.css
project_contents: true
mathjax: true
---

I designed a current transformer whose magnetic core is embedded between PCB layers, with a secondary winding formed by PCB traces and vias. The aim was to assess both the sensing concept and whether the construction could be manufactured repeatably at scale.

## How a PCB Current Transformer Works

A current transformer couples the current in a primary conductor into a secondary winding through a magnetic core. The primary conductor passes through the opening in the core, and its changing current induces a secondary current scaled by the turns ratio:

<div class="math-display">\[I_s \approx \frac{N_p}{N_s}I_p.\]</div>

Unlike an air-cored Rogowski coil, the core concentrates the flux and the secondary delivers a current directly into a burden resistor, without an integrator. The core also brings two limits: a current transformer measures changing current only, so its low-frequency response depends on the magnetising inductance, and the core must not saturate in the intended application. Embedding the core in the board places the magnetic circuit and winding in one compact, galvanically isolated assembly.

<figure>
  <a href="/images/research/pcb-current-transformer/pcb-ct-perspective.png" target="_blank" rel="noopener"><img src="/images/research/pcb-current-transformer/pcb-ct-perspective.png" alt="Perspective rendering of a rectangular PCB current transformer with distributed secondary traces and central aperture" width="602" height="459"></a>
  <figcaption>PCB current transformer with the secondary winding distributed around the central aperture.</figcaption>
</figure>

## Winding Layout and Design Calculation

The layout distributes the secondary turns around the aperture using PCB copper and vias that wrap the embedded ferrite. I developed the board design together with a design workbook that relates turns ratio, ferrite geometry and permeability, winding resistance, burden resistance and parasitics to current transfer and bandwidth.

<figure>
  <a href="/images/research/pcb-current-transformer/pcb-ct-top.png" target="_blank" rel="noopener"><img src="/images/research/pcb-current-transformer/pcb-ct-top.png" alt="Top view of the PCB current transformer showing winding traces around the rectangular aperture" width="602" height="268" loading="lazy"></a>
  <figcaption>Top view of the secondary winding traces around the rectangular aperture.</figcaption>
</figure>

The workbook estimates the magnetising inductance and the lower corner frequency from the core geometry and the burden:

<div class="math-display">\[L_m \approx \frac{\mu_0\mu_r N_s^2 A_c}{l_c}, \qquad f_L \approx \frac{R_{Lm}}{2\pi L_m},\]</div>

where <i>A</i><sub>c</sub> and <i>l</i><sub>c</sub> are the core cross-section and magnetic path length, and <i>R</i><sub>Lm</sub> is the equivalent resistance seen by the magnetising branch. The worked example uses a ferrite core and the following values. They are design estimates, not measured ratings of the finished sensor.

| Workbook parameter | Example value |
| --- | --- |
| Primary and secondary turns | 1 and 100 |
| Primary current | 200 A, giving 2 A secondary current |
| Relative permeability | 125 |
| Effective magnetic path length | 20 mm |
| Core cross-section | 6 mm × 2 mm |
| Secondary burden resistance | 10 Ω |
| Estimated magnetising inductance | 0.942 mH |
| Estimated lower corner frequency | approximately 1.8 kHz |

## Experimental Assessment

I evaluated the prototype for manufacturability as well as sensing performance. In the experiments, its sensitivity and dynamic response were broadly comparable to a commercial Rogowski coil measuring the same current. This is a qualitative comparison: numerical accuracy, bandwidth and production yield were not established in the published summary.

The design files are available in the [PCB current transformer repository](https://github.com/FulongLi/Magnetics-PCBCurrentTransformerTransducer).

[PCB Rogowski Coil](/research/pcb-rogowski-coil/) · [Current Sensing](/research/sensing_devices/) · [Back to Research](/research/)
