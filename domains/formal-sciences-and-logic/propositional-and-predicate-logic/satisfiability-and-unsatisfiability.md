---
id: satisfiability-and-unsatisfiability
title: Satisfiability and Unsatisfiability
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: logical-consequence-and-entailment
  type: hard
builds-toward:
- consistency-and-inconsistency
tags:
- propositional-logic
- satisfiability
- sat-problem
stage: formal-systems
status: draft
---

# Satisfiability and Unsatisfiability

## Core Idea
A formula (or set of formulas) is satisfiable if there exists at least one interpretation making it true; it is unsatisfiable if no such interpretation exists. The satisfiability problem (SAT) is computationally fundamental: checking whether a propositional formula is satisfiable is NP-complete, making it one of the most important problems in computational logic.

## Explainer

From your study of logical consequence and entailment, you know that φ ⊨ ψ means every interpretation making φ true also makes ψ true. **Satisfiability** is the other fundamental semantic concept: it asks not about consequence between formulas, but about *possibility* — is there any interpretation that makes this formula true at all?

A formula φ is **satisfiable** if there exists at least one interpretation (an assignment of truth values to atomic sentences in propositional logic, or a domain and interpretation function in first-order logic) under which φ evaluates to true. It is **unsatisfiable** — also called a **contradiction** — if no such interpretation exists. These concepts connect directly to consequence: φ ⊨ ψ if and only if φ ∧ ¬ψ is unsatisfiable. Proving logical consequence and proving unsatisfiability are two sides of the same coin, which is why many automated theorem provers work by negating the conclusion and seeking a contradiction — a method called **refutation**.

In propositional logic, satisfiability is decidable by truth tables (check all 2^n assignments for n atomic variables), but this brute-force approach is exponential. The **SAT problem** — given a propositional formula, is it satisfiable? — is **NP-complete**, the landmark result of Cook's theorem (1971). Being NP-complete means SAT is at least as hard as any problem whose solution can be verified in polynomial time, and a polynomial-time algorithm for SAT would yield polynomial-time algorithms for all of NP. Despite this worst-case hardness, modern SAT solvers (based on DPLL and conflict-driven clause learning, CDCL) exploit the structure of practical instances to solve formulas with millions of variables efficiently.

**Unsatisfiability** is central to proof systems. A **refutation-complete** proof system — such as resolution — works by taking the negation of a target claim and deriving a contradiction (the empty clause). If the negation is unsatisfiable, the refutation will eventually be found; if it is satisfiable, no refutation exists. The completeness theorem for first-order logic connects these two sides: a sentence φ is unsatisfiable if and only if ⊥ is provable from φ in a complete proof system. Grasping this duality between semantic satisfiability and syntactic provability is essential for understanding both automated reasoning and the theoretical limits of what logic can decide.
