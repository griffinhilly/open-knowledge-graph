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

## Questions

```yaml
- question: "A vertex v has degree 5 in a connected undirected graph. A classmate claims v must be an articulation point because removing it disconnects many edges. Which response is correct?"
  type: multiple-choice
  options:
    - "The classmate is right — high degree means many dependencies, so removal is likely to disconnect the graph"
    - "The classmate is wrong — whether v is an articulation point depends on reachability between its neighbors, not its degree"
    - "The classmate is right only if all five neighbors are in different connected components"
    - "The classmate is wrong — articulation points can only have degree 2 or less"
  answer: 1
  explanation: "Degree alone does not determine whether a vertex is an articulation point. A hub vertex with degree 5 might still leave its neighbors mutually reachable through alternative paths — it would not be an articulation point. Conversely, a degree-2 vertex connecting two otherwise separate subgraphs IS an articulation point. The critical question is: if v is removed, do its neighbors remain connected to each other? That depends on the graph's topology, not v's degree."

- question: "In Tarjan's algorithm, vertex v has a child u in the DFS tree such that low[u] >= disc[v]. What does this tell us?"
  type: multiple-choice
  options:
    - "The subtree rooted at u contains a back edge that reaches an ancestor of v, so v is safe"
    - "The subtree rooted at u has no back edge reaching an ancestor of v, meaning removing v would disconnect u's subtree"
    - "The edge (v, u) is a back edge and should be ignored in the articulation point check"
    - "Vertex u is itself an articulation point"
  answer: 1
  explanation: "low[u] is the smallest discovery time reachable from u's subtree through any combination of tree edges and back edges. If low[u] >= disc[v], the subtree rooted at u cannot reach any ancestor of v without going through v itself. Remove v, and u's entire subtree becomes disconnected — v is an articulation point. If low[u] < disc[v], the subtree has a back edge that bypasses v, so the component stays connected without v."

- question: "A leaf vertex (degree 1) in a connected graph is always an articulation point."
  type: true-false
  answer: false
  explanation: "A leaf is never an articulation point. Removing a leaf leaves the rest of the graph intact — its single neighbor simply loses one connection but remains connected to everything else. Articulation points must be internal vertices whose removal separates the graph into at least two components. The common misconception is conflating 'critical to some connections' with 'critical to graph connectivity.'"

- question: "The root of the DFS tree is an articulation point if and only if it has two or more children in the DFS tree."
  type: true-false
  answer: true
  explanation: "The general articulation point condition (low[child] >= disc[v]) cannot be applied to the root because every vertex has a discovery time >= the root's, making the condition trivially true for all children. The root is special: its children's subtrees are only connected to each other through the root itself. If the root has one child, removing it leaves that single subtree intact. If it has two or more children, removing the root disconnects those subtrees from each other — so it is an articulation point if and only if it has >= 2 DFS children."

- question: "Explain why the 'low value' (lowest discovery time reachable from a subtree via tree edges and back edges) is sufficient to detect articulation points without re-running DFS after each removal."
  type: short-answer
  answer: "The low value answers, in one DFS pass, the key question for every vertex: can my subtree reach above me without going through me? A back edge from a descendant to an ancestor makes that ancestor reachable without traversing the current vertex — it provides an 'escape route.' If low[child] < disc[v], child's subtree has such an escape route and v is not needed for connectivity. If low[child] >= disc[v], there is no escape route; the subtree is entirely dependent on v for connection to the rest of the graph. By computing this bottom-up during DFS, Tarjan's algorithm answers the disconnection question for every vertex simultaneously in O(V+E) time."
  explanation: "The insight is that back edges encode alternative connectivity. DFS already visits every edge, so tracking the minimum reachable discovery time as we go costs no extra traversals. The low value is updated upward through the DFS tree — a descendant's back edge discovery propagates to its ancestors, letting each ancestor know whether that subtree can 'escape' upward. This makes the algorithm a single augmented DFS rather than V separate DFS traversals."
```

## Explainer

From your study of depth-first search, you know that DFS explores a graph by going as deep as possible along each branch before backtracking, producing a DFS tree that spans the graph. The tree edges follow the DFS traversal, while **back edges** connect descendants to ancestors. Articulation points and bridges build directly on this structure by asking: which vertices or edges are so critical that removing them would split the graph into disconnected pieces?

Think of a road network. Most intersections can be closed for construction because alternative routes exist. But some intersections are chokepoints — close them and entire neighborhoods become unreachable. An **articulation point** (or **cut vertex**) is exactly such a chokepoint: a vertex whose removal increases the number of connected components. A **bridge** is the edge equivalent — an edge whose removal disconnects the graph. Identifying these critical points is essential for analyzing network reliability, whether the network carries internet traffic, water, or electrical power.

Tarjan's algorithm finds all articulation points in a single DFS pass using two values per vertex: **discovery time** (`disc[v]`), the order in which DFS first visits the vertex, and **low value** (`low[v]`), the smallest discovery time reachable from the subtree rooted at `v` through any combination of tree edges and back edges. The low value captures a crucial question: can the descendants of `v` reach back above `v` in the DFS tree without going through `v`? If `low[child] >= disc[v]` for some child of `v`, that child's entire subtree has no back edge to an ancestor of `v` — removing `v` would strand that subtree. Vertex `v` is therefore an articulation point. For bridges, the condition is stricter: if `low[child] > disc[v]`, the edge `(v, child)` is a bridge, because the subtree cannot reach `v` itself through any other path.

The root of the DFS tree is a special case. Since every vertex's discovery time is at least as large as the root's, the general condition `low[child] >= disc[root]` is trivially true for all children. Instead, the root is an articulation point if and only if it has **two or more children in the DFS tree**. If the root has only one child, removing it leaves a single connected component (the rest of the tree). If it has multiple children, those subtrees are only connected through the root — removing it splits them apart. The entire algorithm runs in O(V + E) time, the same complexity as DFS itself, because it simply augments the DFS traversal with the discovery and low-value bookkeeping.
