---
id: menger-theorem
title: Menger's Theorem and Edge/Vertex Connectivity
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: network-flows-max-flow-min-cut
  type: hard
tags:
- menger-theorem
- connectivity
- paths
stage: abstract-reasoning
status: draft
---

# Menger's Theorem and Edge/Vertex Connectivity

## Core Idea
Menger's theorem states that the maximum number of edge-disjoint paths between two vertices equals the minimum number of edges whose removal disconnects them. Similarly for vertex-disjoint paths and vertex cuts. These min-max theorems generalize and unify connectivity concepts.

## How It's Best Learned
Draw a graph and find all edge-disjoint paths between two vertices by hand. Then find the minimum edge cut separating them and verify equality.

## Common Misconceptions
- Confusing edge-disjoint paths with internally vertex-disjoint paths; these are different concepts with different connectivity numbers.
