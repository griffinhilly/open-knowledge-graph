---
id: halls-marriage-theorem
title: Hall's Marriage Theorem
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: matchings-bipartite-graphs
  type: hard
builds-toward:
- konig-theorem
- network-flows-max-flow-min-cut
tags:
- halls-theorem
- matching-conditions
- combinatorial-optimization
stage: abstract-reasoning
status: draft
---

# Hall's Marriage Theorem

## Core Idea
Hall's Marriage Theorem states that a bipartite graph has a matching saturating the left part if and only if every subset S of left vertices has at least |S| neighbors. This elegant criterion connects the existence of a perfect matching to a simple neighborhood condition.

## How It's Best Learned
Test the theorem on explicit bipartite graphs by checking the neighborhood condition for all subsets. Identify which subset violates the condition when a perfect matching fails to exist.

## Common Misconceptions
- Thinking the condition is sufficient for matchings that match all vertices (it only guarantees left saturation).
- Overlooking that the condition must hold for every subset, not just a few examples.
- Confusing Hall's theorem with König's theorem or thinking they answer the same question.
