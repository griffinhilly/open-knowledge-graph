---
id: formulas-and-well-formed-expressions
title: Formulas and Well-Formed Expressions
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: terms-and-atomic-formulas
  type: hard
builds-toward:
- structures-and-interpretations
- first-order-logic-syntax
tags:
- syntax
- first-order-logic
stage: formal-systems
status: draft
---

# Formulas and Well-Formed Expressions

## Core Idea
Well-formed formulas are recursively defined: every atomic formula is a wff; if φ and ψ are wffs, then so are ¬φ, (φ ∧ ψ), (φ ∨ ψ), (φ → ψ), ∀x φ, and ∃x φ. This syntax is the foundation for assigning meanings via interpretations in structures.
