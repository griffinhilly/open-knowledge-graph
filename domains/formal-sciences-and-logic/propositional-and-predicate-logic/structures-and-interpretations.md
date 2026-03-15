---
id: structures-and-interpretations
title: Structures and Interpretations
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: formulas-and-well-formed-expressions
  type: hard
- id: set-membership-and-notation
  type: soft
builds-toward:
- satisfaction-in-structures
- model-interpretation-and-satisfaction
tags:
- semantics
- models
- first-order-logic
stage: formal-systems
status: draft
---

# Structures and Interpretations

## Core Idea
A structure M consists of a non-empty domain D and an interpretation function I assigning to each constant a member of D, to each n-ary function symbol a function D^n → D, and to each n-ary predicate a relation on D^n. An interpretation specifies what symbols mean. The same formula can be true in some structures and false in others.

## How It's Best Learned
Construct small explicit models with finite domains. Evaluate formulas in them. Observe how changing a predicate's interpretation changes which formulas are satisfied.
