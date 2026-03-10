---
id: recurrence-relations
title: Setting Up Recurrence Relations
domain: mathematics
course: discrete-math
prerequisites:
- id: mathematical-induction
  type: hard
- id: sequences-and-series-review
  type: soft
- id: counting-principles
  type: soft
builds-toward:
- solving-linear-recurrences
- divide-and-conquer-recurrences
tags:
- recurrence-relations
- sequences
- recursive-definition
- fibonacci
stage: formal-systems
status: draft
---

# Setting Up Recurrence Relations

## Core Idea
A recurrence relation defines each term of a sequence in terms of earlier terms, together with initial conditions. The Fibonacci sequence Fₙ = Fₙ₋₁ + Fₙ₋₂ with F₀ = 0, F₁ = 1 is the canonical example. Recurrences arise in counting problems (tilings, paths in a grid), algorithm analysis (merge sort, Tower of Hanoi), and combinatorics. The core skill is recognizing recursive structure in a problem and translating it faithfully into a recurrence equation with correct initial conditions.

## How It's Best Learned
Build recurrences from physical problems: domino tiling of a 2×n board, staircase-climbing with 1 or 2 steps, Tower of Hanoi. Draw the recursive decomposition before writing the formula. Verify the recurrence produces correct values for small cases before attempting to solve it.

## Common Misconceptions
- Setting up the recurrence correctly but specifying the wrong initial conditions — both parts are required.
- Not verifying the recurrence against small cases.
- Confusing a closed-form (explicit) formula with a recursive definition.
