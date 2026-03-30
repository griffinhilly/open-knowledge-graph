---
id: spectral-graph-algorithms
title: Spectral Graph Algorithms
domain: computer-science
course: advanced-algorithms
prerequisites:
- id: expander-graphs
  type: hard
- id: breadth-first-search
  type: hard
- id: minimum-spanning-trees-kruskal-prim
  type: soft
tags:
- spectral-graph-theory
- graph-laplacian
- cheeger-inequality
- spectral-clustering
stage: expert
status: validated
---

# Spectral Graph Algorithms

## Core Idea
Spectral graph algorithms use eigenvalues and eigenvectors of graph-associated matrices (adjacency matrix, Laplacian) to solve graph problems. The graph Laplacian L = D - A (degree matrix minus adjacency matrix) has eigenvalues 0 = lambda_1 <= lambda_2 <= ... <= lambda_n, where the multiplicity of zero equals the number of connected components and lambda_2 (the algebraic connectivity or Fiedler value) measures how well-connected the graph is. The Fiedler vector (eigenvector for lambda_2) provides a spectral bisection that approximates the minimum ratio cut within a Cheeger-inequality factor of sqrt(lambda_2). Spectral methods yield near-linear time algorithms for graph partitioning, Laplacian system solving (Spielman-Teng), and effective resistance computation, with applications in machine learning (spectral clustering), network analysis, and scientific computing.

## Questions

```yaml
- question: "The Cheeger inequality relates the spectral gap lambda_2 of the normalized graph Laplacian to the edge expansion h(G): lambda_2/2 <= h(G) <= sqrt(2 * lambda_2). Why is the Fiedler vector (eigenvector for lambda_2) useful for graph partitioning?"
  type: multiple-choice
  options:
    - "The Fiedler vector assigns each vertex a real value, and thresholding these values at zero gives a bisection whose expansion is at most sqrt(2 * lambda_2) — within a square-root factor of optimal by the Cheeger inequality"
    - "The Fiedler vector directly encodes the optimal partition"
    - "The Fiedler vector minimizes the number of edges in the graph"
    - "The Fiedler vector is only useful for planar graphs"
  answer: 0
  explanation: "The Fiedler vector v solves min_{v perp 1} (v^T L v)/(v^T v) = lambda_2, where v^T L v = sum_{(i,j) in E} (v_i - v_j)^2 measures how much v varies across edges. Vertices with similar v-values are well-connected; vertices with different values have few edges between them. A sweep cut — sorting vertices by Fiedler value and trying all threshold cuts — finds a cut with expansion at most sqrt(2*lambda_2). Since lambda_2/2 <= h(G), this is within a sqrt(2/lambda_2) factor of the true optimum when lambda_2 is not too small. This spectral relaxation → rounding paradigm mirrors LP relaxation → rounding for combinatorial optimization."

- question: "The number of zero eigenvalues of the graph Laplacian L equals the number of connected components of the graph."
  type: true-false
  answer: true
  explanation: "The Laplacian L = D - A is positive semidefinite with smallest eigenvalue 0. The null space of L is spanned by indicator vectors of the connected components: if x is constant on each component, then x^T L x = sum_{(i,j)} (x_i - x_j)^2 = 0 (all edges connect vertices with the same x-value). Conversely, if x^T L x = 0, then x_i = x_j for all edges (i,j), so x is constant on each component. The dimension of the null space — the multiplicity of eigenvalue 0 — equals the number of connected components. This is the most basic spectral graph fact and motivates all further spectral analysis."

- question: "Explain how Spielman-Teng's near-linear time Laplacian solver works at a high level and why solving Laplacian systems is so broadly useful."
  type: short-answer
  answer: "Spielman-Teng solve Lx = b (where L is a graph Laplacian) in O(m * log^c(n)) time using a hierarchy of graph sparsifiers: each level replaces the graph with a sparser graph (fewer edges) that preserves the Laplacian's spectral properties within (1+epsilon). The solver uses this hierarchy as a preconditioner for an iterative method (preconditioned Chebyshev or conjugate gradient). Each level reduces the problem size, and the hierarchy has O(log n) levels, giving near-linear total work. Laplacian systems arise everywhere: in electrical network analysis (computing effective resistances and current flows), in maximum flow (interior point methods reduce to Laplacian solves), in graph partitioning (computing the Fiedler vector), in machine learning (semi-supervised learning via label propagation), and in scientific computing (finite element methods on meshes)."
  explanation: "The key breakthrough was showing that graph sparsification — replacing a graph with a spectrally similar graph having O(n log n) edges — preserves the solution quality. Batson-Spielman-Srivastava (2012) proved that twice-Ramanujan sparsifiers exist with O(n/epsilon^2) edges, enabling even stronger reductions."

- question: "Spectral clustering uses the top-k eigenvectors of the graph Laplacian to embed vertices in R^k, then applies k-means clustering in this embedding space. This approach has no theoretical guarantees."
  type: true-false
  answer: false
  explanation: "Spectral clustering has strong theoretical guarantees under planted partition models and stochastic block models. If the graph has k well-separated clusters with inter-cluster edge density much lower than intra-cluster density, the top-k eigenvectors approximately recover the cluster indicator vectors, and k-means in the spectral embedding correctly identifies the clusters with high probability. The guarantees are quantified by the eigengap (lambda_k - lambda_{k+1}): a large gap indicates well-separated clusters. Davis-Kahan perturbation theory bounds how much the empirical eigenvectors deviate from the ideal cluster indicators. These results make spectral clustering one of the best-understood clustering algorithms."
```

## Explainer

Every graph has a matrix representation, and the eigenvalues of that matrix encode global structural properties. The graph Laplacian L = D - A is the most important such matrix. Its eigenvalues are all nonnegative (L is positive semidefinite), and the pattern of small eigenvalues reveals the graph's large-scale connectivity structure. Zero eigenvalues correspond to connected components; near-zero eigenvalues indicate bottlenecks (subsets connected by few edges relative to their size).

The Cheeger inequality makes this correspondence quantitative. It relates the second-smallest Laplacian eigenvalue lambda_2 to the edge expansion h(G) — the minimum ratio of cut edges to subset size. Specifically, lambda_2/2 <= h(G) <= sqrt(2*lambda_2). This means spectral methods cannot find the exact minimum cut (the lower bound has a square root), but they provide a useful relaxation that is computable in polynomial time. The Fiedler vector — the eigenvector for lambda_2 — assigns each vertex a real number reflecting its "position" in the graph's connectivity structure, and sweep cuts based on this vector find near-optimal partitions.

Spectral methods extend naturally to multiple clusters via k-way partitioning. The first k eigenvectors of the Laplacian embed each vertex in R^k, where vertices in the same cluster are mapped close together and vertices in different clusters are mapped far apart. Running k-means in this embedding gives spectral clustering, which is both practical (widely used in machine learning and network analysis) and theoretically grounded (provable recovery under stochastic block models). The eigengap lambda_k - lambda_{k+1} predicts how cleanly the clusters separate in the spectral embedding.

The computational frontier is Laplacian system solving. The Spielman-Teng breakthrough showed that Lx = b can be solved in nearly linear time using a multilevel preconditioner built from graph sparsifiers. This has cascading algorithmic consequences: maximum flow algorithms based on interior point methods reduce each iteration to a Laplacian solve, yielding near-linear time max-flow algorithms (Kelner et al., 2014). Effective resistances, random spanning tree generation, and graph sparsification itself all reduce to Laplacian solving. The near-linear time Laplacian solver is becoming the universal subroutine for graph algorithms, much as FFT is for signal processing.
