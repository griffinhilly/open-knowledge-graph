---
id: normal-forms-cnf-dnf
title: Conjunctive and Disjunctive Normal Forms
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: tautologies-and-contradictions
  type: hard
- id: boolean-algebra
  type: soft
- id: truth-tables
  type: soft
builds-toward:
- propositional-compactness
- sequent-calculus-intro
tags:
- CNF
- DNF
- normal-form
- clause
- literal
stage: formal-systems
status: validated
---

# Conjunctive and Disjunctive Normal Forms

## Core Idea
Every propositional formula can be converted to conjunctive normal form (CNF — a conjunction of disjunctions of literals) or disjunctive normal form (DNF — a disjunction of conjunctions of literals). CNF is fundamental to SAT solving and the resolution proof method; DNF makes satisfiability checking easy (a DNF is satisfiable iff any conjunct is consistent). The conversion uses De Morgan's laws, double negation elimination, and distribution. Normal forms provide canonical representations that simplify algorithmic reasoning about formulas.

## How It's Best Learned
Convert the same formula to both CNF and DNF by hand. Verify satisfiability directly from the DNF and check validity via the CNF. Use truth tables to confirm equivalence.

## Common Misconceptions
- CNF and DNF are not unique — a formula has many equivalent CNF/DNF representations.
- A CNF formula with an empty clause is always false; a DNF with an empty conjunct is always true.

## Explainer

You know from truth tables and Boolean algebra that any propositional formula defines a truth function — a mapping from truth assignments to true/false. Normal forms are **canonical structural representations** of those truth functions. Instead of an arbitrary tangle of connectives, CNF and DNF impose a uniform two-level structure that makes certain reasoning tasks dramatically easier.

A **literal** is an atom or its negation: p, ¬p, q, ¬q, and so on. A **clause** in CNF is a disjunction of literals (p ∨ ¬q ∨ r), and a **CNF formula** is a conjunction of clauses — "AND of ORs." A **conjunct** in DNF is a conjunction of literals (p ∧ ¬q ∧ r), and a **DNF formula** is a disjunction of conjuncts — "OR of ANDs." The key insight is that these two structures trade off which reasoning task is easy. In DNF, **satisfiability** is trivial: a DNF is satisfiable if and only if at least one conjunct is internally consistent (contains no literal and its negation). In CNF, **falsifiability** is trivial: a CNF is falsifiable if and only if at least one clause can be made false. Correspondingly, checking DNF validity is hard (every conjunct must be a tautology), while checking CNF satisfiability is hard (the SAT problem).

The conversion procedure builds on De Morgan's laws and distribution. To reach CNF: push negations inward using De Morgan's (¬(A ∧ B) → ¬A ∨ ¬B, ¬(A ∨ B) → ¬A ∧ ¬B), eliminate double negations, then distribute ∨ over ∧ to "open up" each clause. To reach DNF: push negations inward, eliminate double negations, then distribute ∧ over ∨. A shortcut via truth tables: read off a DNF directly by writing one conjunct per row where the formula is true (the **canonical DNF** or **sum of minterms**), or a CNF by writing one clause per row where the formula is false.

CNF is ubiquitous in computational logic because the SAT problem — is this CNF formula satisfiable? — is the canonical NP-complete problem, and modern SAT solvers require CNF input. The **resolution proof method** (which you will encounter next) works exclusively on CNF: two clauses (A ∨ p) and (B ∨ ¬p) resolve to (A ∨ B) by eliminating the complementary literal pair. Understanding CNF as a data structure, not just a normal form, is the key to seeing why so much of automated reasoning is built on it.
