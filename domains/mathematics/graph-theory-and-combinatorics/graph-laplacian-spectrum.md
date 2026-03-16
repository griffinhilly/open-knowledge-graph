---
id: graph-laplacian-spectrum
title: Graph Laplacian and Laplacian Spectrum
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: adjacency-matrix-graphs
  type: hard
builds-toward:
- matrix-tree-theorem
tags:
- graph-laplacian
- spectral-gaps
- connectivity
stage: advanced
status: draft
---

# Graph Laplacian and Laplacian Spectrum

## Core Idea
The Laplacian matrix L = D − A (D = degree diagonal, A = adjacency) is central to spectral graph theory. Its smallest nonzero eigenvalue (algebraic connectivity) measures graph robustness; eigenvectors reveal graph structure. The Laplacian spectrum unifies many graph properties.

## Explainer

From your work with the adjacency matrix, you know how to represent a graph algebraically: entry A[i][j] = 1 if there is an edge between vertices i and j. The **Laplacian matrix** L is built from A by one additional step: construct the **degree matrix** D, a diagonal matrix where D[i][i] is the degree of vertex i (the number of edges incident to it). Then L = D − A. Each row of L sums to zero, which is not a coincidence — it reflects a fundamental balance property of the graph.

The Laplacian's eigenvalues — its **spectrum** — encode structural information about the graph in a remarkably direct way. The smallest eigenvalue is always 0, corresponding to the eigenvector that is constant on all vertices. The number of times 0 appears as an eigenvalue equals the number of **connected components**: a connected graph has exactly one zero eigenvalue, a graph with k components has k. This makes the spectrum an algebraic test for connectivity.

The second-smallest eigenvalue, denoted λ₂ or **algebraic connectivity** (also called the Fiedler value), measures how well-connected a graph is. A small λ₂ means the graph has a bottleneck — there are two large groups of vertices connected by only a thin bridge of edges. A large λ₂ means vertices are densely interconnected. This value appears in bounds on the graph's **edge expansion** (how many edges you must cut to divide the graph in two), making it fundamental to network robustness analysis and the study of expander graphs.

The eigenvector corresponding to λ₂ — the **Fiedler vector** — provides even more: sorting vertices by their Fiedler vector coordinate gives a natural linear ordering that approximates a minimum-cut bisection of the graph. This technique, called **spectral partitioning**, is widely used in clustering algorithms, image segmentation, and graph layout. The Laplacian thus bridges pure combinatorics (counting edges and vertices) and linear algebra (eigenvalues and eigenvectors), providing tools that no purely combinatorial approach can match.
