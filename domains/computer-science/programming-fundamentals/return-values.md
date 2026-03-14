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
