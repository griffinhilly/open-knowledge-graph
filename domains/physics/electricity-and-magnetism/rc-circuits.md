---
id: rc-circuits
title: RC Circuits
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: kirchhoffs-rules
  type: hard
- id: capacitance
  type: hard
- id: differential-equations-intro-separable
  type: soft
builds-toward:
- ac-circuits-fundamentals
- lc-and-rlc-circuits
tags:
- RC-circuit
- time-constant
- charging
- discharging
- transient
stage: formal-systems
status: draft
---

# RC Circuits

## Core Idea
An RC circuit consists of a resistor and capacitor in series. When charging, the voltage across the capacitor rises exponentially: V_C(t) = ε(1 − e^(−t/RC)). When discharging, it decays as V_C(t) = V₀ e^(−t/RC). The time constant τ = RC governs the rate — after one time constant, the capacitor reaches 63% of its final charge. After ~5τ, transient behavior is essentially complete.

## How It's Best Learned
Derive the exponential solutions from Kirchhoff's loop equation using separation of variables. Build intuition by considering limits: t → 0 (capacitor acts as wire) and t → ∞ (capacitor acts as open circuit) to check results.

## Common Misconceptions
- A fully charged capacitor blocks DC current; the current is zero at steady state, not the voltage.
- Larger R slows the charging/discharging rate; larger C also slows it.
- The time constant RC has units of seconds, not ohms or farads individually.
