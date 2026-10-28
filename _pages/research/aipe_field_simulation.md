---
layout: single
title: "AIPE Field Simulation"
permalink: /research/aipe-field-simulation/
author_profile: true
excerpt: "The finite-element agent of the AIPE framework: Gmsh and Elmer workflows for thermal and magnetic fields, illustrated by a heat sink for two TO-247 devices."
body_class: microgrid-project-page
project_stylesheet: /assets/css/marine-project.css
project_contents: true
---

AIPE Field Simulation is the finite-element agent in my AIPE framework. It drives the open-source tools Gmsh and Elmer to solve the thermal, magnetostatic and eddy-current problems of power-electronics design, and records every solve as an auditable case. This page explains the framework it belongs to, its role there, how the agent is organised, and a heat-sink study it has run.

[Explore the repository](https://github.com/FulongLi/AIPE-Field-Simulation)

## The AIPE Framework

{% include aipe-framework.html agent="field" %}

## Role of the Field Simulation Agent

Field Simulation is the solver-backed check on the analytical estimates made earlier in the design. The magnetics and thermal stages size a transformer and a heat sink with fast analytical models; this agent solves the actual fields in those geometries and reports how far the estimates hold. In the 10 kW DAB workflow it computes the leakage inductance of the selected transformer window in 2-D and the temperature of the selected heat sink in 3-D, each at two mesh levels; the workflow then reconciles the circuit model with the magnetics and field results.

| Interface | Content |
| --- | --- |
| Inputs | Model parameters in SI units (geometry, materials, currents, film coefficients); optionally an operating point from the Engineering State, or STEP geometry from the CAD Agent |
| Outputs | A case directory per solve with mesh, solver input, logs and fields, a summary of results and checks, and evidence records with tool versions and SHA-256 hashes |
| Hand-off | AIPE-Workflows records the results under its field-simulation gate and reconciles them with the circuit model; engineering review follows |

Results are verified against closed-form solutions and mesh refinement, not against measurements. The [agent interface](https://github.com/FulongLi/AIPE-Field-Simulation/blob/main/aipe.yaml) defines these inputs, outputs and limits.

## How the Agent Is Organised

A simulation passes through five stages, and each stage hands the next a solver-neutral artefact, so only the solver-execution stage is specific to Elmer. Models and benchmarks are solved on successively finer meshes, so the discretisation error is measured rather than assumed.

<figure class="project-blueprint">
  <a href="/images/research/aipe-field-simulation/agent-architecture.svg" target="_blank" rel="noopener"><img src="/images/research/aipe-field-simulation/agent-architecture.svg" alt="Flow chart of AIPE Field Simulation: model parameters and inputs from other AIPE stages feed geometry and meshing, materials and physics, and Elmer solver execution, followed by post-processing and verification with mesh refinement, then outputs and hand-off" width="760" height="668" loading="lazy"></a>
  <figcaption>Internal organisation of AIPE Field Simulation, from model parameters to verified and recorded field results.</figcaption>
</figure>

| Part | Responsibility |
| --- | --- |
| Geometry and meshing | Parametric Gmsh builders, or an imported STEP model, produce a mesh whose bodies and boundaries carry named groups. |
| Materials and physics | SI material records with sources, and a problem description (heat flux, convection, adiabatic faces, currents) that refers to boundary names rather than solver identifiers. |
| Solver execution | Locates and qualifies Gmsh, ElmerGrid and ElmerSolver, renders an explicit solver input file and runs the case with logs. |
| Post-processing and verification | Re-integrates the solved fields independently with numpy, checks energy balance and compares refinement levels; four benchmarks compare against closed-form solutions. |
| Outputs | A case directory with tool versions, commands and SHA-256 hashes, a summary of results and checks, figures, a report and AIPE evidence records. |

Four benchmarks prove the chain before any design model is trusted: a conduction slab, a coaxial magnetostatic conductor, a 100 kHz copper skin-effect slab and a 3-D fin, each within a fraction of a percent of its analytical solution at the finest mesh. The [architecture](https://github.com/FulongLi/AIPE-Field-Simulation/blob/main/docs/architecture.md) and [benchmarks](https://github.com/FulongLi/AIPE-Field-Simulation/blob/main/docs/validation.md) describe these stages in detail.

## Example: Heat Sink for Two TO-247 Devices

This example sizes the cooling for a pair of power devices: two TO-247 packages, each dissipating 20 W, on a finned aluminium heat sink cooled by natural convection. It asks four questions: how hot the mounting surface gets, where the hotspot is, what the sink-to-ambient thermal resistance is, and whether that number can be trusted numerically. One command runs the whole chain.

| Input | Value |
| --- | --- |
| Base (length × width × thickness) | 100 × 60 × 6 mm aluminium, k = 200 W/m·K |
| Fins | 8 straight fins, 2 mm thick, 25 mm tall |
| Heat sources | Two 16 × 21 mm TO-247 footprints, 20 W each (40 W total) |
| Cooling | Film coefficient 25 W/m²·K on every exposed face, 300 K ambient |
| Mesh | Three levels, maximum tetrahedron size 3, 2 and 1.4 mm |

### Geometry and Mesh

Gmsh builds the base, fins and the two imprinted device footprints, and names the boundary groups the physics refers to: the footprints where heat enters, the convective faces, and the uncovered base bottom, treated as adiabatic.

<figure class="project-blueprint">
  <a href="/images/research/aipe-field-simulation/heatsink-geometry-mesh.png" target="_blank" rel="noopener"><img src="/images/research/aipe-field-simulation/heatsink-geometry-mesh.png" alt="Gmsh surface mesh of the finned heat sink from the fin side and the mounting side, with the TO-247 footprints, convective faces and adiabatic bottom marked" width="1556" height="814" loading="lazy"></a>
  <figcaption>Heat-sink geometry and coarsest surface mesh, with the TO-247 footprints, convective faces and adiabatic bottom.</figcaption>
</figure>

### Temperature Field

On the finest mesh of 112,786 tetrahedra, the hotspot reaches **353.43 K, a 53.4 K rise** above ambient, with the two footprints averaging 352.74 K. The sink's thermal resistance is **1.336 K/W** from hotspot to ambient and 1.319 K/W from the mean footprint.

<figure class="project-blueprint">
  <a href="/images/research/aipe-field-simulation/heatsink-temperature.png" target="_blank" rel="noopener"><img src="/images/research/aipe-field-simulation/heatsink-temperature.png" alt="Surface temperature of the heat sink on the finest mesh, seen from the fin side and the mounting side, with hotspots at the two device footprints" width="1689" height="734" loading="lazy"></a>
  <figcaption>Surface temperature on the finest mesh; the hotspots sit at the centres of the two device footprints.</figcaption>
</figure>

The hotspots are only 0.7 K above the footprint mean, because each footprint spreads well into the 6 mm base. The whole surface spans about 7 K for a 53 K rise, and fin efficiency is 0.97: this design is limited by convection, not conduction. Raising the film coefficient with forced air, or adding area, lowers the temperature almost proportionally, while a thicker base or a better alloy would gain little.

### Verification

| Check | Result |
| --- | --- |
| Energy balance: heat leaving by convection equals the 40 W input | Error 9 × 10⁻¹⁶ |
| Independent re-integration of the solved field matches the solver | Error 3 × 10⁻¹² |
| The two symmetric devices see the same mean temperature | 1.8 × 10⁻⁵ of the rise |
| Hotspot rise between the two finest meshes | Changes by 0.07% (limit 2%) |
| Comparison with classical fin theory | FEM resistance 1.05 × the isothermal-base estimate, as expected from spreading |

<figure>
  <a href="/images/research/aipe-field-simulation/heatsink-mesh-convergence.png" target="_blank" rel="noopener"><img src="/images/research/aipe-field-simulation/heatsink-mesh-convergence.png" alt="Hotspot and mean footprint temperature against number of tetrahedra over three mesh levels, with the Richardson-extrapolated hotspot temperature" width="960" height="630" loading="lazy"></a>
  <figcaption>Mesh refinement: hotspot and mean footprint temperature over three mesh levels, with the Richardson-extrapolated hotspot temperature of 353.50 K.</figcaption>
</figure>

### Task Outputs

The task produced a case directory for each mesh level, with the mesh, solver input, logs and fields, together with a summary, figures and a report. The example runs on every push in continuous integration, and the published results come from such a run. The results are verified for internal consistency and discretisation error, not validated against measurements. The film coefficient is a typical natural-convection value supplied as an input, and is the dominant uncertainty; each device is modelled as a uniform heat flux, without its package or thermal interface.

[AIPE Overview](/research/aipe/) · [Source Code](https://github.com/FulongLi/AIPE-Field-Simulation) · [Back to Research](/research/)
