---
id: variables-and-assignment
title: Variables and Assignment
domain: computer-science
course: programming-fundamentals
prerequisites: []
builds-toward:
- primitive-data-types
- operators-and-expressions
- basic-input-output
tags:
- variables
- assignment
- state
- memory
stage: abstract-reasoning
status: draft
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
