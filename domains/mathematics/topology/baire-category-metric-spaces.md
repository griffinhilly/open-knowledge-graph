---
id: baire-category-metric-spaces
title: Baire Category Theorem for Metric Spaces
domain: mathematics
course: topology
prerequisites:
- id: completeness-metric-spaces-definition
  type: hard
tags:
- baire-category
- metric-spaces
stage: formal-systems
status: draft
---

# Baire Category Theorem for Metric Spaces

## Core Idea
The Baire category theorem: a complete metric space is not a countable union of nowhere-dense sets. Equivalently, every countable intersection of dense open sets is dense. This means complete metric spaces are 'large' topologically. Applications include the open mapping theorem, uniform boundedness principle, and proving existence of continuous nowhere-differentiable functions.

## Explainer

From your study of completeness, you know that a complete metric space has no "missing" limit points — every Cauchy sequence converges. The Baire category theorem reveals that completeness has a remarkable topological consequence: it makes a space "large" in a precise sense. To understand what large means here, you first need two definitions built from your metric-space intuition.

A set S is **nowhere dense** if its closure contains no open ball — equivalently, every open ball intersects the complement of S. Informally, a nowhere dense set has no "chunk." The integers ℤ inside ℝ are nowhere dense: the closure is ℤ itself, and no open interval sits entirely within ℤ. A **meager** set (also called "first category") is a countable union of nowhere-dense sets — a collection of sets each of which has no chunk. The rationals ℚ are meager in ℝ: enumerate the rationals as q₁, q₂, ..., and each singleton {qₙ} is nowhere dense. A set that is not meager is called **second category** or **non-meager**.

The Baire category theorem states: **a complete metric space is non-meager in itself**. Equivalently, it cannot be written as a countable union of nowhere-dense sets. The proof is an elegant application of completeness: if X = ⋃Fₙ where each Fₙ is nowhere dense, construct a Cauchy sequence by choosing nested closed balls, each avoiding the next Fₙ, with radii shrinking to zero — completeness forces this sequence to converge, but the limit point belongs to none of the Fₙ, a contradiction. Notice what this means for ℝ vs ℚ: ℚ is meager (a countable union of singletons), and ℚ is not complete. ℝ is complete, so it is non-meager — even though ℚ is dense in ℝ and "looks large," it is topologically small in this precise sense.

The power of the theorem is in its applications, which follow a common pattern: you express a "degenerate" scenario as a meager set, invoke completeness to rule out that scenario, and conclude that "generic" elements have a non-degenerate property. For example, continuous nowhere-differentiable functions: the set of continuous functions on [0,1] that are differentiable at even one point turns out to be meager in the complete metric space C([0,1]). Baire's theorem then guarantees that the complement is non-meager — meaning "most" continuous functions, in a precise topological sense, are nowhere differentiable. In functional analysis, the theorem underlies the **uniform boundedness principle** (a family of bounded linear operators bounded pointwise is uniformly bounded) and the **open mapping theorem** (a surjective bounded linear map between Banach spaces is open). These are cornerstones of functional analysis, and all ultimately rest on the completeness-implies-non-meagerness insight you now have.
