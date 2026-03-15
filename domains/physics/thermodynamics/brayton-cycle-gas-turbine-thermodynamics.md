---
id: brayton-cycle-gas-turbine-thermodynamics
title: The Brayton Cycle and Gas Turbines
domain: physics
course: thermodynamics
prerequisites:
- id: thermodynamic-processes
  type: hard
- id: isobaric-and-isochoric-processes
  type: hard
builds-toward:
- pv-diagram-interpretation
- ts-diagram-entropy-temperature
tags:
- cycles
- turbines
- continuous-combustion
stage: formal-systems
status: draft
---

# The Brayton Cycle and Gas Turbines

## Core Idea
The Brayton cycle models gas turbines and jet engines: isentropic compression, isobaric (constant-pressure) heat addition in the combustion chamber, isentropic expansion through the turbine, and isobaric heat rejection. The thermal efficiency is η = 1 - 1/r_p^((γ-1)/γ), where r_p = P_2/P_1 is the pressure ratio; unlike the Otto cycle, Brayton efficiency depends on pressure ratio, not volume ratio. The Brayton cycle explains why turbojets operate efficiently at high altitudes and high speeds.

## How It's Best Learned
Sketch the Brayton cycle on both P-V and T-S diagrams. Derive the efficiency formula. Compare with Otto cycle efficiency behavior.

## Common Misconceptions
- Thinking the compression and expansion are isobaric (they are isentropic).
- Confusing pressure ratio with volume ratio.
- Assuming the Brayton cycle has constant efficiency (it improves with pressure ratio).
