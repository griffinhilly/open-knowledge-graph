---
id: bipartite-graphs-characterization
title: Bipartite Graphs and 2-Colorability
domain: mathematics
course: discrete-math
prerequisites:
- id: degree-sequences-graphs
  type: soft
- id: bipartite-graphs-matching
  type: soft
builds-toward:
- graph-matching-halls-theorem
tags:
- graph-theory
- bipartite
- coloring
stage: formal-systems
status: validated
---
# Bipartite Graphs and 2-Colorability

## Core Idea
A graph is bipartite if its vertex set can be partitioned into two independent sets (no edges within each set). A graph is bipartite if and only if it contains no odd-length cycles. Bipartite graphs are 2-colorable and arise naturally in matching problems.

## Questions

```yaml
- question: "You run a BFS coloring algorithm on a graph: start at vertex A, color it red, and alternate colors as you traverse edges. At some point you find an edge connecting two vertices that would both need to be colored red. What does this tell you about the graph?"
  type: multiple-choice
  options:
    - "The graph is bipartite with an unusual structure requiring more than 2 colors"
    - "The graph contains an odd-length cycle and is therefore not bipartite"
    - "The graph contains an even-length cycle which prevents proper 2-coloring"
    - "The BFS coloring algorithm failed — restart from a different vertex"
  answer: 1
  explanation: "When alternating colors in BFS fails — both endpoints of an edge need the same color — you have discovered an odd-length cycle. Traversing an odd cycle with alternating colors always forces you back to the starting vertex needing the opposite color from what it already has, creating the contradiction. This is not a failure of the algorithm: it is exactly how the algorithm detects non-bipartiteness. Even-length cycles cause no such contradiction, which is why they are compatible with bipartiteness."

- question: "A graph has vertices {1, 2, 3, 4} and edges {1-2, 2-3, 3-4, 4-1}, forming a 4-cycle. Is this graph bipartite?"
  type: multiple-choice
  options:
    - "No — any cycle graph is non-bipartite"
    - "Yes — color {1, 3} red and {2, 4} blue; no two adjacent vertices share a color"
    - "No — the graph has an even number of vertices but an odd number of edges"
    - "Yes — but only because the graph has exactly four vertices"
  answer: 1
  explanation: "C4 (the 4-cycle) is bipartite: partition the vertices into {1, 3} and {2, 4}. Every edge runs between the partitions, never within one. Alternatively: C4 contains only even-length cycles (the single cycle has length 4), so by the odd-cycle theorem it is bipartite. The common misconception is that all cycles are non-bipartite — only odd cycles are. Even cycles can always be 2-colored by alternating red and blue around them."

- question: "A graph is bipartite if and only if it contains no odd-length cycles."
  type: true-false
  answer: true
  explanation: "This is the fundamental characterization theorem for bipartite graphs. The 'if' direction: if there are no odd cycles, the BFS coloring algorithm always succeeds — alternating colors around even cycles creates no contradiction. The 'only if' direction: if the graph is bipartite (2-colorable), then any cycle must alternate colors around it; an odd cycle would force the start vertex to need both colors simultaneously, which is impossible in a valid 2-coloring. So odd cycles are precisely the obstruction."

- question: "A complete graph on 4 vertices (K4) is bipartite because its vertex set can be split into two groups of 2."
  type: true-false
  answer: false
  explanation: "K4 is not bipartite. Although it has 4 vertices that can be split into two groups of 2, every vertex is connected to every other vertex — including vertices within the same group. More decisively: K4 contains triangles (3-cycles), which are odd-length cycles. By the odd-cycle theorem, any graph containing an odd cycle cannot be bipartite. Bipartiteness requires that no edges exist within each partition, which K4 violates for any partition."

- question: "Why do odd-length cycles prevent a graph from being 2-colored, while even-length cycles do not?"
  type: short-answer
  answer: "When you traverse a cycle and alternate colors, you need the first and last vertex to receive different colors (since they are the same vertex). An even cycle has an even number of steps, so alternation returns you to the starting color — no contradiction. An odd cycle has an odd number of steps, so alternation returns you to the opposite color, creating a conflict: the vertex would need to be both red and blue simultaneously."
  explanation: "The parity of cycle length is the key. Think of 2-coloring as a checkerboard pattern forced by the edges: each step flips the color. After an even number of steps, you are back to the original color. After an odd number of steps, you are at the flipped color. A cycle forces the first and last vertex to be the same node, so even steps work (same color required, same color produced) and odd steps fail (different color produced from what is required)."
```

## Explainer

A **bipartite graph** is one whose vertices can be split into two camps — call them "red" and "blue" — such that every edge runs between the camps, never within one. Job-applicant matchings are the classic image: one set of vertices represents jobs, the other represents applicants, and edges represent compatible pairs. No job connects directly to another job; no applicant to another applicant. The structure is clean and the two sets are the natural "sides."

The **two-colorability** framing is just a restatement: can you color every vertex red or blue so that no two neighbors share a color? If yes, the graph is bipartite — the two color classes are the two independent sets. This reframing is powerful because it gives you an algorithm: start at any vertex, color it red, then try to consistently color its neighbors blue, their neighbors red, and so on using BFS or DFS. If you ever encounter an edge whose both endpoints would need the same color, the graph is not bipartite.

The **odd cycle theorem** explains exactly when coloring fails. If you traverse a cycle of odd length, you will always return to the starting vertex needing the opposite color from what it already has — a contradiction. Even-length cycles cause no such problem: you can alternate colors around them cleanly. So odd cycles are precisely the obstruction to bipartiteness. If a graph has no odd cycle, it is bipartite; if it does, it is not. This is the graph-theoretic equivalent of "you can't properly 2-color a triangle."

Using what you know about **degree sequences**: in a bipartite graph with parts U and V, counting edges from the U-side and the V-side are both valid ways to count all edges — a preview of double counting ideas. The degree sequence alone does not determine bipartiteness, but understanding degree structure in each part informs matching analysis. This topic directly prepares you for Hall's theorem, which gives a precise condition for when a bipartite graph has a perfect matching: every subset S of one part has at least |S| neighbors in the other part.
