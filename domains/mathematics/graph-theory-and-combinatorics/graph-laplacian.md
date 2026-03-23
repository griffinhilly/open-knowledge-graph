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
stage: formal-systems
status: draft
---

# Graph Laplacian and Spectral Properties

## Core Idea
The Laplacian matrix L = D - A (where D is the diagonal degree matrix) has smallest eigenvalue 0 with eigenvector all-ones. The second-smallest eigenvalue (algebraic connectivity) measures graph connectivity. The Laplacian's null space and eigenvalues reveal graph structure, cuts, and dynamical properties in many applications.

## Questions

```yaml
- question: "A graph has 3 connected components. How many zero eigenvalues does its Laplacian matrix have?"
  type: multiple-choice
  options:
    - "1 — the all-ones vector is always in the null space, giving exactly one zero eigenvalue"
    - "0 — a graph with multiple components is not well-defined for Laplacian analysis"
    - "3 — the number of zero eigenvalues equals the number of connected components"
    - "It depends on the number of edges, not the number of components"
  answer: 2
  explanation: "Each connected component contributes exactly one zero eigenvalue to the Laplacian, with a corresponding eigenvector that is 1 on the vertices of that component and 0 elsewhere. For a single connected graph, only the global all-ones vector is in the null space (one zero eigenvalue). For three components, there are three independent all-ones-on-component vectors in the null space. This means you can determine graph connectivity just by counting zero eigenvalues — no BFS or DFS required."

- question: "Graph A has a Fiedler value (λ₂) near zero; Graph B has a large Fiedler value. Both have the same number of vertices and edges. Which claim is best supported?"
  type: multiple-choice
  options:
    - "Graph A is better connected than B, since a small eigenvalue means more stable dynamics"
    - "Graph A has a near-bottleneck — a small cut set of edges whose removal would nearly disconnect it; Graph B is well-connected with many independent paths"
    - "Graph B has more spanning trees than A, since larger eigenvalues indicate more edges"
    - "Both graphs must be identical in connectivity since they have the same number of edges"
  answer: 1
  explanation: "The Fiedler value measures algebraic connectivity: large λ₂ means the graph is robust and well-connected with many independent paths between most vertex pairs. Small λ₂ (near zero) means the graph is close to being disconnected — there is a bottleneck where a small edge cut would fragment it. The Fiedler vector corresponding to λ₂ encodes the near-optimal partition split, which is why λ₂ and its eigenvector are the basis of spectral graph partitioning and spectral clustering."

- question: "Since L·1 = 0 (the all-ones vector is in the Laplacian's null space), every graph — connected or not — has exactly one zero eigenvalue."
  type: true-false
  answer: false
  explanation: "For a connected graph, there is exactly one zero eigenvalue, corresponding to the global all-ones vector. For a disconnected graph with k components, there are k zero eigenvalues — one per component — because each component contributes its own independent null-space vector (1 on its vertices, 0 elsewhere). Counting zero eigenvalues is precisely how the Laplacian encodes connectivity information."

- question: "The eigenvector corresponding to the Fiedler value (second-smallest eigenvalue of the Laplacian) can be used to partition a graph into two groups with few inter-group edges — the basis of spectral clustering."
  type: true-false
  answer: true
  explanation: "The Fiedler vector assigns a real value to each vertex. By partitioning vertices into those with positive values and those with negative values (or by threshold), you obtain two groups with approximately minimal edge cut between them. This is not an exact solution to the NP-hard minimum cut problem, but the Fiedler vector gives a near-optimal relaxed solution. This spectral approach is widely used in network analysis, image segmentation, and machine learning."

- question: "Why does the graph Laplacian L = D − A always have 0 as an eigenvalue, and what property of the graph does the number of zero eigenvalues reveal?"
  type: short-answer
  answer: "L always has 0 as an eigenvalue because the all-ones vector 1 satisfies L·1 = 0: for each row i, the diagonal entry is deg(i) and each off-diagonal entry is −1 for each neighbor, so the sum is deg(i) − deg(i) = 0. The number of zero eigenvalues equals the number of connected components in the graph, because each component contributes one independent null-space vector."
  explanation: "This is a beautiful example of algebra encoding topology: a purely algebraic object (the eigenvalue count of a matrix) reveals a topological property (connectivity) without any explicit graph traversal. It also motivates why the Laplacian appears in so many contexts — electrical networks, heat diffusion, PageRank — because zero eigenvalues correspond to 'conserved quantities' or 'equilibrium modes' of whatever dynamics the graph represents."
```

## Explainer

You already know the **adjacency matrix** A, where entry A[i][j] = 1 if there's an edge between vertices i and j. Now introduce the **degree matrix** D: a diagonal matrix where D[i][i] is the degree of vertex i (how many edges it has). The **graph Laplacian** is simply L = D − A. For each vertex, the diagonal entry is its degree, and each off-diagonal entry is −1 if the vertices are connected, 0 otherwise. This encoding might seem arbitrary, but it captures a deep geometric structure.

The simplest property: the all-ones vector **1** is always in the null space of L, meaning L**1** = **0**. Check it directly: for row i, the diagonal entry is deg(i), and the off-diagonal entries are −1 for each neighbor of i. Multiplying the all-ones vector gives deg(i) × 1 + (−1) × deg(i) = 0. This means 0 is always an eigenvalue. More importantly, the number of zero eigenvalues equals the number of **connected components** in the graph. A disconnected graph has multiple independent "islands," and the Laplacian's null space captures exactly one eigenvector per island. So just by computing eigenvalues of L, you can determine graph connectivity without doing a BFS or DFS search.

The second-smallest eigenvalue λ₂ is called the **Fiedler value** or **algebraic connectivity**. When λ₂ is large, the graph is "well-connected" — there are many independent paths between most pairs of vertices, no easy bottleneck to cut. When λ₂ is small (but positive), the graph has a "narrow bridge" — a small set of edges whose removal would nearly disconnect it. This is directly useful for **graph partitioning**: the eigenvector corresponding to λ₂ (the Fiedler vector) encodes a near-optimal split of the vertices into two groups, with as few edges as possible crossing between them. This is the basis for **spectral clustering**, a widely used technique in machine learning and network analysis.

The Laplacian also appears in physics and analysis. If you assign a voltage to each vertex and let current flow along edges (like a resistor network), Kirchhoff's laws translate exactly to a linear system Lv = b. The Laplacian operator on continuous surfaces (which you may encounter in calculus or PDEs) is the limiting analog — the matrix Laplacian is literally the discrete version of the continuous ∇² operator. This connection is why the Laplacian appears everywhere from graph algorithms to image processing, finite element analysis, and the simulation of heat diffusion on networks. The eigenvalues don't just describe the matrix — they describe how signals, flows, and information spread through the graph.
