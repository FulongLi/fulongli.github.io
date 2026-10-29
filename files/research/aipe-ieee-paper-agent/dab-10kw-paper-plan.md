# Paper Plan

Produced on 29 October 2026 by following `core/workflows/idea-to-paper.md` and `core/policies/scientific-integrity.md` of AIPE-IEEE-Paper-Agent (commit `5192c62`), with Claude Code as the host agent. Evidence is the executed AIPE-Workflows reference run `examples/dab-10kw` (commit `6284f18`); every number below is copied from that record. Nothing has been drafted as manuscript prose, and no reference has been added.

## Working Title

Agent-Coordinated Design of a 10 kW SiC Dual-Active-Bridge Converter

## Target Venue

IEEE Open Journal of Power Electronics (`ieee-ojpel`): a full-length, two-column power-electronics journal suited to a design-methodology paper. Current length limits must be confirmed before drafting.

## Manuscript Workspace

Paper slug: `dab-10kw-aipe`

Template family: journal, `ieeeojpel` class, initialised with `scripts/create-manuscript.py dab-10kw-aipe --venue ieee-ojpel --domain power-electronics`

Overleaf / local LaTeX notes: upload with `main.tex` as the main document; not compiled yet.

## Research Spine

Problem: early-stage power-converter design spans electrical, magnetic, thermal, field, mechanical and PCB tools, and the data between them is usually passed by hand.

Gap: to be established by a literature review with verified citations (none added yet). The working hypothesis is that design-automation studies typically cover one or two domains, and agent-based approaches rarely record which results are computed, simulated or measured.

Idea: specialist agents exchange a shared Engineering State with provenance, run as a checkpointed task graph with verification gates, and feed downstream results back into upstream models through explicit iterations.

Evidence: the executed 10 kW DAB reference run (800 V to 400 V, 100 kHz; 14 tasks, 12 Engineering State versions), its two recorded feedback iterations and its clean-checkout reproduction.

Impact: a reproducible, auditable multi-domain design record that shows where solver results confirm analytical estimates and where engineering review and measurement are still required.

## Research Questions

1. Does the coordinated chain reproduce the analytical operating point in switching simulation?
2. How closely do the fast analytical sizing models agree with solver-backed field and CAD results?
3. Do downstream results, fed back through explicit iterations, change upstream design quantities?
4. Is the complete run reproducible from a clean checkout?

## Contributions

1. We develop a multi-agent design architecture in which specialist agents share an Engineering State with provenance and pass verification gates that keep computed, simulated and measured evidence distinct.
2. We implement and quantify cross-domain feedback, in which magnetics and finite-element parameters are reconciled back into the circuit model, on a 10 kW SiC DAB.
3. We report an end-to-end design run from specification to CAD and PCB that reproduces from a clean checkout, with failed and unrun gates recorded explicitly.

## Paper Outline

1. Abstract: written last, from the evidence that exists.
2. Introduction: problem, gap (with verified citations), contributions.
3. Related Work: converter design optimisation, design automation, tool-using and multi-agent AI systems.
4. Method: agents, Engineering State, task graph, gates, iterate and reconcile operations.
5. Case Study Setup: DAB specification, tools and versions, run environment.
6. Results: analytical versus simulated operating point; analytical versus FEM and CAD; feedback iterations; reproduction.
7. Limitations: unfinished PCB routing, no Level 3 manufacturer models, correlation film coefficients, no measurement.
8. Conclusion.

## Figure and Table Plan

| Item | Content | Source |
| --- | --- | --- |
| Fig. 1 | Agent architecture and coordination layer | redraw from the AIPE framework diagram |
| Fig. 2 | DAB task graph with verification gates | `results/plan.json`, `results/verification.json` |
| Fig. 3 | Level 1 switching waveforms | `results/figures/circuit-sim-level1-figure-overview.png` |
| Fig. 4 | Transformer-window and heat-sink FEM fields | `results/figures/fem-transformer-window-B_leakage.png`, `fem-heatsink-base_bottom_temperature.png` |
| Table I | Specification and tool versions | `specification.yaml`, `environment-manifest.json` |
| Table II | Analytical versus Level 1 operating point | README, Level 1 table |
| Table III | Analytical versus FEM and CAD | README, window FEM, heat-sink FEM, CAD tables |
| Table IV | Feedback iterations A and D | `results/iteration-example-a/`, `results/iteration-reconcile-it03/` |
| Table V | Gate status, including `cad_pcb` fail and unrun gates | `results/verification.json` |

## Evidence Needed

| Gap | Priority | Note |
| --- | --- | --- |
| Literature review and verified citations for the gap statement | blocking | no reference added; the gap is a hypothesis until cited |
| Baseline for claims about effort, consistency or error compared with a conventional flow | blocking | none exists; without it, claims are limited to what the run shows |
| Hardware measurements for any efficiency or temperature claim | blocking for those claims | the ledger keeps `experimental` and `hardware_qualification` at `not_run`; frame the paper as design methodology with simulation evidence |
| Finished PCB routing | important | `cad_pcb` gate fails: 26 / 23 / 24 unconnected items on the three boards |
| Level 3 manufacturer SPICE model run | important | Level 2 uses a behavioural switch model |
| Engineering review of transformer insulation and heat-sink bushing path | important | recorded as CAD review items |
| CFD for the film coefficients | optional | thermal and FEM use correlation inputs |

## Recommended Template

`ieee-ojpel`, already initialised in `manuscripts/dab-10kw-aipe`.

## Next Actions

1. Run a literature search and verify every citation against its source before drafting the introduction.
2. Decide whether to define a baseline comparison or narrow the claims to the reported run.
3. Draft Method, Case Study Setup and Results against Tables II to V; leave the abstract and introduction until those exist.
4. Compile `main.tex`, inspect the PDF and run the publication-readiness review.
