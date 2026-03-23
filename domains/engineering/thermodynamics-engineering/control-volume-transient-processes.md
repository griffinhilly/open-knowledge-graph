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
stage: formal-systems
status: draft
---

# Transient Processes in Control Volumes

## Core Idea
Transient processes in control volumes involve time-dependent mass and energy balances where system properties change with time. Applications include tank filling/emptying, vessel pressurization, and start-up transients in power systems. Energy balance requires dE_CV/dt = Q̇ - Ẇ + Σ(ṁ_in h_in) - Σ(ṁ_out h_out), accounting for accumulation terms.

## Questions

```yaml
- question: "A rigid, well-insulated tank is initially evacuated and then filled from a supply line at constant temperature T_s and constant enthalpy h_s. After filling to supply pressure, the final temperature T₂ inside the tank will be:"
  type: multiple-choice
  options:
    - "Equal to T_s — no heat transfer means no temperature change from supply conditions"
    - "Less than T_s — the gas expands into the evacuated space and cools"
    - "Greater than T_s — the incoming flow carries enthalpy h_s = u_s + P_sv_s, and the Pv flow work term converts to internal energy, raising the temperature above the supply temperature"
    - "Equal to T_s only for ideal gases; real gases may be higher or lower depending on their equation of state"
  answer: 2
  explanation: "Applying the integrated energy balance m₂u₂ = m_in h_in (with m₁=0, Q=0, W=0): u₂ = h_in = u_in + P_in v_in. The final specific internal energy equals the inlet enthalpy, which exceeds the inlet internal energy by the flow work term P_in v_in. This means the gas inside the tank has higher internal energy (and therefore higher temperature) than the supply gas. For an ideal gas with constant specific heats, T₂ = k·T_s (where k = c_p/c_v), always greater than T_s. The physical explanation: incoming gas pushes against existing contents, converting the flow work into thermal energy."

- question: "For a control volume filling process with one inlet, no outlet, no heat transfer, and no shaft work, which energy balance is correct?"
  type: multiple-choice
  options:
    - "d(m_CV u_CV)/dt = ṁ_in · u_in — internal energy per unit mass enters since the tank is rigid and no boundary work occurs"
    - "d(m_CV u_CV)/dt = ṁ_in · h_in — enthalpy enters across the boundary because flowing mass carries both internal energy and flow work"
    - "dU_CV/dt = Q̇ − Ẇ, with the mass flow terms omitted since the boundary is fixed"
    - "m₂u₂ − m₁u₁ = m_in · (u_in + ½V²) — kinetic energy of the incoming flow must always be included"
  answer: 1
  explanation: "Mass crossing a control volume boundary carries enthalpy h = u + Pv, not just internal energy u. The Pv term is flow work — the work done by upstream fluid pushing the mass into the control volume. Omitting this term (using u instead of h) is a common error that gives a wrong final temperature for filling problems. The correct energy balance is d(m_CV u_CV)/dt = ṁ_in h_in. The rigid-vessel constraint means Ẇ_boundary = 0, but the incoming flow work is not boundary work — it is transported with the mass as part of enthalpy."

- question: "The transient energy balance for a control volume reduces exactly to the steady-state open system energy equation when the accumulation term dE_CV/dt is set to zero."
  type: true-false
  answer: true
  explanation: "The general transient energy balance is dE_CV/dt = Q̇ − Ẇ + Σ(ṁ_in h_in) − Σ(ṁ_out h_out). Setting dE_CV/dt = 0 (no accumulation) and dm_CV/dt = 0 (steady mass) recovers the familiar steady-state open system energy equation: 0 = Q̇ − Ẇ + Σ(ṁ_in h_in) − Σ(ṁ_out h_out). Steady-state analysis is simply the special case where all time derivatives vanish. Transient analysis is the general case — steady-state is not a separate theory but a simplification of it."

- question: "Under the uniform-flow assumption for a transient filling problem, the inlet enthalpy is allowed to vary with time to reflect changes in the supply line conditions during filling."
  type: true-false
  answer: false
  explanation: "The uniform-flow assumption means the inlet conditions are held CONSTANT throughout the filling process — the enthalpy h_in at the inlet does not change with time. This allows the time integral of ṁ_in h_in to simplify to h_in · m_in (total mass that entered times constant inlet enthalpy), converting the differential equation into a single algebraic equation. If inlet conditions varied with time, the integral ∫ṁ_in h_in dt would require knowing the time history of both ṁ and h_in, making the problem significantly more complex."

- question: "In a transient energy balance for a control volume, explain why mass crossing the boundary carries enthalpy h rather than internal energy u."
  type: short-answer
  answer: "When mass flows across a control volume boundary, the upstream fluid must push it into the control volume against the existing pressure — this is called flow work, and it equals Pv per unit mass (pressure times specific volume). The total energy transported per unit mass is therefore u + Pv = h, which is the definition of specific enthalpy. Using only u would ignore this flow work contribution. For a filling tank, this matters: the incoming flow does work on the gas already inside, transferring additional energy beyond what the internal energy of the supply gas alone would suggest. This is why the final temperature of an adiabatically filled rigid tank exceeds the supply temperature."
  explanation: "This is the thermodynamic reason enthalpy appears in all open system analyses — it is not an arbitrary bookkeeping choice but a consequence of the work required to push fluid across boundaries. The same logic explains why enthalpy is the relevant energy quantity in turbines, compressors, nozzles, and heat exchangers: in all of these, mass crosses system boundaries and must do flow work in the process."
```

## Explainer

Your prerequisite on steady-flow control volumes established the standard energy equation by setting the accumulation term to zero: mass and energy inside the control volume stay constant because inflow and outflow exactly balance. Transient analysis simply restores what was set to zero. Now the mass and energy stored inside the control volume are allowed to change with time, and you must track that accumulation explicitly.

The **transient mass balance** is dm_CV/dt = Σṁ_in − Σṁ_out. If more mass flows in than out, the control volume gains mass; if more flows out, it loses mass. The **transient energy balance** is dE_CV/dt = Q̇ − Ẇ + Σ(ṁ_in h_in) − Σ(ṁ_out h_out), where E_CV = m_CV u_CV is the stored internal energy (neglecting kinetic and potential energy for most tank problems). The structure is identical to what you know from the first law for open systems — you are just no longer forcing the left side to be zero.

The canonical application is a **filling tank**: a rigid vessel initially empty (or at some initial state) being supplied through one inlet port, with no outlet. Here, ṁ_out = 0 and Ẇ = 0 (rigid vessel, no shaft). Integrating the mass balance gives m₂ − m₁ = mᵢₙ (total mass that enters). Integrating the energy balance, and applying the **uniform-flow assumption** (inlet properties are constant throughout the fill), gives m₂u₂ − m₁u₁ = Q + mᵢₙhᵢₙ. This one algebraic equation, combined with the thermodynamic property relations for the working fluid, determines the final state. The final temperature inside a rigid adiabatic tank being filled from a supply line at constant enthalpy hₛ is higher than the supply temperature — internal energy rises faster than if you had simply filled it isothermally, because the incoming fluid does flow work pushing against the existing contents.

For **emptying problems**, the analysis reverses: the control volume loses mass and energy. Now you must track how the state of the remaining fluid evolves as the tank drains. The uniform-state assumption — the fluid inside the control volume is uniform at each instant, though its state changes over time — simplifies the integration. More complex problems (non-rigid vessels, multiple inlets and outlets, non-uniform internal states) require integrating the differential form numerically, but the governing equations remain the same two balance statements: conservation of mass and conservation of energy with accumulation terms retained.
