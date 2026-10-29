---
layout: single
title: "PCB Rogowski Coil Current Sensing"
permalink: /research/pcb-rogowski-coil/
author_profile: true
excerpt: "A review of how the Rogowski coil developed and how PCB winding patterns trade off, and five PCB coil designs with on-board signal conditioning for fast current transients in power converters."
body_class: microgrid-project-page
project_stylesheet: /assets/css/marine-project.css
project_contents: true
mathjax: true
---

I reviewed how the Rogowski coil developed, from its origins to coils built into power modules, and how PCB winding patterns trade off against each other. Building on that review, I designed a family of five PCB coils, each with its own signal-conditioning circuit, for measuring fast current transients in power converters.

## How a Rogowski Coil Measures Current

A Rogowski coil is an air-cored winding placed around the conductor carrying the current to be measured. The changing magnetic field of that current induces a voltage in the winding proportional to the rate of change of current:

<div class="math-display">\[v_{\mathrm{coil}}(t)=M\frac{di(t)}{dt},\]</div>

where <i>M</i> is the mutual inductance between the conductor and the coil. Because there is no magnetic core to saturate, the coil suits large, fast-changing currents such as the switching transients of SiC converters; it does not measure steady DC current.

On a PCB, the winding is formed by traces on the top and bottom layers joined by vias, so each turn has a rectangular cross-section set by the board thickness <i>h</i> and the inner and outer radii <i>a</i> and <i>b</i>. For <i>N</i> evenly spaced turns:

<div class="math-display">\[M=\frac{\mu_0 N h}{2\pi}\ln\frac{b}{a}.\]</div>

More turns, a thicker board or a wider winding raise the sensitivity. An integrator then recovers a signal proportional to the current, with gain set by its time constant τ:

<div class="math-display">\[v_{\mathrm{out}}(t)=\frac{1}{\tau}\int v_{\mathrm{coil}}\,dt=\frac{M}{\tau}\,i(t).\]</div>

The integrator's gain, bandwidth and offset drift therefore matter as much as the coil itself.

## Development of the Rogowski Coil

My review, completed in 2022, followed the coil through some 40 publications. The principle predates the coil itself: Chattock's magnetic potentiometer of 1887 measured the line integral of the magnetic field, and Rogowski and Steinhaus described the coil in 1912. From the 1960s, flexible wound coils were developed for wideband and pulsed-power measurement, with currents up to the megampere range. A 1995 patent placed the winding on a printed circuit board, and PCB coils were soon applied to fast power-electronic switching. Since 2014, the coils have moved into the converter itself: compact sensors beside SiC MOSFETs, gate-drive protection, and micro coils embedded in IGBT modules, busbars and GaN half-bridges.

<figure class="project-blueprint">
  <a href="/images/research/pcb-rogowski/development-timeline.svg" target="_blank" rel="noopener"><img src="/images/research/pcb-rogowski/development-timeline.svg" alt="Timeline of the Rogowski coil from Chattock in 1887 and Rogowski in 1912, through wideband and pulsed-power coils and rigid PCB coils, to coils integrated into SiC, GaN and IGBT modules, followed by my review and designs" width="760" height="398" fetchpriority="high"></a>
  <figcaption>Development of the Rogowski coil, from my review; the key references are listed at the end of this page.</figcaption>
</figure>

## Winding Patterns and Their Trade-Offs

On a PCB, the pattern of the turns decides how well the coil rejects current that flows outside it. A coil that responds only to the current through its aperture must close its path completely and must not form loops that link external fields. Koga, Tsukuda, Nakashima and Omura compared four patterns built on four-layer boards, using 9 mm coils whose main winding runs on the outer layers and through-holes [(Koga et al., 2016)](http://hdl.handle.net/10228/5769).

<figure class="project-blueprint">
  <a href="/images/research/pcb-rogowski/winding-shapes.svg" target="_blank" rel="noopener"><img src="/images/research/pcb-rogowski/winding-shapes.svg" alt="Schematic of four PCB winding patterns seen from above: fishbone with return line, saw, triangle, and fishbone without return line" width="760" height="248" loading="lazy"></a>
  <figcaption>The four winding patterns compared by Koga et al., redrawn schematically.</figcaption>
</figure>

| Pattern | Construction | Trade-off | Maximum error from an outside current |
| --- | --- | --- | --- |
| Fishbone | Each turn stands perpendicular to the coil path, with short steps between turns and a return line | Removes unwanted flux paths as far as the PCB process allows; its rejection improves as trace and via pitch shrink | 7% |
| Saw | Traces on one layer cross the path at right angles; traces on the other slant forward to the next turn | Simple to route, and lowest error on one scan path (4%), but the slanted traces leave flux paths that external fields couple into | 10% |
| Triangle | Traces on both layers slant, in opposite directions | Symmetric zigzag, but both slanted layers open the largest unwanted flux paths | 26% |
| Fishbone without return line | Fishbone turns, no return line | Simplest routing, but the winding's advance around the aperture forms a single loop that links external fields | 218% |

The error is the signal from a current flowing outside the coil, relative to the same current through the centre of the aperture, taken as the maximum over four scan paths with the conductor touching the board through 0.1 mm of insulation. The comparison shows two lessons. A return line is essential: without it, the outside-current error rises by more than an order of magnitude. Among the patterns with a return line, the fishbone keeps the turns closest to ideal and rejects outside current best. The same study found the sensitivity to the inside current uniform within −1.1% to +0.7% across the aperture thanks to the return line, and developed both closed and clamp-type coils, the latter opening to fit around an existing conductor.

## My Coil Designs

From the review, I designed five PCB coils in July 2024 that vary one feature at a time: the winding pattern, the return line and the outline. Types 1 and 2 use the saw (sawtooth) pattern on a circular outline, without and with a return line. Types 3 and 4 use the fishbone pattern on a square outline, without and with a return line. Type 5 adds a cutout from the aperture to the board edge, so that the coil can be slid around a conductor that is already in place, in the manner of a clamp-type coil. Each board places its coil beside the same signal-conditioning chain, with amplification and integration stages and coaxial connectors for the raw coil output and the final output, so the coils can be compared with identical electronics.

<figure class="project-blueprint">
  <a href="/images/research/pcb-rogowski/coil-designs.png" target="_blank" rel="noopener"><img src="/images/research/pcb-rogowski/coil-designs.png" alt="Five PCB Rogowski coils side by side: two circular saw windings, without and with return line, two square fishbone windings, without and with return line, and a square fishbone winding with a cutout to the board edge" width="1046" height="236" loading="lazy"></a>
  <figcaption>The five coil designs, Types 1 to 5 from left to right, cropped from the board renders.</figcaption>
</figure>

| | Type 1 | Type 2 | Type 3 | Type 4 | Type 5 |
| --- | --- | --- | --- | --- | --- |
| Pattern | Saw | Saw | Fishbone | Fishbone | Fishbone |
| Return line | No | Yes | No | Yes | Yes |
| Outline | Circular | Circular | Square | Square | Square with cutout |

The complete boards and design files of all five coils are in the [PCB Rogowski coil repository](https://github.com/FulongLi/PCB-Rogowski-Coil).

## Key References

1. A. P. Chattock, "On a magnetic potentiometer," *Philosophical Magazine*, 1887.
2. W. Rogowski and W. Steinhaus, "Die Messung der magnetischen Spannung," *Archiv für Elektrotechnik*, 1912.
3. J. Cooper, "On the high-frequency response of a Rogowski coil," *Journal of Nuclear Energy, Part C*, 1963.
4. D. G. Pellinen et al., "Rogowski coil for measuring fast, high-level pulsed currents," *Review of Scientific Instruments*, 1980.
5. J. A. J. Pettinga and J. Siersema, "A polyphase 500 kA current measuring system with Rogowski coils," *IEE Proceedings B*, 1983.
6. W. F. Ray and C. R. Hewson, "High performance Rogowski current transducers," IEEE IAS Annual Meeting, 2000.
7. C. Baudart, "Device for measuring an electrical current in a conductor using a Rogowski coil," US Patent 5,442,280, 1995.
8. N. Karrer and P. Hofer-Noser, "PCB Rogowski coils for high di/dt current measurement," IEEE PESC, 2000.
9. L. Dalessandro et al., "Online and offline isolated current monitoring of parallel switched high-voltage multi-chip IGBT modules," IEEE PESC, 2008.
10. T. Guillod, D. Gerber, J. Biela and A. Müsing, "Design of a PCB Rogowski coil based on the PEEC method," CIPS, 2012.
11. Y. Xue et al., "A compact planar Rogowski coil current sensor for active current balancing of parallel-connected silicon carbide MOSFETs," IEEE ECCE, 2014.
12. J. Wang, Z. Shen, R. Burgos and D. Boroyevich, "Design of a high-bandwidth Rogowski current sensor for gate-drive short-circuit protection of 1.7 kV SiC MOSFET power modules," IEEE WiPDA, 2015.
13. M. Koga, M. Tsukuda, K. Nakashima and I. Omura, "[Application-specific micro Rogowski coil for power modules: design tool, novel coil pattern and demonstration](http://hdl.handle.net/10228/5769)," CIPS, 2016.
14. Y. Kuwabara, K. Wada, J.-M. Guichon, J.-L. Schanen and J. Roudet, "Bus bar embedded Rogowski coil," IEEE APEC, 2018.
15. J. Walter, J. Acuna and I. Kallfass, "Design and implementation of an integrated current sensor for a gallium nitride half-bridge," PCIM Europe, 2018.
16. C. Jiao, Z. Zhang, Z. Zhao and X. Zhang, "Integrated Rogowski coil sensor for press-pack insulated gate bipolar transistor chips," *Sensors*, 2020.

[PCB Current Transformer](/research/pcb-current-transformer/) · [Current Sensing](/research/sensing_devices/) · [Back to Research](/research/)
