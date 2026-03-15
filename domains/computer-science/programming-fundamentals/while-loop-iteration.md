---
id: while-loop-iteration
title: While Loops and Condition-Controlled Iteration
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: program-structure-and-flow
  type: hard
builds-toward:
- loop-control-statements
- nested-loops
tags:
- loops
- iteration
- while
stage: abstract-reasoning
status: draft
---

# While Loops and Condition-Controlled Iteration

## Core Idea
A while loop repeats as long as a condition is true. The condition is checked before each iteration (pre-test). While loops are flexible and handle unknown iteration counts, such as processing until a sentinel value is read.

## How It's Best Learned
Write while loops that process data until a condition changes. Ensure loop guards prevent infinite loops.

## Common Misconceptions
- While loops always exit (an incorrect guard can cause infinite loops).
- While and for loops are equivalent (they have different strengths; for is clearer for counted loops, while for condition-based).
