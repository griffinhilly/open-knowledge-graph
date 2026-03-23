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
stage: formal-systems
status: validated
---

# Adjacency Matrix and Spectral Basics

## Core Idea
The adjacency matrix A of a graph has A[i,j] = 1 if vertices i,j are adjacent, 0 otherwise. Its eigenvalues (spectrum) encode structural information: largest eigenvalue relates to max degree, closed walks of length k appear in tr(A^k), and spectral properties reveal connectivity, regularity, and expansion. Spectral graph theory bridges linear algebra and graph combinatorics.

## Questions

```yaml
- question: "What does the (i, j) entry of the matrix A³ represent for an undirected graph with adjacency matrix A?"
  type: multiple-choice
  options:
    - "1 if vertices i and j are connected by a path of length exactly 3, 0 otherwise"
    - "The number of walks of length 3 from vertex i to vertex j"
    - "The number of edges on the shortest path between vertices i and j"
    - "The degree of vertex i if i = j, and 0 otherwise"
  answer: 1
  explanation: "A³[i,j] counts the number of *walks* of length 3 from i to j — sequences where each consecutive pair is adjacent, with possible vertex repetition. This is not the same as *paths* (which require no repeated vertices). The result follows from matrix multiplication: (A²)[i,j] = Σₖ A[i,k]·A[k,j] counts length-2 walks; multiplying by A again extends to length 3. The diagonal entries tr(A³) count closed walks of length 3, giving 6 × (number of triangles)."

- question: "A connected graph has a large spectral gap — the difference between its largest and second-largest eigenvalue of the adjacency matrix is close to the maximum degree. What does this imply?"
  type: multiple-choice
  options:
    - "The graph has very few edges relative to its vertex count"
    - "Random walks on the graph mix rapidly and no small cut separates the graph into large pieces"
    - "The graph is bipartite"
    - "The graph has a unique Hamiltonian cycle"
  answer: 1
  explanation: "A large spectral gap is the hallmark of an expander graph — one with strong expansion properties. It means for any set of vertices, many edges leave the set, so no small cut isolates a large portion. Random walks on such graphs also mix to the stationary distribution rapidly. Expanders with large spectral gaps are used in network design, error-correcting codes, and derandomization in theoretical computer science."

- question: "The adjacency matrix of an undirected graph can have complex (non-real) eigenvalues."
  type: true-false
  answer: false
  explanation: "The adjacency matrix of an undirected graph is symmetric (A[i,j] = A[j,i]). By the spectral theorem, every real symmetric matrix has real eigenvalues. Complex eigenvalues can appear in adjacency matrices of *directed* graphs, where A is not necessarily symmetric. This is one reason undirected graphs are algebraically simpler — their spectrum is always a real set of numbers."

- question: "The number of triangles in a graph can be determined from the trace of A³, where A is the adjacency matrix."
  type: true-false
  answer: true
  explanation: "tr(A³) = Σᵢ (A³)[i,i] sums the number of closed walks of length 3 starting and ending at each vertex. Each triangle contributes exactly 6 such walks (two directions of traversal × three choices of starting vertex), so the number of triangles = tr(A³) / 6. This is a direct example of how spectral information encodes combinatorial structure without explicit edge enumeration."

- question: "Why is the spectrum of the adjacency matrix considered a 'structural fingerprint' of a graph rather than simply a convenient way to store edge information?"
  type: short-answer
  answer: "The eigenvalues of the adjacency matrix encode combinatorial properties not obvious from the edge list: the largest eigenvalue bounds maximum degree, the spectral gap measures connectivity and expansion, bipartite graphs have spectra symmetric around zero, and matrix powers count closed walks and detect substructures like triangles. These properties emerge from the eigenvalues themselves, making the spectrum a compressed description of global graph topology."
  explanation: "The deep point is that algebraic properties (eigenvalues) map to combinatorial properties (connectivity, expansion, bipartiteness, subgraph counts). This bridge between linear algebra and graph theory is what makes spectral graph theory powerful: you can analyze global graph structure using efficient matrix tools rather than exhaustive graph traversal."
```

## Explainer

You know how to represent a graph as a list of vertices and edges, and you've studied eigenvalues and eigenvectors as tools for analyzing linear transformations. The adjacency matrix brings these two worlds together: it encodes a graph as a matrix, making the full machinery of linear algebra available for studying graph structure.

The construction is direct. Label the vertices 1 through n. The **adjacency matrix** A is an n×n matrix where A[i,j] = 1 if there is an edge between vertices i and j, and 0 otherwise. For an undirected graph, A is symmetric (A[i,j] = A[j,i]) because edges are mutual. Matrix multiplication immediately reveals structure: A²[i,j] counts the number of walks of length 2 from vertex i to vertex j (one intermediate vertex k must be adjacent to both). More generally, Aᵏ[i,j] counts walks of length k from i to j. The trace tr(Aᵏ) — the sum of diagonal entries — counts **closed walks** of length k: for example, tr(A³)/6 gives the number of triangles in the graph, since each triangle contributes 6 closed walks of length 3 (two directions, three starting vertices).

The **spectrum** of A — its set of eigenvalues — is a structural fingerprint of the graph. Because A is symmetric (for undirected graphs), all eigenvalues are real. The **largest eigenvalue** (spectral radius) is bounded by the maximum degree; a d-regular graph (every vertex has degree d) has spectral radius exactly d, with the all-ones vector as the corresponding eigenvector. The **spectral gap** — the difference between the largest and second-largest eigenvalue — measures how well-connected the graph is. A large spectral gap means random walks on the graph mix rapidly and the graph has strong **expansion** properties: no small set of edges separates the graph into large pieces. This is why expander graphs, which have large spectral gaps, are useful in network design and theoretical computer science.

Spectral properties also reveal combinatorial structure directly. **Bipartite graphs** have spectra symmetric around zero: if λ is an eigenvalue, so is −λ. The number of zero eigenvalues of A is related to the rank of the matrix and the structure of connected components. **Spectral clustering** — partitioning a graph by computing eigenvectors of a related matrix (the graph Laplacian) — exploits these connections to identify natural communities in networks, making spectral graph theory central to machine learning and network analysis. The key takeaway is that a matrix encoding a graph is not just a notation convenience: its eigenvalues carry deep information about connectivity, bottlenecks, and long-term behavior of processes on the graph.
