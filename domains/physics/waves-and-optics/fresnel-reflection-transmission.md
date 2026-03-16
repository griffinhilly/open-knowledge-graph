---
id: fresnel-reflection-transmission
title: 'Fresnel Equations: Reflection and Transmission at Interfaces'
domain: physics
course: waves-and-optics
prerequisites:
- id: snells-law
  type: hard
- id: electromagnetic-waves
  type: soft
builds-toward:
- total-internal-reflection
- thin-film-interference
tags:
- fresnel-equations
- reflection
- transmission
stage: formal-systems
status: draft
---

# Fresnel Equations: Reflection and Transmission at Interfaces

## Core Idea
Fresnel equations describe the amplitude reflection and transmission coefficients for electromagnetic waves at a dielectric interface, accounting for polarization. They explain why reflection depends on angle of incidence, polarization direction, and the refractive index ratio between media.

## Explainer

Snell's law told you *where* light goes at an interface — how the angle changes based on the refractive index ratio. But Snell's law says nothing about *how much* light reflects versus transmits. That is what the Fresnel equations answer. When light hits a glass surface at normal incidence (straight on), roughly 4% reflects and 96% transmits. This partial reflection happens at every dielectric interface, and the Fresnel equations tell you exactly what fraction reflects and transmits as a function of the angle of incidence, the refractive indices, and — crucially — the **polarization** of the light.

Polarization refers to the direction in which the electric field of the light wave oscillates. The Fresnel equations treat two orthogonal polarization cases separately. **s-polarization** (also called TE, for transverse electric) has its electric field oscillating perpendicular to the plane of incidence. **p-polarization** (also called TM, for transverse magnetic) has its electric field oscillating parallel to the plane of incidence. These two cases behave very differently as the angle of incidence changes. For s-polarized light, reflectance increases smoothly from its normal-incidence value toward 100% as the angle approaches 90°. For p-polarized light, something remarkable happens: reflectance first drops to zero at a special angle, then rises back to 100%.

This special angle where p-polarized reflectance goes to zero is **Brewster's angle** (θ_B = arctan(n₂/n₁)). At this angle, the reflected and refracted rays are exactly 90° apart, and the geometry of how oscillating dipoles radiate means p-polarized light cannot reflect. This is why polarizing sunglasses reduce glare: sunlight reflected off a flat road or water surface is preferentially s-polarized near Brewster's angle, and the glasses' vertical polarizer blocks it. The phenomenon has a clean geometric explanation, but the Fresnel equations predict it with mathematical precision.

The Fresnel equations also explain why anti-reflection coatings on glasses and camera lenses work: thin films create destructive interference between reflections from two surfaces, canceling the ~4% reflective loss at each glass boundary. The same physics underlies fiber optics — cables are designed so that light hits the glass-air boundary beyond the critical angle (total internal reflection), and the Fresnel amplitude coefficients go to zero for transmitted light. Starting from Snell's law and the wave behavior of electromagnetic fields, the Fresnel equations are the complete quantitative description of what happens at every optical interface.
