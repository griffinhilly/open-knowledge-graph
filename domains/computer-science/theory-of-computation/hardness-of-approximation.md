---
id: hardness-of-approximation
title: Hardness of Approximation
domain: computer-science
course: theory-of-computation
prerequisites:
- id: approximation-algorithms-design
  type: hard
- id: np-completeness
  type: hard
tags:
- hardness
- inapproximability
- lower-bounds
stage: advanced
status: draft
---

# Hardness of Approximation

## Core Idea
Hardness of approximation studies which optimization problems resist good approximations unless P=NP. Using the PCP (probabilistically checkable proofs) theorem, one proves problems cannot be approximated better than specific thresholds: vertex cover cannot be approximated better than 1.36, max clique not better than n^ε for any ε > 0. This shows approximation hardness is orthogonal to decision hardness—some NP-hard problems have arbitrary approximations, others have tight inapproximability barriers.

## Explainer

From your study of approximation algorithms, you know that when an NP-hard optimization problem can't be solved exactly in polynomial time, the next best thing is an efficient algorithm that gets *close* to optimal — say, within a factor of 2 or 1.5 of the best possible answer. And from NP-completeness, you know that certain problems are computationally intractable unless P = NP. Hardness of approximation asks the natural follow-up: for a given NP-hard problem, *how close* can a polynomial-time algorithm get? The answer, surprisingly, is that many problems have provable limits on how well they can be approximated.

The landscape of approximability is strikingly varied. Some NP-hard problems are easy to approximate: the **traveling salesman problem** with triangle inequality has a 1.5-approximation (Christofides' algorithm), meaning you can always find a tour within 50% of optimal. The **knapsack problem** has a fully polynomial-time approximation scheme (FPTAS) — you can get within any desired factor (1 + ε) of optimal. But other problems resist approximation stubbornly. **Maximum Clique** is so hard to approximate that no polynomial-time algorithm can find a clique within a factor of n^(1-ε) of the largest one, for any ε > 0, unless P = NP. That means even finding a clique that is, say, the square root of the optimal size is intractable. The decision version ("is there a clique of size k?") and the optimization version live in completely different approximability classes.

The key tool for proving these limits is the **PCP theorem** (Probabilistically Checkable Proofs). In its simplest form, the PCP theorem says that every NP proof can be reformulated so that a verifier needs to read only a constant number of randomly chosen bits to be convinced of its correctness, with high probability. This seemingly abstract statement has a stunning consequence: it transforms gap problems — distinguishing between instances where the optimal value is above one threshold versus below another — into NP-hard problems. If you can show that distinguishing "optimum ≥ k" from "optimum ≤ αk" is NP-hard, then no polynomial-time algorithm can achieve an approximation ratio better than α, unless P = NP. This is how inapproximability results for Max-3SAT, Vertex Cover, Set Cover, and many others are established.

The practical takeaway is a classification of NP-hard problems into tiers: those with constant-factor approximations, those with logarithmic-factor approximations, those with PTAS/FPTAS (arbitrarily good approximations), and those that are essentially inapproximable. Knowing which tier your problem falls into tells you what to expect from any algorithm and prevents wasted effort chasing an approximation guarantee that provably cannot exist. This classification is one of the most important contributions of computational complexity theory to practical algorithm design.
