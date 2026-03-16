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

## Explainer

From your study of first-order logic syntax and variable binding, you know that quantifiers bind variables — ∀x means "for all values of x" and ∃x means "there exists a value of x." The open/closed distinction is simply careful bookkeeping: which variables in a formula are bound by a quantifier, and which are left "dangling"? A **closed formula** (or **sentence**) has no free variables — every variable occurrence is within the scope of some quantifier binding it. An **open formula** has at least one **free variable** — an occurrence not captured by any enclosing quantifier.

A few examples sharpen the distinction. The formula ∀x (x > 0 → ∃y (y · y = x)) is a sentence: both x and y are bound. The formula x > 0 is open: x appears with no quantifier. The formula ∃y (y · y = x) is also open: y is bound by ∃y, but x is free. In this last formula, whether the statement is true depends on what value x has — in the natural numbers, it is true when x is a perfect square and false otherwise. The free variable x is like an input to a predicate: it awaits an assignment before the formula has a definite truth value.

The practical significance is immediate: sentences can be evaluated as true or false in a structure directly, with no additional information. "For all x, x · 1 = x" is true in the natural numbers, period. But "x · 1 = x" is an open formula that becomes meaningful only when you supply a **variable assignment** — a function from free variables to elements of the domain. Together, a structure and a variable assignment determine the truth value of any formula, open or closed. For sentences, the assignment is irrelevant (quantifiers handle all variables internally), which is why sentences are the natural objects of logical theorems, axioms, and model theory.

The distinction has deep consequences for proof systems. **Substitution** — replacing a free variable with a term — is how universal instantiation works: from ∀x P(x) you derive P(t) by substituting term t for x. But substitution must be **capture-avoiding**: if t contains a variable y, and y would fall inside a ∀y quantifier after substitution, the free y in t would be "captured" by that quantifier, changing the formula's meaning. The rules for safe substitution are precisely about tracking which variables are free in which subformulas. Mastering open and closed formulas is therefore not a mere syntactic exercise — it is the prerequisite for every formal proof rule and semantic argument you will encounter in predicate logic.
