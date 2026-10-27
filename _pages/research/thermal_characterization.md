---
layout: research
research_area: components
parent:
  title: "Device characterisation"
  url: /research/switching_devices/
title: "Thermal Characterisation"
permalink: /research/thermal-characterization/
excerpt: "Transient thermal-impedance measurement and junction-to-case thermal resistance of power devices and modules."
---

## Engineering problem

Junction temperature limits both the current rating and the lifetime of a power device, but it cannot be measured directly in a packaged part. The thermal path from junction to coolant also includes interfaces such as thermal grease whose resistance varies with mounting. Converter models therefore need a measured thermal network rather than a single datasheet value.

## Objective and scope

Measure transient thermal impedance *Z*<sub>th</sub>(*t*) and junction-to-case thermal resistance *R*<sub>th,jc</sub> of discrete devices and power modules, and express the result as an RC network that a converter-level thermal simulation can use. This work formed part of the characterisation rig I commissioned at CSA Catapult and was used in the P3EP project and in the [device-modelling project](/research/mosfet_ann_modelling/).

## My contribution

I operated the thermal test equipment and carried out the thermal-impedance measurements: calibration, heating and cooling tests, and evaluation of the results.

## Method

1. **Temperature-sensitive electrical parameter (TSEP).** A forward voltage at a small, fixed sensing current is calibrated against temperature on a temperature-controlled fixture. The sensing current is a compromise: too low gives a noisy signal, too high self-heats the device.
2. **Heating and cooling transient.** A heating current is applied until the device reaches thermal equilibrium, then switched to the sensing current while the cooling transient is recorded. Through the calibration, the voltage transient becomes a junction-temperature transient, and
   <span class="equation" style="display:block"><em>Z</em><sub>th</sub>(<em>t</em>) = Δ<em>T</em><sub>j</sub>(<em>t</em>) / <em>P</em></span>
   where *P* is the heating power.
3. **Junction-to-case boundary.** The case-to-heatsink interface is changed between two otherwise identical tests, dry and with thermal grease. The structure functions of the two tests coincide along the shared junction-to-case path and separate at the interface; the separation point gives *R*<sub>th,jc</sub>. This is the transient dual-interface method standardised in JEDEC JESD51-14.
4. **Thermal network.** The structure function is discretised into a Cauer RC ladder for use in circuit-level thermal simulation.

## Results and evidence

The measurements produced calibrated cooling transients, transient thermal-impedance curves, junction-to-case resistances and Cauer networks for the devices tested. The results and the laboratory training material that documents the procedure are internal and are not reproduced here.

## Limitations

- The extracted *R*<sub>th,jc</sub> depends on the evaluation method; structure-function and derivative-based evaluations of the same data can differ, so a quoted value should state its method.
- A junction-to-heatsink result includes the mounting and interface used in the test and does not transfer directly to a different cooling arrangement.

## Related pages

[Electrical characterisation](/research/electrical-characterization/) · [Reliability testing](/research/reliability_testing/) · [ANN-based device modelling](/research/mosfet_ann_modelling/)
