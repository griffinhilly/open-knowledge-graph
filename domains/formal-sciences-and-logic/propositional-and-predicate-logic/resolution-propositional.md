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

## Questions

```yaml
- question: "You want to use propositional resolution to prove that formula φ follows from premises Γ. What is the correct procedure?"
  type: multiple-choice
  options:
    - "Convert φ to CNF and resolve its clauses until you derive each clause of Γ"
    - "Add ¬φ to Γ, convert everything to CNF, and resolve until the empty clause ⊥ is derived"
    - "Convert both φ and Γ to CNF separately and check whether every clause of φ appears in Γ"
    - "Resolve the clauses of Γ together until either φ or ¬φ is derived"
  answer: 1
  explanation: "Resolution is a *refutation* system — it proves things by deriving contradiction, not by constructing proofs forward. To show Γ ⊨ φ, you negate what you want to prove (add ¬φ to Γ), convert everything to CNF, and apply the resolution rule repeatedly. If you derive the empty clause ⊥, you have shown that Γ ∧ ¬φ is unsatisfiable — meaning there is no world where Γ is true and φ is false — which is exactly what Γ ⊨ φ means. Attempting to derive φ directly from Γ (option D) doesn't work because resolution as a rule produces clauses, not arbitrary formulas."

- question: "Applying resolution to clauses (A ∨ B ∨ ¬C) and (C ∨ D), where C is the resolved literal, produces which resolvent?"
  type: multiple-choice
  options:
    - "(A ∨ B ∨ D)"
    - "(A ∨ B ∨ ¬C ∨ C ∨ D)"
    - "(A ∨ B)"
    - "(¬C ∨ C)"
  answer: 0
  explanation: "The resolution rule: from (X ∨ p) and (Y ∨ ¬p), derive (X ∨ Y). Here the complementary pair is ¬C and C. Remove both from their respective clauses and combine the remaining literals: (A ∨ B) from the first clause and (D) from the second, giving (A ∨ B ∨ D). Option B is wrong — it includes both C and ¬C in the resolvent (the whole point is that they cancel). Option C drops D. Option D is a tautology (always true) and is never a valid resolvent from these clauses."

- question: "If propositional resolution derives the empty clause from a set of clauses, this proves that the clause set is satisfiable."
  type: true-false
  answer: false
  explanation: "The opposite is true. The empty clause ⊥ has no literals — it is a disjunction of zero things, which is vacuously false (a contradiction). Deriving ⊥ means the clause set is *unsatisfiable*: there is no truth assignment that makes all clauses simultaneously true. Resolution is a refutation proof system: it proves unsatisfiability, not satisfiability. If you want to prove that a formula φ follows from premises Γ, you *negate* φ and try to derive ⊥, showing that Γ ∧ ¬φ is unsatisfiable — and therefore φ must be true whenever Γ is."

- question: "Resolution is refutation-complete: if a set of propositional clauses is unsatisfiable, there always exists a finite sequence of resolution steps that derives the empty clause."
  type: true-false
  answer: true
  explanation: "Refutation completeness is resolution's central theoretical guarantee. It means that if no truth assignment satisfies all the clauses, then resolution *can* find a derivation of ⊥ — it won't miss an unsatisfiable instance. However, refutation completeness does not mean resolution is efficient: the number of resolution steps may be exponential. Nor does it help with satisfiable instances — if the clause set is satisfiable, resolution will never derive ⊥ (since no contradiction exists), but it also doesn't produce a satisfying assignment directly. Modern SAT solvers address the efficiency gap with conflict-driven clause learning and other heuristics built on top of the resolution foundation."

- question: "Why do automated theorem provers using resolution negate the goal formula before resolving, rather than trying to derive the goal directly from the premises?"
  type: short-answer
  answer: "Resolution is a refutation system — its only mechanism is deriving the empty clause ⊥, which represents a contradiction. It has no rule for directly constructing a proof that a formula is true. To prove Γ ⊨ φ, we use the logical equivalence: Γ ⊨ φ if and only if Γ ∧ ¬φ is unsatisfiable. By adding ¬φ to Γ and converting to CNF, we ask: 'can we find a contradiction in this expanded set?' If resolution derives ⊥, the answer is yes — and that contradiction proves φ must be true whenever Γ holds."
  explanation: "This is proof by contradiction mechanized. It works because of the soundness and refutation-completeness of resolution: if Γ ∧ ¬φ is genuinely unsatisfiable, resolution will find a derivation of ⊥ (completeness), and any derivation of ⊥ correctly certifies unsatisfiability (soundness). The design elegance is that you need only one inference rule (resolution) and one goal (derive ⊥) to handle all propositional reasoning — no separate rules for 'and-introduction,' 'modus ponens,' etc."
```

## Explainer

You already know CNF — conjunctive normal form — where a formula is a conjunction of **clauses**, each clause a disjunction of **literals**. Resolution operates entirely at this level. The single rule is: if you have a clause containing a literal p and another clause containing its negation ¬p, you can derive a new clause by removing both and combining everything else. Formally: from (C ∨ p) and (D ∨ ¬p), derive the **resolvent** (C ∨ D). The complementary pair {p, ¬p} cancels out; what remains is the logical union of the other literals.

The goal of resolution is **refutation**: to prove that a formula is unsatisfiable, you apply the resolution rule repeatedly until you derive the **empty clause** ⊥. The empty clause has no literals at all, representing a contradiction — it is unsatisfiable. If you can derive ⊥ from a clause set, the clause set must be unsatisfiable. The key theorem is **refutation completeness**: if a clause set is unsatisfiable, there exists a finite resolution derivation ending in ⊥. This is the logical engine beneath all automated theorem provers in propositional logic.

Why prove unsatisfiability rather than satisfiability directly? Because refutation composes beautifully with logical reasoning. To prove that a formula φ follows from hypotheses Γ, you **negate** what you want to prove, add ¬φ to Γ, convert to CNF, and run resolution. If you derive ⊥, you have shown Γ ∧ ¬φ is unsatisfiable, which means Γ ⊨ φ. This is the **proof by contradiction** pattern — resolution automates it mechanically.

A small example: suppose your clauses are {p ∨ q}, {¬p ∨ r}, {¬q}, {¬r}. Resolve {p ∨ q} with {¬q} to get {p}. Resolve {p} with {¬p ∨ r} to get {r}. Resolve {r} with {¬r} to get ⊥. The empty clause is derived in three steps, confirming unsatisfiability. Notice that each step eliminates one variable; the process is systematic. The **Davis-Putnam procedure** formalizes this by eagerly applying unit propagation (when a clause has one literal, that literal must be true) and pure literal elimination (if a literal appears only positively or only negatively, set it to satisfy all clauses containing it). Modern SAT solvers build on this foundation with conflict-driven clause learning, making resolution-based reasoning scale to problems with millions of variables.
