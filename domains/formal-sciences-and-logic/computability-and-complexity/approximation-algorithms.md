---
id: approximation-algorithms
title: Approximation Algorithms
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: np-completeness-formal
  type: hard
tags:
- complexity
- approximation
- optimization
- intractability
stage: formal-systems
status: draft
---

# Approximation Algorithms

## Core Idea
Approximation algorithms provide provably near-optimal solutions to NP-hard optimization problems in polynomial time, measured by their approximation ratio — the worst-case ratio between the algorithm's solution and the true optimum. The class APX contains problems with constant-factor approximations, PTAS (Polynomial-Time Approximation Scheme) allows (1+epsilon)-approximation for any epsilon > 0, and FPTAS further requires time polynomial in both input size and 1/epsilon. Inapproximability results, often proved via the PCP theorem and gap-preserving reductions, show that for some problems (like MAX-3SAT or chromatic number), no polynomial-time algorithm can achieve better than a specific ratio unless P = NP.

## How It's Best Learned
Study the 2-approximation for vertex cover (take both endpoints of a maximal matching) and the greedy O(log n)-approximation for set cover as clean introductory examples. Then learn the PTAS for Euclidean TSP and the FPTAS for knapsack to see the full spectrum. Finally, encounter the PCP theorem's implication that MAX-3SAT has no PTAS, which reveals hard limits on approximability.

## Common Misconceptions
- An approximation ratio of 2 does not mean the answer is "twice as bad" in practice — it is a worst-case guarantee, and real performance is often much better.
- Not all NP-hard problems are equally hard to approximate — some admit FPTAS while others cannot be approximated within any constant factor unless P = NP.
