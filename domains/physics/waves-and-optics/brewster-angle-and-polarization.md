---
id: brewster-angle-and-polarization
title: Brewster's Angle and Polarization by Reflection
domain: physics
course: waves-and-optics
prerequisites:
- id: refraction-and-snells-law
  type: hard
builds-toward:
- polarization-of-light
tags:
- brewster-angle
- polarization
- reflection
stage: formal-systems
status: draft
---

# Brewster's Angle and Polarization by Reflection

## Core Idea
At Brewster's angle θB = arctan(n₂/n₁), light reflected from a dielectric interface is completely polarized perpendicular to the plane of incidence (s-polarized). Light in the plane of incidence (p-polarized) is fully transmitted, with no reflection. This effect is exploited to eliminate reflections using polarizers at Brewster's angle.

## Explainer

From Snell's law — your prerequisite — you know that when light crosses from one medium to another with different refractive indices, both a reflected ray and a refracted ray are produced, and the angles are governed by n₁sin(θ₁) = n₂sin(θ₂). What Brewster's angle adds is a special geometric condition: there exists a specific angle of incidence where the reflected and refracted rays are exactly perpendicular to each other, separated by 90°. At that angle, something remarkable happens to polarization.

To understand why, think about how electromagnetic waves work. Light is a transverse wave: the electric field oscillates perpendicular to the direction of propagation. The **p-polarization** component is the part of the electric field oscillating in the **plane of incidence** (the plane containing the incoming ray and the surface normal). The **s-polarization** component oscillates perpendicular to that plane. When the reflected and refracted rays are at 90° to each other, the oscillating dipoles that would re-radiate the p-component into the reflected direction cannot do so — a dipole doesn't radiate along its own axis. So all of the p-polarized light passes through, and only s-polarized light is reflected.

The formula θB = arctan(n₂/n₁) comes directly from combining Snell's law with this 90° condition. If θB + θᵣ = 90° (reflected and refracted rays perpendicular), and Snell's law says n₁sin(θB) = n₂sin(θᵣ) = n₂sin(90° − θB) = n₂cos(θB), then dividing both sides gives tan(θB) = n₂/n₁. For light going from air (n₁ ≈ 1) into glass (n₂ ≈ 1.5), Brewster's angle is arctan(1.5) ≈ 56°. The reflected beam at that angle is 100% s-polarized — completely linearly polarized.

This effect has practical consequences you can observe directly. Glare from a wet road or the surface of water is predominantly s-polarized (horizontal). **Polarized sunglasses** work by blocking s-polarized light, which is why they dramatically cut glare from horizontal surfaces. Photographers use **polarizing filters** to suppress reflections from windows and water, making them transparent or revealing what lies beneath. Laser systems use **Brewster windows** — glass plates tilted at Brewster's angle — so that p-polarized light passes through with zero reflection loss, avoiding the ~4% loss that would occur at each surface at normal incidence.
