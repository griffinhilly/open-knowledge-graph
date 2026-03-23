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
stage: formal-systems
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

## Questions

```yaml
- question: "A function `square(n)` is defined to return `n * n`. What is the value stored in `result` after executing `result = square(3) + 1`?"
  type: multiple-choice
  options:
    - "9"
    - "10"
    - "The code raises an error — you cannot use a function call inside an arithmetic expression"
    - "square(3) — the function call is stored unevaluated"
  answer: 1
  explanation: "A function call that returns a value *becomes* that value in any expression. `square(3)` evaluates to 9, so the expression becomes `9 + 1 = 10`. This is the key insight about return values: they can be used anywhere a value can appear — in assignments, arithmetic expressions, comparisons, or as arguments to other functions. The function call is not a statement that 'does something'; it is an expression that evaluates to a value."

- question: "What happens to code written after a `return` statement in the same function block?"
  type: multiple-choice
  options:
    - "It executes after the returned value has been used by the caller"
    - "It never executes — the `return` statement exits the function immediately"
    - "It executes only if the return value is not None"
    - "It causes a syntax error that prevents the program from running"
  answer: 1
  explanation: "The `return` statement does two things simultaneously: it specifies the value to send back, and it exits the function immediately. Any code after `return` in the same block is unreachable. This is useful for early exits — you can return a result as soon as it's computed without executing the rest of the function. It's also a common source of bugs when programmers accidentally place logic after a return statement, then wonder why it never runs."

- question: "A function call that returns a value can be passed directly as an argument to another function, such as `print(double(5))`, without first storing the returned value in a variable."
  type: true-false
  answer: true
  explanation: "Because a return value *becomes* the value at the call site, it can appear anywhere a value is valid — including as an argument to another function. `print(double(5))` first evaluates `double(5)` to get 10, then passes 10 to `print`. This composability is one of the most powerful features of functions with return values: they can be chained, nested, and plugged into expressions without intermediate variables."

- question: "If a function reaches its end without hitting a `return` statement, it returns 0 by default in most programming languages."
  type: true-false
  answer: false
  explanation: "Most languages return a language-specific 'nothing' value, not 0. Python returns `None`, JavaScript returns `undefined`, and languages like Java and C use `void` return types to indicate no value is returned. Returning 0 would be misleading because 0 is a meaningful integer value that a caller might use in arithmetic. A 'no value' sentinel is semantically distinct from 'the number zero.'"

- question: "What is the difference between a function that *prints* a result and one that *returns* a result, and why does the distinction matter for writing reusable code?"
  type: short-answer
  answer: "A function that prints a result sends it to the screen — the value is consumed immediately and cannot be used elsewhere in the program. A function that returns a result sends the value back to the caller, who can store it, use it in an expression, pass it to another function, or decide not to use it at all. Returning makes a function a reusable computation unit; printing hardwires what happens to the result. Code that returns values composes — you can build larger operations from smaller ones. Code that only prints is inflexible."
  explanation: "This distinction is fundamental to modular design. A `square` function that prints is only useful when you want to print. A `square` function that returns can be used in any context: `area = square(side)`, `if square(n) > 100`, `total = sum(square(x) for x in values)`. Printing is an action with a side effect; returning is producing a value for the caller to use as needed. Separating computation from display is one of the most important patterns in clean code."
```

## Explainer

You already know how to define functions and pass information *into* them using parameters and arguments. **Return values** are the other half of that exchange — they let a function send information *back* to the code that called it. When a function contains a `return` statement followed by an expression, executing that statement immediately exits the function and delivers the computed value to the caller. Think of it like sending a question to someone and getting an answer back: arguments are the question, and the return value is the answer.

Consider a function that doubles a number: `def double(x): return x * 2`. When you write `result = double(5)`, the function receives 5 as the argument, computes `5 * 2`, and returns 10. That returned value is then stored in `result`. The key insight is that the function call `double(5)` *becomes* the value 10 wherever it appears. You can use it in assignments (`result = double(5)`), in expressions (`total = double(5) + 3`), or even as an argument to another function (`print(double(5))`). A function that returns a value is like a custom operator that you can plug into any expression.

The `return` statement does two things simultaneously: it specifies what value to send back, and it **exits the function immediately**. Any code after `return` in the same block will never execute. This is useful for early exits — for instance, a function that checks if a number is negative can `return 0` right away instead of continuing through the rest of the computation. If a function reaches its end without hitting a `return` statement, it returns a default value (typically `None` in Python, `undefined` in JavaScript, or `void` in languages like Java and C).

Understanding return values transforms how you think about program structure. Without returns, functions can only perform actions (print something, modify a global variable). With returns, functions become **reusable computation units** — self-contained pieces that take inputs, compute results, and hand those results back for the caller to use however it needs. This separation between computing a result and deciding what to do with it is one of the most important principles in writing clean, modular code.
