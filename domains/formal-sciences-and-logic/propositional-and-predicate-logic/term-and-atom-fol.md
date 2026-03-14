---
id: term-and-atom-fol
title: Terms and Atomic Formulas in FOL
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: first-order-logic-syntax
  type: hard
builds-toward:
- substitution-and-unification
- variable-binding-and-scope
tags:
- terms
- atomic-formulas
- constants
- variables
- function-symbols
- ground-terms
stage: formal-systems
status: draft
---

# Terms and Atomic Formulas in FOL

## Core Idea
In first-order logic, terms are the expressions that denote objects in the domain: variables (x, y), constants (a, b), and function symbols applied to terms (f(x), g(a, y)). An atomic formula is a predicate symbol applied to terms — P(x, f(a)) asserts that the objects denoted by x and f(a) stand in relation P. A ground term contains no variables and denotes a fixed element; an open term contains free variables and denotes different elements under different variable assignments. The term/formula distinction is fundamental: terms name objects, formulas make claims about them.

## How It's Best Learned
Given a signature (specific constant, function, and predicate symbols with arities), enumerate all terms up to a certain depth, then build all atomic formulas from those terms. Classify each as ground or open and trace how variable assignments affect denotation.

## Common Misconceptions
- Terms are not formulas — P(x) is a formula, but x and f(x) are terms. Confusing the two leads to type errors in formal proofs.
- Constants are not variables — a constant always denotes the same object, while a variable ranges over the domain.
- Function symbols are not predicates — f(x) is a term (it names an object), while P(x) is a formula (it asserts a property).
