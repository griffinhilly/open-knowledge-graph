---
id: truth-tables
title: Truth Tables
domain: mathematics
course: methods-of-proof
prerequisites:
- id: statements-and-logical-connectives
  type: hard
builds-toward:
- logical-equivalences
- conditional-and-biconditional
tags:
- truth-tables
- logic
- tautology
- contradiction
- Boolean
stage: formal-systems
status: validated
---

# Truth Tables

## Core Idea
A truth table systematically lists every possible combination of truth values for the component statements in a compound expression and computes the resulting truth value for the whole. For n atomic statements, there are 2ⁿ rows. Truth tables are the definitive mechanical method for determining whether a compound statement is always true (a tautology), always false (a contradiction), or neither (a contingency).

## How It's Best Learned
Practice constructing truth tables column by column, left to right, building up subexpressions before evaluating the full formula. Verify familiar identities like De Morgan's laws by table. Move toward recognizing common patterns (e.g., P → Q vs. ¬P ∨ Q) without always needing to recompute.

## Common Misconceptions
- Forgetting to enumerate all 2ⁿ rows, especially when n = 3 or more.
- Confusing the order of operations: negation binds tighter than ∧, which binds tighter than ∨, which binds tighter than →.
- Assuming that a formula being true in many cases means it is a tautology — every row must be checked.
