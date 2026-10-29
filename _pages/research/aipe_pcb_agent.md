---
layout: single
title: "AIPE PCB Agent"
permalink: /research/aipe-pcb-agent/
author_profile: true
excerpt: "The PCB design agent of the AIPE framework: from converter requirements to checked KiCad schematics and boards, illustrated by a 5 kW SiC buck converter."
body_class: microgrid-project-page
project_stylesheet: /assets/css/marine-project.css
project_contents: true
---

AIPE PCB Agent is the PCB design agent in the AIPE framework. It turns a converter's requirements into editable KiCad schematics and board layouts, runs KiCad's own checks on them and packages the results for engineering review. This page explains the framework it belongs to, its role there, how the agent is organised, and a 5 kW SiC converter it has designed.

[Explore the repository](https://github.com/FulongLi/AIPE-PCB-Agent)

## The AIPE Framework

{% include aipe-framework.html agent="pcb" %}

## Role of the PCB Agent

PCB Agent works at the physical-design stage, downstream of **AIPE Electrical Design** and alongside the CAD Agent, which produces mechanical geometry such as transformers and heat sinks. It takes the converter's electrical decisions and turns them into boards that an engineer can open, check and revise.

| Interface | Content |
| --- | --- |
| Inputs | Requirement files: converter specification, insulation-coordination table and stack-ups, component selections with sources, interface pin maps, floorplan and routing inputs |
| Outputs | Native KiCad projects, ERC/DRC and layout-check records, manufacturing exports and review documents |
| Hand-off | AIPE-Workflows re-runs the KiCad ERC and DRC on the generated boards for its CAD/PCB gate; the results then go to human engineering review |

A clean ERC/DRC result is a statement about the generated CAD files under the recorded rule set. It does not establish electrical safety, insulation compliance or manufacturability. The [agent interface](https://github.com/FulongLi/AIPE-PCB-Agent/blob/main/aipe.yaml) defines these inputs, outputs and limits.

## How the Agent Is Organised

The agent is built around one shared circuit model. The model records every part, pin and net, while schematic drawing and board geometry are generated from it separately. Checks compare the CAD files with the model and feed their findings back to the stage that needs another pass.

<figure class="project-blueprint">
  <a href="/images/research/aipe-pcb-agent/agent-architecture.svg" target="_blank" rel="noopener"><img src="/images/research/aipe-pcb-agent/agent-architecture.svg" alt="Flow chart of AIPE PCB Agent: requirement files and a knowledge base feed a shared circuit model and design rules, which drive schematic generation and board construction, followed by verification, exports and hand-off, with findings fed back to the model, placement or routing" width="760" height="668" loading="lazy"></a>
  <figcaption>Internal organisation of AIPE PCB Agent, from requirement files to checked and packaged KiCad projects.</figcaption>
</figure>

| Part | Responsibility |
| --- | --- |
| Requirement files | YAML/JSON files hold every number the design uses: ratings, parts, interfaces, insulation distances, stack-ups and floorplan regions. |
| Knowledge base | Design skills, circuit blocks, component records and layout rules, each traced to manufacturer or reference-design sources. |
| Circuit model and rules | Converter-specific Python modules build the part and connection model; net classes and KiCad design rules are derived from the insulation table. |
| Schematic generation | Groups parts by function, draws and routes hierarchical sheets, and refuses to write a sheet whose connectivity differs from the model. |
| Board construction | Sets the stack-up, places parts with insulation-aware spacing, forms copper zones and routes connections with a deterministic grid router. |
| Verification | Runs native `kicad-cli` ERC and DRC with schematic parity, then checks netlist equality, routing quality, layout metrics and copper islands. |
| Exports and records | Writes editable projects, PDFs, Gerber, drill, BOM, placement and STEP files, with SHA-256 manifests linking each output to its sources. |

The converter-specific modules supply only design data and policies, while the shared tools do the CAD generation and checking. This lets buck, DAB and future converter projects reuse the same operations. The [automation architecture](https://github.com/FulongLi/AIPE-PCB-Agent/blob/main/docs/architecture.md) and [task workflow](https://github.com/FulongLi/AIPE-PCB-Agent/blob/main/docs/agent-workflow.md) describe the modules and their acceptance gates.

## Example: 5 kW SiC Buck Converter

This example shows a complete task, from the specification to two routed boards. The agent was asked to design a SiC synchronous buck converter; its [design requirements](https://github.com/FulongLi/AIPE-PCB-Agent/blob/main/examples/sic-buck-400v-200v-5kw/input/requirements.yaml) specify:

| Parameter | Design value |
| --- | --- |
| Nominal input voltage | 400 V |
| Output voltage | 200 V |
| Output power | 5 kW |
| Nominal output current | 25 A |
| Switching frequency | 50 kHz |
| Power devices | Wolfspeed SiC MOSFETs |
| Controller | TI TMS320F28335 DSP |

### From Requirements to Boards

The task followed the agent's workflow:

1. **Requirements and engineering.** Values the task left open, such as the input range, cooling and ripple targets, were recorded as labelled assumptions. Calculations and the knowledge base then selected the parts: Wolfspeed C4MS025120K SiC MOSFETs, UCC21710-Q1 isolated gate drivers with UCC14141-Q1 bias modules, a custom 272 µH High Flux toroid and isolated current and voltage sensing.
2. **Architecture.** The agent compared board arrangements and chose two boards: a power board for conversion, gate drive, sensing and protection, and a DSP control board connected through a 2 × 25 mezzanine.
3. **Schematics and boards.** It generated hierarchical schematics, placed the parts with insulation-aware spacing along each board's isolation barrier, and routed both four-layer boards.
4. **Checks and outputs.** Both boards reached zero native ERC/DRC findings with schematic parity, and the exported netlists matched the circuit model exactly. The task then produced the review package.

### Power Board

The 240 × 180 mm power board groups the SiC switching stage, isolated gate drivers and bias supplies, DC-link capacitors, output filter, sensing and protection circuitry. The layout separates the high-voltage power path from the low-voltage interface used by the control board.

<figure>
  <a href="/images/research/aipe-pcb-agent/power-board-3d.png" target="_blank" rel="noopener"><img src="/images/research/aipe-pcb-agent/power-board-3d.png" alt="KiCad 3D view of the SiC buck power board, showing the switching devices, large magnetic component, capacitor banks and control-board connector" width="1040" height="592" loading="lazy"></a>
  <figcaption>SiC buck power-board CAD view, showing the component arrangement and control-board interface.</figcaption>
</figure>

### Control Board

The 120 × 80 mm control board brings together the TMS320F28335 DSP, local supplies, signal conditioning, PWM and protection interfaces, and debug connections. The mezzanine connector stacks it on the power board's low-voltage strip, keeping the control circuitry on a separate PCB.

<figure>
  <a href="/images/research/aipe-pcb-agent/control-board-3d.png" target="_blank" rel="noopener"><img src="/images/research/aipe-pcb-agent/control-board-3d.png" alt="KiCad 3D view of the control board, showing the central TMS320F28335 DSP, support circuitry, debug headers and mezzanine connector" width="1040" height="592" loading="lazy"></a>
  <figcaption>DSP control-board CAD view with local supplies, signal interfaces and mezzanine connection.</figcaption>
</figure>

### Task Outputs

The task produced two editable KiCad board projects and their schematics, together with BOMs, placement files, Gerbers, drill files, STEP models, check reports and hashed manifests. The design is a CAD-complete prototype for review: no board has been fabricated, energised or measured.

A later clean-sheet revision (V3) redesigned the same converter after an independent review, moving the control board beside the power board on a keyed cable and mounting the heavy magnetics on the chassis. The [V3 package](https://github.com/FulongLi/AIPE-PCB-Agent/blob/main/examples/sic-buck-400v-200v-5kw-v3/README.md) and the [example history](https://github.com/FulongLi/AIPE-PCB-Agent/blob/main/docs/history.md) link each revision to its design records and review packages.

[AIPE Overview](/research/aipe/) · [Source Code](https://github.com/FulongLi/AIPE-PCB-Agent) · [Back to Research](/research/)
