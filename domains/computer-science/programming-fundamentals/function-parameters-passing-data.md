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
stage: abstract-reasoning
status: draft
---

# Function Parameters: Passing Data

## Core Idea
Parameters are variables that receive data from the function call. Arguments are the actual values passed. Parameters enable functions to work with different inputs. Understanding argument order, count, and types prevents errors.

## How It's Best Learned
Write functions with multiple parameters; call them with arguments in different orders to see errors; use default parameters if available.

## Common Misconceptions
That parameters and arguments are the same (parameters are in the definition, arguments in the call); that parameter order doesn't matter; that modifying a parameter always changes the original variable (depends on pass-by-value vs pass-by-reference).

## Explainer

From your work with parameters and arguments, you know that functions can accept inputs and that the names in the function definition are parameters while the values you pass in a call are arguments. This topic deepens that understanding by focusing on *how* data flows into a function and what happens to it once it arrives — the mechanics of **passing data** through parameters.

Think of a function like a recipe card with blanks: "Bake _____ at _____ degrees for _____ minutes." The blanks are **parameters** — placeholders that make the recipe reusable. When you actually bake, you fill in the blanks with specific values: "Bake chicken at 375 degrees for 45 minutes." Those specific values are **arguments**. The recipe does not change; the blanks get temporarily filled each time you use it. In code, `def bake(item, temp, minutes)` defines three parameters, and `bake("chicken", 375, 45)` passes three arguments. Inside the function, `item` holds `"chicken"`, `temp` holds `375`, and `minutes` holds `45`.

**Order and count matter**. When you call `bake(375, "chicken", 45)`, the function does not know you meant 375 as the temperature — it assigns values to parameters strictly by position. `item` becomes `375` and `temp` becomes `"chicken"`, which will almost certainly cause an error or wrong behavior. This positional matching is the default in most languages. Some languages also support **named arguments** (like `bake(temp=375, item="chicken", minutes=45)`), which let you specify which parameter each argument fills regardless of order — but until you encounter that feature, treat argument order as a contract you must honor.

A subtler question is what happens when you modify a parameter inside the function. If you write `temp = temp + 50` inside `bake`, does the variable you passed in also change? The answer depends on whether the language uses **pass-by-value** or **pass-by-reference** — a distinction you will explore in depth next. For now, the key mental model is that parameters are the function's private copies or connections to outside data. Understanding this interface between caller and function is what makes it possible to write functions that are predictable, reusable, and free from surprising side effects.
