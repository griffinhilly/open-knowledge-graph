---
id: models-and-interpretation-basic
title: Models and Interpretations in First-Order Logic
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: first-order-logic-syntax
  type: hard
- id: first-order-semantics
  type: hard
builds-toward:
- domain-and-structure-fol
tags:
- first-order-logic
- models
- semantics
stage: formal-systems
status: draft
---

# Models and Interpretations in First-Order Logic

## Core Idea
In first-order logic, a model (or interpretation) is a structure consisting of a non-empty domain and an assignment of denotations to each constant symbol, function symbol, and predicate symbol in the language. Models make precise the intuitive notion that a formula can be true or false depending on what world we are describing.

## How It's Best Learned
Start with simple structures like the natural numbers with addition, or small finite domains with basic relations. Verify that the same formula can be true in one model and false in another.

## Common Misconceptions
- Thinking a model must be 'the' intended model rather than one of many possible interpretations.
- Confusing the domain (objects) with the interpretation function (what predicates mean).
