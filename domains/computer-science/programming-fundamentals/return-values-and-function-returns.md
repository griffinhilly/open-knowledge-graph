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

## Explainer

You already understand that a function can produce a result using `return`. This topic deepens that understanding by exploring how return values make functions composable — the key property that turns isolated code blocks into a powerful system of building blocks.

Think of a function as a small machine with an input slot and an output slot. Arguments go in, the function does its work, and a **return value** comes out. The caller receives this value and can do anything with it: assign it to a variable, pass it to another function, use it in a comparison, or ignore it entirely. The statement `result = add(3, 4)` calls `add`, which returns `7`, and that `7` gets assigned to `result`. The function is done — it has exited completely — and the caller now owns the value.

The `return` statement does two things simultaneously: it specifies what value to send back, and it **immediately exits the function**. No code after `return` in the same block will execute. This makes `return` a control flow mechanism, not just a value delivery system. You can use this to create **early returns** — exiting a function as soon as you have your answer. For example, a function checking whether a list contains a negative number can return `True` the moment it finds one, without scanning the rest. This pattern is cleaner than setting a flag variable and checking it at the end.

The most persistent confusion at this stage is between `print` and `return`. **`print` displays text to the screen for humans to read; `return` sends data back to the calling code for the program to use.** A function that prints its result but doesn't return it is a dead end — no other code can use that value. If you write `def square(x): print(x * x)` and then try `result = square(5)`, `result` will be `None` (or equivalent), because the function never returned anything. The `25` appeared on screen, but it vanished into the void as far as the program is concerned. The correct version is `def square(x): return x * x`. This distinction matters because **function composition** — using the output of one function as the input to another, like `square(add(2, 3))` — only works with return values, never with print.
