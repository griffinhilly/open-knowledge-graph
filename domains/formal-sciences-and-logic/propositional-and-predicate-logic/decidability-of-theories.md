---
id: decidability-of-theories
title: Decidability of Theories
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: decidability-and-undecidability
  type: hard
- id: formal-arithmetic-and-expressibility
  type: hard
builds-toward:
- godels-incompleteness-theorems
tags:
- decidable-theories
- monadic-logic
- Presburger-arithmetic
- decision-procedures
- undecidable-theories
stage: formal-systems
status: draft
---

# Decidability of Theories

## Core Idea
A first-order theory is decidable if there exists an algorithm that, given any sentence in the theory's language, determines whether the theory entails it. Some fragments of first-order logic are decidable: monadic predicate logic (only unary predicates, no functions), Presburger arithmetic (natural numbers with addition but no multiplication), and the theory of real closed fields (Tarski's quantifier elimination). However, full first-order arithmetic (with both addition and multiplication) is undecidable, as shown by Church and Turing. Understanding which theories are decidable and which are not reveals the boundary between mechanizable and non-mechanizable reasoning.

## How It's Best Learned
Compare Presburger arithmetic (decidable) with Peano arithmetic (undecidable) to see how adding multiplication crosses the decidability boundary. Work through a simple quantifier-elimination example in Presburger arithmetic to see a decision procedure in action.

## Common Misconceptions
- Undecidability of a theory does not mean no sentences can be proved — it means no single algorithm can decide all sentences. Many individual theorems are easily provable.
- Decidability of a fragment does not extend to the full theory — monadic logic is decidable, but adding a single binary predicate makes it undecidable.
- Quantifier elimination is a powerful technique but applies only to specific theories — it is not a general method for first-order logic.
