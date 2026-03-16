---
id: articulation-points-cut-vertices
title: Articulation Points and Bridges in Graphs
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: depth-first-search
  type: hard
tags:
- graphs
- articulation
- connectivity
stage: formal-systems
status: draft
---

# Articulation Points and Bridges in Graphs

## Core Idea
An articulation point (cut vertex) is a vertex whose removal disconnects the graph. A bridge is an edge with the same property. Tarjan's algorithm identifies them in a single DFS pass by tracking discovery time and lowest reachable time. Critical for network reliability and resilience.

## How It's Best Learned
Implement DFS-based articulation point detection. Verify on graphs with known cut vertices (e.g., a tree has internal nodes as articulation points). Apply to network reliability problems.

## Common Misconceptions
- Assuming high-degree vertices are always articulation points; degree alone doesn't determine criticality.
- Not understanding why discovery and low times suffice; the key insight is reachability to descendants.
- Forgetting special cases like the root of the DFS tree and bridges.

## Explainer

From your study of depth-first search, you know that DFS explores a graph by going as deep as possible along each branch before backtracking, producing a DFS tree that spans the graph. The tree edges follow the DFS traversal, while **back edges** connect descendants to ancestors. Articulation points and bridges build directly on this structure by asking: which vertices or edges are so critical that removing them would split the graph into disconnected pieces?

Think of a road network. Most intersections can be closed for construction because alternative routes exist. But some intersections are chokepoints — close them and entire neighborhoods become unreachable. An **articulation point** (or **cut vertex**) is exactly such a chokepoint: a vertex whose removal increases the number of connected components. A **bridge** is the edge equivalent — an edge whose removal disconnects the graph. Identifying these critical points is essential for analyzing network reliability, whether the network carries internet traffic, water, or electrical power.

Tarjan's algorithm finds all articulation points in a single DFS pass using two values per vertex: **discovery time** (`disc[v]`), the order in which DFS first visits the vertex, and **low value** (`low[v]`), the smallest discovery time reachable from the subtree rooted at `v` through any combination of tree edges and back edges. The low value captures a crucial question: can the descendants of `v` reach back above `v` in the DFS tree without going through `v`? If `low[child] >= disc[v]` for some child of `v`, that child's entire subtree has no back edge to an ancestor of `v` — removing `v` would strand that subtree. Vertex `v` is therefore an articulation point. For bridges, the condition is stricter: if `low[child] > disc[v]`, the edge `(v, child)` is a bridge, because the subtree cannot reach `v` itself through any other path.

The root of the DFS tree is a special case. Since every vertex's discovery time is at least as large as the root's, the general condition `low[child] >= disc[root]` is trivially true for all children. Instead, the root is an articulation point if and only if it has **two or more children in the DFS tree**. If the root has only one child, removing it leaves a single connected component (the rest of the tree). If it has multiple children, those subtrees are only connected through the root — removing it splits them apart. The entire algorithm runs in O(V + E) time, the same complexity as DFS itself, because it simply augments the DFS traversal with the discovery and low-value bookkeeping.
