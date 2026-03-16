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

## Explainer

Faraday's law tells you that a changing magnetic flux through a circuit induces an EMF. Self-inductance turns this around and asks: what if the circuit's own current creates the flux? When current I flows through a coil, it generates a magnetic field, which threads through the coil's own turns as flux Φ. If I changes, Φ changes, and by Faraday's law an EMF is induced — in the same coil, opposing the change. **Self-inductance** L is defined as the proportionality constant between flux linkage and current: NΦ = LI. Differentiating, you get ε_L = −L dI/dt, where the negative sign (from Lenz's law, your prerequisite) ensures the induced EMF opposes the current change.

The solenoid is the prototype inductor. From Ampère's law you know the field inside a long solenoid is B = μ₀nI, where n = N/ℓ is the turns per unit length. The flux through each turn is BA = μ₀nIA. The flux linkage through all N turns is NΦ = N·μ₀nIA = μ₀n²ℓA·I. So L = μ₀N²A/ℓ. Notice that L depends entirely on geometry — it is larger for more turns (N²), larger cross-section, and shorter length. More turns means more flux per ampere, and the N² dependence comes from each extra turn both contributing to B and experiencing more flux.

The energy stored in an inductor has a direct parallel with capacitors. A capacitor stores energy U = ½CV² in the electric field; an inductor stores U = ½LI² in the **magnetic field**. You can derive this by calculating the work done against the back-EMF while ramping current from 0 to I: dW = −ε_L·I dt = L I dI, which integrates to ½LI². This energy lives in the magnetic field — for the solenoid, you can show it equals (B²/2μ₀)·volume, the magnetic field energy density times the volume. This is the magnetic analog of the electric field energy density ε₀E²/2.

The behavioral contrast with capacitors is the key to circuit intuition. A capacitor resists changes in voltage (it takes time to charge/discharge); an inductor resists changes in current (it fights any ramp-up or ramp-down of I). At DC steady state, a capacitor is an open circuit (no current flows once charged) while an ideal inductor is a short circuit (no back-EMF once dI/dt = 0). At high frequency, these roles are reversed — capacitors pass current freely, inductors block it. This complementary behavior is why LC circuits oscillate, and why inductors and capacitors appear together in filters and resonators.
