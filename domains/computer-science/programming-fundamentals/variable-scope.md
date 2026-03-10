---
id: variable-scope
title: Variable Scope
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: functions-defining-calling
  type: hard
- id: return-values
  type: soft
builds-toward:
- recursion-basics
- intro-to-classes
tags:
- scope
- local
- global
- namespace
- encapsulation
stage: abstract-reasoning
status: draft
---

# Variable Scope

## Core Idea
Scope defines where in a program a variable is visible and accessible. Local variables exist only inside the function where they are created; global variables are accessible throughout the program. Each function call creates its own local scope (a new set of variable bindings), which is discarded when the function returns. Limiting the scope of variables reduces unintended interactions between parts of a program and makes code easier to reason about.

## How It's Best Learned
Write functions that use the same variable name as a global and observe which takes precedence. Use a debugger or print statements to show variable values at different points in the call stack.

## Common Misconceptions
- Assuming a variable created inside a function is accessible outside it.
- Using global variables when a parameter would be cleaner and safer.
- Confusing the value of a variable at definition time with its value at call time.
