---
id: return-values
title: Return Values
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: parameters-and-arguments
  type: hard
builds-toward:
- variable-scope
- recursion-basics
- error-handling-exceptions
tags:
- return
- output
- functions
- None
- void
stage: abstract-reasoning
status: validated
---

# Return Values

## Core Idea
A return statement ends a function's execution and sends a value back to the caller. Functions that compute results should return those results rather than printing them, making them composable — the output of one function can be passed as input to another. A function without an explicit return statement returns None (or void), which is appropriate for functions called solely for their side effects. Understanding return values is key to writing reusable, testable functions.

## How It's Best Learned
Write mathematical functions (e.g., area of a circle) that return a value, then use the returned value in larger expressions. Compare a version that prints vs. one that returns and observe which composes more naturally.

## Common Misconceptions
- Printing a result inside the function and thinking that's the same as returning it.
- Not capturing the return value at the call site and then wondering why the variable is None.
- Thinking return can only appear once at the end of a function.

## Explainer

You already know that functions accept inputs through parameters. **Return values** are the other half of that contract: they let a function send a result back to the code that called it. When a function hits a `return` statement, two things happen simultaneously — the function stops executing, and the specified value is passed back to the caller. The caller can then store that value in a variable, pass it to another function, or use it in an expression. This is what makes functions composable: the output of one becomes the input of another, like snapping together building blocks.

The most important distinction to internalize early is **returning versus printing**. A `print` statement displays text on the screen for a human to read, but the program itself cannot use that displayed text for anything. A `return` statement sends a value back into the program's flow where other code can use it. Consider a function that calculates the area of a circle. If it prints the result, you can see the number, but you cannot use it to calculate the volume of a cylinder. If it returns the result, you can feed that value into a volume calculation, store it in a database, or compare it to a threshold — whatever the program needs. Printing is for humans; returning is for code.

A function that does not explicitly return a value still returns something — in Python it returns `None`, in Java a `void` function returns nothing at all. This is appropriate for functions whose purpose is a **side effect**: printing to the screen, writing to a file, or modifying a data structure in place. But functions that compute a result should almost always return it rather than printing it, because returning preserves the caller's freedom to decide what to do with the result.

One subtlety worth noting: a function can contain multiple `return` statements. Each one is an exit point — the first `return` that executes ends the function. This is useful for **early returns** that handle special cases. For example, a function that divides two numbers might return an error value immediately if the divisor is zero, rather than proceeding through the normal computation. Any code after a `return` statement in the same block will never execute, which is why your editor may warn you about "unreachable code." Understanding this control-flow behavior of `return` — that it is both a value-delivery mechanism and a function-exit mechanism — sets the foundation for recursion and error handling patterns you will encounter soon.
