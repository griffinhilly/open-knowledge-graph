---
id: boolean-logic-programming
title: Boolean Logic in Programming
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: conditional-statements
  type: hard
- id: boolean-algebra
  type: soft
- id: truth-tables
  type: soft
builds-toward:
- while-loops
- loop-control-statements
tags:
- boolean
- and
- or
- not
- truth tables
- compound conditions
stage: abstract-reasoning
status: validated
---

# Boolean Logic in Programming

## Core Idea
Boolean logic governs how conditions are combined in programs using the operators and, or, and not. A compound condition like (x > 0 and x < 10) is only true when both sub-conditions hold. Short-circuit evaluation means that and stops at the first false operand and or stops at the first true operand, which affects both performance and behavior when sub-expressions have side effects. De Morgan's laws allow equivalent reformulation of compound negations.

## How It's Best Learned
Build truth tables for compound conditions by hand. Write conditions both ways (e.g., not (a and b) vs. (not a) or (not b)) and verify they produce identical results.

## Common Misconceptions
- Writing x > 0 and < 10 instead of x > 0 and x < 10.
- Assuming or is exclusive (it is inclusive in most languages).
- Ignoring short-circuit behavior when a sub-expression has side effects.
