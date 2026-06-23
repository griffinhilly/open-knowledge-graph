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
- id: arithmetic-operators
  type: soft
- id: numeric-types
  type: hard
- id: type-system-basics
  type: soft
builds-toward:
- string-operations
- input-output
- error-handling-exceptions
- comparison-operators
tags:
- casting
- type conversion
- int
- float
- str
- coercion
stage: formal-systems
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

## Questions

```yaml
- question: "A Python program prompts the user to enter their age and then adds 1: age = input('Enter your age: ') + 1. What happens when the user types '25'?"
  type: multiple-choice
  options:
    - "The program returns 26, because Python automatically converts the string to an integer"
    - "The program raises a TypeError, because you cannot add an integer to a string"
    - "The program returns '251', concatenating the string with the integer"
    - "The program returns 25, because addition is undefined between a string and integer"
  answer: 1
  explanation: "In Python, input() always returns a string. The string '25' cannot be added to the integer 1 — Python raises a TypeError because these types are incompatible for addition. This is the core insight: user input always arrives as a string and must be explicitly converted with int() before arithmetic. The fix is: age = int(input('Enter your age: ')) + 1."

- question: "What does int(7.9) evaluate to in Python?"
  type: multiple-choice
  options:
    - "8, because int() rounds to the nearest integer"
    - "7, because int() truncates toward zero"
    - "8.0, because the result remains a float"
    - "A ValueError, because 7.9 is not a valid integer representation"
  answer: 1
  explanation: "int() applied to a float truncates (chops off) the decimal portion — it does not round. int(7.9) → 7, and int(-7.9) → -7 (not -8). This surprises many beginners who expect mathematical rounding behavior. Truncation always moves toward zero, regardless of how close the decimal is to the next integer."

- question: "int('3.14') successfully converts the string '3.14' to the integer 3 in Python."
  type: true-false
  answer: false
  explanation: "int() cannot convert a string containing a decimal point directly to an integer — it raises a ValueError. The string '3.14' must first be converted to a float: float('3.14') gives 3.14, and then int(3.14) gives 3. You cannot skip the intermediate step."

- question: "Any value entered by a user at the keyboard arrives in a Python program as a string, regardless of what they typed."
  type: true-false
  answer: true
  explanation: "This is one of the most important facts about console input. input() always returns a string. If the user types '42', the program receives the string '42', not the integer 42. If the user types '3.14', the program receives the string '3.14'. Arithmetic on these values without explicit conversion will fail or produce unexpected results."

- question: "Why does int('3.14') fail in Python, and what is the correct two-step approach to convert the string '3.14' to the integer 3?"
  type: short-answer
  answer: "int() can only parse strings that represent whole numbers (like '3' or '-10'). A string containing a decimal point is not a valid integer literal, so Python raises a ValueError. The correct approach is to first convert to a float — float('3.14') gives 3.14 — and then convert that float to an integer — int(3.14) gives 3. The two-step process passes through a valid intermediate type before truncating."
  explanation: "This two-step requirement reveals an important principle: type conversions follow valid intermediate states. You cannot jump from a decimal-containing string directly to an integer because those types are too 'far apart' in their representations. Going string→float→int follows a logical path through a compatible intermediate type."
```

## Explainer

You already know that values in a program have types — integers, floats, strings, booleans — and that operators behave differently depending on those types. But what happens when you need to combine values of different types, or when data arrives in one type and you need it in another? This is where **type conversion** (also called **casting**) comes in: explicitly transforming a value from one type to another using built-in functions like `int()`, `float()`, and `str()`.

The most common scenario is processing user input. When a program reads from the keyboard, the result is always a string — even if the user typed `42`. To do arithmetic with that input, you must convert it: `age = int(input("Enter your age: "))`. Without the `int()` call, `age` would hold the string `"42"`, and adding 1 to it would either concatenate the string or raise an error, depending on the language. Going the other direction, `str(42)` turns the integer into the string `"42"`, which you can then concatenate into a message like `"You are " + str(42) + " years old"`.

Not every conversion makes sense, and the language will tell you so with an error. `int("hello")` fails because there is no meaningful integer for arbitrary text. Even `int("3.14")` fails in most languages — you cannot jump directly from a decimal-containing string to an integer. The correct path is `int(float("3.14"))`, converting to float first, then truncating to int. Notice the word **truncating**: `int(3.9)` produces `3`, not `4`. It chops off the decimal portion rather than rounding. This surprises many beginners who expect mathematical rounding behavior.

Some languages also perform **implicit conversion** (or **coercion**), automatically converting types when it seems safe. In Python, `3 + 2.5` silently promotes the integer `3` to `3.0` before adding, yielding `5.5`. This is convenient, but implicit conversion can also hide bugs — JavaScript's `"5" + 3` produces the string `"53"` instead of the number `8`, because it coerces the number to a string for concatenation. Understanding when your language converts implicitly versus when you must convert explicitly is essential for writing code that behaves as you intend.
