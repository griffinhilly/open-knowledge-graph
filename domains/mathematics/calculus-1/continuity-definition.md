---
id: continuity-definition
title: Continuity Definition
domain: mathematics
course: calculus-1
prerequisites:
- id: limit-definition-intuitive
  type: hard
- id: one-sided-limits
  type: hard
- id: limit-laws
  type: soft
- id: piecewise-functions-graphing
  type: soft
builds-toward:
- intermediate-value-theorem
- limit-definition-of-derivative
tags:
- continuity
- limits
- functions
stage: formal-systems
status: validated
---
# Continuity Definition

## Core Idea
A function f is continuous at x = a if three conditions hold: f(a) is defined, lim(x->a) f(x) exists, and lim(x->a) f(x) = f(a). Informally, the graph has no break, jump, or hole at a. Continuity is important because continuous functions behave predictably: they satisfy the Intermediate Value Theorem, and most derivative and integral theorems require continuity.

## How It's Best Learned
Classify discontinuities as removable (hole), jump, or infinite (vertical asymptote) with examples of each. Practice checking the three conditions at specific points. Identify which standard functions are continuous on their domains (polynomials, rationals, trig, exponentials, logarithms).

## Common Misconceptions
- Believing a function is continuous just because it is defined at a (the limit must also match).
- Thinking continuity requires a formula (piecewise functions can be continuous).
- Assuming discontinuities are always obvious from the formula.
