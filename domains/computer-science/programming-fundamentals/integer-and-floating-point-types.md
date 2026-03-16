---
id: integer-and-floating-point-types
title: Integer and Floating-Point Number Types
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: memory-and-data-storage
  type: hard
builds-toward:
- arithmetic-operators-intro
- type-conversion-casting
tags:
- types
- numbers
- numeric
stage: abstract-reasoning
status: draft
---

# Integer and Floating-Point Number Types

## Core Idea
Programs represent numbers in two main forms: integers (whole numbers) and floating-point numbers (decimals). Each has different ranges, precision, and performance characteristics, affecting how calculations are done.

## How It's Best Learned
Test programs that perform arithmetic with both types. Observe rounding errors with floats; verify exact integer arithmetic.

## Common Misconceptions
- Floating-point numbers are always imprecise (they have fixed precision based on bits).
- Integers and floats can be freely mixed without loss (some information may be lost in conversion).

## Explainer

From your study of memory and data storage, you know that computers store everything as patterns of bits. How those bits are *interpreted* depends on the data type. For numbers, the two fundamental types are **integers** and **floating-point numbers**, and understanding the difference matters because each represents numbers in a fundamentally different way with different tradeoffs.

**Integers** represent whole numbers — values like -3, 0, 42, or 1000000. In most languages, an integer is stored as a fixed number of bits (commonly 32 or 64), giving it a fixed range. A 32-bit signed integer can hold values from about -2.1 billion to +2.1 billion. Within that range, integer arithmetic is *exact*: `7 + 3` is always `10`, `100 * 200` is always `20000`, with no rounding or approximation. This makes integers the right choice for counting, indexing, and any situation where fractional values do not apply. In Python specifically, integers have unlimited precision — they grow as large as memory allows — but in languages like C, Java, and JavaScript, overflow is a real concern when values exceed the type's range.

**Floating-point numbers** represent values with a decimal point — like 3.14, -0.001, or 6.022e23. They use a format inspired by scientific notation: a sign, a **significand** (the digits), and an **exponent** (the scale). A 64-bit float (called `double` in many languages) gives about 15-16 significant decimal digits of precision. This is plenty for most purposes, but it means that some numbers cannot be represented exactly. The classic example: `0.1 + 0.2` does not equal `0.3` in most languages — it produces something like `0.30000000000000004`. This is not a bug; it is a fundamental consequence of representing base-10 fractions in base-2. Just as 1/3 cannot be written exactly in decimal (0.333...), 1/10 cannot be written exactly in binary.

The practical rule is straightforward: use integers for discrete quantities (counts, indices, IDs) and floating-point for continuous measurements (distances, temperatures, percentages). Be cautious when **comparing floats for equality** — instead of `x == 0.3`, use a tolerance like `abs(x - 0.3) < 1e-9`. And be aware that when you mix integers and floats in an expression (like `5 + 2.5`), most languages automatically convert the integer to a float before computing, which is usually fine. But converting a very large integer to a float can lose precision: a 64-bit integer can represent values that exceed the 15-16 significant digits a float can hold, so the conversion silently rounds. Understanding these tradeoffs early prevents mysterious bugs in numeric code.
