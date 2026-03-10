---
id: list-comprehensions
title: List Comprehensions
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: list-operations
  type: hard
- id: for-loops
  type: hard
- id: conditional-statements
  type: soft
builds-toward:
- algorithm-design-basics
tags:
- list comprehensions
- concise iteration
- functional style
- filter
- map
stage: abstract-reasoning
status: draft
---

# List Comprehensions

## Core Idea
A list comprehension creates a new list by applying an expression to each element of an iterable, optionally filtered by a condition, in a single readable line: [f(x) for x in iterable if condition]. They are equivalent to a for loop with an accumulator list but are more concise and often faster. List comprehensions express the transformation declaratively (what the result should be) rather than imperatively (how to build it step by step). They are a widely used Python idiom and appear in similar forms in many modern languages.

## How It's Best Learned
Rewrite existing for-loop accumulation patterns as list comprehensions. Start with simple expressions, then add filtering conditions. Verify output matches the loop version exactly.

## Common Misconceptions
- Writing complex nested comprehensions that sacrifice readability for brevity.
- Confusing list comprehensions (produce a list) with generator expressions (produce a lazy iterator).
- Forgetting that the expression comes before the for clause, unlike a for loop.
