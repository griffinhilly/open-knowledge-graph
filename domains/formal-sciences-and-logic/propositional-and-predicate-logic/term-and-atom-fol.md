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

## Explainer

From your study of first-order logic syntax, you know that formulas are built inductively from atomic formulas using connectives and quantifiers. But what exactly are atomic formulas built from? The answer requires distinguishing two separate syntactic categories: **terms** (which denote objects in the domain) and **formulas** (which make assertions about those objects). These two categories are grammatically incompatible — you cannot substitute one for the other — and confusing them produces type errors in formal proofs.

Terms are built from three kinds of ingredients. **Variables** (x, y, z) are ranging placeholders that receive values from the domain under a variable assignment. **Constants** (a, b, c) are names for specific fixed objects that do not change across variable assignments. **Function symbols** applied to terms: if f is a binary function symbol and t₁, t₂ are already terms, then f(t₁, t₂) is a term. A **ground term** contains no variables — it denotes a specific domain element regardless of variable assignment. The term f(a, g(b)) is ground; the term f(x, a) is not, because its denotation depends on what x is assigned. This ground/open distinction matters for substitution: substituting a ground term for a variable produces a formula with one fewer free variable, eventually yielding a ground instance.

An **atomic formula** applies a predicate symbol to the right number of terms: if P is a binary predicate and t₁, t₂ are terms, then P(t₁, t₂) is an atomic formula. Atomic formulas are the base cases from which all formulas are built — but they are not terms. Terms name objects; formulas assert relationships. "The sum of 2 and 3" is a term denoting 5; "2 plus 3 equals 5" is a formula asserting a fact. In formal syntax: plus(2, 3) is a term of sort number, while equals(plus(2, 3), 5) is an atomic formula of sort boolean. The distinction mirrors the noun phrase / sentence distinction in natural language, and it is enforced by the grammar of FOL in the same way type systems enforce it in programming languages.

The practical payoff comes in substitution, unification, and model theory. To substitute a term t for variable x in a formula, you replace each free occurrence of x with t — and you can only substitute *terms* for variables, not formulas for formulas (that would require second-order logic). When you ground a formula by substituting ground terms for all free variables, you get a **ground instance**: a specific claim about specific objects with no remaining ambiguity. The **Herbrand universe** — the set of all ground terms — is the arena for Herbrand's theorem and resolution-based provers. Every first-order formula that is satisfiable has a model built entirely from ground terms. Understanding the term/formula distinction is what makes the structure of this argument visible.
