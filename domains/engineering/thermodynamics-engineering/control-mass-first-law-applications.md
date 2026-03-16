---
id: control-mass-first-law-applications
title: First Law for Control Mass Systems
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: first-law-closed-systems
  type: hard
- id: state-functions-path-functions
  type: soft
builds-toward:
- steady-flow-energy-equation-engineering
- entropy-balance-equations
- control-volume-transient-processes
tags:
- first-law
- closed-systems
- energy-balance
stage: advanced
status: draft
---

# First Law for Control Mass Systems

## Core Idea
For a control mass (closed system), the first law states dE/dt = Q̇ - Ẇ, relating the rate of energy change to heat transfer and work rates. Total energy E = U + KE + PE; applications include pistons, springs, and accumulators where mass is conserved but energy changes through boundary interactions. Process constraints (adiabatic, isothermal) simplify the equation.

## Explainer

You already know the first law for a closed system: energy is conserved, and any change in the system's energy equals net heat added minus net work done by the system. Now you apply that principle to concrete physical processes — pistons compressing gas, rigid tanks storing fluid, springs being loaded — and work through what the energy balance predicts in each case.

The general form is dE/dt = Q̇ − Ẇ, where total energy E = U + KE + PE. For most engineering control mass problems, the system itself isn't moving as a whole, so kinetic and potential energy of the system are negligible. The equation simplifies to dU = δQ − δW. The key skill is correctly identifying Q (heat crossing the system boundary, positive when entering) and W (work done by the system, positive when exiting). Sign conventions matter enormously here; always define them before writing the balance.

**Boundary work** is the work done by a piston face as it moves: W_boundary = ∫P dV. For a constant-pressure (isobaric) process, this simplifies to P ΔV. For a **constant-volume (isochoric) process** — a rigid tank, a bomb calorimeter — the piston doesn't move, so boundary work is zero and the first law becomes ΔU = Q. All heat input goes directly into raising internal energy. For an **adiabatic process**, no heat crosses the boundary (Q = 0), so any work done must draw down internal energy: ΔU = −W.

Each **process constraint** eliminates a term or fixes a relationship between state variables, making the energy balance tractable. For constant-pressure processes in particular, the first law can be rewritten in terms of **enthalpy** H = U + PV: ΔH = Q_P. This substitution absorbs the boundary work P ΔV into the state property H, making enthalpy the natural energy bookkeeping quantity for constant-pressure processes. This is why engineers track enthalpy — not internal energy — for most practical devices, and why property tables list both U and H values. Recognizing which process constraint applies before writing the energy balance is the central problem-solving discipline of this topic.
