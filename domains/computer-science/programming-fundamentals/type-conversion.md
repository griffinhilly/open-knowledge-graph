---
id: type-conversion
title: Type Conversion and Casting
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: primitive-data-types
  type: hard
- id: operators-and-expressions
  type: hard
builds-toward:
- string-operations
- basic-input-output
- error-handling-exceptions
tags:
- casting
- type conversion
- int
- float
- str
- coercion
stage: abstract-reasoning
status: validated
---

# Type Conversion and Casting

## Core Idea
Type conversion (casting) transforms a value from one data type to another. Explicit conversion uses functions like int(), float(), and str() to request a specific type. Implicit conversion (coercion) happens automatically when a language combines compatible types (e.g., adding an int to a float). Not all conversions are valid — converting 'hello' to int raises an error. Understanding when and how to convert types is essential for processing user input and mixing numeric types correctly.

## How It's Best Learned
Write a calculator that reads string input, converts to numbers, computes, and formats the result as a string. Deliberately trigger conversion errors and read the error messages carefully.

## Common Misconceptions
- Assuming int('3.14') succeeds — it does not in most languages; float('3.14') must come first.
- Thinking int(3.9) rounds to 4 — it truncates to 3.
- Not realizing that all console input arrives as a string and must be explicitly converted.

## Explainer

You already know that values in a program have types — integers, floats, strings, booleans — and that operators behave differently depending on those types. But what happens when you need to combine values of different types, or when data arrives in one type and you need it in another? This is where **type conversion** (also called **casting**) comes in: explicitly transforming a value from one type to another using built-in functions like `int()`, `float()`, and `str()`.

The most common scenario is processing user input. When a program reads from the keyboard, the result is always a string — even if the user typed `42`. To do arithmetic with that input, you must convert it: `age = int(input("Enter your age: "))`. Without the `int()` call, `age` would hold the string `"42"`, and adding 1 to it would either concatenate the string or raise an error, depending on the language. Going the other direction, `str(42)` turns the integer into the string `"42"`, which you can then concatenate into a message like `"You are " + str(42) + " years old"`.

Not every conversion makes sense, and the language will tell you so with an error. `int("hello")` fails because there is no meaningful integer for arbitrary text. Even `int("3.14")` fails in most languages — you cannot jump directly from a decimal-containing string to an integer. The correct path is `int(float("3.14"))`, converting to float first, then truncating to int. Notice the word **truncating**: `int(3.9)` produces `3`, not `4`. It chops off the decimal portion rather than rounding. This surprises many beginners who expect mathematical rounding behavior.

Some languages also perform **implicit conversion** (or **coercion**), automatically converting types when it seems safe. In Python, `3 + 2.5` silently promotes the integer `3` to `3.0` before adding, yielding `5.5`. This is convenient, but implicit conversion can also hide bugs — JavaScript's `"5" + 3` produces the string `"53"` instead of the number `8`, because it coerces the number to a string for concatenation. Understanding when your language converts implicitly versus when you must convert explicitly is essential for writing code that behaves as you intend.
