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
- id: first-order-linear-odes
  type: hard
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
status: validated
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

## Explainer

You know from capacitor and inductor theory that these elements store energy — a capacitor stores it in an electric field (voltage), an inductor in a magnetic field (current). You also know from first-order ODE theory that the equation dx/dt + (1/τ)x = f(t) has an exponential solution. First-order transient analysis is where these two threads meet: a single-capacitor or single-inductor circuit, when disturbed, responds with a decaying exponential whose time constant τ tells you how fast the energy dissipates into resistors.

The key first step is to replace all the resistors in the circuit with their **Thevenin equivalent** as seen from the terminals of the storage element. This reduces any complicated resistor network to a single equivalent resistance R_th in series (for RC) or in parallel (for RL). The time constant then follows immediately: τ = R_th · C for a capacitor, τ = L / R_th for an inductor. One τ represents the time to decay about 63% of the way toward the final value; five τ is engineering convention for "effectively done." The Thevenin approach is why you needed that prerequisite — it converts any first-order problem into the same canonical form, regardless of circuit topology.

The complete response has two parts. The **natural response** accounts for initial stored energy draining away: if a capacitor starts at voltage v₀ with no source, it decays as v₀·e^(−t/τ). The **forced response** (or particular solution) accounts for external sources driving the circuit toward a new steady state. For a DC source, the forced response is simply the DC steady-state value v(∞), found by treating the capacitor as an open circuit and the inductor as a short circuit at t → ∞. The total solution combines both: v(t) = v(∞) + [v(0⁺) − v(∞)]·e^(−t/τ).

This **shortcut formula** is worth internalizing because it reduces every DC-forced first-order problem to finding three numbers: the initial value v(0⁺), the final value v(∞), and the time constant τ. Initial conditions follow from continuity: capacitor voltage and inductor current cannot jump instantaneously, so v(0⁺) = v(0⁻) — the value just before switching. The formula then fills in the exponential trajectory between the known initial and final states. Once you see that the natural response and step response are just two special cases of the same formula (one with v(∞) = 0, one with v(0⁺) = 0), the apparent distinction between them dissolves.
