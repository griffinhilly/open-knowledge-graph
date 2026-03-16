---
id: programming-fundamentals-parameters-arguments
title: Parameters and Arguments
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: programming-fundamentals-function-definition
  type: hard
builds-toward:
- programming-fundamentals-variable-scope
tags:
- functions
- parameters
- arguments
stage: abstract-reasoning
status: draft
---

# Parameters and Arguments

## Core Idea
Parameters are variables declared in a function definition; arguments are values passed when calling the function. Parameters act as local variables that receive argument values, allowing functions to operate on different data.

## Explainer

When you learned to define functions, you saw that a function packages a reusable block of code behind a name. But a function that always does exactly the same thing with exactly the same data is limited. **Parameters** are what make functions flexible — they are placeholder variables listed in the function's definition that say "I expect to receive some data here." When you actually call the function and supply specific values, those values are called **arguments**. The parameter is the slot; the argument is what fills it.

Consider a function `def greet(name):` that prints a greeting. Here, `name` is a parameter — a variable that doesn't have a value yet. When you call `greet("Alice")`, the string `"Alice"` is the argument. At the moment of the call, Python creates a local variable called `name` inside the function and assigns it the value `"Alice"`. The function body then uses `name` as if it were any other variable. Call `greet("Bob")` next, and `name` becomes `"Bob"` for that execution. Same function, different data, different results — that's the power of parameterization.

Functions can accept multiple parameters, separated by commas: `def add(a, b):` expects two arguments. The order matters — the first argument fills the first parameter, the second fills the second. Some languages also support **keyword arguments**, where you specify which parameter gets which value by name (`add(b=3, a=7)`), and **default values**, where a parameter gets a fallback if no argument is provided (`def greet(name="world")`). These features give you fine-grained control over how data flows into your functions.

The distinction between parameters and arguments may seem like vocabulary trivia, but it matters when debugging. If a function misbehaves, the first question is: "What arguments did it receive?" Parameters define the function's contract — what it expects. Arguments are what the caller actually delivers. When those don't match (wrong number, wrong type, wrong order), you get errors. Understanding this data-passing mechanism is also the foundation for understanding variable scope, which you'll encounter next: parameters create local variables that exist only inside the function call, isolated from the rest of your program.
