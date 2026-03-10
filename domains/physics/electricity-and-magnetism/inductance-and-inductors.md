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
status: draft
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
