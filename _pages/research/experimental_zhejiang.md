---
layout: single
title: "Zhejiang University 50 kW DC Microgrid Test Bench"
permalink: /research/experimental-platforms/zhejiang/
author_profile: true
body_class: microgrid-project-page
project_stylesheet: /assets/css/marine-project.css
project_contents: true
mathjax: true
excerpt: "A 50 kW DC microgrid test bench at Zhejiang University: converter protection, hierarchical control with passivity-based stabilisation, and droop control of three-phase AC–DC interface converters."
---

A two-month research secondment at Zhejiang University, from March to April 2018 in Prof. Wuhua Li's group, centred on operating the group's **50 kW DC microgrid test bench** and on the design principles behind it: converter protection, hierarchical control, passivity-based stabilisation and the control of three-phase AC–DC interface converters. The secondment also provided systematic training in microgrid test-bench design.

## The Test Bench

The bench houses its power converters in cabinets. Fan-cooled converter modules sit above the auxiliary power supplies, terminal blocks and protection wiring, and a smart-load cabinet alongside provides controllable loads.

<figure>
  <a href="/images/research/experimental-platforms/zju-microgrid-bench.jpg" target="_blank" rel="noopener"><img src="/images/research/experimental-platforms/zju-microgrid-bench.jpg" alt="Open cabinet of the DC microgrid test bench with three fan-cooled converter modules above rows of auxiliary power supplies, terminal blocks and wiring, beside a smart-load cabinet" width="720" height="962" fetchpriority="high"></a>
  <figcaption>Converter cabinet of the 50 kW DC microgrid test bench, with the smart-load cabinet on the left.</figcaption>
</figure>

## Converter Protection

In a system of distributed converters, a single fault can collapse the whole microgrid, so a faulty converter must be isolated immediately. The bench combines hardware relays with software protection, and each converter sits within its own protection chain: external switches and relays at both ports, current sensing on both sides, input and output filters, and a DC circuit breaker after the three-phase bridge, with the DC voltage sensed on both sides of the breaker.

<figure class="project-blueprint">
  <a href="/images/research/experimental-platforms/zju-converter-protection.png" target="_blank" rel="noopener"><img src="/images/research/experimental-platforms/zju-converter-protection.png" alt="Protection chain of a converter: external switch, relay, current sensing, input filter, three-phase bridge, DC circuit breaker, output filter, current sensing, relay and external switch, with voltage sensing on the DC side" width="1400" height="310" loading="lazy"></a>
  <figcaption>Protection chain of each converter on the test bench.</figcaption>
</figure>

## Hierarchical Control

The bench follows a three-layer hierarchical control scheme, which its designers describe as mode-adaptive decentralised control:

| Layer | Control | Function |
| --- | --- | --- |
| Primary | Self-disciplined | Stabilises each converter locally on the basis of passivity theory, with double-loop, droop and voltage feed-forward control |
| Secondary | Self-adaptive | Uses the common DC bus voltage as the signal carrier, so that converters change operating mode without communication links |
| Tertiary | Self-organised | Distributes power over CAN communication according to cost, weather and other conditions, by adjusting the droop coefficients, voltage references and maximum power limits of the lower layers |

The secondary layer applies DC bus signalling, the principle also behind the [dual-window DC bus signalling](/research/dcmg/dc-bus-signalling/) method developed in the PhD research.

## Passivity-Based Stabilisation

Passivity is the core of the scheme, because it guarantees stable operation of the interconnected converters. Consider a system with states <i>x</i> ∈ ℝ<sup><i>n</i></sup>, inputs <i>u</i> ∈ ℝ<sup><i>m</i></sup> and outputs <i>y</i> ∈ ℝ<sup><i>m</i></sup>. The map <i>u</i> → <i>y</i> is passive if there exist a storage function <i>H</i>(<i>x</i>), bounded from below, and a non-negative dissipation <i>d</i>(<i>t</i>) ≥ 0 such that

<div class="math-display">\[H\bigl(x(t)\bigr)-H\bigl(x(0)\bigr)=\int_0^t u^{\top}y\,d\tau-\int_0^t d(\tau)\,d\tau.\]</div>

A passive system cannot store more energy than it is supplied, and an interconnection of passive systems remains passive, so a microgrid whose converters all present passive ports to the DC bus remains stable. A storage function for a complete DC microgrid is difficult to find, so the bench applies the idea at each converter instead: voltage feed-forward control shapes each interface converter to satisfy the passivity condition at its port. The same idea underlies the [passive stabiliser](/research/dcmg/passive-control/) developed for Boost interface converters in the PhD research.

## AC–DC Interface Control

Two three-phase AC–DC interface converters were modelled to study droop control between them. Each regulates its DC output with an outer voltage loop whose reference is drooped by a virtual resistance <i>R</i><sub>v</sub>,

<div class="math-display">\[V^{*}=V_{ref}-R_vI_{out}.\]</div>

A PI controller turns the voltage error into a limited d-axis current reference <i>i</i><sub>d</sub>*, and the q-axis reference <i>i</i><sub>q</sub>* is zero for unity power factor. Inner PI loops regulate <i>i</i><sub>d</sub> and <i>i</i><sub>q</sub>, obtained from the phase currents by the abc–dq transformation, and the inverse transformation returns the phase duty cycles.

<figure class="project-blueprint">
  <a href="/images/research/experimental-platforms/zju-acdc-control.png" target="_blank" rel="noopener"><img src="/images/research/experimental-platforms/zju-acdc-control.png" alt="Control block diagram: the voltage reference minus the virtual-resistance drop gives the drooped reference, a PI controller and limiter produce the d-axis current reference, PI current loops in the dq frame with zero q-axis reference produce the dq duty cycles, and a dq to abc transformation gives the phase duty cycles" width="1400" height="392" loading="lazy"></a>
  <figcaption>Droop and dq current control of the three-phase AC–DC interface converter.</figcaption>
</figure>

In simulation, the load steps at 0.3 s. The converter's DC current rises from about 9 A to about 17.5 A, while the DC voltage, regulated near 670 V, falls slightly, as droop control intends; the modulation index rises from about 0.90 to 0.92 to deliver the extra power.

<figure class="project-blueprint">
  <a href="/images/research/experimental-platforms/zju-droop-simulation.png" target="_blank" rel="noopener"><img src="/images/research/experimental-platforms/zju-droop-simulation.png" alt="Simulated waveforms over 0.5 s: grid voltage and current, converter line voltage, modulation index, DC voltage near 670 V and DC current stepping from about 9 A to 17.5 A at 0.3 s" width="1600" height="757" loading="lazy"></a>
  <figcaption>Simulated response of an AC–DC interface converter to a load step at 0.3 s: grid voltage (pu) and current, converter line voltage, modulation index, DC voltage and DC current.</figcaption>
</figure>

[All experimental platforms](/research/experimental_platforms/) · [DC Microgrid Control Strategies](/research/dcmg/) · [Back to Research](/research/)
