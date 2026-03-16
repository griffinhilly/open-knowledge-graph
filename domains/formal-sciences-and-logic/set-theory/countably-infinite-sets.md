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
status: draft
---

# Countably Infinite Sets

## Core Idea
A set is countably infinite if there exists a bijection with the natural numbers ℕ. Surprisingly, the integers ℤ, rationals ℚ, and all finite sequences from a countable alphabet are countably infinite, suggesting countability is 'larger' than finite but 'smaller' than other infinities.

## Explainer

From finite sets and natural numbers, you know that two sets have the same size when there is a **bijection** (a one-to-one, onto function) between them. For finite sets this agrees with counting: {a, b, c} has 3 elements because it bijects with {1, 2, 3}. The same definition extends to infinite sets, but now produces genuinely surprising results. A set S is **countably infinite** if there is a bijection f : ℕ → S. Equivalently, you can list all elements of S in a sequence s₁, s₂, s₃, … with no repetitions and no omissions. The cardinality of any countably infinite set is **ℵ₀** (aleph-null), the first transfinite cardinal.

The first surprise: the integers ℤ are countably infinite, even though ℤ seems "twice as big" as ℕ (it has negative numbers too). The bijection is the interleaving sequence: 0, 1, −1, 2, −2, 3, −3, … This lists every integer exactly once. Formally, f(n) = n/2 if n is even, f(n) = −(n+1)/2 if n is odd. The lesson is that for infinite sets, a proper subset can have the same cardinality as the whole — ℕ ⊂ ℤ but |ℕ| = |ℤ| = ℵ₀. This is actually a defining property of infinite sets (Dedekind's definition of infinity).

The second surprise: the rationals ℚ are countably infinite, even though between any two rationals there are infinitely many more. The bijection uses **Cantor's diagonal enumeration** of ℤ × ℤ. Arrange all fractions p/q (with q > 0) in an infinite grid: row p, column q. Trace a diagonal zigzag path through the grid — (0/1), (1/1), (0/2), (−1/1), (1/2), (0/3), … — skipping any fraction that reduces to one already seen. This visits every rational exactly once and defines the bijection. The key insight is that a **countable union of countable sets is countable**: ℚ = ∪_{q≥1} {p/q : p ∈ ℤ}, a countable union of countable sets (one for each denominator q). More generally, any finite Cartesian product of countable sets is countable, and so are all finite strings over a countable alphabet (used heavily in computability theory to code programs as natural numbers).

The reason these results feel paradoxical is that our intuition of "more" tracks density or packing, not cardinality. ℚ is dense in ℝ while ℕ is not — but density and cardinality are different properties. What distinguishes ℕ, ℤ, and ℚ from ℝ is not how "packed" they are, but whether they can be listed. Cantor's diagonalization argument (the next topic) will show that ℝ cannot be listed — its cardinality strictly exceeds ℵ₀. The countably infinite sets form a precise boundary: everything listable lands here, and everything that eludes any listing is uncountably infinite.

