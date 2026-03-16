---
id: self-inductance-of-circuits
title: Self-Inductance and Energy Storage
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: inductance-and-inductors
  type: hard
- id: faraday-law-of-induction
  type: hard
builds-toward:
- rc-circuits
- lc-and-rlc-circuits
tags:
- inductance
- self-inductance
- EMF
stage: formal-systems
status: draft
---

# Self-Inductance and Energy Storage

## Core Idea
Self-inductance L is the proportionality between current and magnetic flux: Φ = LI. The self-induced EMF is ε = -L(dI/dt), opposing current changes (Lenz's law). Self-inductance depends on circuit geometry: L = μ₀N²A/l for a solenoid. The circuit stores magnetic energy: U = (1/2)LI². Inductors are essential in filters, oscillators, and power supplies.

## How It's Best Learned
Calculate inductance of simple geometries by integrating magnetic flux. Measure self-induced EMF when current changes. Verify energy storage formula from the magnetic field.

## Common Misconceptions
- Self-inductance creates constant opposing force (it is proportional to rate of change of current).
- Self-inductance and inductance in general are identical (self-inductance is one type; mutual inductance is another).
- Inductors store energy 'like batteries' (they store it temporarily in the magnetic field).

## Explainer

You know from Faraday's law that a changing magnetic flux induces an EMF. Now consider what happens inside a circuit carrying changing current: the current itself creates a magnetic field, and as that current changes, the flux through the circuit's own area changes. The result is an EMF induced by the circuit on *itself* — this is **self-inductance**. The self-inductance L is defined by Φ_B = LI: it is the proportionality constant between the current and the total magnetic flux the circuit threads through itself. It depends entirely on geometry — the size, shape, and number of turns of the conductor — not on the current.

The **self-induced EMF** is ε = −L(dI/dt). This is Faraday's law applied to the circuit's own flux. The negative sign means the self-induced EMF *opposes* the current change: if you try to increase the current quickly, the inductor fights back with a back-EMF; if you try to decrease it, the inductor tries to sustain it. This is the electromagnetic analogue of mechanical inertia. A massive object resists changes to its velocity; an inductor resists changes to its current. The inductance L plays the same role as mass m in the analogy F = m(dv/dt) ↔ ε = L(dI/dt).

For a **solenoid** with N turns, cross-sectional area A, and length ℓ, the inductance is L = μ₀N²A/ℓ. This formula shows what geometrically amplifies inductance: more turns (N² dependence — doubling turns quadruples L), larger cross-section (more flux per unit current), and shorter length (fields are more concentrated). Practical inductors — the coiled components in filters, power supplies, and radios — exploit all three.

The energy stored in an inductor is U = (1/2)LI². This is the magnetic analogue of a capacitor's (1/2)CV². When you ramp up current in an inductor, you do work against the back-EMF; that work is stored in the magnetic field filling the inductor's volume. When current is interrupted — say by opening a switch — the inductor does not simply stop. It drives whatever current it can through whatever path is available, sometimes creating dangerous voltage spikes. The energy was real and stored in the field; it must go somewhere. This is why circuits with large inductors require protective flyback diodes or snubbers to dissipate the stored energy safely.
