---
id: wronskian-linear-independence
title: Wronskian and Linear Independence
domain: mathematics
course: differential-equations
prerequisites:
- id: repeated-roots-reduction-of-order
  type: hard
- id: determinants-2x2-3x3
  type: hard
builds-toward:
- undetermined-coefficients
- variation-of-parameters
tags:
- wronskian
- linear-independence
- theoretical
stage: formal-systems
status: draft
---

# Wronskian and Linear Independence

## Core Idea
The Wronskian W[y₁, y₂] = y₁y₂' - y₂y₁' is a determinant measuring linear independence of two solutions. If W ≠ 0 at any point, the solutions are linearly independent and form a fundamental set generating all solutions. For linear ODEs, the Wronskian is either always zero or never zero, making it a definitive test for independence.

## Explainer

From your study of 2×2 determinants, you know that the determinant of a matrix [[a, b], [c, d]] equals ad - bc, and that a nonzero determinant means the rows (or columns) are linearly independent. The Wronskian applies this idea to functions: it is the determinant of the matrix [[y₁, y₂], [y₁', y₂']], which equals y₁y₂' - y₂y₁'. Think of it as asking whether the functions y₁ and y₂ are "pointing in different directions" in function space — independent in the same sense that two non-parallel vectors are geometrically independent.

If W[y₁, y₂](t₀) ≠ 0 at even a single point, the solutions are **linearly independent** and form a **fundamental set**: every solution to the ODE can be written as y = c₁y₁ + c₂y₂ for some constants c₁ and c₂. This is the ODE analogue of saying two independent vectors span a plane. If W = 0 everywhere, the solutions are **linearly dependent** — one is a constant multiple of the other, and they only span a one-dimensional family of solutions, which is not enough to capture the full solution space of a second-order equation.

The remarkable property specific to linear ODEs is Abel's theorem: the Wronskian satisfies W'(t) = -p(t)W(t) for a linear ODE y'' + p(t)y' + q(t)y = 0. Solving this first-order ODE gives W(t) = W(t₀)e^(-∫p dt), which is either always zero (if W(t₀) = 0) or never zero (if W(t₀) ≠ 0). There is no "sometimes zero, sometimes not." This means you only need to check the Wronskian at a single convenient point — usually t = 0 or t = 1 — to determine independence everywhere.

To use this in practice: whenever you have two candidate solutions y₁ and y₂, compute W[y₁, y₂] and verify it is nonzero before writing down the general solution c₁y₁ + c₂y₂. For example, y₁ = e^(2t) and y₂ = e^(-t): W = e^(2t)(-e^(-t)) - e^(-t)(2e^(2t)) = -e^t - 2e^t = -3e^t ≠ 0. So {e^(2t), e^(-t)} is a fundamental set and the general solution is y = c₁e^(2t) + c₂e^(-t). This structural verification — checking independence before asserting the general solution — prevents the error of writing a "general solution" that secretly misses an entire family of solutions.
