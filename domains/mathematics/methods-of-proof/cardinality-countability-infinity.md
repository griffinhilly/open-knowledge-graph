---
id: cardinality-countability-infinity
title: Cardinality and Countability
domain: mathematics
course: methods-of-proof
prerequisites:
- id: function-composition-and-inverses
  type: hard
tags:
- cardinality
- infinity
- countability
stage: formal-systems
status: draft
---

# Cardinality and Countability

## Core Idea
Two sets have the same cardinality if there exists a bijection between them, extending the notion of 'size' to infinite sets. Countable sets are finite or in bijection with ℕ; uncountable sets like ℝ represent a 'larger' infinity. Cantor's diagonalization proves that no set is in bijection with its power set, revealing an infinite hierarchy of infinities.

## Explainer

From your work with function composition and inverses, you know what a **bijection** is: a function that is both injective (no two inputs share an output) and surjective (every output is hit). Cardinality uses bijections as the measuring instrument for set size. Two sets A and B have the **same cardinality** — written |A| = |B| — if there exists a bijection f: A → B. For finite sets, this agrees with ordinary counting: a bijection between {a, b, c} and {1, 2, 3} pairs every element with exactly one partner, confirming they both have three elements.

The surprising richness begins with infinite sets. Galileo noticed a paradox: the perfect squares {1, 4, 9, 16, ...} seem far fewer than the natural numbers ℕ, yet the bijection n ↦ n² pairs them perfectly. Cantor's key move was to embrace this: infinite sets that can be put in bijection with ℕ are called **countably infinite**, and they are all the "same size" as ℕ. The integers ℤ are countable — list them as 0, 1, −1, 2, −2, ... and you have a bijection with ℕ. The rationals ℚ are also countable, via a diagonal enumeration of all fractions p/q arranged in a grid. These results challenge intuition but are provably correct.

Now comes the genuinely startling result: ℝ is **uncountable** — no bijection between ℕ and ℝ can exist. Cantor's **diagonal argument** proves this by contradiction. Suppose you had a list r₁, r₂, r₃, ... purporting to enumerate all reals in [0, 1]. Construct a new number x: let the nth decimal digit of x differ from the nth decimal digit of rₙ (say, use 1 if that digit is 2, and 2 otherwise). Then x is in [0, 1] but differs from rₙ at the nth decimal place for every n — so x is not on the list, contradicting the assumption that the list was complete. The argument works no matter which list you start with, so no complete list exists, and [0, 1] is uncountable.

The power set hierarchy extends this insight infinitely. **Cantor's theorem** states that for any set A, the power set P(A) — the set of all subsets of A — has strictly larger cardinality than A: |A| < |P(A)|. The proof uses the same diagonal idea as before. If f: A → P(A) were a bijection, consider D = {a ∈ A : a ∉ f(a)}. Then D is a subset of A but D ≠ f(a) for any a (checking each case produces a contradiction). Since D is in P(A) but not in the image of f, no bijection can exist. Applying this repeatedly: |ℕ| < |P(ℕ)| < |P(P(ℕ))| < ..., producing an infinite tower of strictly larger infinities. There is no "largest" infinite set, and infinity comes in infinitely many sizes.
