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
- id: resolution-propositional
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
status: validated
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

## Questions

```yaml
- question: "A student builds a tableau for formula φ and finds one branch still open. They say 'I just haven't finished expanding that branch yet.' When are they right, and when are they wrong?"
  type: multiple-choice
  options:
    - "They are always right — any open branch means more decomposition rules can still be applied"
    - "They are right only if unexpanded formulas remain on that branch; if it is fully expanded, the open branch is a counterexample showing φ is not a tautology"
    - "They are always wrong — an open branch always means the formula is a tautology"
    - "They are right — a tableau proves a tautology when at least one branch closes, not all of them"
  answer: 1
  explanation: "An open branch with unexpanded formulas does mean more work remains. But a *fully expanded* open branch — where every formula has been decomposed as far as the rules allow — is a genuine counterexample: the literals on it form a consistent partial assignment that satisfies ¬φ, proving φ is not a tautology. The key word is 'fully expanded.' Option D reverses the requirement: for a tautology, *every* branch must close — one open branch is enough to refute it."

- question: "In a semantic tableau for the formula ¬(P ∨ Q), what is the correct next step after writing ¬(P ∨ Q) at the root?"
  type: multiple-choice
  options:
    - "Fork the tree into two branches: one with P and one with Q"
    - "Add both ¬P and ¬Q to the same branch, extending it without forking"
    - "Add P and Q to the same branch, since ∨ requires both to be considered"
    - "Close the branch immediately, since a negated disjunction is always false"
  answer: 1
  explanation: "¬(P ∨ Q) is equivalent to ¬P ∧ ¬Q by De Morgan's law — it is a conjunctive form (alpha formula). Conjunctions add both conjuncts to the same branch without forking, because any satisfying assignment must satisfy both. So ¬P and ¬Q are both added to the current branch. Option A describes the rule for a disjunction (P ∨ Q), which would fork the tree. Recognizing whether a formula is conjunctive (alpha) or disjunctive (beta) determines whether to extend or branch."

- question: "Semantic tableaux are a refutation procedure — they prove a formula is a tautology by assuming its negation and showing that assumption leads to contradictions on every branch."
  type: true-false
  answer: true
  explanation: "This is the defining structure of the method. You place ¬φ at the root (assuming φ is false) and systematically decompose it to find any truth assignment that satisfies ¬φ. If every branch closes (contains both φ and ¬φ for some φ), then ¬φ is unsatisfiable — no assignment can make it true. Since ¬φ is unsatisfiable, φ must be true under all assignments — it is a tautology. The indirect proof structure (assume the negation, derive contradiction everywhere) is what makes tableaux a refutation system."

- question: "In a semantic tableau, a disjunction P ∨ Q on a branch means you add both P and Q to that same branch without forking."
  type: true-false
  answer: false
  explanation: "This confuses the rules for conjunctions and disjunctions. A conjunction P ∧ Q adds both P and Q to the same branch (conjunctive/alpha rule), because any satisfying assignment must satisfy both conjuncts. A disjunction P ∨ Q instead forks the tree into two branches — one containing P, one containing Q — because any satisfying assignment must satisfy at least one disjunct but not necessarily both (disjunctive/beta rule). Applying the conjunction rule to disjunctions is the most common tableau error and produces incorrect results."

- question: "Why does a closed semantic tableau prove that the original formula φ is a tautology? Explain the logical chain."
  type: short-answer
  answer: "The tableau starts by assuming ¬φ. Each branch represents a possible way a truth assignment could satisfy ¬φ. A branch closes when it contains both some formula and its negation — a contradiction that no assignment can satisfy. If every branch closes, every possible way to satisfy ¬φ leads to contradiction, so ¬φ is unsatisfiable. A formula is unsatisfiable if and only if its negation is a tautology. Therefore ¬(¬φ) = φ is a tautology."
  explanation: "Three logical steps link the closed tableau to the tautology claim: (1) decomposition rules are truth-preserving — each branch faithfully represents a class of possible assignments; (2) branch closure means that class leads to contradiction and is thus empty; (3) all branches closing means no assignment satisfies ¬φ — ¬φ is unsatisfiable. By the classical equivalence 'φ is a tautology iff ¬φ is unsatisfiable,' the closed tableau proves φ is valid. Soundness of the rules is what justifies step (1); completeness guarantees that every tautology will eventually produce a closed tableau."
```

## Explainer

From your work on propositional semantics, you know that a formula is a **tautology** if it is true under every truth assignment. Truth tables verify this exhaustively, but with n variables, there are 2ⁿ rows. Semantic tableaux offer a smarter alternative: rather than enumerating all satisfying assignments, they systematically search for a *counterexample* and close off every dead end. If no counterexample is possible, the formula is a tautology.

The key idea is **refutation**: to prove φ is a tautology, assume ¬φ and try to satisfy it. Start by placing ¬φ at the root of a tree. Then apply **decomposition rules** that break the formula down without changing satisfiability. The rules come in two types. **Conjunctive rules** (alpha rules) extend a single branch: from φ ∧ ψ on a branch, add both φ and ψ to that branch (both must hold in any satisfying assignment). **Disjunctive rules** (beta rules) fork the tree: from φ ∨ ψ, create two new branches — one with φ, one with ψ — because any satisfying assignment must satisfy at least one. Negations are pushed inward using De Morgan equivalences.

A **branch closes** when it contains both a formula φ and its negation ¬φ: the branch represents a contradictory partial assignment and can be discarded. If *every* branch closes, the negation ¬φ is unsatisfiable — no assignment satisfies it — and therefore φ is a tautology. If some branch remains open after full expansion, that branch is essentially a partial assignment: read off the literals it contains to construct a counterexample that falsifies φ.

The connection to your prior work on truth tables is tight: a fully expanded tableau explores a tree of partial truth assignments, closing branches that lead to contradiction. Whereas a truth table checks 2ⁿ rows blindly, a tableau prunes the search as soon as contradictions arise. This pruning is what makes tableaux practical for formulas where early branching quickly closes. Tableaux are **sound** (closed tableau ⟹ tautology) and **complete** (every tautology has a closed tableau), properties that parallel the soundness and completeness of truth tables, and which you will see extended to first-order logic in the next course step.
