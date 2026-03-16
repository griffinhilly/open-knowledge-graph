---
id: return-values-and-results
title: Return Statements and Return Values
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: parameters-and-arguments
  type: hard
builds-toward:
- variable-scope
tags:
- functions
- return
- results
stage: abstract-reasoning
status: draft
---

# Return Statements and Return Values

## Core Idea
A function may return a value using the return statement. The return value is the result of the function's computation. Functions without an explicit return statement return a default value (void in many languages). Return values allow functions to produce results usable elsewhere.

## How It's Best Learned
Write functions that compute and return values. Use return values in expressions and assignments.

## Common Misconceptions
- A function can return multiple values (it returns one value; use data structures to return multiple results).
- Return executes immediately (the function exits as soon as return is encountered).

## Explainer

You already know how to define functions and pass information *into* them using parameters and arguments. **Return values** are the other half of that exchange — they let a function send information *back* to the code that called it. When a function contains a `return` statement followed by an expression, executing that statement immediately exits the function and delivers the computed value to the caller. Think of it like sending a question to someone and getting an answer back: arguments are the question, and the return value is the answer.

Consider a function that doubles a number: `def double(x): return x * 2`. When you write `result = double(5)`, the function receives 5 as the argument, computes `5 * 2`, and returns 10. That returned value is then stored in `result`. The key insight is that the function call `double(5)` *becomes* the value 10 wherever it appears. You can use it in assignments (`result = double(5)`), in expressions (`total = double(5) + 3`), or even as an argument to another function (`print(double(5))`). A function that returns a value is like a custom operator that you can plug into any expression.

The `return` statement does two things simultaneously: it specifies what value to send back, and it **exits the function immediately**. Any code after `return` in the same block will never execute. This is useful for early exits — for instance, a function that checks if a number is negative can `return 0` right away instead of continuing through the rest of the computation. If a function reaches its end without hitting a `return` statement, it returns a default value (typically `None` in Python, `undefined` in JavaScript, or `void` in languages like Java and C).

Understanding return values transforms how you think about program structure. Without returns, functions can only perform actions (print something, modify a global variable). With returns, functions become **reusable computation units** — self-contained pieces that take inputs, compute results, and hand those results back for the caller to use however it needs. This separation between computing a result and deciding what to do with it is one of the most important principles in writing clean, modular code.
