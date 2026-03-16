---
id: graph-representation
title: 'Graph Representation: Matrices and Lists'
domain: mathematics
course: discrete-math
prerequisites:
- id: graph-theory-intro
  type: hard
- id: matrices-intro
  type: soft
builds-toward:
- graph-connectivity
- graph-isomorphism
tags:
- adjacency-matrix
- adjacency-list
- graph-representation
- incidence-matrix
stage: formal-systems
status: validated
---

# Graph Representation: Matrices and Lists

## Core Idea
Graphs can be represented computationally in multiple ways. An adjacency matrix is an n×n matrix where entry (i,j) is 1 if there is an edge from vertex i to vertex j, and 0 otherwise. An adjacency list stores, for each vertex, the list of its neighbors. Adjacency matrices support O(1) edge lookup but use O(n²) space; adjacency lists use space proportional to vertices plus edges and are preferred for sparse graphs. Powers of the adjacency matrix count the number of walks of a given length between vertices.

## How It's Best Learned
Practice converting between graph drawings and both matrix and list representations for the same graph. Compare storage trade-offs for dense versus sparse graphs with concrete examples. Compute A² for a small graph and verify it counts 2-step walks.

## Common Misconceptions
- Assuming adjacency matrices are always symmetric — this is only true for undirected graphs.
- Ignoring space-versus-time trade-offs when choosing a representation for a given application.

## Questions

```yaml
- question: "A sparse graph has 1,000 vertices and 2,000 edges. Approximately how much memory does an adjacency matrix require compared to an adjacency list?"
  type: multiple-choice
  options:
    - "About the same — both scale with edges"
    - "The adjacency list uses more memory because it stores pointers"
    - "The adjacency matrix uses about 333 times more memory"
    - "The adjacency matrix is always preferred because it supports O(1) lookup"
  answer: 2
  explanation: "The adjacency matrix requires n² = 1,000,000 entries. The adjacency list requires O(|V| + |E|) = 1,000 + 2×2,000 ≈ 5,000 entries (each edge appears in two lists for an undirected graph). That is roughly 1,000,000 / 5,000 = 200× more memory for the matrix. For sparse graphs, adjacency lists are strongly preferred despite the O(1) lookup advantage of matrices."

- question: "For an undirected graph, the adjacency matrix is always symmetric (A[i][j] = A[j][i] for all i, j)."
  type: true-false
  answer: true
  explanation: "In an undirected graph, an edge between vertices i and j means both A[i][j] = 1 and A[j][i] = 1 — the edge exists in both directions. Symmetry follows directly. For directed graphs this does not hold: an arc from i to j sets A[i][j] = 1 but A[j][i] remains 0 unless there is also an arc from j to i. Always check whether the graph is directed before assuming symmetry."

- question: "You compute A², where A is the adjacency matrix of a graph. What does the entry (A²)[i][j] count, and why?"
  type: short-answer
  answer: "It counts the number of distinct walks of length 2 from vertex i to vertex j — that is, the number of intermediate vertices k such that edges i→k and k→j both exist."
  explanation: "Matrix multiplication gives (A²)[i][j] = Σ_k A[i][k] · A[k][j]. The product A[i][k] · A[k][j] equals 1 only when both edges exist (i to k and k to j). Summing over all possible intermediate vertices k counts how many 2-step walks exist from i to j. More generally, (A^m)[i][j] counts walks of length m, making matrix powers a powerful tool for analyzing graph connectivity."
```

## Explainer

When you first learned about graphs, the representation was visual: vertices as dots, edges as lines. To compute with graphs — to run algorithms, store them in memory, or analyze their structure — you need a formal data structure. The two standard choices, adjacency matrices and adjacency lists, each make different operations fast and encode the same information differently.

An **adjacency matrix** is an n×n grid where entry A[i][j] = 1 if there is an edge from vertex i to vertex j, and 0 otherwise. For an undirected graph, it is symmetric. The key advantages: checking whether a specific edge exists is O(1) — just look up the entry. The key cost: it always uses n² space, regardless of how many edges exist. For a dense graph (many edges relative to n²) this is fine; for a sparse graph with only a handful of edges per vertex, most of the matrix is zeros and the space is wasted.

An **adjacency list** stores, for each vertex, only the list of its actual neighbors. Total storage is proportional to |V| + |E| — the number of vertices plus the number of edges. For sparse graphs (common in practice), this is dramatically smaller than n². The trade-off: checking whether a specific edge (i, j) exists requires scanning vertex i's neighbor list, which takes time proportional to i's degree rather than O(1). Many graph algorithms — BFS, DFS, shortest paths — naturally iterate over a vertex's neighbors rather than checking arbitrary edges, which is why they are typically implemented with adjacency lists.

The adjacency matrix also supports a striking algebraic property: the entry (A^m)[i][j] counts the number of walks of length m from vertex i to vertex j. This follows from matrix multiplication: (A²)[i][j] = Σ_k A[i][k] · A[k][j] sums over all intermediate vertices k, counting those where both legs of a 2-step walk exist. This property connects graph theory to linear algebra and enables techniques like computing reachability or counting paths using matrix exponentiation.

Choosing a representation is an engineering decision, not a mathematical one. The right answer depends on the graph's density, the operations your algorithm needs most frequently, and memory constraints. Understanding both representations — and being able to convert between them fluently — is the foundation for analyzing and implementing graph algorithms.
