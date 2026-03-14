---
id: decidability-and-undecidability
title: Decidability and Undecidability
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: formal-arithmetic-and-expressibility
  type: hard
- id: cantor-diagonalization
  type: soft
builds-toward:
- godels-incompleteness-theorems
tags:
- decidability
- undecidability
- halting-problem-formal
- Church-Turing
- decision-procedure
stage: formal-systems
status: validated
---

# Decidability and Undecidability

## Core Idea
A theory is decidable if there is an algorithm that determines whether any given sentence is a theorem. Propositional logic is decidable (truth tables decide validity). First-order logic is semi-decidable — there is a procedure that halts on all valid sentences but may loop on invalid ones. The first-order theory of arithmetic (true arithmetic) is undecidable by Church's theorem, proved via reduction from the halting problem. Undecidability results are established using diagonalization arguments similar to Cantor's, demonstrating that no consistent recursive axiomatization can decide all arithmetic truths.

## How It's Best Learned
Study the decidability of propositional logic and contrast with the undecidability of FOL validity. Trace Church's reduction: show how a Turing machine computation can be expressed as an arithmetic sentence.

## Common Misconceptions
- Undecidable does not mean unprovable — many individual sentences in an undecidable theory are still provable.
- Semi-decidability (enumerability of theorems) is not the same as decidability.
