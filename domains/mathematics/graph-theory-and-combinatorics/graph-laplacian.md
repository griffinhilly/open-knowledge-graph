---
id: graph-laplacian
title: Graph Laplacian and Spectral Properties
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: adjacency-matrix
  type: hard
builds-toward:
- matrix-tree-theorem
tags:
- algebraic-graph-theory
- laplacian
stage: advanced
status: draft
---

# Graph Laplacian and Spectral Properties

## Core Idea
The Laplacian matrix L = D - A (where D is the diagonal degree matrix) has smallest eigenvalue 0 with eigenvector all-ones. The second-smallest eigenvalue (algebraic connectivity) measures graph connectivity. The Laplacian's null space and eigenvalues reveal graph structure, cuts, and dynamical properties in many applications.

## Explainer

You already know the **adjacency matrix** A, where entry A[i][j] = 1 if there's an edge between vertices i and j. Now introduce the **degree matrix** D: a diagonal matrix where D[i][i] is the degree of vertex i (how many edges it has). The **graph Laplacian** is simply L = D − A. For each vertex, the diagonal entry is its degree, and each off-diagonal entry is −1 if the vertices are connected, 0 otherwise. This encoding might seem arbitrary, but it captures a deep geometric structure.

The simplest property: the all-ones vector **1** is always in the null space of L, meaning L**1** = **0**. Check it directly: for row i, the diagonal entry is deg(i), and the off-diagonal entries are −1 for each neighbor of i. Multiplying the all-ones vector gives deg(i) × 1 + (−1) × deg(i) = 0. This means 0 is always an eigenvalue. More importantly, the number of zero eigenvalues equals the number of **connected components** in the graph. A disconnected graph has multiple independent "islands," and the Laplacian's null space captures exactly one eigenvector per island. So just by computing eigenvalues of L, you can determine graph connectivity without doing a BFS or DFS search.

The second-smallest eigenvalue λ₂ is called the **Fiedler value** or **algebraic connectivity**. When λ₂ is large, the graph is "well-connected" — there are many independent paths between most pairs of vertices, no easy bottleneck to cut. When λ₂ is small (but positive), the graph has a "narrow bridge" — a small set of edges whose removal would nearly disconnect it. This is directly useful for **graph partitioning**: the eigenvector corresponding to λ₂ (the Fiedler vector) encodes a near-optimal split of the vertices into two groups, with as few edges as possible crossing between them. This is the basis for **spectral clustering**, a widely used technique in machine learning and network analysis.

The Laplacian also appears in physics and analysis. If you assign a voltage to each vertex and let current flow along edges (like a resistor network), Kirchhoff's laws translate exactly to a linear system Lv = b. The Laplacian operator on continuous surfaces (which you may encounter in calculus or PDEs) is the limiting analog — the matrix Laplacian is literally the discrete version of the continuous ∇² operator. This connection is why the Laplacian appears everywhere from graph algorithms to image processing, finite element analysis, and the simulation of heat diffusion on networks. The eigenvalues don't just describe the matrix — they describe how signals, flows, and information spread through the graph.
