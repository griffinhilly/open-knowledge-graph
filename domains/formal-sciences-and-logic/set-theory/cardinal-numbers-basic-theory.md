---
id: cardinal-numbers-basic-theory
title: Cardinal Numbers and Cardinality
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: injections-surjections-and-inverse-functions
  type: hard
- id: equivalence-relations-and-equivalence-classes
  type: soft
builds-toward:
- cardinal-comparison-and-schroeder-bernstein
- aleph-and-beth-hierarchy-introduction
- cardinal-arithmetic
tags:
- cardinals
- cardinality
- equivalence-classes
stage: formal-systems
status: draft
---

# Cardinal Numbers and Cardinality

## Core Idea
Cardinal numbers measure the 'size' of sets: the cardinality of S is the equivalence class of all sets bijective with S. Two sets have the same cardinality iff there is a bijection between them. Cardinals are partially ordered by injection: |A| ≤ |B| if there exists an injection from A to B.

## Explainer

You already know from your prerequisites what injections, surjections, and bijections are. Cardinality formalizes the intuitive notion of "same size" using bijections: two sets A and B have the **same cardinality** if and only if there exists a bijection f : A → B — a function that pairs every element of A with a unique element of B, leaving nothing out. For finite sets, this matches counting: you can pair up two sets of size 3 perfectly, but not a set of size 3 with one of size 4. Cardinal numbers generalize this to infinite sets, where size becomes genuinely surprising.

The first surprise: ℕ (the natural numbers) and ℤ (the integers) have the same cardinality, even though ℤ seems "twice as large." The bijection is a simple interleaving: 0 → 0, 1 → 1, 2 → −1, 3 → 2, 4 → −2, ..., hitting every integer exactly once. Similarly, ℕ and ℚ (the rationals) have the same cardinality via Cantor's diagonal enumeration of fractions — list all fractions in a grid and traverse it diagonally. Any set in bijection with ℕ is called **countably infinite**, the smallest infinity, designated **ℵ₀** (aleph-null). This seems strange from a naive "size" perspective, but it is exactly what the definition delivers: countability means you can list all elements in a sequence indexed by ℕ, even if that listing requires a clever pattern.

The **ordering** of cardinals is given by injections: |A| ≤ |B| iff there is an injection A → B (you can embed A inside B without collision). Strict inequality |A| < |B| means an injection A → B exists but no bijection does. **Cantor's theorem** establishes that the power set P(A) always has strictly greater cardinality than A: |A| < |P(A)| for every set A. The proof is a diagonal argument: suppose f : A → P(A) is any function; then the set D = {a ∈ A : a ∉ f(a)} is not in the range of f (if it were, say f(d) = D, then d ∈ D iff d ∉ D — a contradiction). Applied to ℕ, this gives the **uncountability of the reals**: |ℝ| = |P(ℕ)| > ℵ₀. The reals cannot be listed in any sequence indexed by ℕ — there are genuinely "more" real numbers than natural numbers.

In ZFC set theory, each infinite cardinal is identified with the smallest ordinal of that cardinality — a **von Neumann cardinal**. The infinite cardinals form the **aleph hierarchy**: ℵ₀ < ℵ₁ < ℵ₂ < ..., where ℵ₁ is the smallest uncountable cardinal. Cardinal arithmetic extends the usual operations: for infinite cardinals κ, both κ + κ = κ and κ · κ = κ (infinite cardinals absorb finite additions and multiplications). Cardinal **exponentiation** is more subtle: 2^ℵ₀ = |ℝ| is the cardinality of the continuum, but its exact position in the aleph hierarchy — is it ℵ₁? ℵ₂? Something larger? — is not determined by ZFC. This is the **Continuum Hypothesis** (CH), which you will encounter in the next topics: it is independent of ZFC, meaning neither CH nor its negation can be proved from the axioms.
