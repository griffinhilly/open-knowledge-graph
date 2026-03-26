---
id: mobius-transformations
title: Möbius Transformations
domain: mathematics
course: complex-analysis
prerequisites:
- id: conformal-mappings
  type: hard
tags:
- mobius-transformations
- linear-fractional
- conformal
stage: advanced
status: validated
---

# Möbius Transformations

## Core Idea
A Möbius transformation is f(z) = (az + b)/(cz + d) where ad - bc ≠ 0. These are conformal maps of the extended complex plane (including ∞) and form a group under composition. They map circles and lines to circles and lines, making them useful for transforming domains in conformal mapping problems.

## Questions

```yaml
- question: "You need a conformal map sending the upper half-plane to the unit disk, mapping i ↦ 0, the point 0 ↦ -1, and ∞ ↦ 1. How many Möbius transformations satisfy all three conditions?"
  type: multiple-choice
  options:
    - "None — the upper half-plane and unit disk are not conformally equivalent"
    - "Infinitely many — there are many ways to construct a Möbius transformation between these domains"
    - "Exactly one — the three-point determination property uniquely fixes the map"
    - "Exactly two — the map and its inverse both satisfy the conditions"
  answer: 2
  explanation: "The three-point rule states that given any two triples of distinct points in ℂ ∪ {∞}, there is exactly one Möbius transformation sending the first triple to the second. Specifying where three boundary points go pins down the map completely — no free parameters remain. This is precisely what makes Möbius transformations so powerful for conformal mapping: you can construct the exact map you need by selecting three convenient boundary correspondences, then verifying the result sends the entire domain correctly."

- question: "Under a Möbius transformation, a circle C in the complex plane maps to a line rather than to another circle. Which of the following must be true?"
  type: multiple-choice
  options:
    - "The map violates conformality at the image, since circles and lines have different curvature"
    - "The circle C passes through the pole of the transformation — the point mapped to ∞"
    - "The transformation is degenerate, meaning ad - bc = 0"
    - "C must be the unit circle |z| = 1, since only it has the symmetry required to map to a line"
  answer: 1
  explanation: "In the extended complex plane, 'lines' are circles through ∞. A circle maps to a line (instead of another circle) precisely when it passes through the pole of the transformation — the point z = -d/c that gets sent to ∞. When the pole lies on C, its image must pass through ∞, which in the standard plane is a line. This is a beautiful illustration of why Möbius transformations are best understood on the Riemann sphere: the distinction between 'circle' and 'line' disappears, and the theorem becomes simply 'circles map to circles.'"

- question: "The composition of two Möbius transformations is always another Möbius transformation — they form a group under composition."
  type: true-false
  answer: true
  explanation: "This group property is what makes Möbius transformations so useful in conformal mapping applications. You can chain them: map a disk to a centered disk, then map the centered disk to the upper half-plane, and the composition is automatically another Möbius transformation — exact and conformal, with no approximation. The group structure also means there is always an inverse (another Möbius transformation), and composition is associative. The group of all Möbius transformations is isomorphic to PSL(2,ℂ), the projective special linear group."

- question: "The condition ad - bc ≠ 0 in a Möbius transformation f(z) = (az+b)/(cz+d) ensures that f is defined for most complex numbers z, including z = -d/c."
  type: true-false
  answer: false
  explanation: "The condition ad - bc ≠ 0 does NOT make f defined at z = -d/c — it maps that point to ∞. The pole z = -d/c is exactly the point where the denominator vanishes, so f is undefined there in the ordinary complex plane; on the Riemann sphere, this point is mapped to ∞. The condition ad - bc ≠ 0 ensures the transformation is non-degenerate (not collapsing to a constant function) — if ad = bc, the 'map' would send every point to a/c. The distinction is important: the condition prevents degeneracy, not the existence of a pole."

- question: "State the three-point rule for Möbius transformations and explain why it is useful when constructing conformal maps between specific domains."
  type: short-answer
  answer: "The three-point rule: given any two triples of distinct points (z₁, z₂, z₃) and (w₁, w₂, w₃) in ℂ ∪ {∞}, there exists exactly one Möbius transformation sending zᵢ ↦ wᵢ. This is useful because it reduces the problem of finding a conformal map between domains to the geometric problem of matching boundary points. To map a disk to the upper half-plane, choose three boundary points of the disk and specify where they go on the real axis; the unique Möbius transformation doing this is the desired map. No solving systems of equations is needed beyond the three-point matching."
  explanation: "This rule underpins virtually all explicit conformal mapping constructions involving Möbius transformations. In practice, you identify three convenient points (often using 0, 1, ∞, or boundary intersection points), specify their images, and read off the map. The uniqueness is as important as the existence: it tells you there is no ambiguity once three correspondences are fixed, and it means you can verify a proposed map by checking just three points."
```

## Explainer

You've already studied conformal mappings — angle-preserving maps of the complex plane that translate, rotate, scale, and transform domains to make boundary value problems solvable. Möbius transformations are the most important class of conformal maps, combining several elementary operations into a single elegant formula that acts on the entire extended complex plane.

A **Möbius transformation** (also called a **linear fractional transformation**) is any map f(z) = (az + b)/(cz + d) where a, b, c, d ∈ ℂ and **ad - bc ≠ 0**. The condition ad - bc ≠ 0 (the determinant of the matrix [[a,b],[c,d]] is nonzero) ensures the map isn't degenerate — if ad = bc, the transformation collapses to a constant. Every Möbius transformation is a composition of three elementary operations you already know: a translation (z ↦ z + b/a), a scaling and rotation (z ↦ az), and an **inversion** (z ↦ 1/z). The inversion is the new ingredient that plain linear maps can't provide — it maps points near the origin to points far away, and vice versa.

The key geometric property: **Möbius transformations map circles and lines to circles and lines**. Here, "line" is treated as a circle through the point at infinity in the extended complex plane ℂ ∪ {∞}. A Möbius transformation sends z = -d/c to ∞ (the pole) and sends ∞ to a/c. This is why they're defined on the **Riemann sphere** — they become bijections of that compact space. The image of a circle under a Möbius transformation is another circle or possibly a line, and critically, angles between curves are preserved (conformality is maintained).

The power of Möbius transformations in applications comes from the **three-point rule**: given any two triples of distinct points (z₁, z₂, z₃) and (w₁, w₂, w₃) in ℂ ∪ {∞}, there is exactly one Möbius transformation sending z_i ↦ w_i. This means you can construct the specific map that transforms a given domain (say, a disk) to a standard domain (say, the upper half-plane) by specifying where three boundary points go. Since Möbius transformations form a **group** under composition, you can chain them: first map disk to disk (centering it), then map disk to half-plane, and the composition is another Möbius transformation — no approximation, exact and conformal.
