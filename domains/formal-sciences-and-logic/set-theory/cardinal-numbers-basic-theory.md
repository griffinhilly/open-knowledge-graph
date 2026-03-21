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

## Questions

```yaml
- question: "A student argues that the set of even natural numbers E = {0, 2, 4, 6, …} has 'half as many' elements as ℕ = {0, 1, 2, 3, …}, so |E| < |ℕ|. What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "The student is correct — E is a proper subset of ℕ so it must have strictly smaller cardinality"
    - "The bijection f(n) = 2n shows every natural number maps to a unique even number and vice versa, so |E| = |ℕ|"
    - "E is finite (it lists every even number up to some bound) so the comparison doesn't apply"
    - "Cardinality is only defined for finite sets; infinite sets cannot be compared by size"
  answer: 1
  explanation: "The bijection f : ℕ → E defined by f(n) = 2n pairs every natural number with a unique even number and hits every even number exactly once. Since a bijection exists, |E| = |ℕ| by definition. The student's intuition — that a proper subset must be smaller — is correct for finite sets but fails for infinite ones. For infinite sets, a proper subset can be in bijection with the whole set. This is sometimes taken as the defining property of infinite sets (the Dedekind-infinite property). Cardinality for infinite sets is defined purely by bijection, not by 'how many' elements in the intuitive counting sense."

- question: "Cantor's theorem states |A| < |P(A)| for every set A. What does this immediately imply about |ℝ| compared to |ℕ|?"
  type: multiple-choice
  options:
    - "Nothing — Cantor's theorem applies only to finite sets"
    - "ℝ and ℕ have the same cardinality because both are infinite"
    - "|ℝ| > |ℕ|, because |P(ℕ)| > |ℕ| and it can be shown that |ℝ| = |P(ℕ)|"
    - "|ℝ| > |ℕ| by Cantor's theorem applied directly to ℕ ⊂ ℝ"
  answer: 2
  explanation: "By Cantor's theorem, |ℕ| < |P(ℕ)|. Separately, it can be shown that |ℝ| = |P(ℕ)| = 2^ℵ₀ (the reals are in bijection with the power set of ℕ, e.g., via binary expansions). Combining these: |ℕ| < |P(ℕ)| = |ℝ|, so the reals are strictly more numerous than the naturals. Option D sounds plausible (ℕ ⊂ ℝ) but is wrong: a proper subset relation does not imply strict cardinality inequality for infinite sets — ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ, yet |ℕ| = |ℤ| = |ℚ| < |ℝ|. The strictly greater cardinality of ℝ requires Cantor's diagonal argument, not just the subset relation."

- question: "There exists a bijection between the natural numbers ℕ and the rational numbers ℚ, so they have the same cardinality ℵ₀."
  type: true-false
  answer: true
  explanation: "This is one of the most surprising results in set theory. Cantor showed that ℚ is countably infinite by constructing an enumeration: list all fractions a/b (in lowest terms, a ∈ ℤ, b ∈ ℕ⁺) in a grid and traverse it diagonally, skipping duplicates. This visits every rational number exactly once, providing a bijection with ℕ. Intuitively, ℚ seems 'denser' than ℕ (between any two integers lie infinitely many rationals), yet they have the same cardinality. Density on the number line is a different concept from cardinality. Any set that can be listed in a sequence indexed by ℕ (even with a clever non-obvious ordering) is countably infinite."

- question: "Since the set of integers ℤ contains the natural numbers ℕ as a proper subset, ℤ must have strictly greater cardinality than ℕ."
  type: true-false
  answer: false
  explanation: "This is the central misconception the topic addresses. For infinite sets, containing a set as a proper subset does NOT imply strictly greater cardinality. The bijection f : ℕ → ℤ defined by the interleaving 0 → 0, 1 → 1, 2 → −1, 3 → 2, 4 → −2, … pairs every natural number with a unique integer and covers all integers. Since a bijection exists, |ℕ| = |ℤ|, even though ℕ ⊊ ℤ. The property 'a proper subset can be in bijection with the whole set' is actually characteristic of infinite sets (Dedekind's definition of infinite). For finite sets, every proper subset does have strictly smaller cardinality."

- question: "Explain what it means for two infinite sets to have the same cardinality, and give an example of two infinite sets with DIFFERENT cardinalities. Explain how we know they are different."
  type: short-answer
  answer: "Two sets have the same cardinality iff there exists a bijection between them — a function pairing every element of one with exactly one element of the other, with no elements left over on either side. ℕ and ℝ have different cardinalities: |ℕ| < |ℝ|. We know this because Cantor's diagonal argument proves no function ℕ → ℝ can be a surjection: for any proposed list of reals, you can construct a real number differing from the nth listed number in its nth decimal place, so it's not in the list."
  explanation: "The diagonal argument is the key tool for proving two sets have different infinite cardinalities. It shows that any attempt to list the reals in a sequence indexed by ℕ necessarily misses some real — the diagonal construction always finds one not in the list. This proves ℝ is uncountably infinite: it cannot be put in bijection with ℕ. The contrast with ℚ (countable) is striking: although ℚ is dense in ℝ (between any two reals lies a rational), ℚ can be enumerated (listed) while ℝ cannot. Density and cardinality are genuinely different properties."
```

## Explainer

You already know from your prerequisites what injections, surjections, and bijections are. Cardinality formalizes the intuitive notion of "same size" using bijections: two sets A and B have the **same cardinality** if and only if there exists a bijection f : A → B — a function that pairs every element of A with a unique element of B, leaving nothing out. For finite sets, this matches counting: you can pair up two sets of size 3 perfectly, but not a set of size 3 with one of size 4. Cardinal numbers generalize this to infinite sets, where size becomes genuinely surprising.

The first surprise: ℕ (the natural numbers) and ℤ (the integers) have the same cardinality, even though ℤ seems "twice as large." The bijection is a simple interleaving: 0 → 0, 1 → 1, 2 → −1, 3 → 2, 4 → −2, ..., hitting every integer exactly once. Similarly, ℕ and ℚ (the rationals) have the same cardinality via Cantor's diagonal enumeration of fractions — list all fractions in a grid and traverse it diagonally. Any set in bijection with ℕ is called **countably infinite**, the smallest infinity, designated **ℵ₀** (aleph-null). This seems strange from a naive "size" perspective, but it is exactly what the definition delivers: countability means you can list all elements in a sequence indexed by ℕ, even if that listing requires a clever pattern.

The **ordering** of cardinals is given by injections: |A| ≤ |B| iff there is an injection A → B (you can embed A inside B without collision). Strict inequality |A| < |B| means an injection A → B exists but no bijection does. **Cantor's theorem** establishes that the power set P(A) always has strictly greater cardinality than A: |A| < |P(A)| for every set A. The proof is a diagonal argument: suppose f : A → P(A) is any function; then the set D = {a ∈ A : a ∉ f(a)} is not in the range of f (if it were, say f(d) = D, then d ∈ D iff d ∉ D — a contradiction). Applied to ℕ, this gives the **uncountability of the reals**: |ℝ| = |P(ℕ)| > ℵ₀. The reals cannot be listed in any sequence indexed by ℕ — there are genuinely "more" real numbers than natural numbers.

In ZFC set theory, each infinite cardinal is identified with the smallest ordinal of that cardinality — a **von Neumann cardinal**. The infinite cardinals form the **aleph hierarchy**: ℵ₀ < ℵ₁ < ℵ₂ < ..., where ℵ₁ is the smallest uncountable cardinal. Cardinal arithmetic extends the usual operations: for infinite cardinals κ, both κ + κ = κ and κ · κ = κ (infinite cardinals absorb finite additions and multiplications). Cardinal **exponentiation** is more subtle: 2^ℵ₀ = |ℝ| is the cardinality of the continuum, but its exact position in the aleph hierarchy — is it ℵ₁? ℵ₂? Something larger? — is not determined by ZFC. This is the **Continuum Hypothesis** (CH), which you will encounter in the next topics: it is independent of ZFC, meaning neither CH nor its negation can be proved from the axioms.
