---
id: malus-law-derivation
title: 'Malus''s Law: Derivation and Applications'
domain: physics
course: waves-and-optics
prerequisites:
- id: malus-law
  type: soft
- id: polarization-linear-production
  type: hard
builds-toward:
- wave-plates-quarter-half-wave
tags:
- malus-law
- polarization
- intensity-transmission
stage: advanced
status: draft
---

# Malus's Law: Derivation and Applications

## Core Idea
Malus's law states that linearly polarized light of intensity I₀ transmitted through a polarizer oriented at angle θ to the polarization direction has transmitted intensity I = I₀cos²θ. This relationship arises from the component of the electric field parallel to the polarizer's transmission axis.

## Explainer

The derivation of Malus's law connects two things you already know: the geometry of linearly polarized light and the fact that intensity is proportional to the square of the electric field amplitude. From your study of linear polarization, you know that the electric field oscillates in a single plane, and you can describe its direction as a vector. A polarizer transmits only the component of the electric field aligned with its **transmission axis** — everything perpendicular to that axis is blocked.

When linearly polarized light with electric field amplitude E₀ strikes a polarizer whose transmission axis makes an angle θ with the polarization direction, only the parallel component passes. That component has amplitude E₀ cos θ — this is straightforward vector projection, the same operation you use to find the component of any vector along a chosen axis. The perpendicular component E₀ sin θ is absorbed or reflected by the polarizer material. The transmitted electric field amplitude is therefore E_t = E₀ cos θ.

Now apply the intensity relationship: intensity is proportional to the square of the field amplitude, I ∝ E². The incident intensity is I₀ ∝ E₀², and the transmitted intensity is I ∝ (E₀ cos θ)² = E₀² cos²θ. Therefore I = I₀ cos²θ. The derivation has exactly two steps: project the field amplitude (cosine), then square for intensity (cosine squared). The cos²θ factor is the complete explanation of why intensity drops to zero at 90° rather than at some other angle — it follows entirely from the vector nature of the electric field.

Several results follow immediately. At θ = 0°, I = I₀ (all transmitted). At θ = 90°, I = 0 (crossed polarizers block all light). At θ = 45°, I = I₀/2 (half transmitted). A striking application is the three-polarizer demonstration: two crossed polarizers block all light, but inserting a third polarizer between them at 45° allows some light through. Applying Malus's law twice — first to the 0°→45° transition (I₁ = I₀/2), then to the 45°→90° transition (I₂ = I₁/2 = I₀/4) — gives the correct result. The intermediate polarizer rotates the polarization state, creating a non-zero component along the final axis. This result is impossible if you think of polarization as simply filtering out some light; it only makes sense when you track the electric field vector through each interaction.
