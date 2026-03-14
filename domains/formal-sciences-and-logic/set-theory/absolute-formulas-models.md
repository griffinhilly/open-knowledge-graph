---
id: absolute-formulas-models
title: Absolute Formulas and Model-Theoretic Absoluteness
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: model-theory-basics
  type: hard
- id: cumulative-hierarchy-ranks
  type: soft
builds-toward:
- elementary-submodels-zfc
- reflection-principles-zfc
tags:
- absoluteness
- models
- inner-models
- formulas
stage: formal-systems
status: draft
---

# Absolute Formulas and Model-Theoretic Absoluteness

## Core Idea
A formula φ is absolute for a model M if M ⊨ φ(x) holds if and only if V ⊨ φ(x) holds, for parameters x in M. Absolute formulas preserve truth across models and meta-models. Many core set-theoretic notions (∈, ⊆, ordinal, etc.) are absolute, but others (cardinality, measurability) are not. Absoluteness is crucial for inner-model constructions.

## How It's Best Learned
Verify that 'x is an ordinal' is absolute: check that L and V agree on which sets are ordinals. Show that 'κ is measurable' is NOT absolute (measurability can differ between models). Use downward absoluteness to prove properties are preserved by inner models.

## Common Misconceptions
- Confusing absoluteness with truth; a formula can be absolute yet false in both models.
- Assuming all mathematical notions are absolute (cardinality and measurability are examples of non-absolute notions).
