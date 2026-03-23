---
id: comparison-operators
title: Comparison Operators and Boolean Tests
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: arithmetic-operators
  type: hard
- id: boolean-logic
  type: hard
- id: numeric-types
  type: soft
builds-toward:
- else-if-chains
- logical-operators
- conditional-statements
tags:
- comparison
- boolean
- logic
stage: abstract-reasoning
status: validated
---
# Comparison Operators and Boolean Tests

## Core Idea
Comparison operators (<, >, ==, !=, <=, >=) return boolean values (true or false). These form the basis of conditional logic. Subtle differences exist: = (assignment) vs == (comparison) is a common source of bugs.

## How It's Best Learned
Build truth tables for comparisons; test edge cases like comparing strings and numbers; deliberately write == instead of = to feel the error.

## Common Misconceptions
That = and == are interchangeable; that comparison of strings is lexicographic not alphabetic (issues with case sensitivity); that 5 == '5' is true (it's false in typed languages).

## Questions

```yaml
- question: "A programmer writes `if (x = 5) { doSomething(); }` intending to check whether x equals 5. In a language like C, what actually happens?"
  type: multiple-choice
  options:
    - "The condition checks whether x is equal to 5 and works as intended"
    - "x is assigned the value 5 and the condition evaluates to true (non-zero), so doSomething() always runs regardless of x's prior value"
    - "A compile error occurs because = is not allowed inside a conditional"
    - "The program compares x to 5 but also stores 5 in x as a side effect"
  answer: 1
  explanation: "In C, `=` is the assignment operator — it stores a value and returns that value. So `x = 5` stores 5 in x and evaluates to 5. Since 5 is non-zero (truthy), the condition is always true. This is one of the most common silent bugs in C programming: the code compiles without error, runs without crashing, and does the wrong thing. Python avoids this by making assignment inside a condition a syntax error, which is why `=` inside `if` is legal in C but illegal in Python."

- question: "What does Python return for the expression `'Banana' < 'apple'`?"
  type: multiple-choice
  options:
    - "False — 'banana' comes after 'apple' alphabetically, so 'Banana' must be greater"
    - "False — Python compares string lengths when letter comparisons are ambiguous"
    - "True — uppercase letters have lower Unicode values than lowercase letters, so 'B' < 'a'"
    - "An error — Python cannot compare strings with mixed case using <"
  answer: 2
  explanation: "String comparison is lexicographic, comparing character by character using Unicode values. Uppercase letters (A=65, B=66) have lower Unicode values than lowercase letters (a=97). So 'B' < 'a' is true, which means 'Banana' < 'apple' evaluates to True — even though 'banana' comes after 'apple' alphabetically. This surprises many beginners who expect string comparison to be purely alphabetical. Case sensitivity is a fundamental property of lexicographic ordering."

- question: "In Python, `'Banana' < 'apple'` evaluates to True, even though 'banana' comes after 'apple' in the dictionary."
  type: true-false
  answer: true
  explanation: "String comparison uses Unicode (character code) ordering, not dictionary alphabetical order. Uppercase letters have lower code values than lowercase letters — 'B' is 66, 'a' is 97. So the comparison 'B' < 'a' is true, making 'Banana' < 'apple' evaluate to True. To compare strings case-insensitively (as a dictionary would), you'd need to normalize them first: `'Banana'.lower() < 'apple'.lower()`."

- question: "The single equals sign (=) and the double equals sign (==) can be used interchangeably in conditional expressions in most programming languages."
  type: true-false
  answer: false
  explanation: "These operators do fundamentally different things. `=` is assignment — it stores a value in a variable. `==` is comparison — it tests equality and returns a boolean. Confusing them is one of the most common beginner bugs. In Python, using `=` inside an `if` condition raises a SyntaxError. In C, it silently assigns the value and evaluates the result as a condition, almost always doing the wrong thing. They are never interchangeable."

- question: "Why do comparison operators return a boolean value, and how does this connect them to conditional statements like `if`?"
  type: short-answer
  answer: "Comparison operators evaluate a relationship between two values and produce a true/false result. Conditional statements like `if` need a condition they can branch on — they execute the body when the condition is true and skip it when false. Comparisons produce exactly this: a boolean that the `if` can act on. This is why comparisons are the building blocks of conditional logic: expressions like `x > 0`, `name == 'admin'`, or `score >= 60` all reduce to true or false, which is the only kind of value a branch needs."
  explanation: "This connection is not accidental — it's by design. Boolean values (true/false) are the common currency of control flow. Comparisons are what produce booleans from non-boolean data (numbers, strings, etc.), which is why they are the bridge between the data a program holds and the decisions it makes. Every `if`, `while`, and `for` loop condition ultimately depends on a boolean, and comparisons are the primary mechanism for generating one."
```

## Explainer

You already know how operators and expressions work, and you understand that boolean values represent true or false. **Comparison operators** are the bridge between these two concepts: they take two values, compare them, and produce a boolean result. Every conditional statement you'll ever write — every `if`, every `while` loop condition — ultimately depends on a comparison evaluating to true or false. The six standard comparison operators are **less than** (`<`), **greater than** (`>`), **equal to** (`==`), **not equal to** (`!=`), **less than or equal** (`<=`), and **greater than or equal** (`>=`).

The most critical distinction for beginners is between `=` and `==`. The single equals sign (`=`) is **assignment** — it stores a value in a variable. The double equals sign (`==`) is **comparison** — it tests whether two values are the same and returns a boolean. Writing `x = 5` sets x to 5. Writing `x == 5` asks "is x equal to 5?" and returns true or false. Accidentally using `=` where you meant `==` is one of the most common bugs in programming. In some languages like C, this mistake compiles without error and silently does the wrong thing (it assigns the value and then treats the result as a boolean). Python avoids this by making assignment inside conditions a syntax error.

Comparisons work straightforwardly with numbers — `3 < 5` is true, `7 >= 7` is true — but they get subtler with other types. **String comparison** is **lexicographic**, meaning strings are compared character by character using their underlying character codes (like ASCII or Unicode values). This means `"apple" < "banana"` is true (a comes before b), but `"Banana" < "apple"` is also true because uppercase letters have lower character codes than lowercase ones. Comparing values of different types depends on the language: Python will refuse to compare a string to a number (`"5" > 3` raises an error), while JavaScript will silently convert types and produce surprising results (`"5" > 3` is true because it converts the string to a number).

You can combine multiple comparisons using the boolean operators you already know — `and`, `or`, and `not`. For example, to check whether a value falls within a range, you write `x >= 0 and x <= 100`. Python uniquely allows the more readable chained form: `0 <= x <= 100`, which works the way you'd read it in math. Understanding how comparisons compose with boolean logic is what makes conditional expressions powerful: you can express arbitrarily complex conditions like "the user is logged in and either has admin privileges or owns this resource" as a single boolean expression built from comparisons.
