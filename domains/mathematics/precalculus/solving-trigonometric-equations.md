---
id: solving-trigonometric-equations
title: Solving Trigonometric Equations
domain: mathematics
course: precalculus
prerequisites:
- id: inverse-trigonometric-functions
  type: hard
- id: trigonometric-identities-pythagorean
  type: hard
- id: unit-circle
  type: hard
- id: double-angle-identities
  type: soft
- id: half-angle-identities
  type: soft
- id: sum-and-difference-identities
  type: soft
builds-toward:
- differential-equations-intro-separable
tags:
- trigonometry
- equations
- solving
stage: formal-systems
status: validated
---
# Solving Trigonometric Equations

## Core Idea
Solving trigonometric equations means finding all angles that satisfy a given equation. The process typically involves isolating the trig function using algebraic techniques and identities, finding reference angles using inverse trig functions, then accounting for periodicity to list all solutions (either in a given interval or as a general solution with + 2*pi*n). This skill ties together everything from the trig unit.

## How It's Best Learned
Start with basic equations like sin(x) = 1/2, find solutions on [0, 2*pi), then write general solutions. Progress to equations requiring identities (e.g., 2sin^2(x) - 1 = 0 using Pythagorean identity) and factoring. Emphasize the systematic approach: isolate, solve, list all solutions.

## Common Misconceptions
- Finding only one solution when there are multiple in the given interval.
- Forgetting to account for periodicity in the general solution.
- Dividing both sides by a trig function, which loses solutions where that function is zero.

## Questions

```yaml
- question: "When solving 2sin²x = sinx, a student divides both sides by sinx and gets 2sinx = 1, arriving at x = π/6 and x = 5π/6 in [0, 2π). What is wrong with this approach?"
  type: multiple-choice
  options:
    - "Nothing is wrong — dividing by sinx is the standard algebraic technique"
    - "The student should have used the Pythagorean identity instead of dividing"
    - "The division by sinx discards solutions where sinx = 0, namely x = 0 and x = π"
    - "The equation has no solutions in [0, 2π) because both sides are quadratic"
  answer: 2
  explanation: "Dividing both sides by sinx assumes sinx ≠ 0 and discards any solutions where sinx = 0. Moving everything to one side and factoring is safe: 2sin²x − sinx = 0 → sinx(2sinx − 1) = 0, giving sinx = 0 (yielding x = 0, π) or 2sinx − 1 = 0 → sinx = 1/2 (yielding x = π/6, 5π/6). There are four solutions total, not two. Whenever you divide by an expression that might equal zero, you risk losing solutions."

- question: "What is the general solution to sin(x) = 1/2?"
  type: multiple-choice
  options:
    - "x = π/6 only, since arcsin(1/2) = π/6"
    - "x = π/6 + πn for all integers n"
    - "x = π/6 + 2πn and x = 5π/6 + 2πn for all integers n"
    - "x = π/6 + 2πn for all integers n"
  answer: 2
  explanation: "The inverse sine function gives only one value (arcsin(1/2) = π/6), but the unit circle shows two angles in [0, 2π) where sin equals 1/2: π/6 (quadrant I) and π/6's symmetric partner 5π/6 (quadrant II), since sin is positive in both. Then periodicity adds 2πn to each branch. Option B (adding πn) confusingly mixes the period of sin (2π) with the spacing between the two solutions; option D forgets the second branch at 5π/6."

- question: "When solving a trigonometric equation, applying the Pythagorean identity (sin²x + cos²x = 1) can convert an equation involving both sine and cosine into an equation in a single trig function, which can then be solved by factoring."
  type: true-false
  answer: true
  explanation: "This is a key technique for equations that mix trig functions. For example, 1 − cos²x = sinx becomes sin²x = sinx (via the Pythagorean identity), which factors as sinx(sinx − 1) = 0. The identity converts the two-function problem into a single-function problem suitable for standard solving techniques."

- question: "The equation cos(x) = 0.8 has exactly two solutions: x = arccos(0.8) and x = −arccos(0.8)."
  type: true-false
  answer: false
  explanation: "These are the two solutions in (−π, π], but because cosine is periodic with period 2π, there are infinitely many solutions. The general solution is x = ±arccos(0.8) + 2πn for all integers n. Inverse trig functions return only one value (within their restricted range) precisely so that they are functions — but this means you must always add the periodicity term to capture all solutions."

- question: "Why is factoring the correct approach when solving sin(x)·cos(x) = sin(x), rather than dividing both sides by sin(x)? What solutions would be lost?"
  type: short-answer
  answer: "Dividing by sin(x) assumes sin(x) ≠ 0, which discards any solutions where sin(x) = 0 (i.e., x = 0, π, 2π, … in [0, 2π]). The correct approach is to move everything to one side: sin(x)·cos(x) − sin(x) = 0, then factor: sin(x)(cos(x) − 1) = 0. Setting each factor to zero gives sin(x) = 0 or cos(x) = 1. Both cases must be solved, yielding x = 0, π (from sin = 0) and x = 0 (from cos = 1). Factoring finds all solutions; division hides the ones that make the divisor zero."
  explanation: "This is the most dangerous shortcut in solving trig equations. Division by a trig expression is only valid when you can prove that expression is never zero on the domain — which is rarely true. Factoring is always safe because zero product property doesn't throw away cases; it just separates them into individual equations."
```

## Explainer

Solving a trigonometric equation is like solving any algebraic equation, but with one critical difference: trig functions are periodic, so equations almost always have infinitely many solutions. Your three core prerequisites — the **unit circle**, **inverse trig functions**, and **Pythagorean identities** — give you exactly the tools to find and organize all of them.

The unit circle is your lookup table. You know that sin(θ) = 1/2 at θ = π/6 and θ = 5π/6 in [0, 2π), and then again every 2π beyond that. The **inverse trig function** arcsin(1/2) = π/6 gives you the reference angle — the first-quadrant solution. But inverse trig functions only return one value (their range is restricted), so you must use the unit circle to find all solutions in the target interval. For sin, a positive value appears in quadrants I and II; for cos, in quadrants I and IV; for tan, in quadrants I and III. The second solution is found by symmetry: for sin(θ) = k > 0, the two solutions in [0, 2π) are arcsin(k) and π − arcsin(k). The **general solution** packages all of them: for sin(θ) = k, write θ = arcsin(k) + 2πn and θ = (π − arcsin(k)) + 2πn for all integers n.

When the equation is more complex, you first simplify using identities before applying this procedure. The **Pythagorean identity** sin²x + cos²x = 1 lets you convert between functions to get an equation in a single trig function. For example, 2sin²x − sinx − 1 = 0 factors as (2sinx + 1)(sinx − 1) = 0, giving sinx = −1/2 or sinx = 1. Solve each case separately using the unit circle. Similarly, a double-angle identity like cos(2x) = 1 − 2sin²x can reduce a degree-2 problem to a linear one. The general strategy is always: isolate one trig function (or factor to get separate simple equations), find the reference angle, use the unit circle to list all solutions in the required interval, and state the general solution with the ± 2πn period.

One dangerous shortcut is **dividing both sides by a trig function** to simplify. For instance, given sinx · cosx = sinx, you might divide by sinx to get cosx = 1. But this discards the solutions where sinx = 0 (namely x = 0, π, 2π, …). The safe approach is to move everything to one side and factor: sinx · cosx − sinx = 0, so sinx(cosx − 1) = 0, giving sinx = 0 or cosx = 1 as two separate cases, both of which must be solved. Factoring preserves all solutions; division hides the ones that make the divisor zero.
