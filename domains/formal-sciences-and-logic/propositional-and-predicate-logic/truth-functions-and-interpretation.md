---
id: truth-functions-and-interpretation
title: Truth Functions and Interpretation
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: propositional-connectives
  type: hard
- id: propositional-semantics
  type: hard
builds-toward:
- formula-evaluation-and-truth-tables
tags:
- propositional-logic
- semantics
- truth-functions
stage: formal-systems
status: draft
---

# Truth Functions and Interpretation

## Core Idea
In propositional logic, each connective (AND, OR, NOT, IMPLIES) defines a truth function that determines the truth value of a complex formula based on the truth values of its parts. An interpretation assigns truth values to atomic propositions, and these combine via truth functions to determine the truth value of any formula.

## How It's Best Learned
Start with small formulas like (A ∧ B) and work through how their truth values depend on A and B. Visualize truth functions with simple diagrams before moving to complex nested formulas.

## Common Misconceptions
- Thinking truth functions are just names of connectives rather than actual functions mapping truth values to truth values.
- Confusing the truth value of a formula under one interpretation with the formula's inherent truth value.
