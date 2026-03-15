---
id: resolution-propositional
title: Propositional Resolution
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: normal-forms-cnf-dnf
  type: hard
- id: propositional-soundness-completeness
  type: soft
- id: boolean-algebra
  type: soft
builds-toward:
- resolution-fol
tags:
- resolution
- refutation
- clause
- Davis-Putnam
- SAT
stage: formal-systems
status: draft
---

# Propositional Resolution

## Core Idea
Resolution is a single inference rule: from clauses (C ∨ p) and (D ∨ ¬p), derive the resolvent (C ∨ D). Applied to a formula in CNF, repeated resolution can derive the empty clause (⊥) if and only if the original clause set is unsatisfiable. This refutation-complete method is the theoretical foundation of SAT solvers and automated theorem proving. The Davis-Putnam procedure systematically applies resolution with unit propagation and pure literal elimination to decide satisfiability efficiently in practice.

## How It's Best Learned
Convert a small unsatisfiable formula to CNF, list its clauses, and resolve pairs step by step until the empty clause appears. Then try a satisfiable formula and observe that no empty clause can be derived.

## Common Misconceptions
- Resolution proves unsatisfiability, not satisfiability — it is a refutation system, so you negate the goal before resolving.
- The resolvent drops the complementary literal pair; beginners often forget to remove both p and ¬p from the result.
- Resolution is refutation-complete but not efficient by itself — modern SAT solvers augment it with clause learning, backjumping, and heuristics.
