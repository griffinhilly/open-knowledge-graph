---
id: loop-control-statements
title: 'Loop Control: Break and Continue'
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: for-loop-iteration
  type: hard
- id: while-loop-iteration
  type: hard
builds-toward:
- nested-loops
tags:
- loops
- control
- break-continue
stage: abstract-reasoning
status: draft
---

# Loop Control: Break and Continue

## Core Idea
Break exits a loop immediately; continue skips the rest of the current iteration and proceeds to the next. These statements provide fine-grained control over loop execution without restructuring the loop condition.

## How It's Best Learned
Write loops that use break (e.g., to exit early on a match) and continue (e.g., to skip invalid values). Compare with conditional guards.

## Common Misconceptions
- Break and continue affect all enclosing loops (they only affect the innermost enclosing loop).
- Overusing break and continue is clearer (excessive use makes control flow harder to follow).
