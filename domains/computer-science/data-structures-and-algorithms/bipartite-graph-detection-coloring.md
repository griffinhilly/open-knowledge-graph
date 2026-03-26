---
id: bipartite-graph-detection-coloring
title: 'Bipartite Graphs: Detection and Two-Coloring'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: breadth-first-search
  type: hard
- id: graph-depth-first-search-applications
  type: soft
tags:
- graphs
- bipartite
- coloring
stage: formal-systems
status: validated
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

## Questions

```yaml
- question: "You run BFS-based 2-coloring on a graph and find that two adjacent vertices both receive color 'red.' What can you conclude?"
  type: multiple-choice
  options:
    - "The graph has a triangle (3-cycle), which disqualifies bipartiteness"
    - "The graph contains an odd-length cycle, so it is not bipartite"
    - "The graph contains an even-length cycle, so it is not bipartite"
    - "BFS was applied incorrectly; restarting from a different vertex may succeed"
  answer: 1
  explanation: "A same-color conflict during 2-coloring means the graph is not bipartite. The conflict corresponds to an odd-length cycle — specifically, the BFS tree path between those two vertices combined with the edge between them forms an odd cycle. The cycle need not be a triangle; cycles of length 5, 7, etc. also cause conflicts. A graph can lack triangles entirely and still be non-bipartite if it has a longer odd cycle (e.g., a 5-cycle)."

- question: "A graph has n vertices and n−1 edges and is connected. Is it necessarily bipartite?"
  type: multiple-choice
  options:
    - "Yes — any tree is bipartite because trees have no cycles at all"
    - "Yes — any graph with fewer than n edges is bipartite"
    - "No — a connected graph with n−1 edges might still contain odd cycles"
    - "No — bipartiteness only applies to dense graphs"
  answer: 0
  explanation: "A connected graph with n vertices and n−1 edges is a tree, and all trees are bipartite. Trees contain no cycles at all, so they trivially satisfy the condition of having no odd cycles. The 2-coloring of a tree is straightforward: BFS assigns alternating colors down each branch and never encounters a conflict. This is a useful special case: whenever you know a graph is a tree (or forest), you also know it is bipartite."

- question: "A graph with no triangles (3-cycles) is very likely to be bipartite."
  type: true-false
  answer: false
  explanation: "This is a classic misconception. Bipartiteness requires the absence of ALL odd-length cycles, not just triangles. A 5-cycle (pentagon) is not bipartite — it contains no triangle, yet it has an odd cycle. Try 2-coloring a 5-cycle: alternating red/blue around the ring, you return to the start needing the wrong color. The correct characterization is: a graph is bipartite if and only if it contains no odd-length cycle of any length."

- question: "Bipartite graph detection using BFS runs in O(V²) time because it should check most pairs of vertices."
  type: true-false
  answer: false
  explanation: "BFS-based 2-coloring runs in O(V + E) — the same time complexity as BFS itself. Each vertex is visited once and colored once; each edge is examined once to check whether its endpoints have conflicting colors. There is no need to check all vertex pairs. This linear time complexity is one of the important practical points about bipartite detection: it is cheap to test and enables efficient algorithms like bipartite matching (Hopcroft-Karp) to begin with a linear-time feasibility check."

- question: "Explain why an odd-length cycle prevents a graph from being 2-colorable, and why an even-length cycle does not."
  type: short-answer
  answer: "In a 2-coloring, adjacent vertices must receive opposite colors. Walking around a cycle and alternating colors, each step flips the color. After k steps, you return to the start; if k is even, you have flipped an even number of times and end with the starting color — no conflict. If k is odd, you end with the opposite color, creating a conflict with the starting vertex. Even cycles can always be 2-colored; odd cycles cannot."
  explanation: "This parity argument is the heart of the bipartite theorem. It shows that the obstruction to bipartiteness is exactly odd cycles — not self-loops, not even cycles, not any other structure. The BFS 2-coloring algorithm directly implements this check: a same-color conflict between an edge's endpoints means there is an odd-length path in the BFS tree connecting them, and that path plus the edge form an odd cycle."
```

## Explainer

From your work with breadth-first search, you know how BFS explores a graph level by level, visiting all vertices at distance 1 from the source before those at distance 2, and so on. Bipartite graph detection is one of the most elegant applications of BFS, because the level structure of BFS directly corresponds to the two-coloring that defines bipartiteness.

A graph is **bipartite** if its vertices can be divided into two disjoint sets — call them "red" and "blue" — such that every edge connects a red vertex to a blue vertex. No edge ever connects two vertices of the same color. Think of a scheduling problem: students on one side, courses on the other, with edges representing enrollment. No edge connects two students or two courses — the graph is naturally bipartite. Trees are always bipartite. Grid graphs (like a checkerboard) are always bipartite. But add a single edge that creates an odd-length cycle, and bipartiteness breaks.

The detection algorithm is BFS with coloring. Pick any unvisited vertex, color it red, and add it to the queue. When you dequeue a vertex, examine each neighbor: if the neighbor is uncolored, color it the opposite color and enqueue it. If the neighbor is already colored and has the **same** color as the current vertex, you have found a conflict — the graph is not bipartite. If BFS completes without conflicts, the graph is bipartite, and the coloring you assigned is a valid 2-coloring. For disconnected graphs, repeat from each unvisited vertex. The entire process runs in O(V + E), the same as BFS itself.

Why does an odd cycle break bipartiteness? Walk around a cycle, alternating colors: red, blue, red, blue, ... If the cycle has even length, you return to the starting vertex with the correct color. If the cycle has odd length, you return needing the opposite color — a contradiction. This is not just an intuition but a theorem: **a graph is bipartite if and only if it contains no odd-length cycle**. The BFS algorithm detects this because any same-color conflict corresponds to an odd-length path between two vertices in the same BFS level, which combined with the BFS tree path forms an odd cycle. Bipartiteness is a foundational property because it enables efficient algorithms for **maximum matching** (the Hungarian algorithm, Hopcroft-Karp), **vertex cover**, and **independent set** — problems that are NP-hard on general graphs but polynomial on bipartite graphs.
