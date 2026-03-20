---
id: snells-law
title: Snell's Law
domain: physics
course: waves-and-optics
prerequisites:
- id: refraction-intro
  type: hard
- id: right-triangle-trigonometry-intro
  type: hard
- id: sine-cosine-tangent-ratios
  type: soft
builds-toward:
- total-internal-reflection
- dispersion-and-prisms
- thin-film-interference
tags:
- Snell's law
- index of refraction
- angles
- quantitative refraction
stage: formal-systems
status: validated
---

# Snell's Law

## Core Idea
Snell's law gives the quantitative relationship between incident and refracted angles at a boundary: n₁sinθ₁ = n₂sinθ₂. Here n₁ and n₂ are the refractive indices of the two media, and the angles are measured from the normal. When light moves from a lower-index medium to a higher-index medium, it bends toward the normal (θ₂ < θ₁). Snell's law is derived from the requirement that frequency is preserved at the boundary while speed changes.

## How It's Best Learned
Trace a light ray through a glass block with known index (~1.5), measure both angles, and verify n₁sinθ₁ = n₂sinθ₂. Then solve a progression of problems: air-to-water, water-to-glass, and multi-layer systems.

## Common Misconceptions
- Students sometimes swap n₁ and n₂ or θ₁ and θ₂; draw a clear diagram labeling which side is which before substituting.
- Snell's law applies to the transmitted (refracted) ray, not the reflected ray.

## Questions

```yaml
- question: "Light travels from air (n = 1.00) into water (n = 1.33) at an incident angle of 30° from the normal. What is the approximate refracted angle in water?"
  type: multiple-choice
  options: ["22°", "30°", "42°", "48°"]
  answer: 0
  explanation: "Applying Snell's law: n₁ sinθ₁ = n₂ sinθ₂ → (1.00)(sin 30°) = (1.33)(sin θ₂) → sin θ₂ = 0.5/1.33 ≈ 0.376 → θ₂ ≈ 22°. Because light enters a denser medium (higher n), it bends toward the normal, so the refracted angle is smaller than the incident angle."

- question: "When light passes from air into glass (higher index of refraction), it bends away from the normal."
  type: true-false
  answer: false
  explanation: "Light bends toward the normal when entering a medium with a higher index of refraction. A higher index means a slower wave speed. Because the frequency is fixed (it doesn't change at the boundary), the wavelength shortens, and the wavefront pivots toward the normal. Bending away from the normal happens only when going from a higher-index medium back to a lower-index one."

- question: "Why does the index of refraction determine how much light bends at a boundary, and what does a higher index tell you about light's speed in that medium?"
  type: short-answer
  answer: "The index of refraction n = c/v, so a higher n means light travels more slowly in that medium. At a boundary, frequency is preserved but speed changes, forcing the wavelength and direction to change. The greater the speed difference (larger Δn), the more the ray bends."
  explanation: "Snell's law is fundamentally a consequence of wave physics: the component of the wave's phase velocity parallel to the boundary must be continuous across it. This forces n₁ sinθ₁ = n₂ sinθ₂. A medium with a high refractive index slows light dramatically, causing a large bend for even moderate incident angles."
```

## Explainer

From your introduction to refraction, you know that light changes direction when it crosses a boundary between two media. Snell's law gives you the precise quantitative rule for *how much* it bends: n₁ sinθ₁ = n₂ sinθ₂. To use it correctly, you need to be clear on two things — what n means and how to measure the angles.

The **index of refraction** n = c/v tells you how much slower light travels in a medium compared to a vacuum. Air has n ≈ 1.00 (light barely slows down), water has n ≈ 1.33, and glass has n ≈ 1.5. The higher the index, the slower the speed. Angles in Snell's law are always measured from the **normal** — the imaginary line perpendicular to the surface at the point of contact. Drawing this normal explicitly in every diagram is the single most reliable way to avoid sign and labeling errors.

The bending direction follows a simple rule: when light enters a *denser* medium (higher n), it bends *toward* the normal, so the transmitted angle is smaller than the incident angle. When light enters a *less dense* medium (lower n), it bends *away* from the normal. You can verify this directly from the equation: if n₂ > n₁, then sinθ₂ < sinθ₁, so θ₂ < θ₁. The physical reason is that light slows down in the denser medium, and the wavefront has to pivot — like a row of marching soldiers where one end hits mud before the other.

To solve Snell's law problems, the workflow is straightforward: (1) draw the boundary and the normal, (2) label n₁, n₂, θ₁ on your diagram, (3) substitute into n₁ sinθ₁ = n₂ sinθ₂ and solve for the unknown. The most common mistakes are swapping which side is 1 and which is 2, and forgetting that the angles are measured from the normal rather than the surface itself.

Snell's law only describes the *refracted* ray. There is always a reflected ray as well (at the same angle as incidence, on the same side of the boundary), but that is governed by the law of reflection — a separate rule. A consequence of Snell's law you will explore soon is **total internal reflection**: when light tries to exit a denser medium at a steep enough angle, sinθ₂ would have to exceed 1, which is impossible, so no refracted ray exists and all the light reflects back internally. This is the principle behind optical fibers.
