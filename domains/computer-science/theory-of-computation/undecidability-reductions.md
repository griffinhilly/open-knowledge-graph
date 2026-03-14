---
id: undecidability-reductions
title: Reductions and Undecidability
domain: computer-science
course: theory-of-computation
prerequisites:
- id: halting-problem
  type: hard
- id: recognizability-vs-decidability
  type: soft
builds-toward:
- rice-theorem
- np-completeness
tags:
- reductions
- undecidability
- mapping-reduction
- computable
stage: advanced
status: validated
---
# Reductions and Undecidability

## Core Idea
A many-one (mapping) reduction from language A to language B is a computable function f such that x ∈ A ⟺ f(x) ∈ B, written A ≤ₘ B. If A ≤ₘ B and B is decidable, then A is decidable; contrapositively, if A is undecidable and A ≤ₘ B, then B is undecidable. Reductions are the primary tool for proving new languages undecidable: show that solving B would let you solve HALT_TM. The direction of reduction is critical and easily confused: to prove B undecidable, reduce the *known-undecidable* problem *to* B.

## How It's Best Learned
Prove a sequence of languages undecidable via chain reduction: HALT_TM → E_TM (is L(M) empty?) → EQ_TM (are two TMs equivalent?). Each step reinforces the direction convention. Sketch the computable f in prose first, then formalize.

## Common Misconceptions
- Reducing in the wrong direction: to prove B undecidable you must reduce A (known undecidable) TO B, not B to A.
- Confusing many-one reductions with Turing reductions (oracle reductions), which are more powerful but less commonly used for undecidability proofs at this level.
