---
id: entropy-definition-and-calculation
title: Entropy Definition and Calculation
domain: physics
course: thermodynamics
prerequisites:
- id: reversible-isothermal-expansion
  type: hard
- id: second-law-of-thermodynamics
  type: hard
- id: logarithm-properties
  type: soft
- id: logarithmic-functions-review
  type: hard
tags:
- entropy
- reversible
- thermodynamic-definition
stage: formal-systems
status: draft
---

# Entropy Definition and Calculation

## Core Idea
For a reversible process, entropy change is defined as dS = dQ_rev / T. For an ideal gas expanding isothermally, ΔS = nR ln(V_f/V_i). Entropy is a state function—it depends only on the current state, not the path. This definition provides a rigorous connection between heat, temperature, and microscopic disorder.

## Questions

```yaml
- question: "An ideal gas undergoes free expansion into a vacuum: it doubles in volume, but no heat is transferred and no work is done (Q = 0, W = 0). What is the entropy change ΔS of the gas?"
  type: multiple-choice
  options:
    - "Zero, because no heat was transferred (Q = 0)"
    - "Zero, because internal energy didn't change (ΔU = 0)"
    - "nR ln(2), positive — calculated via an equivalent reversible path"
    - "Negative, because the gas expanded spontaneously into disorder"
  answer: 2
  explanation: "Entropy is a state function, so ΔS depends only on the initial and final states, not on the actual (irreversible) path. Even though Q_actual = 0, you must compute ΔS by imagining a reversible isothermal expansion between the same two states, giving ΔS = nR ln(V_f/V_i) = nR ln(2) > 0. Option A is the most tempting mistake: using Q_actual in dS = dQ/T. The subscript 'rev' in dS = dQ_rev/T is essential — it demands the reversible path, not the actual one."

- question: "A Carnot engine absorbs Q_H = 1000 J from a reservoir at T_H = 600 K and exhausts Q_C to a reservoir at T_C = 300 K. What is the total entropy change of the universe per cycle?"
  type: multiple-choice
  options:
    - "Zero — a Carnot engine is reversible, so the universe's entropy doesn't change"
    - "Positive — heat flows from hot to cold, so entropy must increase"
    - "Negative — work is extracted, reducing the universe's disorder"
    - "+Q_H/T_H = 1000/600 ≈ 1.67 J/K"
  answer: 0
  explanation: "For a Carnot engine with efficiency η = 1 − T_C/T_H = 0.5, the work output is 500 J and the heat rejected is Q_C = 500 J. The entropy change of the hot reservoir is −Q_H/T_H = −1000/600, and of the cold reservoir is +Q_C/T_C = +500/300. These cancel exactly: −5/3 + 5/3 = 0. This is the defining property of a reversible engine — zero net entropy change. Any irreversible engine would produce Q_C/T_C > Q_H/T_H, giving a positive total ΔS."

- question: "Entropy is a state function, which means its change between two states is the same regardless of which path — reversible or irreversible — connects them."
  type: true-false
  answer: true
  explanation: "This is the foundational property that makes entropy calculable. Just as the change in gravitational potential energy between two heights is path-independent, ΔS between two thermodynamic states is fixed. This is why you are allowed — and required — to use a reversible path to compute ΔS even when the actual process was irreversible. The actual process might involve ΔQ_actual ≠ Q_rev, but the entropy change is the same."

- question: "For any real process involving heat transfer, you can calculate the entropy change using ΔS = Q_actual/T, where Q_actual is the heat exchanged during the process."
  type: true-false
  answer: false
  explanation: "This formula is only valid for reversible processes. For irreversible processes, Q_actual ≠ Q_rev, and using Q_actual gives the wrong answer — as the free-expansion example shows starkly (Q_actual = 0, yet ΔS > 0). The correct definition is dS = dQ_rev/T, where the heat integral must be taken along a reversible path connecting the same endpoints. For irreversible processes, ΔS_universe > 0, which is encoded in the Clausius inequality: ∮ dQ/T ≤ 0, with equality only for reversible cycles."

- question: "Why must you use a reversible path to calculate entropy change, even when the actual process was irreversible?"
  type: short-answer
  answer: "Entropy is a state function — it has a definite value at each equilibrium state, and the change between two states is path-independent. This means you can choose any convenient path between the same initial and final states to calculate ΔS. Because the definition dS = dQ/T is only rigorously valid for reversible processes (where the system is always near equilibrium), you must construct a reversible path. The actual irreversible path may involve different heat exchanges, but since ΔS is path-independent, the result calculated via the reversible path applies to any process between those states."
  explanation: "The subtlety is that dQ/T along an irreversible path does not give the entropy change — it gives a lower bound (Clausius inequality). Only along a reversible path does dQ_rev/T exactly equal dS. The state-function property is what licenses this substitution: you compute using the convenient reversible path, and the answer is valid for the actual path too."
```

## Explainer

The second law of thermodynamics tells you that certain processes are irreversible — heat flows from hot to cold, not the reverse; compressed gas expands spontaneously but doesn't spontaneously recompress. You know this from experience, but you also know it leaves something unexplained: *how much* more irreversible is one process than another? Entropy is the answer. It is a state function that quantifies the direction and degree of thermodynamic change, turning the qualitative arrow of time into a calculable quantity.

The definition dS = dQ_rev / T requires care. The subscript *rev* is doing all the work: it says you must calculate the entropy change by imagining a **reversible path** between the initial and final states, even if the actual process was irreversible. This is valid because entropy is a state function — like internal energy U, it depends only on the current state, not on how you got there. So you are free to choose the most convenient reversible path connecting the same two endpoints and integrate dQ/T along it. For an isothermal reversible expansion of an ideal gas from V_i to V_f, all the heat absorbed is Q_rev = nRT ln(V_f/V_i) (since internal energy doesn't change for an ideal gas at constant T), giving ΔS = nR ln(V_f/V_i).

Two cases illustrate the state-function nature. First: an ideal gas that expands irreversibly into a vacuum absorbs no heat (Q = 0, since it pushes against nothing), so you might naively conclude ΔS = 0. But entropy still increases — you must use the reversible path (the isothermal expansion), not the actual path. The entropy change is ΔS = nR ln(V_f/V_i) > 0 regardless. Second: a heat engine absorbs Q_H from a hot reservoir at T_H and rejects Q_C to a cold reservoir at T_C. The engine's entropy change over a cycle is zero (it returns to the same state). The total entropy change of the universe is −Q_H/T_H + Q_C/T_C, which the second law says must be ≥ 0. This forces Q_C/T_C ≥ Q_H/T_H, giving you the Carnot efficiency limit directly from the entropy definition.

The connection to **microscopic disorder** comes from Boltzmann's relation S = k_B ln W, where W is the number of microstates consistent with the macroscopic state. This is not a separate definition — it turns out to be equivalent to the thermodynamic definition for systems in thermal equilibrium. The logarithm is why entropy is additive: if you have two independent systems with W₁ and W₂ microstates, the combined system has W₁W₂ microstates, and ln(W₁W₂) = ln W₁ + ln W₂. The connection between dQ_rev/T and ln W is one of the deepest results in physics, bridging macroscopic thermodynamics and statistical mechanics in a single formula.
