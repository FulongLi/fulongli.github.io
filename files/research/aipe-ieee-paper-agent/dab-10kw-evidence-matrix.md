# Evidence Matrix

| Research question | Contribution claim | Evidence type and file | Figure/table/section | Status | Gap priority |
| --- | --- | --- | --- | --- | --- |
| RQ1: Does the chain reproduce the analytical operating point in switching simulation? | C3 | Simulation: AIPE-Workflows `results/circuit-sim-level1/`, `results/timestep-convergence-table.json` (9,996.8 W against 10,000 W; series current 13.6779 A against 13.6775 A; phase shift 22.5000°) | Table II, Fig. 3 | verified (analytical gate pass) | none |
| RQ2: How closely do analytical models agree with FEM and CAD? | C1 | Simulation: `results/fem-transformer-window/` (leakage −4.4 %), `results/fem-heatsink/` (thermal resistance +8.6 %), `results/cad-heatsink/` (mass −1.3 %) | Table III, Fig. 4 | verified (field-simulation gate pass) | none |
| RQ3: Does feedback change upstream design quantities? | C2 | Simulation: `results/iteration-example-a/` (phase shift 22.50° → 21.26°, peak current +14 %), `results/iteration-reconcile-it03/` (loss 131.7 → 127.2 W, hottest junction 63.0 → 61.7 °C) | Table IV | available | important: no baseline flow for comparison |
| RQ4: Is the run reproducible from a clean checkout? | C3 | Other: `results/acceptance-2026-10-21/` (every engineering value identical) | Table V | verified | none |
| Gap statement | C1 | Literature: none yet | Introduction, Related Work | planned | blocking |
| Comparison with a conventional design flow | C1, C2 | none | Results | planned | blocking for comparative claims |
| Hardware performance | none claimed | Experiment: none (`experimental` and `hardware_qualification` gates `not_run`) | Limitations | missing | blocking for any hardware claim |
| PCB completion | C3 | Other: `results/pcb-erc-drc/` (DRC errors 0 / 0 / 0, unconnected 26 / 23 / 24; gate fail) | Table V, Limitations | available, gate fail | important |

Keep 2–4 concrete contribution claims; distinguish planned evidence from results.
