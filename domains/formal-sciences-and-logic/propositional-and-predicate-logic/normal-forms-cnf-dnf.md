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
status: draft
---

# Conjunctive and Disjunctive Normal Forms

## Core Idea
Every propositional formula can be converted to conjunctive normal form (CNF — a conjunction of disjunctions of literals) or disjunctive normal form (DNF — a disjunction of conjunctions of literals). CNF is fundamental to SAT solving and the resolution proof method; DNF makes satisfiability checking easy (a DNF is satisfiable iff any conjunct is consistent). The conversion uses De Morgan's laws, double negation elimination, and distribution. Normal forms provide canonical representations that simplify algorithmic reasoning about formulas.

## How It's Best Learned
Convert the same formula to both CNF and DNF by hand. Verify satisfiability directly from the DNF and check validity via the CNF. Use truth tables to confirm equivalence.

## Common Misconceptions
- CNF and DNF are not unique — a formula has many equivalent CNF/DNF representations.
- A CNF formula with an empty clause is always false; a DNF with an empty conjunct is always true.
