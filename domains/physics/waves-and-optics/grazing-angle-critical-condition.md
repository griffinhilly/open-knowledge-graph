---
id: grazing-angle-critical-condition
title: Total Internal Reflection and the Critical Angle
domain: physics
course: waves-and-optics
prerequisites:
- id: refraction-interface-snell-relation
  type: hard
tags:
- refraction
- tir
- optics
stage: advanced
status: draft
---

# Total Internal Reflection and the Critical Angle

## Core Idea
When light travels from a denser to a less dense medium (e.g., glass to air), Snell's law predicts a refraction angle beyond 90° at large incidence angles. This is impossible, so instead total internal reflection occurs for incident angles exceeding the critical angle θ_c = arcsin(n₂/n₁). Optical fibers rely on TIR to guide light; the critical angle also explains why underwater objects appear to reflect light from below the water surface.

## Common Misconceptions
Total internal reflection requires light to travel from a denser to less dense medium—it does not occur for the opposite direction.

## Explainer

You already know Snell's law: n₁ sinθ₁ = n₂ sinθ₂. When light travels from a less dense medium into a denser one (say, air into glass), sinθ₂ = (n₁/n₂)sinθ₁, and because n₁/n₂ < 1, the refracted angle is always smaller than the incident angle — light bends toward the normal. Total internal reflection cannot happen in this direction, no matter how steep the angle, because the refracted ray always has somewhere to go.

Now reverse the setup: light inside glass (n₁ = 1.5) heading toward air (n₂ = 1.0). Snell's law gives sinθ₂ = (n₁/n₂)sinθ₁ = 1.5 sinθ₁. For small incident angles this is fine — the refracted ray exits at a larger angle than it entered. But as θ₁ increases, sinθ₂ = 1.5 sinθ₁ eventually reaches 1.0, meaning θ₂ = 90°. The refracted ray skims along the interface rather than exiting. This incident angle is the **critical angle**: θ_c = arcsin(n₂/n₁). Push θ₁ even slightly past θ_c and sinθ₂ would need to exceed 1, which is impossible — there is no refracted ray at all. Instead, 100% of the light is reflected back into the denser medium.

This is not partial reflection — it is *total* internal reflection. No energy escapes into the less-dense medium. Optical fibers exploit exactly this: a glass or plastic core with refractive index n₁ is surrounded by a cladding with slightly lower index n₂. As long as the light ray's angle with the fiber axis stays within the acceptance cone (equivalently, the angle at the core-cladding wall exceeds θ_c), the light bounces repeatedly off the wall and propagates along the fiber without loss to the surroundings. A fiber can carry a signal around corners and over kilometers because the critical angle condition is maintained at every reflection.

The **critical angle** formula θ_c = arcsin(n₂/n₁) is worth building intuition around. The closer n₂ is to n₁ — the more similar the two media — the larger the critical angle, meaning TIR only kicks in at steep incidence. The larger the contrast (small n₂/n₁ ratio), the smaller the critical angle, meaning TIR activates at shallower angles and light is trapped more easily. This is why diamond, with a very high refractive index (~2.4), has a small critical angle (~24°), trapping most entering light through multiple internal reflections before it finally exits — the origin of a diamond's brilliance.
