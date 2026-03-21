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

## Questions

```yaml
- question: "A program reads a user's age from keyboard input and stores it in the variable `age`. When the program tries to compute `age + 1`, it crashes with a type error. What is most likely the cause?"
  type: multiple-choice
  options:
    - "The variable name `age` is reserved by the language and cannot be used for arithmetic"
    - "User input is always read as a string, so `age` holds the text '25' rather than the number 25; you must convert it with int(age) before doing arithmetic"
    - "Adding 1 to a user-provided value requires a special input-handling function"
    - "Floats should always be used for age calculations to prevent integer overflow errors"
  answer: 1
  explanation: "When a program reads input from a keyboard or file, the value almost always arrives as a string — even if it looks like a number. The string '25' and the integer 25 are entirely different values: you cannot do arithmetic with a string. Most languages will raise a type error when you try to add a number to a string. The fix is explicit conversion: int(age) turns the string '25' into the integer 25. This is one of the most common beginner bugs and exactly the kind of error type awareness prevents."

- question: "Why does `0.1 + 0.2` produce something like `0.30000000000000004` in most programming languages, rather than exactly `0.3`?"
  type: multiple-choice
  options:
    - "It is a bug in the standard math library that major languages haven't yet fixed"
    - "Floats use binary representation with limited precision, so many decimal fractions cannot be stored exactly — the result is a tiny rounding error"
    - "The interpreter prioritizes calculation speed over precision when adding decimals"
    - "This only happens in older languages; modern languages store floating-point numbers exactly"
  answer: 1
  explanation: "Floats are stored in binary using a fixed number of bits (typically 64). Just as 1/3 cannot be expressed exactly as a decimal (it becomes 0.3333...), many decimal fractions like 0.1 cannot be expressed exactly in binary. The value stored is a very close approximation, and when you add two approximations, the tiny errors compound. This is not a bug — it is a fundamental property of floating-point representation. For most purposes the error is negligible, but for money calculations or exact comparisons, integers or specialized decimal types are needed."

- question: "In most programming languages, evaluating '5' + '3' produces '53' (string concatenation) rather than 8 (arithmetic addition)."
  type: true-false
  answer: true
  explanation: "When both operands are strings, the + operator concatenates them — it joins the two character sequences end to end. The string '5' is the text character five, not the number 5. This is why the string '5' and the integer 5 are entirely different values with entirely different valid operations. Understanding this distinction prevents the class of bugs that arise when numeric-looking data arrives as text (from user input, file reading, or JSON parsing) and is used in arithmetic without conversion."

- question: "Using floats instead of integers is always the safer choice for numeric variables, because floats can represent more values including decimals."
  type: true-false
  answer: false
  explanation: "Floats represent more values, but with limited precision — meaning they introduce the possibility of rounding errors that integers completely avoid. For counting discrete things (loop iterations, array indices, number of items), integers are exact and therefore safer. Using a float as a loop counter is risky because accumulated floating-point errors might cause a loop that increments by 0.1 to miss its termination condition of 1.0. The rule is: use integers when counting discrete things; use floats when measuring continuous quantities where small errors are acceptable."

- question: "Why should you use an integer rather than a float to represent a loop counter, and what can go wrong if you use a float instead?"
  type: short-answer
  answer: "A loop counter must be exact — you need to know precisely when you've completed 0, 1, 2, 3... iterations. Integers are exact by design; adding 1 to an integer always produces a reliable result. Floats have limited binary precision, so repeated addition of small values can accumulate rounding errors. For example, a loop that increments by 0.1 may not reach exactly 1.0 after ten iterations — it might land on 0.9999999999999999 or 1.0000000000000002 — causing a termination condition to fail or producing an off-by-one error. For anything requiring discrete, exact counting, an integer is both correct and semantically appropriate."
  explanation: "Type choice is not just about what values are possible but about what guarantees each type provides. Integers guarantee exact arithmetic for whole numbers; floats sacrifice exactness for range and fractional representation. Choosing the right type for the job eliminates an entire category of subtle bugs."
```

## Explainer

You already know that data in a program has types. Now let's look at the three most common primitive types and understand what makes each one distinct. An **integer** stores a whole number — no decimal point, no fractional part. Examples: `0`, `-7`, `42`, `1000000`. Integers are exact: `3 + 4` always equals `7`, with no rounding or approximation. They are the right choice whenever you are counting discrete things — number of students, loop iterations, array indices.

A **float** (short for floating-point number) stores a number with a decimal part: `3.14`, `-0.001`, `2.0`. Floats can represent a huge range of values, from the astronomically large to the microscopically small. But they come with a critical tradeoff: **limited precision**. Internally, a float is stored in binary using a fixed number of bits, which means many decimal fractions cannot be represented exactly. Try `0.1 + 0.2` in most languages and you will get something like `0.30000000000000004` instead of `0.3`. This is not a bug — it is a fundamental property of how floating-point numbers work. For most calculations (physics, graphics, statistics) the tiny errors are negligible. But for money or exact comparisons, integers or specialized decimal types are safer.

A **string** stores text — a sequence of characters enclosed in quotes: `"hello"`, `'42'`, `"Jane Doe"`. Here is the crucial point: the string `"5"` and the integer `5` are entirely different values. The string `"5"` is a text character — you can concatenate it with other strings (`"5" + "3"` gives `"53"`, not `8`), but you cannot do arithmetic with it. The integer `5` is a number — you can add it, multiply it, use it as a loop counter. Most languages will refuse to add a string to an integer directly, and for good reason: the operation is ambiguous. You need to explicitly convert between types using functions like `int("5")` or `str(5)`.

Understanding these distinctions prevents an entire class of bugs. When you read input from a user or a file, it almost always arrives as a string, even if it looks like a number. Before doing math with it, you must convert it to an integer or float. When you choose a type for a variable, ask: am I counting something discrete (integer), measuring something continuous (float), or storing text (string)? The answer determines which operations are valid, how much memory is used, and whether subtle precision bugs can creep in.
