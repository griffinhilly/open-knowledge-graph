---
id: working-with-numbers-integers-floats
title: 'Working with Numbers: Integers and Floats'
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: primitive-types-integers-floats-strings
  type: hard
builds-toward:
- arithmetic-operators-and-precedence
- type-conversion-intro
tags:
- arithmetic
- numbers
- types
stage: abstract-reasoning
status: draft
---

# Working with Numbers: Integers and Floats

## Core Idea
Integer arithmetic is exact but can overflow; floating-point arithmetic is approximate and can lose precision. Understanding integer division (7/2 = 3 in many languages) and floating-point errors prevents logic bugs. Different languages handle these differently.

## How It's Best Learned
Perform calculations by hand, predict the result, then run code and compare; test edge cases like division by zero or very large numbers.

## Common Misconceptions
That division always returns a decimal; that floating-point math is exact (0.1 + 0.2 may not equal 0.3); that integers overflow silently (behavior varies by language).
