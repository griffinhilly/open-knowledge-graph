---
id: derangements
title: Derangements and Fixed-Point-Free Permutations
domain: mathematics
course: discrete-math
prerequisites:
- id: permutations-and-arrangements
  type: hard
- id: inclusion-exclusion-principle
  type: soft
tags:
- combinatorics
- permutations
stage: formal-systems
status: validated
---

# Derangements and Fixed-Point-Free Permutations

## Core Idea
A derangement is a permutation where no element appears in its original position. The number of derangements D(n) satisfies the recurrence D(n) = (n-1)[D(n-1) + D(n-2)]. Derangements can be counted using the inclusion-exclusion principle.

## How It's Best Learned
Start with small cases (n=2,3,4) and count derangements by hand. Then derive the formula using inclusion-exclusion.

## Common Misconceptions
- Assuming D(n) = n! / 2 or other incorrect formulas.
- Confusing derangements with permutations with no fixed points in a general context.
- Not recognizing the connection to inclusion-exclusion.

## Questions

```yaml
- question: "A group of 30 people each write their name on a slip, put it in a bowl, and everyone draws one at random. Approximately what is the probability that nobody draws their own name?"
  type: multiple-choice
  options:
    - "Exactly 1/2, since each person either draws their own name or they don't"
    - "Approximately 1/e ≈ 0.368, regardless of the size of the group"
    - "Close to 0, since it becomes increasingly unlikely that no one draws their own name as the group grows"
    - "Exactly 1/30, because only one permutation has everyone mismatched"
  answer: 1
  explanation: "D(n)/n! = Σ (−1)^k/k! for k=0 to n, which converges to e⁻¹ ≈ 0.368 as n grows. The remarkable fact is that this fraction stabilizes quickly — for groups as small as 5 or 6, the probability is already very close to 1/e. It is not 1/2 (a common guess), and it does not approach 0 as the group grows. Roughly 37% of all permutations are derangements regardless of n."

- question: "In the inclusion-exclusion derivation of D(n), what do the sets A_i represent, and what are we computing the complement of?"
  type: multiple-choice
  options:
    - "A_i is the set of permutations where element i is NOT in its original position; we count permutations with at least one fixed point"
    - "A_i is the set of permutations where element i IS in its original position; we count permutations where none of the A_i events occur"
    - "A_i is the set of all derangements of i elements; we sum over all subset sizes"
    - "A_i is the set of permutations where elements 1 through i are all fixed; we count permutations with no such prefix"
  answer: 1
  explanation: "A_i is the set of permutations where element i lands in its own original position (a 'fixed point'). We want permutations where NONE of the A_i events occur — no element is fixed. Inclusion-exclusion gives |A_1 ∪ ... ∪ A_n|, and we subtract this from n! to get D(n). The formula D(n) = n! · Σ (−1)^k/k! for k=0 to n emerges from this alternating sum, and its convergence to n!/e is the connection to Euler's number."

- question: "For large n, the probability that a randomly chosen permutation of n objects is a derangement approaches 1/e ≈ 0.368, regardless of the value of n."
  type: true-false
  answer: true
  explanation: "D(n)/n! = Σ (−1)^k/k! for k=0 to n, which is the partial sum of the Taylor series for e⁻¹. As n → ∞ this converges to e⁻¹ ≈ 0.368. Even for small n (n = 5 or 6), the probability is already very close to 1/e. The fraction of permutations that are derangements stabilizes at about 37% — a fixed proportion of all possible rearrangements are always 'completely misaligned.'"

- question: "D(5) = 5!/2 = 60."
  type: true-false
  answer: false
  explanation: "D(5) = 44, not 60. Using the recurrence with D(1)=0, D(2)=1, D(3)=2, D(4)=9: D(5) = 4·(D(4)+D(3)) = 4·(9+2) = 44. The formula D(n) = n!/2 is a common misconception. D(n)/n! converges to 1/e ≈ 0.368, which is close to but not 1/2. For n=5: D(5)/5! = 44/120 ≈ 0.367 ≈ 1/e, confirming the convergence."

- question: "Explain why D(n) ≈ n!/e for large n, connecting the derivation to the inclusion-exclusion formula."
  type: short-answer
  answer: "Using inclusion-exclusion, D(n) = n! · Σ (−1)^k/k! for k=0 to n. This is the partial sum of the Taylor series for e⁻¹ = Σ (−1)^k/k! for k=0 to ∞. As n increases, more terms of the series are included and the sum converges to e⁻¹, giving D(n) ≈ n!/e. The convergence is fast: by n=5, the approximation is already very accurate."
  explanation: "The key connection is recognizing that the alternating sum from inclusion-exclusion is exactly the Taylor series for e⁻¹ truncated at n terms. This is why a combinatorial counting problem produces e as a natural constant — not because e was assumed, but because the alternating harmonic series that defines e⁻¹ arises naturally from the mechanics of counting forbidden fixed points."
```

## Explainer

You already know what a permutation is: a rearrangement of n objects. A **derangement** is a permutation with one extra restriction — no object is allowed to land back in its own original position. Think of it as a secret-Santa gift exchange where no one is allowed to draw their own name. Every possible assignment is a permutation of participants; a derangement is one where nobody gives a gift to themselves.

The count of derangements D(n) can be derived using the inclusion-exclusion principle you've studied. Let A_i be the set of permutations where element i *is* in its original position (a "fixed point"). We want to count permutations where none of the A_i events occur — the complement. Inclusion-exclusion gives D(n) = n! − C(n,1)(n−1)! + C(n,2)(n−2)! − ⋯, which simplifies to the elegant formula D(n) = n! · Σ (−1)^k / k! for k = 0 to n. For large n, this sum converges to e⁻¹ ≈ 0.368, meaning roughly 37% of all permutations are derangements regardless of how large n grows.

There's also a satisfying recurrence: D(n) = (n − 1)[D(n − 1) + D(n − 2)]. You can derive it by considering where element 1 goes. It must go somewhere other than position 1 — say, position k. Now element k has two choices: go to position 1 (giving a derangement of the remaining n − 2 elements, contributing D(n − 2)) or not go to position 1 (effectively giving a derangement of n − 1 elements, contributing D(n − 1)). Since there are n − 1 choices for k, the total is (n − 1)(D(n − 1) + D(n − 2)).

Derangements appear throughout combinatorics in problems involving "forbidden positions." Any time you need to count arrangements where certain pairs are prohibited, the derangement framework generalizes naturally. The deeper lesson is how inclusion-exclusion turns a complicated constraint (nothing in its original slot) into a tractable alternating sum — and how a combinatorial identity and a limiting probability (1/e) can emerge from the same algebraic object.
