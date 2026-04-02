---
id: variables-and-assignment
title: Variables and Assignment
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: memory-and-data-storage
  type: hard
builds-toward:
- primitive-data-types
- operators-and-expressions
- input-output
- arithmetic-operators
- variable-scope
- function-design-and-contracts
- scope-shadowing-and-lifetime
tags:
- variables
- assignment
- state
- memory
stage: formal-systems
status: validated
---
# Variables and Assignment

## Core Idea
A variable is a named container that holds a value in memory. Assignment binds a name to a value using the assignment operator (e.g., x = 5), replacing any previous value. Variables allow programs to store, retrieve, and update information as computation proceeds. Unlike mathematical variables, programming variables are mutable by default and represent a location in memory, not an unknown.

## How It's Best Learned
Trace through short programs by hand, writing down the current value of each variable after each assignment statement. Experimenting in a REPL (read-eval-print loop) gives immediate feedback.

## Common Misconceptions
- Confusing = (assignment) with == (equality test).
- Thinking a variable holds the expression that created it rather than the evaluated value.
- Assuming variables are shared across programs or sessions by default.

## Questions

```yaml
- question: "What is the value of x after these three lines execute?\nx = 10\ny = x\nx = 20"
  type: multiple-choice
  options: ["x is 10, y is 10", "x is 20, y is 20", "x is 20, y is 10", "x is 10, y is 20"]
  answer: 2
  explanation: "After line 1, x holds 10. Line 2 copies the current value of x (which is 10) into y. Line 3 reassigns x to 20. Crucially, y still holds 10 — it captured the value at the time of assignment, not a live link to x. This tests the misconception that variables store expressions or references to other variables rather than evaluated values."

- question: "In most programming languages, the statement x = x + 1 is a valid assignment."
  type: true-false
  answer: true
  explanation: "In programming, = is the assignment operator, not a statement of mathematical equality. The right side (x + 1) is evaluated first using the current value of x, and the result is stored back into x. In math, x = x + 1 has no solution, which is why this confuses beginners who think of = as 'equals.'"

- question: "Explain why the order of assignment statements matters. Give a brief example."
  type: short-answer
  answer: "Assignment is sequential: each statement uses the current values of variables at that moment. For example, 'a = 5; b = a + 1; a = 0' results in b = 6 and a = 0, not b = 1, because b was assigned before a changed."
  explanation: "Variables hold snapshots, not formulas. Each assignment reads the current state, computes a value, and writes it. Reordering assignments can produce completely different results because the state changes between lines."
```

## Explainer

A variable in programming is, at its core, a named location in memory that stores a value. When you write `x = 5`, you are telling the computer: "reserve a spot called x, and put the number 5 there." From that point forward, whenever the program encounters `x`, it looks up what is stored in that spot and uses the value it finds.

Assignment is the act of putting a value into a variable, and it works differently from the equals sign in math. The `=` in programming means "evaluate the right side, then store the result in the left side." This is why `x = x + 1` makes perfect sense in code — it means "take the current value of x, add 1, and store the result back in x." If x was 7, it becomes 8. In mathematics, the equation x = x + 1 is a contradiction, but in programming it is one of the most common operations: incrementing a counter.

One subtle point that trips up beginners is that assignment captures a *value*, not a *connection*. If you write `a = 5` and then `b = a`, b gets the value 5 — a copy of what a held at that moment. If you later change a to 100, b is still 5. Variables do not "watch" each other; they simply hold whatever was last assigned to them. This means the order of statements matters enormously. Swapping the order of two assignments can produce completely different results.

Variables also have types — the kind of data they hold. In some languages you must declare the type explicitly (e.g., `int count = 0`), while in others the language figures out the type from the value you assign (e.g., `count = 0` in Python). Either way, the concept is the same: the variable holds a value, and that value has a type (integer, string, boolean, etc.) that determines what operations you can perform on it. You will explore types in depth when you reach data types, but for now, the key idea is that variables are the fundamental mechanism for storing and manipulating state in a program.
