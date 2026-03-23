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
stage: formal-systems
status: draft
---

# Function Return Values

## Core Idea
A function returns a value using the return statement, which exits the function and provides a result to the caller. The return type specifies what kind of value is returned.

## Questions

```yaml
- question: "A student writes a function that prints the result of a calculation but has no return statement. They then write: result = calculate(10). What will the variable result contain?"
  type: multiple-choice
  options:
    - "The calculated value, because the function computed it"
    - "A string representation of the printed output"
    - "A special 'nothing' value (None in Python, undefined in JavaScript) because the function has no return statement"
    - "An error — assigning from a function with no return is not allowed"
  answer: 2
  explanation: "A function without a return statement returns a special 'nothing' value automatically. The variable result is assigned that nothing value, not the computed value that was printed. This is a fundamental distinction: printing is a side effect that sends output to the screen but does not produce a value for the calling code to use. To use a computed value outside the function, you must return it. This is why functions that compute should return and functions that do something are used differently."

- question: "Which of the following correctly uses a function's return value, and which demonstrates the key property that makes return values powerful?"
  type: multiple-choice
  options:
    - "square(5) — calling the function; the result is computed but discarded"
    - "print(square(5)) — the return value of square becomes the argument to print, showing that returned values can appear anywhere a value can"
    - "square(5) = 25 — storing the result back into the function call"
    - "return = square(5) — explicitly capturing the return value"
  answer: 1
  explanation: "Option B demonstrates the key insight: a function call with a return value *becomes* that value in the calling context. This means function calls can appear anywhere a value can — as arguments to other functions (print(square(5))), inside expressions (square(3) + square(4)), or in conditions (if is_even(n)). Option A is technically valid but the value is immediately thrown away. Options C and D are not valid syntax."

- question: "In the expression x = double(4) + double(3), the two function calls appear inside an arithmetic expression. This is valid because each call becomes its return value during evaluation."
  type: true-false
  answer: true
  explanation: "This is exactly the composability that return values enable. double(4) evaluates to 8 and double(3) evaluates to 6 before the addition is performed, so x = 8 + 6 = 14. Return values integrate seamlessly into any expression context — arithmetic, boolean, function arguments — making functions interchangeable with literal values wherever values are expected."

- question: "If a return statement appears in the middle of a function, any code that follows it in the same block will still execute as long as it is at the correct indentation level."
  type: true-false
  answer: false
  explanation: "return exits the function immediately and unconditionally. Any code after a return in the same block is unreachable and will never execute, regardless of indentation. This behavior is actually useful: early returns let you handle special cases at the top of a function without wrapping the rest of the body in an else block. But it also means you must be deliberate about return placement — accidentally returning early will skip code you intended to run."

- question: "Explain what it means for a function call to 'become' its return value. How does this property allow functions to be composed and chained together?"
  type: short-answer
  answer: "When a function returns a value, the function call expression is replaced by that value in the calling context. For example, square(5) evaluates to 25, so print(square(5)) is equivalent to print(25). This 'substitution' property means you can nest function calls: sqrt(square(3) + square(4)) computes each inner call, substitutes the results, then passes them to sqrt. Functions become building blocks that can be freely combined because each one produces a value that another can consume — the output of one function can be the input of another."
  explanation: "This composability is the core power of return values and distinguishes them from side effects. Side effects (like printing) are not composable — you can't use the screen output of one print as the input to another function. Return values are composable because they are values, and values can always be passed around. This is why functional programming principles — and good software design generally — favor functions that return values over functions that produce side effects."
```

## Explainer

You already know how to define and call functions — you can package a block of code, give it a name, and invoke it from elsewhere. But so far, a function is like sending someone on an errand without asking them to bring anything back. A **return value** is what the function brings back to the caller. When a function executes a `return` statement, two things happen simultaneously: the function stops executing (no code after the return runs), and the specified value is sent back to wherever the function was called.

The key insight is that a function call with a return value *becomes* that value in the calling code. If you write `result = square(5)`, the call `square(5)` is replaced by whatever the function returns — in this case, 25. This means function calls can appear anywhere a value can: inside arithmetic expressions (`square(3) + square(4)`), as arguments to other functions (`print(square(5))`), or in conditions (`if (is_even(n))`). Return values are what make functions composable — you can chain them, nest them, and build complex computations from simple building blocks.

A function without a return statement (or with a bare `return` and no value) returns a special "nothing" value — `None` in Python, `undefined` in JavaScript, `void` in C-family languages. This distinction matters: a function that *does* something (prints to the screen, modifies a file) versus a function that *computes* something (calculates a result and returns it) are fundamentally different in how you use them. Functions that return values are easier to test, reuse, and compose because their output is a value you can inspect, store, and pass around rather than a side effect you have to observe indirectly.

One important behavior to internalize: **return exits the function immediately**. Any code after a return statement in the same block is unreachable — it will never execute. This is actually useful: you can use early returns to handle special cases at the top of a function and keep the main logic unindented. For example, checking `if (n < 0) return -1` at the start of a function lets you handle the error case and move on, rather than wrapping the entire function body in an else block.
