---
id: parameters-and-arguments
title: Function Parameters and Argument Passing
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: function-definition-and-calls
  type: hard
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

## Explainer

You already know how to define and call functions — you can write `def greet():` and invoke it with `greet()`. But functions become truly powerful when they can accept **input** that changes their behavior. Instead of writing a separate function for every greeting, you write `def greet(name):` and pass different names each time. The variable `name` in the function signature is a **parameter** — a placeholder that receives a value when the function is called. The value you pass in — like `greet("Alice")` — is the **argument**. The parameter gets bound to the argument's value at call time, and within the function body, you use the parameter just like any other variable.

Functions can take multiple parameters, separated by commas: `def add(a, b):` defines a function that expects two arguments. When you call `add(3, 7)`, the argument `3` is bound to parameter `a` and `7` is bound to parameter `b`. The order matters — the first argument goes to the first parameter, the second to the second, and so on. This is called **positional argument** passing. Many languages also support **keyword arguments** (or named arguments), where you specify which parameter gets which value explicitly: `add(b=7, a=3)`. This is especially useful when a function has many parameters and you want clarity, or when you want to skip parameters that have default values.

**Default parameter values** let you make some arguments optional. In `def greet(name, greeting="Hello"):`, the second parameter has a default. Calling `greet("Alice")` uses the default greeting; calling `greet("Alice", "Hey")` overrides it. This pattern is ubiquitous — it lets you keep simple calls simple while allowing customization when needed. The parameters with defaults must come after those without, so the function signature reads left-to-right from required to optional.

One subtle but important point is what happens when you modify a parameter inside a function. For simple types like numbers and strings, changing the parameter does not affect the original variable outside the function — the parameter is effectively a local copy. But for mutable objects like lists and dictionaries, the parameter refers to the *same object* in memory. If you call `def append_item(lst): lst.append(42)` with `append_item(my_list)`, `my_list` itself is modified. This is the difference between **pass-by-value** (copying the value) and **pass-by-reference** (sharing the object). Python technically uses "pass-by-object-reference" — the parameter and the argument point to the same object, but reassigning the parameter (`lst = []`) only changes the local variable, not the caller's. Understanding this distinction prevents a whole class of bugs where functions unexpectedly modify — or unexpectedly fail to modify — the data you pass to them.
