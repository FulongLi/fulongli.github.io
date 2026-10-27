---
layout: research
research_area: microgrids
title: "PV Battery System"
permalink: /research/pv_systems/
excerpt: "Modified P&O MPPT with integrated battery charging limits: PV-battery architecture, active power control and experimental comparison of two operating points."
---

<h2 id="overview">Overview</h2>

An off-grid PV-battery system needs to harvest solar energy while respecting the battery's charging limits. As the battery approaches full charge, continuing to extract maximum PV power can overcharge it. This work integrates **maximum power point tracking (MPPT)** and **active PV power control** in one converter controller, using measured battery current and voltage to determine when generation should be reduced.

**My contribution:** During my early PhD research, I investigated PV-battery charging control. Our **ICRERA 2016 paper** presents the modified perturb-and-observe (P&O) algorithm, its implementation on an off-grid experimental system, and a comparison of reduced-power operating points on either side of the PV maximum power point.

<nav class="project-contents" aria-label="Project contents">
  <p><strong>On this page</strong></p>
  <ul>
    <li><a href="#overview">Overview</a></li>
    <li><a href="#system-architecture">System architecture</a></li>
    <li><a href="#charging-constraints">Battery charging constraints</a></li>
    <li><a href="#modified-mppt-and-integrated-active-power-control">Modified MPPT algorithm</a></li>
    <li><a href="#operating-points">Two operating points</a></li>
    <li><a href="#experimental-validation">Experimental validation</a></li>
    <li><a href="#outcomes">Outcomes</a></li>
    <li><a href="#project-resources">Sources and related work</a></li>
  </ul>
</nav>

<h2 id="system-architecture">1. System architecture and feedback</h2>

The architecture connects a PV source to a battery bank through a **boost converter**. A digital controller measures PV voltage and current for power tracking, together with battery charging voltage and current for enforcing charging limits. Its output is the converter's PWM duty ratio.

<figure>
  <a href="/images/research/pv-battery/system-architecture.png" target="_blank" rel="noopener" aria-label="View original: PV-battery control architecture"><img src="/images/research/pv-battery/system-architecture.png" alt="PV source connected through a boost converter to batteries, with PV and battery voltage and current feedback to a shared MPPT and charging controller" width="651" height="371" fetchpriority="high"></a>
  <figcaption><strong>PV-battery system architecture.</strong> Power tracking and battery charging feedback share the same converter controller. <span class="figure-source">ICRERA 2016, Figure 1, p. 743.</span></figcaption>
</figure>

The control sequence connects **measurements → charging constraints → MPPT or power reduction → converter actuation → measured response**. Here, the operating decision is made inside the PV controller, on the timescale of converter power control.

<h2 id="charging-constraints">2. Battery charging sets the operating constraints</h2>

The study uses **valve-regulated lead-acid (VRLA) batteries**. Their charging requirements change as charging progresses, so maximum available solar power is useful only while the battery can accept it.

<figure>
  <a href="/images/research/pv-battery/battery-charging-stages.png" target="_blank" rel="noopener" aria-label="View original: three-stage battery charging"><img src="/images/research/pv-battery/battery-charging-stages.png" alt="Original three-stage lead-acid charging diagram showing bulk charging, constant-voltage absorption and lower-voltage float charging" width="708" height="413" loading="lazy"></a>
  <figcaption><strong>Charging stages and control limits.</strong> The changing current and voltage requirements motivate integration of battery constraints into MPPT. <span class="figure-source">ICRERA 2016, Figure 2, p. 743.</span></figcaption>
</figure>

<div class="project-table-scroll" role="region" aria-label="Battery charging stages and control decisions" tabindex="0" markdown="1">

| Charging stage | Battery requirement | PV controller response |
|---|---|---|
| Bulk | Keep charging current within its allowed maximum as battery voltage rises | Track MPP when available PV power is acceptable; reduce power if the charging-current limit is exceeded |
| Absorption | Hold charging voltage at its limit while charging current tapers | Reduce PV output when the voltage limit is exceeded |
| Float | Maintain full charge with a lower maintenance-voltage requirement | The paper describes intermittent charging for this stage; the modified MPPT design focuses on bulk and absorption |

</div>

<h2 id="modified-mppt-and-integrated-active-power-control">3. Modified MPPT with integrated active power control</h2>

Conventional **P&O** perturbs the converter operating point, observes the change in PV power, and keeps or reverses the perturbation direction to approach MPP. The modification adds a battery-limit check to that process:

1. Measure **PV voltage and current**, and **battery charging voltage and current**.
2. Calculate PV power, **P<sub>PV</sub> = V<sub>PV</sub> × I<sub>PV</sub>**, and compare it with the previous sample to update the P&O direction.
3. Check whether **V<sub>charging</sub> > V<sub>ref</sub>** or **I<sub>charging</sub> > I<sub>ref</sub>**. If a limit is exceeded, change the tracking direction to move toward reduced PV power.
4. Apply the duty-ratio perturbation and repeat, allowing the operating point to respond to both available solar power and battery acceptance.

<figure>
  <a href="/images/research/pv-battery/modified-mppt-flowchart.png" target="_blank" rel="noopener" aria-label="View original: modified MPPT algorithm flowchart"><img src="/images/research/pv-battery/modified-mppt-flowchart.png" alt="Original algorithm flowchart: sample PV and battery measurements, calculate power, update the perturbation direction, check battery current or voltage limits, and update converter duty ratio" width="515" height="799" loading="lazy"></a>
  <figcaption><strong>Modified P&O algorithm.</strong> The charging-limit decision is integrated into the perturbation logic before updating the PWM duty ratio. <span class="figure-source">ICRERA 2016, Figure 3, p. 743.</span></figcaption>
</figure>

The operating point adapts through measured feedback. The paper uses a **fixed 100 ms P&O update interval** and a duty-ratio perturbation step; it does not report an adaptive step-size optimisation method. The central change is the integration of charging constraints into MPPT.

<h2 id="operating-points">4. Choosing between two reduced-power operating points</h2>

Below the maximum available power, the PV power–voltage curve admits two operating points: a **left operating point (LOP)** at lower PV voltage and a **right operating point (ROP)** at higher PV voltage. Both can reduce power, but their current, voltage and transient responses differ.

<figure>
  <a href="/images/research/pv-battery/two-operating-points.png" target="_blank" rel="noopener" aria-label="View original: two reduced-power operating points"><img src="/images/research/pv-battery/two-operating-points.png" alt="Original PV power–voltage curves with left and right operating points intersecting the same reduced-power limit on either side of MPP" width="781" height="494" loading="lazy"></a>
  <figcaption><strong>Two ways to curtail PV power.</strong> The same power limit can be reached on either side of MPP. This is the paper's illustrative characteristic, separate from the emulator settings used below. <span class="figure-source">ICRERA 2016, Figure 4, p. 744.</span></figcaption>
</figure>

Moving left reduces PV voltage and increases PV current; moving right raises voltage and reduces current. The paper tests both choices and compares how quickly they settle after irradiance changes.

<h2 id="experimental-validation">5. Experimental validation</h2>

### Bench configuration

The algorithm was implemented on a **TMS320F28335 microcontroller**, using a **200 W boost converter**, a **62050H-600S PV emulator**, and **four 12 V YPC33-12 VRLA batteries**. The absorption-stage experiment used a **53.3 V charging-voltage limit** for the battery bank.

<div class="project-table-scroll" role="region" aria-label="PV emulator settings from Table I" tabindex="0" markdown="1">

| PV emulator parameter | Setting |
|---|---|
| Open-circuit voltage, V<sub>OC</sub> | 35.0 V |
| Short-circuit current, I<sub>SC</sub> | 3.0 A |
| MPP voltage, V<sub>MP</sub> | 30.0 V |
| MPP current, I<sub>MP</sub> | 2.5 A |

</div>

These are the **Table I emulator settings**. The converter's 200 W rating describes the hardware, rather than the PV power delivered in this test.

### From maximum power tracking to battery-voltage limitation

The waveforms show three phases: initial MPP search, charging at MPP as battery voltage rises, and active power reduction once the charging-voltage limit is reached. With right-side operation, PV voltage rises and PV current falls as power is curtailed, keeping battery voltage from continuing to increase.

<figure>
  <a href="/images/research/pv-battery/right-operating-point-waveforms.png" target="_blank" rel="noopener" aria-label="View original: right-side MPPT to power-limiting transition"><img src="/images/research/pv-battery/right-operating-point-waveforms.png" alt="Measured PV voltage, battery voltage, PV current and PV power during MPP search, MPP charging and transition to battery-voltage limitation on the right operating branch" width="609" height="994" loading="lazy"></a>
  <figcaption><strong>Automatic transition to power limitation.</strong> The marked limit point separates maximum-power charging from reduced-power operation on the right branch. <span class="figure-source">ICRERA 2016, Figure 7, p. 745.</span></figcaption>
</figure>

<details markdown="1">
<summary>Compare left-side charging and the measured power–voltage trajectories</summary>

The left-side test reaches the charging limit by lowering PV voltage. The two measured P–V trajectories show how each operating point moves away from MPP.

<figure>
  <a href="/images/research/pv-battery/left-operating-point-waveforms.png" target="_blank" rel="noopener" aria-label="View original: left-side charging waveforms"><img src="/images/research/pv-battery/left-operating-point-waveforms.png" alt="Measured voltage, current and power waveforms for the transition to left-side PV power limitation" width="613" height="991" loading="lazy"></a>
  <figcaption><strong>Left-side charging and power limitation.</strong> PV voltage decreases after the battery reaches its limit. <span class="figure-source">ICRERA 2016, Figure 5, p. 744.</span></figcaption>
</figure>

<figure>
  <a href="/images/research/pv-battery/left-operating-point-pv-curve.png" target="_blank" rel="noopener" aria-label="View original: measured left-side PV trajectory"><img src="/images/research/pv-battery/left-operating-point-pv-curve.png" alt="Oscilloscope power–voltage trajectory showing MPP tracking followed by movement toward the left reduced-power operating point" width="617" height="609" loading="lazy"></a>
  <figcaption><strong>Measured left-side P–V trajectory.</strong> <span class="figure-source">ICRERA 2016, Figure 6, p. 744.</span></figcaption>
</figure>

<figure>
  <a href="/images/research/pv-battery/right-operating-point-pv-curve.png" target="_blank" rel="noopener" aria-label="View original: measured right-side PV trajectory"><img src="/images/research/pv-battery/right-operating-point-pv-curve.png" alt="Oscilloscope power–voltage trajectory showing MPP tracking followed by movement toward the right reduced-power operating point" width="617" height="613" loading="lazy"></a>
  <figcaption><strong>Measured right-side P–V trajectory.</strong> <span class="figure-source">ICRERA 2016, Figure 8, p. 745.</span></figcaption>
</figure>

</details>

### Response to changing irradiance

The fast-change test increased irradiance from **600 to 1,000 W/m² in 1 second**. The original left- and right-side measurements below show the controller adjusting PV output while limiting battery voltage.

<figure>
  <a href="/images/research/pv-battery/fast-irradiance-left.png" target="_blank" rel="noopener" aria-label="View original: fast irradiance change on the left branch"><img src="/images/research/pv-battery/fast-irradiance-left.png" alt="Original left-side experimental traces of PV current, power, PV voltage and battery voltage during the fast irradiance increase, with response interval t1 marked" width="561" height="994" loading="lazy"></a>
  <figcaption><strong>Fast irradiance change: left operating point.</strong> The marked interval t<sub>1</sub> identifies the response to increased irradiance. <span class="figure-source">ICRERA 2016, Figure 9, p. 745.</span></figcaption>
</figure>

<figure>
  <a href="/images/research/pv-battery/fast-irradiance-right.png" target="_blank" rel="noopener" aria-label="View original: fast irradiance change on the right branch"><img src="/images/research/pv-battery/fast-irradiance-right.png" alt="Original right-side experimental traces under fast irradiance increase, with response interval t2 marked" width="561" height="994" loading="lazy"></a>
  <figcaption><strong>Fast irradiance change: right operating point.</strong> The comparison uses the interval t<sub>2</sub>. <span class="figure-source">ICRERA 2016, Figure 10, p. 745.</span></figcaption>
</figure>

<figure>
  <a href="/images/research/pv-battery/dynamic-response-comparison.png" target="_blank" rel="noopener" aria-label="View original: dynamic response comparison"><img src="/images/research/pv-battery/dynamic-response-comparison.png" alt="Battery-voltage response comparison for left and right operating points, with t1 and t2 marked and a shorter interval for right-side operation" width="571" height="494" loading="lazy"></a>
  <figcaption><strong>Right-side operation responds faster in the reported test.</strong> The paper reports t<sub>2</sub> &lt; t<sub>1</sub>; it does not tabulate numerical settling times or a percentage improvement. <span class="figure-source">ICRERA 2016, Figure 12, p. 746.</span></figcaption>
</figure>

<details markdown="1">
<summary>Slow irradiance-change experiment</summary>

For the slower test, irradiance increased from **600 to 1,000 W/m² over 45 seconds**. The left-side operating point adjusted while battery voltage remained approximately constant.

<figure>
  <a href="/images/research/pv-battery/slow-irradiance-left.png" target="_blank" rel="noopener" aria-label="View original: slow irradiance change"><img src="/images/research/pv-battery/slow-irradiance-left.png" alt="Original slow irradiance-change test showing changing PV current, power and voltage while battery voltage remains approximately constant" width="564" height="991" loading="lazy"></a>
  <figcaption><strong>Slow irradiance variation with battery-voltage limitation.</strong> <span class="figure-source">ICRERA 2016, Figure 11, p. 746.</span></figcaption>
</figure>

</details>

<h2 id="outcomes">Outcomes and engineering implications</h2>

The study demonstrates a feedback-based transition between maximum-energy harvesting and battery-constrained PV generation using one modified P&O algorithm. The absorption-stage experiments show battery-voltage limitation under changing irradiance, and the operating-point comparison supports **right-side operation for faster response in the tested conditions**.

The controller is intended to avoid overcharging. The paper's evidence consists of short-term electrical waveforms; battery-lifetime extension and long-term energy-yield gains were not measured in this study.

<h2 id="project-resources">Sources and related work</h2>
<span id="pv-integration-into-dc-microgrids"></span>

- **Publication:** Fulong Li, Muhannad Alshareef, Zhengyu Lin and Wei Jiang, [“A modified MPPT algorithm with integrated active power control for PV-battery systems,” IEEE ICRERA 2016](https://ieeexplore.ieee.org/document/7884432), pp. 742–746.
- **Figure provenance:** All figures above are extracted from the supplied paper, retaining their original colours, proportions and annotations. [Figure source manifest](/files/research/pv-battery/figure-sources.json).
- **System coordination:** [DC Microgrid Control Strategies](/research/dcmg/) and [Rule-Based EMS](/research/dcmg/rule-based-ems/) place PV power limitation within wider source-and-storage operation.
- **Related work:** [Battery Energy Storage Systems](/research/battery_storage/), [Energy Management Systems](/research/ems/) and [Experimental Platforms](/research/experimental_platforms/).

