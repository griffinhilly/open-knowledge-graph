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
stage: formal-systems
status: draft
---

# First Law for Control Mass Systems

## Core Idea
For a control mass (closed system), the first law states dE/dt = Q̇ - Ẇ, relating the rate of energy change to heat transfer and work rates. Total energy E = U + KE + PE; applications include pistons, springs, and accumulators where mass is conserved but energy changes through boundary interactions. Process constraints (adiabatic, isothermal) simplify the equation.

## Questions

```yaml
- question: "A rigid sealed tank contains steam. Heat is added until the steam's internal energy increases by 500 kJ. How much boundary work was done, and how much heat was added?"
  type: multiple-choice
  options:
    - "W = 500 kJ, Q = 1000 kJ — boundary work equals the heat required to maintain pressure"
    - "W = 0, Q = 500 kJ — a rigid tank has no volume change, so boundary work is zero and all heat input becomes internal energy change"
    - "W = 500 kJ, Q = 0 — the process is adiabatic so work must supply the internal energy"
    - "W = −500 kJ, Q = 0 — internal energy increases by work done on the system"
  answer: 1
  explanation: "For a rigid tank, the volume cannot change (ΔV = 0), so boundary work W = ∫P dV = 0. The first law for a closed system reduces to ΔU = Q − W = Q − 0 = Q. Therefore Q = ΔU = 500 kJ: all the heat added goes directly into increasing the internal energy of the steam. This is the isochoric (constant-volume) process — the simplest application of the first law because the work term vanishes completely."

- question: "A piston-cylinder device compresses a gas at constant pressure. An engineer wants to calculate the heat transferred during this compression. Which approach is most direct?"
  type: multiple-choice
  options:
    - "Use ΔU = Q − W, then separately calculate W = PΔV and subtract from ΔU to find Q"
    - "Use ΔH = Q_P directly — at constant pressure, the enthalpy change equals the heat transferred, automatically accounting for the boundary work"
    - "Set Q = 0 since compression processes are adiabatic by assumption"
    - "Use dE/dt = Q̇ − Ẇ with the rate form since piston problems require differential analysis"
  answer: 1
  explanation: "At constant pressure, the first law ΔU = Q − PΔV can be rearranged to Q = ΔU + PΔV = ΔH (since H = U + PV, so ΔH = ΔU + PΔV at constant pressure). This means the heat transferred in any constant-pressure process equals the change in enthalpy — no separate calculation of boundary work is needed. This is exactly why enthalpy is tabulated in property tables: it bundles internal energy and the PV work of expansion together into one state property, making constant-pressure energy balances a single lookup rather than a two-step calculation."

- question: "For a gas that expands adiabatically in a piston-cylinder device (no heat transfer), the internal energy of the gas decreases by exactly the amount of work done by the gas on the piston."
  type: true-false
  answer: true
  explanation: "For an adiabatic process Q = 0, so the first law ΔU = Q − W becomes ΔU = −W. The gas does positive work W on the piston (the gas pushes the piston outward), and its internal energy falls by exactly that amount. Energy is conserved: the gas's thermal energy converts to mechanical work. This is the operating principle of an adiabatic expansion turbine — the working fluid's internal energy decreases and that energy appears as shaft work output."

- question: "Enthalpy is useful for constant-pressure processes because it represents the total 'heat content' stored in a substance at any given state."
  type: true-false
  answer: false
  explanation: "Enthalpy H = U + PV is a state function, but calling it 'heat content' is a misconception — heat is a path function (energy in transit), not a property stored in a substance. Enthalpy is useful for constant-pressure processes for a specific reason: at constant pressure, ΔH = Q_P, meaning the change in enthalpy equals the heat transferred during a constant-pressure process. This identity absorbs the P ΔV boundary work into H, making the energy balance simpler. But outside of constant-pressure conditions, ΔH does not generally equal heat transferred, and enthalpy has no meaning as a 'stored heat.'"

- question: "Why do engineers typically use enthalpy rather than internal energy when analyzing constant-pressure processes, and what does the enthalpy function absorb that makes it convenient?"
  type: short-answer
  answer: "At constant pressure, the first law is ΔU = Q − PΔV, which requires tracking both internal energy change and the boundary work PΔV separately. Enthalpy is defined as H = U + PV, so ΔH = ΔU + Δ(PV) = ΔU + PΔV at constant pressure. Substituting into the first law gives ΔH = Q_P — the heat transferred at constant pressure equals simply the enthalpy change, with no need to calculate boundary work separately. Enthalpy absorbs the P ΔV expansion work into a single composite state property. This is why thermodynamic tables list H values: most practical engineering devices (boilers, condensers, turbines, nozzles at steady state) operate at approximately constant pressure, and tracking enthalpy reduces every energy balance to a single property difference."
  explanation: "The deeper point is that enthalpy is a convenient accounting fiction tailored to constant-pressure conditions. It is not physically more fundamental than internal energy — it is a bundle designed to simplify a specific class of calculations. Recognizing which process constraint applies (isochoric, isobaric, adiabatic) before writing the energy balance is the central problem-solving skill: the right choice of variables follows directly from the constraint."
```

## Explainer

You already know the first law for a closed system: energy is conserved, and any change in the system's energy equals net heat added minus net work done by the system. Now you apply that principle to concrete physical processes — pistons compressing gas, rigid tanks storing fluid, springs being loaded — and work through what the energy balance predicts in each case.

The general form is dE/dt = Q̇ − Ẇ, where total energy E = U + KE + PE. For most engineering control mass problems, the system itself isn't moving as a whole, so kinetic and potential energy of the system are negligible. The equation simplifies to dU = δQ − δW. The key skill is correctly identifying Q (heat crossing the system boundary, positive when entering) and W (work done by the system, positive when exiting). Sign conventions matter enormously here; always define them before writing the balance.

**Boundary work** is the work done by a piston face as it moves: W_boundary = ∫P dV. For a constant-pressure (isobaric) process, this simplifies to P ΔV. For a **constant-volume (isochoric) process** — a rigid tank, a bomb calorimeter — the piston doesn't move, so boundary work is zero and the first law becomes ΔU = Q. All heat input goes directly into raising internal energy. For an **adiabatic process**, no heat crosses the boundary (Q = 0), so any work done must draw down internal energy: ΔU = −W.

Each **process constraint** eliminates a term or fixes a relationship between state variables, making the energy balance tractable. For constant-pressure processes in particular, the first law can be rewritten in terms of **enthalpy** H = U + PV: ΔH = Q_P. This substitution absorbs the boundary work P ΔV into the state property H, making enthalpy the natural energy bookkeeping quantity for constant-pressure processes. This is why engineers track enthalpy — not internal energy — for most practical devices, and why property tables list both U and H values. Recognizing which process constraint applies before writing the energy balance is the central problem-solving discipline of this topic.
