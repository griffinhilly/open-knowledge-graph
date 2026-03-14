---
id: tautologies-and-contradictions
title: Tautologies, Contradictions, and Satisfiability
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: propositional-semantics
  type: hard
- id: logical-equivalences
  type: soft
- id: truth-tables
  type: soft
builds-toward:
- normal-forms-cnf-dnf
- propositional-soundness-completeness
tags:
- tautology
- contradiction
- satisfiability
- validity
stage: formal-systems
status: validated
---

# Tautologies, Contradictions, and Satisfiability

## Core Idea
A tautology is a formula true under every possible valuation (e.g., p ∨ ¬p); a contradiction is false under every valuation (e.g., p ∧ ¬p); a contingency is neither. A formula is satisfiable if at least one valuation makes it true. These classifications partition the space of propositional formulas and are central to logic — proof systems aim to derive exactly the tautologies. The semantic notion of validity (⊨ φ) is the target that syntactic proof systems strive to match.

## How It's Best Learned
Classify a variety of formulas before and after applying De Morgan's laws. Practice converting the question 'is φ a tautology?' to 'is ¬φ a contradiction?' and verify the equivalence.

## Common Misconceptions
- A tautology is not just 'always probably true' — it must hold for literally every truth assignment.
- Satisfiable does not mean true; it means true in at least one scenario.
