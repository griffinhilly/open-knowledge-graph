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

## Explainer

You already know that the halting problem is undecidable — no Turing machine can correctly decide for every input whether a given machine halts. That single result is powerful, but its real leverage comes from **reductions**, a technique that lets you transfer undecidability from HALT_TM to an unlimited number of other problems. The core idea is surprisingly simple: if you could solve problem B, and you can show that solving B would also let you solve HALT_TM, then B must be undecidable too — because we already know HALT_TM cannot be solved.

A **many-one reduction** (or mapping reduction) from language A to language B is a computable function f that transforms every instance of A into an instance of B, preserving membership: x ∈ A if and only if f(x) ∈ B. Think of f as a compiler that translates A-questions into B-questions without losing or distorting the answer. If such an f exists, we write A ≤ₘ B, read "A reduces to B." The subscript m stands for "many-one" — many inputs to A may map to the same element of B. The critical consequence: if A is undecidable and A ≤ₘ B, then B is undecidable. A decider for B would, composed with f, yield a decider for A — a contradiction.

The direction of reduction is the single most common source of confusion. To prove that a new language B is undecidable, you reduce the **known-hard** problem **to** B, not B to the known-hard problem. The intuition: you are showing that B is *at least as hard* as the known-hard problem. Reducing B to HALT_TM would only show that B is no harder than HALT_TM — which tells you nothing, since HALT_TM is already very hard. The arrow points from the problem you understand toward the problem you are investigating: HALT_TM ≤ₘ B means "if I could decide B, I could decide HALT_TM."

In practice, undecidability proofs follow a template. You want to show that some language B (say, E_TM = {⟨M⟩ : L(M) = ∅}) is undecidable. You construct a computable function f that takes an input ⟨M, w⟩ for HALT_TM and produces a machine description ⟨M'⟩ such that M halts on w if and only if L(M') is nonempty (i.e., ⟨M'⟩ ∉ E_TM). The machine M' is typically built by hardcoding w into M's behavior: M' ignores its own input, runs M on w, and accepts if M halts. Designing this f is the creative step — the rest is mechanical. Once you have one chain (HALT_TM → E_TM → EQ_TM → ...), each new proof gets easier because you can reduce from whichever earlier problem is most convenient, not just from HALT_TM directly.
