---
id: skolemization-and-witnesses
title: Skolemization and Witness Functions
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: prenex-normal-form
  type: hard
- id: skolem-functions-and-witnesses
  type: soft
builds-toward:
- herbrand-universe-and-base
- clausal-form-conversion
tags:
- first-order-logic
- skolemization
- automated-reasoning
stage: formal-systems
status: draft
---

# Skolemization and Witness Functions

## Core Idea
Skolemization is the process of replacing existential quantifiers with function symbols (Skolem functions) that witness the existence claims. When a formula ∃x φ(x) is true, we can replace it with φ(f(y₁,...,yₙ)) where f is a new function and y₁,...,yₙ are universally quantified variables. This transformation preserves satisfiability and is crucial for converting formulas into a form suitable for automated reasoning.
