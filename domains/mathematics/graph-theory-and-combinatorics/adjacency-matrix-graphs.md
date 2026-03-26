---
id: adjacency-matrix-graphs
title: Adjacency Matrix and Spectral Graph Theory
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: formal-definitions-graph-theory
  type: hard
- id: eigenvalues-and-eigenvectors
  type: hard
builds-toward:
- graph-laplacian-spectrum
- matrix-tree-theorem
tags:
- adjacency-matrix
- spectral-methods
- eigenvalues
stage: formal-systems
status: validated
---

# Adjacency Matrix and Spectral Graph Theory

## Core Idea
The adjacency matrix A of a graph encodes its structure; its eigenvalues (spectrum) reveal deep information about the graph. The largest eigenvalue λ₁ relates to edge density, expansion properties, and diameter. Spectral methods connect linear algebra to graph combinatorics.

## Questions

```yaml
- question: "What does the (i, j) entry of A³ — the cube of an adjacency matrix — represent?"
  type: multiple-choice
  options:
    - "1 if there is a path of length at most 3 from vertex i to vertex j, and 0 otherwise"
    - "The number of walks of length 3 from vertex i to vertex j"
    - "The number of triangles in the graph that contain both vertex i and vertex j"
    - "The third power of the edge weight between vertices i and j"
  answer: 1
  explanation: "Matrix multiplication gives (A²)ᵢⱼ = Σₖ AᵢₖAₖⱼ, counting 2-step walks by summing over intermediate vertices. Extending to A³, (A³)ᵢⱼ counts all 3-step walks from i to j. Crucially, this is the number of walks (allowing revisits of vertices), not paths (which require distinct vertices) — option A confuses walks with shortest paths. Option C is related but not exact: triangle counting uses the trace of A³, not off-diagonal entries."

- question: "A network designer measures the spectral gap (λ₁ − λ₂) of two proposed topologies: topology A has spectral gap 0.05 while topology B has spectral gap 2.3. Which is preferable for rapid information broadcast, and why?"
  type: multiple-choice
  options:
    - "Topology A, because a small spectral gap means the network has more uniform edge distribution"
    - "Topology A, because small λ₂ indicates the network has fewer bottlenecks for routing"
    - "Topology B, because a large spectral gap characterizes good expanders where random walks mix quickly"
    - "Topology B, because a large spectral gap means the network is nearly complete (fully connected)"
  answer: 2
  explanation: "A large spectral gap (topology B's 2.3) means the graph is a good expander — random walks mix rapidly, information spreads quickly, and no sparse cut traps traffic in a cluster. A small spectral gap (topology A's 0.05) means the graph is nearly disconnected — a sparse cut separates large components. The Cheeger inequality makes this precise by bounding edge expansion above and below by functions of the spectral gap. Option D is wrong: expander families have bounded degree and large spectral gap without being near-complete."

- question: "For a d-regular graph (every vertex has exactly d neighbors), the largest eigenvalue of the adjacency matrix equals d."
  type: true-false
  answer: true
  explanation: "For a d-regular graph, the all-ones vector 𝟏 is an eigenvector of A with eigenvalue d, because (A𝟏)ᵢ = Σⱼ Aᵢⱼ = degree of i = d for every vertex i. By the Perron-Frobenius theorem, the largest eigenvalue of a non-negative matrix equals its maximum row sum, confirming λ₁ = d exactly. The corresponding eigenvector 𝟏 reflects the graph's uniform degree structure."

- question: "The eigenvalues of the adjacency matrix can primarily tell us how many edges a graph has — they can rarely reveal global connectivity or structural properties."
  type: true-false
  answer: false
  explanation: "The spectrum encodes rich structural information far beyond edge count. The spectral gap determines expansion and connectivity; the multiplicity of eigenvalue 0 is related to bipartiteness; and the smallest eigenvalues' eigenvectors reveal community structure, forming the mathematical basis of spectral clustering. A graph's edge count is captured by Tr(A²)/2 = |E|, but eigenvalues collectively reveal global topological properties that are invisible from individual matrix entries."

- question: "Why does the spectral gap — the difference between the two largest eigenvalues — determine how quickly a random walk on a graph converges to its stationary distribution?"
  type: short-answer
  answer: "A random walk is governed by the (normalized) adjacency matrix. Its powers converge to the stationary distribution at a rate determined by how quickly non-dominant eigenvector components decay. The dominant eigenvector (eigenvalue λ₁) represents the stationary distribution; the second eigenvector (eigenvalue λ₂) is the slowest-decaying deviation from stationarity. After each step, this deviation shrinks by a factor of λ₂/λ₁. A large spectral gap means λ₂/λ₁ is small — the deviation decays rapidly and the walk mixes quickly. A small spectral gap means slow decay and slow mixing."
  explanation: "This connection is the core of expander graph theory. Expanders are designed to have large spectral gaps with sparse graphs (few edges), ensuring rapid mixing despite low connectivity — which is why they appear in derandomization, error-correcting codes, and network design."
```

## Explainer

The **adjacency matrix** A of a graph with n vertices is an n × n matrix where entry Aᵢⱼ = 1 if there is an edge between vertex i and vertex j, and 0 otherwise. For an undirected graph, A is symmetric — Aᵢⱼ = Aⱼᵢ. This encoding is not just a bookkeeping device; multiplying A by itself reveals structure invisible to the eye. The entry (A²)ᵢⱼ counts the number of walks of length 2 from vertex i to vertex j, because you sum over all possible intermediate vertices k the product Aᵢₖ · Aₖⱼ. More generally, (Aᵏ)ᵢⱼ counts walks of length k between i and j. Graph connectivity questions become matrix power questions.

Because A is a real symmetric matrix, your prerequisite on eigenvalues guarantees it has n real eigenvalues and n orthogonal eigenvectors. The eigenvalues of A, sorted as λ₁ ≥ λ₂ ≥ … ≥ λₙ, are called the **spectrum** of the graph. The largest eigenvalue λ₁ (the **spectral radius**) is tightly connected to the graph's edge density: for a d-regular graph (every vertex has degree d), λ₁ = d exactly, and the eigenvector corresponding to λ₁ is the all-ones vector. The remaining eigenvalues measure how much the graph deviates from this uniform structure.

The **spectral gap** — the difference λ₁ − λ₂ — is one of the most important quantities in spectral graph theory. A large spectral gap means the graph is a good **expander**: information, random walks, or network traffic spreads quickly and does not get trapped in clusters. Expander graphs are used in error-correcting codes, derandomization, and network design precisely because their spectral gap guarantees rapid mixing. Conversely, a small spectral gap indicates that the graph is nearly disconnected — it can be cut into large pieces with few crossing edges. The **Cheeger inequality** makes this intuition precise by bounding the edge expansion ratio above and below by functions of the spectral gap.

Spectral methods also detect clustering and community structure. The eigenvectors corresponding to the smallest eigenvalues tend to assign similar values to vertices in the same community and different values to vertices in different communities — this is the mathematical basis for **spectral clustering**, a technique widely used in data science and machine learning. The adjacency matrix bridge between graph combinatorics and linear algebra is one of the most productive in all of mathematics: discrete, combinatorial structure becomes continuous geometry in eigenspace, and techniques from one world illuminate the other.
