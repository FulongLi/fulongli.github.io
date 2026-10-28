---
layout: single
title: "AIPE PCB Agent"
permalink: /research/aipe-pcb-agent/
author_profile: true
excerpt: "Requirement-driven PCB design automation with Python and KiCad, illustrated by a 5 kW SiC buck converter."
body_class: microgrid-project-page
project_stylesheet: /assets/css/marine-project.css
project_contents: true
---

AIPE PCB Agent is my open-source project for automating power-electronics PCB design. It connects structured engineering requirements to editable KiCad projects, with Python generators for schematics, component placement, routing, checks and exports. Within the AIPE workflow, it sits downstream of electrical design and turns circuit and layout inputs into a traceable CAD package.

[Explore the repository](https://github.com/FulongLi/AIPE-PCB-Agent)

## Framework

The framework separates the electrical circuit model from its schematic presentation and PCB geometry. A shared model records components, pins and nets; separate generators decide how to draw the circuit and arrange the board. This lets the automation reuse common tools across converter projects.

| Layer | Role |
| --- | --- |
| Requirements | Capture specifications, components, interfaces, insulation constraints, floorplans and routing inputs in YAML/JSON files. |
| Engineering knowledge | Retrieve reference-derived circuit blocks, component records and layout rules with links to their sources. |
| Circuit and CAD generation | Build the circuit model, hierarchical schematics, project libraries, board stack-up, net classes and design rules. |
| Placement and routing | Arrange functional regions, define copper zones and keep-outs, and route connections with a grid-based router. |
| Checks and outputs | Run native KiCad ERC/DRC, compare netlists, inspect routing geometry and export files with SHA-256 manifests. |

The main implementation lives in `automation/`: `kicad_tools/` provides shared CAD and routing utilities, `knowledge/` handles engineering references, and converter-specific modules such as `sic_v3/` and `dab_v1/` assemble the design pipelines. `examples/` holds design inputs and generated projects; `docs/` explains the architecture and workflow.

The resulting workflow is:

1. Define requirements and document engineering assumptions.
2. Build the circuit model and generate schematics and board rules.
3. Place components, construct copper regions and route connections.
4. Run checks and produce review views and manufacturing exports.

See the [automation architecture](https://github.com/FulongLi/AIPE-PCB-Agent/blob/main/docs/architecture.md) for the module interfaces and generation flow.

## Example: 5 kW SiC Buck Converter

The SiC synchronous buck example illustrates the workflow with separate power and control boards. Its [design requirements](https://github.com/FulongLi/AIPE-PCB-Agent/blob/main/examples/sic-buck-400v-200v-5kw/input/requirements.yaml) specify:

| Parameter | Design value |
| --- | --- |
| Nominal input voltage | 400 V |
| Output voltage | 200 V |
| Output power | 5 kW |
| Nominal output current | 25 A |
| Switching frequency | 50 kHz |
| Power devices | Wolfspeed SiC MOSFETs |
| Controller | TI TMS320F28335 DSP |

### Power Board

The power board groups the SiC switching stage, isolated gate drivers and bias supplies, DC-link capacitors, output filter, sensing and protection circuitry. The layout separates the high-voltage power path from the low-voltage interface used by the control board.

<figure>
  <a href="/images/research/aipe-pcb-agent/power-board-3d.png" target="_blank" rel="noopener"><img src="/images/research/aipe-pcb-agent/power-board-3d.png" alt="KiCad 3D view of the SiC buck power board, showing the switching devices, large magnetic component, capacitor banks and control-board connector" width="1040" height="592" loading="lazy"></a>
  <figcaption>SiC buck power-board CAD view, showing the component arrangement and control-board interface.</figcaption>
</figure>

### Control Board

The control board brings together the TMS320F28335 DSP, local supplies, signal conditioning, PWM and protection interfaces, and debug connections. A mezzanine connector links it to the power board, keeping the control circuitry on a separate PCB.

<figure>
  <a href="/images/research/aipe-pcb-agent/control-board-3d.png" target="_blank" rel="noopener"><img src="/images/research/aipe-pcb-agent/control-board-3d.png" alt="KiCad 3D view of the control board, showing the central TMS320F28335 DSP, support circuitry, debug headers and mezzanine connector" width="1040" height="592" loading="lazy"></a>
  <figcaption>DSP control-board CAD view with local supplies, signal interfaces and mezzanine connection.</figcaption>
</figure>

The example connects requirements, circuit records, editable schematics and PCB layouts with BOMs, placement files, Gerbers, drill files and STEP models. The repository also records successive design revisions and their associated review outputs in the [example history](https://github.com/FulongLi/AIPE-PCB-Agent/blob/main/docs/history.md).

[AIPE Overview](/research/aipe/) · [Source Code](https://github.com/FulongLi/AIPE-PCB-Agent) · [Back to Research](/research/)
