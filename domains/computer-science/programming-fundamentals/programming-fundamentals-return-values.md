---
id: programming-fundamentals-return-values
title: Function Return Values
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: programming-fundamentals-function-definition
  type: hard
builds-toward:
- programming-fundamentals-variable-scope
tags:
- functions
- return
- results
stage: abstract-reasoning
status: draft
---

# Function Return Values

## Core Idea
A function returns a value using the return statement, which exits the function and provides a result to the caller. The return type specifies what kind of value is returned.

## Explainer

You already know how to define and call functions — you can package a block of code, give it a name, and invoke it from elsewhere. But so far, a function is like sending someone on an errand without asking them to bring anything back. A **return value** is what the function brings back to the caller. When a function executes a `return` statement, two things happen simultaneously: the function stops executing (no code after the return runs), and the specified value is sent back to wherever the function was called.

The key insight is that a function call with a return value *becomes* that value in the calling code. If you write `result = square(5)`, the call `square(5)` is replaced by whatever the function returns — in this case, 25. This means function calls can appear anywhere a value can: inside arithmetic expressions (`square(3) + square(4)`), as arguments to other functions (`print(square(5))`), or in conditions (`if (is_even(n))`). Return values are what make functions composable — you can chain them, nest them, and build complex computations from simple building blocks.

A function without a return statement (or with a bare `return` and no value) returns a special "nothing" value — `None` in Python, `undefined` in JavaScript, `void` in C-family languages. This distinction matters: a function that *does* something (prints to the screen, modifies a file) versus a function that *computes* something (calculates a result and returns it) are fundamentally different in how you use them. Functions that return values are easier to test, reuse, and compose because their output is a value you can inspect, store, and pass around rather than a side effect you have to observe indirectly.

One important behavior to internalize: **return exits the function immediately**. Any code after a return statement in the same block is unreachable — it will never execute. This is actually useful: you can use early returns to handle special cases at the top of a function and keep the main logic unindented. For example, checking `if (n < 0) return -1` at the start of a function lets you handle the error case and move on, rather than wrapping the entire function body in an else block.
