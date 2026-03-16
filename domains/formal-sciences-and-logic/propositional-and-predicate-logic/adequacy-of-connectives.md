---
id: adequacy-of-connectives
title: Adequacy and Completeness of Connective Sets
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: logical-equivalence-propositional
  type: hard
builds-toward:
- normal-forms-cnf-dnf
tags:
- semantics
- completeness
- propositional
stage: formal-systems
status: draft
---

# Adequacy and Completeness of Connective Sets

## Core Idea
A set of connectives is adequate if every truth function can be expressed using only those connectives. For example, {¬, ∧, ∨} is adequate, as is {¬, →}, but {∧, ∨} alone is not. Adequacy shows which minimal collections suffice to capture all logical structure.

## Explainer

A **truth function** for n variables is simply a function from {T, F}^n to {T, F} — a complete specification of an output for every combination of input truth values. For one variable there are 4 such functions (constant-T, constant-F, identity, negation); for two variables there are 16. The question of adequacy asks: which sets of logical connectives can express *all* such functions? From your prerequisite study of logical equivalence, you already know that ¬, ∧, and ∨ together are sufficient, because every truth function can be written in disjunctive normal form (DNF) — an OR of ANDs of possibly negated variables. This is the baseline: {¬, ∧, ∨} is adequate.

The interesting question is which *smaller* sets are adequate. {¬, ∧} is adequate because ∨ can be recovered: p ∨ q ≡ ¬(¬p ∧ ¬q) by De Morgan's law. {¬, ∨} is adequate by the symmetric argument. {¬, →} is adequate because p → q ≡ ¬p ∨ q, and negation lets you recover disjunction. But {∧, ∨} alone fails: every formula built from only ∧ and ∨ is a **monotone** function — flipping any input from F to T can never flip the output from T to F. Since negation is not monotone, it cannot be expressed in {∧, ∨}. This is an example of proving *non*-adequacy by identifying a structural invariant preserved by the inadequate set.

More surprisingly, even single connectives can be adequate. The **NAND** connective p ↑ q (true unless both p and q are true) is adequate alone: ¬p ≡ p ↑ p, and p ∧ q ≡ (p ↑ q) ↑ (p ↑ q). The **NOR** connective p ↓ q (true only when both are false) is also singly adequate: ¬p ≡ p ↓ p, and p ∨ q ≡ (p ↓ p) ↓ (q ↓ q). These are the only binary connectives that are singly adequate, a fact you can verify by checking all 16 two-variable connectives for the structural properties necessary to simulate negation and conjunction.

Adequacy matters beyond its own sake because it tells you how much expressible content a logic has. In digital circuit design, NAND and NOR gates are universal — any circuit can be built from one gate type alone, which is why hardware manufactures favor them. In proof theory, a Hilbert system using {¬, →} as primitive connectives is complete (adequate), meaning its axioms can express any tautology; proofs using only those connectives are sufficient. When you build a formal logic, choosing your primitive connectives determines what the language can say, and adequacy is the exact criterion for expressive completeness at the level of propositional truth functions.
