---
id: parameters-and-arguments
title: Function Parameters and Argument Passing
domain: computer-science
course: programming-fundamentals
prerequisites:
- function-definition-and-calls
builds-toward:
- return-values
- variable-scope
tags:
- functions
- parameters
- arguments
stage: abstract-reasoning
status: draft
---

# Function Parameters and Argument Passing

## Core Idea
Parameters are variables declared in a function's signature; arguments are values passed to a function. When a function is called, arguments are bound to parameters. This mechanism allows functions to operate on different data without rewriting code.

## How It's Best Learned
Write functions with one, two, and many parameters. Call functions with different argument values and observe parameter binding.

## Common Misconceptions
- Parameters and arguments are the same (parameters are formal variables; arguments are actual values).
- Changing a parameter inside a function always affects the original variable (this depends on pass-by-value vs. pass-by-reference).
