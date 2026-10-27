---
layout: research
research_area: components
title: "PCB-Integrated Current Sensing"
permalink: /research/sensing_devices/
excerpt: "PCB Rogowski coils and a PCB embedded-core current transformer developed for current measurement in fast-switching SiC converters."
---

## Engineering problem

SiC converters switch current in tens of nanoseconds, so the current sensor has to combine wide bandwidth with galvanic isolation and a small insertion footprint in a tightly laid-out power loop. Coaxial shunts and clamp-on probes work on a bench but are difficult to integrate into the converter itself. Building the sensor into the PCB keeps it in the commutation path without adding loop inductance or a separate mechanical part.

## Scope

Two sensor concepts were developed within the **ELIPS** (Enhanced Liquid-cooled Power Supplies) project at CSA Catapult, alongside the [LLC and DAB converter work](/research/isolated_converters/) for the same application:

- an **air-cored PCB Rogowski coil** with on-board signal conditioning; and
- a **PCB current transformer with an embedded magnetic core**.

## My contribution

I developed both sensor designs; the Rogowski sensor boards were designed together with a colleague. The coil variants and design drawings are published in a public repository under CC BY 4.0.

## PCB Rogowski coil {#pcb-rogowski-coil}

A Rogowski coil is an air-cored winding around the conductor. Its output voltage is proportional to the rate of change of the enclosed current, *v* = *M* d*i*/d*t*, so the current waveform is recovered by integration. Because there is no core, the coil does not saturate, which suits the large d*i*/d*t* and current pulses in SiC switching cells. The design questions are the mutual inductance *M* (set by turn count and winding cross-section), the coil's self-resonance, which limits bandwidth, and rejection of external fields, which depends on the return conductor.

<figure>
  <a href="/images/research/Rogcoil/RogT4_d.png" target="_blank" rel="noopener"><img src="/images/research/Rogcoil/RogT4_d.png" alt="3D CAD render of a PCB Rogowski coil board: a square coil around a circular conductor opening, followed by analogue conditioning stages with separate raw-output and final-output connectors" width="602" height="445" loading="lazy"></a>
  <figcaption><span class="figure-kind">Design render</span><strong>PCB Rogowski coil sensor board.</strong> The coil surrounds the conductor opening; the analogue stages between the raw-output and final-output connectors condition and integrate the coil signal. This is a CAD render, not a photograph of tested hardware. <span class="figure-source">Public repository PCB-Rogowski-Coil, coil type 4.</span></figcaption>
</figure>

The public repository contains five coil variants with top, bottom and layout views and a PDF design file for each.

## PCB embedded-core current transformer {#pcb-embedded-core-current-transformer}

The second concept places a magnetic core inside the PCB, with the secondary winding formed by tracks and vias around it. Compared with the air-cored coil, the core gives higher sensitivity at lower frequencies and a current output that does not need integration, at the cost of core saturation limits and the manufacturing constraints of embedding a core in a laminated board.

<figure>
  <a href="/images/research/CT/CT1_d.png" target="_blank" rel="noopener"><img src="/images/research/CT/CT1_d.png" alt="3D CAD render of a rectangular PCB with a central slot surrounded by a dense array of vias forming the current-transformer winding" width="602" height="459" loading="lazy"></a>
  <figcaption><span class="figure-kind">Design render</span><strong>PCB current-transformer winding.</strong> Vias and tracks around the rectangular opening form the secondary winding around the embedded core position. <span class="figure-source">Project design files.</span></figcaption>
</figure>

## Results and evidence

The evidence that is public at present is design evidence: the coil geometries, board layouts and design files. Measured sensitivity, bandwidth and comparison with a reference probe are not published here, so no performance figures are claimed for either sensor.

## Limitations

- No measured frequency response or calibration data is presented.
- The public current-transformer repository currently contains no documentation beyond its title.

## References and resources

- [PCB Rogowski coil designs (GitHub, CC BY 4.0)](https://github.com/FulongLi/PCB-Rogowski-Coil)
- [PCB current transformer (GitHub)](https://github.com/FulongLi/Magnetics-PCBCurrentTransformerTransducer)
