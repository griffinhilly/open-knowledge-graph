---
id: programming-fundamentals-arithmetic-operators
title: Arithmetic Operators
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: programming-fundamentals-variables-assignment
  type: hard
builds-toward:
- programming-fundamentals-operator-precedence
- programming-fundamentals-comparison-operators
tags:
- operators
- arithmetic
- math
stage: abstract-reasoning
status: draft
---

# Arithmetic Operators

## Core Idea
Arithmetic operators (+, -, *, /, %) perform mathematical operations on numbers. Addition and subtraction add/remove values; multiplication and division scale values; modulo (%) returns the remainder after division.

## Explainer

Now that you understand variables and assignment, arithmetic operators are how you make those stored values do useful work. You already know that a variable holds a value and that you can assign new values to it. Arithmetic operators let you compute new values from existing ones: `total = price * quantity` takes two variables you've already stored and produces a third. The result of any arithmetic expression is itself a value that can be assigned, printed, or passed along — it slots right into the variable system you already know.

The five core operators map directly to the math you already know, with one newcomer. **Addition** (`+`) and **subtraction** (`-`) work exactly as expected. **Multiplication** (`*`) and **division** (`/`) scale values up or down. The one that trips people up is **modulo** (`%`), which returns the remainder after integer division. Think of it this way: `17 % 5` asks "if I divide 17 into groups of 5, what's left over?" The answer is 2, because 5 goes into 17 three times (15) with 2 remaining. Modulo is surprisingly useful — it can tell you whether a number is even (`n % 2 == 0`), cycle through a fixed range, or extract digits from a number.

One critical detail: division behaves differently depending on the types involved. In many languages, dividing two integers performs **integer division**, which truncates the decimal part — so `7 / 2` gives `3`, not `3.5`. This is not a bug; it is a deliberate design choice rooted in how computers represent numbers. If you want the decimal result, at least one operand must be a floating-point number (e.g., `7.0 / 2`). Getting surprised by integer division is one of the most common sources of logic errors for beginners.

Finally, arithmetic operators combine with assignment in a natural way. Instead of writing `count = count + 1`, most languages offer shorthand like `count += 1`. These **compound assignment operators** (`+=`, `-=`, `*=`, `/=`, `%=`) are just syntactic sugar — they do exactly the same thing as writing the long form. They exist because updating a variable based on its current value is so common that a shorter notation pays for itself in readability. Once you're comfortable with these five operators and how they interact with variable assignment, you have the basic machinery to express any computation.
