---
id: root-locus-angle-magnitude-equations
title: 'Root Locus: Angle and Magnitude Conditions'
domain: engineering
course: control-systems
prerequisites:
- id: transfer-function-derivation-differential-equations
  type: hard
- id: complex-numbers-intro
  type: soft
builds-toward:
- root-locus-asymptote-centroid-breakaway
- steady-state-error-types-system-classification
tags:
- root-locus
- angle-condition
- magnitude-condition
- locus
stage: abstract-reasoning
status: draft
---

# Root Locus: Angle and Magnitude Conditions

## Core Idea
Root locus points satisfy ∠[1 + KG(s)] = ±180°(2k+1) (angle) and |1 + KG(s)| = 0 (magnitude). The locus traces closed-loop pole trajectories as gain K varies from 0 to ∞. Angle condition determines which points lie on the locus; magnitude condition determines the gain K at each point.

## Explainer

From your study of transfer functions, you know that the closed-loop poles — the roots of the characteristic equation 1 + KG(s) = 0 — determine whether a system is stable and how its transient response behaves. Poles in the left half-plane mean decaying oscillations (stable); poles in the right half-plane mean growing oscillations (unstable). The **root locus** answers the natural design question: as we turn up the gain K from zero to infinity, where do the closed-loop poles go? The angle and magnitude conditions are the mathematical tests that define this trajectory.

The **angle condition** is derived directly from the characteristic equation. A point s₀ in the complex plane lies on the root locus if and only if it satisfies 1 + KG(s₀) = 0, which means KG(s₀) = −1. A complex number equals −1 when its magnitude is 1 and its angle is ±180°(2k+1) for integer k. The angle condition is the phase part of this requirement: ∠G(s₀) = ±180°(2k+1). This condition is independent of K — it depends only on the geometry of the open-loop poles and zeros, not on the gain value. To check whether any candidate point lies on the locus, you sum the angles contributed by all open-loop zeros (positive) and subtract the angles contributed by all open-loop poles (negative), measuring each angle as the argument of the vector from that pole or zero to the candidate point. If the total is an odd multiple of ±180°, the point is on the locus.

The **magnitude condition** is the other half: once you have confirmed a point lies on the locus (angle condition satisfied), the gain K at that point is determined by |KG(s₀)| = 1, so K = 1/|G(s₀)|. Geometrically, |G(s₀)| is the product of the distances from the candidate point to all open-loop zeros, divided by the product of the distances to all open-loop poles. This ratio equals 1/K, so larger distances correspond to smaller gain. At K = 0, the locus starts at the open-loop poles (where |G(s₀)| → ∞, making K → 0). As K → ∞, the locus ends at the open-loop zeros (finite zeros) or extends to infinity along asymptotes (for systems with more poles than zeros).

Together, the two conditions give you a complete geometric picture of how gain selection moves the closed-loop poles. In practice, you rarely test individual points by hand — the 180° rule and other construction rules (asymptotes, breakaway points, imaginary-axis crossings) let you sketch the locus quickly. But every rule in root locus construction is derived from these two fundamental conditions, so understanding them deeply means you can always return to first principles when a standard rule does not apply.
