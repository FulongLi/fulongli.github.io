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

AIPE PCB Agent is my open-source project for turning power-electronics design requirements into editable KiCad schematics and PCB layouts. Its framework combines structured design inputs, reusable engineering knowledge, Python automation and native KiCad checks. The 5 kW SiC buck example below shows how a task moves through that framework to a set of board designs and engineering files.

[Explore the repository](https://github.com/FulongLi/AIPE-PCB-Agent)

## Role in the AIPE Agent Framework

In the AIPE workflow, PCB Agent sits downstream of **AIPE Electrical Design**. It receives the converter specification, component and connection data, interface definitions and physical design constraints, then translates them into a board-level implementation.

> Electrical design → PCB Agent → CAD projects, check reports and engineering review package

Its outputs include native KiCad projects, schematic and layout views, connectivity and rule-check reports, and manufacturing exports. These give the engineer a consistent set of files to inspect and revise. The [repository overview](https://github.com/FulongLi/AIPE-PCB-Agent) and [agent interface](https://github.com/FulongLi/AIPE-PCB-Agent/blob/main/aipe.yaml) describe its place in the wider workflow and its input/output contracts.

## Internal Architecture

The implementation connects three main parts around a shared circuit model. That model records components, pins and nets; schematic presentation and PCB geometry are generated separately from it.

| Part | Responsibility |
| --- | --- |
| Design inputs and knowledge | YAML/JSON requirements define specifications, parts, interfaces, insulation constraints and board plans. A reference-derived knowledge base supplies circuit blocks, component records and layout rules. |
| Generation tools | Converter-specific Python modules build the circuit model. Shared KiCad utilities generate hierarchical schematics, libraries, board rules, placement, copper regions and routed connections. |
| Checks and records | Native KiCad ERC/DRC, netlist comparisons and geometry checks produce reports. Export tools generate review and manufacturing files with SHA-256 manifests. |

The converter modules supply design-specific data and policies while shared tools handle CAD generation and checking. This separation lets different converter projects reuse the same underlying operations. See the [automation architecture](https://github.com/FulongLi/AIPE-PCB-Agent/blob/main/docs/architecture.md) for the module interfaces.

## How a Task Runs

The task follows a sequence from requirements to board design, with checks feeding corrections back into the relevant stage:

1. **Define the task.** Capture operating conditions, parts, interfaces and physical constraints, and record engineering assumptions alongside the requirements.
2. **Build the electrical model.** Use calculations and component references to establish the parts and pin-to-net connections, then generate schematics and run electrical rule checks.
3. **Construct the boards.** Define stack-ups and design rules, place functional groups, form copper zones and keep-outs, and route the connections.
4. **Check and revise.** Compare the CAD netlists with the model, run PCB design-rule checks and inspect layout metrics. Findings identify where the model, placement or routing needs another pass; unresolved connections remain in the reports.
5. **Package the outputs.** Export editable projects, review views and manufacturing files, with manifests linking the results to the checked source files.

The [task workflow](https://github.com/FulongLi/AIPE-PCB-Agent/blob/main/docs/agent-workflow.md) describes the stages and their acceptance gates.

## Example: 5 kW SiC Buck Converter

For this task, the agent takes a SiC synchronous buck specification through circuit generation, board design and output packaging. Its [design requirements](https://github.com/FulongLi/AIPE-PCB-Agent/blob/main/examples/sic-buck-400v-200v-5kw/input/requirements.yaml) specify:

| Parameter | Design value |
| --- | --- |
| Nominal input voltage | 400 V |
| Output voltage | 200 V |
| Output power | 5 kW |
| Nominal output current | 25 A |
| Switching frequency | 50 kHz |
| Power devices | Wolfspeed SiC MOSFETs |
| Controller | TI TMS320F28335 DSP |

The example uses a two-board architecture: a power board for conversion, gate drive, sensing and protection, and a DSP control board connected through a mezzanine interface. The CAD views below show the physical arrangement produced for those two roles.

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

### Task Outputs

The task produces the two editable KiCad board projects and their schematics, alongside BOMs, placement files, Gerbers, drill files, STEP models and check reports. These files connect the original specification to the illustrated board arrangement. The [example history](https://github.com/FulongLi/AIPE-PCB-Agent/blob/main/docs/history.md) links successive revisions to their design records and review packages.

[AIPE Overview](/research/aipe/) · [Source Code](https://github.com/FulongLi/AIPE-PCB-Agent) · [Back to Research](/research/)
