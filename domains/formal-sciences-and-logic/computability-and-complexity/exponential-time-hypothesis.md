---
id: exponential-time-hypothesis
title: Exponential Time Hypothesis (ETH)
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: np-completeness-formal
  type: hard
- id: time-complexity-classes-formal
  type: soft
tags:
- conjecture
- lower-bounds
- hardness
stage: advanced
status: draft
---

# Exponential Time Hypothesis (ETH)

## Core Idea
The Exponential Time Hypothesis (ETH) conjectures that 3-SAT requires time 2^(c·n) for some constant c > 0, implying SAT cannot be solved in 2^(o(n)) time. ETH is a refined hardness assumption stronger than P ≠ NP but potentially weaker than assuming exponential lower bounds hold universally. It has become influential for proving conditional lower bounds: many problems' hardness is established assuming ETH holds.

## Explainer

The Exponential Time Hypothesis sits at the boundary between what we believe and what we can prove about computational hardness. You already know from NP-completeness that 3-SAT is among the hardest problems in NP — but knowing a problem is NP-complete only tells you no polynomial-time algorithm exists (assuming P ≠ NP). ETH makes a sharper claim: 3-SAT doesn't just require superpolynomial time, it requires genuinely exponential time, at minimum 2^(cn) for some constant c > 0, where n is the number of variables.

To appreciate why this matters, consider what "no 2^(o(n)) algorithm" rules out concretely. It says no algorithm can solve 3-SAT in, say, 2^(√n) time or 2^(n/log n) time — both of which are vastly faster than 2^n but still not polynomial. Such **subexponential** algorithms, while impractical for large n, would represent genuine structural breakthroughs. ETH says they don't exist. This is why ETH is called a "refined" hardness assumption: it is strictly stronger than P ≠ NP (which says nothing about the exponent) but potentially weaker than claiming all exponential hardness results we care about hold simultaneously.

The real power of ETH emerges in **conditional lower bounds** — proofs of the form "if ETH holds, then problem X cannot be solved faster than T(n)." For example, under ETH, k-Clique cannot be solved in time f(k) · n^(o(k)), and many parameterized problems have tight running-time bounds. This lets researchers prove *optimality*: not just "we don't know a faster algorithm" but "no faster algorithm exists unless ETH fails." This transforms complexity theory from a study of hardness classes into a study of precise running times, and makes ETH central to the field of **fine-grained complexity**.

The **Sparsification Lemma** is the key technical tool for applying ETH: it shows that, without loss of generality when analyzing ETH lower bounds, 3-SAT instances can be assumed to have O(n) clauses rather than O(n^3). This means the hardest 3-SAT instances are *sparse* — a counterintuitive but important fact. Together with reductions that preserve instance size tightly (unlike classical polynomial reductions, which may blow up sizes), ETH lets researchers pin down the exact exponent of the best algorithm for each problem. The goal is no longer merely "polynomial or exponential?" but "2^n or 2^(n/2) or n^k for which k?" — a far more precise account of algorithmic difficulty.
