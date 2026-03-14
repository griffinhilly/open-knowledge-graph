---
id: return-values-and-function-returns
title: Return Values and Function Returns
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: return-values
  type: hard
builds-toward:
- function-design-and-contracts
tags:
- functions
- return
- values
stage: abstract-reasoning
status: draft
---

# Return Values and Function Returns

## Core Idea
Functions return a single value (or none) to the caller. The return statement ends the function immediately. Return type determines what kind of value the function produces. Understanding return values is essential for composing functions.

## How It's Best Learned
Write functions that return different types; trace execution to see where the return value is used; test functions that return early with conditional returns.

## Common Misconceptions
That print and return are the same (print displays, return sends data back); that functions can return multiple values as separate returns (only the first executes); that a function without explicit return returns null/undefined in all languages (some return 0 or void).
