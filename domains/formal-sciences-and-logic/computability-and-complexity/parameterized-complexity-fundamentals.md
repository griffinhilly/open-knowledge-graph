---
id: parameterized-complexity-fundamentals
title: Parameterized Complexity and Fixed-Parameter Tractability
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: np-completeness-formal
  type: hard
- id: polynomial-time-reductions
  type: soft
builds-toward:
- kolmogorov-complexity-properties
tags:
- parameterized-complexity
- FPT
- kernelization
stage: advanced
status: draft
---

# Parameterized Complexity and Fixed-Parameter Tractability

## Core Idea
Parameterized complexity treats problem instances as pairs (x, k) where k is a parameter (e.g., solution size). An NP-hard problem can be fixed-parameter tractable (FPT) if solvable in time f(k) · poly(|x|), making it practical for small parameters despite NP-hardness. This framework explains why many intractable problems become tractable on restricted inputs and guides algorithm design.

## Explainer

You already know that NP-completeness is a worst-case statement: no polynomial-time algorithm handles *all* instances. But NP-completeness hides enormous variation within a problem. Consider the Vertex Cover problem: given a graph G and integer k, does G have a vertex cover of size ≤ k? This is NP-complete. But in practice, the k you care about might be small — perhaps you're covering 10 vertices in a network of millions. Parameterized complexity formalizes this intuition by asking: can we solve the problem efficiently when k is small, even if the input n is huge?

A problem is **fixed-parameter tractable (FPT)** if there exists an algorithm running in time f(k) · poly(n), where f is any computable function of k alone (often something like 2^k or k!), and poly(n) is polynomial in the input size. The key insight is that the super-polynomial part depends only on k. If k = 10, even 2^k = 1024 is a small constant multiplied by a polynomial — the algorithm is practical. For Vertex Cover, a classical FPT algorithm runs in time O(2^k · n): at each step, pick an uncovered edge, branch on including one of its two endpoints, and recurse. The depth is at most k, giving 2^k leaves, and each path processes the graph in linear time.

**Kernelization** is a complementary technique: reduce any instance (x, k) to an equivalent smaller instance (x', k') where |x'| ≤ g(k) for some function g. This reduced instance is the **kernel**. For Vertex Cover, the classic kernel applies the crown rule and LP relaxation to reduce to a graph with at most 2k vertices — so you can solve any instance with k ≤ 50 by first kernelizing down to 100 vertices, then running any algorithm on that tiny instance. Kernelization is often the most practical tool because it shrinks the problem before any other computation begins.

The FPT class has an intractability analog: **W[1]**-hardness means (under standard assumptions) that no FPT algorithm exists, because the problem requires f(k) · n^g(k) time at best. The canonical W[1]-complete problem is k-Clique: find a clique of size k in a graph. This separates problems that are tractable-when-parameterized (FPT) from those that remain hard regardless of how small k is. The hierarchy FPT ⊆ W[1] ⊆ W[2] ⊆ ... mirrors the polynomial hierarchy in classical complexity. When you encounter an NP-hard problem, asking "what is a natural parameter, and is this problem FPT in that parameter?" is often the most practical path to an efficient algorithm.

