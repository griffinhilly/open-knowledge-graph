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

## Questions

```yaml
- question: "A function compute_tax(amount) prints the tax value inside the function. A developer writes total = amount + compute_tax(amount) expecting total to hold the sum. What will actually happen?"
  type: multiple-choice
  options:
    - "total will hold the correct sum because the printed value is captured automatically"
    - "total will be None (or cause a TypeError) because compute_tax returns nothing, not the tax value"
    - "total will hold just the amount, since print is ignored in arithmetic expressions"
    - "total will hold the printed string concatenated with amount"
  answer: 1
  explanation: "print() displays text for humans — it does not send a value back into the program. A function that only prints has no explicit return, so it returns None. Using None in arithmetic with amount raises a TypeError (or in some languages produces undefined behavior). The fix is to replace print(tax) with return tax, so the caller receives the value it needs."

- question: "Which of the following accurately describes what happens when Python executes a return statement inside a function?"
  type: multiple-choice
  options:
    - "The function displays the value and continues running any remaining statements"
    - "The function pauses execution and waits for the caller to request the value"
    - "The function immediately stops executing and sends the specified value back to the caller"
    - "The function stores the value in a global variable accessible to the caller"
  answer: 2
  explanation: "A return statement does two things simultaneously: it ends the function's execution at that point (no further lines in the function run), and it delivers the value back to the caller. This is why 'unreachable code' warnings appear for statements after a return — they will never execute. The caller receives the value directly and can use it in expressions, assign it to variables, or pass it to other functions."

- question: "A function can contain more than one return statement, and the first one that is reached during execution will end the function."
  type: true-false
  answer: true
  explanation: "Multiple return statements are valid and common — each is an independent exit point. Early returns are a standard pattern: for example, checking for invalid input at the top of a function and returning an error value before reaching the main logic. The function ends at whichever return is executed first during a given call."

- question: "Printing a result inside a function and returning a result from a function are equivalent, because both make the value available to the rest of the program."
  type: true-false
  answer: false
  explanation: "print() sends text to the screen for a human to read — the program itself cannot use that text for computation. A return statement sends the value back into the program's flow, where it can be stored in a variable, passed to another function, or used in an expression. A function that prints its result cannot be composed with other functions; a function that returns its result can. This distinction is fundamental to writing reusable, testable code."

- question: "Why should a function that computes a result return it rather than print it?"
  type: short-answer
  answer: "Returning a value keeps the caller in control of what to do with the result — store it, pass it to another function, compare it to a threshold, or print it if desired. Printing inside the function makes the decision for the caller and makes the function non-composable: its output cannot be fed into other computations. A function that returns is testable and reusable; a function that only prints is a dead end in the program's data flow."
  explanation: "The composability argument is the core insight. If circle_area() returns the area, you can write cylinder_volume = circle_area(r) * height. If it only prints, you cannot. Printing is a side effect for human consumption; returning is the mechanism by which functions contribute to program logic. Functions that compute should return — functions that exist solely for side effects (writing files, sending data) may legitimately return nothing."
```

## Explainer

You already know that functions accept inputs through parameters. **Return values** are the other half of that contract: they let a function send a result back to the code that called it. When a function hits a `return` statement, two things happen simultaneously — the function stops executing, and the specified value is passed back to the caller. The caller can then store that value in a variable, pass it to another function, or use it in an expression. This is what makes functions composable: the output of one becomes the input of another, like snapping together building blocks.

The most important distinction to internalize early is **returning versus printing**. A `print` statement displays text on the screen for a human to read, but the program itself cannot use that displayed text for anything. A `return` statement sends a value back into the program's flow where other code can use it. Consider a function that calculates the area of a circle. If it prints the result, you can see the number, but you cannot use it to calculate the volume of a cylinder. If it returns the result, you can feed that value into a volume calculation, store it in a database, or compare it to a threshold — whatever the program needs. Printing is for humans; returning is for code.

A function that does not explicitly return a value still returns something — in Python it returns `None`, in Java a `void` function returns nothing at all. This is appropriate for functions whose purpose is a **side effect**: printing to the screen, writing to a file, or modifying a data structure in place. But functions that compute a result should almost always return it rather than printing it, because returning preserves the caller's freedom to decide what to do with the result.

One subtlety worth noting: a function can contain multiple `return` statements. Each one is an exit point — the first `return` that executes ends the function. This is useful for **early returns** that handle special cases. For example, a function that divides two numbers might return an error value immediately if the divisor is zero, rather than proceeding through the normal computation. Any code after a `return` statement in the same block will never execute, which is why your editor may warn you about "unreachable code." Understanding this control-flow behavior of `return` — that it is both a value-delivery mechanism and a function-exit mechanism — sets the foundation for recursion and error handling patterns you will encounter soon.
