---
id: programming-fundamentals-variable-scope
title: Variable Scope and Lifetime
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: programming-fundamentals-function-definition
  type: hard
builds-toward:
- programming-fundamentals-recursion-basics
tags:
- scope
- lifetime
- variables
stage: abstract-reasoning
status: draft
---

# Variable Scope and Lifetime

## Core Idea
Scope determines where a variable is accessible in the code. Global scope means accessible everywhere; local scope means accessible only within a function or block. Lifetime is how long a variable exists in memory.

## Explainer

When you define a function — your hard prerequisite here — you create a self-contained block of code with its own inputs and outputs. But what happens to the variables you create inside that function? Can the rest of your program see them? The answer is no, and understanding why is what **variable scope** is all about. Scope is the region of your source code where a particular variable name is valid and accessible.

A **local variable** is one you create inside a function. It exists only while that function is running and can only be referenced within that function's body. Once the function returns, the local variable is destroyed — its memory is reclaimed and its name becomes meaningless. A **global variable**, by contrast, is defined at the top level of your program, outside any function. It is accessible from anywhere in the code. This distinction matters because it determines which parts of your program can read or modify which data. If you create a variable `count` inside a function `tally()`, no other function can see or change that `count` — it is local to `tally()`.

The closely related concept of **lifetime** describes how long a variable exists in memory, as opposed to where it is visible. For most local variables, scope and lifetime coincide: the variable comes into existence when execution enters the function and is destroyed when execution leaves. But they are conceptually distinct. In some languages, a variable can exist in memory (it is still alive) but not be accessible from a certain part of the code (it is out of scope). This separation becomes important as you encounter closures and nested functions in later topics.

Why does any of this matter practically? Scope is what makes functions truly independent and reusable. Because local variables are invisible outside their function, you can name a variable `result` in ten different functions without any conflict. Each function operates in its own namespace, its own little world. This is also why global variables should be used sparingly — they break this isolation. If multiple functions read and modify the same global variable, a change in one function can cause unexpected behavior in another. That kind of invisible coupling makes bugs extremely hard to track down. The discipline of keeping variables as local as possible is one of the most important habits in writing clean, maintainable code, and it builds directly toward understanding recursion, where each function call gets its own independent set of local variables.
