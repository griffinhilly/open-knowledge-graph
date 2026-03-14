---
id: rl-circuits
title: RL Circuits
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: inductance-and-inductors
  type: hard
- id: kirchhoffs-rules
  type: hard
- id: differential-equations-intro-separable
  type: soft
builds-toward:
- lc-and-rlc-circuits
- ac-circuits-fundamentals
tags:
- RL-circuit
- time-constant
- transient
- exponential
stage: formal-systems
status: validated
---

# RL Circuits

## Core Idea
An RL circuit contains a resistor and inductor in series. When a voltage source is applied, the current builds exponentially: I(t) = (ε/R)(1 − e^(−t/τ)) with time constant τ = L/R. When the source is removed, the current decays as I(t) = I₀ e^(−t/τ). The inductor initially opposes the change in current (acts like an open circuit at t = 0) and at steady state allows full current (acts like a wire). Larger L or smaller R gives a slower response.

## How It's Best Learned
Derive the exponential solution from the Kirchhoff loop equation ε = IR + L dI/dt using separation of variables. Compare and contrast with RC circuits: τ = RC vs. τ = L/R; capacitor charges up and blocks DC, while inductor builds current and passes DC.

## Common Misconceptions
- At t = 0, the inductor does not block all current — it constrains the rate of change, making dI/dt finite.
- For t >> τ, the inductor acts as a short circuit in a DC circuit.
- Suddenly opening an RL circuit can produce a very large voltage spike — the inductor drives V = L dI/dt with a very large dI/dt.
