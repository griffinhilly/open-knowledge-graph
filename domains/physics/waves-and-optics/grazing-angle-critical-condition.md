---
id: grazing-angle-critical-condition
title: Total Internal Reflection and the Critical Angle
domain: physics
course: waves-and-optics
prerequisites:
- id: refraction-interface-snell-relation
  type: hard
- id: combined-optical-system-magnification
  type: soft
tags:
- refraction
- tir
- optics
stage: advanced
status: validated
---
# Total Internal Reflection and the Critical Angle

## Core Idea
When light travels from a denser to a less dense medium (e.g., glass to air), Snell's law predicts a refraction angle beyond 90° at large incidence angles. This is impossible, so instead total internal reflection occurs for incident angles exceeding the critical angle θ_c = arcsin(n₂/n₁). Optical fibers rely on TIR to guide light; the critical angle also explains why underwater objects appear to reflect light from below the water surface.

## Common Misconceptions
Total internal reflection requires light to travel from a denser to less dense medium—it does not occur for the opposite direction.

## Questions

```yaml
- question: "Why can total internal reflection NOT occur when light travels from air (n = 1.0) into glass (n = 1.5)?"
  type: multiple-choice
  options:
    - "Glass absorbs all light at large incidence angles, preventing a reflected beam from forming"
    - "When light enters a denser medium, the refracted angle is always smaller than the incident angle, so there is always a valid refracted ray regardless of the incidence angle"
    - "Air has a higher refractive index than glass at large angles due to dispersion"
    - "Snell's law breaks down at the air-glass interface for angles above 45°"
  answer: 1
  explanation: "Snell's law gives sinθ₂ = (n₁/n₂)sinθ₁. Going from air to glass, n₁/n₂ = 1.0/1.5 < 1, so sinθ₂ < sinθ₁ always — the refracted ray bends toward the normal. No matter how large θ₁ gets (up to 90°), sinθ₂ can never exceed n₁/n₂ < 1, so θ₂ always has a valid solution. Total internal reflection requires that sinθ₂ would need to exceed 1 — and this can only happen when n₁/n₂ > 1, i.e., going from denser to less dense medium."

- question: "Diamond has a refractive index of about 2.4; glass has about 1.5. For TIR going into air (n = 1.0), how do their critical angles compare, and why?"
  type: multiple-choice
  options:
    - "Diamond has a larger critical angle than glass, since diamond is denser and holds light more strongly"
    - "Diamond has a smaller critical angle than glass, since the larger index contrast means TIR activates at shallower incidence angles"
    - "Both have the same critical angle, since the external medium (air) is the same in both cases"
    - "The critical angle is undefined for diamond because its high density prevents TIR"
  answer: 1
  explanation: "The critical angle formula is θ_c = arcsin(n₂/n₁). For glass-to-air: θ_c = arcsin(1.0/1.5) ≈ 42°. For diamond-to-air: θ_c = arcsin(1.0/2.4) ≈ 24°. Diamond's larger index contrast produces a smaller critical angle — TIR kicks in at shallower incidence, trapping light more aggressively. This is why diamonds are cut with many facets at specific angles: most light entering the top face undergoes multiple total internal reflections before exiting, creating brilliance. A larger n₁/n₂ ratio always gives a smaller critical angle."

- question: "Total internal reflection is simply very strong partial reflection — a small fraction of light still crosses into the less-dense medium when the incidence angle exceeds the critical angle."
  type: true-false
  answer: false
  explanation: "The word 'total' is essential and accurate. Above the critical angle, Snell's law has no real solution for the refracted angle — sinθ₂ would exceed 1, which is impossible for a propagating ray. The electromagnetic boundary conditions require that 100% of the energy is reflected back into the denser medium. No propagating wave exists in the less-dense medium (there is an evanescent field that decays exponentially, but it carries no net energy away). This perfect reflection is what makes optical fibers lossless at the core-cladding interface."

- question: "An optical fiber guides light by maintaining total internal reflection at the interface between the fiber core (higher n) and the surrounding cladding (lower n)."
  type: true-false
  answer: true
  explanation: "This is the operating principle of optical fiber communication. The fiber core has a slightly higher refractive index than the cladding. Light entering within the acceptance cone (angles steep enough to exceed the critical angle at the core-cladding wall) undergoes repeated TIR at every bounce and propagates along the fiber without loss to the surroundings. The light can travel kilometers around bends and curves as long as the angle condition is maintained at every reflection point."

- question: "Explain using Snell's law why a critical angle must exist when light travels from a denser to a less dense medium, and what physically happens when the incidence angle exceeds it."
  type: short-answer
  answer: "Snell's law gives sinθ₂ = (n₁/n₂)sinθ₁. When n₁ > n₂ (denser to less dense), the ratio n₁/n₂ > 1, so sinθ₂ > sinθ₁ — the refracted ray bends away from the normal. As θ₁ increases, sinθ₂ = (n₁/n₂)sinθ₁ eventually reaches 1 when sinθ₁ = n₂/n₁, giving θ₂ = 90°: the refracted ray skims along the interface. This defines the critical angle θ_c = arcsin(n₂/n₁). For θ₁ > θ_c, sinθ₂ would exceed 1 — no real refracted angle exists. Electromagnetic boundary conditions then require 100% of the light to be reflected back into the denser medium: total internal reflection."
  explanation: "The evanescent wave deserves mention for completeness: even above the critical angle, Maxwell's equations predict an exponentially decaying field on the less-dense side. It carries no net energy away but can be 'frustrated' — if a second denser medium is brought very close, some light tunnels through, a phenomenon called frustrated TIR or optical tunneling."
```

## Explainer

You already know Snell's law: n₁ sinθ₁ = n₂ sinθ₂. When light travels from a less dense medium into a denser one (say, air into glass), sinθ₂ = (n₁/n₂)sinθ₁, and because n₁/n₂ < 1, the refracted angle is always smaller than the incident angle — light bends toward the normal. Total internal reflection cannot happen in this direction, no matter how steep the angle, because the refracted ray always has somewhere to go.

Now reverse the setup: light inside glass (n₁ = 1.5) heading toward air (n₂ = 1.0). Snell's law gives sinθ₂ = (n₁/n₂)sinθ₁ = 1.5 sinθ₁. For small incident angles this is fine — the refracted ray exits at a larger angle than it entered. But as θ₁ increases, sinθ₂ = 1.5 sinθ₁ eventually reaches 1.0, meaning θ₂ = 90°. The refracted ray skims along the interface rather than exiting. This incident angle is the **critical angle**: θ_c = arcsin(n₂/n₁). Push θ₁ even slightly past θ_c and sinθ₂ would need to exceed 1, which is impossible — there is no refracted ray at all. Instead, 100% of the light is reflected back into the denser medium.

This is not partial reflection — it is *total* internal reflection. No energy escapes into the less-dense medium. Optical fibers exploit exactly this: a glass or plastic core with refractive index n₁ is surrounded by a cladding with slightly lower index n₂. As long as the light ray's angle with the fiber axis stays within the acceptance cone (equivalently, the angle at the core-cladding wall exceeds θ_c), the light bounces repeatedly off the wall and propagates along the fiber without loss to the surroundings. A fiber can carry a signal around corners and over kilometers because the critical angle condition is maintained at every reflection.

The **critical angle** formula θ_c = arcsin(n₂/n₁) is worth building intuition around. The closer n₂ is to n₁ — the more similar the two media — the larger the critical angle, meaning TIR only kicks in at steep incidence. The larger the contrast (small n₂/n₁ ratio), the smaller the critical angle, meaning TIR activates at shallower angles and light is trapped more easily. This is why diamond, with a very high refractive index (~2.4), has a small critical angle (~24°), trapping most entering light through multiple internal reflections before it finally exits — the origin of a diamond's brilliance.
