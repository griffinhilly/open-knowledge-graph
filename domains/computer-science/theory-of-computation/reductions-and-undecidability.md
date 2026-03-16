---
id: reductions-and-undecidability
title: Reductions and Proving Undecidability
domain: computer-science
course: theory-of-computation
prerequisites:
- id: undecidable-problems
  type: hard
builds-toward:
- rice-theorem
tags:
- reductions
- undecidability
- proof-technique
stage: abstract-reasoning
status: draft
---

# Reductions and Proving Undecidability

## Core Idea
A many-to-one reduction from language A to language B shows that if B is decidable, then A is decidable. Contrapositive: if A is undecidable, then B is undecidable. Reductions allow proving undecidability of new problems without reconstructing diagonalization proofs.

## Explainer

From your study of undecidable problems, you know that the halting problem (A_TM) cannot be decided by any Turing machine — the diagonalization proof established this directly. But there are infinitely many other undecidable problems, and you would not want to construct a fresh diagonalization argument for each one. **Reductions** provide a systematic way to transfer undecidability from a known undecidable problem to a new one, acting as a kind of proof-by-comparison.

A **many-to-one reduction** from language A to language B is a computable function f such that for every input w, w ∈ A if and only if f(w) ∈ B. Think of f as a translator: it converts instances of problem A into instances of problem B in a way that preserves yes/no answers. If such a reduction exists and B is decidable (has a Turing machine that always halts with the correct answer), then A is also decidable — you can decide A by first applying f, then running B's decider on the result. The contrapositive is the powerful direction: if A is *undecidable* and reduces to B, then B must also be undecidable. If B were decidable, A would be too, contradicting what we know.

The standard workflow is: take a problem B that you suspect is undecidable, then construct a computable function that maps instances of A_TM (the halting problem) into instances of B. For example, to show that the problem "does Turing machine M accept the empty string?" is undecidable, you build a reduction that takes a pair ⟨M, w⟩ and constructs a new machine M' that ignores its own input and instead simulates M on w. Now M' accepts the empty string if and only if M accepts w, so deciding the empty-string problem would let you decide the halting problem — a contradiction. The art of reduction proofs lies in designing this intermediate machine that bridges the two problems.

Reductions do more than prove individual undecidability results — they organize the landscape of unsolvable problems into a hierarchy of relative difficulty. If A reduces to B, then B is "at least as hard" as A. This framework extends throughout complexity theory: the same reduction concept, with tighter constraints on the function f (polynomial-time computable, log-space computable), underpins the theories of NP-completeness and space complexity that you will encounter later. Mastering reductions here gives you a proof technique that scales across the entire field.
