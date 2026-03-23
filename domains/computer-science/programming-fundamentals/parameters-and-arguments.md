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
stage: formal-systems
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

## Questions

```yaml
- question: "In Python, consider: `def double(x): x = x * 2`. After running `n = 5; double(n)`, what is the value of n?"
  type: multiple-choice
  options:
    - "10 — the function modified x, and x was bound to n"
    - "5 — x is a local variable; reassigning x inside the function does not affect n"
    - "None — functions without return statements set caller variables to None"
    - "An error occurs because x is modified inside the function"
  answer: 1
  explanation: "When `n` is passed to `double`, the parameter `x` receives a copy of the value 5. Reassigning `x = x * 2` only changes the local variable `x` inside the function — it does not reach back and change `n` in the caller. For simple immutable types like integers, the parameter is effectively a local copy. This is a key distinction: modifying the parameter's value (reassignment) is different from mutating the object the parameter points to."

- question: "A function is defined as `def append_zero(lst): lst.append(0)`. After running `my_list = [1, 2]; append_zero(my_list)`, what is `my_list`?"
  type: multiple-choice
  options:
    - "[1, 2] — the function worked on a copy of the list"
    - "[1, 2, 0] — the parameter referred to the same list object in memory"
    - "[0] — the function replaced the list's contents"
    - "An error — lists cannot be passed as arguments"
  answer: 1
  explanation: "Lists are mutable objects. When `my_list` is passed to `append_zero`, the parameter `lst` points to the *same list object* in memory — not a copy. Calling `lst.append(0)` mutates that shared object, so the change is visible in the caller through `my_list`. This contrasts with the integer case: here the function didn't *reassign* `lst` (which would have had no effect on `my_list`); it *mutated* the object `lst` refers to."

- question: "Modifying a parameter inside a function always changes the original variable that was passed as the argument."
  type: true-false
  answer: false
  explanation: "Whether the original is affected depends on whether you mutate the object (changes are visible) or reassign the parameter (no effect on caller). For immutable types like integers and strings, 'modification' necessarily means reassignment, so the caller is never affected. For mutable types like lists, calling a mutating method (`.append()`, `.sort()`) affects the shared object, but reassigning the parameter (`lst = []`) does not reach the caller."

- question: "The terms 'parameter' and 'argument' refer to different things: parameters are the named placeholders declared in a function's definition, while arguments are the actual values supplied when the function is called."
  type: true-false
  answer: true
  explanation: "This distinction is precise and useful. In `def greet(name):`, `name` is a parameter — a formal variable in the function signature. In `greet('Alice')`, `'Alice'` is the argument — the actual value bound to that parameter at call time. Conflating the two makes it harder to reason about function definitions versus function calls, and obscures the mechanics of how values flow into and through functions."

- question: "Explain why calling `lst.append(42)` inside a function changes the caller's list, but assigning `lst = []` inside the same function does not."
  type: short-answer
  answer: "When a list is passed as an argument, the parameter `lst` and the caller's variable both point to the same list object in memory. Calling `lst.append(42)` mutates that shared object, so the change is visible through both references. Assigning `lst = []` only rebinds the local variable `lst` to a new empty list — it breaks `lst`'s connection to the original object without affecting the caller's variable, which still points to the original list."
  explanation: "This is Python's 'pass-by-object-reference' model. The parameter and the argument start as two names for the same object. Mutation changes the object itself (seen by everyone who holds a reference). Reassignment changes which object the local name refers to (invisible to the caller). Understanding this distinction prevents an entire class of bugs where functions unexpectedly do or do not modify the data passed to them."
```

## Explainer

You already know how to define and call functions — you can write `def greet():` and invoke it with `greet()`. But functions become truly powerful when they can accept **input** that changes their behavior. Instead of writing a separate function for every greeting, you write `def greet(name):` and pass different names each time. The variable `name` in the function signature is a **parameter** — a placeholder that receives a value when the function is called. The value you pass in — like `greet("Alice")` — is the **argument**. The parameter gets bound to the argument's value at call time, and within the function body, you use the parameter just like any other variable.

Functions can take multiple parameters, separated by commas: `def add(a, b):` defines a function that expects two arguments. When you call `add(3, 7)`, the argument `3` is bound to parameter `a` and `7` is bound to parameter `b`. The order matters — the first argument goes to the first parameter, the second to the second, and so on. This is called **positional argument** passing. Many languages also support **keyword arguments** (or named arguments), where you specify which parameter gets which value explicitly: `add(b=7, a=3)`. This is especially useful when a function has many parameters and you want clarity, or when you want to skip parameters that have default values.

**Default parameter values** let you make some arguments optional. In `def greet(name, greeting="Hello"):`, the second parameter has a default. Calling `greet("Alice")` uses the default greeting; calling `greet("Alice", "Hey")` overrides it. This pattern is ubiquitous — it lets you keep simple calls simple while allowing customization when needed. The parameters with defaults must come after those without, so the function signature reads left-to-right from required to optional.

One subtle but important point is what happens when you modify a parameter inside a function. For simple types like numbers and strings, changing the parameter does not affect the original variable outside the function — the parameter is effectively a local copy. But for mutable objects like lists and dictionaries, the parameter refers to the *same object* in memory. If you call `def append_item(lst): lst.append(42)` with `append_item(my_list)`, `my_list` itself is modified. This is the difference between **pass-by-value** (copying the value) and **pass-by-reference** (sharing the object). Python technically uses "pass-by-object-reference" — the parameter and the argument point to the same object, but reassigning the parameter (`lst = []`) only changes the local variable, not the caller's. Understanding this distinction prevents a whole class of bugs where functions unexpectedly modify — or unexpectedly fail to modify — the data you pass to them.
