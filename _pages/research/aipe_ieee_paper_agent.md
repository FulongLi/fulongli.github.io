---
layout: single
title: "AIPE IEEE Paper Agent"
permalink: /research/aipe-ieee-paper-agent/
author_profile: true
excerpt: "The research-writing agent of the AIPE framework: evidence-linked paper plans and venue-specific IEEE manuscripts, illustrated by a paper plan for the 10 kW DAB benchmark."
body_class: microgrid-project-page
project_stylesheet: /assets/css/marine-project.css
project_contents: true
---

AIPE IEEE Paper Agent is the research-writing agent in the AIPE framework. It turns a research idea and the evidence recorded by the design agents into an evidence-linked paper plan and a LaTeX manuscript workspace built on the official IEEE template of the chosen venue. It never invents results or reference metadata. This page explains the framework it belongs to, its role there, how the agent is organised, and a paper plan it has produced for the 10 kW DAB benchmark.

[Explore the repository](https://github.com/FulongLi/AIPE-IEEE-Paper-Agent)

## The AIPE Framework

{% include aipe-framework.html agent="paper" %}

## Role of the IEEE Paper Agent

The design agents end in a review package: results, evidence and open items for engineering review. The IEEE Paper Agent works from that record. It frames a research question, maps each claim to evidence the workflow actually produced, and prepares the manuscript in the venue's own template. Where the evidence is missing, it records a gap instead of filling it, so computed, simulated and measured results stay distinct in the paper as they are in the Engineering State.

| Interface | Content |
| --- | --- |
| Inputs | A research question with scope and target venue; Engineering State fields and evidence IDs from AIPE runs |
| Outputs | A paper plan with evidence matrix, a venue-specific LaTeX workspace, and citation and LaTeX audit reports |
| Hand-off | The author drafts or reviews the prose, compiles and inspects the PDF, verifies citations and submits; submission is never automatic |

The Engineering State maps onto the paper by meaning rather than by an automatic converter:

| Engineering State | Paper workflow |
| --- | --- |
| Project, requirements, architecture | Scope, research questions and design intent |
| Simulation runs | Reproducible methods, with tool versions and inputs |
| Validation checks | Evidence supporting or contradicting a specific claim |
| Evidence records | Source identifiers, provenance, artefacts and review status |
| Unreviewed assumptions | Stated hypotheses and limitations, never measured results |

The [agent interface](https://github.com/FulongLi/AIPE-IEEE-Paper-Agent/blob/main/aipe.yaml) and [AIPE integration notes](https://github.com/FulongLi/AIPE-IEEE-Paper-Agent/blob/main/docs/aipe-integration.md) define these inputs, outputs and limits.

## How the Agent Is Organised

The agent is a single maintained instruction layer with Python tools around it. Writing, citation and review rules live in one set of core workflows and policies; venue profiles wrap the official IEEE templates; scripts initialise and audit manuscripts. A Codex or Claude host follows the workflows, and the scripts make the template and audit steps deterministic.

<figure class="project-blueprint">
  <a href="/images/research/aipe-ieee-paper-agent/agent-architecture.svg" target="_blank" rel="noopener"><img src="/images/research/aipe-ieee-paper-agent/agent-architecture.svg" alt="Flow chart of AIPE IEEE Paper Agent: a research idea and AIPE evidence feed research planning, venue profiles and the manuscript workspace, followed by evidence-based drafting and audits, with missing evidence returned to the plan, then hand-off to the author" width="760" height="668" loading="lazy"></a>
  <figcaption>Internal organisation of AIPE IEEE Paper Agent, from a research idea and recorded evidence to an audited manuscript workspace.</figcaption>
</figure>

| Part | Responsibility |
| --- | --- |
| Research planning | The idea-to-paper workflow builds a Problem, Gap, Idea, Evidence and Impact spine, three to five testable questions, two to four verifiable claims and an evidence matrix that ranks each gap as blocking, important or optional. |
| Venue profiles | Six profiles (IEEE conference, Transactions, Access, Open Journal of Power Electronics, Transactions on AI, Open Journal of Control Systems) record each official template's entry file, class options, front matter and required assets. |
| Manuscript workspace | The generator copies the real template, keeps its preamble and front-matter order, and inserts section files and planning notes with explicit TODOs in place of sample prose. |
| Evidence-based drafting | Sections are drafted Method, Setup and Results first, Introduction and Abstract last, so summary claims describe evidence that exists. An optional power-electronics domain pack adds curated terminology and knowledge, never evidence. |
| Audits | A citation audit against the indexed reference collection, a static LaTeX and venue audit, and a publication-readiness review that lists blockers first. |

Four policies govern every stage: scientific integrity, citations, LaTeX and figures. The same workflows are packaged as portable Codex and Claude skills with checksums back to the canonical files, and 21 tests guard template integrity, venue differences and the generated packages. The [architecture](https://github.com/FulongLi/AIPE-IEEE-Paper-Agent/blob/main/docs/architecture.md) and [usage guide](https://github.com/FulongLi/AIPE-IEEE-Paper-Agent/blob/main/docs/usage.md) describe these parts in detail.

## Example: Paper Plan for the 10 kW DAB Benchmark

This example takes the AIPE benchmark, a 10 kW dual-active-bridge converter from 800 V to 400 V at 100 kHz, from executed design run to paper plan. The agent's idea-to-paper workflow was run with Claude Code as the host, together with its scripts to initialise and audit the manuscript. The evidence is the [AIPE-Workflows reference run](https://github.com/FulongLi/AIPE-Workflows/blob/main/examples/dab-10kw/README.md) of the converter: 14 tasks from specification to CAD and PCB, with every result recorded against a verification gate.

| Input | Value |
| --- | --- |
| Research idea | Coordinated specialist agents with a shared Engineering State and verification gates, demonstrated on the DAB benchmark |
| Evidence | Executed AIPE-Workflows DAB run, its two feedback iterations and its clean-checkout reproduction |
| Venue | IEEE Open Journal of Power Electronics (`ieee-ojpel`) |
| Domain pack | Power electronics |
| Working title | Agent-Coordinated Design of a 10 kW SiC Dual-Active-Bridge Converter |

### Research Spine

| Element | Statement |
| --- | --- |
| Problem | Early-stage converter design spans electrical, magnetic, thermal, field, mechanical and PCB tools, and the data between them is usually passed by hand. |
| Gap | A working hypothesis, to be established by a literature review with verified citations: design-automation studies typically cover one or two domains, and agent-based approaches rarely record which results are computed, simulated or measured. |
| Idea | Specialist agents exchange a shared Engineering State with provenance, run as a checkpointed task graph with verification gates, and feed downstream results back through explicit iterations. |
| Evidence | The executed DAB run, its feedback iterations and its reproduction from a clean checkout. |
| Impact | A reproducible, auditable multi-domain design record that shows where solvers confirm analytical estimates and where review and measurement are still required. |

### Research Questions and Evidence

Each question maps to results the run has already recorded, and every number is copied from the run record.

| Research question | Evidence from the run | Status |
| --- | --- | --- |
| Does the chain reproduce the analytical operating point in switching simulation? | 9,996.8 W against 10,000 W; series current 13.6779 A against 13.6775 A; phase shift 22.5000° against 22.5° | Verified |
| How closely do analytical models agree with field and CAD results? | Transformer leakage from FEM 4.4 % below the 1-D estimate; heat-sink resistance from FEM 8.6 % above the analytical model; CAD sink mass 1.3 % below the model | Verified |
| Do downstream results, fed back, change upstream quantities? | Turns ratio 2.1: phase shift 22.50° to 21.26°, peak current +14 %. Reconciled leakage and magnetising inductance: loss 131.7 to 127.2 W, hottest junction 63.0 to 61.7 °C | Available |
| Is the run reproducible from a clean checkout? | Every engineering value identical in the acceptance re-run | Verified |

From this mapping, the agent proposed three contributions:

1. A multi-agent design architecture in which specialist agents share an Engineering State with provenance and pass verification gates that keep computed, simulated and measured evidence distinct.
2. Cross-domain feedback, in which magnetics and finite-element parameters are reconciled back into the circuit model, quantified on the 10 kW SiC DAB.
3. An end-to-end design run from specification to CAD and PCB that reproduces from a clean checkout, with failed and unrun gates recorded explicitly.

### Evidence Gaps

The plan also records what the paper cannot yet claim. The agent ranked what is still needed before drafting:

| Gap | Priority | Reason |
| --- | --- | --- |
| Literature review and verified citations | Blocking | The gap statement is a hypothesis until it is cited; no reference has been added |
| Baseline comparison with a conventional design flow | Blocking for comparative claims | Without it, claims are limited to what the run shows |
| Hardware measurements | Blocking for any efficiency or temperature claim | The run keeps its experimental and hardware-qualification gates at not run, so the paper is framed as design methodology with simulation evidence |
| Finished PCB routing | Important | The CAD and PCB gate fails, with 23 to 26 unconnected items on each board |
| Manufacturer SPICE model run | Important | The detailed circuit model uses a behavioural switch model |
| Engineering review of insulation and mounting | Important | Recorded as CAD review items |
| CFD for the film coefficients | Optional | Thermal and FEM results use correlation inputs |

### Manuscript Workspace and Audits

The agent then initialised the OJPEL workspace from the official template and ran its audits. The workspace holds `main.tex` with the journal's class, logo and front matter intact, seven section files with explicit TODOs, figure, table and reference folders, and notes for the paper plan, evidence matrix, citation audit and LaTeX tasks.

| Step | Result |
| --- | --- |
| Repository tests | 21 tests pass |
| Manuscript initialisation for `ieee-ojpel` | Workspace created; template files unchanged |
| Static LaTeX and venue audit | Pass against the OJPEL profile: class, required front-matter commands and assets |
| Citation audit | 0 citations and 0 bibliography entries, as intended before the literature review |
| Reference index | 4,758 records indexed; 191 duplicate keys and 35 records flagged as needing verification |

### Task Outputs

The task produced the [paper plan](/files/research/aipe-ieee-paper-agent/dab-10kw-paper-plan.md) and [evidence matrix](/files/research/aipe-ieee-paper-agent/dab-10kw-evidence-matrix.md), and an audited manuscript workspace ready for drafting. No manuscript prose was drafted and no reference was added; the PDF was not compiled, because no TeX distribution was installed on the machine used. The static audits confirm structure, not citation truth or scientific quality, and the plan's claims stay limited to the simulation evidence until the blocking gaps are closed.

[AIPE Overview](/research/aipe/) · [Source Code](https://github.com/FulongLi/AIPE-IEEE-Paper-Agent) · [Back to Research](/research/)
