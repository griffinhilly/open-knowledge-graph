---
id: hardness-approximation
title: Hardness of Approximation Introduction
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: approximation-algorithms
  type: hard
- id: three-sat-reductions
  type: hard
tags:
- approximation-hardness
- inapproximability
- reductions
- lower-bounds
stage: advanced
status: draft
---

# Hardness of Approximation Introduction

## Core Idea
Even when a problem is NP-hard, we sometimes compute approximate solutions rather than exact ones. Hardness of approximation results show that some NP-hard problems are also hard to approximate: there exist constants c > 1 such that achieving a c-approximation is NP-hard. These results reveal fundamental limits to what approximation algorithms can achieve.

## How It's Best Learned
Study the PCP (Probabilistically Checkable Proofs) theorem at an intuitive level. Work through one inapproximability result, like the maximal independent set hardness.

## Explainer

From your study of approximation algorithms, you know the standard framework: since many optimization problems are NP-hard to solve exactly, we settle for algorithms that return solutions within a provable factor of optimal. A **ρ-approximation algorithm** guarantees an answer no worse than ρ times the optimal value. For some problems this works beautifully — the greedy algorithm gives a 2-approximation for vertex cover, and more sophisticated methods give (1 + ε)-approximations for many scheduling and packing problems. The natural question is: how far does this go? Can every NP-hard optimization problem be approximated to within any fixed ratio?

The answer is no, and **hardness of approximation** results make this precise. These results show that for certain NP-hard problems, even achieving a ρ-approximation is NP-hard — meaning no polynomial-time algorithm can guarantee that ratio unless P = NP. The key tool is the **PCP theorem** (Probabilistically Checkable Proofs), which provides a reformulation of NP: every NP language has a proof system where a verifier can check a proof by reading only a *constant* number of bits, with the guarantee that valid proofs are always accepted and invalid proofs are rejected with probability at least 1/2. This may seem unrelated to approximation, but the connection is powerful.

The PCP theorem implies inapproximability via **gap amplification**: if you could approximate MAX-3SAT to within a ratio better than some constant c < 1, you could distinguish satisfiable instances from highly unsatisfiable ones — which the PCP theorem shows is NP-hard. Concretely, there is a constant ε > 0 such that no polynomial-time algorithm achieves a (1 − ε)-approximation for MAX-3SAT unless P = NP. From this "base" inapproximability, reductions from your prerequisite work propagate hardness to other problems. The MAX-CLIQUE problem is especially striking: it cannot be approximated within a factor of n^(1−ε) for any ε > 0 unless P = NP — so the approximability gap is polynomial, not just a small constant.

The conceptual shift from NP-hardness reductions to inapproximability reductions is worth emphasizing. An ordinary reduction from 3-SAT to a problem X shows that exact optimization is hard. A *gap-preserving* reduction preserves a gap in the objective value between YES and NO instances — it shows that even finding a solution in the gap is hard. Constructing such reductions requires careful attention to how the transformation affects objective values, not just feasibility. This is why inapproximability proofs tend to be more intricate than their exact-hardness counterparts, and why the PCP theorem — which creates the initial gap "for free" — is such a powerful foundation for the whole theory.
