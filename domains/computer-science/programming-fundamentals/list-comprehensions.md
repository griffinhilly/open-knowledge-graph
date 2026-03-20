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
- id: nested-loops
  type: soft
builds-toward:
- algorithm-design-basics
tags:
- list comprehensions
- concise iteration
- functional style
- filter
- map
stage: formal-systems
status: validated
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

## Explainer

You are comfortable with for loops and list operations — you know how to iterate through a collection and build up a new list by appending to it inside a loop. **List comprehensions** are a more concise syntax for exactly that pattern, and once you see the correspondence, they become a natural part of how you write Python.

Consider a common pattern: starting with an empty list, looping through some items, transforming each one, and appending the result. For example, to square every number in a list: `squares = []`, then `for x in numbers: squares.append(x ** 2)`. The list comprehension equivalent is `squares = [x ** 2 for x in numbers]`. The expression before `for` (here `x ** 2`) is the transformation applied to each element. The `for x in numbers` part is the iteration. The result is a new list containing every transformed value. The logic is identical to the loop — the comprehension is just a more compact way to express it.

You can also add a **filter** with an `if` clause. To get only the even squares: `even_squares = [x ** 2 for x in numbers if x % 2 == 0]`. This is equivalent to putting an if-statement inside the loop before the append. The reading order is: "give me `x ** 2` for each `x` in `numbers`, but only if `x` is even." You can also nest comprehensions for working with multi-dimensional data — `[cell for row in matrix for cell in row]` flattens a list of lists — though nested comprehensions should be used sparingly because they become hard to read quickly.

The advantage of comprehensions is not just brevity — they also signal **intent**. When a reader sees a list comprehension, they immediately know the result is a new list derived from an existing iterable. A for loop could be doing anything: printing, modifying global state, calling APIs. A comprehension declares "I am building a list by transforming data," which makes the code's purpose clear at a glance. As a rule of thumb, if the transformation and filter fit comfortably on one line and are easy to read, use a comprehension. If the logic requires multiple statements, intermediate variables, or complex branching, stick with a regular loop. The goal is always readability — comprehensions are a tool for clarity, not a puzzle to see how much logic you can compress into a single line.
