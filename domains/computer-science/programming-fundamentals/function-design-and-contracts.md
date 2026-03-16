---
id: function-design-and-contracts
title: Function Design and Contracts
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: functions-decomposing-problems
  type: hard
- id: return-values-and-function-returns
  type: hard
builds-toward:
- recursion-thinking-recursively
- testing-and-validation-basics
tags:
- functions
- design
- contracts
stage: abstract-reasoning
status: draft
---

# Function Design and Contracts

## Core Idea
A function contract specifies what the function promises: input types and meanings, output type and meaning, preconditions (what must be true before calling), postconditions (what's true after). A well-documented contract makes functions easier to use and test.

## How It's Best Learned
Document existing functions with contracts; test functions at boundary conditions specified in the contract; deliberately violate contracts to see failures.

## Common Misconceptions
That contracts are optional documentation; that a function should work with any input (preconditions define valid inputs); that contracts are too formal for simple code (they scale from simple to complex).

## Explainer

You already know how to decompose a problem into functions and how to return values from them. But consider this: you write a function `calculate_average(numbers)` that divides the sum by the length of the list. A colleague calls it with an empty list. The program crashes with a division-by-zero error. Whose fault is it — yours for not handling empty lists, or your colleague's for passing one? Without a clear agreement, this question has no answer. A **function contract** is that agreement, made explicit.

A contract has two sides. **Preconditions** state what must be true *before* the function is called — the caller's obligations. For `calculate_average`, a precondition might be "the list must contain at least one number." **Postconditions** state what the function guarantees *after* it returns — the function's obligations. Here, the postcondition might be "returns a float equal to the arithmetic mean of all elements in the list." If the caller violates a precondition (passing an empty list), the function is not at fault for misbehaving. If the caller meets all preconditions, the function *must* deliver on its postconditions.

This framing transforms how you think about error handling and testing. Instead of writing defensive code that tries to handle every conceivable bad input, you define the boundary clearly: "I handle *this*; you are responsible for *that*." Testing becomes systematic — you write tests that exercise the postconditions when preconditions are met, and you write tests that verify the function rejects or signals an error when preconditions are violated. Boundary values are especially important: if the precondition says "list must have at least one element," test with exactly one element (the boundary) and with an empty list (the violation).

Well-designed contracts also guide **function decomposition**. If you find it hard to state a function's contract concisely — if the preconditions are tangled or the postconditions have many special cases — that is a signal the function is doing too much. Break it into smaller functions, each with a clean, simple contract. A function with a clear contract is a function that is easy to understand in isolation, easy to test, and easy to compose with other functions. The contract is not bureaucratic overhead — it is the specification that makes reliable software possible.
