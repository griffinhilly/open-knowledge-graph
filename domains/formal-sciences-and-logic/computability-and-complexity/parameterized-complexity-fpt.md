---
id: parameterized-complexity-fpt
title: Parameterized Complexity and Fixed-Parameter Tractability
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: np-completeness-theorem
  type: hard
- id: approximation-algorithms
  type: soft
tags:
- parameterized-complexity
- fpt
- kernelization
- w-hierarchy
stage: advanced
status: draft
---

# Parameterized Complexity and Fixed-Parameter Tractability

## Core Idea
Parameterized complexity classifies problems not just by input size n but by a secondary parameter k. A problem is fixed-parameter tractable (FPT) if solvable in time f(k)·poly(n) for some function f. Many NP-hard problems (like vertex cover with parameter size k) are FPT, offering a refined view of tractability beyond P versus NP.

## Explainer

NP-completeness tells you a problem is hard in the worst case, but it says nothing about whether the hardness is spread uniformly across all instances or concentrated in a specific structural dimension. **Parameterized complexity** introduces a secondary measure — the **parameter k** — to make this distinction precise. Instead of asking "can we solve this in polynomial time overall?", we ask "can we solve this efficiently when k is small, even if n is large?" The key is that k might represent something structurally meaningful: solution size, tree-width, number of exceptions, or any other dimension that happens to be small in practice.

A problem is **fixed-parameter tractable (FPT)** if it can be solved in time f(k)·poly(n), where f is any computable function of k alone (perhaps doubly exponential) and the polynomial part depends only on n. The crucial feature is that the k-dependence is isolated: for any fixed k, the running time is polynomial in n. **Vertex cover** is the classic example. Finding a vertex cover of size k in a graph with n vertices is NP-hard when both n and k vary, but it is FPT with parameter k: a simple branching algorithm runs in time 2^k · n. For social networks where a small set of highly-connected nodes exists, k might be 10 while n is a million — and 2^10 · n is completely tractable.

The FPT property is achieved by two main techniques. **Branching algorithms** split the problem into at most f(k) subproblems, each with parameter k − 1, yielding a recursion tree of bounded depth and size f(k) with polynomial work per node. **Kernelization** is often more powerful: reduce the instance in polynomial time to an equivalent "kernel" whose size depends only on k, not n. For vertex cover, any vertex of degree > k must be included, so after including all such vertices and reducing k accordingly, the remaining graph has at most k² vertices. This compressed problem is then solved by any method. A polynomial kernel means the hard combinatorial work is bounded entirely by the parameter.

Not all parameterized problems are FPT. The **W-hierarchy** (W[1], W[2],…) classifies parameterized intractability by analogy with NP. W[1]-hard problems (like k-clique or k-independent-set) are believed not to be FPT — a W[1]-hardness result is the parameterized analog of NP-completeness. The key separation conjecture is FPT ≠ W[1], which is implied by (but not equivalent to) P ≠ NP. This gives a finer classification: vertex cover is FPT, but k-clique is W[1]-complete and unlikely to be FPT.

The practical upshot is a richer vocabulary for problem analysis. When you encounter an NP-hard problem, the NP-hardness result tells you what to avoid (polynomial-time exact algorithms with no extra structure). Parameterized complexity tells you what to look for: a natural small parameter that makes the problem tractable. This turns the question from "is the problem hard?" to "hard along which dimension?" — a much more actionable question for algorithm design.
