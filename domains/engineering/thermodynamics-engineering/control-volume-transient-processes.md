---
id: control-volume-transient-processes
title: Transient Processes in Control Volumes
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: control-volume-steady-flow
  type: hard
- id: first-law-open-systems
  type: hard
builds-toward:
- transient-filling-emptying-tanks
- exergy-balance-unsteady-flow
tags:
- transient
- unsteady-flow
- filling
- emptying
- control-volume
stage: advanced
status: draft
---

# Transient Processes in Control Volumes

## Core Idea
Transient processes in control volumes involve time-dependent mass and energy balances where system properties change with time. Applications include tank filling/emptying, vessel pressurization, and start-up transients in power systems. Energy balance requires dE_CV/dt = Q̇ - Ẇ + Σ(ṁ_in h_in) - Σ(ṁ_out h_out), accounting for accumulation terms.

## Explainer

Your prerequisite on steady-flow control volumes established the standard energy equation by setting the accumulation term to zero: mass and energy inside the control volume stay constant because inflow and outflow exactly balance. Transient analysis simply restores what was set to zero. Now the mass and energy stored inside the control volume are allowed to change with time, and you must track that accumulation explicitly.

The **transient mass balance** is dm_CV/dt = Σṁ_in − Σṁ_out. If more mass flows in than out, the control volume gains mass; if more flows out, it loses mass. The **transient energy balance** is dE_CV/dt = Q̇ − Ẇ + Σ(ṁ_in h_in) − Σ(ṁ_out h_out), where E_CV = m_CV u_CV is the stored internal energy (neglecting kinetic and potential energy for most tank problems). The structure is identical to what you know from the first law for open systems — you are just no longer forcing the left side to be zero.

The canonical application is a **filling tank**: a rigid vessel initially empty (or at some initial state) being supplied through one inlet port, with no outlet. Here, ṁ_out = 0 and Ẇ = 0 (rigid vessel, no shaft). Integrating the mass balance gives m₂ − m₁ = mᵢₙ (total mass that enters). Integrating the energy balance, and applying the **uniform-flow assumption** (inlet properties are constant throughout the fill), gives m₂u₂ − m₁u₁ = Q + mᵢₙhᵢₙ. This one algebraic equation, combined with the thermodynamic property relations for the working fluid, determines the final state. The final temperature inside a rigid adiabatic tank being filled from a supply line at constant enthalpy hₛ is higher than the supply temperature — internal energy rises faster than if you had simply filled it isothermally, because the incoming fluid does flow work pushing against the existing contents.

For **emptying problems**, the analysis reverses: the control volume loses mass and energy. Now you must track how the state of the remaining fluid evolves as the tank drains. The uniform-state assumption — the fluid inside the control volume is uniform at each instant, though its state changes over time — simplifies the integration. More complex problems (non-rigid vessels, multiple inlets and outlets, non-uniform internal states) require integrating the differential form numerically, but the governing equations remain the same two balance statements: conservation of mass and conservation of energy with accumulation terms retained.
