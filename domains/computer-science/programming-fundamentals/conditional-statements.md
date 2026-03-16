---
id: conditional-statements
title: Conditional Statements
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: operators-and-expressions
  type: hard
builds-toward:
- boolean-logic-programming
- while-loops
- error-handling-exceptions
tags:
- if
- else
- elif
- branching
- control flow
stage: abstract-reasoning
status: validated
---

# Conditional Statements

## Core Idea
Conditional statements allow a program to choose between different paths of execution based on whether a boolean expression is true or false. An if statement executes a block only when its condition holds; an else clause handles the alternative; elif (or else if) chains allow multiple mutually exclusive branches. Conditionals are the foundation of decision-making in programs and are essential for handling different cases of input or state.

## How It's Best Learned
Trace through if-else chains by hand for several input values, including edge cases. Write a program that classifies input (e.g., grade letter from score) using nested and chained conditionals.

## Common Misconceptions
- Using = instead of == inside a condition.
- Forgetting that only the first true branch executes in an elif chain.
- Accidentally writing overlapping conditions that shadow intended cases.

## Explainer

Up to this point, your programs have executed every line in order, top to bottom. **Conditional statements** give programs the ability to make decisions — to choose one path of execution over another based on the current state of the data. This is a fundamental leap: programs go from being simple calculators that always do the same thing to being responsive tools that adapt their behavior to different situations.

The basic building block is the **if statement**. It evaluates a boolean expression — a condition that is either true or false — and executes a block of code only when the condition is true. You already know from operators and expressions how to write comparisons like `x > 0` or `name == "Alice"`. The if statement uses these comparisons to control what happens next. If the condition is false, the block is simply skipped, and execution continues after it. Adding an **else** clause provides an alternative path: "if the condition is true, do this; otherwise, do that." Every possible input is now handled — one branch or the other will always execute.

When you have more than two possibilities, **elif** (or `else if`) chains let you test multiple conditions in sequence. The program checks each condition from top to bottom and executes the block of the *first* one that is true, then skips all the rest. This "first match wins" behavior is crucial to understand. If you write `if score >= 90: grade = "A"` followed by `elif score >= 80: grade = "B"`, a score of 95 matches the first condition and gets "A" — it never checks the second condition, even though 95 is also >= 80. This is why the order of conditions matters: put the most specific or restrictive conditions first.

A common beginner mistake is using separate if statements when you meant elif. If you write three independent `if` statements instead of an `if/elif/elif` chain, all three conditions are checked independently, and multiple blocks might execute. Another classic error is writing `if x = 5` (assignment) instead of `if x == 5` (comparison) — some languages catch this as a syntax error, but others silently treat the assignment as a truthy value. When your conditionals behave unexpectedly, the first thing to check is whether your conditions are actually testing what you think they are and whether your branches are properly exclusive.
