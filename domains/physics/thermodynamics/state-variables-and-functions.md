---
id: state-variables-and-functions
title: State Variables and Functions
domain: physics
course: thermodynamics
prerequisites:
- id: thermodynamic-processes
  type: hard
- id: intensive-and-extensive-properties
  type: soft
builds-toward:
- path-functions-vs-state-functions
- exact-and-inexact-differentials
- maxwell-relations-thermodynamics
tags:
- properties
- functions
- path-independence
stage: formal-systems
status: validated
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

## Questions

```yaml
- question: "A gas is taken from state A to state B via two different paths: path 1 is an isothermal expansion; path 2 is an adiabatic expansion followed by isochoric (constant-volume) heating. Which quantities are necessarily equal for both paths?"
  type: multiple-choice
  options:
    - "Q and W — both are determined only by the endpoints"
    - "ΔU only — internal energy depends only on the initial and final states"
    - "Q only — heat exchanged is path-independent"
    - "ΔU, Q, and W — all thermodynamic quantities are path-independent"
  answer: 1
  explanation: "Internal energy U is a state function: ΔU depends only on the initial and final states, not on the path taken between them. Heat Q and work W, however, are path functions — they differ depending on how the process proceeds. The First Law (ΔU = Q − W) guarantees that even though Q and W are different along each path, their difference ΔU is the same. This is exactly what distinguishes state functions from path functions."

- question: "Which of the following is NOT a state function?"
  type: multiple-choice
  options:
    - "Entropy (S)"
    - "Work done during an isothermal expansion (W)"
    - "Enthalpy (H = U + PV)"
    - "Temperature (T)"
  answer: 1
  explanation: "Work W is a path function, not a state function. The work done during an isothermal expansion depends on the specific path (e.g., reversible expansion vs. expansion against a fixed external pressure gives different W). You cannot say 'the work content of this gas' because work has no definite value at a state — only during a process. Entropy, enthalpy, and temperature are all state functions: their values are uniquely determined by the equilibrium state of the system."

- question: "Heat Q is a state function because it contributes to the internal energy of a system through the First Law ΔU = Q − W."
  type: true-false
  answer: false
  explanation: "This is the most common misconception about state functions. Q contributing to ΔU does not make Q a state function — it makes ΔU a state function (specifically, it means ΔU = Q − W where the difference Q − W is path-independent even though Q and W individually are not). Heat is a process quantity: it describes energy transfer during a process, not a property stored in a state. A system does not 'have' a certain amount of heat; it has internal energy, temperature, and entropy — all state functions."

- question: "Because entropy is a state function, you can calculate ΔS for an irreversible process by constructing a reversible path between the same endpoints and integrating dS along that path."
  type: true-false
  answer: true
  explanation: "This is the practical power of state functions. For an irreversible process, dS = đQ_rev/T cannot be directly applied (since the process isn't reversible). But because S is a state function, ΔS depends only on the endpoints. You are free to choose any convenient path between those endpoints — including a hypothetical reversible path — and integrate dS = dQ_rev/T along it. The result is the same ΔS regardless of which actual irreversible path occurred. This technique underlies most entropy calculations in thermodynamics."

- question: "Explain why heat (Q) is a path function rather than a state function, and describe what practical consequence this distinction has for thermodynamic calculations."
  type: short-answer
  answer: "Heat is a path function because it measures energy transfer across the system boundary during a specific process — it is not a property stored in the system at a state. Two processes connecting the same initial and final states can involve completely different amounts of heat (and work), as long as their difference Q − W = ΔU is the same. The practical consequence: you cannot look up Q in a table for a given state, and you cannot calculate Q for an irreversible process using only state variables at the endpoints. You must know the specific path. In contrast, state functions like ΔU and ΔH can be calculated via any convenient hypothetical path — even physically unrealizable ones — making them far easier to tabulate and use in calculations."
  explanation: "This distinction underlies Hess's law, entropy calculations, and the entire framework of thermodynamic potentials. State functions are powerful precisely because they free you from tracking every step of a process — you only need the endpoints. Path functions require process-level information, making them harder to use for predictive calculations."
```

## Explainer

From your study of thermodynamic processes, you learned to describe what happens to a gas along specific paths: isothermal, adiabatic, isobaric, and isochoric. Each process traces a different curve on the P-V diagram between two states. Now step back from the paths and ask: what is special about the endpoints themselves? Two states are connected by infinitely many different paths — you could heat the gas at constant pressure, then cool it at constant volume to reach the same final (P, V, T). The heat transferred Q and work done W differ along each path. But the internal energy change ΔU = Q − W is the same regardless of path. Internal energy U is a **state function** — it depends only on which state the system is in, not on the history of how it got there.

A state function can always be written as a function of other state variables: U = U(T, V) for an ideal gas, or more generally U = U(T, V, n, …). The defining mathematical property is that its differential dU is **exact** — the integral ∫dU between two states gives the same result no matter which path you integrate along. Geometrically, if you return to the original state by any closed path, the net change is zero: ∮dU = 0. Temperature T, pressure P, volume V, entropy S, enthalpy H = U + PV, and Gibbs free energy G = H − TS are all state functions with this property. You can tabulate their values at each equilibrium state and use those tabulated values for any process, without caring how the system arrived at that state.

Contrast this with **path functions** Q (heat) and W (work). These are not properties of a state; they are properties of a process. You cannot say "the heat content of a gas at 300 K and 1 atm is X joules" — the gas has no stored Q. You can only say "during this particular process, Q joules flowed in." To see why this matters, consider two routes from state A to state B: isothermal expansion versus adiabatic expansion followed by isochoric heating. Each route has a different Q and a different W, but the same ΔU (first law). The function dQ is **inexact** — the integral ∫dQ depends on the path. Mathematically, inexact differentials are written with a bar through the d (đQ, đW) to signal they are not proper differentials of any function.

The practical power of state functions is enormous. Because ΔU, ΔH, and ΔS depend only on initial and final states, you can calculate them via any convenient hypothetical path — even one that would be physically unrealizable — as long as both endpoints are equilibrium states. This is the basis of Hess's law in chemistry (enthalpy of reaction is path-independent), of entropy calculations along reversible paths (even for irreversible processes), and of the entire framework of thermodynamic potentials. The existence of state functions is not obvious — it is a consequence of the First and Second Laws. The First Law guarantees U is a state function. The Second Law guarantees S is a state function. Without them, thermodynamics would be unable to make predictions about any process without tracking every intermediate step.
