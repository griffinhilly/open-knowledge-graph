---
id: solving-logarithmic-equations
title: Solving Logarithmic Equations
domain: mathematics
course: algebra-2
prerequisites:
  - id: logarithm-properties
    type: hard
  - id: logarithms-intro
    type: hard
builds-toward:
  - natural-logarithm-and-e
tags: [logarithms, equations, solving, extraneous-solutions]
stage: abstract-reasoning
status: validated
---

# Solving Logarithmic Equations

## Core Idea
Logarithmic equations contain logarithmic expressions with the variable in the argument. Two main strategies: (1) If the equation has a single log on each side with the same base, set the arguments equal: log_b(A) = log_b(B) implies A = B. (2) If the equation has log = constant, convert to exponential form: log_b(A) = c means A = b^c. Use log properties to condense multiple log terms first. Always check for extraneous solutions (arguments of log must be positive).

## How It's Best Learned
Practice converting between log and exponential forms. Solve equations by condensing log expressions using properties, then converting. Emphasize domain checking: solutions must make all original log arguments positive. Give examples where extraneous solutions arise.

## Common Misconceptions
- Not checking domain restrictions (log of a negative number is undefined).
- Forgetting to condense multiple log terms before converting to exponential form.
- Confusing log_b(x) = y with b*x = y (should be b^y = x).
- Thinking that because algebraic steps produce a valid number, it must be a valid solution (must check domain).
