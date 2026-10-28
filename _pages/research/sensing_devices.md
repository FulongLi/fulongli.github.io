---
layout: single
title: "Current Sensing"
permalink: /research/sensing_devices/
author_profile: true
excerpt: "Compact PCB-integrated current sensors for fast-switching power converters: a PCB Rogowski coil and an embedded-core PCB current transformer."
---

Fast-switching SiC converters need current sensors that are compact, fit close to the power devices and respond quickly enough to capture switching transients. I developed two PCB-integrated sensors that balance bandwidth, sensitivity, isolation and manufacturability in different ways.

## PCB Rogowski Coil (PCB-RC)

An air-cored PCB winding senses the rate of change of current, and an on-board integrator recovers the current signal. With no core to saturate, it suits large, fast transients. I designed the coil layouts and signal-conditioning circuits, then compared the sensing chain with a commercial Rogowski coil.

[Read the PCB Rogowski coil project](/research/pcb-rogowski-coil/)

## Embedded-Core PCB Current Transformer (PCB-CT)

A ferrite core embedded between PCB layers, with a secondary winding formed by traces and vias, delivers a scaled secondary current without an integrator. I designed the winding layout and design calculations, and assessed the prototype for sensing performance and manufacturability.

[Read the PCB current transformer project](/research/pcb-current-transformer/)

[Power Device Characterization](/research/switching_devices/) · [Back to Research](/research/)
