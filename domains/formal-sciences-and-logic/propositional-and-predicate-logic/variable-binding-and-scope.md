---
id: variable-binding-and-scope
title: Variable Binding and Scope
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: first-order-logic-syntax
  type: hard
builds-toward:
- substitution-and-unification
- quantifier-scope-ambiguity
tags:
- free-variables
- bound-variables
- scope
- quantifier-scope
- alpha-equivalence
stage: formal-systems
status: draft
---

# Variable Binding and Scope

## Core Idea
A quantifier (∀x or ∃x) binds every free occurrence of x within its scope — the subformula it governs. A variable occurrence is free if it is not bound by any quantifier, and bound if it falls within the scope of a matching quantifier. The same variable name can appear both free and bound in a single formula (e.g., P(x) ∧ ∀x Q(x)), which is legal but confusing. Alpha-equivalence says that renaming bound variables (∀x P(x) ≡ ∀y P(y)) does not change a formula's meaning, so bound variable names are arbitrary labels.

## How It's Best Learned
Mark every variable occurrence in a complex formula as free or bound, then draw scope brackets to visualize which quantifier governs which occurrences. Practice alpha-renaming to eliminate variable name clashes and confirm that meaning is preserved.

## Common Misconceptions
- A variable is not inherently free or bound — the same variable can have free and bound occurrences in the same formula.
- Renaming bound variables is always safe (alpha-equivalence), but renaming free variables changes the formula's meaning.
- The scope of a quantifier is determined by the syntactic structure (parentheses), not by proximity or left-to-right reading.
