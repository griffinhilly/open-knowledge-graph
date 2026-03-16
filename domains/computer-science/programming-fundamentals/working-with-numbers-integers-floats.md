---
id: working-with-numbers-integers-floats
title: 'Working with Numbers: Integers and Floats'
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: primitive-types-integers-floats-strings
  type: hard
builds-toward:
- arithmetic-operators-and-precedence
- type-conversion-intro
tags:
- arithmetic
- numbers
- types
stage: abstract-reasoning
status: draft
---

# Working with Numbers: Integers and Floats

## Core Idea
Integer arithmetic is exact but can overflow; floating-point arithmetic is approximate and can lose precision. Understanding integer division (7/2 = 3 in many languages) and floating-point errors prevents logic bugs. Different languages handle these differently.

## How It's Best Learned
Perform calculations by hand, predict the result, then run code and compare; test edge cases like division by zero or very large numbers.

## Common Misconceptions
That division always returns a decimal; that floating-point math is exact (0.1 + 0.2 may not equal 0.3); that integers overflow silently (behavior varies by language).

## Explainer

From your study of primitive types, you know that integers and floats are distinct types that represent numbers differently. This topic digs into the practical consequences of that distinction — the subtle ways that integer and floating-point arithmetic can surprise you if you don't understand what's happening under the hood.

**Integers** represent whole numbers exactly. `7` is exactly `7`, and `7 + 3` is exactly `10` — no approximation involved. The catch is that integers have a fixed size in most languages (typically 32 or 64 bits), which means they have a maximum value. In a 32-bit signed integer, the largest value is 2,147,483,647. Add 1 to it and you get **integer overflow** — the number wraps around to a negative value or raises an error, depending on the language. Python is an exception here: its integers automatically grow as large as needed, so overflow isn't an issue. But in C, Java, or JavaScript (for typed arrays), overflow is a real and silent bug. Integer division is the other gotcha: in many languages, `7 / 2` yields `3`, not `3.5`, because dividing two integers produces an integer result with the decimal part truncated.

**Floating-point numbers** (floats) represent decimal values, but they do so approximately. A float stores a number in scientific notation using binary: a significand and an exponent, packed into 32 or 64 bits. This representation can exactly store values like 0.5 (which is 1/2 in binary) but cannot exactly store 0.1 (which in binary is a repeating fraction, like 1/3 is in decimal). The result is that `0.1 + 0.2` evaluates to something like `0.30000000000000004`, not `0.3`. This is not a bug in your language — it is a fundamental consequence of representing infinitely many real numbers with a finite number of bits.

The practical takeaway is to never compare floats for exact equality. Instead of `if total == 0.3`, use a tolerance: `if abs(total - 0.3) < 0.0001`. For financial calculations where exact decimal arithmetic matters, most languages provide a dedicated decimal type (like Python's `decimal.Decimal`) that avoids binary floating-point errors entirely, at the cost of slower computation. Understanding when to use integers, floats, and decimal types is a judgment call that depends on what your program needs: integers for counting discrete items, floats for scientific computation where small errors are acceptable, and decimals for money and other contexts where precision is non-negotiable.
