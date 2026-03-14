---
id: inductance-circuits-rl-transients
title: Inductance and Transient Response in RL Circuits
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: lenz-law-induced-currents
  type: hard
- id: magnetic-torque-dipole
  type: soft
builds-toward:
- lorentz-force-complete-em
tags:
- inductance
- rl-circuit
- transient
stage: formal-systems
status: draft
---

# Inductance and Transient Response in RL Circuits

## Core Idea
Self-inductance L relates induced EMF to changing current: ε = −L dI/dt. RL circuit: I(t) = (ε/R)(1 − e^(−t/τ)) for charging, τ = L/R. Energy stored in inductor: U = ½LI². Inductance arises from magnetic flux linkage.
