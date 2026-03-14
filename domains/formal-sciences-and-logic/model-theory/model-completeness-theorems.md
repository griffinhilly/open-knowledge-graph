---
id: model-completeness-theorems
title: Model Completeness and the Model Completeness Test
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: model-theory-basics
  type: hard
- id: first-order-semantics
  type: hard
- id: complete-first-order-theories
  type: hard
builds-toward:
- quantifier-elimination-decidability
- decidable-theories
tags:
- model-completeness
- universal-formulas
- decidability
stage: advanced
status: draft
---

# Model Completeness and the Model Completeness Test

## Core Idea
A theory T is model-complete if every formula is equivalent to a universal formula, equivalently, if every embedding of one model of T into another model of T is an elementary embedding. Model completeness implies that models embed elementarily into larger models. The model completeness test (Tarski's criterion) provides a decidable way to verify this property.

## How It's Best Learned
Study the MCT and work through examples: algebraically closed fields, real closed fields, and divisible abelian groups. Compare model completeness with completeness and saturation.

## Common Misconceptions
Model completeness is not the same as completeness. A model-complete theory need not be complete. Also, model-completeness does not imply all models are isomorphic.
