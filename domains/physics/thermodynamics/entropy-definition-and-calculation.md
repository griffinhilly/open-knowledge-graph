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

## Explainer

The second law of thermodynamics tells you that certain processes are irreversible — heat flows from hot to cold, not the reverse; compressed gas expands spontaneously but doesn't spontaneously recompress. You know this from experience, but you also know it leaves something unexplained: *how much* more irreversible is one process than another? Entropy is the answer. It is a state function that quantifies the direction and degree of thermodynamic change, turning the qualitative arrow of time into a calculable quantity.

The definition dS = dQ_rev / T requires care. The subscript *rev* is doing all the work: it says you must calculate the entropy change by imagining a **reversible path** between the initial and final states, even if the actual process was irreversible. This is valid because entropy is a state function — like internal energy U, it depends only on the current state, not on how you got there. So you are free to choose the most convenient reversible path connecting the same two endpoints and integrate dQ/T along it. For an isothermal reversible expansion of an ideal gas from V_i to V_f, all the heat absorbed is Q_rev = nRT ln(V_f/V_i) (since internal energy doesn't change for an ideal gas at constant T), giving ΔS = nR ln(V_f/V_i).

Two cases illustrate the state-function nature. First: an ideal gas that expands irreversibly into a vacuum absorbs no heat (Q = 0, since it pushes against nothing), so you might naively conclude ΔS = 0. But entropy still increases — you must use the reversible path (the isothermal expansion), not the actual path. The entropy change is ΔS = nR ln(V_f/V_i) > 0 regardless. Second: a heat engine absorbs Q_H from a hot reservoir at T_H and rejects Q_C to a cold reservoir at T_C. The engine's entropy change over a cycle is zero (it returns to the same state). The total entropy change of the universe is −Q_H/T_H + Q_C/T_C, which the second law says must be ≥ 0. This forces Q_C/T_C ≥ Q_H/T_H, giving you the Carnot efficiency limit directly from the entropy definition.

The connection to **microscopic disorder** comes from Boltzmann's relation S = k_B ln W, where W is the number of microstates consistent with the macroscopic state. This is not a separate definition — it turns out to be equivalent to the thermodynamic definition for systems in thermal equilibrium. The logarithm is why entropy is additive: if you have two independent systems with W₁ and W₂ microstates, the combined system has W₁W₂ microstates, and ln(W₁W₂) = ln W₁ + ln W₂. The connection between dQ_rev/T and ln W is one of the deepest results in physics, bridging macroscopic thermodynamics and statistical mechanics in a single formula.
