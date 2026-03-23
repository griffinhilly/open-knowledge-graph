---
id: cycle-notation-and-decomposition
title: Cycle Notation and Decomposition
domain: mathematics
course: abstract-algebra
prerequisites:
- id: permutation-groups
  type: hard
builds-toward:
- sign-of-a-permutation
tags:
- cycle-notation
- permutations
- representations
stage: advanced
status: validated
---

# Cycle Notation and Decomposition

## Core Idea
Cycle notation (a b c) means a→b→c→a. Every permutation decomposes uniquely into disjoint cycles. The order equals the LCM of cycle lengths. Disjoint cycles commute, making decomposition a powerful tool.

## How It's Best Learned
Write permutations in both one-line and cycle notation. Practice decomposing into disjoint cycles and computing orders using LCM.

## Common Misconceptions
- Assuming overlapping cycles can be combined; only disjoint cycles can be multiplied arbitrarily.
- Forgetting that cycle notation specifies only the cyclic structure, not starting position.

## Questions

```yaml
- question: "What is the order of the permutation (1 2 3)(4 5 6 7)?"
  type: multiple-choice
  options:
    - "3 — the length of the first cycle"
    - "4 — the length of the second cycle"
    - "7 — the total number of elements moved"
    - "12 — the LCM of the cycle lengths"
  answer: 3
  explanation: "The order of a permutation in disjoint cycle form equals the LCM of its cycle lengths, not the sum or product. Here LCM(3, 4) = 12: after 12 applications, the 3-cycle has completed 4 full rotations (back to start) and the 4-cycle has completed 3 full rotations (back to start), so every element is back to its original position. 12 is the smallest such number. The common wrong answers — 3 or 4 — confuse the order with one cycle's length, and 7 confuses it with a sum."

- question: "A student writes: '(1 2)(2 3) = (2 3)(1 2) because disjoint cycles commute.' What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Nothing — both expressions produce the same permutation since order never matters for two-cycles"
    - "The student forgot that cycles must first be converted to one-line notation before comparing"
    - "These cycles are not disjoint — they share element 2 — so the commutative property does not apply"
    - "Disjoint cycles do not actually commute; the student has misremembered the theorem"
  answer: 2
  explanation: "The commutative property applies only to DISJOINT cycles — cycles whose element sets have no overlap. (1 2) and (2 3) both contain element 2, so they are not disjoint. In fact, (1 2)(2 3) and (2 3)(1 2) produce different permutations: the first sends 1→3, while the second sends 1→2→... — they are not equal. The theorem that disjoint cycles commute is a precise exception to the general non-commutativity of permutation composition, not a blanket rule."

- question: "The permutation (1 3 5)(2 4) and the permutation (2 4)(1 3 5) are equal, because disjoint cycles commute."
  type: true-false
  answer: true
  explanation: "This is correct. (1 3 5) acts on {1, 3, 5} and (2 4) acts on {2, 4} — these sets are disjoint. Because the cycles act on completely separate elements, each cycle has no effect on the elements of the other. Applying them in either order produces identical results for every element in the set. This is the one important exception to the general rule that permutation composition is not commutative."

- question: "The permutation (1 2 3 4 5)(6 7) has order 7, because 5 + 2 = 7."
  type: true-false
  answer: false
  explanation: "The order equals the LCM of the cycle lengths, not their sum. LCM(5, 2) = 10, not 7. After 10 applications, the 5-cycle has completed 2 full rotations and the 2-cycle has completed 5 full rotations — every element is back to its start. After only 7 applications, the 5-cycle would have completed 1 full rotation plus 2 extra steps, so elements 1–5 would NOT be back to their original positions. The sum-of-lengths is a very common wrong answer; always use LCM."

- question: "Why does the order of a permutation equal the LCM of its cycle lengths rather than the sum or product? Explain the reasoning in terms of what 'order' means."
  type: short-answer
  answer: "The order of a permutation is the smallest number of times you must apply it for every element to return to its starting position. Each disjoint cycle operates independently on its own set of elements. A k-cycle returns to the identity after exactly k applications. For all cycles to simultaneously return to their starting positions, you need a number of applications that is a multiple of each cycle length — the smallest such number is the LCM. The sum has no such interpretation, and the product is generally too large."
  explanation: "This is a direct consequence of how disjoint cycles interact (or rather, don't interact). Because they act on separate elements, each cycle's 'reset time' is independent. You need to wait until ALL cycles have simultaneously completed whole numbers of rotations — that's the definition of LCM. A concrete check: for (1 2 3)(4 5), after 3 steps the first cycle resets but the second hasn't (it needs 2 or 4 steps to reset); after 2 steps the second resets but the first hasn't; after LCM(3,2)=6 steps, both reset simultaneously."
```

## Explainer

Cycle notation is a compact, readable way to describe permutations. You already know from permutation groups that a permutation is a bijection from a set to itself. Writing out every mapping explicitly in two-line notation gets unwieldy fast for large sets. Cycle notation compresses this by recording only the elements that move, grouping them by their orbit. The notation **(a b c)** means a maps to b, b maps to c, and c maps back to a — a cyclic rotation among those three elements. Fixed points (elements that map to themselves) are simply omitted.

So the permutation on {1, 2, 3, 4, 5} that sends 1→3, 3→5, 5→1, 2→4, 4→2 can be written **(1 3 5)(2 4)**. This is far easier to read and compute with than a two-line table. The key theorem is that every permutation decomposes **uniquely** into **disjoint cycles** — cycles whose element sets don't overlap. This uniqueness (up to cycling elements within each cycle and reordering the cycles) makes disjoint cycle form the canonical representation of any permutation.

To find the decomposition, "chase orbits": pick any element, follow it through the permutation until you return to the start — that's one cycle. Pick any element not yet placed and repeat. For example, the permutation sending 1→4, 4→2, 2→1, 3→5, 5→3 decomposes as (1 4 2)(3 5). The first cycle has length 3, the second length 2.

Two critical consequences follow immediately. First, **disjoint cycles commute**: (1 4 2)(3 5) = (3 5)(1 4 2), because they act on completely separate elements. This is remarkable — permutation composition in general is not commutative, but disjoint cycles are the exception. Second, the **order** of a permutation (the smallest n such that applying it n times returns every element to its original position) equals the **LCM of the cycle lengths**. For (1 4 2)(3 5), the order is LCM(3, 2) = 6: after 6 applications, the 3-cycle has completed 2 full rotations and the 2-cycle has completed 3 full rotations, so everything is back to start. This LCM formula makes order computation trivial once you have the disjoint cycle decomposition.
