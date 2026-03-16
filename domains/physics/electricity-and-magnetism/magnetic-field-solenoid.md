---
id: magnetic-field-solenoid
title: Magnetic Fields in Solenoids and Toroids
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: ampere-law-field
  type: hard
builds-toward:
- self-inductance
tags:
- solenoid
- toroid
- field
stage: formal-systems
status: draft
---

# Magnetic Fields in Solenoids and Toroids

## Core Idea
A solenoid with N turns, length ℓ, and cross-sectional area A produces a uniform field B = μ₀nI = μ₀NI/ℓ inside, and essentially zero outside (ideal solenoid). A toroid has field B = μ₀NI/(2πr) at radius r in the toroidal cross-section, zero outside. These geometries confine magnetic fields efficiently and are fundamental to transformers, electromagnets, and inductors.

## Explainer

From Ampère's law, you know that the line integral of B around any closed path equals μ₀ times the total current threading through that path: ∮B·dl = μ₀I_enc. The solenoid and toroid are the two canonical geometries where a clever choice of Amperian loop reduces this integral to a trivial calculation, much as a Gaussian sphere reduces Gauss's law to a single multiplication.

For a **solenoid** — a tightly wound helix of N turns, length ℓ — draw a rectangular Amperian loop with one long side inside the solenoid and one outside. Along the inside, B is uniform and parallel to the loop edge, contributing B·ℓ_side. Along the outside, B is essentially zero (the fields from opposite sides of the helix cancel for an ideal solenoid, and field lines form closed loops that spread out far from the solenoid). The two short sides contribute nothing because B is perpendicular to them. The total current threading the loop is I times the number of turns in the rectangle, which is n·ℓ_side where n = N/ℓ is the turn density. Setting B·ℓ_side = μ₀·n·ℓ_side·I gives B = μ₀nI. The field inside is **perfectly uniform** — independent of position along the axis — and the field outside is zero. This makes solenoids ideal field-generation devices for applications requiring a controlled, uniform magnetic field.

A **toroid** is a solenoid bent into a closed ring. Now the Amperian loop is a circle at radius r centered on the axis. By symmetry, B must be constant in magnitude and tangent to the circle everywhere. The enclosed current is N·I (all N turns thread through), so B·(2πr) = μ₀NI, giving B = μ₀NI/(2πr). The field is confined entirely within the toroidal volume and is not uniform — it varies as 1/r, being strongest at the inner radius. Outside the toroid, any Amperian circle encloses zero net current (every turn contributes both an inward and an outward threading as you go around), so B = 0 exactly. The complete confinement of the field is what makes toroids essential in transformers and inductors where stray fields would interfere with neighboring circuits.

The key conceptual thread is that these geometries convert the continuous current distribution into a problem with high symmetry, and symmetry is what makes Ampère's law calculationally tractable. Both results also reveal the solenoid and toroid as controlled magnetic field factories: the field inside scales linearly with n (or N) and I, making it easy to design a device with a specific target field by choosing the winding density and current. This linear control, combined with efficient field confinement, explains their ubiquity in inductors, magnetic resonance machines, and particle accelerators.
