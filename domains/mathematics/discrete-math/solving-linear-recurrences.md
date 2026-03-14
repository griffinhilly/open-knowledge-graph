---
id: solving-linear-recurrences
title: 'Solving Linear Recurrences: The Characteristic Equation'
domain: mathematics
course: discrete-math
prerequisites:
- id: recurrence-relations
  type: hard
- id: quadratic-formula
  type: hard
- id: complex-numbers-intro
  type: soft
builds-toward:
- generating-functions-intro
- divide-and-conquer-recurrences
tags:
- linear-recurrences
- characteristic-equation
- closed-form
- fibonacci
- golden-ratio
stage: formal-systems
status: validated
---

# Solving Linear Recurrences: The Characteristic Equation

## Core Idea
A linear homogeneous recurrence with constant coefficients (e.g., aₙ = c₁aₙ₋₁ + c₂aₙ₋₂) is solved by assuming aₙ = rⁿ and finding roots of the characteristic polynomial. The general solution is a linear combination of rⁿ terms, with coefficients determined by initial conditions. Repeated roots require polynomial multipliers (nrⁿ, n²rⁿ, …). Applying this method to Fibonacci yields the closed form Fₙ = (φⁿ − ψⁿ)/√5, where φ = (1+√5)/2 is the golden ratio.

## How It's Best Learned
Work through the Fibonacci case in complete detail, including solving the 2×2 linear system for the constants. Solve additional second-order examples before tackling higher-order or non-homogeneous cases (which use variation of parameters or particular solutions). Always verify closed forms against the original recurrence.

## Common Misconceptions
- Forgetting to apply initial conditions after finding the general solution — the constants are essential.
- Incorrectly handling repeated roots by using only rⁿ instead of rⁿ and nrⁿ.
- Thinking the characteristic equation method only applies to second-order recurrences.
