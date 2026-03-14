---
id: substitution-and-unification
title: Substitution and Unification
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: first-order-logic-syntax
  type: hard
- id: term-and-atom-fol
  type: hard
builds-toward:
- resolution-fol
- natural-deduction-fol
tags:
- substitution
- unification
- most-general-unifier
- variable-capture
- automated-reasoning
stage: formal-systems
status: draft
---

# Substitution and Unification

## Core Idea
Substitution replaces free occurrences of a variable x in a formula with a term t, written φ[t/x]. The operation must be capture-avoiding: if t contains a variable y that would become bound in φ, the bound variable must first be renamed (alpha-conversion) to prevent the substituted variable from being inadvertently captured. Unification is the inverse problem — given two terms or atoms, find a substitution (called a unifier) that makes them syntactically identical. The most general unifier (MGU) is the least committal such substitution. Robinson's unification algorithm computes the MGU in near-linear time, and it is the engine behind resolution-based theorem proving and logic programming.

## How It's Best Learned
Perform substitutions by hand on formulas with nested quantifiers, deliberately encountering variable-capture problems and fixing them. Then unify pairs of atomic formulas step by step using Robinson's algorithm, building the MGU incrementally.

## Common Misconceptions
- Substitution only replaces free occurrences — bound occurrences of the same variable name are untouched.
- Variable capture is a real and common bug, not an edge case — failing to rename bound variables before substitution can silently change a formula's meaning.
- Not all pairs of terms are unifiable (e.g., f(x) and g(x) cannot unify if f ≠ g); unification can fail, and recognizing failure is part of the algorithm.
