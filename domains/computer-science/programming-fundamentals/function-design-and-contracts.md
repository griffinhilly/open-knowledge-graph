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
