---
id: dense-sets-and-nowhere-dense
title: Dense Sets and Nowhere Dense Sets
domain: mathematics
course: topology
prerequisites:
- id: closure-interior-and-boundary
  type: hard
builds-toward:
- separability-topology
- baire-category-theorem
tags:
- dense-sets
- nowhere-dense
- meager-sets
stage: advanced
status: draft
---

# Dense Sets and Nowhere Dense Sets

## Core Idea
A set is dense if its closure is the whole space—intuitively, its points are everywhere. A set is nowhere dense if its closure has empty interior. The study of dense sets leads to the Baire category theorem, which shows that complete metric spaces cannot be expressed as countable unions of nowhere dense sets, providing a powerful tool for existence arguments.

## Explainer

From your prerequisite on **closure, interior, and boundary**, you know that cl(A) is the smallest closed set containing A, and int(A) is the largest open set contained in A. Dense sets and nowhere dense sets are defined in terms of these operations, so the definitions come with immediate geometric meaning. A set A ⊆ X is **dense** in X if cl(A) = X — every point of X is either in A or is a limit point of A, meaning every open set contains a point of A. Intuitively, A's points are "everywhere present" in X: no matter where you look in X, you find points of A nearby.

The canonical dense set is ℚ inside ℝ: between any two real numbers lies a rational, so every open interval contains rationals, so cl(ℚ) = ℝ. What makes this striking is that ℚ is countable and, in a measure-theoretic sense, "negligible" (it has Lebesgue measure zero). Yet it is topologically everywhere present. This shows that topological density is genuinely different from measure-theoretic density — the two notions of "size" answer different questions and do not track each other.

A set A is **nowhere dense** if int(cl(A)) = ∅ — its closure contains no open set. The integers ℤ in ℝ are nowhere dense: cl(ℤ) = ℤ itself (ℤ is closed), and ℤ contains no open interval. A more sophisticated example is the **Cantor set** C ⊆ [0,1]: C is closed, so cl(C) = C, and C contains no open interval (its complement is open and dense), so C is nowhere dense. Yet C is uncountable — it has the same cardinality as ℝ. Nowhere dense sets are "topologically thin" in a way that cardinality does not capture.

The **Baire Category Theorem** elevates these definitions into a powerful existence tool. It says: in a complete metric space (or locally compact Hausdorff space), the whole space cannot be written as a countable union of nowhere dense sets. A set expressible as a countable union of nowhere dense sets is called **meager** (or "of first category"); the theorem says the ambient space is **non-meager**. This lets analysts prove that "generic" elements of a function space have extreme properties, without constructing a single example. The classic application: the continuous functions on [0,1] that are differentiable at even one point form a meager subset of C([0,1]) — so in a precise topological sense, *most* continuous functions are nowhere differentiable, even though constructing an explicit example (like the Weierstrass function) requires significant work.
