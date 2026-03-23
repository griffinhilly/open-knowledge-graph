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
stage: formal-systems
status: draft
---

# Graph Representation: Adjacency and Incidence Matrices

## Core Idea
An adjacency matrix A represents a graph where A[i,j] is the number of edges from vertex i to vertex j (0 or 1 for simple graphs). An incidence matrix shows vertex-edge relationships. These representations enable algorithmic computation on graphs.

## How It's Best Learned
Construct adjacency matrices for small graphs by hand. Observe that A² counts paths of length 2. See how matrix properties (symmetry, sparsity) reflect graph structure.

## Common Misconceptions
The adjacency matrix for an undirected graph is symmetric; for directed graphs it need not be. Diagonal entries are 0 in simple graphs (no self-loops).

## Questions

```yaml
- question: "For a graph G with adjacency matrix A, the entry (A²)[i][j] = 3. What does this tell you about the graph?"
  type: multiple-choice
  options:
    - "There are 3 edges directly connecting vertex i to vertex j"
    - "There are 3 distinct walks of length exactly 2 from vertex i to vertex j — meaning 3 different intermediate vertices k such that edges i→k and k→j both exist"
    - "Vertex i and vertex j are 3 hops apart in the shortest path"
    - "There are 3 triangles (3-cycles) in the graph that include both vertex i and vertex j"
  answer: 1
  explanation: "Matrix multiplication encodes path counting. The entry (A²)[i][j] = Σ_k A[i][k] × A[k][j] counts the number of intermediate vertices k where both A[i][k] = 1 and A[k][j] = 1 — i.e., the number of length-2 walks from i to j. A value of 3 means there are exactly 3 such intermediate vertices. This is not the shortest-path distance (that would require different algorithms like BFS), and it counts walks, not paths — if any of those 3 walks revisit vertices, they still count. This connection between linear algebra and graph structure is the key insight of the adjacency matrix representation."

- question: "For which type of graph is an adjacency list representation generally preferred over an adjacency matrix, and why?"
  type: multiple-choice
  options:
    - "Dense graphs, because adjacency lists enumerate all edges explicitly while matrices require index lookups"
    - "Small graphs, because adjacency lists fit in a single array while matrix construction is computationally expensive"
    - "Sparse graphs, because the adjacency matrix is mostly zeros and wastes O(n²) space to represent O(n) or O(m) edges"
    - "Directed graphs, because adjacency lists naturally represent asymmetric relationships while matrices require separate row/column logic"
  answer: 2
  explanation: "An adjacency matrix for an n-vertex graph always requires O(n²) space regardless of the number of edges. For a sparse graph — one with far fewer edges than n² — the matrix is mostly zeros and this space is wasted. An adjacency list represents only the edges that actually exist, using O(n + m) space where m is the number of edges. For a sparse graph where m << n², the adjacency list is dramatically more efficient. For a dense graph (m close to n²), the matrix is more appropriate, especially since it enables fast edge-existence queries (O(1) vs. O(degree) for lists) and leverages linear algebra tools like matrix multiplication and eigendecomposition."

- question: "The adjacency matrix of an undirected graph is always symmetric because every edge {i, j} contributes entries in both A[i][j] and A[j][i]."
  type: true-false
  answer: true
  explanation: "In an undirected graph, an edge between vertices i and j means you can traverse it in either direction. The adjacency matrix represents this by setting both A[i][j] = 1 and A[j][i] = 1. Since this is true for every edge, the resulting matrix satisfies A = Aᵀ — the definition of a symmetric matrix. This symmetry is not a coincidence but a direct encoding of the undirected nature of the edges. For directed graphs, an edge i → j only contributes A[i][j] = 1, with no automatic reciprocal, so the matrix need not be symmetric."

- question: "If A[i][j] = 1 in the adjacency matrix of a directed graph, then A[j][i] must also equal 1."
  type: true-false
  answer: false
  explanation: "In a directed graph (digraph), A[i][j] = 1 means there is a directed edge from vertex i to vertex j. This says nothing about whether there is an edge from j back to i. A[j][i] = 1 would require a separate directed edge j → i to exist. The adjacency matrix of a directed graph is therefore not necessarily symmetric. This asymmetry is precisely what makes the directed/undirected distinction matter in the matrix representation: symmetry is a property of the undirected case, not a general property of adjacency matrices."

- question: "Explain what information is encoded in the matrix A² (A squared), and describe why this result connects matrix algebra to graph reachability."
  type: short-answer
  answer: "A² is computed by the standard matrix product: (A²)[i][j] = Σ_k A[i][k] × A[k][j]. Because A[i][k] and A[k][j] are each 0 or 1 (for a simple graph), their product is 1 only when both edges exist — i.e., when k is an intermediate vertex with edges from i to k and from k to j. Summing over all k therefore counts the number of length-2 walks from i to j. More generally, (Aᵏ)[i][j] counts all walks of exactly length k from i to j. This connects to reachability: if any entry of A + A² + ... + Aⁿ⁻¹ is positive for all (i,j) pairs, the graph is strongly connected — every vertex can reach every other within at most n-1 steps. The matrix representation thus allows questions about graph structure (connectivity, path counting) to be answered using the toolkit of linear algebra."
  explanation: "This connection is the foundation of spectral graph theory: the eigenvalues and eigenvectors of the adjacency matrix encode deep structural properties of the graph — including connectivity, bipartiteness, and expansion. Matrix multiplication is just the entry point into this much richer relationship."
```

## Explainer

You've already met the **adjacency matrix** as a way to represent a graph. Now we extend that idea and think more carefully about what these matrix representations buy us computationally.

The adjacency matrix A of an n-vertex graph is an n×n matrix where A[i][j] = 1 if there is an edge from vertex i to vertex j, and 0 otherwise. For an undirected graph, every edge {i, j} contributes a 1 in both A[i][j] and A[j][i], which is why the matrix is symmetric. For a directed graph (digraph), an edge i → j contributes only to A[i][j] — there's no automatic reciprocal — so symmetry is not guaranteed. Diagonal entries are 0 in a simple graph because self-loops are disallowed.

What makes the adjacency matrix powerful is that matrix multiplication encodes graph structure. The entry (A²)[i][j] counts the number of length-2 walks from vertex i to vertex j — the number of intermediate vertices k such that i → k and k → j. More generally, (Aᵏ)[i][j] counts all walks of exactly length k from i to j. This connects linear algebra to graph reachability: if all entries of A + A² + … + Aⁿ⁻¹ are positive, the graph is strongly connected.

The **incidence matrix** is a different representation. For a graph with n vertices and m edges, the incidence matrix is an n×m matrix where each column corresponds to one edge. For an undirected graph, each column has exactly two 1s (marking the two endpoints of that edge). For directed graphs, each column has a +1 at the tail vertex and a −1 at the head vertex. This matrix is particularly useful in circuit analysis and network flow, where it encodes how edges connect into vertices.

A practical consideration: for large sparse graphs (graphs with few edges relative to the number of vertices), the adjacency matrix is wasteful — most entries are 0. In these cases, an **adjacency list** representation is preferred algorithmically. But the matrix form remains indispensable for theoretical analysis and for dense graphs, because matrix operations are well-studied and can leverage linear algebra's full toolkit, including eigendecomposition and spectral methods.
