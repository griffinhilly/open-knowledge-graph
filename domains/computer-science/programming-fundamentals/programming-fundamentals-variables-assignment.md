---
id: programming-fundamentals-variables-assignment
title: Variables and Assignment
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: variables-and-assignment
  type: soft
builds-toward:
- programming-fundamentals-primitive-types
- programming-fundamentals-arithmetic-operators
tags:
- variables
- assignment
- fundamentals
stage: abstract-reasoning
status: draft
---
# Variables and Assignment

## Core Idea
A variable is a named container that stores a value in memory. Assignment uses the = operator to bind a value to a variable name. Variables allow programs to store, retrieve, and manipulate data throughout execution.

## Explainer

Every useful program needs to remember things. When you calculate a total, look up a user's name, or count how many times a loop has run, you need somewhere to put that information so you can use it later. A **variable** is that "somewhere" — a named slot in the computer's memory that holds a value. Think of it like a labeled box: the label is the variable's name, and whatever you put inside is its current value.

**Assignment** is the act of putting a value into that box. In most languages, you write it with the `=` sign: `score = 0` creates a variable called `score` and stores the number `0` in it. This is different from mathematical equality — it's a command, not a statement of fact. The left side is always the name, and the right side is always the value (or an expression that produces a value). So `score = score + 10` makes perfect sense in programming: it means "take the current value of `score`, add 10, and store the result back in `score`."

You can reassign a variable at any time, and its old value is simply replaced. If you write `color = "red"` and later `color = "blue"`, the variable `color` now holds `"blue"` — the `"red"` is gone. This is what makes variables powerful: they let your program's state change over time. A countdown timer, a running total, a user's input — all of these are values that change as the program executes, and variables are how you track them.

Choosing good variable names is one of the first habits worth building. A name like `x` tells you nothing, while `total_price` immediately communicates what the variable represents. Names typically follow rules: they can contain letters, numbers, and underscores, but cannot start with a number or contain spaces. Most languages are case-sensitive, so `Score` and `score` would be two different variables. Getting comfortable with variables and assignment is foundational — nearly every concept you encounter next, from arithmetic operations to conditionals to loops, depends on being able to store and retrieve values by name.
