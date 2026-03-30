---
id: baire-category-metric-spaces
title: Baire Category Theorem for Metric Spaces
domain: mathematics
course: topology
prerequisites:
- id: completeness-metric-spaces
  type: hard
tags:
- baire-category
- metric-spaces
stage: expert
status: validated
---

# Baire Category Theorem for Metric Spaces

## Core Idea
The Baire category theorem: a complete metric space is not a countable union of nowhere-dense sets. Equivalently, every countable intersection of dense open sets is dense. This means complete metric spaces are 'large' topologically. Applications include the open mapping theorem, uniform boundedness principle, and proving existence of continuous nowhere-differentiable functions.

## Questions

```yaml
- question: "The rational numbers ℚ are dense in ℝ — every open interval contains a rational. Does this make ℚ a 'large' set in the Baire category sense?"
  type: multiple-choice
  options:
    - "Yes; a dense set is non-meager by definition in any metric space"
    - "Yes; density implies non-meagerness because dense sets 'fill' the space"
    - "No; ℚ is meager — a countable union of singletons, each nowhere dense — even though it is dense in ℝ"
    - "No; ℚ is meager because countable sets are always meager in any metric space"
  answer: 2
  explanation: "Density and meagerness are independent properties. ℚ is dense in ℝ (every open interval contains a rational), yet it is meager: enumerate the rationals q₁, q₂, ..., and each singleton {qₙ} is nowhere dense (its closure is itself, containing no open interval). Their countable union is ℚ — meager by definition. This shows that a set can be topologically 'everywhere present' (dense) yet categorically 'small' (meager). Baire category measures a different dimension of size than density."

- question: "The Baire Category Theorem guarantees that a complete metric space X cannot be written as a countable union of nowhere-dense sets. What does this directly imply?"
  type: multiple-choice
  options:
    - "Each individual nowhere-dense set in X has positive Lebesgue measure"
    - "The union of countably many nowhere-dense sets must miss at least one point of X"
    - "The intersection of the nowhere-dense sets is empty"
    - "The nowhere-dense sets must form a finite collection"
  answer: 1
  explanation: "The theorem says the countable union of nowhere-dense sets cannot equal all of X — it must miss at least a point (in fact, a dense Gδ set of points). This is the direct content of the theorem. Option A is wrong because nowhere-dense sets can have positive measure. Option C is wrong because the intersection of the Fₙ could be non-empty. Option D is wrong because the theorem applies to countably infinite collections, not just finite ones."

- question: "A meager set in ℝ can rarely be dense in ℝ."
  type: true-false
  answer: false
  explanation: "ℚ is the standard counterexample: it is both meager (a countable union of nowhere-dense singletons) and dense in ℝ (every open interval contains a rational). Density and meagerness measure different properties. Density says the set comes arbitrarily close to every point; meagerness says the set is a 'thin' union of sets with no interior. A set can be simultaneously thin (meager) and everywhere present (dense)."

- question: "The Baire Category Theorem has an equivalent formulation: in a complete metric space, every countable intersection of dense open sets is itself dense."
  type: true-false
  answer: true
  explanation: "This is the standard dual formulation. Taking complements: a set is nowhere dense if and only if its complement contains a dense open set. So a countable union of nowhere-dense sets corresponds (via complement) to a countable intersection of dense open sets. The theorem saying 'the union doesn't cover X' is equivalent to saying 'the intersection is non-empty (and in fact dense).' Both formulations capture the same content: complete metric spaces are topologically 'large.'"

- question: "Why does the Baire Category Theorem require completeness, and what breaks down in an incomplete metric space?"
  type: short-answer
  answer: "The proof constructs a Cauchy sequence by choosing nested closed balls, each shrinking in radius and each avoiding the next nowhere-dense set Fₙ. Completeness guarantees this Cauchy sequence converges to a limit point — and that limit point avoids every Fₙ, providing the contradiction. Without completeness, the Cauchy sequence might not converge in the space, and the contradiction fails. The rationals ℚ confirm this is necessary: ℚ is not complete, and ℚ is a countable union of singletons (each nowhere dense), which would violate the Baire conclusion — showing completeness cannot be dropped."
  explanation: "The key step 'the Cauchy sequence converges' is exactly where completeness enters. This is not a technicality — it is the heart of the proof. The theorem is false for incomplete spaces, so the condition is necessary, not just sufficient. Understanding this also shows why the theorem is a result about complete metric spaces specifically, not about arbitrary metric or topological spaces."
```

## Explainer

From your study of completeness, you know that a complete metric space has no "missing" limit points — every Cauchy sequence converges. The Baire category theorem reveals that completeness has a remarkable topological consequence: it makes a space "large" in a precise sense. To understand what large means here, you first need two definitions built from your metric-space intuition.

A set S is **nowhere dense** if its closure contains no open ball — equivalently, every open ball intersects the complement of S. Informally, a nowhere dense set has no "chunk." The integers ℤ inside ℝ are nowhere dense: the closure is ℤ itself, and no open interval sits entirely within ℤ. A **meager** set (also called "first category") is a countable union of nowhere-dense sets — a collection of sets each of which has no chunk. The rationals ℚ are meager in ℝ: enumerate the rationals as q₁, q₂, ..., and each singleton {qₙ} is nowhere dense. A set that is not meager is called **second category** or **non-meager**.

The Baire category theorem states: **a complete metric space is non-meager in itself**. Equivalently, it cannot be written as a countable union of nowhere-dense sets. The proof is an elegant application of completeness: if X = ⋃Fₙ where each Fₙ is nowhere dense, construct a Cauchy sequence by choosing nested closed balls, each avoiding the next Fₙ, with radii shrinking to zero — completeness forces this sequence to converge, but the limit point belongs to none of the Fₙ, a contradiction. Notice what this means for ℝ vs ℚ: ℚ is meager (a countable union of singletons), and ℚ is not complete. ℝ is complete, so it is non-meager — even though ℚ is dense in ℝ and "looks large," it is topologically small in this precise sense.

The power of the theorem is in its applications, which follow a common pattern: you express a "degenerate" scenario as a meager set, invoke completeness to rule out that scenario, and conclude that "generic" elements have a non-degenerate property. For example, continuous nowhere-differentiable functions: the set of continuous functions on [0,1] that are differentiable at even one point turns out to be meager in the complete metric space C([0,1]). Baire's theorem then guarantees that the complement is non-meager — meaning "most" continuous functions, in a precise topological sense, are nowhere differentiable. In functional analysis, the theorem underlies the **uniform boundedness principle** (a family of bounded linear operators bounded pointwise is uniformly bounded) and the **open mapping theorem** (a surjective bounded linear map between Banach spaces is open). These are cornerstones of functional analysis, and all ultimately rest on the completeness-implies-non-meagerness insight you now have.
