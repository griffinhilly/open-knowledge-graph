---
id: biot-savart-field
title: Magnetic Field from Biot-Savart Law
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: magnetic-torque-dipole
  type: soft
builds-toward:
- ampere-law-field
tags:
- biot-savart
- field
- current
stage: formal-systems
status: draft
---

# Magnetic Field from Biot-Savart Law

## Core Idea
The Biot-Savart law gives magnetic field from a current element: dB⃗ = (μ₀/4π) I (d⃗ℓ × r̂) / r². Total field: B⃗ = (μ₀/4π) I ∫ (d⃗ℓ × r̂) / r². For an infinite straight wire: B = μ₀I/(2πr). For a circular loop on axis: B = μ₀IR²/[2(R² + z²)^(3/2)]. This fundamental law applies to all current distributions.

## Explainer

The Biot-Savart law is the magnetic analog of Coulomb's law: it gives the magnetic field contributed by each tiny piece of current-carrying wire. Just as Coulomb's law says a point charge contributes a field dE pointing radially outward, Biot-Savart says a current element Idℓ contributes a dB pointing *perpendicular* to both the current direction and the line from the element to the field point. The cross product dℓ × r̂ encodes this geometry: if you point your fingers in the direction of current and curl them toward r̂, your thumb points in the direction of dB. This perpendicularity is the magnetic signature — magnetic fields always curl around currents rather than pointing radially outward like electric fields from charges.

For an infinite straight wire, every element contributes a dB that circles the wire, and integration yields B = μ₀I/(2πr). This follows from the translational symmetry of the infinite wire: since the field cannot vary along the axis, it can only depend on the perpendicular distance r, and it wraps in concentric circles. For a circular loop, the on-axis result B = μ₀IR²/[2(R² + z²)^(3/2)] falls off more steeply at large z — it behaves like a **magnetic dipole** far from the loop, exactly analogous to an electric dipole's field, because contributions from opposite sides of the loop partially cancel off-axis.

The key to applying Biot-Savart is a systematic integration strategy. Choose a coordinate along the wire, express r (the displacement from each source element to your field point) as a function of that coordinate, evaluate the cross product, and integrate. For symmetric geometries, use symmetry first: for a straight wire, every element above and below the perpendicular plane contributes dB in the same circling sense, so there is no cancellation and only the magnitude integral remains. Getting the geometry of dℓ × r̂ right before integrating is the most common point of difficulty.

The deeper lesson from Biot-Savart is that **magnetic fields have no sources** — they form closed loops around currents, never beginning or ending on anything. This contrasts with electric fields, which begin on positive charges and end on negative charges. Mathematically, this means ∇·B = 0 everywhere, a symmetry you will formalize when you study Maxwell's equations in differential form. Ampere's law (the next topic) encodes the same physics more efficiently for symmetric current distributions, just as Gauss's law simplifies Coulomb for symmetric charge distributions.
