---
id: parameters-and-arguments
title: Parameters and Arguments
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: functions-defining-calling
  type: hard
builds-toward:
- return-values
- variable-scope
- recursion-basics
tags:
- parameters
- arguments
- input
- function signature
- default values
stage: abstract-reasoning
status: validated
---

# Parameters and Arguments

## Core Idea
Parameters are the named placeholders listed in a function's definition; arguments are the actual values passed when the function is called. Parameters allow functions to operate on different data each time they are called, making them general and reusable. Many languages support default parameter values (used when no argument is provided) and keyword arguments (passed by name rather than position). The parameter list defines the function's interface.

## How It's Best Learned
Write functions with multiple parameters and call them with different arguments. Experiment with default values and keyword arguments. Deliberately pass the wrong number of arguments to understand error messages.

## Common Misconceptions
- Confusing parameters (definition) with arguments (call site).
- Assuming modifying a parameter inside a function changes the original variable (depends on pass-by-value vs. pass-by-reference semantics).
- Forgetting that positional arguments must appear in the declared order.
