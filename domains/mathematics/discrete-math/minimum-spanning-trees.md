---
id: minimum-spanning-trees
title: Minimum Spanning Trees
domain: mathematics
course: discrete-math
prerequisites:
- id: trees-in-graph-theory
  type: hard
tags:
- minimum-spanning-tree
- kruskal
- prim
- greedy
- weighted-graphs
stage: formal-systems
status: draft
---

# Minimum Spanning Trees

## Core Idea
A minimum spanning tree (MST) of a weighted connected graph is a spanning tree with the smallest possible total edge weight. Kruskal's algorithm builds an MST by greedily adding the cheapest edge that does not create a cycle. Prim's algorithm grows an MST from a seed vertex by repeatedly adding the cheapest edge that connects the current tree to a new vertex. Both algorithms are provably correct by the cut property: the minimum-weight edge crossing any cut of the graph belongs to some MST.

## How It's Best Learned
Trace both algorithms by hand on weighted graphs of 6-8 vertices. Spend time on correctness proofs, not just execution. Understand the cut property as the theoretical justification for why greedy works here, and contrast it with cases where greedy fails.

## Common Misconceptions
- Thinking there is always a unique MST — if edge weights are not all distinct, multiple MSTs can share the same total weight.
- Confusing the MST (globally minimal spanning tree) with shortest paths (a different problem entirely).
