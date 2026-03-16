---
id: critical-angle-total-internal-reflection-optical
title: Critical Angle and Total Internal Reflection
domain: physics
course: waves-and-optics
prerequisites:
- id: refraction-and-snells-law
  type: hard
- id: refractive-index-material-property
  type: hard
builds-toward:
- total-internal-reflection
tags:
- critical-angle
- total-internal-reflection
- optical
stage: formal-systems
status: draft
---

# Critical Angle and Total Internal Reflection

## Core Idea
When light travels from a denser medium (higher n) to a less dense medium (lower n), total internal reflection occurs if the incident angle exceeds the critical angle θc = arcsin(n₂/n₁). At and beyond the critical angle, light is completely reflected back into the original medium with no refracted ray. This principle enables fiber optics and prism-based optical devices.

## Explainer

You already know from Snell's law that light bends when it crosses from one medium to another, and that the bending depends on the ratio of refractive indices. You also know that a higher refractive index means light travels more slowly in that medium. Now consider what happens when light travels the other direction: from a slow medium (like glass or water) into a fast one (like air).

When light exits glass into air, Snell's law requires n₁ sin θ₁ = n₂ sin θ₂. Because n₁ > n₂, sin θ₂ must be larger than sin θ₁ — so the refracted ray bends *away* from the normal. As you increase the incident angle θ₁, the refracted angle θ₂ grows larger. At some point, θ₂ reaches 90°, meaning the refracted ray runs along the surface. That incident angle is the **critical angle**: θc = arcsin(n₂/n₁). Beyond this angle, Snell's law would require sin θ₂ > 1, which has no solution — there is simply no transmitted ray.

Instead, all the light bounces back into the original medium: **total internal reflection** (TIR). This is not ordinary reflection with some transmission — it is geometrically complete, with 100% of the energy reflected. No conventional mirror achieves this; even the best mirror absorbs a small fraction of incident light. TIR is only possible when light travels from a denser to a less dense medium and exceeds the critical angle.

The practical consequences are enormous. **Optical fibers** exploit TIR to carry light signals around bends with negligible loss: the glass core has a higher index than its surrounding cladding, so light launched at shallow angles bounces from wall to wall the entire length of the cable without escaping. Prisms in binoculars use TIR to fold the optical path compactly without a lossy mirror coating. Even the sparkle of a diamond traces to TIR — diamond has a very low critical angle (about 24°) that causes most light entering the stone to be internally reflected multiple times before exiting in a dazzling spray of directions.
