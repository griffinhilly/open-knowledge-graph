---
id: first-order-logic-syntax
title: First-Order Logic Syntax
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: propositional-syntax
  type: hard
- id: predicates-and-quantifiers
  type: hard
- id: negation-of-quantifiers
  type: hard
- id: set-membership-and-notation
  type: soft
- id: set-fundamentals
  type: soft
- id: functions-and-function-properties
  type: soft
- id: relations-as-set-subsets
  type: soft
builds-toward:
- first-order-semantics
- natural-deduction-fol
- formal-arithmetic-and-expressibility
tags:
- first-order-logic
- quantifiers
- variables
- terms
- formulas
- FOL
stage: formal-systems
status: validated
---

# First-Order Logic Syntax

## Core Idea
First-order logic (FOL) extends propositional logic with terms (variables, constants, function symbols applied to terms) and atomic formulas (predicate symbols applied to terms). Quantifiers ∀ (for all) and ∃ (there exists) bind variables, giving rise to the distinction between free and bound occurrences. A sentence is a formula with no free variables. The language of a first-order theory is specified by its signature: a collection of constant, function, and predicate symbols with their arities. Different signatures yield different logical languages (e.g., the language of arithmetic vs. the language of set theory).

## How It's Best Learned
Practice translating English statements into FOL and back. Carefully track variable scope to distinguish bound and free occurrences. Build formulas of increasing complexity from simple atomic predicates.

## Common Misconceptions
- Quantifiers bind variables, not predicates — ∀x P(x) quantifies over the domain, not over predicates.
- Free variables in a formula are implicitly universally quantified in some contexts but not others; always be explicit about scope.
