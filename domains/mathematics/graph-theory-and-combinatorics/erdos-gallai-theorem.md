---
id: erdos-gallai-theorem
title: Erdős-Gallai Theorem
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: degree-sequences
  type: hard
tags:
- graph-theory
- degree-sequences
- extremal
stage: formal-systems
status: validated
---

# Erdős-Gallai Theorem

## Core Idea
The Erdős-Gallai theorem provides a necessary and sufficient condition for a sequence of non-negative integers to be graphical: the sequence must be non-increasing, have even sum, and satisfy a specific inequality at each prefix. This completely characterizes which sequences can be realized as degree sequences of simple graphs.

## How It's Best Learned
Apply the theorem to several candidate sequences—both known-graphical and non-graphical. Verify the inequality holds at each step to develop intuition.

## Common Misconceptions
Just checking that the sum is even is insufficient; many even-sum sequences fail the prefix inequalities and are not graphical.

## Questions

```yaml
- question: "Is the sequence (3, 3, 3, 1) graphical? Apply the Erdős-Gallai theorem."
  type: multiple-choice
  options:
    - "Yes — the sum is 10, which is even, and even-sum sequences are always graphical"
    - "No — the prefix inequality fails at k = 2"
    - "Yes — the prefix inequality holds at k = 1, so no further checking is needed"
    - "No — the sequence must be strictly decreasing to be graphical"
  answer: 1
  explanation: "The sum is 10 (even) ✓. Check k=2: left side = 3+3 = 6. Right side = k(k−1) + Σmin(dᵢ,k) = 2(1) + min(3,2) + min(1,2) = 2 + 2 + 1 = 5. Since 6 > 5, the inequality fails at k=2, so the sequence is NOT graphical. Option A shows the key misconception: even sum is necessary but not sufficient. The prefix inequalities must also hold."

- question: "In the Erdős-Gallai inequality, the right side includes Σᵢ₌ₖ₊₁ⁿ min(dᵢ, k) rather than just Σdᵢ. Why is the min(dᵢ, k) cap necessary?"
  type: multiple-choice
  options:
    - "Because outside vertices can only connect to each other, not to the top-k group"
    - "Because each outside vertex can contribute at most k edges to the top-k group, since the group has only k members"
    - "Because min(dᵢ, k) ensures outside vertices have lower degree than top-k vertices"
    - "Because dᵢ alone would double-count edges within the outside group"
  answer: 1
  explanation: "Each vertex outside the top-k group can connect to at most k members of the group — the group only has k members. Even if an outside vertex has degree dᵢ > k, at most k of those edges go to the group. So min(dᵢ, k) correctly caps each outside vertex's maximum contribution to the top-k group's total degree. This makes the right side a genuine upper bound on what the top-k vertices can collectively achieve."

- question: "A sequence of non-negative integers with an even sum is always the degree sequence of some simple graph."
  type: true-false
  answer: false
  explanation: "Even sum is necessary but not sufficient. The sequence (3, 3, 3, 1) has even sum 10 but fails the Erdős-Gallai prefix inequality at k=2 and cannot be realized as a simple graph's degree sequence. The theorem requires both the even-sum condition and the prefix inequalities at every k. Many even-sum sequences are non-graphical."

- question: "To apply the Erdős-Gallai theorem, it is sufficient to check the prefix inequality only at k = 1 and k = n."
  type: true-false
  answer: false
  explanation: "The prefix inequality must hold for every k from 1 to n. Failure at any single k is enough to disqualify the sequence. While in practice many sequences fail (or pass) early — at small values of k — there is no guarantee that checking only the endpoints is sufficient. The complete check requires verifying all n inequalities."

- question: "Explain the intuition behind the Erdős-Gallai prefix inequality: why does k(k−1) + Σ min(dᵢ, k) represent a bound on what the top-k vertices can achieve?"
  type: short-answer
  answer: "The right side counts the maximum possible edges the k highest-degree vertices could collectively have in any simple graph. The term k(k−1) is the number of edges in a complete graph on k vertices — the most those k vertices can share among themselves. The term Σ min(dᵢ, k) adds the maximum contribution from each remaining vertex: each outside vertex can supply at most k edges to the group. If the actual degree sum of the top-k vertices exceeds this bound, no valid simple graph can exist."
  explanation: "This is a packing argument: can the high-degree vertices actually be satisfied given the edges available to them? The bound is tight because it counts every possible edge the top-k vertices could have — edges within the group and edges from outside. If the sequence demands more edges than this maximum allows, the degree requirements are geometrically impossible. The theorem is both necessary and sufficient: it fails precisely when no graph can accommodate the requirements."
```

## Explainer

From degree sequences, you know that the degree of a vertex counts its neighbors, and that every edge contributes exactly 2 to the total degree sum. This means a **graphical sequence** — a sequence that can actually be realized as the degree sequence of some simple graph — must have an even sum. But even-sum is not enough. The Erdős-Gallai theorem tells you exactly what else is required.

The theorem states: a non-increasing sequence d₁ ≥ d₂ ≥ ⋯ ≥ dₙ ≥ 0 is graphical if and only if (1) the sum d₁ + d₂ + ⋯ + dₙ is even, and (2) for every k from 1 to n, the inequality Σᵢ₌₁ᵏ dᵢ ≤ k(k−1) + Σᵢ₌ₖ₊₁ⁿ min(dᵢ, k) holds. The left side is the total degree among the k highest-degree vertices. The right side bounds how many edges those k vertices can collectively have: at most k(k−1) edges among themselves (a complete graph on k vertices) plus at most k edges from each remaining vertex. If the top-k vertices collectively claim more edges than that bound allows, no valid graph exists.

The intuition is a packing argument. Imagine placing the k highest-degree vertices first and trying to satisfy their degree requirements by connecting them to each other and to the remaining n−k vertices. The bound k(k−1) comes from the maximum edges within the group (every pair connected), and Σ min(dᵢ, k) comes from capping each outside vertex's contribution at k (it can connect to at most k members of the group). If the required degree sum exceeds what is geometrically possible, the sequence is non-graphical.

To apply the theorem in practice: sort the sequence in non-increasing order, check that the sum is even, then check the inequality at each prefix k = 1, 2, …, n. Most sequences fail (or pass) early, so you rarely need to check every prefix. The theorem is also constructive — the **Hakimi algorithm** (greedily connect the highest-degree vertex to the next highest-degree vertices, then reduce degrees and repeat) builds a realizing graph when one exists, giving you a concrete way to move from a valid sequence to an actual graph.
