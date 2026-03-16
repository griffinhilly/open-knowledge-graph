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

## Explainer

A **recurrence relation** is an equation that defines each term of a sequence in terms of earlier terms. You already have intuition for this from the definition of recurrences: rather than giving a formula that directly computes the nth term, a recurrence says "here is how the nth term relates to the ones before it." Combined with **initial conditions** — explicit values for the first one or more terms — the recurrence pins down a unique sequence. Without initial conditions, infinitely many sequences satisfy the same recurrence, as the core misconception warns.

The Fibonacci sequence is the canonical example: F(n) = F(n-1) + F(n-2), with F(1) = 1 and F(2) = 1, giving 1, 1, 2, 3, 5, 8, 13, .... Change the initial conditions to F(1) = 2 and F(2) = 2 and you get 2, 2, 4, 6, 10, 16, ... — different sequence, same recurrence. Factorial satisfies n! = n · (n-1)! — a first-order recurrence, requiring only one initial condition (0! = 1). The **Tower of Hanoi** gives T(n) = 2T(n-1) + 1 with T(1) = 1: to move n disks, move n-1 disks to the spare peg, move the largest disk, then move the n-1 stack on top. The recurrence captures the recursive structure of the problem directly.

Recurrences arise naturally in counting. The number of ways to climb n stairs taking 1 or 2 steps at a time satisfies the same recurrence as Fibonacci. The number of binary strings of length n with no two consecutive 1s satisfies a similar recurrence. In each case, the key step is to condition on the first (or last) choice, reducing the problem to smaller instances of itself. Translating a combinatorial problem into a recurrence is a skill: identify the choices at the first step, express the count in terms of smaller counts, and you have the recurrence.

Classifying recurrences guides which solution methods apply. A **linear recurrence** has the form aₙ = c₁aₙ₋₁ + c₂aₙ₋₂ + ⋯ + cₖaₙ₋ₖ + f(n). When f(n) = 0, it is **homogeneous**; otherwise it is **non-homogeneous**. Linear homogeneous recurrences with constant coefficients — including Fibonacci — have closed-form solutions via the characteristic equation, a technique you'll study next. Non-linear recurrences and those with variable coefficients require different tools. Recognizing which class a recurrence belongs to is always the first step toward solving it.
