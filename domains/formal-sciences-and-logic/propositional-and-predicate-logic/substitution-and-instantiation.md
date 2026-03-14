---
id: substitution-and-instantiation
title: Substitution and Instantiation in Predicate Logic
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: free-variables-and-bound-variables
  type: hard
builds-toward:
- natural-deduction-fol
- skolem-functions-and-witnesses
tags:
- syntax
- inference
- first-order-logic
stage: formal-systems
status: draft
---

# Substitution and Instantiation in Predicate Logic

## Core Idea
Substitution replaces variables with terms; instantiation substitutes a variable with a constant. Key rule: from ∀x φ(x), we can derive φ(t) for any term t. Capture-avoiding substitution prevents free variables of the substituted term from becoming unintentionally bound.
