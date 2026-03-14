---
id: rankine-cycle-steam-power
title: The Rankine Cycle and Steam Power Plants
domain: physics
course: thermodynamics
prerequisites:
- id: phase-transitions
  type: hard
- id: thermodynamic-processes
  type: hard
builds-toward:
- ts-diagram-entropy-temperature
- pv-diagram-interpretation
tags:
- cycles
- steam-power
- two-phase
stage: formal-systems
status: draft
---

# The Rankine Cycle and Steam Power Plants

## Core Idea
The Rankine cycle models steam power plants: isentropic compression of liquid water (pump), isobaric heat addition to produce steam (boiler), isentropic expansion through a turbine (power output), and isobaric heat rejection in the condenser. The Rankine efficiency is typically η = (W_net)/Q_in = (W_turbine - W_pump)/Q_boiler; real cycles have lower efficiency due to irreversibilities. Understanding the Rankine cycle is essential for power plant design and explains the two-phase behavior needed for efficient large-scale power generation.

## How It's Best Learned
Use steam tables to solve Rankine cycle problems. Plot cycles on T-S diagrams. Compare ideal (isentropic) with real (irreversible) turbines.

## Common Misconceptions
- Thinking the pump work is negligible (it is small compared to turbine work, but not zero).
- Assuming all expansion is isentropic (real turbines have non-zero entropy increase).
- Confusing the condenser temperature with ambient temperature (it can be higher due to pressure).
