---
id: ricci-tensor-scalar-curvature
title: Ricci Tensor and Scalar Curvature
domain: physics
course: general-relativity
prerequisites:
- id: riemann-curvature-tensor
  type: hard
tags:
- ricci-tensor
- scalar-curvature
- contraction
- einstein-tensor
- volume-deformation
stage: expert
status: validated
---

# Ricci Tensor and Scalar Curvature

## Core Idea
The Ricci tensor R_μν and the Ricci scalar R are contractions of the Riemann curvature tensor that extract the part of curvature directly coupled to matter. The Ricci tensor R_μν = R^λ_{μλν} is a symmetric (0,2) tensor that measures how volumes of small geodesic balls are deformed relative to flat space — it tells you whether nearby geodesics converge or diverge on average. The Ricci scalar R = g^{μν}R_μν is the trace of the Ricci tensor, a single scalar measuring the total curvature at a point. Together they form the Einstein tensor G_μν = R_μν - (1/2)g_μν R, which appears on the left side of Einstein's field equations. In vacuum (no matter), R_μν = 0, but the full Riemann tensor can still be nonzero — the remaining curvature is encoded in the Weyl tensor, which describes tidal forces and gravitational waves in empty space.

## Questions

```yaml
- question: "In vacuum (T_μν = 0), the Einstein field equations reduce to R_μν = 0. Which of the following is a correct consequence?"
  type: multiple-choice
  options:
    - "Spacetime must be flat (Riemann tensor vanishes)"
    - "The Riemann tensor can be nonzero — the Weyl tensor carries curvature information not captured by the Ricci tensor"
    - "Gravitational waves cannot propagate in vacuum"
    - "The scalar curvature R is nonzero but the Ricci tensor vanishes"
  answer: 1
  explanation: "R_μν = 0 means the Ricci tensor vanishes, but the full Riemann tensor has 20 independent components — only 10 are in the Ricci tensor. The remaining 10 are in the Weyl tensor C_{ρσμν}, which can be nonzero even when R_μν = 0. This is why the Schwarzschild solution is curved (tidal forces exist) despite being a vacuum solution. Gravitational waves also propagate in vacuum as Weyl curvature. If R_μν = 0, then R = g^{μν}R_μν = 0 as well, so option D is wrong."

- question: "The Ricci scalar R is always positive in a region where matter is present."
  type: true-false
  answer: false
  explanation: "The sign of R depends on the equation of state of the matter. For a perfect fluid with energy density ρ and pressure p, the trace of the Einstein equations gives R = -8πG(ρ - 3p)/c⁴ (in the +−−− convention) or similar expressions depending on sign convention. For ordinary matter (ρ > 0, p ≥ 0), R can be negative. For a cosmological constant (dark energy with p = -ρc²), R can be positive. The sign of R is not determined by the presence of matter alone."

- question: "Explain the physical meaning of the Ricci tensor in terms of the volume of a small ball of freely falling test particles."
  type: short-answer
  answer: "Consider a small ball of test particles initially at rest relative to each other in a local inertial frame. As they fall freely, the ball deforms due to tidal forces. The Ricci tensor determines the rate of change of the volume of this ball: the fractional rate of volume decrease (convergence of geodesics) is proportional to R_μν u^μ u^ν, where u^μ is the four-velocity. In the presence of matter with positive energy density, R_μν u^μ u^ν > 0, so the volume decreases — gravity is attractive. In vacuum, R_μν = 0, so the volume of the ball is preserved to first order, even though its shape changes (tidal distortion from the Weyl tensor stretches it in some directions and compresses it in others)."
  explanation: "This geometric interpretation makes clear the distinction between Ricci and Weyl curvature. The Ricci tensor controls volume changes (focusing of geodesics, directly sourced by matter), while the Weyl tensor controls shape changes (tidal distortion, present even in vacuum). A black hole's vacuum exterior has zero Ricci curvature but strong Weyl curvature — volumes are preserved but shapes are dramatically distorted."

- question: "Why is the Einstein tensor G_μν = R_μν - (1/2)g_μν R preferred over the Ricci tensor alone on the left side of the field equations?"
  type: short-answer
  answer: "The Einstein tensor is divergence-free: ∇^μ G_μν = 0 identically, as a consequence of the contracted Bianchi identity. This is essential because the right side of the field equations, 8πG T_μν / c⁴, must also be divergence-free (∇^μ T_μν = 0) to ensure local conservation of energy and momentum. The Ricci tensor alone does not satisfy ∇^μ R_μν = 0 in general, so using R_μν = 8πG T_μν / c⁴ alone would be inconsistent with energy-momentum conservation. The combination G_μν = R_μν - (1/2)g_μν R is the unique symmetric, divergence-free tensor built from the metric and its first two derivatives (up to the cosmological constant term)."
  explanation: "The contracted Bianchi identity is the mathematical guarantee that Einstein's field equations are self-consistent: the geometry automatically conserves energy-momentum. This identity also reduces the number of truly independent field equations from 10 to 6, which is exactly right given the 4 coordinate degrees of freedom."
```

## Explainer

The Riemann curvature tensor R^ρ_{σμν} has 20 independent components in four dimensions and contains complete information about the curvature at each point. For the Einstein field equations, however, you do not need all 20 components — you need a (0,2) tensor that can be equated to the stress-energy tensor. The Ricci tensor R_μν = R^λ_{μλν} is obtained by contracting (tracing over) the first and third indices of the Riemann tensor. This contraction reduces the 20 components to 10 independent ones (the Ricci tensor is symmetric, R_μν = R_νμ, as a consequence of the Riemann tensor's symmetries). The Ricci scalar R = g^{μν}R_μν is the further contraction to a single number, giving the total curvature at a point.

Physically, the Ricci tensor measures how spacetime curvature focuses or defocuses bundles of geodesics — equivalently, how it changes the volume of a small freely falling ball of test particles. If you release a small spherical cloud of dust particles from rest, the initial rate of volume contraction is proportional to R_μν u^μ u^ν, where u^μ is the common four-velocity. In the presence of ordinary matter, this quantity is positive: gravity causes the ball to shrink, which is the attractive nature of gravity expressed geometrically. In vacuum, R_μν = 0, and the ball maintains its volume but changes its shape — it gets stretched in some directions and squeezed in others. The shape-changing part is encoded in the Weyl tensor, which is the trace-free part of the Riemann tensor.

The Einstein tensor G_μν = R_μν - (1/2)g_μν R is the specific combination of Ricci tensor and scalar that appears in the field equations. Its special property is the contracted Bianchi identity: ∇^μ G_μν = 0 holds as a mathematical identity, requiring no assumptions about the spacetime or the matter content. This is crucial because the stress-energy tensor on the right side of the field equations must satisfy ∇^μ T_μν = 0 (local energy-momentum conservation). If the geometric side of the equation were not automatically divergence-free, the field equations would impose additional constraints on the matter that would generally be inconsistent. The Einstein tensor is, up to the addition of a cosmological constant term Λg_μν, the unique symmetric, divergence-free (0,2) tensor constructible from the metric and its first and second derivatives.

The vacuum field equations R_μν = 0 are deceptively simple-looking — they are 10 coupled, nonlinear, second-order partial differential equations for the 10 independent metric components. Despite R_μν = 0, the spacetime can be highly curved because the Weyl tensor (the remaining 10 components of the Riemann tensor) can be nonzero. The Schwarzschild solution (the spacetime outside a spherical mass) satisfies R_μν = 0 everywhere outside the mass, yet it has nonzero Weyl curvature that produces tidal forces, bends light, and creates the event horizon of a black hole. Gravitational waves in vacuum are also propagating Weyl curvature — oscillating tidal distortions traveling at the speed of light with zero Ricci curvature.
