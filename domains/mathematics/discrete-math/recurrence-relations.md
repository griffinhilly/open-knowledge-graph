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
status: validated
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

## Questions

```yaml
- question: "A 2×n board can be tiled with 1×2 dominoes. Let T(n) be the number of tilings. Which recurrence and initial conditions are correct?"
  type: multiple-choice
  options:
    - "T(n) = T(n-1) + T(n-2), with T(0) = 0 and T(1) = 1"
    - "T(n) = T(n-1) + T(n-2), with T(0) = 1 and T(1) = 1"
    - "T(n) = 2·T(n-1), with T(1) = 1"
    - "T(n) = T(n-1) + T(n-2), with T(1) = 2 and T(2) = 3"
  answer: 1
  explanation: "Place the first domino: either vertically (covering column 1, leaving a 2×(n-1) board) or as two horizontals stacked (covering columns 1-2, leaving a 2×(n-2) board). So T(n) = T(n-1) + T(n-2). The base cases are T(0) = 1 (one way to tile an empty board — the empty tiling) and T(1) = 1 (only a vertical domino fits). Wrong initial conditions produce the wrong sequence, which is the most common setup error."

- question: "A recurrence relation alone, without any initial conditions, uniquely determines a sequence."
  type: true-false
  answer: false
  explanation: "A recurrence like aₙ = aₙ₋₁ + aₙ₋₂ is satisfied by infinitely many sequences depending on the starting values. For example, Fibonacci (0, 1, 1, 2, 3, ...) and Lucas (2, 1, 3, 4, 7, ...) both satisfy the same recurrence but have different initial conditions. Initial conditions are required to pin down a unique sequence."

- question: "What does it mean to 'verify a recurrence against small cases,' and why is this step important?"
  type: short-answer
  answer: "Compute the first several terms both by directly counting the objects (e.g., by hand or by enumeration) and by applying the recurrence formula, then confirm the two match."
  explanation: "Even a logically derived recurrence can have subtle errors — especially in the initial conditions or off-by-one boundary cases. Checking that T(1), T(2), T(3) match direct counts is a fast sanity check that catches most setup mistakes before you invest effort in solving the recurrence."
```

## Explainer

A recurrence relation is a rule that defines each term of a sequence using earlier terms. The classic example is the Fibonacci sequence: F₀ = 0, F₁ = 1, and Fₙ = Fₙ₋₁ + Fₙ₋₂ for n ≥ 2. The recurrence equation (Fₙ = Fₙ₋₁ + Fₙ₋₂) tells you how to generate new terms; the initial conditions (F₀ = 0, F₁ = 1) tell you where to start. Without both pieces, the sequence is not determined.

The key skill in this topic is setting up a recurrence from a problem — not just recognizing one. The strategy is to think recursively: suppose you have already solved the problem for smaller inputs. How does the solution for size n relate to solutions for smaller sizes? For domino tiling, you ask: "What are the choices for the first column?" Each choice leaves a smaller board, and the number of ways to complete that board is a value you've already labeled T(k). Writing out those choices and adding them gives you the recurrence. The initial conditions come from the smallest cases you can count by hand.

This process shares deep structure with mathematical induction, which you already know. In induction, you prove a statement for n by assuming it for n-1 (or smaller values). In recurrence setup, you define the count for n by expressing it in terms of counts for smaller values. The recursive decomposition is the same — you're just computing instead of proving.

One pitfall to watch for: getting the initial conditions wrong while getting the recurrence right. For example, if you define T(0) = 0 instead of T(0) = 1 for the tiling problem, every subsequent term will be off. Always verify your recurrence by computing T(1), T(2), and T(3) both from the formula and by direct enumeration. If they disagree, something is wrong — and it is usually the initial conditions.

Finally, resist the temptation to jump immediately to a closed-form formula. A recurrence is a perfectly valid, complete description of a sequence. Techniques for solving recurrences (finding closed forms) come later; the foundational skill here is faithfully capturing recursive structure as an equation.
