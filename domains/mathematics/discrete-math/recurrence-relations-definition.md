---
id: recurrence-relations-definition
title: Recurrence Relations and Recursive Sequences
domain: mathematics
course: discrete-math
prerequisites:
- id: generating-functions-discrete
  type: soft
builds-toward:
- linear-recurrence-solutions
tags:
- recurrence-relations
- sequences
stage: formal-systems
status: draft
---

# Recurrence Relations and Recursive Sequences

## Core Idea
A recurrence relation defines a sequence by expressing each term as a function of previous terms and an initial condition. Classic examples include Fibonacci a(n) = a(n-1) + a(n-2) and geometric a(n) = ra(n-1). Recurrence relations arise naturally from algorithms and combinatorial counting.

## Explainer

A **recurrence relation** defines a sequence not by giving a direct formula for the n-th term, but by expressing each new term as a function of previous terms. The Fibonacci sequence is the canonical example: F(n) = F(n−1) + F(n−2), with **initial conditions** F(1) = 1 and F(2) = 1. To compute F(5), you don't need a formula — you unwind the recurrence: F(3) = 2, F(4) = 3, F(5) = 5. The recurrence is the rule; the initial conditions are the starting values that pin down which sequence you're describing.

Recurrences arise naturally whenever a problem decomposes into smaller versions of itself. Suppose you want to count binary strings of length n that contain no two consecutive 1s. Every such string either ends in 0 (with the first n−1 characters forming a valid string of length n−1) or ends in 10 (with the first n−2 characters forming a valid string of length n−2). So the count satisfies the same Fibonacci recurrence — and this is no coincidence. Any recursive process, whether a combinatorial construction or a divide-and-conquer algorithm, naturally expresses its behavior as a recurrence. The runtime of merge sort (T(n) = 2T(n/2) + n) is a recurrence. Recurrences are the language of recursion.

The **initial conditions** matter as much as the recurrence rule. The recurrence a(n) = 2a(n−1) with a(0) = 1 gives powers of two: 1, 2, 4, 8, .... The same recurrence with a(0) = 3 gives 3, 6, 12, 24, .... The recurrence defines the shape; the initial conditions place it. For an order-k recurrence (one that looks back k steps), you need exactly k initial conditions to fully determine the sequence. Specifying too few leaves the sequence ambiguous; the initial conditions are not optional.

**Linear recurrences** are the most tractable family: a(n) = c₁a(n−1) + c₂a(n−2) + ... + cₖa(n−k), where the coefficients cᵢ are constants. The geometric recurrence a(n) = ra(n−1) is the simplest: a(n) = r^n · a(0). More complex linear recurrences have **closed-form solutions** — formulas that give the n-th term without unwinding the recurrence step by step. The Fibonacci sequence has the famous Binet formula involving powers of the golden ratio. Finding these closed forms is the subject of the next topic; for now, the essential skills are reading a recurrence, computing terms from initial conditions, and recognizing what growth behavior — linear, exponential, oscillating — the recurrence produces.
