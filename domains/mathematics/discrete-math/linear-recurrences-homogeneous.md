---
id: linear-recurrences-homogeneous
title: Solving Linear Recurrence Relations
domain: mathematics
course: discrete-math
prerequisites:
- id: recurrence-relations-discrete
  type: hard
- id: characteristic-polynomial
  type: soft
builds-toward:
- generating-functions-basics
tags:
- linear-recurrences
- characteristic-equation
- closed-form
stage: formal-systems
status: draft
---

# Solving Linear Recurrence Relations

## Core Idea
Linear homogeneous recurrences like aₙ = c₁aₙ₋₁ + c₂aₙ₋₂ + ... + cₖaₙ₋ₖ have closed-form solutions via the characteristic equation rᵏ − c₁rᵏ⁻¹ − ... − cₖ = 0. The roots determine the general form; initial conditions pin down constants.

## How It's Best Learned
Solve Fibonacci step-by-step: characteristic equation r² = r + 1 gives roots (1±√5)/2; express aₙ as a linear combination scaled by these roots. Verify by computing initial terms.

## Common Misconceptions
The characteristic equation is rᵏ = c₁rᵏ⁻¹ + ... + cₖ, not rᵏ⁻¹ etc. Repeated roots require adjusted forms (terms multiplied by n).
