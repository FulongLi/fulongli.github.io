---
layout: single
title: "SinO-OFH: WP4.1 Thermal Evaluation"
permalink: /research/sino-ofh/
author_profile: true
body_class: marine-project-page
project_stylesheet: /assets/css/marine-project.css
project_script: /assets/js/marine-project.js
excerpt: "Leading SinO-OFH WP4.1: engine-room thermal modelling, enclosure and fan sensitivity studies, and climate comparisons for the North Sea, Persian Gulf and Singapore."
---

<h2 id="overview">Overview</h2>
<span id="sino-ofh-wp41-thermal-evaluation"></span>

I led **Work Package 4.1 (WP4.1), Thermal Evaluation**, within the **SinO-OFH project in 2024**. The work assessed how the enclosure, equipment surface temperature, outdoor climate and ventilation affect the room temperature around the fuel-cell and converter equipment.

**My role:** Work package lead, covering requirement capture, construction of the room-temperature model, sensitivity studies and updated operating-condition simulations.

This work followed the [3MW marine fuel-cell hybrid powertrain project](/research/3mw-marine-fuel-cell/), which I led as a whole. That project quantified heat generation alongside the electrical schedule. SinO-OFH WP4.1 examined the thermal environment in which the equipment must operate.

<nav class="project-contents" aria-label="Project contents">
  <p><strong>On this page</strong></p>
  <ul>
    <li><a href="#overview">Overview</a></li>
    <li><a href="#model-development">Model development</a></li>
    <li><a href="#climate-scenarios">Climate scenarios</a></li>
    <li><a href="#north-sea">North Sea</a></li>
    <li><a href="#persian-gulf">Persian Gulf</a></li>
    <li><a href="#singapore">Singapore</a></li>
    <li><a href="#outcomes">Outcomes</a></li>
    <li><a href="#project-resources">Project resources</a></li>
  </ul>
</nav>

<h2 id="model-development">1. Requirements and model development</h2>

I represented the enclosure through the thermal capacity of its internal air, heat transfer through its boundaries, heat input from the fuel-cell/converter equipment and fan-driven air exchange. Initial studies varied enclosure thermal resistance and fan capacity to understand the model’s response before applying updated project specifications.

The requirements capture identified the information needed to make the assessment meaningful: room dimensions and construction, insulation properties, equipment surface temperatures, fan airflow, target room temperature and external temperature variation. The model then progressed from an initial enclosure description to the July 2024 update with revised aluminium wall and door construction and rock-wool insulation assumptions.

| Updated model input | Study condition |
|---|---|
| Enclosure dimensions | 6 m × 2.4 m × 3.5 m |
| Walls and door | Revised 5 mm aluminium construction with insulation assumptions |
| Door dimensions | 2 m × 0.8 m |
| Windows | None |
| Air-filled fraction | 50% |
| Equipment surface temperatures | 45°C and 60°C |
| Temperature reference in updated plots | 25°C |
| Climate cases | North Sea, Persian Gulf and Singapore |

The equipment surface temperature is a heat-source input to this room model. It is distinct from the total fuel-cell heat-energy outputs in the [3MW powertrain study](/research/3mw-marine-fuel-cell/). The work established the connection between electrical operation and enclosure assessment without assuming that every unit of stack heat entered the room air.

<details class="project-appendix">
<summary>Initial sensitivity studies: enclosure resistance and fan size</summary>
<p>The initial model examples use a 35°C reference. They precede the updated project scenarios below, which use 25°C. The plots explore the effect of thermal resistance and airflow rather than establish final equipment specifications.</p>
<div class="project-figures">
<figure>
  <a href="/images/research/marine-fuel-cell/sino-sensitivity-normal-resistance.png" target="_blank" rel="noopener" aria-label="View original: Fan off: reference enclosure resistance"><img src="/images/research/marine-fuel-cell/sino-sensitivity-normal-resistance.png" alt="Fan off: reference enclosure resistance" width="875" height="646" loading="lazy"></a>
  <figcaption><strong>Fan off: reference enclosure resistance.</strong> The initial example shows room temperature rising above the 35°C reference. <span class="figure-source">SinO-OFH WP4.1, slide 6.</span></figcaption>
</figure>
<figure>
  <a href="/images/research/marine-fuel-cell/sino-sensitivity-high-resistance.png" target="_blank" rel="noopener" aria-label="View original: Fan off: high enclosure resistance"><img src="/images/research/marine-fuel-cell/sino-sensitivity-high-resistance.png" alt="Fan off: high enclosure resistance" width="875" height="646" loading="lazy"></a>
  <figcaption><strong>Fan off: high enclosure resistance.</strong> Greater thermal isolation changes the response to heat input and ambient variation. <span class="figure-source">SinO-OFH WP4.1, slide 6.</span></figcaption>
</figure>
<figure>
  <a href="/images/research/marine-fuel-cell/sino-sensitivity-low-resistance.png" target="_blank" rel="noopener" aria-label="View original: Fan off: low enclosure resistance"><img src="/images/research/marine-fuel-cell/sino-sensitivity-low-resistance.png" alt="Fan off: low enclosure resistance" width="875" height="646" loading="lazy"></a>
  <figcaption><strong>Fan off: low enclosure resistance.</strong> With strong heat exchange, the room temperature closely follows the outdoor profile. <span class="figure-source">SinO-OFH WP4.1, slide 6.</span></figcaption>
</figure>
<figure>
  <a href="/images/research/marine-fuel-cell/sino-sensitivity-small-fan.png" target="_blank" rel="noopener" aria-label="View original: Small-fan example"><img src="/images/research/marine-fuel-cell/sino-sensitivity-small-fan.png" alt="Small-fan example" width="875" height="646" loading="lazy"></a>
  <figcaption><strong>Small-fan example.</strong> The fan runs for most of the example cycle and the room still exceeds the reference during parts of the cycle. <span class="figure-source">SinO-OFH WP4.1, slide 6.</span></figcaption>
</figure>
<figure>
  <a href="/images/research/marine-fuel-cell/sino-sensitivity-medium-fan.png" target="_blank" rel="noopener" aria-label="View original: Medium-fan example"><img src="/images/research/marine-fuel-cell/sino-sensitivity-medium-fan.png" alt="Medium-fan example" width="875" height="646" loading="lazy"></a>
  <figcaption><strong>Medium-fan example.</strong> In this example the model switches the fan as the room approaches the reference. <span class="figure-source">SinO-OFH WP4.1, slide 6.</span></figcaption>
</figure>
<figure>
  <a href="/images/research/marine-fuel-cell/sino-sensitivity-large-fan.png" target="_blank" rel="noopener" aria-label="View original: Large-fan example"><img src="/images/research/marine-fuel-cell/sino-sensitivity-large-fan.png" alt="Large-fan example" width="875" height="646" loading="lazy"></a>
  <figcaption><strong>Large-fan example.</strong> Increased airflow changes the temperature response and fan switching pattern. <span class="figure-source">SinO-OFH WP4.1, slide 6.</span></figcaption>
</figure>
</div>
</details>

<h2 id="climate-scenarios">2. Comparing three climates at 45°C and 60°C equipment temperature</h2>

The July update compared both equipment-temperature inputs in three operating regions. The climate ranges below are the scenarios specified in the project deck. The thermal-result plots use **time in seconds**, extending to approximately two days.

| Climate case | Ambient-air range | Seawater range recorded in the study |
|---|---:|---:|
| North Sea | 6–14°C | 3.5–11.4°C |
| Persian Gulf | 14–46.6°C | 19.3–34.4°C |
| Singapore | 24.3–32.4°C | 30.5–31°C |

<h2 id="north-sea">3. North Sea: cooler ambient conditions</h2>

For both heat-source temperatures, the simulated room stays below the 25°C reference and the fan remains off. Increasing the equipment surface temperature raises the room-temperature trace, while the cool external conditions continue to influence the enclosure strongly.

<div class="project-figures">
<figure>
  <a href="/images/research/marine-fuel-cell/sino-north-sea-45c.png" target="_blank" rel="noopener" aria-label="View original: North Sea: 45°C heat source"><img src="/images/research/marine-fuel-cell/sino-north-sea-45c.png" alt="North Sea: 45°C heat source" width="875" height="645" loading="lazy"></a>
  <figcaption><strong>North Sea: 45°C heat source.</strong> Room and outdoor temperatures remain below the 25°C reference; the fan stays off. <span class="figure-source">SinO-OFH WP4.1, slide 14.</span></figcaption>
</figure>
<figure>
  <a href="/images/research/marine-fuel-cell/sino-north-sea-60c.png" target="_blank" rel="noopener" aria-label="View original: North Sea: 60°C heat source"><img src="/images/research/marine-fuel-cell/sino-north-sea-60c.png" alt="North Sea: 60°C heat source" width="875" height="645" loading="lazy"></a>
  <figcaption><strong>North Sea: 60°C heat source.</strong> The warmer equipment changes the room response, which remains below the reference in this scenario. <span class="figure-source">SinO-OFH WP4.1, slide 15.</span></figcaption>
</figure>
</div>

<h2 id="persian-gulf">4. Persian Gulf: high ambient temperature</h2>

The fan switches on during hot periods in both cases. Room temperature nevertheless rises above the 25°C reference as the outdoor air becomes hotter. This result illustrates the constraint on using ambient-air ventilation to achieve a temperature target during hot-weather operation.

<div class="project-figures">
<figure>
  <a href="/images/research/marine-fuel-cell/sino-persian-gulf-45c.png" target="_blank" rel="noopener" aria-label="View original: Persian Gulf: 45°C heat source"><img src="/images/research/marine-fuel-cell/sino-persian-gulf-45c.png" alt="Persian Gulf: 45°C heat source" width="875" height="645" loading="lazy"></a>
  <figcaption><strong>Persian Gulf: 45°C heat source.</strong> Fan operation follows the hotter part of the ambient cycle, while the room exceeds the reference. <span class="figure-source">SinO-OFH WP4.1, slide 14.</span></figcaption>
</figure>
<figure>
  <a href="/images/research/marine-fuel-cell/sino-persian-gulf-60c.png" target="_blank" rel="noopener" aria-label="View original: Persian Gulf: 60°C heat source"><img src="/images/research/marine-fuel-cell/sino-persian-gulf-60c.png" alt="Persian Gulf: 60°C heat source" width="875" height="645" loading="lazy"></a>
  <figcaption><strong>Persian Gulf: 60°C heat source.</strong> The higher source-temperature case retains the strong influence of the outdoor temperature cycle. <span class="figure-source">SinO-OFH WP4.1, slide 15.</span></figcaption>
</figure>
</div>

<h2 id="singapore">5. Singapore: sustained warm conditions</h2>

The room exceeds the 25°C reference for much of the simulated period and the fan remains on throughout both plotted cases. This contrasts with the North Sea result, showing that the same enclosure and control target lead to different ventilation duties in different climates.

<div class="project-figures">
<figure>
  <a href="/images/research/marine-fuel-cell/sino-singapore-45c.png" target="_blank" rel="noopener" aria-label="View original: Singapore: 45°C heat source"><img src="/images/research/marine-fuel-cell/sino-singapore-45c.png" alt="Singapore: 45°C heat source" width="875" height="645" loading="lazy"></a>
  <figcaption><strong>Singapore: 45°C heat source.</strong> The fan remains on and the room temperature follows the warm ambient cycle. <span class="figure-source">SinO-OFH WP4.1, slide 14.</span></figcaption>
</figure>
<figure>
  <a href="/images/research/marine-fuel-cell/sino-singapore-60c.png" target="_blank" rel="noopener" aria-label="View original: Singapore: 60°C heat source"><img src="/images/research/marine-fuel-cell/sino-singapore-60c.png" alt="Singapore: 60°C heat source" width="875" height="645" loading="lazy"></a>
  <figcaption><strong>Singapore: 60°C heat source.</strong> The higher equipment-temperature input raises the room response while fan operation remains continuous. <span class="figure-source">SinO-OFH WP4.1, slide 15.</span></figcaption>
</figure>
</div>

The thermal study showed why enclosure construction and the operating environment belong in the assessment alongside the heat-source specification. Ventilation duty differed substantially between the three simulated regions. Temperature predictions remain conditional on the enclosure, insulation, heat-transfer and airflow assumptions used in each model version.

<h2 id="outcomes">6. Work package outcomes and my contribution</h2>

I developed an enclosure model for comparing heat-source conditions and ventilation behaviour across three climates. The work progressed from initial requirement capture and model sensitivity studies to the updated July 2024 enclosure and operating scenarios.

The results distinguish the cooler North Sea case, where the fan stays off, from the Persian Gulf case with changing fan duty and the Singapore case with continuous fan operation. They also show the limits of using ambient-air ventilation to reach the same temperature reference under different external conditions.

The work package provided a basis for reviewing enclosure, insulation and airflow assumptions alongside the equipment heat-source specification. These are model-dependent predictions for the documented scenarios.

<h2 id="project-resources">Project evidence and resources</h2>

The original figures come from my **SinO-OFH WP4.1 progress** presentation, including the initial model examples and the July 2024 update. Select a figure to open its original image.

[SinO-OFH figure sources and slide numbers](/files/research/marine-fuel-cell/sino-ofh-figure-sources.json)

[Microgrid Energy Management](/research/mgapp/) · [3MW Marine Fuel-Cell Project](/research/3mw-marine-fuel-cell/) · [Back to Research](/research/)
