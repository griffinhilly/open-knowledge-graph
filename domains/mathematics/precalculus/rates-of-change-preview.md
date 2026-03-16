---
id: rates-of-change-preview
title: Average Rate of Change and Secant Lines
domain: mathematics
course: precalculus
prerequisites:
  - id: function-notation-review
    type: hard
builds-toward:
  - limit-definition-of-derivative
  - derivative-as-slope-of-tangent
tags: [rates, secant-lines, calculus-preview]
stage: formal-systems
status: validated
---

# Average Rate of Change and Secant Lines

## Core Idea
The average rate of change of f(x) on [a, b] is (f(b) - f(a))/(b - a), which is the slope of the secant line through (a, f(a)) and (b, f(b)). This is a generalization of "rise over run" to any function. As the interval shrinks (b approaches a), the secant line approaches the tangent line, and the average rate of change approaches the instantaneous rate of change. This idea is the conceptual gateway to the derivative.

## How It's Best Learned
Compute average rates of change for various functions and intervals. Graph the secant lines and observe how they rotate as the interval shrinks. Use the difference quotient (f(a + h) - f(a))/h as preparation for the derivative definition.

## Common Misconceptions
- Confusing average rate of change with the average value of the function.
- Believing the average rate of change is always the rate at the midpoint.
- Not connecting secant line slopes to the derivative concept that follows.

## Explainer

From your work with function notation, you know that f(x) is a rule that assigns an output to each input. The **average rate of change** asks: how fast does the output change relative to the input, over some interval? The formula is (f(b) − f(a)) / (b − a), which you will recognize immediately as "rise over run" from your experience with linear functions. For a line y = mx + c, this formula always returns m, no matter which interval you pick. For a curved function, the result depends on which interval you choose — and that dependence is exactly what makes the concept rich.

Geometrically, (f(b) − f(a)) / (b − a) is the slope of the **secant line** — the straight line connecting the two points (a, f(a)) and (b, f(b)) on the graph of f. "Secant" comes from Latin for "cutting": the line cuts across the curve. For a parabola f(x) = x², the secant from x = 1 to x = 3 has slope (9 − 1)/(3 − 1) = 4. But the function's "steepness" varies — at x = 1 it rises more slowly than at x = 3. The secant slope of 4 is an average over the interval, not an exact instantaneous rate at any single point.

Now imagine squeezing the interval. Keep a = 1 fixed and let b approach 1: compute the secant slope for b = 1.5, then b = 1.1, then b = 1.01. For f(x) = x², the slope is (b² − 1)/(b − 1) = b + 1 (by factoring). As b → 1, this approaches 2. The secant lines rotate toward a single limiting position — the **tangent line** at x = 1, with slope exactly 2. This limiting process is precisely the definition of the derivative. The average rate of change over [a, b] is the raw ingredient; taking the limit as b → a cooks it into the instantaneous rate of change.

The **difference quotient** (f(a + h) − f(a)) / h is a rewrite of the same idea with b = a + h. As h → 0, you get the derivative. Practicing with the difference quotient now — simplifying it algebraically for specific functions before taking any limit — is exactly the preparation for calculus. For f(x) = x², you get ((a+h)² − a²)/h = (2ah + h²)/h = 2a + h. As h → 0, this gives 2a: the derivative of x² at any point a. You have already done most of the work of differentiation before calculus officially begins.
