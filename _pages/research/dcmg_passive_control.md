---
layout: single
title: "Passive Control for Boost Converter"
permalink: /research/dcmg/passive-control/
author_profile: true
excerpt: "A high-pass-filtered passive stabiliser that suppresses Boost converter oscillation in DC microgrids without shifting the bus voltage."
body_class: microgrid-project-page
project_stylesheet: /assets/css/marine-project.css
project_contents: true
mathjax: true
---

In my PhD I developed a passive stabiliser for Boost interface converters in DC microgrids. Derived from an averaged converter model, it adds a high-pass-filtered feedforward path that suppresses oscillation without shifting the steady-state bus voltage, and I verified it experimentally on a single converter and on parallel converters.

<h2 id="overview">Passivity and Boost Converter Stability</h2>

A Boost converter's voltage-control plant contains a right-half-plane zero: a change in duty cycle first drives the output voltage in the opposite direction to its final response. This non-minimum-phase behaviour constrains the voltage-loop design and, in a DC microgrid with several interacting converters, can contribute to instability.

Passivity offers a design criterion that holds as systems are connected together. A passive system cannot deliver more energy than it receives plus its initially stored energy. For input <i>u</i>, output <i>y</i>, stored energy <i>H</i> and dissipated energy ε, the energy balance is:

<div class="math-display">\[\int_0^t u^{\mathsf T}(\tau)y(\tau)\,d\tau = H\bigl(x(t)\bigr)-H\bigl(x(0)\bigr)+\varepsilon(t),\qquad \varepsilon(t)\ge 0.\]</div>

For a stable linear time-invariant, single-input single-output system, passivity corresponds to a positive-real transfer function:

<div class="math-display">\[\operatorname{Re}\!\left\{G(j\omega)\right\}\ge 0.\]</div>

The design therefore asks where the Boost converter's outer-loop plant fails this condition, and how to correct it.

<h2 id="stabiliser-design">Designing the Passive Stabiliser</h2>

<h3 id="converter-model">Averaged Model and Outer-Loop Plant</h3>

Neglecting small parasitic resistances, the averaged inductor-current and output-voltage equations are:

<div class="math-display">\[\begin{aligned}
L\frac{di_L}{dt}&=v_g-d'v,\\
C\frac{dv}{dt}&=d'i_L-i_o,\qquad d'=1-d,
\end{aligned}\]</div>

where <i>v</i><sub>g</sub> is the source voltage, <i>i</i><sub>L</sub> the inductor current, <i>v</i> the DC-bus voltage, <i>i</i><sub>o</sub> the output current and <i>d</i> the duty ratio. Linearising around an operating point gives the duty-to-voltage and duty-to-current transfer functions:

<div class="math-display">\[\begin{aligned}
\operatorname{den}(s)&=1+\frac{sL}{D'^2R}+\frac{s^2LC}{D'^2},\\
G_{vd}(s)&=\frac{V}{D'}\frac{1-s\frac{L}{D'^2R}}{\operatorname{den}(s)},\\
G_{id}(s)&=\frac{2V}{D'^2R}\frac{1+s\frac{RC}{2}}{\operatorname{den}(s)}.
\end{aligned}\]</div>

With the inner current loop following its reference closely, the common denominator cancels, giving the approximate outer-loop plant from current reference to bus voltage:

<div class="math-display">\[G_{vc}(s)\approx\frac{1}{R_f}\frac{G_{vd}(s)}{G_{id}(s)}=\alpha\frac{1-s\beta}{1+s\gamma},\qquad \alpha=\frac{D'R}{2R_f},\quad \beta=\frac{L}{D'^2R},\quad \gamma=\frac{RC}{2},\]</div>

where <i>R</i><sub>f</sub> is the current-sampling gain, <i>R</i> the equivalent load resistance and <i>D</i>′ the steady-state complementary duty ratio. The numerator zero lies in the right half-plane.

<h3 id="positive-real-analysis">Where the Plant Loses Passivity</h3>

The real part of the plant response is:

<div class="math-display">\[\operatorname{Re}\!\left\{G_{vc}(j\omega)\right\}=\alpha\frac{1-\omega^2\beta\gamma}{1+\omega^2\gamma^2}.\]</div>

It becomes negative above a crossing frequency and tends to a negative high-frequency limit:

<div class="math-display">\[\omega_N=\frac{1}{\sqrt{\beta\gamma}},\qquad f_N=\frac{1}{2\pi}\sqrt{\frac{2D'^2}{LC}},\qquad \lim_{\omega\to\infty}G_{vc}(j\omega)=-\frac{\alpha\beta}{\gamma}.\]</div>

<figure class="project-blueprint">
  <a href="/images/research/dc-microgrid-control/nyquist-stages.png" target="_blank" rel="noopener"><img src="/images/research/dc-microgrid-control/nyquist-stages.png" alt="Three Nyquist sketches: uncompensated Boost plant, constant feedforward gain, and high-pass-filtered feedforward gain" width="1860" height="459" loading="lazy"></a>
  <figcaption>Conceptual Nyquist sketches: the uncompensated plant enters the negative-real region (left); a constant gain shifts the whole locus right (centre); a filtered gain moves only the high-frequency end (right).</figcaption>
</figure>

<h3 id="constant-feedforward">Constant Feedforward</h3>

Adding a parallel feedforward gain <i>K</i> shifts the plant towards the positive-real region:

<div class="math-display">\[G'_{vc}(s)=G_{vc}(s)+K=\frac{(\alpha+K)+s(K\gamma-\alpha\beta)}{1+s\gamma}.\]</div>

A gain at least as large as the negative asymptote offsets it, but the same gain changes the DC value from α to α + <i>K</i> and so shifts the steady-state bus voltage. This motivates a feedforward path that is suppressed at low frequency.

<h3 id="filtered-stabiliser">Filtered Passive Stabiliser</h3>

A first-order high-pass filter keeps the high-frequency compensation while its DC gain tends to zero:

<div class="math-display">\[G_p(s)=\frac{Ks}{s+\delta},\qquad \operatorname{Re}\!\left\{G'_{vc}(j\omega)\right\}=\alpha\frac{1-\omega^2\beta\gamma}{1+\omega^2\gamma^2}+K\frac{\omega^2}{\omega^2+\delta^2}.\]</div>

The gain compensates the high-frequency deficit, and the filter corner sits below the frequency at which the uncompensated plant loses passivity:

<div class="math-display">\[K\ge\frac{\alpha\beta}{\gamma},\qquad 0<\delta<\omega_N.\]</div>

<figure>
  <a href="/images/research/dc-microgrid-control/passive-control-block.png" target="_blank" rel="noopener"><img src="/images/research/dc-microgrid-control/passive-control-block.png" alt="Boost interface-converter control diagram with droop, inner current loop, outer voltage loop and filtered passive stabiliser" width="1248" height="543" fetchpriority="high"></a>
  <figcaption>The filtered passive stabiliser added in parallel with the outer voltage controller, alongside droop and the inner current loop.</figcaption>
</figure>

In the control structure, the current controller regulates the inductor current and the voltage controller supplies its reference; droop control adjusts the voltage reference for power sharing, and the stabiliser shapes the outer-loop dynamics in parallel. I discretised the current controller, voltage controller and stabiliser with a bilinear approximation for implementation on the converter's DSP.

<h2 id="results">Simulation and Experimental Results</h2>

<h3 id="numerical-comparison">Frequency-Domain Comparison</h3>

For the thesis example parameters, numerical Nyquist plots confirm the distinction between the two approaches: a constant gain shifts both real-axis endpoints, while the filtered gain leaves the low-frequency endpoint unchanged as the gain increases.

<figure class="project-blueprint">
  <a href="/images/research/dc-microgrid-control/nyquist-comparison.png" target="_blank" rel="noopener"><img src="/images/research/dc-microgrid-control/nyquist-comparison.png" alt="Numerical Nyquist plots comparing constant gain and high-pass-filtered gain for increasing compensation" width="1995" height="810" loading="lazy"></a>
  <figcaption>Numerical Nyquist plots for increasing compensation gain: constant gain (left) and high-pass-filtered gain (right).</figcaption>
</figure>

<h3 id="experimental-results">Experimental Results</h3>

To expose an oscillatory case on the laboratory converter, I reduced the terminal capacitor from **470 µF to 100 µF**. Enabling constant-gain compensation suppressed the oscillation, but with the predicted drop in bus voltage.

<figure>
  <a href="/images/research/dc-microgrid-control/passive-constant-gain-result.png" target="_blank" rel="noopener"><img src="/images/research/dc-microgrid-control/passive-constant-gain-result.png" alt="Oscilloscope trace showing oscillation suppression and a voltage drop when constant-gain passive control is switched on" width="1293" height="444" loading="lazy"></a>
  <figcaption>Constant-gain compensation: the oscillation is suppressed, but the DC bus voltage shifts when passive control is enabled.</figcaption>
</figure>

The high-pass-filtered stabiliser suppressed the same oscillation without the steady-state voltage shift.

<figure>
  <a href="/images/research/dc-microgrid-control/passive-hpf-result.png" target="_blank" rel="noopener"><img src="/images/research/dc-microgrid-control/passive-hpf-result.png" alt="DC bus voltage trace with oscillations suppressed after enabling high-pass-filtered passive control at K equals 1.9" width="1293" height="444" loading="lazy"></a>
  <figcaption>High-pass-filtered compensation with K = 1.9: the oscillation is suppressed and the bus voltage keeps its operating point.</figcaption>
</figure>

Further tests covered **K = 2.5** and two parallel converters sharing current through droop control. Removing the stabilisers from the parallel-converter test produced oscillation, linking the local design to operation with multiple converters. The design applies to the analysed converter and its operating assumptions; the gain, filter corner and terminal capacitance must be reviewed for a different operating point or load.

[PhD thesis: Control Strategies for Low Voltage DC Microgrids](https://publications.aston.ac.uk/id/eprint/46135/), Chapter 5. · [Novel Passive Controller Design for Enhancing Boost Converter Stability in DC Microgrid Applications](https://ieeexplore.ieee.org/document/9391691), IEEE JESTPE, 2021.

[DC Microgrid Control Strategies](/research/dcmg/) · [Dual-Window DC Bus Signalling](/research/dcmg/dc-bus-signalling/) · [Back to Research](/research/)
