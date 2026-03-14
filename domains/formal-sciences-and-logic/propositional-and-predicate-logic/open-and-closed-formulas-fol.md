---
id: open-and-closed-formulas-fol
title: Open and Closed Formulas in First-Order Logic
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: first-order-logic-syntax
  type: hard
- id: variable-binding-and-scope
  type: hard
builds-toward:
- ground-terms-and-formulas
- quantifier-instantiation-rules
- variable-substitution-capture-avoidance
tags:
- first-order-logic
- variables
- binding
- scope
stage: formal-systems
status: draft
---

# Open and Closed Formulas in First-Order Logic

## Core Idea
A closed formula (or sentence) in first-order logic is a formula where every variable is bound by a quantifier; an open formula has at least one free (unbound) variable. For example, ∀x P(x) is closed, but P(x) and ∃y Q(x, y) are open (in the latter, x is free). Closed formulas are meaningful as statements: they are either true or false in a structure. Open formulas need an assignment of values to free variables to determine truth value.

## How It's Best Learned
Use concrete examples with marked quantifiers. Identify bound vs. free variables systematically, drawing scope lines for quantifiers. Emphasize that truth value of a closed formula is structure-relative (no variable assignment needed), while truth of an open formula depends on both the structure and variable assignment.

## Common Misconceptions
- Thinking all formulas must be closed (many proof systems and model-theoretic arguments involve open formulas).
- Confusing the same variable name in nested quantifiers (∀x ∃x P(x) binds two different instances).
- Believing a free variable is always 'undefined' (it's not — its truth value depends on the chosen assignment).
