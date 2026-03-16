---
id: primitive-data-types
title: Primitive Data Types
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: variables-and-assignment
  type: hard
builds-toward:
- operators-and-expressions
- type-conversion
- string-basics
tags:
- types
- integers
- floats
- booleans
- characters
stage: abstract-reasoning
status: validated
---

# Primitive Data Types

## Core Idea
Primitive data types are the basic building blocks of data in a program: integers (whole numbers), floating-point numbers (decimals), booleans (true/false), and characters or strings. Every value in a program has a type that determines what operations are valid and how the value is stored in memory. Strongly typed languages enforce type rules at compile time, while dynamically typed languages check types at runtime. Choosing the right type matters for correctness and efficiency.

## How It's Best Learned
Write short programs that declare variables of each type and print them. Try operations that mix types (e.g., integer + float) and observe the results. Compare how different languages handle the same type questions.

## Common Misconceptions
- Confusing integer division with float division (e.g., 5/2 = 2 in many languages, not 2.5).
- Assuming all numbers are the same type.
- Thinking booleans are just integers without understanding their distinct semantic role.

## Explainer

From your work with variables and assignment, you know that variables hold values in memory. But not all values are the same kind of thing — the number 42, the decimal 3.14, the word "hello", and the truth value `true` are fundamentally different, and the computer needs to know which kind it's dealing with. **Primitive data types** are the basic categories that classify these values, and every programming language has them as its foundation.

**Integers** store whole numbers: -3, 0, 42, 1000000. They support arithmetic operations like addition, subtraction, multiplication, and division. A critical detail: in many languages, dividing two integers gives an integer result, so `7 / 2` produces `3`, not `3.5` — the decimal part is simply dropped. This is **integer division**, and it catches beginners constantly. **Floating-point numbers** (floats) store decimal values: 3.14, -0.001, 2.0. They handle the fractional values that integers cannot, but they come with their own surprise — floats are approximations. The expression `0.1 + 0.2` produces `0.30000000000000004` in most languages, not `0.3`, because of how decimal fractions are represented in binary. This isn't a bug; it's a fundamental limitation of how computers store non-integer numbers.

**Booleans** hold exactly two values: true and false. They're the result of comparisons (`x > 5` evaluates to true or false) and the basis for all decision-making in programs. **Characters** represent individual letters, digits, or symbols ('A', '7', '!'). In some languages like Python, there's no separate character type — single characters are just strings of length one. **Strings** store sequences of characters ("hello", "42", "true") and are technically not always primitive, but they're so fundamental that most languages treat them as basic building blocks.

The type of a value determines **what operations are valid**. You can add two integers (5 + 3 = 8), and you can concatenate two strings ("hello" + " world" = "hello world"), but adding an integer to a string means different things in different languages — some concatenate ("5" + "3" = "53"), some throw an error, some convert automatically. This is where **type systems** diverge. Statically typed languages like Java or C require you to declare each variable's type upfront (`int score = 42;`), catching type errors before the program runs. Dynamically typed languages like Python infer the type from the value assigned (`score = 42`), checking types only when operations execute. Neither approach is inherently better — they trade early error detection for flexibility. Understanding types prevents a whole category of bugs and is essential as you move into operators, expressions, and type conversions.
