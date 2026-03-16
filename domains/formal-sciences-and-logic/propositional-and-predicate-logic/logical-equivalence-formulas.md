---
id: logical-equivalence-formulas
title: Logical Equivalence of Formulas
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: formula-evaluation-and-truth-tables
  type: hard
builds-toward:
- logical-consequence-and-entailment
tags:
- propositional-logic
- equivalence
- transformation
stage: formal-systems
status: draft
---

# Logical Equivalence of Formulas

## Core Idea
Two formulas are logically equivalent if they have the same truth value under every possible interpretation. Logical equivalence is an equivalence relation on formulas and forms the basis for simplifying, transforming, and understanding the deep structure of logical formulas.

## Explainer

You know how to evaluate a propositional formula's truth value using **truth tables**: for each possible assignment of T/F to the variables, compute the formula's output. Two formulas are **logically equivalent** — written φ ≡ ψ — if they produce identical truth tables. Every row gives the same output. This means they express the same logical content; one can always replace the other in any context without changing the truth value of the compound formula containing them.

The most important logical equivalences form a small algebra of propositional logic. **De Morgan's laws** let you push negations inward: ¬(A ∧ B) ≡ (¬A ∨ ¬B), and ¬(A ∨ B) ≡ (¬A ∧ ¬B). Think of negating a conjunction as distributing the negation and flipping the connective from "and" to "or." **Double negation elimination** gives ¬¬A ≡ A. The **conditional equivalence** A → B ≡ ¬A ∨ B is crucial: it rewrites an implication purely in terms of disjunction and negation. **Distributive laws** mirror their algebraic counterparts: A ∧ (B ∨ C) ≡ (A ∧ B) ∨ (A ∧ C). Verify any of these by drawing the full truth table for both sides — every row will match.

These equivalences are the engine for converting formulas into **normal forms** — canonical representations with standardized structure. Applying De Morgan's laws, double negation, and distribution systematically converts any formula into **Conjunctive Normal Form (CNF)**: a conjunction (AND) of clauses, where each clause is a disjunction (OR) of literals. CNF is the standard input format for SAT solvers, making these equivalences directly relevant to automated reasoning. Every formula is also reducible to **Disjunctive Normal Form (DNF)**: a disjunction of conjunctions. The existence of both normal forms proves that ∧, ∨, and ¬ together are **functionally complete** — sufficient to express any truth function.

Logical equivalence is an **equivalence relation** on formulas: every formula is equivalent to itself, equivalence is symmetric, and it is transitive (if φ ≡ ψ and ψ ≡ χ then φ ≡ χ). This partitions the space of all formulas into equivalence classes of "synonymous" expressions. The practical payoff is the **substitution theorem**: if φ ≡ ψ, then replacing any occurrence of φ inside a larger formula with ψ preserves the larger formula's truth value under every interpretation. This is what makes algebraic manipulation of logic possible — the same way you substitute equals for equals in arithmetic, you substitute logically equivalent formulas in logic, and the surrounding structure is unaffected.
