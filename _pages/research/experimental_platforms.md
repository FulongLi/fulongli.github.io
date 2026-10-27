---
layout: research
research_area: microgrids
title: "DC Microgrid Experimental Platforms"
permalink: /research/experimental_platforms/
excerpt: "A modular low-voltage DC microgrid bench built during the PhD and extended at Loughborough, and a 50 kW DC microgrid platform operated at Zhejiang University."
---

Most of my DC microgrid control results were obtained on laboratory hardware. This page separates the bench I built from the platform I used.

## Low-voltage DC microgrid bench (Aston University and Loughborough University)

**Purpose.** Test converter control, DC bus signalling and power management with real converters, sources and loads rather than only in simulation.

**My contribution.** During my PhD (Aston University, 2016–2019, within the RDC2MT project) I built a modular DC microgrid test bench of about 500 W per module, covering system construction, converter control design and real-time experimental validation. As a Research Associate at Loughborough University (2019–2022, on an EPSRC-funded project) I designed and built a low-voltage DC microgrid experimental platform and developed online monitoring tools for real-time data acquisition.

**Configuration.** Four DSP-controlled bidirectional interface converters connect a grid emulator (a DC supply with a resistor to absorb returned power), two battery banks and a PV emulator to a common DC bus, with electronic and resistive loads, in grid-connected or islanded operation. The public repository documents two hardware versions; the second raised the per-converter rating from 100 W to 500 W and added a wireless communication module to the control board.

<figure>
  <a href="/images/research/dc-microgrid-control/laboratory-bench.jpg" target="_blank" rel="noopener"><img src="/images/research/dc-microgrid-control/laboratory-bench.jpg" alt="Laboratory bench with DC microgrid interface converters, PV emulator, electronic load and oscilloscope" width="1212" height="915" loading="lazy"></a>
  <figcaption><span class="figure-kind">Laboratory photograph</span><strong>The low-voltage DC microgrid bench used in the PhD experiments.</strong> <span class="figure-source">PhD thesis, Figure 3.1, p. 63.</span></figcaption>
</figure>

**Evidence.** The experiments run on this bench are documented in the [PhD thesis](https://publications.aston.ac.uk/id/eprint/46135/) (see [DC microgrid control strategies](/research/dcmg/)), and its hardware is described in a public repository.

## 50 kW DC microgrid platform (Zhejiang University) {#zhejiang-university-50-kw-dc-microgrid-platform}

As a visiting PhD student at Zhejiang University (March–April 2018), supervised by Prof. Wuhua Li, I tested and operated an existing 50 kW DC microgrid platform with a three-phase VSC grid interface, and modified primary control strategies to improve stability and dynamic response. The platform and its VSC were existing laboratory equipment.

## References and resources

- F. Li, *[Control Strategies for Low Voltage DC Microgrids](https://publications.aston.ac.uk/id/eprint/46135/)*, PhD thesis, Aston University, 2020, Chapter 3.
- [DCMicrogridTestBench (GitHub, CC BY 4.0)](https://github.com/FulongLi/DCMicrogridTestBench): power and control boards, source connections and bench versions.
- Related: [Interface converters](/research/nonisolated_converters/) · [Battery storage control](/research/battery_storage/)
