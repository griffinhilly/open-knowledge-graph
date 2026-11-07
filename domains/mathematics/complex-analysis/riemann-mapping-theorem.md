---
id: riemann-mapping-theorem
title: The Riemann Mapping Theorem
domain: mathematics
course: complex-analysis
prerequisites:
  - id: schwarz-lemma
    type: hard
  - id: conformal-mappings
    type: hard
  - id: connected-simply-connected-plane
    type: hard
  - id: liouville-theorem
    type: soft
  - id: arzela-ascoli-theorem
    type: soft
builds-toward: []
tags: [complex-analysis, conformal-maps, riemann-mapping-theorem, simply-connected, normal-families]
stage: advanced
status: validated
---

# The Riemann Mapping Theorem

## Core Idea
The Riemann mapping theorem states that every nonempty, simply connected, open subset U of the complex plane other than ℂ itself can be mapped onto the open unit disk D by a holomorphic bijection. Such a map is conformal, and its inverse is holomorphic too. The map is unique once you choose a point z₀ in U to send to 0 and require f'(z₀) to be a positive real number. So, as far as complex analysis can tell, all such regions look alike, however irregular their boundaries are.

## How It's Best Learned
First build explicit examples: the Cayley map (z - i)/(z + i) from the upper half-plane to the disk, and compositions with powers, exponentials and Möbius maps for wedges and strips. Then explain why ℂ is excluded using Liouville's theorem. Present the proof as an extremal problem: among one-to-one maps of U into the disk that send z₀ to 0, find the one with the largest |f'(z₀)|, and show it must be onto.

## Common Misconceptions
- Every simply connected open set, including ℂ, is conformally equivalent to the disk. (A holomorphic bijection from ℂ onto D would be a bounded entire function, which is constant by Liouville's theorem.)
- The theorem gives a formula for the mapping function. (It proves existence and uniqueness; explicit formulas are known only for special regions.)
- The theorem applies to regions with holes, such as an annulus. (The region must be simply connected; two annuli are conformally equivalent only when the ratios of their outer to inner radii are equal.)
- The conformal map onto the disk is unique. (It is unique only up to composition with the disk's automorphisms; fixing f(z₀) = 0 and f'(z₀) > 0 pins it down.)

## Questions

```yaml
- question: "Which region can NOT be mapped onto the unit disk by a holomorphic bijection?"
  type: multiple-choice
  options:
    - "The upper half-plane"
    - "The strip 0 < Im z < 1"
    - "The whole plane ℂ"
    - "The plane with the ray (-∞, 0] removed"
  answer: 2
  explanation: "The other three regions are simply connected proper open subsets of ℂ, so the theorem applies. A holomorphic bijection from ℂ onto the disk would be a bounded entire function, hence constant by Liouville's theorem, which is impossible for a bijection."

- question: "For a fixed simply connected proper region U and point z₀ in U, there is exactly one holomorphic bijection f of U onto the disk with f(z₀) = 0 and f'(z₀) > 0."
  type: true-false
  answer: true
  explanation: "If f and g both qualify, then g ∘ f⁻¹ is an automorphism of the disk fixing 0, so it is a rotation e^(iθ)z by Schwarz's lemma. The condition that both derivatives at z₀ are positive real numbers forces e^(iθ) = 1, so g = f."

- question: "Verify that f(z) = (z - i)/(z + i) maps the upper half-plane into the unit disk."
  type: short-answer
  answer: "For Im z > 0, z is closer to i than to -i, so |z - i| < |z + i| and |f(z)| < 1."
  explanation: "The upper half-plane is the set of points closer to i than to -i, since the real axis is the perpendicular bisector of the segment from -i to i. The Cayley map is a Möbius transformation, and it maps the half-plane onto the whole disk with inverse w ↦ i(1 + w)/(1 - w)."

- question: "In the standard proof, why is the extremal map (the one maximizing |f'(z₀)|) shown to be onto the disk?"
  type: short-answer
  answer: "If it missed a point of the disk, a square-root construction composed with disk automorphisms would give another one-to-one map into the disk with a larger |f'(z₀)|, contradicting maximality."
  explanation: "This is where Schwarz's lemma enters. The old map equals the new map followed by squaring composed with disk automorphisms. That self-map of the disk fixes 0 and is not a rotation, so its derivative at 0 has modulus less than 1. Hence the new map has a strictly larger |f'(z₀)|."
```

## Explainer

Conformal maps preserve angles, and Möbius transformations, powers and exponentials let you map many regions to one another by explicit formulas. The upper half-plane goes to the unit disk by the Cayley map f(z) = (z - i)/(z + i). A quarter-plane goes to the half-plane by z ↦ z². A strip goes to a half-plane by an exponential. It is natural to ask how far this goes. Bernhard Riemann stated the answer in his 1851 doctoral thesis.

Theorem. Let U be a nonempty, simply connected, open subset of ℂ with U ≠ ℂ. Then there is a holomorphic bijection f: U → D onto the unit disk. For each z₀ in U there is exactly one such f with f(z₀) = 0 and f'(z₀) > 0.

The hypotheses are needed. The region must be simply connected, because a holomorphic bijection is a homeomorphism and the disk has no holes. It must also be a proper subset. A holomorphic bijection from ℂ onto D would be a bounded entire function, and by Liouville's theorem it would be constant.

Uniqueness follows from Schwarz's lemma. If f and g both satisfy the normalization, then g ∘ f⁻¹ is an automorphism of the disk that fixes 0. Such maps are rotations, and the positivity of both derivatives at z₀ forces the rotation to be the identity.

Existence is the hard part, and its proof is an extremal argument. Consider the family F of one-to-one holomorphic maps from U into D that send z₀ to 0. This family is nonempty: U misses some point a, and because U is simply connected, a branch of √(z - a) exists on U. That branch is one-to-one and its image avoids a small disk, so a Möbius map moves the image inside D. Next, the functions in F are uniformly bounded, so by Montel's theorem (a consequence of the Arzelà-Ascoli theorem) every sequence in F has a subsequence converging uniformly on compact subsets. Take a sequence whose values |f'(z₀)| approach the largest possible value, and pass to a limit. Hurwitz's theorem shows the limit is still one-to-one, so it lies in F. Finally, if this extremal map missed some point of D, a square-root construction would produce another member of F with a larger |f'(z₀)|. So the extremal map is onto.

As a result, a problem posed on such a region, such as finding a harmonic function with given boundary values, can often be moved to the disk, solved there, and moved back.
