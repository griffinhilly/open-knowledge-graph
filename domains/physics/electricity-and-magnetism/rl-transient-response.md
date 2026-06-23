---
id: rl-transient-response
title: Transient Response in RL Circuits
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: self-inductance
  type: hard
- id: rc-transient-response
  type: soft
builds-toward:
- ac-impedance
tags:
- rl-circuit
- transient
- inductance
stage: formal-systems
status: validated
---

# Transient Response in RL Circuits

## Core Idea
In an RL circuit, current grows as I(t) = (V/R)(1 − e^(−t/τ)) when voltage is applied, where τ = L/R is the time constant. Inductance opposes current changes, so initial current is zero and voltage across the inductor is V_L = L dI/dt. At large times, current approaches V/R as inductance effects become negligible. Time constant scales with inductance and inversely with resistance.

## Questions

```yaml
- question: "At the instant t = 0 when a battery of voltage V is connected to a series RL circuit (initially at rest), what is the voltage across the inductor?"
  type: multiple-choice
  options:
    - "Zero — current hasn't flowed yet so the inductor is inactive"
    - "V/2 — the voltage is split equally between the inductor and resistor at t = 0"
    - "V — all of the battery voltage appears across the inductor because current is zero and V_R = IR = 0"
    - "V/R — the same as the steady-state current times resistance"
  answer: 2
  explanation: "At t = 0, the inductor enforces I = 0 (it cannot allow an instantaneous current jump). Since V_R = IR = 0·R = 0, Kirchhoff's voltage law (V = V_R + V_L) gives V_L = V − 0 = V. All of the battery voltage is initially across the inductor. As current builds and I increases, V_R grows and V_L shrinks, until at steady state V_L = 0 and V_R = V. The transient is a smooth handoff of voltage from inductor to resistor."

- question: "An engineer doubles the inductance L in an RL circuit while keeping resistance R constant. What happens to the time constant τ and the speed at which current approaches its final value?"
  type: multiple-choice
  options:
    - "τ is halved — larger inductance means the circuit reaches steady state faster"
    - "τ is unchanged — only R affects the time constant"
    - "τ is doubled — the inductor fights harder against current changes, so the rise is slower"
    - "τ is doubled and the final current I = V/R is also doubled"
  answer: 2
  explanation: "τ = L/R, so doubling L doubles τ. A larger inductance means greater opposition to current changes (larger back-EMF for the same dI/dt), so it takes longer for current to build to its final value. The final current V/R is unchanged — it depends only on resistance. After one τ, current reaches 63% of V/R; after 5τ, it is at 99%. Doubling τ means it takes twice as long to reach each milestone. Larger L = slower transient; larger R = faster transient (τ = L/R decreases)."

- question: "A larger resistance R in a series RL circuit causes the current to rise more slowly to its final steady-state value."
  type: true-false
  answer: false
  explanation: "Larger R actually speeds up the transient. The time constant is τ = L/R, so increasing R decreases τ, meaning the current approaches its final value faster. Intuitively, higher R dissipates energy more rapidly, reducing the inductor's ability to sustain its opposition. The final current V/R is also smaller (since R is larger), but it is reached in fewer seconds. Many students expect larger R to slow things down because it 'resists' current — but the time constant τ = L/R shows R appears in the denominator."

- question: "At steady state in a DC RL circuit, the inductor carries the full steady-state current and behaves effectively as a short circuit (a plain wire)."
  type: true-false
  answer: true
  explanation: "At steady state, dI/dt = 0 because current is no longer changing. The inductor's voltage is V_L = L dI/dt = L·0 = 0. An element with zero voltage drop and nonzero current through it is electrically equivalent to a wire (short circuit). All of the battery voltage then appears across the resistor, and I = V/R. This is why inductors 'look like wires' to DC at steady state and why they are used to block AC signals while passing DC — at steady DC, they disappear electrically."

- question: "Why is the initial current in a DC RL circuit exactly zero when voltage is first applied, and why does the final current equal V/R rather than some other value?"
  type: short-answer
  answer: "The initial current is zero because the inductor enforces continuity of current — any instantaneous jump would require infinite voltage (V_L = L dI/dt with dI/dt → ∞). The inductor opposes the change, so current starts at zero and builds gradually. The final current equals V/R because at steady state the current is no longer changing (dI/dt = 0), so the inductor's voltage drop V_L = L dI/dt = 0, and Kirchhoff's law gives V = IR, so I = V/R."
  explanation: "These two boundary conditions — I(0) = 0 and I(∞) = V/R — fully determine the exponential solution I(t) = (V/R)(1 − e^(−t/τ)). The initial condition comes from the inductor's physical constraint (current continuity); the final condition comes from the DC steady state where inductance is irrelevant. The exponential curve with time constant τ = L/R smoothly interpolates between these two values. Understanding the physics at t = 0 and t → ∞ is the key to understanding the transient at all intermediate times."
```

## Explainer

From self-inductance, you know that an inductor resists changes in current — its back-EMF is V_L = L dI/dt. When you connect a battery to an RL circuit at t = 0, the inductor doesn't let the current jump instantly to V/R the way a purely resistive circuit would. Instead, the inductor demands that current change gradually. To see why, apply Kirchhoff's voltage law around the loop: V = IR + L dI/dt. This is a first-order linear differential equation, and its solution is I(t) = (V/R)(1 − e^(−t/τ)) where τ = L/R is the **time constant**.

Trace the physics through time. At t = 0, current is zero (the inductor enforces this — any instantaneous jump would require infinite voltage). All of the battery voltage appears across the inductor: V_L = V, while V_R = 0. As current slowly builds, the voltage across the resistor IR grows, so the inductor's share V_L = V − IR shrinks. The inductor's opposition weakens as the rate of change dI/dt decreases. At large times, dI/dt → 0 and the inductor looks like a plain wire: the final current is simply V/R and all the voltage is across the resistor. The exponential curve traces this smooth handoff of voltage from inductor to resistor.

A useful analogy is the RC circuit's transient response, which you may know: a capacitor charges toward its final voltage exponentially with time constant τ = RC, while the resistor voltage decays. The RL circuit is its dual — the inductor's current builds up while the inductor voltage decays. In both cases, the time constant measures the same thing: "how long does the transient last?" After one τ, the current reaches 63% of its final value; after 5τ, it's within 1% and considered steady-state. Large L means slow current rise (the inductor fights harder); large R means fast rise (the resistor dissipates energy quickly, reducing the current overshoot problem).

This transient behavior is why inductors appear in switching power supplies, relay circuits, and motor control — anywhere the sudden interruption or application of current would otherwise cause voltage spikes. When you open a switch in an RL circuit (forcing I → 0 suddenly), the inductor attempts to maintain current by generating a large voltage spike — V_L = L dI/dt with a very large dI/dt. Engineers exploit this in boost converters and must protect against it in relay drivers using flyback diodes. The time constant τ = L/R is the single parameter governing how much time is available to manage these transitions.
