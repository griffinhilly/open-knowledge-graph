---
id: energy-equation-steady-flow
title: Energy Equation for Steady Flow
domain: engineering
course: fluid-mechanics
prerequisites:
- id: bernoullis-equation
  type: hard
- id: control-volume-mass-balance
  type: soft
builds-toward:
- mechanical-energy-head-forms
- pipe-flow-network-analysis
tags:
- energy
- conservation
- steady-flow
stage: formal-systems
status: validated
---

# Energy Equation for Steady Flow

## Core Idea
The steady-flow energy equation (also called the extended Bernoulli equation) accounts for heat transfer and work: H₁ + Q − W_s = H₂, where H is total enthalpy, Q is heat added, and W_s is shaft work. This forms the basis for analyzing pumps, turbines, and thermal energy balance in piping systems.

## Questions

```yaml
- question: "Water flows through a pump that adds 50 J/kg of shaft work. There is no heat transfer. Which equation correctly applies to find outlet conditions?"
  type: multiple-choice
  options:
    - "Bernoulli's equation: p₁/ρg + V₁²/2g + z₁ = p₂/ρg + V₂²/2g + z₂"
    - "The extended Bernoulli equation: p₁/ρg + V₁²/2g + z₁ + h_pump = p₂/ρg + V₂²/2g + z₂"
    - "The heat-transfer form of the energy equation: H₁ + Q = H₂"
    - "Bernoulli's equation is sufficient — shaft work does not affect incompressible flow"
  answer: 1
  explanation: "Bernoulli's equation applies only when there is no energy addition or removal — no pumps, turbines, or heat transfer. When a pump adds shaft work, you must use the extended form that includes the pump head h_pump as an addition on the inlet side. Option D is wrong: pumps absolutely affect incompressible flow, and ignoring shaft work gives incorrect results. Option C handles heat transfer, which is not the relevant term here (Q = 0). The extended Bernoulli is the correct tool for pump or turbine problems with incompressible flow."

- question: "A steam turbine receives high-pressure steam at station 1 and exhausts lower-pressure steam at station 2. It produces shaft work W_s > 0. There is no heat transfer. Which energy balance is correct?"
  type: multiple-choice
  options:
    - "H₁ = H₂ — enthalpy is conserved in steady flow through any device"
    - "H₁ − W_s = H₂ — inlet enthalpy minus shaft work extracted equals outlet enthalpy"
    - "H₁ + W_s = H₂ — shaft work adds to the fluid's energy at the outlet"
    - "H₁ = H₂ + Q — a heat rejection term explains the enthalpy drop"
  answer: 1
  explanation: "The steady-flow energy equation is H₁ + Q − W_s = H₂. For a turbine with Q = 0 and positive shaft output W_s > 0, this gives H₁ − W_s = H₂. Outlet enthalpy is lower because the fluid has done work on the turbine shaft, transferring energy out. Option A (H₁ = H₂) would mean zero shaft work — contradicting the turbine operation. Option C has the sign wrong: shaft work out reduces the fluid's energy, not increases it. A quick check: energy must decrease when a turbine is present."

- question: "Bernoulli's equation is a special case of the steady-flow energy equation that applies when shaft work and heat transfer are both zero."
  type: true-false
  answer: true
  explanation: "This is precisely the relationship between the two equations. The steady-flow energy equation H₁ + Q − W_s = H₂ reduces to Bernoulli's equation when Q = 0 (no heat transfer) and W_s = 0 (no shaft work), and for incompressible flow where enthalpy differences reduce to pressure, velocity, and elevation terms. Bernoulli is not a separate law — it is the mechanical-energy-only special case of the general energy balance. Recognizing this hierarchy helps you choose which equation to apply."

- question: "For a pump in a piping system, the steady-flow energy equation guarantees that fluid pressure must increase between inlet and outlet."
  type: true-false
  answer: false
  explanation: "A pump adds total head — the sum of pressure head, velocity head, and elevation head — not necessarily pressure alone. If the pump lifts water to a significantly higher elevation, much of the added energy goes into potential energy, and outlet pressure could actually be lower than inlet pressure. The energy equation correctly accounts for all energy forms. You cannot infer that pressure alone must increase just because a pump is present; you must account for all terms on both sides of the equation."

- question: "What does the steady-flow energy equation add that Bernoulli's equation lacks, and why does this matter for analyzing real engineering systems like pumps and turbines?"
  type: short-answer
  answer: "The steady-flow energy equation adds terms for shaft work (energy added by pumps or extracted by turbines) and heat transfer across the control volume boundary. Bernoulli only accounts for mechanical energy of the flowing fluid. Real systems almost always involve one or both of these interactions — a pump adds energy, a turbine extracts it, a heat exchanger transfers thermal energy. Without the shaft work term, you cannot compute how much pressure a pump adds or how much power a turbine produces."
  explanation: "In practice, the skill is recognizing which terms are zero for a given system and reducing to the appropriate simplified form. No heat transfer and no rotating machinery → Bernoulli. Pump present, incompressible, no heat → extended Bernoulli with pump head. Compressible fluid (steam) and turbine → full enthalpy formulation. Mastering the energy equation means learning to strip away irrelevant terms while keeping every term that matters for the specific device being analyzed."
```

## Explainer

You already know Bernoulli's equation: for steady, inviscid, incompressible flow along a streamline, the sum of pressure energy, kinetic energy, and potential energy per unit volume is constant. That equation works beautifully for nozzles and pipes with no machinery — but it breaks down the moment something adds or removes energy from the fluid. The **steady-flow energy equation** generalizes Bernoulli by tracking every energy interaction crossing the control volume boundary: heat transfer Q in and shaft work W_s out.

The accounting is straightforward once you see the structure. Fluid entering the control volume carries **total enthalpy** H = h + V²/2 + gz, where h is specific enthalpy (internal energy plus flow work pv), V²/2 is kinetic energy, and gz is gravitational potential energy. Heat Q added to the fluid increases its energy; shaft work W_s done by the fluid on rotating machinery (a turbine) removes energy. The energy balance for steady flow then reads: H₁ + Q − W_s = H₂. For an incompressible fluid with no heat transfer, this collapses back to Bernoulli plus a work term — the familiar pump or turbine head equation: (p₁/ρg + V₁²/2g + z₁) + h_pump − h_turbine = p₂/ρg + V₂²/2g + z₂.

The sign convention matters enormously in practice. For a **pump**, mechanical work is added *to* the fluid, so W_s is negative in the convention above (or equivalently, you subtract h_pump with a negative sign, or add it positively depending on how you define W_s direction). For a **turbine**, the fluid does work on the shaft, so W_s is positive and the downstream enthalpy is lower. A useful check: energy must increase when a pump is present (downstream head > upstream head) and decrease when a turbine is present. If your calculation gives the opposite, you've likely flipped a sign.

The equation is the master tool for analyzing any steady-flow thermal-fluid device. For a pump in an incompressible system with no heat transfer, it gives the hydraulic head added to the fluid — directly comparable to pump curve data. For a steam turbine, it connects inlet steam conditions (high temperature and pressure, high h₁) to outlet conditions and extracted shaft work. For a heat exchanger with no work, it reduces to h₁ + Q = h₂, directly tracking how much heat crosses the boundary. Mastering the energy equation means learning to strip away the terms that are zero or negligible in a given physical situation, leaving the minimal equation needed to solve the problem.


