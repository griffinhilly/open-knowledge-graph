---
id: basic-input-output
title: Basic Input and Output
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: variables-and-assignment
  type: hard
- id: primitive-data-types
  type: soft
builds-toward:
- string-operations
- file-io-basics
tags:
- I/O
- print
- input
- console
- user interaction
stage: abstract-reasoning
status: draft
---

# Basic Input and Output

## Core Idea
Programs communicate with users through input and output operations. Output (e.g., print) sends text or values to the console; input (e.g., input() or scanf) reads text typed by the user. All console input arrives as text (strings), so numeric input must be converted to the appropriate type before arithmetic. Clear, informative output is a form of program documentation for the user.

## How It's Best Learned
Write interactive programs that prompt for input, compute something, and display results. Deliberately forget type conversion and observe the resulting error.

## Common Misconceptions
- Assuming input() returns a number when the user types digits — it returns a string.
- Forgetting to include a newline or space in prompts, leaving the cursor on a confusing line.
