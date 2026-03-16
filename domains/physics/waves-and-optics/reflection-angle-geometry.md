---
id: reflection-angle-geometry
title: Law of Reflection and Angle Relationships
domain: physics
course: waves-and-optics
prerequisites:
- id: reflection-and-law-of-reflection
  type: soft
builds-toward:
- concave-convex-mirror-image
tags:
- reflection
- optics
- geometry
stage: formal-systems
status: draft
---

# Law of Reflection and Angle Relationships

## Core Idea
The law of reflection states that the angle of incidence equals the angle of reflection, both measured from the normal to the surface. This law applies to all types of waves and surfaces, whether smooth or rough (rough surfaces scatter in many directions, each obeying the local reflection law). Reflection is the foundation of mirror optics.

## Explainer

The law of reflection is deceptively simple, but the geometry it implies is rich. The single rule — **angle of incidence equals angle of reflection**, both measured from the normal — contains everything you need to trace where reflected rays go. The **normal** is an imaginary line perpendicular to the surface at the point of contact. Measuring angles from the normal (not from the surface itself) is what makes the law universally applicable, regardless of how the surface is tilted.

To build intuition, imagine a ball bouncing off a wall: it arrives at some angle and leaves at the symmetric angle on the other side. Light behaves the same way — it is not that the surface "knows" where the light came from; rather, it is that the wave's interaction with the surface enforces this symmetry. The incoming and outgoing rays, along with the normal, always lie in the same plane. This coplanarity is the geometric constraint that makes image formation in mirrors predictable.

The distinction between **specular reflection** (smooth surface) and **diffuse reflection** (rough surface) comes down to what "smooth" means at the scale of the wavelength. A mirror is smooth relative to visible light wavelengths (~500 nm), so all rays reflecting from nearby points on the surface have nearly parallel normals — they all obey the law of reflection consistently, preserving the geometry of the incoming beam. A sheet of white paper is microscopically rough: each tiny patch has its own local normal pointing in a random direction, so reflected rays scatter in all directions. Each patch still obeys θi = θr perfectly; the overall diffuse appearance is just the statistical average of many differently-oriented reflections.

A practical application: if you tilt a flat mirror by an angle α, the reflected beam rotates by 2α. This factor of two arises because rotating the mirror changes the normal direction by α, which shifts both the incidence and reflection angles by α — a total deflection of 2α. Laser galvanometers and laser scanning systems exploit this amplification to sweep beams rapidly across large angles with small physical mirror movements. Whenever you work with mirror systems, the angle-doubling rule is your first tool for predicting where reflected rays end up.
