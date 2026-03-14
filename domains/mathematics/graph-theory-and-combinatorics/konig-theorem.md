---
id: konig-theorem
title: König's Theorem and Min-Max Relations
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: halls-marriage-theorem
  type: hard
builds-toward:
- network-flows-max-flow-min-cut
tags:
- konig-theorem
- min-max
- vertex-cover
stage: abstract-reasoning
status: draft
---

# König's Theorem and Min-Max Relations

## Core Idea
König's theorem states that in a bipartite graph, the size of a maximum matching equals the size of a minimum vertex cover. This min-max equality is a central result in combinatorial optimization and does not hold for general graphs.

## How It's Best Learned
Compute both the maximum matching and minimum vertex cover for several small bipartite graphs to verify equality. Use the duality to understand why König's theorem fails on odd cycles.

## Common Misconceptions
- Thinking the matching-vertex-cover duality holds for all graphs (it fails on non-bipartite graphs like K₃).
- Confusing minimum vertex cover with minimum edge cover; these are different problems.
