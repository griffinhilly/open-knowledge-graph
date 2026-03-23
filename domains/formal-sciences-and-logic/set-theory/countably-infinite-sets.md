---
id: countably-infinite-sets
title: Countably Infinite Sets
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: finite-sets-and-natural-numbers
  type: hard
- id: axiom-of-infinity
  type: soft
builds-toward:
- uncountable-sets-and-cantor-diagonalization
tags:
- countable
- infinite
- aleph-0
stage: formal-systems
status: validated
---

# Countably Infinite Sets

## Core Idea
A set is countably infinite if there exists a bijection with the natural numbers ℕ. Surprisingly, the integers ℤ, rationals ℚ, and all finite sequences from a countable alphabet are countably infinite, suggesting countability is 'larger' than finite but 'smaller' than other infinities.

## Questions

```yaml
- question: "The set of positive even numbers E = {2, 4, 6, 8, ...} is a proper subset of ℕ = {1, 2, 3, ...}. What does this tell us about the cardinality of E compared to ℕ?"
  type: multiple-choice
  options:
    - "E has strictly smaller cardinality than ℕ — a proper subset is always smaller"
    - "E has the same cardinality as ℕ — the bijection n ↦ 2n maps ℕ onto E one-to-one"
    - "E is uncountable since its elements grow without bound"
    - "The cardinality of E is undefined because it is a proper subset of an infinite set"
  answer: 1
  explanation: "For infinite sets, cardinality is defined by bijections, not by the subset relation. The function f(n) = 2n maps ℕ → E bijectively: every natural number maps to a distinct even number, and every even number is hit. So |E| = |ℕ| = ℵ₀. For infinite sets, a proper subset can have the same cardinality as the whole — in fact this property (having a proper subset of equal cardinality) is Dedekind's definition of what it means to be infinite."

- question: "Which of the following sets has cardinality strictly greater than ℵ₀?"
  type: multiple-choice
  options:
    - "The set of all integers ℤ"
    - "The set of all rational numbers ℚ"
    - "The set of all finite binary strings"
    - "The set of all real numbers in the interval [0, 1]"
  answer: 3
  explanation: "ℤ, ℚ, and all finite strings over any finite alphabet are countably infinite — each can be listed in a sequence via a bijection with ℕ. The real numbers in [0, 1] are uncountably infinite; Cantor's diagonalization argument shows no such listing is possible. Their cardinality is 2^ℵ₀, which is strictly greater than ℵ₀."

- question: "The rational numbers ℚ are countably infinite even though between any two rationals there are infinitely many more rationals."
  type: true-false
  answer: true
  explanation: "Density and cardinality are different properties. 'Dense' means no gaps in the ordering — between any two rationals lie infinitely many more. 'Countably infinite' means a bijection with ℕ exists. Cantor's diagonal enumeration constructs this bijection by arranging all fractions in an infinite grid and tracing a diagonal path, visiting every rational exactly once. ℚ is dense in ℝ but still countable; density is a topological property, not a cardinality property."

- question: "If A is a proper subset of B (A ⊊ B), then A has strictly fewer elements than B."
  type: true-false
  answer: false
  explanation: "This is true for finite sets but fails completely for infinite ones. The even integers are a proper subset of ℤ, yet both have cardinality ℵ₀. The natural numbers are a proper subset of the rationals, yet |ℕ| = |ℚ| = ℵ₀. Having a proper subset of the same cardinality is not just possible for infinite sets — it is their defining characteristic (Dedekind's definition of infinity). Intuitions built on finite sets do not transfer to infinite ones."

- question: "The rational numbers seem far denser than the integers, yet both are countably infinite. Explain what 'countably infinite' means and why density doesn't determine countability."
  type: short-answer
  answer: "A set is countably infinite if there exists a bijection with ℕ — equivalently, all its elements can be arranged in a sequence s₁, s₂, s₃, ... with no repetitions or omissions. Density describes how elements are spaced within their natural ordering (ℚ is dense — no gaps between rationals; ℤ is not). But density says nothing about whether a bijection with ℕ can be constructed. Cantor showed such a bijection exists for ℚ by arranging all fractions in a grid and tracing a diagonal path. What distinguishes countable from uncountable sets is whether any listing is possible at all."
  explanation: "The moral is that infinite cardinality is determined by bijections, not by intuitive notions of size, density, or subset. ℚ being dense in ℝ says something about the order topology — rationals cluster near every real number. That's a topological statement, not a cardinality statement. The two properties are independent: ℚ is dense and countable; the Cantor set is uncountable but nowhere dense. Cantor's diagonalization (the next topic) shows why ℝ escapes every attempted listing."
```

## Explainer

From finite sets and natural numbers, you know that two sets have the same size when there is a **bijection** (a one-to-one, onto function) between them. For finite sets this agrees with counting: {a, b, c} has 3 elements because it bijects with {1, 2, 3}. The same definition extends to infinite sets, but now produces genuinely surprising results. A set S is **countably infinite** if there is a bijection f : ℕ → S. Equivalently, you can list all elements of S in a sequence s₁, s₂, s₃, … with no repetitions and no omissions. The cardinality of any countably infinite set is **ℵ₀** (aleph-null), the first transfinite cardinal.

The first surprise: the integers ℤ are countably infinite, even though ℤ seems "twice as big" as ℕ (it has negative numbers too). The bijection is the interleaving sequence: 0, 1, −1, 2, −2, 3, −3, … This lists every integer exactly once. Formally, f(n) = n/2 if n is even, f(n) = −(n+1)/2 if n is odd. The lesson is that for infinite sets, a proper subset can have the same cardinality as the whole — ℕ ⊂ ℤ but |ℕ| = |ℤ| = ℵ₀. This is actually a defining property of infinite sets (Dedekind's definition of infinity).

The second surprise: the rationals ℚ are countably infinite, even though between any two rationals there are infinitely many more. The bijection uses **Cantor's diagonal enumeration** of ℤ × ℤ. Arrange all fractions p/q (with q > 0) in an infinite grid: row p, column q. Trace a diagonal zigzag path through the grid — (0/1), (1/1), (0/2), (−1/1), (1/2), (0/3), … — skipping any fraction that reduces to one already seen. This visits every rational exactly once and defines the bijection. The key insight is that a **countable union of countable sets is countable**: ℚ = ∪_{q≥1} {p/q : p ∈ ℤ}, a countable union of countable sets (one for each denominator q). More generally, any finite Cartesian product of countable sets is countable, and so are all finite strings over a countable alphabet (used heavily in computability theory to code programs as natural numbers).

The reason these results feel paradoxical is that our intuition of "more" tracks density or packing, not cardinality. ℚ is dense in ℝ while ℕ is not — but density and cardinality are different properties. What distinguishes ℕ, ℤ, and ℚ from ℝ is not how "packed" they are, but whether they can be listed. Cantor's diagonalization argument (the next topic) will show that ℝ cannot be listed — its cardinality strictly exceeds ℵ₀. The countably infinite sets form a precise boundary: everything listable lands here, and everything that eludes any listing is uncountably infinite.

