---
id: recurrence-relations-discrete
title: Recurrence Relations and Their Definitions
domain: mathematics
course: discrete-math
prerequisites:
- id: recurrence-relations
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
status: validated
---

# Recurrence Relations and Their Definitions

## Core Idea
A recurrence relation defines a sequence where each term depends on previous terms: aₙ = f(aₙ₋₁, aₙ₋₂, ...). Initial conditions specify the first few terms. Fibonacci, factorials, and Hanoi tower sequences are classic examples.

## How It's Best Learned
Compute the first several terms of well-known recurrences. Recognize linear vs. non-linear, homogeneous vs. non-homogeneous forms. Write recurrence relations from problem descriptions (counting paths, rabbits, etc.).

## Common Misconceptions
A recurrence relation alone is incomplete without initial conditions. Without them, infinitely many sequences satisfy the same recurrence.

## Questions

```yaml
- question: "The recurrence T(n) = 2T(n−1) with T(1) = 3 gives the sequence 3, 6, 12, 24, .... What sequence does T(n) = 2T(n−1) with T(1) = 1 produce?"
  type: multiple-choice
  options:
    - "3, 6, 12, 24, ... — the recurrence determines the sequence, not the initial value."
    - "1, 2, 4, 8, ... — a different initial condition produces a different sequence."
    - "0, 1, 2, 4, ... — the sequence shifts by one position when T(1) changes."
    - "1, 3, 6, 12, ... — the new first term is prepended before the original sequence."
  answer: 1
  explanation: "The same recurrence with different initial conditions produces entirely different sequences. With T(1) = 1, the terms are T(2) = 2, T(3) = 4, T(4) = 8, giving 1, 2, 4, 8, .... Option A reflects the core misconception that the recurrence alone determines the sequence — but without initial conditions, infinitely many sequences satisfy T(n) = 2T(n−1)."

- question: "A person climbs a staircase by taking 1 or 2 steps at a time. Let f(n) be the number of distinct ways to climb n stairs. Which recurrence captures this correctly?"
  type: multiple-choice
  options:
    - "f(n) = 2 × f(n−1), because at every step there are always two choices."
    - "f(n) = f(n−1) × f(n−2), because the two sub-problems multiply together."
    - "f(n) = f(n−1) + f(n−2), because the last move was either 1 step (from position n−1) or 2 steps (from position n−2)."
    - "f(n) = n × f(n−1), because more stairs means proportionally more paths."
  answer: 2
  explanation: "Condition on the last move: if the final step was a single step, you arrived from stair n−1, with f(n−1) ways to have reached it; if it was a double step, you arrived from stair n−2, with f(n−2) ways. These cases are mutually exclusive and exhaustive, so f(n) = f(n−1) + f(n−2) — the Fibonacci recurrence. Option A is wrong because doubling the paths from n−1 ignores the distinct paths that arrive via a 2-step jump from n−2."

- question: "The same recurrence relation with different initial conditions can produce entirely different sequences."
  type: true-false
  answer: true
  explanation: "True. The recurrence gives the rule for continuation, but the initial conditions are what anchor the sequence. Fibonacci with F(1) = 1, F(2) = 1 gives 1, 1, 2, 3, 5, 8, ...; the same recurrence with F(1) = 2, F(2) = 2 gives 2, 2, 4, 6, 10, 16, .... Different starting points, same rule, different sequences."

- question: "A recurrence relation alone is sufficient to uniquely determine a sequence."
  type: true-false
  answer: false
  explanation: "False. A recurrence constrains how terms relate to each other but leaves the starting values unspecified. Without initial conditions, infinitely many sequences satisfy any given recurrence. For example, T(n) = T(n−1) + 1 is satisfied by 1, 2, 3, 4, ... and also by 5, 6, 7, 8, ... and by every arithmetic sequence with common difference 1. Initial conditions are what make the sequence unique."

- question: "Why are initial conditions an essential component of a recurrence relation definition, and what goes wrong if they are omitted?"
  type: short-answer
  answer: "Initial conditions specify the explicit values of the first one or more terms. Without them, the recurrence only tells you how each term relates to previous ones but provides no concrete anchor. As a result, infinitely many sequences satisfy the same recurrence. For example, any sequence aₙ = c · 2ⁿ satisfies aₙ = 2aₙ₋₁ for any constant c. Only by fixing a starting value — say a₁ = 3 — do we pin down a unique sequence."
  explanation: "A recurrence is like a rule for generating next steps without telling you where to start. Initial conditions are the foundation — the recurrence stacks terms on top of them. This parallels a differential equation needing initial values to select one unique solution from a family of solutions."
```

## Explainer

A **recurrence relation** is an equation that defines each term of a sequence in terms of earlier terms. You already have intuition for this from the definition of recurrences: rather than giving a formula that directly computes the nth term, a recurrence says "here is how the nth term relates to the ones before it." Combined with **initial conditions** — explicit values for the first one or more terms — the recurrence pins down a unique sequence. Without initial conditions, infinitely many sequences satisfy the same recurrence, as the core misconception warns.

The Fibonacci sequence is the canonical example: F(n) = F(n-1) + F(n-2), with F(1) = 1 and F(2) = 1, giving 1, 1, 2, 3, 5, 8, 13, .... Change the initial conditions to F(1) = 2 and F(2) = 2 and you get 2, 2, 4, 6, 10, 16, ... — different sequence, same recurrence. Factorial satisfies n! = n · (n-1)! — a first-order recurrence, requiring only one initial condition (0! = 1). The **Tower of Hanoi** gives T(n) = 2T(n-1) + 1 with T(1) = 1: to move n disks, move n-1 disks to the spare peg, move the largest disk, then move the n-1 stack on top. The recurrence captures the recursive structure of the problem directly.

Recurrences arise naturally in counting. The number of ways to climb n stairs taking 1 or 2 steps at a time satisfies the same recurrence as Fibonacci. The number of binary strings of length n with no two consecutive 1s satisfies a similar recurrence. In each case, the key step is to condition on the first (or last) choice, reducing the problem to smaller instances of itself. Translating a combinatorial problem into a recurrence is a skill: identify the choices at the first step, express the count in terms of smaller counts, and you have the recurrence.

Classifying recurrences guides which solution methods apply. A **linear recurrence** has the form aₙ = c₁aₙ₋₁ + c₂aₙ₋₂ + ⋯ + cₖaₙ₋ₖ + f(n). When f(n) = 0, it is **homogeneous**; otherwise it is **non-homogeneous**. Linear homogeneous recurrences with constant coefficients — including Fibonacci — have closed-form solutions via the characteristic equation, a technique you'll study next. Non-linear recurrences and those with variable coefficients require different tools. Recognizing which class a recurrence belongs to is always the first step toward solving it.
