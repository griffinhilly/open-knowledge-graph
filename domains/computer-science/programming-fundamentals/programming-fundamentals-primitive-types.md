---
id: programming-fundamentals-primitive-types
title: Primitive Data Types
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: programming-fundamentals-variables-assignment
  type: hard
builds-toward:
- programming-fundamentals-type-conversion
- programming-fundamentals-strings-introduction
tags:
- types
- data
- primitives
stage: abstract-reasoning
status: draft
---

# Primitive Data Types

## Core Idea
Primitive data types are the basic building blocks for storing information: integers (whole numbers), floats (decimals), booleans (true/false), and characters. Each type has a defined size and set of allowed values.

## Questions

```yaml
- question: "In a language that uses integer division, what is the result of 7 / 2?"
  type: multiple-choice
  options:
    - "3 — integer division truncates the fractional part, discarding the remainder"
    - "3.5 — division always produces the exact mathematical result"
    - "4 — integer division rounds to the nearest whole number"
    - "An error — you cannot divide an odd integer by 2"
  answer: 0
  explanation: "Integer division truncates toward zero — it drops the fractional part entirely rather than rounding. 7 / 2 = 3.5 mathematically, but integer division discards the 0.5 and returns 3. The result is not 4 (which would be rounding). This surprises many beginners and causes real bugs when programmers need a decimal result but accidentally use integer operands."

- question: "A student writes `result = 0.1 + 0.2` and then checks `result == 0.3`. What is the most likely outcome, and why?"
  type: multiple-choice
  options:
    - "False — 0.1 and 0.2 cannot be represented exactly in binary, so their sum introduces a small rounding error"
    - "True — modern processors perform decimal arithmetic precisely for simple values like 0.1"
    - "True — floating-point addition is exact for numbers with one decimal place"
    - "An error — equality comparisons are not defined for floating-point numbers"
  answer: 0
  explanation: "Floating-point numbers are stored in binary. The decimal value 0.1 has no exact binary representation (just as 1/3 has no exact decimal representation), so both 0.1 and 0.2 are stored as close approximations. Their sum is not exactly 0.3 — in Python, 0.1 + 0.2 evaluates to 0.30000000000000004. This is not a bug; it is a fundamental consequence of how floats are encoded. Programmers who treat floats as exact decimals encounter subtle comparison failures and accumulating rounding errors."

- question: "The character '7' and the integer 7 represent the same value in a program and can be used interchangeably."
  type: true-false
  answer: false
  explanation: "A character is a symbol from a character set, stored as a numeric code (ASCII 55 for '7'). An integer 7 is stored as the number 7. They are different types with different memory representations and different valid operations. You can do arithmetic with integer 7 (7 + 3 = 10), but the character '7' behaves differently under the same operation — producing a character offset result or an error depending on the language. The visual similarity masks a fundamental difference in meaning and behavior."

- question: "The type of a variable matters not only for what values it can hold, but also for how operations behave on those values."
  type: true-false
  answer: true
  explanation: "Type governs both storage and behavior. Integer division produces truncated integers; float division produces decimals. Adding two characters may concatenate them or offset their ASCII codes, not sum their visual digits. Boolean comparisons work differently than numeric comparisons. Choosing the wrong type can silently produce incorrect results — the program runs without error but computes the wrong answer. Type is a semantic contract about what the value means and what operations are valid."

- question: "Why does the type of a variable matter beyond just knowing what kind of value it holds? Give an example where the wrong type produces a surprising or incorrect result."
  type: short-answer
  answer: "Type determines which operations are valid and how they behave — not just what can be stored. A key example: using integer division when decimal precision is needed. If `total` and `count` are both integers, `average = total / count` silently truncates (7/2 = 3, not 3.5). Another: expecting 0.1 + 0.2 == 0.3 to be true for floats — it is not, due to binary rounding. In both cases the program runs without error but produces a wrong answer. The type shapes the meaning and behavior of every operation."
  explanation: "Type is a semantic contract: it tells the runtime what the value means and what computations are defined. Mixing types carelessly — treating a character as a number, expecting exact decimals from floats, or using integer division for fractional quantities — causes logic errors that produce no error messages, just silently wrong results. This is why choosing the right type from the start is as important as choosing the right variable name."
```

## Explainer

You already know that variables are named storage locations in a program. **Primitive data types** define what kind of value a variable can hold and what operations make sense for it. Think of a variable as a labeled box and the type as the shape of the box — an integer box holds whole numbers, a float box holds decimals, a boolean box holds only true or false, and a character box holds a single letter or symbol. The type determines not just what fits inside, but what you can do with it: you can add two integers, but you cannot divide a boolean by a character.

**Integers** store whole numbers like -3, 0, and 42. They support arithmetic operations — addition, subtraction, multiplication, and division — but integer division truncates the decimal part (7 / 2 gives 3, not 3.5, in most languages). **Floats** (or doubles) store numbers with decimal points like 3.14 or -0.001. They handle fractional values but introduce subtle rounding issues because computers represent decimals in binary — the value 0.1 cannot be stored exactly, which is why 0.1 + 0.2 might not equal exactly 0.3. This is not a bug; it is a fundamental consequence of how floating-point numbers are encoded in memory.

**Booleans** are the simplest type: they hold exactly two possible values, `true` or `false`. Despite their simplicity, booleans are everywhere — they control if-statements, loop conditions, and logical comparisons. When you write `x > 5`, the result is a boolean. **Characters** represent single symbols from a character set (like the letter 'A' or the digit '7' as text). A character is not the same as the number it might visually resemble: the character '7' and the integer 7 are stored differently and behave differently under operations.

Understanding primitive types matters because they affect how your program behaves in subtle ways. Mixing types without care — such as adding an integer to a float, or comparing a string to a number — produces either implicit conversions (which can surprise you) or errors (which stop your program). As you progress to type conversion and strings, you will learn how to move values between types deliberately. For now, the key insight is that every value in your program has a type, and that type governs what the value means and what you can do with it.
