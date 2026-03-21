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

## Questions

```yaml
- question: "Light travels from air (n = 1.0) into glass (n = 1.5) at a large angle. What happens?"
  type: multiple-choice
  options:
    - "Total internal reflection occurs if the angle exceeds the critical angle"
    - "The light refracts into the glass — TIR cannot occur here"
    - "The light is completely absorbed by the glass surface"
    - "TIR occurs because glass has a higher refractive index than air"
  answer: 1
  explanation: "Total internal reflection is only possible when light travels from a medium of higher refractive index to one of lower refractive index (denser to less-dense). Going from air (n=1.0) into glass (n=1.5) is the opposite direction — light is entering the denser medium. In this case, the refracted ray bends toward the normal, and no matter how large the incident angle, Snell's law always has a solution. TIR is geometrically impossible here. Option D names a real condition for TIR but gets the direction backwards."

- question: "Light in glass (n = 1.5) strikes the glass-air interface at the critical angle θc. What happens to the refracted ray?"
  type: multiple-choice
  options:
    - "The refracted ray enters the air at 45°"
    - "The refracted ray travels along the interface at 90° — it grazes the surface"
    - "There is no refracted ray — total internal reflection occurs at exactly θc"
    - "The refracted ray returns through the glass along the incident path"
  answer: 1
  explanation: "The critical angle is defined as the incident angle at which the refracted angle reaches exactly 90°. At θc = arcsin(n₂/n₁) = arcsin(1/1.5) ≈ 41.8°, Snell's law gives n₁ sin θc = n₂ sin 90° = n₂. The refracted ray runs along the interface — it grazes the surface. For angles just below θc, refraction still occurs (with large refracted angles close to 90°). TIR begins strictly above θc, not at it. At exactly θc, there is technically a refracted ray, but it has zero intensity in the normal direction."

- question: "Total internal reflection is only possible when light travels from a medium with a higher refractive index into a medium with a lower refractive index."
  type: true-false
  answer: true
  explanation: "TIR requires the refracted angle to exceed 90°, which Snell's law only allows when n₁ > n₂. If n₁ sin θ₁ = n₂ sin θ₂ and n₁ > n₂, then sin θ₂ = (n₁/n₂) sin θ₁ > sin θ₁. As θ₁ increases, θ₂ reaches 90° before θ₁ does, and beyond that, no real solution exists. When n₁ < n₂ (light going into the denser medium), sin θ₂ < sin θ₁ always, so θ₂ < θ₁ for all angles — the refracted ray always exists and TIR never occurs."

- question: "Total internal reflection reflects light with near-perfect efficiency — slightly less than 100% due to scattering and absorption losses in the medium."
  type: true-false
  answer: false
  explanation: "TIR is geometrically complete: exactly 100% of the incident energy is reflected back into the original medium. This is not 'near-perfect' — it is a mathematical consequence of Snell's law having no solution above the critical angle. No transmitted wave exists to carry energy into the second medium. This is fundamentally different from ordinary mirror reflection, which always involves some absorption. It is why optical fibers achieve such low signal loss and why TIR prisms are used instead of mirror coatings in precision optics."

- question: "Why is total internal reflection impossible when light travels from air into water, regardless of the incident angle?"
  type: short-answer
  answer: "TIR requires n₁ > n₂ — the light must be traveling from the denser medium into the less-dense one. Air has n ≈ 1.0 and water has n ≈ 1.33, so n_air < n_water. When light goes from air into water, it is entering the denser medium. Snell's law gives sin θ₂ = (n_air/n_water) sin θ₁ < sin θ₁, so the refracted angle is always smaller than the incident angle. The refracted ray always exists and bends toward the normal. There is no incident angle at which Snell's law fails to produce a solution."
  explanation: "The critical angle formula θc = arcsin(n₂/n₁) only makes sense when n₂ < n₁, because arcsin is only defined for arguments between −1 and 1. When n₂ > n₁, the argument exceeds 1 and no critical angle exists — confirming that TIR is impossible in this direction. The geometry is asymmetric: looking up from underwater you can see the entire outside world compressed into a cone (Snell's window), while light hitting the surface from below at a wide enough angle undergoes TIR back into the water."
```

## Explainer

You already know from Snell's law that light bends when it crosses from one medium to another, and that the bending depends on the ratio of refractive indices. You also know that a higher refractive index means light travels more slowly in that medium. Now consider what happens when light travels the other direction: from a slow medium (like glass or water) into a fast one (like air).

When light exits glass into air, Snell's law requires n₁ sin θ₁ = n₂ sin θ₂. Because n₁ > n₂, sin θ₂ must be larger than sin θ₁ — so the refracted ray bends *away* from the normal. As you increase the incident angle θ₁, the refracted angle θ₂ grows larger. At some point, θ₂ reaches 90°, meaning the refracted ray runs along the surface. That incident angle is the **critical angle**: θc = arcsin(n₂/n₁). Beyond this angle, Snell's law would require sin θ₂ > 1, which has no solution — there is simply no transmitted ray.

Instead, all the light bounces back into the original medium: **total internal reflection** (TIR). This is not ordinary reflection with some transmission — it is geometrically complete, with 100% of the energy reflected. No conventional mirror achieves this; even the best mirror absorbs a small fraction of incident light. TIR is only possible when light travels from a denser to a less dense medium and exceeds the critical angle.

The practical consequences are enormous. **Optical fibers** exploit TIR to carry light signals around bends with negligible loss: the glass core has a higher index than its surrounding cladding, so light launched at shallow angles bounces from wall to wall the entire length of the cable without escaping. Prisms in binoculars use TIR to fold the optical path compactly without a lossy mirror coating. Even the sparkle of a diamond traces to TIR — diamond has a very low critical angle (about 24°) that causes most light entering the stone to be internally reflected multiple times before exiting in a dazzling spray of directions.
