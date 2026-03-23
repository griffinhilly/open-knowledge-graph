---
id: numeric-types
title: Integer and Floating-Point Number Types
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: memory-and-data-storage
  type: hard
- id: primitive-data-types
  type: hard
builds-toward:
- arithmetic-operators
- type-conversion-casting
- type-conversion-intro
tags:
- types
- numbers
- numeric
stage: formal-systems
status: validated
---
# Integer and Floating-Point Number Types

## Core Idea
Programs represent numbers in two main forms: integers (whole numbers) and floating-point numbers (decimals). Each has different ranges, precision, and performance characteristics, affecting how calculations are done.

## How It's Best Learned
Test programs that perform arithmetic with both types. Observe rounding errors with floats; verify exact integer arithmetic.

## Common Misconceptions
- Floating-point numbers are always imprecise (they have fixed precision based on bits).
- Integers and floats can be freely mixed without loss (some information may be lost in conversion).

## Questions

```yaml
- question: "Why does `0.1 + 0.2` produce approximately `0.30000000000000004` rather than exactly `0.3` in most programming languages?"
  type: multiple-choice
  options:
    - "This is a bug in the language's math library that has not been patched"
    - "Floating-point arithmetic is inherently random and produces slightly different results each time"
    - "The number 0.1 cannot be represented exactly in binary, just as 1/3 cannot be written exactly in decimal — so a rounding error is introduced during representation, not calculation"
    - "The CPU performs addition before converting binary to decimal, introducing a translation error"
  answer: 2
  explanation: "The error is in the representation, not the arithmetic. Just as the fraction 1/3 has no finite decimal representation (0.333...), the fraction 1/10 has no finite binary representation. When 0.1 is stored as a float, it's rounded to the nearest representable binary value — slightly off. When you add two slightly-off values, the error accumulates. This is deterministic and predictable, not random."

- question: "A program converts a very large 64-bit integer (e.g., 2^60) to a 64-bit float before doing arithmetic. What risk does this introduce?"
  type: multiple-choice
  options:
    - "The program will throw a runtime error because floats cannot store values that large"
    - "The value will always be rounded down to the nearest power of 2"
    - "The integer's value may be silently rounded because a 64-bit float only stores about 15–16 significant decimal digits, which may be fewer than the integer requires"
    - "No risk — converting integers to floats is always lossless regardless of magnitude"
  answer: 2
  explanation: "A 64-bit integer can represent values requiring up to 19 significant decimal digits with full precision, but a 64-bit float only provides about 15–16 significant digits. For large integers, the conversion silently rounds to the nearest representable float value — losing precision. This is a real source of bugs in financial and scientific software where large exact integers are common."

- question: "In Python specifically, integer arithmetic is exact with no overflow risk, regardless of how large the numbers get."
  type: true-false
  answer: true
  explanation: "Python integers use arbitrary-precision arithmetic — they grow to use as much memory as needed. There is no fixed bit width, so there is no overflow. Computing 10**100 or 2**1000 returns an exact integer in Python. This distinguishes Python from C, Java, and JavaScript, where integer types are fixed-width (e.g., 32-bit or 64-bit) and will overflow or wrap around when values exceed their range."

- question: "Floating-point imprecision is unpredictable — you can't know in advance which calculations will produce rounding errors."
  type: true-false
  answer: false
  explanation: "Floating-point behavior is entirely deterministic and follows the IEEE 754 standard. The same operation on the same values always produces the same result. The rule is precise: a value is rounded to the nearest representable binary floating-point number. Whether a specific value like 0.1 or 0.5 is exact (0.5 is, because it's 1/2) or inexact (0.1 is not) is knowable in advance. Imprecision is systematic, not random."

- question: "Why is it a mistake to compare floating-point numbers with ==, and what should you do instead?"
  type: short-answer
  answer: "Because floating-point arithmetic accumulates small rounding errors, two calculations that should theoretically produce the same value may produce results that differ by a tiny amount (e.g., 0.30000000000000004 vs. 0.3). Comparing with == will then return false even when the values are practically equal. Instead, check whether the absolute difference falls within a small tolerance: abs(x - expected) < 1e-9 (or some appropriate epsilon for your domain)."
  explanation: "This is a direct consequence of the representation issue. The == operator checks for bit-for-bit equality, which floating-point arithmetic rarely guarantees. Tolerance-based comparison acknowledges the fundamental nature of floating-point numbers — they are approximations — and makes the code robust to the small rounding errors that are unavoidable in floating-point computation."
```

## Explainer

From your study of memory and data storage, you know that computers store everything as patterns of bits. How those bits are *interpreted* depends on the data type. For numbers, the two fundamental types are **integers** and **floating-point numbers**, and understanding the difference matters because each represents numbers in a fundamentally different way with different tradeoffs.

**Integers** represent whole numbers — values like -3, 0, 42, or 1000000. In most languages, an integer is stored as a fixed number of bits (commonly 32 or 64), giving it a fixed range. A 32-bit signed integer can hold values from about -2.1 billion to +2.1 billion. Within that range, integer arithmetic is *exact*: `7 + 3` is always `10`, `100 * 200` is always `20000`, with no rounding or approximation. This makes integers the right choice for counting, indexing, and any situation where fractional values do not apply. In Python specifically, integers have unlimited precision — they grow as large as memory allows — but in languages like C, Java, and JavaScript, overflow is a real concern when values exceed the type's range.

**Floating-point numbers** represent values with a decimal point — like 3.14, -0.001, or 6.022e23. They use a format inspired by scientific notation: a sign, a **significand** (the digits), and an **exponent** (the scale). A 64-bit float (called `double` in many languages) gives about 15-16 significant decimal digits of precision. This is plenty for most purposes, but it means that some numbers cannot be represented exactly. The classic example: `0.1 + 0.2` does not equal `0.3` in most languages — it produces something like `0.30000000000000004`. This is not a bug; it is a fundamental consequence of representing base-10 fractions in base-2. Just as 1/3 cannot be written exactly in decimal (0.333...), 1/10 cannot be written exactly in binary.

The practical rule is straightforward: use integers for discrete quantities (counts, indices, IDs) and floating-point for continuous measurements (distances, temperatures, percentages). Be cautious when **comparing floats for equality** — instead of `x == 0.3`, use a tolerance like `abs(x - 0.3) < 1e-9`. And be aware that when you mix integers and floats in an expression (like `5 + 2.5`), most languages automatically convert the integer to a float before computing, which is usually fine. But converting a very large integer to a float can lose precision: a 64-bit integer can represent values that exceed the 15-16 significant digits a float can hold, so the conversion silently rounds. Understanding these tradeoffs early prevents mysterious bugs in numeric code.
