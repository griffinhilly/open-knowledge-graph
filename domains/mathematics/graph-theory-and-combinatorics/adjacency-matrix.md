---
id: adjacency-matrix
title: Adjacency Matrix and Spectral Basics
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: graph-representation
  type: hard
- id: eigenvalues-and-eigenvectors
  type: hard
builds-toward:
- graph-laplacian
- matrix-tree-theorem
tags:
- algebraic-graph-theory
- matrices
- spectrum
stage: advanced
status: draft
---

# Adjacency Matrix and Spectral Basics

## Core Idea
The adjacency matrix A of a graph has A[i,j] = 1 if vertices i,j are adjacent, 0 otherwise. Its eigenvalues (spectrum) encode structural information: largest eigenvalue relates to max degree, closed walks of length k appear in tr(A^k), and spectral properties reveal connectivity, regularity, and expansion. Spectral graph theory bridges linear algebra and graph combinatorics.

## Explainer

You know how to represent a graph as a list of vertices and edges, and you've studied eigenvalues and eigenvectors as tools for analyzing linear transformations. The adjacency matrix brings these two worlds together: it encodes a graph as a matrix, making the full machinery of linear algebra available for studying graph structure.

The construction is direct. Label the vertices 1 through n. The **adjacency matrix** A is an n×n matrix where A[i,j] = 1 if there is an edge between vertices i and j, and 0 otherwise. For an undirected graph, A is symmetric (A[i,j] = A[j,i]) because edges are mutual. Matrix multiplication immediately reveals structure: A²[i,j] counts the number of walks of length 2 from vertex i to vertex j (one intermediate vertex k must be adjacent to both). More generally, Aᵏ[i,j] counts walks of length k from i to j. The trace tr(Aᵏ) — the sum of diagonal entries — counts **closed walks** of length k: for example, tr(A³)/6 gives the number of triangles in the graph, since each triangle contributes 6 closed walks of length 3 (two directions, three starting vertices).

The **spectrum** of A — its set of eigenvalues — is a structural fingerprint of the graph. Because A is symmetric (for undirected graphs), all eigenvalues are real. The **largest eigenvalue** (spectral radius) is bounded by the maximum degree; a d-regular graph (every vertex has degree d) has spectral radius exactly d, with the all-ones vector as the corresponding eigenvector. The **spectral gap** — the difference between the largest and second-largest eigenvalue — measures how well-connected the graph is. A large spectral gap means random walks on the graph mix rapidly and the graph has strong **expansion** properties: no small set of edges separates the graph into large pieces. This is why expander graphs, which have large spectral gaps, are useful in network design and theoretical computer science.

Spectral properties also reveal combinatorial structure directly. **Bipartite graphs** have spectra symmetric around zero: if λ is an eigenvalue, so is −λ. The number of zero eigenvalues of A is related to the rank of the matrix and the structure of connected components. **Spectral clustering** — partitioning a graph by computing eigenvectors of a related matrix (the graph Laplacian) — exploits these connections to identify natural communities in networks, making spectral graph theory central to machine learning and network analysis. The key takeaway is that a matrix encoding a graph is not just a notation convenience: its eigenvalues carry deep information about connectivity, bottlenecks, and long-term behavior of processes on the graph.
