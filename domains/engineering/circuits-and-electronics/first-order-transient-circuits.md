---
id: first-order-transient-circuits
title: First-Order Transient Circuit Response
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: capacitor-inductor-energy-storage
  type: hard
- id: thevenin-norton-equivalents
  type: hard
- id: differential-equations-intro-separable
  type: hard
- id: rc-circuits
  type: soft
- id: rl-circuits
  type: soft
builds-toward:
- second-order-transient-circuits
tags:
- transient-response
- RC
- RL
- time-constant
- natural-response
- step-response
stage: formal-systems
status: draft
---

# First-Order Transient Circuit Response

## Core Idea
First-order circuits containing a single capacitor or inductor plus resistors are governed by a first-order linear ODE whose solution is an exponential. The time constant is τ = RC for RC circuits and τ = L/R for RL circuits, where R is the Thevenin resistance seen by the storage element. The complete response equals the natural response (decaying exponential driven by initial conditions) plus the forced response (due to sources). A shortcut formula v(t) = v(∞) + [v(0⁺) − v(∞)]·e^(−t/τ) applies to any DC-forced first-order circuit.

## How It's Best Learned
Use Thevenin equivalents to find τ systematically for any RC or RL topology. Practice identifying initial conditions at t = 0⁺ using continuity of capacitor voltage and inductor current, and final conditions at t → ∞ by treating C as open and L as short in DC steady state.

## Common Misconceptions
- Computing τ from the nominal component values rather than from the Thevenin resistance seen by the storage element.
- Setting initial conditions from the circuit after switching rather than just before (at t = 0⁻).
- Confusing natural and step response — both are exponential but driven by different initial and final conditions.
