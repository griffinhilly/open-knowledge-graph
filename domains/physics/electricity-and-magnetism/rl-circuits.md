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

## Explainer

An RL circuit is the magnetic analogue of the RC circuit: where a capacitor stores energy in an electric field and resists sudden voltage changes, an **inductor** stores energy in a magnetic field and resists sudden current changes. You already know from inductance theory that V = L dI/dt — the inductor's voltage is proportional to how rapidly the current is changing. When you first close the switch on an RL circuit, the current is zero and the inductor's back-EMF exactly cancels the source voltage, so the initial rate of change dI/dt = ε/L is large. As current builds, the back-EMF shrinks, and the rate of growth slows. The result is an exponential approach to the steady-state current.

To derive this precisely, apply Kirchhoff's voltage law around the loop: ε = IR + L dI/dt. Rearranging gives L dI/dt = ε − IR, a first-order linear ODE. Separating variables and integrating gives I(t) = (ε/R)(1 − e^(−t/τ)) where the **time constant τ = L/R** sets the timescale. At t = τ, the current has reached about 63% of its final value; at t = 5τ, it is within 1% of ε/R. The final current is simply ε/R — Ohm's law — because in DC steady state, dI/dt = 0, so the inductor contributes no voltage drop and looks like a short circuit (a plain wire).

A useful physical analogy: the inductor acts like inertia in mechanics, and the resistor acts like friction. When you push on a massive object (apply a voltage), it doesn't instantly reach full speed (current) — it accelerates gradually. The time constant τ = L/R is analogous to the mass-to-friction ratio: a heavy object with little friction takes a long time to reach terminal velocity. Larger L means more magnetic inertia, more stored energy per unit current, and a slower response. Smaller R means less dissipation per unit current, so the energy that was supposed to damp the transient dissipates more slowly.

When the source is switched off and the circuit is opened through the same resistance, the energy stored in the inductor (U = ½LI₀²) drives a decaying current I(t) = I₀ e^(−t/τ) as the magnetic energy is dissipated in the resistor. If instead the circuit is opened abruptly through a very high resistance or a switch — making R effectively infinite — the energy must dissipate in a tiny τ, which means dI/dt is enormous. Since V_L = L dI/dt, this produces a massive voltage spike across the inductor. This is not an abstraction: the spike can arc across switch contacts and destroy semiconductor devices. In practical circuits, a **snubber diode** (flyback diode) is placed across the inductor to provide an alternative current path and tame the spike — a direct application of understanding the inductive voltage-current relationship.
