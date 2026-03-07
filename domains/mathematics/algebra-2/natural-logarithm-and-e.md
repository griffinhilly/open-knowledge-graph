---
id: natural-logarithm-and-e
title: Natural Logarithm and e
domain: mathematics
course: algebra-2
prerequisites:
  - id: logarithms-intro
    type: hard
  - id: exponential-growth-and-decay
    type: hard
builds-toward:
  - calculus-limits
  - calculus-derivatives
tags: [natural-logarithm, e, euler, continuous-compounding]
stage: abstract-reasoning
status: draft
---

# Natural Logarithm and e

## Core Idea
The number e (approximately 2.71828) is the base of the natural exponential function and natural logarithm. It arises naturally from continuous compounding: as n approaches infinity, (1 + 1/n)^n approaches e. The natural logarithm ln(x) = log_e(x) is the inverse of e^x. The pair (e^x, ln(x)) is fundamental in calculus because the derivative of e^x is e^x itself. Continuous growth/decay is modeled by A = A_0 * e^(kt).

## How It's Best Learned
Motivate e through compound interest: show that compounding more frequently approaches a limit. Define e as that limit. Practice converting between e^x = y and ln(y) = x. Solve equations involving e^x and ln(x). Compare natural log with common log. Emphasize that e is just a number (albeit irrational and transcendental), not a variable.

## Common Misconceptions
- Thinking e is a variable rather than a specific constant.
- Confusing ln(x) with log(x) (ln uses base e, log typically uses base 10).
- Thinking ln(e) = e (ln(e) = 1, because e^1 = e).
- Not recognizing that ln(1) = 0 and ln(e^x) = x.
