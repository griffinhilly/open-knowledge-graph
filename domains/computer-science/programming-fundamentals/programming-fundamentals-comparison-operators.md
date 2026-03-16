---
id: programming-fundamentals-comparison-operators
title: Comparison Operators
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: programming-fundamentals-arithmetic-operators
  type: hard
builds-toward:
- programming-fundamentals-logical-operators
- programming-fundamentals-if-else-statements
tags:
- operators
- comparison
- boolean
stage: abstract-reasoning
status: draft
---

# Comparison Operators

## Core Idea
Comparison operators (==, !=, <, >, <=, >=) test relationships between values and return a boolean result (true or false). These are essential for making decisions in code.

## Explainer

You already know how arithmetic operators take two numbers and produce a new number — for example, `5 + 3` yields `8`. **Comparison operators** work similarly in structure, but instead of producing a number, they produce a **boolean**: either `true` or `false`. Think of them as questions you ask about two values. `5 > 3` is asking "is five greater than three?" and the answer is `true`. `5 == 3` asks "are these equal?" and the answer is `false`. This shift from computing values to asking yes-or-no questions is what makes decision-making in programs possible.

There are six comparison operators to learn, and they come in natural pairs. **Equality** (`==`) and **inequality** (`!=`) test whether two values are the same or different. **Less than** (`<`) and **greater than** (`>`) test strict ordering. **Less than or equal** (`<=`) and **greater than or equal** (`>=`) include the boundary case where values are exactly equal. A common early mistake is confusing the assignment operator `=` with the equality operator `==`. Assignment stores a value; equality tests whether two values match. Writing `x = 5` puts 5 into x, while `x == 5` asks whether x currently holds 5.

Comparison operators work on more than just integers. You can compare floating-point numbers, characters (by their underlying encoding order), and in many languages, strings (alphabetically). However, comparing floating-point numbers for exact equality is unreliable because of how computers store decimals — `0.1 + 0.2 == 0.3` often returns `false` due to rounding. For floats, check whether the difference is smaller than some tiny threshold instead.

The real power of comparison operators emerges when you combine them with control flow. Every `if` statement you will write depends on a comparison (or a combination of comparisons) evaluating to `true` or `false`. When you later learn **logical operators** like `&&` (and) and `||` (or), you will chain comparisons together to express complex conditions like "is the temperature between 60 and 80?" as `temp >= 60 && temp <= 80`. But that all rests on the foundation here: each individual comparison reduces a relationship between two values to a single boolean answer that your program can act on.
