---
layout: single
title: "Current Sensing"
permalink: /research/sensing_devices/
author_profile: true
body_class: microgrid-project-page
project_stylesheet: /assets/css/marine-project.css
project_contents: true
mathjax: true
---

My current-sensing work concerns compact PCB-integrated sensors for power converters. The two approaches below explore different relationships between bandwidth, sensitivity, isolation and manufacturability.

## PCB Rogowski Coil (PCB-RC)

A PCB Rogowski coil uses an air-cored winding and an integrator to recover the current signal. PCB geometry, shielding and signal integration shape its suitability for fast switching measurements.

[PCB Rogowski coil project](https://github.com/FulongLi/Magnetics-PCBRogowskiCoil)

## Embedded-Core PCB Current Transformer (PCB-CT)

I designed a current transformer with a magnetic core embedded between PCB layers and a secondary winding formed by PCB traces and vias. The aim was to assess both the sensing concept and its suitability for repeatable, large-scale manufacturing. The primary conductor passes through the opening; its changing current couples magnetic flux into the core and induces a secondary signal. A current transformer measures changing current, so its low-frequency response and core saturation must be considered in the intended application.

<figure>
  <a href="/images/research/pcb-current-transformer/pcb-ct-perspective.png" target="_blank" rel="noopener"><img src="/images/research/pcb-current-transformer/pcb-ct-perspective.png" alt="Perspective rendering of a rectangular PCB current transformer with distributed secondary traces and central aperture" width="602" height="459"></a>
  <figcaption>PCB current transformer design with a distributed winding around the central aperture.</figcaption>
</figure>

### Design and Manufacturing Approach

The layout distributes the secondary turns around the aperture using PCB copper and vias. Embedding the magnetic material in the board brings the magnetic circuit and winding into a compact assembly; the investigation considered whether this construction could be manufactured at scale as well as whether it could sense current effectively. The design worksheet identifies the core material as **ferrite**; it does not identify a specific ferrite grade.

<figure>
  <a href="/images/research/pcb-current-transformer/pcb-ct-top.png" target="_blank" rel="noopener"><img src="/images/research/pcb-current-transformer/pcb-ct-top.png" alt="Top view of the PCB current transformer showing winding traces around the rectangular aperture" width="602" height="268" loading="lazy"></a>
  <figcaption>Top view of the PCB winding layout.</figcaption>
</figure>

### Design Calculation

The design workbook explores how turns ratio, ferrite geometry and permeability, winding resistance, burden resistance and parasitics influence current transfer and bandwidth. Its example uses the following assumptions and calculated values; these are **design estimates**, not measured ratings of the finished sensor.

| Worksheet parameter | Example value |
| --- | --- |
| Primary and secondary turns | 1 and 100 |
| Primary current input | 200 A |
| Relative permeability assumed | 125 |
| Effective magnetic path length | 20 mm |
| Assumed core cross-section | 6 mm × 2 mm |
| Secondary burden resistance | 10 Ω |
| Estimated magnetising inductance | 0.942 mH |
| Estimated lower corner frequency | approximately 1.8 kHz |

In the ideal turns-ratio calculation, the 200 A example gives a secondary current of 2 A. The worksheet estimates magnetising inductance and the lower-frequency corner using:

<div class="math-display">\[ I_s \approx \frac{N_p}{N_s}I_p, \qquad L_m \approx \frac{\mu_0\mu_r N_s^2 A_c}{l_c}, \qquad f_L \approx \frac{R_{Lm}}{2\pi L_m}. \]</div>

Here <i>A</i><sub>c</sub> and <i>l</i><sub>c</sub> are the assumed core cross-section and magnetic path length; <i>R</i><sub>Lm</sub> is the model's equivalent resistance seen by the magnetising branch. The estimate depends on the assumed material properties and load. The workbook also includes winding and parasitic calculations; its bandwidth model follows [Kondrath and Kazimierczuk, “Bandwidth of Current Transformers”](https://doi.org/10.1109/TIM.2008.2006134).

### Experimental Assessment

The prototype was evaluated for feasibility and manufacturability as well as sensing performance. In the experiments, its sensitivity and dynamic response were broadly comparable to a commercial Rogowski coil. This is a qualitative comparison from the project; numerical accuracy, bandwidth and production yield are not specified here.

[PCB current transformer design repository](https://github.com/FulongLi/Magnetics-PCBCurrentTransformerTransducer) · [Power Device Characterization](/research/switching_devices/) · [Back to Research](/research/)
