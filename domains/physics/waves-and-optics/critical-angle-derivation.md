---
id: critical-angle-derivation
title: Critical Angle and Total Internal Reflection Derivation
domain: physics
course: waves-and-optics
prerequisites:
- id: total-internal-reflection
  type: soft
- id: snells-law
  type: hard
builds-toward:
- fiber-optics-and-waveguides
tags:
- total-internal-reflection
- critical-angle
stage: formal-systems
status: draft
---

# Critical Angle and Total Internal Reflection Derivation

## Core Idea
When light travels from a denser to less dense medium, total internal reflection occurs when the incident angle exceeds the critical angle θc = arcsin(n₂/n₁). At this angle, the refracted ray would be 90°; beyond it, all light reflects. This phenomenon is essential for fiber optics and optical waveguides.

## Explainer

The critical angle derivation is a direct consequence of Snell's law pushed to its logical limit. Recall Snell's law from your prerequisite work: n₁ sin θ₁ = n₂ sin θ₂. When light moves from a denser medium (higher n₁, like glass) into a less dense one (lower n₂, like air), the refracted ray bends away from the normal — θ₂ > θ₁. As you increase the incident angle θ₁, the refracted angle θ₂ grows faster. The question is: what happens when θ₂ tries to reach 90°?

At θ₂ = 90°, the refracted ray would travel exactly along the interface — it skims the surface and never actually enters the second medium. Plugging this into Snell's law: n₁ sin θc = n₂ sin 90° = n₂. Solving for the **critical angle**: θc = arcsin(n₂/n₁). This is the threshold. At angles below θc, light partially refracts and partially reflects (as you know from normal refraction). At angles above θc, Snell's law has no solution — there is no refracted ray — and all the light reflects back into the first medium. This is **total internal reflection**.

The key intuition is that total internal reflection is not a special phenomenon — it is simply what happens when refraction becomes geometrically impossible. The math doesn't give you a valid θ₂ above θc because sin θ₂ would need to exceed 1, which has no physical solution. Nature's response is to reflect all the light instead. Think of it as the boundary refusing to let light through.

The practical consequence is striking: light trapped inside a glass fiber by total internal reflection can travel enormous distances with almost no loss, because it never escapes the sides of the fiber. Every bend in a fiber-optic cable maintains the critical angle condition, keeping the light bouncing internally from wall to wall. The same principle explains why a swimming pool bottom looks silvery when you look at it from a shallow angle underwater, and why diamonds are cut at angles that maximize total internal reflection — trapping light inside until it exits through the top face.
