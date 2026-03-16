---
id: path-functions-vs-state-functions
title: Path Functions versus State Functions
domain: physics
course: thermodynamics
prerequisites:
- id: first-law-of-thermodynamics
  type: hard
- id: state-variables-and-functions
  type: hard
builds-toward:
- exact-and-inexact-differentials
- work-types-mechanical-pdv
tags:
- first-law
- energy
- process-dependence
stage: formal-systems
status: draft
---

# Path Functions versus State Functions

## Core Idea
Heat and work are path functions—their values depend on the specific process (path) followed between two states, so ∫đQ and ∫đW must be specified for a particular path. State functions like internal energy, entropy, and enthalpy are path-independent, meaning their change ΔU, ΔS, ΔH depends only on initial and final states, not the route taken. The first law of thermodynamics relates these: ΔU = Q - W, combining a state function change with two path functions.

## How It's Best Learned
Calculate Q and W for the same state change via different paths (isothermal vs. adiabatic, etc.). Verify that ΔU is path-independent while Q and W vary.

## Common Misconceptions
- Thinking work done ON a system is always positive.
- Assuming total heat content is conserved (enthalpy is conserved under certain conditions, not heat).
- Confusing path functions with irreversible processes.

## Explainer

The distinction between state functions and path functions is one of the most conceptually important ideas in thermodynamics, and a clean analogy makes it intuitive: think of a hiker going from sea level to the top of a mountain. The **altitude gain** is a state function — it depends only on the starting and ending elevations, regardless of the route. The **distance walked** is a path function — it depends entirely on the route taken. A direct steep scramble and a long winding trail both end at the same altitude, but the hiker walks very different distances. In thermodynamics, **internal energy** U plays the role of altitude, and **heat Q** and **work W** play the role of distance walked.

From the first law, you know ΔU = Q − W. The left side, ΔU, is a state function: its value is completely determined by the initial and final thermodynamic states (temperature, pressure, volume), independent of how the system got from one to the other. The right side consists of two path functions. You can take a gas from state A (low T, low P) to state B (high T, high P) along infinitely many different paths — isothermal compression followed by heating at constant volume, or adiabatic compression followed by isobaric heating, or any combination. For each path, Q and W will differ. But ΔU will always be the same, because U depends only on the state. This is why we write the first law with δQ and δW (inexact differentials, path-dependent) but dU (an exact differential, path-independent).

A concrete numerical illustration cements this. Suppose a gas expands isothermally and reversibly from V₁ to V₂ at temperature T. The work done by the gas is W = nRT ln(V₂/V₁). For an ideal gas, U depends only on T, so ΔU = 0 for an isothermal process, and therefore Q = W — all the heat absorbed went into doing work. Now take the same gas through the same initial and final states, but via a free expansion into vacuum (irreversible). The gas does no work (W = 0) against the vacuum, and for an ideal gas in thermal isolation, no heat is exchanged (Q = 0). So Q and W are both zero — completely different from the isothermal case — yet ΔU = 0 in both cases. The state didn't change; only the path did.

Recognizing whether a quantity is a state or path function is a practical skill for every thermodynamic calculation. **Entropy** S, **enthalpy** H = U + PV, and **Gibbs free energy** G = H − TS are all state functions — their changes can be computed from initial and final states alone, and they can be used in cycle analyses where the system returns to its starting point. The fact that ΔG = 0 around any reversible cycle, for example, is central to chemical equilibrium. Heat and work, being path functions, cannot be used this way: you cannot define the "heat content" of a system in a given state, because the heat exchanged depends on how the system arrived there. The common misconception of treating "heat" as a stored quantity is precisely this error — treating a path function as if it were a state function.
