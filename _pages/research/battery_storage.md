---
layout: single
title: "Battery Energy Storage Systems"
permalink: /research/battery_storage/
author_profile: true
excerpt: "Battery coordination in DC microgrids, from plug-and-play power sharing to degradation-aware energy scheduling."
---

My battery storage research connects converter-level coordination with system-level scheduling: sharing power between storage modules, and deciding how to use them while accounting for battery lifetime.

## Batteries in DC Microgrids

In a DC microgrid, batteries balance generation and demand and can regulate the bus voltage. Several battery modules are often connected in parallel through their own converters, so their currents must be shared fairly and new modules should connect without reconfiguring the system. At system level, every charge and discharge cycle also wears the battery, so an energy schedule that ignores degradation can trade short-term savings for a shorter battery life.

## Converter-Level Control

<h3 id="battery-power-sharing-and-plug-and-play-storage">Power Sharing and Plug-and-Play Storage</h3>

I developed control methods for coordinating modular batteries in DC microgrids: a multifunctional plug-and-play control scheme, and a reconstructed droop control that achieves current sharing between peer battery converters. These build on my [bidirectional battery interface converters](/research/nonisolated_converters/#bidirectional-buck-boost-converter) and the [hierarchical DC microgrid framework](/research/dcmg/).

[Multifunctional plug-and-play control](https://ieeexplore.ieee.org/document/9152414) · [Reconstructed droop control for peer current sharing](https://ieeexplore.ieee.org/document/9504641)

## System-Level Energy Management

<h3 id="battery-degradation-modelling-and-energy-management-optimisation">Battery Degradation and Scheduling</h3>

At the University of Waterloo, I modelled battery degradation within a GAMS-based energy management optimisation for DC microgrids, bringing battery use and its degradation cost into the scheduling problem.

[Read the battery-degradation EMS](/research/mgapp/battery-degradation-ems/) · [IEEE PESGM 2020 paper](https://ieeexplore.ieee.org/document/9281580)

[Energy Management Systems](/research/ems/) · [Experimental Platforms](/research/experimental_platforms/) · [Back to Research](/research/)
