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
status: draft
---

# Cycle Notation and Decomposition

## Core Idea
Cycle notation (a b c) means a→b→c→a. Every permutation decomposes uniquely into disjoint cycles. The order equals the LCM of cycle lengths. Disjoint cycles commute, making decomposition a powerful tool.

## How It's Best Learned
Write permutations in both one-line and cycle notation. Practice decomposing into disjoint cycles and computing orders using LCM.

## Common Misconceptions
- Assuming overlapping cycles can be combined; only disjoint cycles can be multiplied arbitrarily.
- Forgetting that cycle notation specifies only the cyclic structure, not starting position.

## Explainer

Cycle notation is a compact, readable way to describe permutations. You already know from permutation groups that a permutation is a bijection from a set to itself. Writing out every mapping explicitly in two-line notation gets unwieldy fast for large sets. Cycle notation compresses this by recording only the elements that move, grouping them by their orbit. The notation **(a b c)** means a maps to b, b maps to c, and c maps back to a — a cyclic rotation among those three elements. Fixed points (elements that map to themselves) are simply omitted.

So the permutation on {1, 2, 3, 4, 5} that sends 1→3, 3→5, 5→1, 2→4, 4→2 can be written **(1 3 5)(2 4)**. This is far easier to read and compute with than a two-line table. The key theorem is that every permutation decomposes **uniquely** into **disjoint cycles** — cycles whose element sets don't overlap. This uniqueness (up to cycling elements within each cycle and reordering the cycles) makes disjoint cycle form the canonical representation of any permutation.

To find the decomposition, "chase orbits": pick any element, follow it through the permutation until you return to the start — that's one cycle. Pick any element not yet placed and repeat. For example, the permutation sending 1→4, 4→2, 2→1, 3→5, 5→3 decomposes as (1 4 2)(3 5). The first cycle has length 3, the second length 2.

Two critical consequences follow immediately. First, **disjoint cycles commute**: (1 4 2)(3 5) = (3 5)(1 4 2), because they act on completely separate elements. This is remarkable — permutation composition in general is not commutative, but disjoint cycles are the exception. Second, the **order** of a permutation (the smallest n such that applying it n times returns every element to its original position) equals the **LCM of the cycle lengths**. For (1 4 2)(3 5), the order is LCM(3, 2) = 6: after 6 applications, the 3-cycle has completed 2 full rotations and the 2-cycle has completed 3 full rotations, so everything is back to start. This LCM formula makes order computation trivial once you have the disjoint cycle decomposition.
