---
id: limit-laws
title: Limit Laws
domain: mathematics
course: calculus-1
prerequisites:
  - id: limit-definition-intuitive
    type: hard
builds-toward:
  - continuity-definition
  - squeeze-theorem
  - limits-at-infinity
tags: [limits, laws, computation]
stage: formal-systems
status: validated
---

# Limit Laws

## Core Idea
Limit laws are rules that allow you to compute limits algebraically by breaking complex expressions into simpler pieces. If lim f(x) = L and lim g(x) = M, then lim(f + g) = L + M, lim(f * g) = L * M, lim(f/g) = L/M (when M is not 0), and lim(f^n) = L^n. These laws formalize the intuition that the limit of a combination equals the combination of limits, and they are the workhorse tools for evaluating limits without tables or graphs.

## How It's Best Learned
State each law, verify with examples, then practice applying them to compute limits of polynomial and rational functions. Show that for polynomials, limits can be found by direct substitution (a consequence of the limit laws). Emphasize the cases where the laws do not directly apply (0/0 indeterminate forms).

## Common Misconceptions
- Applying the quotient law when the denominator's limit is zero (this requires further analysis, not the quotient law).
- Assuming all limit laws hold for infinite limits (some do, some produce indeterminate forms).
- Believing limit laws are definitions rather than consequences of the precise limit definition.
