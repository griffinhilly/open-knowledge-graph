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

## Explainer

You already know that variables are named storage locations in a program. **Primitive data types** define what kind of value a variable can hold and what operations make sense for it. Think of a variable as a labeled box and the type as the shape of the box — an integer box holds whole numbers, a float box holds decimals, a boolean box holds only true or false, and a character box holds a single letter or symbol. The type determines not just what fits inside, but what you can do with it: you can add two integers, but you cannot divide a boolean by a character.

**Integers** store whole numbers like -3, 0, and 42. They support arithmetic operations — addition, subtraction, multiplication, and division — but integer division truncates the decimal part (7 / 2 gives 3, not 3.5, in most languages). **Floats** (or doubles) store numbers with decimal points like 3.14 or -0.001. They handle fractional values but introduce subtle rounding issues because computers represent decimals in binary — the value 0.1 cannot be stored exactly, which is why 0.1 + 0.2 might not equal exactly 0.3. This is not a bug; it is a fundamental consequence of how floating-point numbers are encoded in memory.

**Booleans** are the simplest type: they hold exactly two possible values, `true` or `false`. Despite their simplicity, booleans are everywhere — they control if-statements, loop conditions, and logical comparisons. When you write `x > 5`, the result is a boolean. **Characters** represent single symbols from a character set (like the letter 'A' or the digit '7' as text). A character is not the same as the number it might visually resemble: the character '7' and the integer 7 are stored differently and behave differently under operations.

Understanding primitive types matters because they affect how your program behaves in subtle ways. Mixing types without care — such as adding an integer to a float, or comparing a string to a number — produces either implicit conversions (which can surprise you) or errors (which stop your program). As you progress to type conversion and strings, you will learn how to move values between types deliberately. For now, the key insight is that every value in your program has a type, and that type governs what the value means and what you can do with it.
