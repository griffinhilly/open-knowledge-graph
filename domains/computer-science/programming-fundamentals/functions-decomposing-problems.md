---
id: functions-decomposing-problems
title: 'Functions: Decomposing Problems'
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: functions-defining-calling
  type: hard
builds-toward:
- function-parameters-passing-data
- function-design-and-contracts
tags:
- functions
- decomposition
- design
stage: abstract-reasoning
status: draft
---

# Functions: Decomposing Problems

## Core Idea
Functions break large problems into smaller, reusable pieces. Each function should do one thing well (single responsibility). Decomposition reduces complexity, enables testing, and makes code reusable. A well-designed function has a clear name, few parameters, and obvious behavior.

## How It's Best Learned
Refactor existing code by extracting repeated logic into functions; practice naming functions to reflect their purpose (calcSum, validateEmail).

## Common Misconceptions
That functions must be long or complex; that small functions are inefficient; that every piece of code should be in a function (main logic is okay).

## Explainer

You already know how to define and call functions — you can write `def greet(name):` and invoke it with `greet("Alice")`. Decomposition is the *design skill* of deciding when and how to break a larger problem into functions. It is the difference between knowing the syntax of functions and knowing how to use them well.

Consider a program that reads a CSV file of student grades, calculates each student's average, determines letter grades, and prints a formatted report. You *could* write this as 80 lines in a single block. But if the averaging logic has a bug, you have to read through file-parsing and formatting code to find it. If you later need to calculate averages for a different file format, you cannot reuse anything. **Decomposition** means identifying the distinct sub-tasks — parsing the file, computing averages, converting to letter grades, formatting output — and making each one a function. Each function takes inputs, produces outputs, and does one clearly defined thing.

The guiding principle is **single responsibility**: a function should have one reason to exist and one reason to change. `calculate_average(scores)` takes a list of numbers and returns their mean. It does not know about files, letter grades, or formatting — those are other functions' jobs. This separation makes each function easy to test in isolation: you can verify `calculate_average([90, 80, 70])` returns `80.0` without setting up any files. It also makes the top-level code read like an outline of the solution: `scores = parse_file(path)`, `averages = [calculate_average(s) for s in scores]`, `grades = [to_letter(a) for a in averages]`, `print_report(grades)`. Someone reading this can understand the program's structure in seconds.

A practical heuristic for when to extract a function: if you find yourself writing a comment like "now calculate the average" before a block of code, that block probably wants to be a function *named* `calculate_average`, eliminating the need for the comment. Similarly, if the same logic appears in two places, extract it — not primarily to save lines, but to ensure that fixing a bug in one place fixes it everywhere. Start with the whole problem, identify 3–5 natural sub-tasks, write a function for each, and compose them in a main flow. This top-down decomposition is one of the most transferable skills in programming, applicable in every language and at every scale.
