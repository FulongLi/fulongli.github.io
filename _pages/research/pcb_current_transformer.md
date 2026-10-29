---
layout: single
title: "Embedded-Core PCB Current Transformer"
permalink: /research/pcb-current-transformer/
author_profile: true
excerpt: "A current transformer with a ferrite core embedded in the PCB and a secondary winding of traces and vias, sized with a design workbook for bandwidth, saturation and trace current."
body_class: microgrid-project-page
project_stylesheet: /assets/css/marine-project.css
project_contents: true
mathjax: true
---

This work designed a current transformer whose magnetic core is embedded between PCB layers, with a secondary winding formed by PCB traces and vias, and built a design workbook that sizes it for bandwidth, saturation and trace current. The construction aims at compact, isolated current sensing that can be manufactured repeatably at scale.

## How a PCB Current Transformer Works

A current transformer couples the current in a primary conductor into a secondary winding through a magnetic core. The primary conductor passes through the opening in the core, and its changing current induces a secondary current scaled by the turns ratio:

<div class="math-display">\[I_s \approx \frac{N_p}{N_s}I_p.\]</div>

Unlike an air-cored Rogowski coil, the core concentrates the flux and the secondary delivers a current directly into a burden resistor, without an integrator. The core also brings two limits: a current transformer measures changing current only, so its low-frequency response depends on the magnetising inductance, and the core must not saturate in the intended application.

The concept embeds a rectangular ferrite core in the board around a slot for the primary conductor. The secondary turns are routed as traces and vias along both long sides of the core and joined across the far end, with the terminals and protection diodes at the connector end.

<figure class="project-blueprint">
  <a href="/images/research/pcb-current-transformer/pcb-ct-concept-layout.png" target="_blank" rel="noopener"><img src="/images/research/pcb-current-transformer/pcb-ct-concept-layout.png" alt="Original PCB layout concept of the current transformer, with secondary turns along both long sides of a rectangular core around a central slot and the terminals at the connector end" width="1508" height="436" fetchpriority="high"></a>
  <figcaption>Original layout concept: secondary turns wrapped around the embedded core on both sides of the primary slot.</figcaption>
</figure>

## Equivalent Circuit and Bandwidth

Referred to the secondary, the transformer behaves as an ideal 1 : <i>n</i> transformer loaded by the magnetising inductance <i>L</i><sub>m</sub> and core-loss resistance <i>R</i><sub>c</sub>, followed by the leakage inductance <i>L</i><sub>l</sub>, winding resistance <i>R</i><sub>s</sub>, stray capacitance <i>C</i> and the burden <i>R</i>. The workbook follows the bandwidth model of [Kondrath and Kazimierczuk](https://doi.org/10.1109/TIM.2008.2006134).

<figure class="project-blueprint">
  <a href="/images/research/pcb-current-transformer/ct-equivalent-circuit.svg" target="_blank" rel="noopener"><img src="/images/research/pcb-current-transformer/ct-equivalent-circuit.svg" alt="Current transformer equivalent circuit referred to the secondary, from the primary current source through the ideal transformer, core, winding and stray elements to the burden resistor" width="760" height="246" loading="lazy"></a>
  <figcaption>Current transformer equivalent circuit, referred to the secondary.</figcaption>
</figure>

The core geometry sets the magnetising inductance and core-loss resistance, with core path length <i>l</i><sub>c</sub>, cross-section <i>A</i><sub>c</sub>, permeability μ<sub>r</sub> and ferrite resistivity ρ<sub>c</sub>:

<div class="math-display">\[L_m=\frac{\mu_0\mu_r n^2 A_c}{l_c},\qquad R_c=\frac{\rho_c\,l_c}{A_c}.\]</div>

At low frequency, <i>L</i><sub>m</sub> shunts current away from the burden; the lower corner is set by the resistance it sees. At high frequency, the stray capacitance and the leakage inductance each add a pole:

<div class="math-display">\[f_L=\frac{R_{Lm}}{2\pi L_m},\qquad R_{Lm}=R_c\parallel(R+R_s),\]</div>

<div class="math-display">\[\frac{1}{f_H^2}=\frac{1}{f_{p1}^2}+\frac{1}{f_{p2}^2},\qquad f_{p1}=\frac{1}{2\pi RC},\qquad f_{p2}=\frac{R_c}{2\pi L_l}.\]</div>

The usable bandwidth is <i>f</i><sub>H</sub> − <i>f</i><sub>L</sub>. More turns or a higher-permeability core lower <i>f</i><sub>L</sub>; a smaller burden or less stray capacitance raises <i>f</i><sub>H</sub>.

## Design Calculation

The workbook takes the core, winding and burden as inputs, then returns the corner frequencies, the saturation margin and the minimum trace width. For a 200 A primary current through a single primary turn:

| Input | Value |
| --- | --- |
| Turns, primary and secondary | 1 and 100, giving 2 A secondary current |
| Ferrite core | 20 mm path length, 6 mm × 2 mm cross-section, μ<sub>r</sub> = 125, ρ<sub>c</sub> = 10 Ω·m |
| Secondary winding | 2 oz (70 µm) copper, 0.4 mm traces, 5 mm per turn, 1 m in total |
| Burden | 10 Ω, with 0.1 µH series inductance |
| Parasitics | 0.126 µH leakage inductance, 0.81 nF stray capacitance |

| Result | Value |
| --- | --- |
| Magnetising inductance <i>L</i><sub>m</sub> | 0.942 mH |
| Core-loss resistance <i>R</i><sub>c</sub> | 16.7 kΩ |
| Winding resistance <i>R</i><sub>s</sub> | 0.62 Ω |
| Lower corner <i>f</i><sub>L</sub> | 1.8 kHz |
| Upper corner <i>f</i><sub>H</sub> | 19.7 MHz, set by the burden and stray capacitance; the leakage pole lies near 21 GHz |
| Bandwidth | about 19.7 MHz |
| Saturation current, secondary | 7.2 A, against 2 A in operation |
| Minimum trace width for 2 A at 10 °C rise | 0.39 mm, met by the 0.4 mm traces |
| Burden dissipation at 2 A | 40 W |

These are design estimates, not measured ratings of a finished sensor. The last line shows the main trade-off at this current: a 10 Ω burden carrying the full 2 A must dissipate 40 W, so a lower burden or more secondary turns would be needed for a practical sensor.

## Board Design

From the concept, the board was designed with the secondary winding distributed around the central aperture, so the magnetic circuit and winding form one compact, galvanically isolated assembly.

<figure class="half">
  <a href="/images/research/pcb-current-transformer/pcb-ct-perspective.png" target="_blank" rel="noopener"><img src="/images/research/pcb-current-transformer/pcb-ct-perspective.png" alt="Perspective rendering of the rectangular PCB current transformer with distributed secondary traces and central aperture" width="602" height="459" loading="lazy"></a>
  <a href="/images/research/pcb-current-transformer/pcb-ct-top.png" target="_blank" rel="noopener"><img src="/images/research/pcb-current-transformer/pcb-ct-top.png" alt="Top view of the PCB current transformer showing winding traces around the rectangular aperture" width="602" height="268" loading="lazy"></a>
  <figcaption>PCB current transformer in perspective (left) and from the top (right), with the secondary winding around the aperture.</figcaption>
</figure>

The design files are available in the [PCB current transformer repository](https://github.com/FulongLi/Magnetics-PCBCurrentTransformerTransducer).

[PCB Rogowski Coil](/research/pcb-rogowski-coil/) · [Current Sensing](/research/sensing_devices/) · [Back to Research](/research/)
