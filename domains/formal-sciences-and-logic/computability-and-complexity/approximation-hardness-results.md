---
id: approximation-hardness-results
title: Approximation Algorithms and Hardness of Approximation
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: approximation-algorithms
  type: hard
- id: np-completeness-formal
  type: hard
builds-toward:
- parameterized-complexity-fundamentals
tags:
- approximation
- hardness
- inapproximability
stage: advanced
status: draft
---

# Approximation Algorithms and Hardness of Approximation

## Core Idea
For NP-hard optimization problems, approximation algorithms find near-optimal solutions efficiently. Hardness of approximation results (assuming P ≠ NP) establish how close to optimal approximation is possible. For instance, unless P = NP, no polynomial-time c-approximation exists for some problems at certain thresholds, creating a landscape of computational difficulty ranging from exact to barely-approximable.

## Explainer

You already know from NP-completeness that problems like Traveling Salesman and Vertex Cover likely have no polynomial-time exact algorithms. But NP-hardness doesn't end the story—it motivates a new question: if we can't solve these problems exactly, how close can we get? An **approximation algorithm** returns a solution whose objective value is within a **ratio** ρ of optimal (ρ ≥ 1 for minimization, ρ ≤ 1 for maximization). Your earlier study of approximation algorithms gave you examples: the 2-approximation for Vertex Cover, the (1 - 1/e)-approximation for Set Cover. Hardness of approximation asks: can we do better, or is even a good approximation NP-hard?

The key tool is the **PCP Theorem** (Probabilistically Checkable Proofs), which fundamentally reframes NP. Every NP language has proofs that can be verified by reading only a constant number of random bits, yet still detecting errors with constant probability. This probabilistic characterization implies surprising inapproximability: for Max-3SAT, no polynomial-time algorithm can exceed a 7/8-approximation unless P = NP—and a simple random assignment already achieves exactly 7/8. This is a *tight* result: the algorithm is provably optimal up to the NP conjecture.

Different NP-hard optimization problems inhabit different regions of the approximability landscape. Some admit a **PTAS** (polynomial-time approximation scheme)—for any fixed ε > 0, a (1+ε)-approximation runs in polynomial time; Euclidean TSP is an example. Others allow constant-factor approximations but no PTAS—general Metric TSP has a classical 1.5-approximation (Christofides) but no PTAS under standard assumptions. Still others resist any constant-factor approximation: the clique problem cannot be approximated within n^{1-ε} in polynomial time unless P = NP. This mirrors the hierarchy of NP-hardness but with finer resolution.

**Gap-introducing reductions** are the technical engine. Rather than reducing exact decision problems (as in standard NP-completeness), you reduce to problems with a large *gap* between YES instances and NO instances, showing that distinguishing "optimal ≤ α·OPT" from "optimal ≥ β·OPT" is itself NP-hard. This framework extends the reductions you learned for NP-completeness into a richer setting: instead of asking "is an exact solution computable in polynomial time?", you ask "within what precision can the optimal value be estimated efficiently?" The inapproximability results that emerge are conditional theorems—they hold assuming P ≠ NP—but they are among the sharpest statements complexity theory can make about the inherent cost of optimization.
