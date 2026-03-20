---
id: graph-matrices-representations
title: 'Graph Representation: Adjacency and Incidence Matrices'
domain: mathematics
course: discrete-math
prerequisites:
- id: adjacency-matrix
  type: hard
- id: graph-fundamentals-discrete
  type: hard
builds-toward:
- connectivity-components-discrete
tags:
- adjacency-matrix
- incidence-matrix
- representation
- computation
stage: advanced
status: draft
---

# Graph Representation: Adjacency and Incidence Matrices

## Core Idea
An adjacency matrix A represents a graph where A[i,j] is the number of edges from vertex i to vertex j (0 or 1 for simple graphs). An incidence matrix shows vertex-edge relationships. These representations enable algorithmic computation on graphs.

## How It's Best Learned
Construct adjacency matrices for small graphs by hand. Observe that A² counts paths of length 2. See how matrix properties (symmetry, sparsity) reflect graph structure.

## Common Misconceptions
The adjacency matrix for an undirected graph is symmetric; for directed graphs it need not be. Diagonal entries are 0 in simple graphs (no self-loops).

## Explainer

You've already met the **adjacency matrix** as a way to represent a graph. Now we extend that idea and think more carefully about what these matrix representations buy us computationally.

The adjacency matrix A of an n-vertex graph is an n×n matrix where A[i][j] = 1 if there is an edge from vertex i to vertex j, and 0 otherwise. For an undirected graph, every edge {i, j} contributes a 1 in both A[i][j] and A[j][i], which is why the matrix is symmetric. For a directed graph (digraph), an edge i → j contributes only to A[i][j] — there's no automatic reciprocal — so symmetry is not guaranteed. Diagonal entries are 0 in a simple graph because self-loops are disallowed.

What makes the adjacency matrix powerful is that matrix multiplication encodes graph structure. The entry (A²)[i][j] counts the number of length-2 walks from vertex i to vertex j — the number of intermediate vertices k such that i → k and k → j. More generally, (Aᵏ)[i][j] counts all walks of exactly length k from i to j. This connects linear algebra to graph reachability: if all entries of A + A² + … + Aⁿ⁻¹ are positive, the graph is strongly connected.

The **incidence matrix** is a different representation. For a graph with n vertices and m edges, the incidence matrix is an n×m matrix where each column corresponds to one edge. For an undirected graph, each column has exactly two 1s (marking the two endpoints of that edge). For directed graphs, each column has a +1 at the tail vertex and a −1 at the head vertex. This matrix is particularly useful in circuit analysis and network flow, where it encodes how edges connect into vertices.

A practical consideration: for large sparse graphs (graphs with few edges relative to the number of vertices), the adjacency matrix is wasteful — most entries are 0. In these cases, an **adjacency list** representation is preferred algorithmically. But the matrix form remains indispensable for theoretical analysis and for dense graphs, because matrix operations are well-studied and can leverage linear algebra's full toolkit, including eigendecomposition and spectral methods.
