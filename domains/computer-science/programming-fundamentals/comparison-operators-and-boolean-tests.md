---
id: comparison-operators-and-boolean-tests
title: Comparison Operators and Boolean Tests
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: operators-and-expressions
  type: hard
- id: boolean-logic-programming
  type: hard
builds-toward:
- if-else-branching-logic
- conditional-logic-chains
tags:
- comparison
- boolean
- logic
stage: formal-systems
status: draft
---

# Comparison Operators and Boolean Tests

## Core Idea
Comparison operators (<, >, ==, !=, <=, >=) return boolean values (true or false). These form the basis of conditional logic. Subtle differences exist: = (assignment) vs == (comparison) is a common source of bugs.

## How It's Best Learned
Build truth tables for comparisons; test edge cases like comparing strings and numbers; deliberately write == instead of = to feel the error.

## Common Misconceptions
That = and == are interchangeable; that comparison of strings is lexicographic not alphabetic (issues with case sensitivity); that 5 == '5' is true (it's false in typed languages).

## Explainer

You already know how operators and expressions work, and you understand that boolean values represent true or false. **Comparison operators** are the bridge between these two concepts: they take two values, compare them, and produce a boolean result. Every conditional statement you'll ever write — every `if`, every `while` loop condition — ultimately depends on a comparison evaluating to true or false. The six standard comparison operators are **less than** (`<`), **greater than** (`>`), **equal to** (`==`), **not equal to** (`!=`), **less than or equal** (`<=`), and **greater than or equal** (`>=`).

The most critical distinction for beginners is between `=` and `==`. The single equals sign (`=`) is **assignment** — it stores a value in a variable. The double equals sign (`==`) is **comparison** — it tests whether two values are the same and returns a boolean. Writing `x = 5` sets x to 5. Writing `x == 5` asks "is x equal to 5?" and returns true or false. Accidentally using `=` where you meant `==` is one of the most common bugs in programming. In some languages like C, this mistake compiles without error and silently does the wrong thing (it assigns the value and then treats the result as a boolean). Python avoids this by making assignment inside conditions a syntax error.

Comparisons work straightforwardly with numbers — `3 < 5` is true, `7 >= 7` is true — but they get subtler with other types. **String comparison** is **lexicographic**, meaning strings are compared character by character using their underlying character codes (like ASCII or Unicode values). This means `"apple" < "banana"` is true (a comes before b), but `"Banana" < "apple"` is also true because uppercase letters have lower character codes than lowercase ones. Comparing values of different types depends on the language: Python will refuse to compare a string to a number (`"5" > 3` raises an error), while JavaScript will silently convert types and produce surprising results (`"5" > 3` is true because it converts the string to a number).

You can combine multiple comparisons using the boolean operators you already know — `and`, `or`, and `not`. For example, to check whether a value falls within a range, you write `x >= 0 and x <= 100`. Python uniquely allows the more readable chained form: `0 <= x <= 100`, which works the way you'd read it in math. Understanding how comparisons compose with boolean logic is what makes conditional expressions powerful: you can express arbitrarily complex conditions like "the user is logged in and either has admin privileges or owns this resource" as a single boolean expression built from comparisons.
