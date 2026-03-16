---
id: cycle-detection-directed-undirected
title: Cycle Detection in Directed and Undirected Graphs
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: depth-first-search
  type: hard
builds-toward:
- topological-sort
tags:
- graphs
- cycles
- dfs
stage: formal-systems
status: draft
---

# Cycle Detection in Directed and Undirected Graphs

## Core Idea
In undirected graphs, a back edge (to a visited neighbor other than the parent) signals a cycle. In directed graphs, back edges are those to ancestors in the DFS tree. Both detections run in O(V+E) during DFS. Cycle detection is essential for dependency resolution and deadlock detection.

## How It's Best Learned
Implement DFS with three vertex states (white, gray, black). Use gray edges as back edges. Trace on examples with and without cycles. Apply to topological sorting and deadlock detection.

## Common Misconceptions
- Treating directed and undirected cycle detection identically; the algorithms differ significantly.
- Not handling self-loops and parallel edges correctly.
- Assuming cycle detection requires storing all edges; DFS detects them during traversal.

## Explainer

From your study of depth-first search, you know that DFS explores a graph by going as deep as possible before backtracking, and that the edges it encounters can be classified based on the DFS tree it builds. **Cycle detection** exploits this classification. The core insight is that a cycle exists if and only if DFS encounters an edge that points back to a node already on the current exploration path — a **back edge**. But the precise definition of "back edge" differs between undirected and directed graphs, and conflating the two is a common source of bugs.

In an **undirected graph**, every edge is traversed in both directions during DFS. When you visit node A and see neighbor B, you will later visit B and see A as a neighbor too. This means you must distinguish between "B is my parent in the DFS tree" (not a cycle) and "B is a visited node that is not my parent" (a cycle). The algorithm is straightforward: during DFS, if you encounter a neighbor that has already been visited and is not the node you came from, you have found a cycle. For example, in a triangle A-B-C-A, when DFS reaches C (having come from B) and sees A is already visited, that back edge reveals the cycle. No special node coloring is needed — a simple visited/unvisited flag plus parent tracking suffices.

**Directed graphs** are more subtle. Here, a visited node is not necessarily evidence of a cycle — it might have been fully explored in a previous DFS subtree that has no connection back to the current path. The solution is to track three states for each node: **white** (undiscovered), **gray** (discovered, currently being explored — on the recursion stack), and **black** (fully explored, all descendants processed). A back edge in a directed graph is specifically an edge from a gray node to another gray node — both are on the current DFS path, forming a cycle. An edge from a gray node to a black node is a **cross edge** or **forward edge**, not a cycle. This three-color scheme is what makes directed cycle detection work correctly.

These algorithms run in **O(V + E)** time, matching the cost of DFS itself, because cycle detection adds only constant work per edge. The applications are pervasive in computing. Package managers use cycle detection to verify that dependency graphs are acyclic (a cycle means "A requires B which requires A" — an unresolvable deadlock). Compilers check for circular dependencies between modules. Operating systems detect deadlocks by looking for cycles in resource allocation graphs. And **topological sorting** — which you will study next — is only possible on directed acyclic graphs (DAGs), so verifying the absence of cycles is a prerequisite for topological ordering.
