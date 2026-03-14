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
