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
- id: graphing-sine-and-cosine
  type: soft
- id: graphing-tangent-and-reciprocal-trig
  type: soft
builds-toward:
- trigonometric-integrals
tags:
- derivatives
- trigonometry
stage: formal-systems
status: validated
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

## Explainer

The derivatives of the six trigonometric functions are not arbitrary formulas to memorize in isolation — they follow directly from two foundational limits and systematic application of the rules you already know. The entire structure builds from one key limit proved by the squeeze theorem: lim(h→0) sin(h)/h = 1. If you've worked through the squeeze theorem, you've already established the machinery that makes trig differentiation possible.

To find d/dx[sin(x)], apply the limit definition of the derivative: (sin(x+h) − sin(x))/h as h → 0. Expand sin(x+h) using the angle addition identity sin(x+h) = sin(x)cos(h) + cos(x)sin(h). The expression becomes [sin(x)cos(h) + cos(x)sin(h) − sin(x)]/h = sin(x) · (cos(h)−1)/h + cos(x) · sin(h)/h. As h → 0, sin(h)/h → 1 and (cos(h)−1)/h → 0 (a second squeeze theorem limit). The result: **d/dx[sin(x)] = cos(x)**. The cosine derivative follows by the same method or by treating cos(x) = sin(π/2 − x) and applying the chain rule: d/dx[cos(x)] = −sin(x).

The remaining four derivatives come from expressing each function in terms of sine and cosine and applying the quotient rule. For example, tan(x) = sin(x)/cos(x), so by the quotient rule: d/dx[tan(x)] = (cos²(x) + sin²(x))/cos²(x) = 1/cos²(x) = sec²(x). The Pythagorean identity sin²(x) + cos²(x) = 1 is the algebraic glue that simplifies these quotient-rule results into clean forms. The pattern across all six: **co-functions pick up a minus sign** (d/dx[cos] = −sin, d/dx[cot] = −csc², d/dx[csc] = −csc·cot).

In practice, you'll combine these derivatives constantly with the chain rule. When the argument isn't simply x — say sin(3x²) — the chain rule adds an outer derivative: d/dx[sin(3x²)] = cos(3x²) · 6x. Every composite trig function follows this pattern: differentiate the outer trig function (using the table), leave the inner function alone, then multiply by the inner function's derivative. Mastering trig derivatives is mostly mastering this interplay between the six basic formulas and the chain rule.
