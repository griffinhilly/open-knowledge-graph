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
stage: expert
status: draft
---

# Root Locus: Angle and Magnitude Conditions

## Core Idea
Root locus points satisfy ∠[1 + KG(s)] = ±180°(2k+1) (angle) and |1 + KG(s)| = 0 (magnitude). The locus traces closed-loop pole trajectories as gain K varies from 0 to ∞. Angle condition determines which points lie on the locus; magnitude condition determines the gain K at each point.

## Questions

```yaml
- question: "A control engineer wants to determine whether a specific point s₀ in the complex plane lies on the root locus. Which condition should they check, and what does checking it require?"
  type: multiple-choice
  options:
    - "The magnitude condition — compute |KG(s₀)| and check whether it equals 1 for some positive K"
    - "The angle condition — sum the angles from all open-loop poles and zeros to s₀ and check whether the total is an odd multiple of ±180°"
    - "Both conditions simultaneously — a point must satisfy both angle and magnitude to lie on the locus"
    - "Whether s₀ lies in the left half-plane — only stable points can be on the root locus"
  answer: 1
  explanation: "The angle condition is the membership test: a point lies on the root locus if and only if the total angle contribution of all poles and zeros (angles subtracted for poles, added for zeros, measured as the argument of the vector from each to s₀) sums to an odd multiple of ±180°. This condition is independent of K — it depends only on the geometry of the open-loop poles and zeros. The magnitude condition is not a membership test; once a point is confirmed on the locus by the angle condition, the magnitude condition computes the specific gain K at that point. Option D is wrong because root locus can include right-half-plane points (they represent unstable poles at certain gain values)."

- question: "As gain K is increased from 0 toward infinity, where do the closed-loop poles begin and where do they end up?"
  type: multiple-choice
  options:
    - "They begin at the open-loop zeros and migrate toward the open-loop poles as K grows"
    - "They begin at the origin and spread outward symmetrically as K grows"
    - "They begin at the open-loop poles (K = 0) and end at open-loop zeros or go to infinity (K → ∞)"
    - "Their starting and ending positions depend on the specific gain value and cannot be stated generally"
  answer: 2
  explanation: "At K = 0, the characteristic equation 1 + KG(s) = 0 reduces to G(s) → ∞, which occurs at the open-loop poles. As K → ∞, the equation requires G(s) → 0, which occurs at the open-loop zeros (finite zeros) or as s → ∞ along asymptotes (for systems with more poles than zeros). This start-at-poles, end-at-zeros rule follows directly from the magnitude condition: K = 1/|G(s₀)|, so K = 0 where |G| → ∞ (at poles) and K → ∞ where |G| → 0 (at zeros). All other root locus construction rules are derived from this foundation."

- question: "The angle condition for the root locus depends on the value of gain K being used."
  type: true-false
  answer: false
  explanation: "The angle condition is completely independent of K. It tests only the phase of G(s₀): whether the sum of angles to the candidate point from all zeros minus the sum of angles from all poles equals an odd multiple of ±180°. This phase requirement comes from the fact that KG(s₀) must equal −1, and the phase of −1 is ±180° regardless of its magnitude. K only affects the magnitude of KG(s₀), not its angle. This is why the angle condition can be checked without knowing K, and why the locus is determined entirely by the open-loop pole and zero locations."

- question: "The magnitude condition is used after the angle condition to determine the gain K required to place a closed-loop pole at a specific point on the locus."
  type: true-false
  answer: true
  explanation: "The two conditions play complementary roles: the angle condition identifies which points are on the locus (no K needed); the magnitude condition then computes K for any confirmed locus point. Geometrically, K = 1/|G(s₀)| equals the product of distances from s₀ to all open-loop poles divided by the product of distances to all open-loop zeros. This geometric interpretation allows gain to be read off a root locus diagram using measurements, which was the original manual design method before computational tools. The two conditions are thus sequential: first check membership (angle), then compute gain (magnitude)."

- question: "Explain the distinct roles of the angle condition and the magnitude condition in root locus analysis, and why the angle condition must be checked before the magnitude condition."
  type: short-answer
  answer: "The angle condition determines which points in the complex plane lie on the root locus: a point s₀ is on the locus if and only if ∠G(s₀) = ±180°(2k+1). This check is independent of K — it depends only on the geometry of open-loop poles and zeros. The magnitude condition then determines the value of gain K at any point already confirmed to be on the locus: K = 1/|G(s₀)|, computed as the product of pole-distances divided by the product of zero-distances to s₀. The angle condition must come first because the magnitude condition is meaningless for points not on the locus — any K will satisfy |KG(s₀)| = 1 if you choose K = 1/|G(s₀)|, whether or not s₀ is actually a closed-loop pole location. Only angle determines membership; magnitude determines the K value at confirmed locus points."
  explanation: "This separation of concerns — angle for membership, magnitude for gain — is what makes root locus a geometric method. You can sketch the entire locus shape using only angle considerations and construction rules, then use magnitude to annotate specific gain values at key points (stability crossings, desired damping ratios). Engineers designing controllers use this to pick a gain that places closed-loop poles at a desired location."
```

## Explainer

From your study of transfer functions, you know that the closed-loop poles — the roots of the characteristic equation 1 + KG(s) = 0 — determine whether a system is stable and how its transient response behaves. Poles in the left half-plane mean decaying oscillations (stable); poles in the right half-plane mean growing oscillations (unstable). The **root locus** answers the natural design question: as we turn up the gain K from zero to infinity, where do the closed-loop poles go? The angle and magnitude conditions are the mathematical tests that define this trajectory.

The **angle condition** is derived directly from the characteristic equation. A point s₀ in the complex plane lies on the root locus if and only if it satisfies 1 + KG(s₀) = 0, which means KG(s₀) = −1. A complex number equals −1 when its magnitude is 1 and its angle is ±180°(2k+1) for integer k. The angle condition is the phase part of this requirement: ∠G(s₀) = ±180°(2k+1). This condition is independent of K — it depends only on the geometry of the open-loop poles and zeros, not on the gain value. To check whether any candidate point lies on the locus, you sum the angles contributed by all open-loop zeros (positive) and subtract the angles contributed by all open-loop poles (negative), measuring each angle as the argument of the vector from that pole or zero to the candidate point. If the total is an odd multiple of ±180°, the point is on the locus.

The **magnitude condition** is the other half: once you have confirmed a point lies on the locus (angle condition satisfied), the gain K at that point is determined by |KG(s₀)| = 1, so K = 1/|G(s₀)|. Geometrically, |G(s₀)| is the product of the distances from the candidate point to all open-loop zeros, divided by the product of the distances to all open-loop poles. This ratio equals 1/K, so larger distances correspond to smaller gain. At K = 0, the locus starts at the open-loop poles (where |G(s₀)| → ∞, making K → 0). As K → ∞, the locus ends at the open-loop zeros (finite zeros) or extends to infinity along asymptotes (for systems with more poles than zeros).

Together, the two conditions give you a complete geometric picture of how gain selection moves the closed-loop poles. In practice, you rarely test individual points by hand — the 180° rule and other construction rules (asymptotes, breakaway points, imaginary-axis crossings) let you sketch the locus quickly. But every rule in root locus construction is derived from these two fundamental conditions, so understanding them deeply means you can always return to first principles when a standard rule does not apply.
