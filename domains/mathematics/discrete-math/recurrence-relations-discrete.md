---
id: recurrence-relations-discrete
title: Recurrence Relations and Their Definitions
domain: mathematics
course: discrete-math
prerequisites:
- id: recurrence-relations-definition
  type: hard
- id: sequences-convergence
  type: soft
builds-toward:
- linear-recurrences-homogeneous
- generating-functions-basics
tags:
- recurrence
- sequences
- recursive
- definition
stage: formal-systems
status: draft
---

# Recurrence Relations and Their Definitions

## Core Idea
A recurrence relation defines a sequence where each term depends on previous terms: aₙ = f(aₙ₋₁, aₙ₋₂, ...). Initial conditions specify the first few terms. Fibonacci, factorials, and Hanoi tower sequences are classic examples.

## How It's Best Learned
Compute the first several terms of well-known recurrences. Recognize linear vs. non-linear, homogeneous vs. non-homogeneous forms. Write recurrence relations from problem descriptions (counting paths, rabbits, etc.).

## Common Misconceptions
A recurrence relation alone is incomplete without initial conditions. Without them, infinitely many sequences satisfy the same recurrence.
