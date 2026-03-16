---
id: state-variables-and-functions
title: State Variables and Functions
domain: physics
course: thermodynamics
prerequisites:
- id: thermodynamic-processes
  type: hard
builds-toward:
- path-functions-vs-state-functions
- exact-and-inexact-differentials
- maxwell-relations-thermodynamics
tags:
- properties
- functions
- path-independence
stage: formal-systems
status: draft
---

# State Variables and Functions

## Core Idea
State variables (or state functions) are properties that depend only on the current state of a system, not on how it reached that state—examples include temperature, pressure, volume, and entropy. They uniquely determine the thermodynamic state of a system and can be written as mathematical functions of other state variables. The existence of state functions is what allows thermodynamics to be a predictive science despite path-dependent processes.

## How It's Best Learned
Compare paths between two states: different heating/cooling paths that yield the same ΔU or ΔS, versus paths that give different Q or W. Plot processes on P-V diagrams.

## Common Misconceptions
- Thinking heat and work are state functions because they contribute to internal energy.
- Confusing the symbol U (state function) with Q or W (path functions).
- Assuming all thermodynamic properties are state functions.

## Explainer

From your study of thermodynamic processes, you learned to describe what happens to a gas along specific paths: isothermal, adiabatic, isobaric, and isochoric. Each process traces a different curve on the P-V diagram between two states. Now step back from the paths and ask: what is special about the endpoints themselves? Two states are connected by infinitely many different paths — you could heat the gas at constant pressure, then cool it at constant volume to reach the same final (P, V, T). The heat transferred Q and work done W differ along each path. But the internal energy change ΔU = Q − W is the same regardless of path. Internal energy U is a **state function** — it depends only on which state the system is in, not on the history of how it got there.

A state function can always be written as a function of other state variables: U = U(T, V) for an ideal gas, or more generally U = U(T, V, n, …). The defining mathematical property is that its differential dU is **exact** — the integral ∫dU between two states gives the same result no matter which path you integrate along. Geometrically, if you return to the original state by any closed path, the net change is zero: ∮dU = 0. Temperature T, pressure P, volume V, entropy S, enthalpy H = U + PV, and Gibbs free energy G = H − TS are all state functions with this property. You can tabulate their values at each equilibrium state and use those tabulated values for any process, without caring how the system arrived at that state.

Contrast this with **path functions** Q (heat) and W (work). These are not properties of a state; they are properties of a process. You cannot say "the heat content of a gas at 300 K and 1 atm is X joules" — the gas has no stored Q. You can only say "during this particular process, Q joules flowed in." To see why this matters, consider two routes from state A to state B: isothermal expansion versus adiabatic expansion followed by isochoric heating. Each route has a different Q and a different W, but the same ΔU (first law). The function dQ is **inexact** — the integral ∫dQ depends on the path. Mathematically, inexact differentials are written with a bar through the d (đQ, đW) to signal they are not proper differentials of any function.

The practical power of state functions is enormous. Because ΔU, ΔH, and ΔS depend only on initial and final states, you can calculate them via any convenient hypothetical path — even one that would be physically unrealizable — as long as both endpoints are equilibrium states. This is the basis of Hess's law in chemistry (enthalpy of reaction is path-independent), of entropy calculations along reversible paths (even for irreversible processes), and of the entire framework of thermodynamic potentials. The existence of state functions is not obvious — it is a consequence of the First and Second Laws. The First Law guarantees U is a state function. The Second Law guarantees S is a state function. Without them, thermodynamics would be unable to make predictions about any process without tracking every intermediate step.
