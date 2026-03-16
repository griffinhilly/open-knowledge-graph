---
id: biot-savart-law-applications
title: 'Biot-Savart Law: Calculating Magnetic Fields'
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: magnetic-field-definition
  type: hard
- id: line-integrals-vector-fields
  type: hard
builds-toward:
- ampere-law-applications
tags:
- biot-savart
- integration
- current-source
stage: formal-systems
status: draft
---

# Biot-Savart Law: Calculating Magnetic Fields

## Core Idea
The Biot-Savart law gives magnetic field from current elements: dB = (μ₀/4π) I(dL × r̂)/r². Integrating over a current distribution yields total field. For complex geometries, this approach is systematic but often computationally intensive.

## Explainer

The Biot-Savart law is the magnetic analogue of Coulomb's law for electric fields. Just as Coulomb's law tells you the electric field contribution from a small charge element dq, the Biot-Savart law tells you the magnetic field contribution **dB** from a small current element I dL⃗. The key formula is dB⃗ = (μ₀/4π) · I(dL⃗ × r̂)/r², where r̂ is the unit vector pointing from the source element to the field point, and r is the distance between them. Like Coulomb's law, the field falls off as 1/r²; unlike Coulomb's law, the direction is determined by a cross product, so the geometry of the current matters as much as the distance.

The cross product dL⃗ × r̂ is where most difficulty enters. For a current element pointing in the x-direction and a field point in the x-y plane, the cross product gives a field pointing in the z-direction — the magnetic field curls around the current, never pointing along it. To use the law, you must set up coordinates, express the current element dL⃗ and the displacement vector r in terms of an integration variable (typically position along the wire), then evaluate the integral. For a long straight wire, this integration yields the familiar result B = μ₀I/2πd, where d is the perpendicular distance from the wire.

For a **circular current loop**, Biot-Savart gives its most instructive result. By symmetry, all field-point components cancel except along the axis of the loop. Integrating around the loop, you find B = μ₀IR²/2(R²+z²)^(3/2) along the axis, where R is the loop radius and z is the axial distance. At large z, this falls as 1/z³ — faster than the 1/r² of a point charge — which anticipates the dipole field pattern you'll encounter in more advanced topics. The circular loop result is also the foundational building block for the solenoid: a solenoid is just many loops stacked together, and their axial fields add.

The Biot-Savart law is general and systematic, but often computationally intensive. For current distributions with high symmetry (infinite wire, infinite plane, toroid), **Ampère's law** is far more efficient — it uses the symmetry to avoid integration. Biot-Savart's power is precisely in the cases where symmetry is absent: a finite wire, an off-axis field, or an irregular loop. When Ampère's law doesn't apply because the geometry lacks symmetry, Biot-Savart is your tool. Working through both methods for the infinite wire — integrating with Biot-Savart, then closing an Amperian loop — builds the deepest understanding of how the same physical law can appear in two very different computational forms.
