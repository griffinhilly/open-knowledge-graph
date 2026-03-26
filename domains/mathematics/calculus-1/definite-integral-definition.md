---
id: definite-integral-definition
title: Definite Integral Definition
domain: mathematics
course: calculus-1
prerequisites:
  - id: riemann-sums
    type: hard
  - id: limit-definition-intuitive
    type: hard
builds-toward:
  - fundamental-theorem-of-calculus-part-1
  - fundamental-theorem-of-calculus-part-2
tags: [integration, definite-integral, area]
stage: formal-systems
status: validated
---

# Definite Integral Definition

## Core Idea
The definite integral of f from a to b, written as the integral from a to b of f(x) dx, is defined as the limit of Riemann sums as the number of subintervals approaches infinity. When f(x) >= 0, the definite integral equals the area under the curve. When f takes negative values, it computes signed area (negative below the x-axis). The definite integral is a number, not a function, and it has properties: linearity, additivity over intervals, and comparison properties.

## How It's Best Learned
Connect to Riemann sums by computing limits of sums for simple functions (polynomials). State and apply properties of definite integrals. Emphasize that the definite integral is defined independently of antiderivatives (the FTC connects them, but they are conceptually separate).

## Common Misconceptions
- Believing the definite integral always represents area (it represents signed area; area requires taking absolute values).
- Confusing definite integrals (numbers with bounds) and indefinite integrals (functions with +C).
- Forgetting that the integral from a to a of f(x) dx = 0 and the integral from b to a equals the negative of the integral from a to b.

## Questions

```yaml
- question: "The function f(x) = x - 2 is negative on the interval [0, 2] and positive on [2, 4]. What does the definite integral from 0 to 4 of f(x) dx represent?"
  type: multiple-choice
  options: ["The total area between the curve and the x-axis on [0, 4]", "The signed area: the area above the x-axis minus the area below it", "Twice the area under the curve, because the interval has length 4", "Zero, because the function crosses the x-axis"]
  answer: 1
  explanation: "The definite integral computes signed area. On [0, 2] the function is below the x-axis, contributing negative area; on [2, 4] it is above, contributing positive area. The integral gives the net result. If the two pieces happen to be equal, the integral is 0 — but that is a coincidence of this function, not a general rule about functions that cross the axis."

- question: "The definite integral of a continuous function f from a to b usually equals the area enclosed between the curve y = f(x) and the x-axis on [a, b]."
  type: true-false
  answer: false
  explanation: "The definite integral computes signed area: regions where f(x) < 0 contribute negative values. To find the geometric area (always non-negative), you must integrate the absolute value of f, or split the integral at the zeros and take the absolute value of each piece."

- question: "What is the conceptual difference between a definite integral and an indefinite integral?"
  type: short-answer
  answer: "A definite integral has specific bounds a and b and evaluates to a number (the signed area). An indefinite integral has no bounds and evaluates to a family of functions (the antiderivatives), written with a +C."
  explanation: "This distinction is frequently blurred, but it is fundamental. The definite integral is a completed calculation that produces a scalar. The indefinite integral is a question about which functions have a given derivative — its output is a function (or family of functions), not a number."
```

## Explainer

Earlier in calculus you learned about Riemann sums: divide the interval [a, b] into n subintervals, approximate the curve's height on each with a rectangle, and sum the rectangle areas. As n grows larger, the rectangles get thinner and the sum gets closer to the "true" area. The **definite integral** is the formalization of that limit: the integral from a to b of f(x) dx is defined as the limit of Riemann sums as n → ∞.

The key word in that definition is *signed* area. When f(x) is positive, the rectangles sit above the x-axis and their heights are positive — they add to the sum. When f(x) is negative, the rectangles sit below the x-axis and their heights are negative — they *subtract* from the sum. The definite integral accounts for both simultaneously. This is why the integral of sin(x) from 0 to 2π equals zero: the area above the axis from 0 to π exactly cancels the area below it from π to 2π. The geometric areas are equal and opposite; the signed areas sum to zero.

This brings up one of the most common confusions: **the definite integral is not always the same as area**. If you want the total geometric area between a curve and the x-axis (always a non-negative number), you must either split the integral at each zero of f and take absolute values, or integrate |f(x)|. The definite integral gives you the net signed balance.

The definite integral also satisfies important properties that follow directly from its definition. Linearity means you can pull out constants and split sums: the integral of (cf + g) equals c times the integral of f plus the integral of g. Interval additivity means the integral from a to c equals the integral from a to b plus the integral from b to c, for any b in between. And the integral from a to a equals zero, because there is no interval — no width, no area.

One more distinction worth cementing: the definite integral (a number with bounds) and the indefinite integral (a family of antiderivatives, written with +C) are related but different objects. The Fundamental Theorem of Calculus connects them — it says you *can* compute a definite integral using an antiderivative — but conceptually they are answering different questions. The definite integral asks "how much accumulated change is there from a to b?" The indefinite integral asks "what function has this derivative?" Keeping these separate prevents a persistent category error that trips up many calculus students.
