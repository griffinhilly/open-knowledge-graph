---
id: functions-defining-calling
title: Defining and Calling Functions
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: variables-and-assignment
  type: hard
- id: conditional-statements
  type: soft
builds-toward:
- parameters-and-arguments
- return-values
- variable-scope
- recursion-basics
- intro-to-classes
tags:
- functions
- def
- call
- abstraction
- modularity
stage: abstract-reasoning
status: validated
---

# Defining and Calling Functions

## Core Idea
A function is a named, reusable block of code that performs a specific task. Defining a function (using def, function, or similar keywords) specifies what the function does; calling it by name executes that code. Functions promote abstraction by hiding implementation details behind a name, and modularity by separating a program into independent, testable units. Well-named functions make code read like a description of what it does rather than how.

## How It's Best Learned
Refactor a long script into smaller functions, one task each. Write each function before calling it. Practice reading function signatures to understand what a function expects and produces.

## Common Misconceptions
- Defining and calling are not the same — a function must be called to run.
- Thinking a function runs when it is defined.
- Placing the function call before the definition in languages that require declaration order.
