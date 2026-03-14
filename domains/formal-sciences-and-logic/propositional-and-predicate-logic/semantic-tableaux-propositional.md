---
id: semantic-tableaux-propositional
title: Semantic Tableaux (Propositional)
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: propositional-semantics
  type: hard
builds-toward:
- semantic-tableaux-fol
- propositional-soundness-completeness
tags:
- tableaux
- tree-method
- refutation
- branch
- systematic-proof
stage: formal-systems
status: draft
---

# Semantic Tableaux (Propositional)

## Core Idea
The semantic tableau (or tree method) is a systematic refutation procedure: to test whether a formula is a tautology, assume its negation and decompose it into a tree of simpler subformulas using branching rules. Conjunctions extend a single branch; disjunctions fork into two branches. A branch closes when it contains both a literal and its negation. If every branch closes, the original negation is unsatisfiable and the formula is a tautology. Tableaux are both sound (closed tableaux prove validity) and complete (every tautology has a closed tableau).

## How It's Best Learned
Work through tableaux for formulas you already know are tautologies (e.g., p → p, ¬(p ∧ ¬p)) and for non-tautologies to see open branches that yield counterexamples. Practice the discipline of applying rules in a fixed order to ensure systematic coverage.

## Common Misconceptions
- An open branch does not mean the formula is invalid — it means you may not have finished expanding; only a fully expanded open branch is a counterexample.
- Tableaux are refutation systems: you negate the formula first, then show the negation is unsatisfiable.
- The order of rule application affects tree size but not correctness — any order yields the same verdict.
