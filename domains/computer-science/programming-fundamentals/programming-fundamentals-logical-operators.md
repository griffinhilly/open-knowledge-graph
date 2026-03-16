---
id: programming-fundamentals-logical-operators
title: Logical Operators
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: programming-fundamentals-comparison-operators
  type: hard
builds-toward:
- programming-fundamentals-operator-precedence
- programming-fundamentals-if-else-statements
tags:
- operators
- logic
- boolean
stage: abstract-reasoning
status: draft
---

# Logical Operators

## Core Idea
Logical operators (and, or, not) combine or modify boolean values to form compound conditions. AND returns true only if both operands are true; OR returns true if at least one is true; NOT inverts the boolean value.

## Explainer

You already know how comparison operators produce boolean values — expressions like `x > 5` or `name == "Alice"` evaluate to either true or false. But real programs rarely depend on a single condition. You might need to check whether a user is logged in *and* has admin privileges, or whether a temperature is below freezing *or* above boiling. **Logical operators** let you combine multiple boolean expressions into compound conditions.

The three fundamental logical operators map directly to everyday English reasoning. **AND** (written `and` in Python, `&&` in many other languages) requires *both* sides to be true. The expression `age >= 18 and has_ticket` is true only when someone is both old enough and holds a ticket — if either condition is false, the whole expression is false. **OR** (written `or` or `||`) requires *at least one* side to be true. The expression `is_student or is_senior` grants a discount if either condition holds, or if both do. **NOT** (written `not` or `!`) flips a single boolean value: `not is_locked` is true when `is_locked` is false, and vice versa.

A useful mental model is to think of AND as a strict gatekeeper — everyone must pass — and OR as a lenient one — anyone can pass. NOT is simply a reversal. You can chain these operators to build complex conditions: `(temperature > 100 or pressure > 50) and not emergency_shutdown`. Parentheses control grouping, just like in arithmetic. Without parentheses, most languages evaluate NOT first, then AND, then OR, but explicit parentheses make your intent clear and prevent subtle bugs.

One practical behavior worth knowing early is **short-circuit evaluation**. When evaluating `A and B`, if `A` is false, the language skips evaluating `B` entirely — the result is already determined to be false regardless of `B`. Similarly, `A or B` skips `B` if `A` is true. This is not just an optimization; it lets you write guards like `x != 0 and 100 / x > 10`, where the division only happens when `x` is nonzero. Understanding short-circuiting turns logical operators from abstract logic into a practical programming tool.
