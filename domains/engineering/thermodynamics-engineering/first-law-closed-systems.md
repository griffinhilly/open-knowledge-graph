---
id: first-law-closed-systems
title: First Law of Thermodynamics for Closed Systems
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: first-law-of-thermodynamics
  type: hard
- id: energy-conservation-mechanical-systems
  type: soft
- id: energy-conservation-applications
  type: hard
builds-toward:
- first-law-open-systems
- rankine-cycle-thermodynamic-analysis
- brayton-cycle-gas-turbine
- otto-cycle-spark-ignition-engine
- refrigeration-thermodynamic-analysis
- exergy-concept-availability
tags:
- first-law
- energy-balance
- closed-systems
stage: advanced
status: draft
---

# First Law of Thermodynamics for Closed Systems

## Core Idea
The first law for a closed system states that energy change equals heat added minus work done by the system: ΔU = Q - W. This energy balance applies to any system undergoing any process and is the foundation for analyzing turbines, compressors, and heat exchangers with fixed mass. Identifying all forms of work (boundary, shaft) and heat transfer is critical to correct application.

## How It's Best Learned
Write the first law ΔU = Q - W for various processes (isothermal, isobaric, isochoric) and identify which terms vanish. Practice calculating work for boundary-displacement processes (W = ∫P dV) and recognize that polytropic processes (PVⁿ = const) are common idealizations. Always draw the system boundary clearly and identify work and heat at the boundary.

## Common Misconceptions
- The first law applies only to reversible processes; it applies to all processes.
- Work is always done by expanding gases and against compressing fluids; work can be done on a gas by compression or by a gas through expansion or shaft rotation.
- ΔU depends on the path taken; internal energy is a state function and depends only on initial and final states.
