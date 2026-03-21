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

## Questions

```yaml
- question: "A circuit has a 12 V battery, a 4 Ω resistor, and an 8 H inductor in series. The switch is closed at t = 0. What is the current through the circuit immediately after the switch closes?"
  type: multiple-choice
  options:
    - "3 A — Ohm's law gives I = ε/R = 12/4"
    - "0 A — the inductor prevents any instantaneous change in current"
    - "1.5 A — the inductor acts as a 4 Ω equivalent impedance at t = 0"
    - "Undefined — no current flows until the transient ends"
  answer: 1
  explanation: "At t = 0, the inductor's back-EMF exactly cancels the source voltage, so the initial current is zero. The inductor does not block current permanently — it resists instantaneous *changes* in current. The current builds exponentially toward ε/R = 3 A over time. Option A is the steady-state answer, not the t = 0 answer. This is the most common confusion: treating the inductor's initial behavior as a steady-state Ohm's law calculation."

- question: "What happens to the time constant τ of a series RL circuit if the resistance R is doubled while the inductance L stays the same?"
  type: multiple-choice
  options:
    - "τ doubles, because more resistance means slower current flow"
    - "τ halves, because τ = L/R and doubling R reduces τ"
    - "τ stays the same, because L is unchanged"
    - "τ increases by a factor of 4, because energy dissipation goes as R²"
  answer: 1
  explanation: "The time constant is τ = L/R. Doubling R halves τ, meaning the circuit reaches steady state twice as fast. This is counterintuitive to many students who think more resistance means slower response — but more resistance means more energy dissipated per unit current, which actually drains the transient faster. Compare with RC circuits where τ = RC and larger R *slows* the response: in RL circuits, R plays the opposite role."

- question: "In an RL circuit at t = 0, the inductor acts like an open circuit because no current can ever flow through an inductor."
  type: true-false
  answer: false
  explanation: "The inductor acts like an open circuit *initially* (at t = 0) only in the sense that it constrains the current to start at zero and change at a finite rate. Current does flow through the inductor — it just cannot change instantaneously. The open-circuit analogy describes the initial state: the back-EMF equals the source voltage, so net current is zero. But current builds continuously after that, and at steady state the inductor acts as a plain wire (short circuit) with no voltage drop at all."

- question: "Abruptly opening an RL circuit while a large current is flowing can produce a voltage spike much larger than the original source voltage."
  type: true-false
  answer: true
  explanation: "The inductor's voltage is V = L dI/dt. If the circuit is interrupted suddenly — making the current drop from I₀ to zero in a very short time — then dI/dt is enormous, and the inductor produces a correspondingly huge voltage spike. This can arc across switch contacts and destroy semiconductor components. This is why real circuits use snubber (flyback) diodes across inductors: they provide an alternative current path to allow the energy to dissipate safely rather than appearing as a destructive spike."

- question: "Why does the current in a DC RL circuit approach ε/R at steady state rather than continuing to grow? What role does the inductor play once steady state is reached?"
  type: short-answer
  answer: "At steady state, dI/dt = 0 — the current is no longer changing. Since the inductor's voltage is V_L = L dI/dt, a zero rate of change means the inductor contributes no voltage drop. It behaves as a plain wire (short circuit). With only the resistor left in the circuit, Ohm's law gives I = ε/R. The current doesn't grow indefinitely because as it approaches ε/R, the back-EMF of the inductor decreases, reducing dI/dt, which is the self-limiting exponential approach to equilibrium."
  explanation: "This is the key to understanding inductor behavior in DC circuits: inductors only 'fight back' when current is changing. Once steady state is reached and dI/dt = 0, the inductor is electrically invisible. It becomes relevant again the moment any change is introduced — a switch opened or closed, a load added — at which point it resists the new change and the transient begins again."
```

## Explainer

An RL circuit is the magnetic analogue of the RC circuit: where a capacitor stores energy in an electric field and resists sudden voltage changes, an **inductor** stores energy in a magnetic field and resists sudden current changes. You already know from inductance theory that V = L dI/dt — the inductor's voltage is proportional to how rapidly the current is changing. When you first close the switch on an RL circuit, the current is zero and the inductor's back-EMF exactly cancels the source voltage, so the initial rate of change dI/dt = ε/L is large. As current builds, the back-EMF shrinks, and the rate of growth slows. The result is an exponential approach to the steady-state current.

To derive this precisely, apply Kirchhoff's voltage law around the loop: ε = IR + L dI/dt. Rearranging gives L dI/dt = ε − IR, a first-order linear ODE. Separating variables and integrating gives I(t) = (ε/R)(1 − e^(−t/τ)) where the **time constant τ = L/R** sets the timescale. At t = τ, the current has reached about 63% of its final value; at t = 5τ, it is within 1% of ε/R. The final current is simply ε/R — Ohm's law — because in DC steady state, dI/dt = 0, so the inductor contributes no voltage drop and looks like a short circuit (a plain wire).

A useful physical analogy: the inductor acts like inertia in mechanics, and the resistor acts like friction. When you push on a massive object (apply a voltage), it doesn't instantly reach full speed (current) — it accelerates gradually. The time constant τ = L/R is analogous to the mass-to-friction ratio: a heavy object with little friction takes a long time to reach terminal velocity. Larger L means more magnetic inertia, more stored energy per unit current, and a slower response. Smaller R means less dissipation per unit current, so the energy that was supposed to damp the transient dissipates more slowly.

When the source is switched off and the circuit is opened through the same resistance, the energy stored in the inductor (U = ½LI₀²) drives a decaying current I(t) = I₀ e^(−t/τ) as the magnetic energy is dissipated in the resistor. If instead the circuit is opened abruptly through a very high resistance or a switch — making R effectively infinite — the energy must dissipate in a tiny τ, which means dI/dt is enormous. Since V_L = L dI/dt, this produces a massive voltage spike across the inductor. This is not an abstraction: the spike can arc across switch contacts and destroy semiconductor devices. In practical circuits, a **snubber diode** (flyback diode) is placed across the inductor to provide an alternative current path and tame the spike — a direct application of understanding the inductive voltage-current relationship.
