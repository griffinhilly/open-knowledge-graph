---
id: inductance-and-inductors
title: Inductance and Inductors
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: faradays-law
  type: hard
- id: amperes-law
  type: soft
- id: lenzs-law
  type: soft
builds-toward:
- rl-circuits
- lc-and-rlc-circuits
- energy-stored-in-fields
tags:
- inductance
- inductor
- self-inductance
- solenoid
- henry
stage: formal-systems
status: validated
---
# Inductance and Inductors

## Core Idea
Self-inductance L is the property of a circuit by which a change in current induces an opposing EMF in the same circuit: ε_L = −L dI/dt, measured in henries (H = V·s/A). For a solenoid with N turns, area A, and length ℓ, L = μ₀N²A/ℓ. The energy stored in an inductor is U = ½LI², analogous to the capacitor formula ½CV². Mutual inductance M describes EMF induced in one coil by changing current in another, forming the basis of transformers.

## How It's Best Learned
Derive the solenoid self-inductance from the Biot-Savart/Ampère result for B inside a solenoid, then compute the flux linkage NΦ. Contrast inductors with capacitors: inductors resist changes in current; capacitors resist changes in voltage.

## Common Misconceptions
- Inductors oppose changes in current, not current itself — at steady state, an ideal inductor is a short circuit.
- The energy in an inductor is stored in the magnetic field, just as a capacitor stores energy in the electric field.
- A large inductance does not mean large current or large flux — it means large EMF per unit rate of current change.

## Questions

```yaml
- question: "An ideal inductor is connected in a simple DC circuit with a resistor and a battery. After the circuit has been running for a very long time (steady state), what is the voltage across the inductor?"
  type: multiple-choice
  options:
    - "Equal to the battery voltage, since the inductor is in the circuit"
    - "Zero, because dI/dt = 0 at steady state, so ε_L = −L dI/dt = 0"
    - "Equal to L times the current flowing through it"
    - "Undefined, because inductors cannot operate in DC circuits"
  answer: 1
  explanation: "This tests the most important behavioral fact about inductors: they oppose changes in current, not current itself. The induced EMF is ε_L = −L dI/dt. At DC steady state, current is constant — dI/dt = 0 — so the back-EMF is zero. The inductor behaves like a short circuit: all voltage drops across the resistor, and the inductor passes current freely. This is opposite to a capacitor, which at DC steady state is fully charged and acts as an open circuit. Confusing 'opposes current' with 'opposes changes in current' is the most common error with inductors."

- question: "A solenoid has inductance L = μ₀N²A/ℓ. Which single modification would double L?"
  type: multiple-choice
  options:
    - "Doubling the current flowing through it"
    - "Doubling the number of turns N (while keeping length and area the same)"
    - "Halving the length ℓ (while keeping N and area the same)"
    - "Doubling both the length and area simultaneously"
  answer: 2
  explanation: "From L = μ₀N²A/ℓ, halving the length doubles L (since L ∝ 1/ℓ). Doubling N would quadruple L — the N² dependence means each extra turn both contributes to B and experiences more flux. Doubling the current doesn't affect L at all: inductance is a geometric property, entirely independent of current. Doubling both length and area simultaneously leaves L unchanged (2A/2ℓ = A/ℓ). The N² relationship is the subtlest — students often expect a linear relationship between turns and inductance."

- question: "The energy stored in an inductor carrying current I equals ½LI², and this energy resides in the magnetic field surrounding the conductor."
  type: true-false
  answer: true
  explanation: "Both parts are correct. The energy formula U = ½LI² comes from integrating the work done against the back-EMF while ramping current from 0 to I. That energy resides in the magnetic field — for a solenoid, the energy density is B²/2μ₀ throughout the field volume, and integrating over the solenoid volume gives exactly ½LI². This is the magnetic analog of a capacitor's ½CV², whose energy resides in the electric field. When current is interrupted, that stored magnetic energy drives a large voltage spike as the field collapses."

- question: "An inductor with a larger inductance will carry more current than one with a smaller inductance when both are connected to the same DC voltage source."
  type: true-false
  answer: false
  explanation: "Inductance determines how strongly a coil opposes changes in current, not how much current flows in steady state. In a DC circuit at steady state, an ideal inductor is a short circuit regardless of its inductance value — the steady-state current is determined by circuit resistance (V = IR), not by L. Larger L means the current takes longer to reach steady state (time constant τ = L/R is larger), but the final current is identical. Confusing 'larger L resists current changes more strongly' with 'larger L carries less current' is a common misconception — L controls rate of change, not magnitude."

- question: "What does the equation ε_L = −L dI/dt reveal about how an inductor behaves differently when current is changing rapidly versus when current is constant?"
  type: short-answer
  answer: "When current is changing rapidly (large dI/dt), the equation produces a large back-EMF — the inductor strongly resists the change, acting like a high-impedance element. When current is constant (dI/dt = 0 at DC steady state), the back-EMF is zero regardless of L — the inductor offers no opposition and acts as a short circuit. This duality explains why inductors block high-frequency AC signals (rapidly changing current generates large back-EMF) while passing DC freely (no change, no opposition). The negative sign reflects Lenz's law: the induced EMF always opposes the change causing it."
  explanation: "Inductors are current-inertia devices — like mechanical inertia, they resist changes to the state (current) rather than the state itself. A massive object is hard to accelerate or decelerate but doesn't resist moving at constant velocity. An inductor is hard to ramp up or down but offers no resistance to steady current flow. This analogy makes the steady-state short-circuit behavior intuitive rather than surprising."
```

## Explainer

Faraday's law tells you that a changing magnetic flux through a circuit induces an EMF. Self-inductance turns this around and asks: what if the circuit's own current creates the flux? When current I flows through a coil, it generates a magnetic field, which threads through the coil's own turns as flux Φ. If I changes, Φ changes, and by Faraday's law an EMF is induced — in the same coil, opposing the change. **Self-inductance** L is defined as the proportionality constant between flux linkage and current: NΦ = LI. Differentiating, you get ε_L = −L dI/dt, where the negative sign (from Lenz's law, your prerequisite) ensures the induced EMF opposes the current change.

The solenoid is the prototype inductor. From Ampère's law you know the field inside a long solenoid is B = μ₀nI, where n = N/ℓ is the turns per unit length. The flux through each turn is BA = μ₀nIA. The flux linkage through all N turns is NΦ = N·μ₀nIA = μ₀n²ℓA·I. So L = μ₀N²A/ℓ. Notice that L depends entirely on geometry — it is larger for more turns (N²), larger cross-section, and shorter length. More turns means more flux per ampere, and the N² dependence comes from each extra turn both contributing to B and experiencing more flux.

The energy stored in an inductor has a direct parallel with capacitors. A capacitor stores energy U = ½CV² in the electric field; an inductor stores U = ½LI² in the **magnetic field**. You can derive this by calculating the work done against the back-EMF while ramping current from 0 to I: dW = −ε_L·I dt = L I dI, which integrates to ½LI². This energy lives in the magnetic field — for the solenoid, you can show it equals (B²/2μ₀)·volume, the magnetic field energy density times the volume. This is the magnetic analog of the electric field energy density ε₀E²/2.

The behavioral contrast with capacitors is the key to circuit intuition. A capacitor resists changes in voltage (it takes time to charge/discharge); an inductor resists changes in current (it fights any ramp-up or ramp-down of I). At DC steady state, a capacitor is an open circuit (no current flows once charged) while an ideal inductor is a short circuit (no back-EMF once dI/dt = 0). At high frequency, these roles are reversed — capacitors pass current freely, inductors block it. This complementary behavior is why LC circuits oscillate, and why inductors and capacitors appear together in filters and resonators.
