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

## Explainer

You know how to store values in variables and use conditional statements to make decisions. Functions take these building blocks and give you a way to organize them into reusable, named units. Think of a function like a recipe: the **definition** is writing the recipe down (ingredients needed, steps to follow, what comes out at the end), and the **call** is actually cooking the dish. Writing a recipe doesn't produce food — you have to follow it. Similarly, defining a function doesn't execute the code inside it — you have to call the function by name.

In most languages, you define a function with a keyword (`def` in Python, `function` in JavaScript), a name, parentheses for any inputs, and a body of code. For example, `def greet(): print("Hello!")` defines a function named `greet` that prints a greeting. To actually execute it, you write `greet()` — the parentheses are what trigger execution. Without them, you're just referring to the function as an object, not running it. This distinction between defining and calling is the single most important thing to internalize: **definition creates the function; calling executes it**. You can call a function as many times as you want after defining it once, which is the source of its power.

Functions serve two fundamental purposes: **abstraction** and **modularity**. Abstraction means hiding complexity behind a name. Instead of writing ten lines of code every time you need to calculate a tax amount, you write a function called `calculate_tax` and call it by name. The caller doesn't need to know how the calculation works — just what to pass in and what comes back. This makes code read like a description of what it does rather than how it does it. Modularity means breaking a program into independent pieces, each responsible for one task. A function that calculates tax doesn't also format output or read user input — it does one thing. This makes functions easier to test, debug, and reuse. If your tax calculation has a bug, you fix it in one place, and every call site benefits.

The flow of execution when a function is called follows a specific pattern: the program pauses at the call site, jumps to the function body, executes the code inside, and then returns to exactly where it left off. You can trace this by imagining a bookmark: the program puts a bookmark at the call, runs the function, and then picks up where the bookmark is. This is how the call stack works under the hood — each function call adds a frame, and when the function completes, its frame is removed and execution returns to the caller. Understanding this flow is critical for reasoning about program behavior, especially as you move on to topics like parameters, return values, and eventually recursion, all of which build directly on this foundation.
