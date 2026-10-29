---
layout: single
title: "10 kW LLC Resonant Converter"
permalink: /research/isolated-converters/llc/
author_profile: true
excerpt: "Resonant-tank design and closed-loop simulation of a 10 kW, 750 V to 50 V LLC converter for data-centre power."
body_class: microgrid-project-page
project_stylesheet: /assets/css/marine-project.css
project_contents: true
mathjax: true
---

This study examined an isolated 10 kW LLC resonant converter for a data-centre power application, from resonant-tank design by first-harmonic analysis to closed-loop simulation. The work remained at the simulation stage; no hardware prototype was built or tested.

## How an LLC Converter Regulates Its Output

An LLC converter places a resonant tank between a switching bridge and an isolating transformer. The tank is formed by a resonant capacitor <i>C</i><sub>r</sub>, a resonant inductor <i>L</i><sub>r</sub> and the transformer's magnetising inductance <i>L</i><sub>m</sub>. The voltage gain of the tank depends on the switching frequency, so the controller regulates the output by varying frequency as the input voltage and load change. Around the series resonant frequency, the transformer turns ratio sets the voltage conversion, and operating near resonance allows soft switching, which keeps losses low at high frequency.

<figure>
  <a href="/images/research/llc-converter/llc-circuit.png" target="_blank" rel="noopener"><img src="/images/research/llc-converter/llc-circuit.png" alt="Full-bridge LLC converter with switching bridge, resonant tank, transformer and diode rectifier, and output capacitor" width="784" height="366" fetchpriority="high"></a>
  <figcaption>Full-bridge LLC power stage: switching bridge, LLC tank, transformer and rectifier, and output capacitor.</figcaption>
</figure>

## Specification and Design Method

The converter must supply a regulated 50 V output from a 750 V input that varies by ±10%:

| Design target | Value |
| --- | --- |
| Input voltage | 750 V nominal; 675–825 V range |
| Output voltage | 50 V |
| Maximum output power | 10 kW |
| Target operating frequency | 200 kHz |

The tank was designed by first-harmonic approximation: the square-wave bridge voltage is replaced by its fundamental, and the rectifier and load by an equivalent AC resistance <i>R</i><sub>ac</sub>, which turns the converter into a linear resonant circuit.

<figure>
  <a href="/images/research/llc-converter/llc-fha-equivalent.png" target="_blank" rel="noopener"><img src="/images/research/llc-converter/llc-fha-equivalent.png" alt="First-harmonic equivalent circuit with series resonant capacitor and inductor, magnetising inductance and equivalent AC load resistance" width="642" height="227" loading="lazy"></a>
  <figcaption>First-harmonic equivalent circuit of the LLC tank.</figcaption>
</figure>

With the series resonant frequency <i>f</i><sub>r</sub>, the quality factor <i>Q</i> and the inductance ratio <i>m</i>,

<div class="math-display">\[f_r=\frac{1}{2\pi\sqrt{L_rC_r}},\]</div>

<div class="math-display">\[Q=\frac{\sqrt{L_r/C_r}}{R_{ac}},\qquad m=\frac{L_r+L_m}{L_r},\]</div>

the tank's voltage gain at normalised frequency <i>F</i><sub>x</sub> = <i>f</i><sub>s</sub>/<i>f</i><sub>r</sub> is

<div class="math-display">\[K=\frac{(m-1)F_x^2}{\sqrt{\bigl(mF_x^2-1\bigr)^2+F_x^2\bigl(F_x^2-1\bigr)^2(m-1)^2Q^2}}.\]</div>

With a 15 : 1 transformer, the nominal 750 V input needs a gain of 1, and the 675–825 V range needs a gain from 0.909 to 1.111. The tank's peak gain <i>K</i><sub>max</sub> must therefore exceed 1.111 at full load.

## Choosing Q and m

<i>Q</i> was swept at <i>m</i> = 10, then <i>m</i> at <i>Q</i> = 0.4. A low <i>Q</i> gives a high, sharp gain peak but makes the gain very sensitive to frequency; a high <i>Q</i> flattens the peak below the required gain. Reducing <i>m</i>, a smaller magnetising inductance, raises the peak gain at the cost of more circulating magnetising current.

<figure class="project-blueprint">
  <a href="/images/research/llc-converter/llc-gain-sweeps.svg" target="_blank" rel="noopener"><img src="/images/research/llc-converter/llc-gain-sweeps.svg" alt="LLC voltage gain against normalised frequency for Q from 0.1 to 1 at m of 10 and for m from 2 to 15 at Q of 0.4, with the selected design highlighted and the required gain band shaded" width="760" height="410" loading="lazy"></a>
  <figcaption>Tank gain from the first-harmonic model, sweeping <i>Q</i> (left) and <i>m</i> (right); the selected <i>Q</i> = 0.4 and <i>m</i> = 10 is highlighted, and the shaded band is the gain the input range requires.</figcaption>
</figure>

The selected <i>Q</i> = 0.4 and <i>m</i> = 10 give a peak gain of 1.115 at <i>F</i><sub>x</sub> = 0.504, just above the required 1.111, with these tank values:

| Parameter | Value |
| --- | --- |
| Resonant inductance <i>L</i><sub>r</sub> | 14.51 µH |
| Resonant capacitance <i>C</i><sub>r</sub> | 43.6 nF |
| Magnetising inductance <i>L</i><sub>m</sub> | 130.62 µH |
| Transformer turns ratio | 15 : 1 |
| Minimum switching frequency | 100.8 kHz |

Because the margin is small, lower <i>m</i> and a lower resonant frequency were also examined:

| Variant | Peak gain | Minimum frequency | Tank values |
| --- | --- | --- | --- |
| <i>Q</i> = 0.4, <i>m</i> = 9 | 1.155 | 97.9 kHz | <i>L</i><sub>m</sub> = 116.1 µH; <i>L</i><sub>r</sub>, <i>C</i><sub>r</sub> and turns ratio unchanged |
| <i>Q</i> = 0.4, <i>m</i> = 8 | 1.209 | 96.5 kHz | <i>L</i><sub>m</sub> = 101.6 µH; <i>L</i><sub>r</sub>, <i>C</i><sub>r</sub> and turns ratio unchanged |
| <i>f</i><sub>r</sub> = 100 kHz, <i>Q</i> = 0.9, <i>m</i> = 10 | 1.009 | 92.5 kHz | <i>L</i><sub>r</sub> = 18.55 µH, <i>C</i><sub>r</sub> = 136.5 nF, <i>L</i><sub>m</sub> = 167.0 µH, turns ratio 8.0 : 1 |

Lowering <i>m</i> to 9 or 8 adds gain margin with the same resonant components. The 100 kHz variant roughly halves the turns ratio, so the tank only needs a gain of about 0.5, well below its peak of 1.009, which leaves ample margin even with a flatter, higher-<i>Q</i> tank.

## Closed-Loop Simulation

A PI controller regulates the output voltage by adjusting the switching frequency. In simulation, the input steps from 825 V to 675 V and the load then falls from 10 kW to 5 kW. After the input step, the output voltage dips and returns towards 50 V; the load reduction produces a smaller transient.

<figure>
  <a href="/images/research/llc-converter/llc-output-transient.png" target="_blank" rel="noopener"><img src="/images/research/llc-converter/llc-output-transient.png" alt="Simulated LLC output voltage and output power during changes in input voltage and load" width="644" height="274" loading="lazy"></a>
  <figcaption>Simulated output voltage and power during an input-voltage step from 825 V to 675 V and a load reduction.</figcaption>
</figure>

The switching waveforms show the operating principle: complementary gate signals for the two bridge diagonals, a MOSFET drain–source voltage, the sinusoidal resonant current with the triangular magnetising current, and the alternating rectifier diode currents.

<figure>
  <a href="/images/research/llc-converter/llc-switching-waveforms.png" target="_blank" rel="noopener"><img src="/images/research/llc-converter/llc-switching-waveforms.png" alt="Simulated gate signals, MOSFET voltage, resonant and magnetising inductor currents and rectifier diode currents over a few switching cycles" width="848" height="939" loading="lazy"></a>
  <figcaption>Simulated switching waveforms: gate signals, MOSFET voltage, resonant (<i>I</i><sub>Lr</sub>) and magnetising (<i>I</i><sub>Lm</sub>) currents, and rectifier diode currents.</figcaption>
</figure>

The simulation confirmed that the operating margin is tight at the low-frequency end of the range, where the tank must provide its highest gain, which motivated the lower-<i>m</i> and lower-frequency variants. Switching performance, losses, thermal behaviour and manufacturability would need further design and experimental verification.

[Isolated Converters](/research/isolated_converters/) · [Converter Design Optimisation](/research/converter_optimization/) · [Back to Research](/research/)
