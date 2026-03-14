---
id: formal-arithmetic-and-expressibility
title: Formal Arithmetic and Expressibility
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: first-order-logic-syntax
  type: hard
- id: mathematical-induction
  type: soft
builds-toward:
- godels-incompleteness-theorems
- decidability-and-undecidability
tags:
- Peano-arithmetic
- formal-arithmetic
- representability
- primitive-recursion
stage: formal-systems
status: validated
---

# Formal Arithmetic and Expressibility

## Core Idea
Peano Arithmetic (PA) is a first-order theory with axioms for zero, successor, addition, and multiplication, plus an induction schema. PA is powerful enough to express and prove a vast range of arithmetic truths. A key concept is representability: a function f is representable in PA if there is a formula φ(x, y) such that PA proves φ(n, f(n)) for each numeral n and PA proves ∀y(φ(n, y) → y = f(n)). Gödel showed that all primitive recursive functions are representable in PA, which is the technical foundation for encoding proofs as numbers (Gödel numbering).

## How It's Best Learned
Write out the Peano axioms explicitly and verify small arithmetic facts from them. Trace Gödel numbering on a simple formula to see how syntax becomes arithmetic. The induction schema is an axiom scheme, not a single axiom.

## Common Misconceptions
- PA is not the same as 'all of mathematics' — it cannot prove the consistency of set theory or many combinatorial principles.
- The induction axiom schema has infinitely many instances (one per formula), not just one.
