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
status: draft
---

# Erdős-Gallai Theorem

## Core Idea
The Erdős-Gallai theorem provides a necessary and sufficient condition for a sequence of non-negative integers to be graphical: the sequence must be non-increasing, have even sum, and satisfy a specific inequality at each prefix. This completely characterizes which sequences can be realized as degree sequences of simple graphs.

## How It's Best Learned
Apply the theorem to several candidate sequences—both known-graphical and non-graphical. Verify the inequality holds at each step to develop intuition.

## Common Misconceptions
Just checking that the sum is even is insufficient; many even-sum sequences fail the prefix inequalities and are not graphical.

## Explainer

From degree sequences, you know that the degree of a vertex counts its neighbors, and that every edge contributes exactly 2 to the total degree sum. This means a **graphical sequence** — a sequence that can actually be realized as the degree sequence of some simple graph — must have an even sum. But even-sum is not enough. The Erdős-Gallai theorem tells you exactly what else is required.

The theorem states: a non-increasing sequence d₁ ≥ d₂ ≥ ⋯ ≥ dₙ ≥ 0 is graphical if and only if (1) the sum d₁ + d₂ + ⋯ + dₙ is even, and (2) for every k from 1 to n, the inequality Σᵢ₌₁ᵏ dᵢ ≤ k(k−1) + Σᵢ₌ₖ₊₁ⁿ min(dᵢ, k) holds. The left side is the total degree among the k highest-degree vertices. The right side bounds how many edges those k vertices can collectively have: at most k(k−1) edges among themselves (a complete graph on k vertices) plus at most k edges from each remaining vertex. If the top-k vertices collectively claim more edges than that bound allows, no valid graph exists.

The intuition is a packing argument. Imagine placing the k highest-degree vertices first and trying to satisfy their degree requirements by connecting them to each other and to the remaining n−k vertices. The bound k(k−1) comes from the maximum edges within the group (every pair connected), and Σ min(dᵢ, k) comes from capping each outside vertex's contribution at k (it can connect to at most k members of the group). If the required degree sum exceeds what is geometrically possible, the sequence is non-graphical.

To apply the theorem in practice: sort the sequence in non-increasing order, check that the sum is even, then check the inequality at each prefix k = 1, 2, …, n. Most sequences fail (or pass) early, so you rarely need to check every prefix. The theorem is also constructive — the **Hakimi algorithm** (greedily connect the highest-degree vertex to the next highest-degree vertices, then reduce degrees and repeat) builds a realizing graph when one exists, giving you a concrete way to move from a valid sequence to an actual graph.
