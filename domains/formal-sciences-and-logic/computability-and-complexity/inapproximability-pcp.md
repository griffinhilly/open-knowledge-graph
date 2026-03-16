---
id: inapproximability-pcp
title: Inapproximability and the PCP Theorem
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: approximation-algorithms
  type: hard
- id: np-completeness-formal
  type: hard
tags:
- approximation
- hardness
- pcp
stage: advanced
status: draft
---

# Inapproximability and the PCP Theorem

## Core Idea
The PCP (Probabilistically Checkable Proofs) theorem equates NP with a class of languages having efficiently verifiable proofs checkable by reading only a constant number of random bits. This has powerful consequences: unless P=NP, many optimization problems admit no polynomial-time approximation schemes, establishing tight inapproximability bounds for TSP, set cover, and other classic problems.

## Explainer

From your study of approximation algorithms, you know that when a problem is NP-hard, practitioners often settle for a solution guaranteed to be within a factor of the optimum. A natural question arises: how good can this guarantee get? Can we always get within 1.01× of optimal if we allow polynomial time? The answer, for many problems, is definitively no — and the reason is the PCP theorem.

**PCP** stands for **Probabilistically Checkable Proof**. Classically, an NP proof is a certificate you read in full to verify correctness. A PCP proof is a redundantly encoded proof where a randomized verifier can check validity by reading only a *constant* number of bits — say, 3 — chosen using a logarithmic number of random coins. Despite reading almost nothing, the verifier catches any fake proof with constant probability (say, at least ½). The PCP theorem says NP equals exactly the class of languages with such proofs: **NP = PCP(log n, O(1))**. This is one of the most surprising equalities in complexity theory.

The bridge to inapproximability runs through a problem called **Max-3SAT**: given a 3-CNF formula, find an assignment satisfying the maximum number of clauses. The reduction from NP problems to Max-3SAT, combined with PCP, shows that if you could distinguish "all clauses satisfiable" from "at most 7/8 + ε satisfiable" in polynomial time, you could solve NP in polynomial time. This establishes a **hardness-of-approximation threshold**: no polynomial-time algorithm can do better than roughly 7/8 of optimal for Max-3SAT unless P=NP.

From this anchor, a web of reductions creates inapproximability results for dozens of problems. **Set cover** admits no (1 − ε) ln n approximation for any ε > 0 unless P=NP. **Vertex cover** has a threshold near 1.36. **TSP with triangle inequality** can be approximated to 3/2 (Christofides), but without the triangle inequality, no constant factor is possible unless P=NP. Each such result is proven by a gap-preserving reduction: a polynomial-time transformation that converts a hard Max-3SAT instance into an optimization instance while maintaining the gap between "good" and "not good."

The key conceptual shift PCP demands is this: approximation is not a way to escape hardness — it *is* hardness, measured at a finer scale. The question is no longer "can we solve this?" but "at what approximation ratio does the problem become tractable?" This transforms approximation algorithms from a practical workaround into a precise theoretical domain, with tight upper and lower bounds meeting at provable thresholds.
