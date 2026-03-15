---
id: formula-evaluation-and-truth-tables
title: Formula Evaluation and Truth Tables
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: truth-functions-and-interpretation
  type: hard
- id: propositional-syntax
  type: hard
- id: truth-tables-and-evaluation
  type: soft
- id: boolean-functions
  type: soft
builds-toward:
- logical-equivalence-formulas
tags:
- propositional-logic
- truth-tables
- semantic-analysis
stage: formal-systems
status: draft
---

# Formula Evaluation and Truth Tables

## Core Idea
A truth table systematically lists all possible truth assignments to atomic formulas and computes the resulting truth value of a complex formula. This mechanical method makes it easy to determine whether a formula is always true (tautology), sometimes true (contingent), or never true (contradiction).

## How It's Best Learned
Build truth tables by hand for increasingly complex formulas, working column by column. Use software tools to verify your work and explore patterns in larger formulas.

## Common Misconceptions
- Errors in operator precedence when building truth tables—always clarify parentheses.
- Thinking a truth table proves something rather than just computing truth values for all cases.
