---
id: function-parameters-passing-data
title: 'Function Parameters: Passing Data'
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: parameters-and-arguments
  type: hard
- id: variables-and-assignment
  type: hard
builds-toward:
- parameter-passing-value-vs-reference
- return-values-and-function-returns
tags:
- functions
- parameters
- arguments
stage: formal-systems
status: draft
---

# Function Parameters: Passing Data

## Core Idea
Parameters are variables that receive data from the function call. Arguments are the actual values passed. Parameters enable functions to work with different inputs. Understanding argument order, count, and types prevents errors.

## How It's Best Learned
Write functions with multiple parameters; call them with arguments in different orders to see errors; use default parameters if available.

## Common Misconceptions
That parameters and arguments are the same (parameters are in the definition, arguments in the call); that parameter order doesn't matter; that modifying a parameter always changes the original variable (depends on pass-by-value vs pass-by-reference).

## Questions

```yaml
- question: "A function is defined as def calculate(base, rate, years). A student calls it as calculate(0.05, 1000, 10), intending base=1000, rate=0.05, years=10. What is the problem?"
  type: multiple-choice
  options:
    - "There is no problem — Python infers which argument matches which parameter based on their values"
    - "Arguments are assigned by position, so base receives 0.05, rate receives 1000, and years receives 10 — the wrong values"
    - "The function will raise a TypeError because the argument types do not match"
    - "The function will produce a warning but still compute the correct result"
  answer: 1
  explanation: "Arguments are matched to parameters strictly by position in the default calling convention. The function has no way to know the programmer's intent: it assigns the first argument to the first parameter, second to second, and so on. So base=0.05, rate=1000, years=10 — the calculation will run with inverted values and produce a wrong result, likely without any error. This is a silent logic bug, which is harder to catch than a crash."

- question: "What is the fundamental difference between a parameter and an argument?"
  type: multiple-choice
  options:
    - "Parameters appear in the function call; arguments appear in the function definition"
    - "Parameters are the named placeholders in the function definition; arguments are the actual values passed during the call"
    - "Parameters are used for primitive data types; arguments are used for complex objects"
    - "There is no meaningful difference — the terms are interchangeable"
  answer: 1
  explanation: "Parameters are the named variables declared in the function signature (definition): def bake(item, temp, minutes) — item, temp, and minutes are parameters. Arguments are the concrete values supplied when calling the function: bake('chicken', 375, 45) — 'chicken', 375, and 45 are arguments. Conflating these terms creates confusion when debugging call errors, because error messages distinguish them: 'missing 1 required positional argument' means you provided too few arguments, not that you defined the parameter incorrectly."

- question: "In most languages that use positional argument matching, passing arguments in the wrong order will always trigger a runtime error, making the mistake easy to detect."
  type: true-false
  answer: false
  explanation: "This is the dangerous aspect of the wrong-order mistake. Most languages will happily run the function with arguments in the wrong positions — no error is raised. The function receives values in the wrong parameters and computes a wrong result silently. For example, a function expecting (principal, rate) called with (rate, principal) will execute without complaint and return an incorrect number. Silent logic errors are harder to diagnose than crashes."

- question: "Parameters are the named placeholders in the function definition, while arguments are the specific values provided at the call site — they are distinct concepts."
  type: true-false
  answer: true
  explanation: "This distinction is fundamental and precise. def add(x, y): x and y are parameters — they exist only inside the function, as temporary receptacles waiting to receive values. When you call add(3, 5), the values 3 and 5 are arguments — they travel from the call site into the function, filling the parameters. Understanding the distinction helps diagnose errors: 'wrong number of arguments' tells you something about the call site; 'parameter not defined' tells you something about the function definition."

- question: "Why does argument order matter when calling a function? What goes wrong when arguments are passed in the wrong order?"
  type: short-answer
  answer: "Arguments are assigned to parameters by their position in the call. The function receives values in the order they are passed, with no knowledge of what the programmer intended. Passing arguments in the wrong order means each parameter receives the wrong value — the function runs with incorrect data and produces a wrong result. Because most languages do not raise an error for mismatched-but-type-compatible arguments, this produces a silent logic bug that can be difficult to trace."
  explanation: "This is why understanding positional matching is practical, not just theoretical. Debugging a wrong-order call requires knowing that argument position is the contract between caller and function — a contract that the language enforces structurally, not semantically. Named arguments (where supported) are one way to make calls more self-documenting and order-independent."
```

## Explainer

From your work with parameters and arguments, you know that functions can accept inputs and that the names in the function definition are parameters while the values you pass in a call are arguments. This topic deepens that understanding by focusing on *how* data flows into a function and what happens to it once it arrives — the mechanics of **passing data** through parameters.

Think of a function like a recipe card with blanks: "Bake _____ at _____ degrees for _____ minutes." The blanks are **parameters** — placeholders that make the recipe reusable. When you actually bake, you fill in the blanks with specific values: "Bake chicken at 375 degrees for 45 minutes." Those specific values are **arguments**. The recipe does not change; the blanks get temporarily filled each time you use it. In code, `def bake(item, temp, minutes)` defines three parameters, and `bake("chicken", 375, 45)` passes three arguments. Inside the function, `item` holds `"chicken"`, `temp` holds `375`, and `minutes` holds `45`.

**Order and count matter**. When you call `bake(375, "chicken", 45)`, the function does not know you meant 375 as the temperature — it assigns values to parameters strictly by position. `item` becomes `375` and `temp` becomes `"chicken"`, which will almost certainly cause an error or wrong behavior. This positional matching is the default in most languages. Some languages also support **named arguments** (like `bake(temp=375, item="chicken", minutes=45)`), which let you specify which parameter each argument fills regardless of order — but until you encounter that feature, treat argument order as a contract you must honor.

A subtler question is what happens when you modify a parameter inside the function. If you write `temp = temp + 50` inside `bake`, does the variable you passed in also change? The answer depends on whether the language uses **pass-by-value** or **pass-by-reference** — a distinction you will explore in depth next. For now, the key mental model is that parameters are the function's private copies or connections to outside data. Understanding this interface between caller and function is what makes it possible to write functions that are predictable, reusable, and free from surprising side effects.
