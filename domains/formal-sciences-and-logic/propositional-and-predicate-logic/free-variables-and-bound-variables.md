---
id: free-variables-and-bound-variables
title: Free Variables and Bound Variables
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: universal-quantifier-semantics
  type: hard
- id: existential-quantifier-semantics
  type: hard
builds-toward:
- substitution-and-instantiation
- variable-binding-and-scope
tags:
- syntax
- semantics
- variables
stage: formal-systems
status: draft
---

# Free Variables and Bound Variables

## Core Idea
A variable x is bound if it appears within the scope of ∀x or ∃x; otherwise it is free. Bound variables are placeholders—renaming them does not change the formula's meaning. Free variables affect truth conditions; a sentence (no free variables) has a definite truth value in a structure, while an open formula does not.

## How It's Best Learned
Visually mark quantifier scopes in complex formulas. Identify which variable occurrences are bound vs. free. Observe that ∀x P(x, y) is true iff P(a, y) holds for all a, showing free y remains unquantified.

## Common Misconceptions
Thinking a formula with free variables is incomplete or invalid. Confusing variable name with binding status. Not recognizing that free variables parameterize a family of formulas.
