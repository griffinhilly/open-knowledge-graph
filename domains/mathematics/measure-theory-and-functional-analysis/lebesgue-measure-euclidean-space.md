---
id: lebesgue-measure-euclidean-space
title: Lebesgue Measure on ℝⁿ
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: lebesgue-measure-real-line
  type: hard
builds-toward:
- product-measures-fubini-theorem
tags:
- lebesgue-measure
stage: expert
status: draft
---

# Lebesgue Measure on ℝⁿ

## Core Idea
Lebesgue measure on ℝⁿ extends the one-dimensional measure via product measure, assigning volume to measurable sets. Lower-dimensional sets (lines, planes) have measure zero, reflecting that they are 'negligible' in the higher-dimensional space.

## Questions

```yaml
- question: "Consider an infinite plane in ℝ³ — a 2-dimensional flat surface extending in all directions. What is its Lebesgue measure λ₃?"
  type: multiple-choice
  options:
    - "Infinite — it has infinite 2D area, so its 3D measure must also be infinite"
    - "Zero — it has no 3-dimensional thickness, so it contributes nothing to 3D volume"
    - "One — by convention, a codimension-1 set is assigned unit measure"
    - "Undefined — Lebesgue measure only applies to sets with the same dimension as the ambient space"
  answer: 1
  explanation: "A plane in ℝ³ has λ₃-measure zero, even though it has infinite 2D area. The key insight is that Lebesgue measure on ℝⁿ measures n-dimensional volume. A 2D plane, no matter how large, has no 3-dimensional thickness — it cannot be approximated by any finite or even σ-finite collection of 3D boxes with positive total volume. This is why lower-dimensional sets are 'negligible' in the measure-theoretic sense: they contribute zero to integrals over ℝ³, regardless of their geometric size in their own dimension."

- question: "A function f: ℝ² → ℝ is defined everywhere and you change its values on the x-axis (a 1-dimensional line in ℝ²). How does this affect the Lebesgue integral ∫∫f dλ₂?"
  type: multiple-choice
  options:
    - "The integral changes by an amount proportional to the total variation of f on the x-axis"
    - "The integral is unchanged — the x-axis has λ₂-measure zero, so changes on it are irrelevant to integration"
    - "The integral is undefined after the modification because the function is no longer measurable"
    - "The integral changes only if f was previously continuous on the x-axis"
  answer: 1
  explanation: "The x-axis in ℝ² has λ₂-measure zero (it is a 1-dimensional set in a 2-dimensional space). Lebesgue integration ignores sets of measure zero: ∫f dλ = ∫g dλ whenever f = g almost everywhere (i.e., everywhere except possibly on a set of measure zero). This robustness is one of the fundamental advantages of Lebesgue over Riemann integration — you can change function values on any lower-dimensional set, any countable set, or any other measure-zero set without affecting the integral at all."

- question: "Any smooth surface (such as a sphere or a paraboloid) in ℝ³ has λ₃-measure zero."
  type: true-false
  answer: true
  explanation: "True. Smooth surfaces are 2-dimensional manifolds embedded in ℝ³. They have no 3-dimensional thickness — they cannot fill any open ball in ℝ³, and they can be covered by 3D boxes of arbitrarily small total volume. Formally, this follows from the general principle that any k-dimensional smooth manifold (k < n) has λₙ-measure zero. This means integration over ℝ³ is completely unaffected by what a function does on any smooth surface, curve, or point."

- question: "A set of Lebesgue measure zero in ℝⁿ must be either finite or countably infinite."
  type: true-false
  answer: false
  explanation: "False. Many uncountable sets have Lebesgue measure zero. The classic example on ℝ is the Cantor set — uncountable yet λ₁-measure zero. In ℝⁿ, any smooth curve, surface, or lower-dimensional manifold is uncountable and yet has measure zero. For instance, the x-axis in ℝ² contains uncountably many points but has λ₂-measure zero. The 'negligibility' captured by measure zero is about n-dimensional volume, not cardinality."

- question: "Explain why a 2-dimensional plane has Lebesgue measure zero in ℝ³, and why this fact matters for integration over ℝ³."
  type: short-answer
  answer: "A plane in ℝ³ has no 3-dimensional thickness: it can be enclosed in a collection of 3D boxes whose total volume is arbitrarily small (take boxes of height ε centered on the plane). By definition, this means its λ₃-measure is zero. For integration, this means changes to a function on any plane — or any surface, curve, or lower-dimensional set — leave the Lebesgue integral unchanged. This is what 'almost everywhere' means: properties that hold everywhere except on a set of measure zero are sufficient for all integration-theoretic purposes."
  explanation: "This measure-zero phenomenon is not merely a curiosity — it underpins the concept of 'almost everywhere' equality, which makes Lebesgue integration robust and allows function spaces like L² to treat functions that differ only on a set of measure zero as identical. It also explains why you can safely ignore discontinuities on curves or surfaces when computing integrals, and why Fourier series can converge almost everywhere even to functions with countably many jumps."
```

## Explainer

You already understand Lebesgue measure on ℝ — it assigns a "length" to subsets of the real line in a way that extends the intuitive notion of length for intervals while handling pathological sets. The key move in building Lebesgue measure on ℝⁿ is to apply that same idea dimensionally: start with **product measure**. In ℝ², the natural way to measure a rectangle [a, b] × [c, d] is as its width times its height: (b − a)(d − c). The Lebesgue measure on ℝ² is the unique measure that assigns exactly this value to rectangles and extends to all measurable sets via the product construction.

The formal mechanism is Carathéodory's extension theorem applied to the product σ-algebra. But the geometric intuition is accessible: just as you built the Lebesgue σ-algebra on ℝ by starting with intervals and closing under countable unions and complements, the Lebesgue σ-algebra on ℝⁿ starts with n-dimensional rectangles (products of intervals) and closes under the same operations. The measure λₙ(A) that results agrees with your intuitions — the unit cube [0,1]ⁿ has measure 1, a ball of radius r in ℝ³ has volume (4/3)πr³, and so on.

The most conceptually important feature of higher-dimensional Lebesgue measure is the **measure-zero phenomenon**: a set can be geometrically rich in one sense while being completely negligible from the standpoint of integration in a higher-dimensional space. A line in ℝ² has λ₂-measure zero. A plane in ℝ³ has λ₃-measure zero. More generally, any k-dimensional set (k < n), including smooth curves and surfaces, has **λₙ-measure zero**. The intuition: a lower-dimensional set has no "n-dimensional thickness," so it occupies no fraction of n-dimensional volume, no matter how it is oriented or how large it is.

This measure-zero fact is not merely aesthetic — it is operationally decisive. When you integrate over ℝⁿ, you can ignore what a function does on any set of measure zero without changing the integral. Changing the value of a function on a line, a surface, or even a countable dense set does not affect a Lebesgue integral. This is the precision behind the measure-theoretic notion of "almost everywhere," and it is what makes Lebesgue integration robust in ways that Riemann integration is not.
