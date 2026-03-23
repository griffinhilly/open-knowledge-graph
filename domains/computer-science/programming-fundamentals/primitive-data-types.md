---
id: primitive-data-types
title: Primitive Data Types
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: variables-and-assignment
  type: hard
builds-toward:
- operators-and-expressions
- type-conversion
- string-basics
tags:
- types
- integers
- floats
- booleans
- characters
stage: formal-systems
status: validated
---

# Primitive Data Types

## Core Idea
Primitive data types are the basic building blocks of data in a program: integers (whole numbers), floating-point numbers (decimals), booleans (true/false), and characters or strings. Every value in a program has a type that determines what operations are valid and how the value is stored in memory. Strongly typed languages enforce type rules at compile time, while dynamically typed languages check types at runtime. Choosing the right type matters for correctness and efficiency.

## How It's Best Learned
Write short programs that declare variables of each type and print them. Try operations that mix types (e.g., integer + float) and observe the results. Compare how different languages handle the same type questions.

## Common Misconceptions
- Confusing integer division with float division (e.g., 5/2 = 2 in many languages, not 2.5).
- Assuming all numbers are the same type.
- Thinking booleans are just integers without understanding their distinct semantic role.

## Questions

```yaml
- question: "A programmer writes `result = 7 / 2` in a language where both 7 and 2 are integers. What is the value of `result`?"
  type: multiple-choice
  options:
    - "3.5"
    - "3"
    - "4"
    - "This is a syntax error — you cannot divide two integers"
  answer: 1
  explanation: "Integer division truncates the fractional part rather than rounding, so 7/2 = 3. To get 3.5, at least one operand must be a float (e.g., 7.0/2 or float(7)/2). This surprises many beginners who assume division always produces a decimal result — option 0 is the most tempting wrong answer because it's mathematically correct for real-number division, but type-constrained integer division is a different operation."

- question: "A language that infers a variable's type from the assigned value and checks type rules when operations execute is called:"
  type: multiple-choice
  options:
    - "Statically typed"
    - "Dynamically typed"
    - "Weakly typed"
    - "Polymorphic"
  answer: 1
  explanation: "Dynamically typed languages (like Python) infer type from value and check rules at runtime. Statically typed languages (like Java or C) require explicit declarations and catch type errors before the program runs. 'Weakly typed' describes how strictly type conversions are enforced — a separate concept — and polymorphism describes how operations can work on multiple types, which is unrelated to when type-checking occurs."

- question: "In most programming languages, the expression `0.1 + 0.2` evaluates to exactly `0.3`."
  type: true-false
  answer: false
  explanation: "This is false. Floating-point numbers are stored in binary, and most decimal fractions cannot be represented exactly. `0.1 + 0.2` produces `0.30000000000000004` in most languages — not a bug, but a fundamental limitation of binary floating-point representation. It matters in practice: comparing floats for exact equality (`x == 0.3`) is unreliable; you must use an epsilon comparison or a decimal library instead."

- question: "Booleans in modern typed languages are simply a special name for the integers 0 and 1."
  type: true-false
  answer: false
  explanation: "While some older languages (like C) used integers for boolean values, modern type systems treat booleans as a distinct type with a distinct semantic role: representing truth or falsity, not quantity. The confusion conflates implementation detail with conceptual meaning. A boolean answers 'is this condition true?' — a fundamentally different question from 'how many?' Using integers as booleans obscures intent and invites errors like using 2 (truthy in most languages) where only 0 or 1 is expected."

- question: "Why does the type of a value matter in programming, beyond just labeling it? Give a concrete example of a type affecting what an operation produces."
  type: short-answer
  answer: "Type determines which operations are valid and what they produce. For example, `5 + 3` on integers yields 8 (arithmetic sum), while `'5' + '3'` on strings yields '53' (concatenation) in many languages — the same operator symbol performs fundamentally different actions depending on operand types. Without types, the computer cannot know which behavior is intended, and silent type confusion causes bugs that are difficult to trace."
  explanation: "This is the core insight: types are not labels, they are specifications of behavior. Integer division vs. float division, string concatenation vs. numeric addition — these distinctions explain entire categories of beginner bugs. Understanding types is what allows you to predict, rather than guess, what a program will do."
```

## Explainer

From your work with variables and assignment, you know that variables hold values in memory. But not all values are the same kind of thing — the number 42, the decimal 3.14, the word "hello", and the truth value `true` are fundamentally different, and the computer needs to know which kind it's dealing with. **Primitive data types** are the basic categories that classify these values, and every programming language has them as its foundation.

**Integers** store whole numbers: -3, 0, 42, 1000000. They support arithmetic operations like addition, subtraction, multiplication, and division. A critical detail: in many languages, dividing two integers gives an integer result, so `7 / 2` produces `3`, not `3.5` — the decimal part is simply dropped. This is **integer division**, and it catches beginners constantly. **Floating-point numbers** (floats) store decimal values: 3.14, -0.001, 2.0. They handle the fractional values that integers cannot, but they come with their own surprise — floats are approximations. The expression `0.1 + 0.2` produces `0.30000000000000004` in most languages, not `0.3`, because of how decimal fractions are represented in binary. This isn't a bug; it's a fundamental limitation of how computers store non-integer numbers.

**Booleans** hold exactly two values: true and false. They're the result of comparisons (`x > 5` evaluates to true or false) and the basis for all decision-making in programs. **Characters** represent individual letters, digits, or symbols ('A', '7', '!'). In some languages like Python, there's no separate character type — single characters are just strings of length one. **Strings** store sequences of characters ("hello", "42", "true") and are technically not always primitive, but they're so fundamental that most languages treat them as basic building blocks.

The type of a value determines **what operations are valid**. You can add two integers (5 + 3 = 8), and you can concatenate two strings ("hello" + " world" = "hello world"), but adding an integer to a string means different things in different languages — some concatenate ("5" + "3" = "53"), some throw an error, some convert automatically. This is where **type systems** diverge. Statically typed languages like Java or C require you to declare each variable's type upfront (`int score = 42;`), catching type errors before the program runs. Dynamically typed languages like Python infer the type from the value assigned (`score = 42`), checking types only when operations execute. Neither approach is inherently better — they trade early error detection for flexibility. Understanding types prevents a whole category of bugs and is essential as you move into operators, expressions, and type conversions.
