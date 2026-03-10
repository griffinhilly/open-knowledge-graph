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
status: draft
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
