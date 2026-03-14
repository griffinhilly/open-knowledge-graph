---
id: four-color-theorem
title: The Four Color Theorem
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: planar-graphs-kuratowski-wagner
  type: hard
builds-toward:
- graph-minors-robertson-seymour
tags:
- four-color-theorem
- planar-graphs
- chromatic-number
stage: abstract-reasoning
status: draft
---

# The Four Color Theorem

## Core Idea
The Four Color Theorem states that every planar graph is 4-colorable: χ(G) ≤ 4 for all planar G. Proven in 1976, it was the first major theorem requiring computer verification. The theorem is tight; not all planar graphs are 3-colorable.

## How It's Best Learned
Study the history and proof sketch, focusing on the unavoidable set and discharging argument. Apply the theorem to real planar graphs (maps, planar circuit diagrams) and verify the bound.

## Common Misconceptions
- Thinking the theorem implies all maps are 4-colorable without understanding the reduction to graph coloring.
- Assuming the bound is tight for all planar graphs; many are 3-colorable or even 2-colorable (bipartite).
