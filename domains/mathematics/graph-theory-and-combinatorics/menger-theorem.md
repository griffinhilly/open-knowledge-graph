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
stage: formal-systems
status: draft
---

# Menger's Theorem and Edge/Vertex Connectivity

## Core Idea
Menger's theorem states that the maximum number of edge-disjoint paths between two vertices equals the minimum number of edges whose removal disconnects them. Similarly for vertex-disjoint paths and vertex cuts. These min-max theorems generalize and unify connectivity concepts.

## How It's Best Learned
Draw a graph and find all edge-disjoint paths between two vertices by hand. Then find the minimum edge cut separating them and verify equality.

## Common Misconceptions
- Confusing edge-disjoint paths with internally vertex-disjoint paths; these are different concepts with different connectivity numbers.

## Explainer

Menger's theorem is a **min-max theorem**: it equates two seemingly different quantities — the maximum number of paths you can pack between two vertices, and the minimum number of edges (or vertices) you need to remove to disconnect them. Min-max theorems are important throughout combinatorics because they let you prove an upper bound and a lower bound coincide, often revealing deep structural duality.

You already know the max-flow min-cut theorem from your prerequisite: in a network, the maximum flow from source s to sink t equals the minimum capacity of any cut separating s from t. Menger's theorem is essentially this same result applied to unweighted graphs. In an unweighted graph, every edge has capacity 1. **Edge-disjoint paths** between s and t are paths that share no edges (they may share vertices). The maximum number of edge-disjoint paths equals the maximum integer flow from s to t when every edge has unit capacity. By max-flow min-cut, this equals the size of the minimum edge cut — the minimum number of edges whose removal disconnects s from t. That's Menger's theorem for edge connectivity.

The vertex version is slightly different and requires care. **Internally vertex-disjoint paths** share no intermediate (internal) vertices — the endpoints s and t are allowed to be shared, but no other vertex appears in two paths. The maximum number of such paths equals the minimum **vertex cut**: the minimum number of internal vertices whose removal disconnects s from t. To reduce this to a flow problem, replace each vertex v (except s and t) with two vertices vᵢₙ and vₒᵤₜ connected by a single unit-capacity edge. Any path through v must now use this bottleneck edge. Edge-disjoint paths in this expanded graph correspond exactly to internally vertex-disjoint paths in the original, and max-flow min-cut gives the result.

Menger's theorem has an important global form: a graph G is k-edge-connected (meaning at least k edges must be removed to disconnect any pair of vertices) if and only if there are k edge-disjoint paths between every pair of vertices. Similarly, G is k-vertex-connected if and only if there are k internally vertex-disjoint paths between every pair. This makes connectivity a "packing" quantity — you can measure how hard a graph is to disconnect by counting how many paths you can simultaneously route between any two points.
