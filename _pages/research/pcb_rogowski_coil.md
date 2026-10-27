---
layout: single
title: "PCB Rogowski Coil Current Sensing"
permalink: /research/pcb-rogowski-coil/
author_profile: true
body_class: microgrid-project-page
project_stylesheet: /assets/css/marine-project.css
project_contents: true
mathjax: true
---

## Review, Design and Testing

I reviewed Rogowski coil current-sensing research and commercial specifications, then designed PCB coils and their signal-conditioning circuits. The work examined coil geometry, sensing performance and the complete measurement chain. In tests, the prototype's response was broadly comparable to a commercial Rogowski coil.

## Rogowski Coil Development

The review compared historical and contemporary designs, including flexible coils, rigid PCB windings and compact sensors integrated near power devices. The comparison considered winding geometry and size, current range, sensitivity, bandwidth and external circuits. The timeline below captures the development paths surveyed in 2022.

<figure>
  <a href="/images/research/pcb-rogowski/rogowski-timeline.png" target="_blank" rel="noopener"><img src="/images/research/pcb-rogowski/rogowski-timeline.png" alt="Rogowski coil development timeline through 2022, with flexible coils and rigid and flexible PCB windings" width="846" height="373"></a>
  <figcaption>Rogowski coil development timeline.</figcaption>
</figure>

The review includes examples from literature and commercial products. Their specifications describe different geometries, test conditions and measurement chains, so individual bandwidth and sensitivity figures should be compared in context.

## PCB Coil and Signal Conditioning

A Rogowski coil is an air-cored winding around the conductor. Its induced voltage is proportional to the rate of change of primary current; a signal-conditioning circuit integrates that voltage to recover a current-proportional signal. Winding geometry, return paths and shielding influence sensitivity and susceptibility to interference. The coil does not directly measure steady DC current.

<div class="math-display">\[v_{\mathrm{coil}}(t)=M\frac{di(t)}{dt}.\]</div>

Here <i>M</i> is the mutual inductance between the conductor and coil. The practical signal chain also needs to manage gain, bandwidth and integrator offset.

<figure>
  <a href="/images/research/pcb-rogowski/circular-coil-pcb.png" target="_blank" rel="noopener"><img src="/images/research/pcb-rogowski/circular-coil-pcb.png" alt="PCB Rogowski coil design with a circular winding and integrated signal-conditioning circuitry" width="602" height="432" loading="lazy"></a>
  <figcaption>Circular PCB coil and signal-conditioning circuit.</figcaption>
</figure>

I designed several PCB winding layouts and the accompanying amplification and signal-conditioning circuitry. The board designs place the coil and conditioning electronics together so the sensing element and its output circuit can be assessed as a system.

<figure>
  <a href="/images/research/pcb-rogowski/rectangular-coil-pcb.png" target="_blank" rel="noopener"><img src="/images/research/pcb-rogowski/rectangular-coil-pcb.png" alt="PCB Rogowski sensor design with a rectangular winding and signal-conditioning components" width="602" height="457" loading="lazy"></a>
  <figcaption>Alternative PCB coil layout.</figcaption>
</figure>

## Experimental Comparison

The designed sensing chain was tested against a commercial Rogowski coil. Its measured response was broadly in line with the commercial reference in the project tests. This comparison is qualitative here: the available summary does not establish a numerical error, frequency range or test uncertainty for the prototype.

[PCB Rogowski coil design repository](https://github.com/FulongLi/PCB-Rogowski-Coil) · [Current Sensing](/research/sensing_devices/) · [Back to Research](/research/)
