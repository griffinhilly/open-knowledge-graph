---
id: parameterized-complexity
title: Parameterized Complexity
domain: computer-science
course: advanced-algorithms
prerequisites:
- id: np-completeness
  type: hard
- id: vertex-cover-clique-problems
  type: hard
- id: dynamic-programming-intro
  type: soft
tags:
- parameterized-complexity
- fpt
- treewidth
- kernelization
stage: expert
status: validated
---

# Parameterized Complexity

## Core Idea
Parameterized complexity refines the NP-hardness classification by asking: is a problem solvable in time f(k) * n^O(1), where k is a parameter of the input (not the input size)? Problems solvable in this form are Fixed-Parameter Tractable (FPT). Vertex cover parameterized by solution size k is FPT: solvable in O(2^k * n) time via bounded search trees. Treewidth is a structural parameter that measures how "tree-like" a graph is — many NP-hard problems (independent set, coloring, Hamiltonian cycle) become FPT when parameterized by treewidth, solvable in time f(tw) * n via dynamic programming on tree decompositions. Kernelization provides a complementary approach: reducing the instance to an equivalent instance of size bounded by g(k), independent of n. The W-hierarchy (W[1], W[2], ...) classifies parameterized problems believed not to be FPT, analogous to the polynomial hierarchy for classical complexity.

## Questions

```yaml
- question: "The vertex cover problem asks: does graph G have a vertex cover of size at most k? The bounded search tree algorithm solves this in O(2^k * n) time. Why is this fundamentally different from O(2^n) exhaustive search?"
  type: multiple-choice
  options:
    - "2^k * n is always less than 2^n"
    - "When k is small relative to n (e.g., k = 20 in a million-vertex graph), 2^k * n ≈ 10^6 * 10^6 = 10^12 is tractable, while 2^n is astronomical — the exponential blowup is confined to the parameter k, not the input size n"
    - "The bounded search tree algorithm uses polynomial space while exhaustive search uses exponential space"
    - "The bounded search tree algorithm always finds the optimal solution while exhaustive search may not"
  answer: 1
  explanation: "The key insight of FPT is that the exponential dependence is on the PARAMETER k, not the input size n. For vertex cover of a network with n = 10^6 vertices and k = 20, the FPT algorithm does about 10^6 * 2^20 ≈ 10^12 operations — feasible on modern hardware. Exhaustive search over all subsets of size 20 does C(10^6, 20) ≈ 10^99 operations — utterly infeasible. The FPT framework recognizes that many real-world instances have small parameter values, making the exponential dependence on k acceptable."

- question: "Every NP-hard problem parameterized by its solution size is Fixed-Parameter Tractable."
  type: true-false
  answer: false
  explanation: "This is the central negative result of parameterized complexity. The W-hierarchy classifies problems by their likely parameterized intractability. Clique parameterized by clique size k is W[1]-complete — believed not to be FPT. If k-Clique were FPT (solvable in f(k) * n^O(1) time), then every problem in W[1] would be FPT, which is believed false (analogous to P != NP for classical complexity). Other W[1]-hard problems include Independent Set (parameterized by solution size), k-Path, and k-Dominating Set. The distinction: vertex cover is FPT while clique and independent set are W[1]-hard, despite all being NP-hard."

- question: "Explain what treewidth measures and why it makes NP-hard problems tractable."
  type: short-answer
  answer: "Treewidth measures how close a graph is to being a tree. A tree decomposition maps a graph into a tree of 'bags,' where each bag contains a subset of vertices, every edge is contained in some bag, and for each vertex the bags containing it form a connected subtree. Treewidth is the maximum bag size minus 1. Trees have treewidth 1; complete graphs have treewidth n-1; planar graphs have treewidth O(sqrt(n)). NP-hard problems become tractable on bounded treewidth because dynamic programming on the tree decomposition processes the graph one bag at a time, with state space exponential only in the bag size (treewidth). For example, maximum independent set on graphs of treewidth w is solvable in O(2^w * n) time — the DP tracks which subset of each bag is in the independent set, and the tree structure ensures only O(w) vertices interact at each step."
  explanation: "Courcelle's theorem generalizes this: every graph property expressible in monadic second-order logic is decidable in f(w) * n time on graphs of treewidth w. This is a sweeping meta-theorem — it shows that treewidth captures a fundamental barrier to computational hardness for graph problems."

- question: "A kernelization algorithm for k-Vertex Cover produces an equivalent instance with at most 2k vertices. This kernel is known to be essentially optimal: no polynomial-time algorithm can produce a kernel with (2-epsilon)k vertices unless the polynomial hierarchy collapses."
  type: true-false
  answer: true
  explanation: "The classical Crown Reduction and Buss kernelization for vertex cover produce a kernel with at most 2k vertices and k^2 edges. This means a million-vertex graph with a minimum vertex cover of size 100 can be reduced to at most 200 vertices in polynomial time, after which any algorithm (even brute force) runs fast. The lower bound of (2-epsilon)k vertices (under complexity-theoretic assumptions) shows this is essentially tight. Kernelization lower bounds use the framework of cross-composition and are one of the major tools in parameterized complexity theory."
```

## Explainer

NP-hardness is a blunt instrument: it says that no polynomial-time algorithm solves all instances, but says nothing about which instances are hard. Parameterized complexity provides a finer lens. Instead of measuring complexity solely as a function of input size n, it measures complexity as f(k) * n^c, where k is a problem-specific parameter and f can be any computable function. If c is a constant (independent of k), the problem is Fixed-Parameter Tractable (FPT) — the combinatorial explosion is confined to the parameter, and for small k the algorithm is efficient.

Vertex cover is the poster child. The bounded search tree algorithm picks any edge (u,v), branches on whether u or v is in the cover (one must be), and recurses with k decremented. The recursion depth is k, branching factor is 2, and each step does O(n) work: total O(2^k * n). For k = 30 in a graph with a million vertices, this is about 10^15 — feasible with a fast computer. The same problem solved by brute-force enumeration of size-30 subsets would require C(10^6, 30) operations — a number with 160 digits. FPT algorithms exploit problem structure (here, the constraint that cover vertices must hit every edge) to confine the exponential search to the parameter.

Treewidth provides a structural approach to parameterized tractability. A tree decomposition breaks a graph into overlapping "bags" arranged in a tree structure, with the constraint that each edge appears in some bag and each vertex's bags form a connected subtree. The treewidth — maximum bag size minus 1 — measures the graph's departure from tree-likeness. On trees (treewidth 1), many problems are solvable by straightforward DP. On graphs of bounded treewidth w, the same DP works but with state space exponential in w instead of n. Courcelle's meta-theorem makes this precise: any property definable in monadic second-order logic is decidable in f(w) * n time on graphs of treewidth w.

Kernelization complements FPT algorithms by reducing instances to equivalent smaller ones. A kernelization algorithm runs in polynomial time and produces an instance with size bounded by g(k) — independent of n — that has a solution if and only if the original does. For vertex cover, kernelization reduces to at most 2k vertices. This is powerful in practice: a huge graph with a small vertex cover parameter can be reduced to a tiny equivalent instance. The theory of kernelization lower bounds, using cross-composition and polynomial parameter transformations, proves that certain problems cannot have small kernels under complexity assumptions, providing a fine-grained map of which problems compress and which do not.
