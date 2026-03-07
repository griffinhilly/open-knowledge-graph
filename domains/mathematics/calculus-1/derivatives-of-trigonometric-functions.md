---
id: derivatives-of-trigonometric-functions
title: Derivatives of Trigonometric Functions
domain: mathematics
course: calculus-1
prerequisites:
  - id: chain-rule
    type: soft
  - id: squeeze-theorem
    type: hard
  - id: trigonometric-identities-pythagorean
    type: hard
builds-toward:
  - trigonometric-integrals
tags: [derivatives, trigonometry]
stage: formal-systems
status: draft
---

# Derivatives of Trigonometric Functions

## Core Idea
The derivatives of the six trig functions are: d/dx[sin(x)] = cos(x), d/dx[cos(x)] = -sin(x), d/dx[tan(x)] = sec^2(x), d/dx[cot(x)] = -csc^2(x), d/dx[sec(x)] = sec(x)tan(x), d/dx[csc(x)] = -csc(x)cot(x). The sine and cosine derivatives follow from the limit definition using lim sin(h)/h = 1 (proved by the squeeze theorem). The others are derived using the quotient rule and Pythagorean identities.

## How It's Best Learned
Derive d/dx[sin(x)] from the limit definition using sum identity and the two key limits. Derive d/dx[cos(x)] similarly or from the chain rule with sin(pi/2 - x). Derive the remaining four using quotient rule. Practice with the chain rule: d/dx[sin(3x)] = 3cos(3x).

## Common Misconceptions
- Forgetting the negative sign in d/dx[cos(x)] = -sin(x).
- Not applying the chain rule when the argument is not just x.
- Mixing up the derivative pairs (sec goes with sec*tan, csc goes with -csc*cot).
