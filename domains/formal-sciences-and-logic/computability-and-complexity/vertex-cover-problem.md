---
id: vertex-cover-problem
title: Vertex Cover and Set Cover Problems
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: three-sat-np-complete
  type: hard
- id: np-completeness-formal
  type: hard
builds-toward:
- fixed-parameter-tractability
tags:
- graph-problems
- np-complete
- optimization
stage: advanced
status: draft
---

# Vertex Cover and Set Cover Problems

## Core Idea
The vertex cover problem asks whether a graph has a set of k vertices such that every edge touches at least one vertex in the set. This classic NP-complete problem serves as a foundation for parameterized complexity. It demonstrates how many combinatorial optimization problems can be shown NP-hard through polynomial reductions from 3-SAT.

## How It's Best Learned
Begin with small graphs and try to find vertex covers by hand. Then reduce 3-SAT to vertex cover: each clause becomes a triangle and variables are connected via gadgets.

## Common Misconceptions
- Vertex cover becomes easy if we allow approximation (approximation is hard too, by PCP).
- All NP-complete problems reduce to vertex cover (only true for problems NP-hard via specific reductions).
