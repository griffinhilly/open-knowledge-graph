---
id: multivariable-functions-intro-domain
title: 'Functions of Several Variables: Domain and Range'
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: multivariable-functions-intro
  type: hard
builds-toward:
- contour-maps
- multivariable-limits
tags:
- multivariable-functions
- domain
- range
stage: formal-systems
status: validated
---

# Functions of Several Variables: Domain and Range

## Core Idea
A function f: D → ℝ maps points (x, y) or (x, y, z) in domain D to real numbers. The domain is the set of inputs where f is defined; the range is the set of outputs. Domains in ℝ² are regions (open, closed, or neither).

## Explainer

From your introduction to multivariable functions, you know that a function of several variables takes a point in the plane (or space) as input and returns a real number. Now the question is: for which points is the function actually defined? The **domain** is the set of all input points where the formula makes sense — no division by zero, no square roots of negative numbers, no logarithms of non-positive numbers. For a function of one variable, the domain is usually an interval on the number line. For a function of two variables, the domain is typically a **region** in the plane — a two-dimensional subset of ℝ².

Finding the domain of f(x, y) means identifying every constraint the formula imposes and intersecting the sets where each constraint is satisfied. For f(x, y) = √(1 − x² − y²), the square root requires 1 − x² − y² ≥ 0, which means x² + y² ≤ 1 — the closed unit disk. For f(x, y) = 1/(x − y), the denominator requires x ≠ y — the plane minus the diagonal line. The **range** is then the set of output values f actually achieves on its domain, which can require more work to determine: for the disk example, z = √(1 − x² − y²) ranges from 0 (on the boundary circle) to 1 (at the origin), so the range is [0, 1].

The geometric distinction between **open** and **closed** domains matters for limits and continuity. A domain is **open** if every point in it has a small disk entirely contained in the domain — there are no boundary points included. It is **closed** if it contains all its boundary points. It can be neither (like a half-open interval in one variable, extended to two dimensions). This matters because functions on closed, bounded (compact) domains are guaranteed to attain their maximum and minimum values — the two-dimensional version of the Extreme Value Theorem you know from single-variable calculus.

Understanding domain and range sets you up for studying **level curves** and **contour maps** — the graphs of the equation f(x, y) = c for different constants c. A level curve lives entirely within the domain (assuming c is in the range), and reading a set of level curves gives geometric insight into how f varies over its domain. You will also need precise domain language when you define limits and continuity in two variables, because the notion of "approaching a point" depends on the topology of the domain — you can approach along many different paths, not just from left or right as in one dimension.

## Questions

```yaml
- question: "Find the domain of f(x, y) = ln(x + y − 1)."
  type: short-answer
  answer: "The domain is the set of (x, y) where x + y − 1 > 0, i.e., x + y > 1. This is the open half-plane above the line x + y = 1."
  explanation: "The natural logarithm requires a strictly positive argument, so we need x + y − 1 > 0, or equivalently x + y > 1. In the plane, x + y = 1 is a line with slope −1 passing through (1, 0) and (0, 1). The domain is the open half-plane on the side where x + y exceeds 1 (upper-right region). Note the domain is open because it excludes the boundary line itself."
```