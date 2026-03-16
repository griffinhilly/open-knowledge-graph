---
id: fixed-parameter-tractability
title: Fixed-Parameter Tractability (FPT)
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: np-completeness-formal
  type: hard
- id: vertex-cover-problem
  type: soft
tags:
- parameterized-complexity
- tractable-hardness
- algorithms
stage: advanced
status: draft
---

# Fixed-Parameter Tractability (FPT)

## Core Idea
Fixed-parameter tractability asks: while a problem is NP-hard in general, can it be solved in time f(k)·n^O(1) where k is a problem parameter (like solution size) and f is an arbitrary computable function? A problem is FPT if such algorithms exist. For instance, vertex cover is FPT parameterized by cover size k, though NP-complete in general. FPT provides a refined complexity landscape beyond classical NP-hardness.

## Explainer

From NP-completeness theory, you know that many important problems are NP-hard: no polynomial-time algorithm is known, and finding one would imply P = NP. But NP-hardness is a worst-case statement that treats all inputs as equally difficult. In practice, inputs to hard problems often have **structure** — a small solution size, sparse graphs, bounded tree-width — and exploiting that structure can make the problem tractable. Fixed-parameter tractability formalizes this observation.

The key idea is to identify a **parameter** k that captures the "hard part" of the input, then analyze complexity in terms of both n (input size) and k. A problem is **FPT** (fixed-parameter tractable) with respect to k if it can be solved in time f(k) · n^c, where f is any computable function (possibly exponential or worse in k) and c is a constant. The crucial point: for any *fixed* value of k, the running time is polynomial in n. When k is small, f(k) is just a constant multiplier, and the algorithm runs efficiently even on large inputs.

The **vertex cover** problem illustrates this perfectly. The problem asks: given a graph G and an integer k, does G have a vertex cover of size at most k? (A vertex cover is a set S of vertices such that every edge has at least one endpoint in S.) The brute-force approach checks all k-subsets of vertices, costing O(n^k) — polynomial for fixed k, but the degree grows with k, which isn't FPT. The FPT algorithm uses a different insight: pick any uncovered edge (u,v); a valid cover must include u or v (or both). Branch into two subproblems — include u, or include v — and recurse with k decremented. The search tree has depth k and branching factor 2, so at most 2^k leaf nodes, each checkable in polynomial time. Total cost: O(2^k · n). This is f(k) · n^1, which is FPT.

The function f(k) can be wild — 2^(2^k), k!, anything computable — and the problem is still FPT. The point is that when your actual inputs have k ≤ 20 or k ≤ 50, even an exponential-in-k factor is manageable. This makes FPT algorithms genuinely useful for real instances of NP-hard problems, provided the right parameter is small. Not every parameterization works: **W[1]-hard** problems (the parameterized analog of NP-hard) are unlikely to be FPT under the standard parameterization, forming a separate hardness class. The existence of a rich hierarchy (W[1], W[2], ...) shows that parameterized complexity theory, like classical complexity, has deep structure beyond a simple FPT/non-FPT divide.

The conceptual shift from classical to parameterized complexity is a shift from binary classification (tractable vs. intractable) to a **refined landscape**: the same problem can be FPT under one parameterization and W[1]-hard under another. Vertex cover parameterized by solution size is FPT; parameterized by the number of vertices in the complement, it's W[1]-hard. Choosing the right parameter to expose tractability is both the art and the science of the field.

