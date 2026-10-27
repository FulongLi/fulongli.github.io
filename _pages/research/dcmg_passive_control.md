---
layout: single
title: "Passive Control for Boost Converter"
permalink: /research/dcmg/passive-control/
author_profile: true
body_class: microgrid-project-page
project_stylesheet: /assets/css/marine-project.css
project_contents: true
mathjax: true
excerpt: "Passivity-based Boost converter control: averaged modelling, positive-real analysis, feedforward passivation and a filtered stabiliser."
---

<h2 id="overview">Passivity and Boost Converter Stability</h2>

A Boost converter's voltage-control plant contains a right-half-plane zero: a duty-cycle change initially drives the output voltage in the opposite direction to its eventual response. In a DC microgrid this non-minimum-phase behaviour constrains the voltage-loop design and can contribute to instability.

My thesis develops a passive stabiliser from an averaged converter model. The analysis first identifies the non-passive part of the outer-loop plant, then adds a feedforward path, and finally filters that path to preserve the steady operating point. The equations below follow Chapter 5, with the thesis's idealised component assumptions.

<h2 id="passivity">Passivity Criteria</h2>

A passive system cannot deliver more energy than it receives plus its initially stored energy. For input <i>u</i>, output <i>y</i>, stored energy <i>H</i> and dissipated energy ε, the thesis writes the energy balance as:

<div class="math-display">\[\int_0^t u^{\mathsf T}(\tau)y(\tau)\,d\tau = H\bigl(x(t)\bigr)-H\bigl(x(0)\bigr)+\varepsilon(t),\qquad \varepsilon(t)\ge 0.\]</div>

For the stable linear time-invariant system considered in the design, passivity is examined through its positive-real transfer function. In the single-input, single-output case, the frequency-domain condition is:

<div class="math-display">\[\operatorname{Re}\!\left\{G(j\omega)\right\}\ge 0.\]</div>

The thesis examines the relevant frequency range up to the converter switching frequency. This is a design-oriented frequency-domain assessment of the linearised plant; the conclusion depends on the model, operating point and bandwidth considered.

<h2 id="converter-model">Averaged Model and the Outer-Loop Plant</h2>

Ignoring the small parasitic resistances in the thesis model, the averaged inductor-current and output-voltage equations are:

<div class="math-display">\[\begin{aligned}
L\frac{di_L}{dt}&=v_g-d'v,\\
C\frac{dv}{dt}&=d'i_L-i_o,\qquad d'=1-d.
\end{aligned}\]</div>

Here <i>v</i><sub>g</sub> is the source voltage, <i>i</i><sub>L</sub> is the inductor current, <i>v</i> is the DC-bus voltage, <i>i</i><sub>o</sub> is the output current, and <i>d</i> is duty ratio. Linearising around an operating point gives the duty-to-voltage and duty-to-current transfer functions with a common denominator:

<div class="math-display">\[\begin{aligned}
\operatorname{den}(s)&=1+\frac{sL}{D'^2R}+\frac{s^2LC}{D'^2},\\
G_{vd}(s)&=\frac{V}{D'}\frac{1-s\frac{L}{D'^2R}}{\operatorname{den}(s)},\\
G_{id}(s)&=\frac{2V}{D'^2R}\frac{1+s\frac{RC}{2}}{\operatorname{den}(s)}.
\end{aligned}\]</div>

The steady-state output voltage is <i>V</i>. With the inner current loop following its reference closely, the common denominator cancels in their ratio, giving the approximate outer-loop plant:

<div class="math-display">\[G_{vc}(s)=\frac{\Delta v}{\Delta v_c}\approx\frac{1}{R_f}\frac{G_{vd}(s)}{G_{id}(s)}
=\frac{D'R}{2R_f}\frac{1-s\frac{L}{D'^2R}}{1+s\frac{RC}{2}}.\]</div>

The current-sampling gain is <i>R</i><sub>f</sub>, <i>R</i> is the equivalent load resistance, and <i>D</i>′ is the steady-state complementary duty ratio. The numerator zero lies in the right half-plane. For compact analysis, define:

<div class="math-display">\[\alpha=\frac{D'R}{2R_f},\qquad \beta=\frac{L}{D'^2R},\qquad \gamma=\frac{RC}{2},\qquad G_{vc}(s)\approx\alpha\frac{1-s\beta}{1+s\gamma}.\]</div>

<h2 id="positive-real-analysis">Uncompensated Plant</h2>

Substituting <i>s</i> = jω separates the real part of the plant response:

<div class="math-display">\[\operatorname{Re}\!\left\{G_{vc}(j\omega)\right\}=\alpha\frac{1-\omega^2\beta\gamma}{1+\omega^2\gamma^2}.\]</div>

The denominator is positive. The numerator becomes negative above the crossing frequency, so the plant no longer satisfies the positive-real condition in that region. The crossing and the high-frequency limit are:

<div class="math-display">\[\omega_N=\frac{1}{\sqrt{\beta\gamma}},\qquad f_N=\frac{1}{2\pi}\sqrt{\frac{2D'^2}{LC}},\qquad \lim_{\omega\to\infty}G_{vc}(j\omega)=-\frac{\alpha\beta}{\gamma}.\]</div>

<figure class="project-blueprint">
  <a href="/images/research/dc-microgrid-control/nyquist-stages.png" target="_blank" rel="noopener"><img src="/images/research/dc-microgrid-control/nyquist-stages.png" alt="Three Nyquist sketches: uncompensated Boost plant, constant feedforward gain, and high-pass-filtered feedforward gain" width="1860" height="459" loading="lazy"></a>
  <figcaption>Nyquist evolution during passivation.</figcaption>
</figure>

From left to right, the sketches show the uncompensated plant entering the negative-real region, constant gain shifting the whole locus to the right, and filtered gain moving the high-frequency end while retaining the low-frequency endpoint. The colours in the latter two sketches indicate increasing gain. These are conceptual sketches of the plant response, not closed-loop stability plots.

<h2 id="constant-feedforward">First Iteration: Constant Feedforward</h2>

Adding a parallel feedforward gain shifts the outer plant towards the positive real region:

<div class="math-display">\[G'_{vc}(s)=G_{vc}(s)+K=\frac{(\alpha+K)+s(K\gamma-\alpha\beta)}{1+s\gamma}.\]</div>

The high-frequency limit becomes the gain <i>K</i> minus the magnitude of the negative asymptote. In the idealised model, a gain at least as large as that magnitude offsets the negative asymptote. But the same gain changes the DC value from α to α + <i>K</i>, shifting the quiescent voltage reference. This motivates a feedforward path that is suppressed at low frequency.

<h2 id="stabiliser-design">Filtered Passive Stabiliser</h2>

A first-order high-pass filter retains the high-frequency compensation while its DC gain tends to zero:

<div class="math-display">\[G_p(s)=\frac{Ks}{s+\delta},\qquad G'_{vc}(s)=\alpha\frac{1-s\beta}{1+s\gamma}+\frac{Ks}{s+\delta}.\]</div>

<figure>
  <a href="/images/research/dc-microgrid-control/passive-control-block.png" target="_blank" rel="noopener"><img src="/images/research/dc-microgrid-control/passive-control-block.png" alt="Original Boost interface-converter control diagram with droop, inner current loop, outer voltage loop and filtered passive stabiliser" width="1248" height="543" fetchpriority="high"></a>
  <figcaption>Integration with the converter control loops.</figcaption>
</figure>

The stabiliser adds a filtered feedforward path alongside the outer voltage controller.

The filtered plant approaches α at DC and the gain <i>K</i> minus the magnitude of the negative asymptote at high frequency. Its frequency-domain real part is:

<div class="math-display">\[\operatorname{Re}\!\left\{G'_{vc}(j\omega)\right\}=\alpha\frac{1-\omega^2\beta\gamma}{1+\omega^2\gamma^2}+K\frac{\omega^2}{\omega^2+\delta^2}.\]</div>

The thesis uses the high-frequency compensation requirement and places the filter corner below the frequency at which the uncompensated plant enters the negative real region:

<div class="math-display">\[K\ge\frac{\alpha\beta}{\gamma},\qquad 0<\delta<\omega_N.\]</div>

<figure class="project-blueprint">
  <a href="/images/research/dc-microgrid-control/nyquist-comparison.png" target="_blank" rel="noopener"><img src="/images/research/dc-microgrid-control/nyquist-comparison.png" alt="Numerical Nyquist plots comparing constant gain and high-pass-filtered gain for increasing compensation" width="1995" height="810" loading="lazy"></a>
  <figcaption>Constant and filtered gain: numerical Nyquist comparison.</figcaption>
</figure>

For the thesis's example parameters, the numerical curves show the same distinction: constant gain shifts both real-axis endpoints, while filtered gain leaves the low-frequency endpoint unchanged as the gain increases. The curves illustrate the particular model and parameter choices; positive realness must be checked across the relevant frequency range.

These endpoint and corner-frequency choices guide the design; the real part over the complete frequency range and the closed-loop margins still need checking for the chosen values and operating conditions.

<h2 id="system-integration">Application in the Control Structure</h2>

The current controller regulates the inductor current; the voltage controller supplies its reference. Droop control modifies the voltage reference for power sharing, while the parallel passive stabiliser shapes the outer-loop dynamics. The existing current and voltage controllers can be designed for adequate margins; the additional path is then selected from the plant analysis above.

The thesis also discretises the current controller, voltage controller and stabiliser for DSP implementation using a bilinear approximation. The resulting design applies to the analysed converter and assumptions; its gain, filter corner and terminal-capacitance requirements must be reviewed for a different operating point or load.

<h2 id="sources">Sources</h2>

[PhD thesis: Control Strategies for Low Voltage DC Microgrids](https://publications.aston.ac.uk/id/eprint/46135/), Chapter 5, pp. 88–102. · [Novel Passive Controller Design for Enhancing Boost Converter Stability in DC Microgrid Applications](https://ieeexplore.ieee.org/document/9391691), IEEE JESTPE, 2021.

[DC Microgrid Control Strategies](/research/dcmg/) · [Dual-Window DC Bus Signalling](/research/dcmg/dc-bus-signalling/) · [Back to Research](/research/)
