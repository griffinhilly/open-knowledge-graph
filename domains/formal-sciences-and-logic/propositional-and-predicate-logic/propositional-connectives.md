---
id: propositional-connectives
title: Propositional Connectives
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: propositional-syntax
  type: hard
builds-toward:
- propositional-semantics
- tautologies-and-contradictions
tags:
- connectives
- negation
- conjunction
- disjunction
- implication
- biconditional
- truth-functional
stage: formal-systems
status: draft
---

# Propositional Connectives

## Core Idea
The five standard propositional connectives — NOT (¬), AND (∧), OR (∨), IMPLIES (→), and IFF (↔) — are defined purely by their truth-functional behavior: the truth value of any compound formula is entirely determined by the truth values of its components. Each connective has a fixed truth table that serves as its semantic definition. Precedence conventions (¬ binds tightest, then ∧, then ∨, then →, then ↔) reduce the need for parentheses, but understanding this hierarchy is essential for correct parsing.

## How It's Best Learned
Build the truth table for each connective from scratch, then combine them to evaluate compound formulas step by step. Pay special attention to material implication (→), whose truth table surprises most beginners: a false antecedent makes the conditional true regardless of the consequent.

## Common Misconceptions
- Material implication (→) does not capture causation or temporal sequence — "if P then Q" is true whenever P is false, which feels counterintuitive but is logically consistent.
- Inclusive OR (∨) is true when both disjuncts are true, unlike the everyday "or" which often implies exclusivity.
- Precedence is a notational convention, not a logical fact — when in doubt, use parentheses.
