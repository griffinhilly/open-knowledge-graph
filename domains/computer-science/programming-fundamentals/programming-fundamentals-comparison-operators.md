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

## Questions

```yaml
- question: "A programmer intends to check whether a variable x holds the value 5, but writes: if (x = 5). In most programming languages, what does this code actually do?"
  type: multiple-choice
  options:
    - "It compares x to 5 and executes the if-block if they are equal"
    - "It assigns the value 5 to x, then evaluates the assignment result (which is 5, treated as truthy)"
    - "It produces a syntax error because = is not a valid operator inside an if statement"
    - "It checks whether x was previously equal to 5 before any modifications"
  answer: 1
  explanation: "In most languages (C, C++, Java, JavaScript), a single = is the assignment operator, not a comparison. Writing x = 5 inside a condition assigns 5 to x and then evaluates the expression — since 5 is a non-zero (truthy) value, the if-block will execute regardless of x's original value. This is a common and dangerous bug. The intended code is x == 5. Some languages (Python) prevent this by not allowing assignment inside conditions; others (C-family) permit it silently."

- question: "In most programming languages, what does the expression (0.1 + 0.2 == 0.3) evaluate to?"
  type: multiple-choice
  options:
    - "true, because 0.1 + 0.2 is mathematically equal to 0.3"
    - "false, because floating-point numbers are stored with rounding errors that make exact equality unreliable"
    - "true in statically typed languages and false in dynamically typed languages"
    - "It causes a runtime error because floating-point values cannot be compared with =="
  answer: 1
  explanation: "This evaluates to false in most languages. Computers store floating-point numbers in binary, and most decimal fractions cannot be represented exactly — 0.1 and 0.2 each carry small rounding errors, and their sum does not equal the stored representation of 0.3. The correct approach for floating-point comparison is to check whether the absolute difference is smaller than some small threshold (e.g., Math.abs(a - b) < 0.0001). This is a fundamental property of IEEE 754 binary floating-point arithmetic, not a language quirk."

- question: "The expression (7 != 7) evaluates to true."
  type: true-false
  answer: false
  explanation: "The != operator tests inequality — it returns true if and only if the two values are different. Since 7 and 7 are the same value, 7 != 7 returns false. The expression is asking 'is 7 not equal to 7?' and the answer is no."

- question: "Comparison operators can only be meaningfully applied to integer values; applying them to strings or characters produces undefined behavior."
  type: true-false
  answer: false
  explanation: "Comparison operators work on many types beyond integers. Characters can be compared by their underlying encoding order (e.g., 'a' < 'b' is true in ASCII). Strings can often be compared alphabetically. Floating-point numbers can be compared (with the caveat about exact equality). The types that support comparison depend on the language, but integers are not special — the important limitation is the floating-point equality problem specifically."

- question: "Why do comparison operators return a boolean (true or false) rather than a number, and why does this design choice matter for programming?"
  type: short-answer
  answer: "Comparison operators return a boolean because they answer a fundamentally different kind of question than arithmetic operators. Arithmetic computes a new value from two inputs; comparison evaluates whether a relationship holds between two values. The boolean result — a yes-or-no answer — is exactly what decision-making structures (if statements, while loops, logical operators) need as input. If comparisons returned numbers, you would need an additional layer to interpret what the number means. By returning a boolean directly, the comparison becomes a statement the program can act on: 'if this condition is true, do this; otherwise, do that.' This is the foundation of all conditional logic."
  explanation: "The key insight is the shift from computing to asking. Arithmetic produces values; comparisons produce answers. Every if-statement, every loop condition, every filter operation — all rest on the ability to reduce a relationship to a single true/false that the program can branch on."
```

## Explainer

You already know how arithmetic operators take two numbers and produce a new number — for example, `5 + 3` yields `8`. **Comparison operators** work similarly in structure, but instead of producing a number, they produce a **boolean**: either `true` or `false`. Think of them as questions you ask about two values. `5 > 3` is asking "is five greater than three?" and the answer is `true`. `5 == 3` asks "are these equal?" and the answer is `false`. This shift from computing values to asking yes-or-no questions is what makes decision-making in programs possible.

There are six comparison operators to learn, and they come in natural pairs. **Equality** (`==`) and **inequality** (`!=`) test whether two values are the same or different. **Less than** (`<`) and **greater than** (`>`) test strict ordering. **Less than or equal** (`<=`) and **greater than or equal** (`>=`) include the boundary case where values are exactly equal. A common early mistake is confusing the assignment operator `=` with the equality operator `==`. Assignment stores a value; equality tests whether two values match. Writing `x = 5` puts 5 into x, while `x == 5` asks whether x currently holds 5.

Comparison operators work on more than just integers. You can compare floating-point numbers, characters (by their underlying encoding order), and in many languages, strings (alphabetically). However, comparing floating-point numbers for exact equality is unreliable because of how computers store decimals — `0.1 + 0.2 == 0.3` often returns `false` due to rounding. For floats, check whether the difference is smaller than some tiny threshold instead.

The real power of comparison operators emerges when you combine them with control flow. Every `if` statement you will write depends on a comparison (or a combination of comparisons) evaluating to `true` or `false`. When you later learn **logical operators** like `&&` (and) and `||` (or), you will chain comparisons together to express complex conditions like "is the temperature between 60 and 80?" as `temp >= 60 && temp <= 80`. But that all rests on the foundation here: each individual comparison reduces a relationship between two values to a single boolean answer that your program can act on.
