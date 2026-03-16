---
id: boolean-type-and-truth-values
title: Boolean Type and Truth Values
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: memory-and-data-storage
  type: hard
builds-toward:
- logical-operators-and-gates
- conditional-statements
tags:
- types
- boolean
- logic
stage: abstract-reasoning
status: draft
---

# Boolean Type and Truth Values

## Core Idea
The boolean type represents two values: true and false. Booleans are produced by comparisons and logical operations, and are used to make decisions in programs through conditionals and loops.

## How It's Best Learned
Write expressions that evaluate to true or false. Explore how different comparisons produce booleans.

## Common Misconceptions
- Booleans are just flags (they are first-class values that can be stored and reasoned about).
- True and false are numbers (they are distinct values; some languages may convert them, but they're conceptually different).

## Explainer

You already understand that computers store data in memory and that variables hold values. The **boolean type** is the simplest data type possible: it has exactly two values, **true** and **false**. Named after mathematician George Boole, booleans represent the answers to yes-or-no questions. Is 5 greater than 3? True. Is "hello" equal to "goodbye"? False. Every comparison you write in a program produces a boolean result.

Booleans are created most often through **comparison operators**. When you write `x > 10`, the computer evaluates this expression and produces either true or false depending on the current value of x. The expression `temperature == 100` checks equality and produces true or false. These comparisons — greater than, less than, equal to, not equal to — are the basic building blocks that generate boolean values. The key insight is that the result of a comparison is itself a value, just like the number 42 or the text "hello". You can store it in a variable: `is_adult = age >= 18` puts either true or false into `is_adult`.

What makes booleans powerful is that they are the language of **decisions** in programs. Every time a program chooses between two paths — should I show an error message or continue? should I keep looping or stop? — it evaluates a boolean expression. The `if` statement you'll encounter next takes a boolean and executes one block of code when it's true and optionally another when it's false. Loops repeat as long as a boolean condition remains true. Without booleans, programs would execute the same instructions every time with no ability to respond to different situations.

A common source of confusion is the relationship between booleans and numbers. In many languages, true behaves like 1 and false like 0 when used in arithmetic, and non-zero numbers are treated as "truthy" in boolean contexts. But treating booleans as mere numbers misses their purpose. A boolean carries **meaning** — it represents a logical proposition, not a quantity. The variable `is_logged_in` communicates intent in a way that the number 1 never could. As you move into logical operators and conditionals, thinking of booleans as answers to questions rather than as numbers will make your code clearer and your reasoning more precise.
