---
id: bipartite-graph-detection-coloring
title: 'Bipartite Graphs: Detection and Two-Coloring'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: breadth-first-search
  type: hard
- id: graph-connectivity-components-dfs
  type: soft
tags:
- graphs
- bipartite
- coloring
stage: formal-systems
status: draft
---

# Bipartite Graphs: Detection and Two-Coloring

## Core Idea
A bipartite graph has no odd cycles and can be 2-colored: partition vertices into two sets such that all edges cross between sets. Detection via BFS/DFS is O(V+E): try to 2-color greedily; if a conflict arises, the graph is non-bipartite.

## How It's Best Learned
Implement bipartite checking by attempting 2-coloring during BFS. Test on graphs known to be bipartite (e.g., grid graphs, trees) and on graphs with odd cycles. Apply to matching problems.

## Common Misconceptions
- Assuming a graph is bipartite if it lacks triangles; odd cycles of any length disqualify it.
- Not recognizing that bipartiteness is a fundamental property enabling efficient matching and other algorithms.
- Thinking bipartite detection is expensive; BFS/DFS makes it linear time.

## Explainer

From your work with breadth-first search, you know how BFS explores a graph level by level, visiting all vertices at distance 1 from the source before those at distance 2, and so on. Bipartite graph detection is one of the most elegant applications of BFS, because the level structure of BFS directly corresponds to the two-coloring that defines bipartiteness.

A graph is **bipartite** if its vertices can be divided into two disjoint sets — call them "red" and "blue" — such that every edge connects a red vertex to a blue vertex. No edge ever connects two vertices of the same color. Think of a scheduling problem: students on one side, courses on the other, with edges representing enrollment. No edge connects two students or two courses — the graph is naturally bipartite. Trees are always bipartite. Grid graphs (like a checkerboard) are always bipartite. But add a single edge that creates an odd-length cycle, and bipartiteness breaks.

The detection algorithm is BFS with coloring. Pick any unvisited vertex, color it red, and add it to the queue. When you dequeue a vertex, examine each neighbor: if the neighbor is uncolored, color it the opposite color and enqueue it. If the neighbor is already colored and has the **same** color as the current vertex, you have found a conflict — the graph is not bipartite. If BFS completes without conflicts, the graph is bipartite, and the coloring you assigned is a valid 2-coloring. For disconnected graphs, repeat from each unvisited vertex. The entire process runs in O(V + E), the same as BFS itself.

Why does an odd cycle break bipartiteness? Walk around a cycle, alternating colors: red, blue, red, blue, ... If the cycle has even length, you return to the starting vertex with the correct color. If the cycle has odd length, you return needing the opposite color — a contradiction. This is not just an intuition but a theorem: **a graph is bipartite if and only if it contains no odd-length cycle**. The BFS algorithm detects this because any same-color conflict corresponds to an odd-length path between two vertices in the same BFS level, which combined with the BFS tree path forms an odd cycle. Bipartiteness is a foundational property because it enables efficient algorithms for **maximum matching** (the Hungarian algorithm, Hopcroft-Karp), **vertex cover**, and **independent set** — problems that are NP-hard on general graphs but polynomial on bipartite graphs.
