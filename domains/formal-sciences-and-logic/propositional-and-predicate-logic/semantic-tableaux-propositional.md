---
id: semantic-tableaux-propositional
title: Semantic Tableaux (Propositional)
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: propositional-semantics
  type: hard
- id: truth-tables-and-evaluation
  type: soft
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

## Explainer

From your work on propositional semantics, you know that a formula is a **tautology** if it is true under every truth assignment. Truth tables verify this exhaustively, but with n variables, there are 2ⁿ rows. Semantic tableaux offer a smarter alternative: rather than enumerating all satisfying assignments, they systematically search for a *counterexample* and close off every dead end. If no counterexample is possible, the formula is a tautology.

The key idea is **refutation**: to prove φ is a tautology, assume ¬φ and try to satisfy it. Start by placing ¬φ at the root of a tree. Then apply **decomposition rules** that break the formula down without changing satisfiability. The rules come in two types. **Conjunctive rules** (alpha rules) extend a single branch: from φ ∧ ψ on a branch, add both φ and ψ to that branch (both must hold in any satisfying assignment). **Disjunctive rules** (beta rules) fork the tree: from φ ∨ ψ, create two new branches — one with φ, one with ψ — because any satisfying assignment must satisfy at least one. Negations are pushed inward using De Morgan equivalences.

A **branch closes** when it contains both a formula φ and its negation ¬φ: the branch represents a contradictory partial assignment and can be discarded. If *every* branch closes, the negation ¬φ is unsatisfiable — no assignment satisfies it — and therefore φ is a tautology. If some branch remains open after full expansion, that branch is essentially a partial assignment: read off the literals it contains to construct a counterexample that falsifies φ.

The connection to your prior work on truth tables is tight: a fully expanded tableau explores a tree of partial truth assignments, closing branches that lead to contradiction. Whereas a truth table checks 2ⁿ rows blindly, a tableau prunes the search as soon as contradictions arise. This pruning is what makes tableaux practical for formulas where early branching quickly closes. Tableaux are **sound** (closed tableau ⟹ tautology) and **complete** (every tautology has a closed tableau), properties that parallel the soundness and completeness of truth tables, and which you will see extended to first-order logic in the next course step.
