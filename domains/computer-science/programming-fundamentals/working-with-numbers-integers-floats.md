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
stage: formal-systems
status: draft
---

# Working with Numbers: Integers and Floats

## Core Idea
Integer arithmetic is exact but can overflow; floating-point arithmetic is approximate and can lose precision. Understanding integer division (7/2 = 3 in many languages) and floating-point errors prevents logic bugs. Different languages handle these differently.

## How It's Best Learned
Perform calculations by hand, predict the result, then run code and compare; test edge cases like division by zero or very large numbers.

## Common Misconceptions
That division always returns a decimal; that floating-point math is exact (0.1 + 0.2 may not equal 0.3); that integers overflow silently (behavior varies by language).

## Questions

```yaml
- question: "A financial application checks `if total == 0.30` to validate a cart containing items priced at $0.10 and $0.20. The check fails even though the cart is correct. What is the most likely cause?"
  type: multiple-choice
  options:
    - "The addition operator is broken for small decimal numbers in this language"
    - "0.1 and 0.2 cannot be exactly represented in binary floating-point, so their sum evaluates to something like 0.30000000000000004, not exactly 0.3"
    - "The `==` operator does not work for decimal comparisons in most languages"
    - "The cart is calculating in integer cents and rounding incorrectly"
  answer: 1
  explanation: "This is the canonical floating-point equality bug. Both 0.1 and 0.2 are repeating fractions in binary (just as 1/3 is in decimal), so they cannot be represented exactly. When added together, their accumulated representational errors produce a result like 0.30000000000000004 — close to 0.3 but not bit-for-bit equal to it. The fix is to avoid exact equality with floats and instead check whether the absolute difference is smaller than a small tolerance."

- question: "In Python 3, what does the expression `7 // 2` evaluate to?"
  type: multiple-choice
  options:
    - "3.5"
    - "4 (rounds up to the nearest integer)"
    - "3 (integer division truncates toward zero, discarding the decimal)"
    - "An error, because 7 is not evenly divisible by 2"
  answer: 2
  explanation: "The `//` operator in Python performs integer (floor) division, which truncates toward negative infinity — discarding the decimal part. 7 / 2 = 3.5, and truncation gives 3. In many other languages (C, Java), the standard `/` operator also truncates when both operands are integers: `7 / 2` gives `3`, not `3.5`. This is a frequent source of off-by-one errors when programmers expect decimal results."

- question: "In most mainstream programming languages, dividing two integers with the standard division operator produces a floating-point result."
  type: true-false
  answer: false
  explanation: "In many languages — C, Java, Go, and Python 2 — dividing two integers with `/` produces an integer result with the decimal part truncated. Python 3 is an exception: its `/` operator always returns a float, and `//` is used for integer division. Assuming division always returns a decimal is a common and dangerous misconception that causes silent logic errors."

- question: "Floating-point arithmetic is approximate because programming languages implement it imprecisely — this is a bug that better implementations will eventually fix."
  type: true-false
  answer: false
  explanation: "Floating-point approximation is a mathematical inevitability, not a language bug. There are infinitely many real numbers but only finitely many bit patterns to represent them. Values like 0.1 are repeating fractions in binary, just as 1/3 is in decimal. No finite binary representation can store them exactly. IEEE 754 floating-point is a standard, carefully designed format — its approximation behavior is specified, documented, and unavoidable."

- question: "Why should you avoid using exact equality (`==`) to compare floating-point numbers, and what should you do instead?"
  type: short-answer
  answer: "Floating-point numbers are stored as binary approximations, and arithmetic on them accumulates small representational errors — 0.1 + 0.2 may evaluate to 0.30000000000000004, not 0.3. Using `==` checks for bit-perfect equality, which fails for computed float values even when they are mathematically 'close enough.' Instead, check whether the absolute difference falls within a small tolerance: `abs(a - b) < 0.0001`. For applications requiring exact decimal arithmetic — like financial calculations — use a dedicated decimal type (such as Python's `decimal.Decimal`) that avoids binary floating-point representation entirely."
  explanation: "The broader principle is to choose the right numeric type for the job: integers for exact counting, floats for scientific computation where small errors are acceptable, and decimal types for money or other contexts where precision is non-negotiable. Understanding the representational trade-offs is what lets you make that choice deliberately rather than being surprised by the results."
```

## Explainer

From your study of primitive types, you know that integers and floats are distinct types that represent numbers differently. This topic digs into the practical consequences of that distinction — the subtle ways that integer and floating-point arithmetic can surprise you if you don't understand what's happening under the hood.

**Integers** represent whole numbers exactly. `7` is exactly `7`, and `7 + 3` is exactly `10` — no approximation involved. The catch is that integers have a fixed size in most languages (typically 32 or 64 bits), which means they have a maximum value. In a 32-bit signed integer, the largest value is 2,147,483,647. Add 1 to it and you get **integer overflow** — the number wraps around to a negative value or raises an error, depending on the language. Python is an exception here: its integers automatically grow as large as needed, so overflow isn't an issue. But in C, Java, or JavaScript (for typed arrays), overflow is a real and silent bug. Integer division is the other gotcha: in many languages, `7 / 2` yields `3`, not `3.5`, because dividing two integers produces an integer result with the decimal part truncated.

**Floating-point numbers** (floats) represent decimal values, but they do so approximately. A float stores a number in scientific notation using binary: a significand and an exponent, packed into 32 or 64 bits. This representation can exactly store values like 0.5 (which is 1/2 in binary) but cannot exactly store 0.1 (which in binary is a repeating fraction, like 1/3 is in decimal). The result is that `0.1 + 0.2` evaluates to something like `0.30000000000000004`, not `0.3`. This is not a bug in your language — it is a fundamental consequence of representing infinitely many real numbers with a finite number of bits.

The practical takeaway is to never compare floats for exact equality. Instead of `if total == 0.3`, use a tolerance: `if abs(total - 0.3) < 0.0001`. For financial calculations where exact decimal arithmetic matters, most languages provide a dedicated decimal type (like Python's `decimal.Decimal`) that avoids binary floating-point errors entirely, at the cost of slower computation. Understanding when to use integers, floats, and decimal types is a judgment call that depends on what your program needs: integers for counting discrete items, floats for scientific computation where small errors are acceptable, and decimals for money and other contexts where precision is non-negotiable.
