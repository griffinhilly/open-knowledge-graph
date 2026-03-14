---
id: malus-law
title: Malus's Law
domain: physics
course: waves-and-optics
prerequisites:
- id: polarization-of-light
  type: hard
- id: sine-cosine-tangent-ratios
  type: hard
tags:
- Malus's law
- intensity
- polarizer angle
- cosine squared
stage: formal-systems
status: validated
---

# Malus's Law

## Core Idea
When polarized light of intensity I₀ passes through a polarizer whose transmission axis makes an angle θ with the polarization direction of the incoming light, the transmitted intensity is I = I₀cos²θ. At θ = 0°, full transmission; at θ = 90°, no transmission. For initially unpolarized light passing through a single polarizer, the transmitted intensity is always I₀/2 regardless of orientation, since all directions are equally represented.

## How It's Best Learned
Use a photometer behind two polarizers; rotate the second polarizer while recording intensity. Plot I vs. θ and verify the cos²θ dependence. Extrapolate to θ = 90° to confirm complete extinction.

## Common Misconceptions
- Malus's law applies to already-polarized incident light; for unpolarized light, the first polarizer always transmits exactly half, independent of its orientation.
- Students apply cosθ instead of cos²θ because they project the electric field amplitude (cosθ) but forget that intensity ∝ E².
