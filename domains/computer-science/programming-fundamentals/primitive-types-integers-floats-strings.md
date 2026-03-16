---
id: primitive-types-integers-floats-strings
title: 'Primitive Types: Integers, Floats, and Strings'
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: primitive-data-types
  type: hard
builds-toward:
- arithmetic-operators-and-precedence
- character-and-string-basics
- working-with-numbers-integers-floats
tags:
- types
- data
- fundamentals
stage: abstract-reasoning
status: draft
---

# Primitive Types: Integers, Floats, and Strings

## Core Idea
Primitive types represent basic values: integers store whole numbers, floats store decimals, strings store text. Each type has specific operations (addition works on numbers, concatenation on strings) and memory costs. Choosing the right type prevents bugs and wasted memory.

## How It's Best Learned
Experiment with operations on each type; print the type of variables using type() or similar to confirm what you're working with.

## Common Misconceptions
That '5' (string) and 5 (integer) are the same; that floats are infinitely precise (they have rounding errors); that all numbers should be floats for 'safety.'

## Explainer

You already know that data in a program has types. Now let's look at the three most common primitive types and understand what makes each one distinct. An **integer** stores a whole number — no decimal point, no fractional part. Examples: `0`, `-7`, `42`, `1000000`. Integers are exact: `3 + 4` always equals `7`, with no rounding or approximation. They are the right choice whenever you are counting discrete things — number of students, loop iterations, array indices.

A **float** (short for floating-point number) stores a number with a decimal part: `3.14`, `-0.001`, `2.0`. Floats can represent a huge range of values, from the astronomically large to the microscopically small. But they come with a critical tradeoff: **limited precision**. Internally, a float is stored in binary using a fixed number of bits, which means many decimal fractions cannot be represented exactly. Try `0.1 + 0.2` in most languages and you will get something like `0.30000000000000004` instead of `0.3`. This is not a bug — it is a fundamental property of how floating-point numbers work. For most calculations (physics, graphics, statistics) the tiny errors are negligible. But for money or exact comparisons, integers or specialized decimal types are safer.

A **string** stores text — a sequence of characters enclosed in quotes: `"hello"`, `'42'`, `"Jane Doe"`. Here is the crucial point: the string `"5"` and the integer `5` are entirely different values. The string `"5"` is a text character — you can concatenate it with other strings (`"5" + "3"` gives `"53"`, not `8`), but you cannot do arithmetic with it. The integer `5` is a number — you can add it, multiply it, use it as a loop counter. Most languages will refuse to add a string to an integer directly, and for good reason: the operation is ambiguous. You need to explicitly convert between types using functions like `int("5")` or `str(5)`.

Understanding these distinctions prevents an entire class of bugs. When you read input from a user or a file, it almost always arrives as a string, even if it looks like a number. Before doing math with it, you must convert it to an integer or float. When you choose a type for a variable, ask: am I counting something discrete (integer), measuring something continuous (float), or storing text (string)? The answer determines which operations are valid, how much memory is used, and whether subtle precision bugs can creep in.
