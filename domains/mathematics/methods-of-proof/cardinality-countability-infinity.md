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

## Questions

```yaml
- question: "A student argues: 'The set of even numbers is strictly smaller than ℕ, because it is missing all the odd numbers — every even number is in ℕ but not vice versa.' What is the correct response?"
  type: multiple-choice
  options:
    - "The student is correct — the even numbers are a proper subset, so they must have smaller cardinality"
    - "The student is wrong — the even numbers are not a proper subset of ℕ"
    - "The student is wrong — the function n ↦ 2n is a bijection between ℕ and the evens, so they have the same cardinality"
    - "The student is partially right — the even numbers are countably infinite, which is smaller than ℕ's uncountable infinity"
  answer: 2
  explanation: "For infinite sets, 'proper subset' does not imply 'smaller cardinality.' Cardinality is defined by bijection, not containment. The map n ↦ 2n is a bijection from ℕ to the even numbers: every natural number is paired with exactly one even number, and every even number is hit. So |ℕ| = |evens| even though the evens are a proper subset. This is Galileo's paradox — one of the genuinely counterintuitive features of infinite sets that Cantor embraced rather than avoided."

- question: "Cantor's diagonal argument proves ℝ is uncountable by:"
  type: multiple-choice
  options:
    - "Showing that ℝ has more elements than ℕ by direct counting"
    - "Assuming a complete list of all reals in [0,1] exists, then constructing a real number that differs from each listed number at a specific decimal position — so it cannot be on the list"
    - "Proving that no bijection between ℕ and ℝ can be written down in finite time"
    - "Using the power set of ℕ to show ℝ has strictly more subsets than ℕ has elements"
  answer: 1
  explanation: "The diagonal argument is a proof by contradiction. Assume a complete enumeration r₁, r₂, r₃, ... of all reals in [0,1] exists. Construct x so that its nth decimal digit differs from the nth decimal digit of rₙ. Then x ∈ [0,1] but x ≠ rₙ for every n — so x is not on the supposed complete list. The contradiction shows no such list can exist. The power in the argument is that it works for any list you could name, not just specific ones."

- question: "The rationals ℚ have greater cardinality than the integers ℤ, since between any two integers there are infinitely many rationals."
  type: true-false
  answer: false
  explanation: "Both ℤ and ℚ are countably infinite — they both have cardinality ℵ₀, the same as ℕ. Despite the dense ordering of ℚ (infinitely many rationals between any two integers), a bijection between ℕ and ℚ exists via a diagonal enumeration of all fractions p/q in a grid. The 'density' of ℚ in ℝ is a topological property, not a cardinality property. Cardinality is about bijections, not about order or density."

- question: "For any set A, infinite or finite, the power set P(A) has strictly greater cardinality than A."
  type: true-false
  answer: true
  explanation: "This is Cantor's theorem. The proof is a generalization of the diagonal argument: suppose f: A → P(A) is a bijection. Define D = {a ∈ A : a ∉ f(a)}. Then D ∈ P(A) but D ≠ f(a) for any a (checking a ∈ D and a ∉ D both produce contradictions). So no bijection can exist, and |P(A)| > |A|. This holds for finite sets too (a 3-element set has 2³ = 8 subsets), but for infinite sets it produces an infinite tower of strictly larger infinities."

- question: "The function n ↦ n² pairs every natural number with a perfect square. Explain why this shows that ℕ and the perfect squares have the same cardinality, even though every perfect square is in ℕ but not vice versa."
  type: short-answer
  answer: "Cardinality is defined by the existence of a bijection, not by containment. The function f(n) = n² is injective (different inputs produce different outputs: n² = m² implies n = m for positive integers) and surjective onto the perfect squares (every perfect square k² is hit by f(k)). So it is a bijection from ℕ to the perfect squares, which by definition means they have the same cardinality. The fact that the perfect squares are a proper subset of ℕ is irrelevant to cardinality for infinite sets."
  explanation: "This is precisely Galileo's paradox, resolved by Cantor's definition. In everyday counting, a proper subset is always smaller. But 'smaller' in that sense means the subset fails to contain some elements of the superset — it says nothing about whether a perfect pairing (bijection) exists. For infinite sets, such bijections can always be found between a set and many of its proper subsets. This is what makes infinite sets genuinely different from finite ones, and it is the foundational insight that makes all of cardinality theory possible."
```

## Explainer

From your work with function composition and inverses, you know what a **bijection** is: a function that is both injective (no two inputs share an output) and surjective (every output is hit). Cardinality uses bijections as the measuring instrument for set size. Two sets A and B have the **same cardinality** — written |A| = |B| — if there exists a bijection f: A → B. For finite sets, this agrees with ordinary counting: a bijection between {a, b, c} and {1, 2, 3} pairs every element with exactly one partner, confirming they both have three elements.

The surprising richness begins with infinite sets. Galileo noticed a paradox: the perfect squares {1, 4, 9, 16, ...} seem far fewer than the natural numbers ℕ, yet the bijection n ↦ n² pairs them perfectly. Cantor's key move was to embrace this: infinite sets that can be put in bijection with ℕ are called **countably infinite**, and they are all the "same size" as ℕ. The integers ℤ are countable — list them as 0, 1, −1, 2, −2, ... and you have a bijection with ℕ. The rationals ℚ are also countable, via a diagonal enumeration of all fractions p/q arranged in a grid. These results challenge intuition but are provably correct.

Now comes the genuinely startling result: ℝ is **uncountable** — no bijection between ℕ and ℝ can exist. Cantor's **diagonal argument** proves this by contradiction. Suppose you had a list r₁, r₂, r₃, ... purporting to enumerate all reals in [0, 1]. Construct a new number x: let the nth decimal digit of x differ from the nth decimal digit of rₙ (say, use 1 if that digit is 2, and 2 otherwise). Then x is in [0, 1] but differs from rₙ at the nth decimal place for every n — so x is not on the list, contradicting the assumption that the list was complete. The argument works no matter which list you start with, so no complete list exists, and [0, 1] is uncountable.

The power set hierarchy extends this insight infinitely. **Cantor's theorem** states that for any set A, the power set P(A) — the set of all subsets of A — has strictly larger cardinality than A: |A| < |P(A)|. The proof uses the same diagonal idea as before. If f: A → P(A) were a bijection, consider D = {a ∈ A : a ∉ f(a)}. Then D is a subset of A but D ≠ f(a) for any a (checking each case produces a contradiction). Since D is in P(A) but not in the image of f, no bijection can exist. Applying this repeatedly: |ℕ| < |P(ℕ)| < |P(P(ℕ))| < ..., producing an infinite tower of strictly larger infinities. There is no "largest" infinite set, and infinity comes in infinitely many sizes.
