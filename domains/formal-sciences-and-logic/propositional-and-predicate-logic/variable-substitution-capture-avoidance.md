---
id: variable-substitution-capture-avoidance
title: Variable Substitution and Capture-Avoidance in First-Order Logic
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: term-and-atom-fol
  type: hard
- id: open-and-closed-formulas-fol
  type: hard
- id: variable-binding-and-scope
  type: hard
builds-toward:
- quantifier-instantiation-rules
- proof-strategies-natural-deduction
tags:
- first-order-logic
- substitution
- variable-capture
- free-variables
stage: formal-systems
status: draft
---

# Variable Substitution and Capture-Avoidance in First-Order Logic

## Core Idea
Variable substitution in first-order logic is the operation of replacing free occurrences of a variable x in a formula φ with a term t, written φ[t/x]. Capture-avoidance is the critical constraint: if t contains variables, those variables must not become bound by quantifiers in φ. For example, substituting y for x in ∃y P(x, y) cannot naively give ∃y P(y, y) because y in t becomes captured. Proper substitution requires renaming bound variables in φ to avoid this. This technical detail is crucial for the correctness of proof rules and model-theoretic arguments.

## How It's Best Learned
Practice substitution on simple formulas, identifying when capture would occur. Understand that renaming bound variables preserves logical equivalence and allows safe substitution. Use concrete examples where capture-avoidance is essential (e.g., universal instantiation in proofs).

## Common Misconceptions
- Ignoring variable capture and applying substitution naively (leading to incorrect formulas).
- Thinking renaming bound variables changes the formula's meaning (it doesn't — α-equivalence preserves meaning).
- Assuming substitution of a ground term (no variables) always avoids capture (it does, which is why ground instances are often used in proofs).
