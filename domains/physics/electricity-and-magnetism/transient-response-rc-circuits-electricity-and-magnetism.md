---
id: transient-response-rc-circuits-electricity-and-magnetism
title: Transient Response in RC Circuits
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: network-circuit-analysis-methods
  type: hard
- id: differential-equations-intro-separable
  type: hard
builds-toward:
- magnetic-force-moving-charges
tags:
- transient
- rc-circuit
- time-constant
stage: formal-systems
status: draft
---

# Transient Response in RC Circuits

## Core Idea
RC charging: Q(t) = Q₀(1 − e^(−t/RC)), with time constant τ = RC. RC discharging: Q(t) = Q₀e^(−t/RC). Voltage and current similarly decay exponentially. Time constant determines how quickly the circuit reaches steady state.

## Questions

```yaml
- question: "A capacitor is 90% charged. Roughly how many time constants have elapsed since charging began?"
  type: multiple-choice
  options:
    - "0.9 time constants — the capacitor charges linearly at 100%/τ"
    - "1 time constant — the capacitor is fully charged after one τ"
    - "About 2.3 time constants"
    - "Exactly 10 time constants"
  answer: 2
  explanation: "Charging follows V(t) = V₀(1 − e^(−t/τ)). Setting 0.90 = 1 − e^(−t/τ) gives e^(−t/τ) = 0.10, so t/τ = −ln(0.10) ≈ 2.3. The charging curve is exponential, not linear — it rushes quickly at first and slows as it approaches the asymptote. One τ only gets you to about 63%, not 90%, and the capacitor never formally 'fully charges' in finite time."

- question: "Doubling the resistance in an RC circuit while keeping capacitance fixed will double the time constant and therefore halve the initial charging current."
  type: true-false
  answer: false
  explanation: "Doubling R does double the time constant τ = RC — the circuit now charges more slowly. But the initial charging current I₀ = V/R is halved by doubling R. The statement says this 'halves' the current, which is actually true numerically, but the claim combines two separate effects as if they follow the same logic. More importantly, a common confusion is thinking τ increasing means the circuit reaches steady state faster. The opposite is true: τ doubling means the circuit takes twice as long to reach any given fraction of its final charge."

- question: "At t = τ (one time constant) during RC discharge, what percentage of the initial charge remains on the capacitor?"
  type: true-false
  answer: false
  explanation: "At t = τ, Q(τ) = Q₀e^(−1) ≈ 0.368 Q₀, meaning about 37% of the initial charge remains — not 50%. A common misconception is that τ is the 'half-life.' The half-life of an RC discharge is t₁/₂ = τ ln(2) ≈ 0.693τ. The statement is false; after one time constant, roughly 63% has discharged, not 50%."

- question: "If you increase both R and C by a factor of 10 each, what happens to the time constant?"
  type: multiple-choice
  options:
    - "It stays the same — the increases cancel each other out"
    - "It increases by a factor of 10"
    - "It increases by a factor of 100"
    - "It decreases by a factor of 10, since more resistance reduces current flow"
  answer: 2
  explanation: "τ = RC, so if R → 10R and C → 10C, then τ → (10R)(10C) = 100RC = 100τ. The time constant is a product of resistance and capacitance, not a ratio. Both increases multiply together. The misconception in option A (that they cancel) would apply if τ were R/C or C/R, but it is their product."

- question: "Why does the voltage across a capacitor change exponentially rather than linearly during charging, and what physical constraint causes this shape?"
  type: short-answer
  answer: "The charging current equals (V_battery − V_C)/R. As the capacitor charges, V_C rises, which reduces the voltage difference driving the current, which slows the rate of charging. The rate of change of charge is proportional to the remaining 'gap' — exactly the condition that produces exponential growth toward an asymptote. The same feedback logic appears in any first-order system: the closer you get to the target, the slower you approach it."
  explanation: "The exponential shape is not arbitrary; it is the mathematical solution to dQ/dt = −Q/(RC), where the rate of change is proportional to the current state. In charging: the driving force (battery EMF minus capacitor voltage) shrinks as charge accumulates, continuously slowing the rate. In discharging: the driving force (the capacitor voltage itself) shrinks as charge leaves, again slowing the rate. The time constant τ = RC quantifies this self-limiting timescale."
```

## Explainer

From your circuit analysis work, you know how to apply Kirchhoff's laws to find voltages and currents in steady-state networks. But what happens in the moments after you close a switch or change a voltage? That transition — the **transient response** — is what RC circuits are built to reveal. The capacitor is the element that makes things time-dependent: because V_C = Q/C and charge can only accumulate at a finite rate, the capacitor voltage cannot jump instantaneously, and this constraint governs the entire circuit's evolution.

Start with a discharging RC circuit: a capacitor with initial charge Q₀ connected in series with a resistor. Applying Kirchhoff's voltage law gives V_C − V_R = 0, i.e., Q/C = IR = (−dQ/dt)R, which rearranges to dQ/dt = −Q/(RC). You learned to solve exactly this type of separable differential equation in your prerequisite: the solution is Q(t) = Q₀e^(−t/RC). The charge (and therefore the voltage across the capacitor, V_C = Q₀e^(−t/RC)/C) decays **exponentially** toward zero. The current I(t) = −dQ/dt = (Q₀/RC)e^(−t/RC) also decays exponentially, starting at a maximum and falling to zero as the capacitor empties.

The **time constant** τ = RC encodes the characteristic timescale. At t = τ, the charge has fallen to e⁻¹ ≈ 37% of its initial value; at t = 2τ it is about 14%; at t = 5τ it is effectively zero (less than 1%). The units check out: ohms × farads = (V/A) × (C/V) = C/(C/s) = seconds. A large resistance slows the discharge because less current can flow; a large capacitance slows it because more charge must be removed. The charging case is the mirror image: connect a capacitor through a resistor to a battery of EMF ε, and Q(t) = Q₀(1 − e^(−t/RC)), approaching its equilibrium value Q₀ = Cε asymptotically, never quite reaching it in finite time.

The exponential form is not just a mathematical accident — it is the signature of any system where the rate of change is proportional to the current state. The same differential equation describes radioactive decay, Newton's law of cooling, and many biological processes. Recognizing this pattern — first-order linear ODE with constant coefficients → exponential solution → time constant = 1/(coefficient) — lets you read off the transient behavior by inspection once you have the governing equation. In circuit design, τ = RC is the key design parameter: filters, timers, signal-shaping networks, and analog integrators all work by choosing R and C to set the desired timescale of response.
