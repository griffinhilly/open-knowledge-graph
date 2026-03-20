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
stage: advanced
status: draft
---

# Energy Equation for Steady Flow

## Core Idea
The steady-flow energy equation (also called the extended Bernoulli equation) accounts for heat transfer and work: H₁ + Q − W_s = H₂, where H is total enthalpy, Q is heat added, and W_s is shaft work. This forms the basis for analyzing pumps, turbines, and thermal energy balance in piping systems.

## Explainer

You already know Bernoulli's equation: for steady, inviscid, incompressible flow along a streamline, the sum of pressure energy, kinetic energy, and potential energy per unit volume is constant. That equation works beautifully for nozzles and pipes with no machinery — but it breaks down the moment something adds or removes energy from the fluid. The **steady-flow energy equation** generalizes Bernoulli by tracking every energy interaction crossing the control volume boundary: heat transfer Q in and shaft work W_s out.

The accounting is straightforward once you see the structure. Fluid entering the control volume carries **total enthalpy** H = h + V²/2 + gz, where h is specific enthalpy (internal energy plus flow work pv), V²/2 is kinetic energy, and gz is gravitational potential energy. Heat Q added to the fluid increases its energy; shaft work W_s done by the fluid on rotating machinery (a turbine) removes energy. The energy balance for steady flow then reads: H₁ + Q − W_s = H₂. For an incompressible fluid with no heat transfer, this collapses back to Bernoulli plus a work term — the familiar pump or turbine head equation: (p₁/ρg + V₁²/2g + z₁) + h_pump − h_turbine = p₂/ρg + V₂²/2g + z₂.

The sign convention matters enormously in practice. For a **pump**, mechanical work is added *to* the fluid, so W_s is negative in the convention above (or equivalently, you subtract h_pump with a negative sign, or add it positively depending on how you define W_s direction). For a **turbine**, the fluid does work on the shaft, so W_s is positive and the downstream enthalpy is lower. A useful check: energy must increase when a pump is present (downstream head > upstream head) and decrease when a turbine is present. If your calculation gives the opposite, you've likely flipped a sign.

The equation is the master tool for analyzing any steady-flow thermal-fluid device. For a pump in an incompressible system with no heat transfer, it gives the hydraulic head added to the fluid — directly comparable to pump curve data. For a steam turbine, it connects inlet steam conditions (high temperature and pressure, high h₁) to outlet conditions and extracted shaft work. For a heat exchanger with no work, it reduces to h₁ + Q = h₂, directly tracking how much heat crosses the boundary. Mastering the energy equation means learning to strip away the terms that are zero or negligible in a given physical situation, leaving the minimal equation needed to solve the problem.


