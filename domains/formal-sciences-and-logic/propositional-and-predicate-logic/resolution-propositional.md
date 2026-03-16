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

## Explainer

You already know CNF — conjunctive normal form — where a formula is a conjunction of **clauses**, each clause a disjunction of **literals**. Resolution operates entirely at this level. The single rule is: if you have a clause containing a literal p and another clause containing its negation ¬p, you can derive a new clause by removing both and combining everything else. Formally: from (C ∨ p) and (D ∨ ¬p), derive the **resolvent** (C ∨ D). The complementary pair {p, ¬p} cancels out; what remains is the logical union of the other literals.

The goal of resolution is **refutation**: to prove that a formula is unsatisfiable, you apply the resolution rule repeatedly until you derive the **empty clause** ⊥. The empty clause has no literals at all, representing a contradiction — it is unsatisfiable. If you can derive ⊥ from a clause set, the clause set must be unsatisfiable. The key theorem is **refutation completeness**: if a clause set is unsatisfiable, there exists a finite resolution derivation ending in ⊥. This is the logical engine beneath all automated theorem provers in propositional logic.

Why prove unsatisfiability rather than satisfiability directly? Because refutation composes beautifully with logical reasoning. To prove that a formula φ follows from hypotheses Γ, you **negate** what you want to prove, add ¬φ to Γ, convert to CNF, and run resolution. If you derive ⊥, you have shown Γ ∧ ¬φ is unsatisfiable, which means Γ ⊨ φ. This is the **proof by contradiction** pattern — resolution automates it mechanically.

A small example: suppose your clauses are {p ∨ q}, {¬p ∨ r}, {¬q}, {¬r}. Resolve {p ∨ q} with {¬q} to get {p}. Resolve {p} with {¬p ∨ r} to get {r}. Resolve {r} with {¬r} to get ⊥. The empty clause is derived in three steps, confirming unsatisfiability. Notice that each step eliminates one variable; the process is systematic. The **Davis-Putnam procedure** formalizes this by eagerly applying unit propagation (when a clause has one literal, that literal must be true) and pure literal elimination (if a literal appears only positively or only negatively, set it to satisfy all clauses containing it). Modern SAT solvers build on this foundation with conflict-driven clause learning, making resolution-based reasoning scale to problems with millions of variables.
