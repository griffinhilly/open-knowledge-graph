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

## Questions

```yaml
- question: "You compute W[y₁, y₂](0) = 0 for two solutions of a linear ODE. What can you conclude?"
  type: multiple-choice
  options:
    - "Nothing yet — the Wronskian might be nonzero at other points, so independence is still possible"
    - "The solutions are linearly dependent everywhere, because for linear ODEs the Wronskian is either always zero or never zero"
    - "The general solution is y = c₁y₁ + c₂y₂ — you need more information to determine independence"
    - "The ODE has no fundamental set of solutions"
  answer: 1
  explanation: "By Abel's theorem, the Wronskian of two solutions to a linear ODE satisfies W(t) = W(t₀)e^(-∫p dt), which is either always zero or never zero. If W(0) = 0, then W(t) = 0 everywhere — the solutions are linearly dependent globally, not just at t = 0. Option A reflects the common misconception that you need to check multiple points; the 'always or never' property means a single evaluation is definitive."

- question: "Two functions y₁ = sin(t) and y₂ = 2sin(t) are proposed as a fundamental set of solutions for a second-order ODE. Without computing the Wronskian, you can already determine this is incorrect because:"
  type: multiple-choice
  options:
    - "Trigonometric functions cannot be solutions to ODEs with constant coefficients"
    - "y₂ is a constant multiple of y₁, so they are linearly dependent and cannot span the full solution space of a second-order ODE"
    - "The Wronskian of sine functions is always zero regardless of coefficient"
    - "A fundamental set must consist of exponential functions, not trigonometric ones"
  answer: 1
  explanation: "Linear dependence means one function is a scalar multiple of the other — here y₂ = 2y₁, which is the definition of linear dependence. A fundamental set for a second-order ODE must consist of two linearly independent solutions to span the full two-dimensional solution space. The combination c₁y₁ + c₂(2y₁) = (c₁ + 2c₂)y₁ produces only a one-dimensional family — missing entire solutions. Computing the Wronskian would give zero, confirming the dependence."

- question: "If the Wronskian W[y₁, y₂](t₀) ≠ 0 at a single point t₀, then the solutions are linearly independent at all points on the interval."
  type: true-false
  answer: true
  explanation: "This follows from Abel's theorem: for solutions of y'' + p(t)y' + q(t)y = 0, the Wronskian satisfies W(t) = W(t₀)e^(-∫p dt). If W(t₀) ≠ 0, the exponential factor is always positive and finite, so W(t) ≠ 0 everywhere p is continuous. This 'global from local' property is what makes the Wronskian efficient — you pick one easy point rather than checking infinitely many."

- question: "If W[y₁, y₂] ≠ 0, then y₁ and y₂ form a fundamental set, so the general solution is c₁y₁ + c₂y₂."
  type: true-false
  answer: true
  explanation: "This is correct and is the main use of the Wronskian in ODE practice. If W ≠ 0, the two solutions are linearly independent and span the full solution space of the second-order linear ODE — every solution can be written as c₁y₁ + c₂y₂ for some constants c₁, c₂. The Wronskian check is the structural verification step before writing the general solution, preventing the error of using two linearly dependent solutions that would capture only a one-dimensional subset of all solutions."

- question: "Why is Abel's theorem significant for the practical use of the Wronskian as a test of linear independence?"
  type: short-answer
  answer: "Abel's theorem shows that the Wronskian of two solutions to a linear ODE is either always zero or never zero — it cannot vanish at some points and be nonzero at others. This means you only need to evaluate the Wronskian at one convenient point (usually t = 0) to determine independence everywhere on the interval. Without Abel's theorem, you would have to worry that the Wronskian might vanish at some critical point even if it is nonzero elsewhere, undermining the reliability of the test."
  explanation: "The practical payoff is efficiency and confidence. To check if e^(2t) and e^(-t) form a fundamental set, compute W at t = 0: W(0) = (1)(−1) − (1)(2) = −3 ≠ 0. Abel's theorem guarantees this single nonzero evaluation means W ≠ 0 everywhere, so the pair is a fundamental set. The 'always or never' property makes the Wronskian far more useful than if it were only a local test."
```

## Explainer

From your study of 2×2 determinants, you know that the determinant of a matrix [[a, b], [c, d]] equals ad - bc, and that a nonzero determinant means the rows (or columns) are linearly independent. The Wronskian applies this idea to functions: it is the determinant of the matrix [[y₁, y₂], [y₁', y₂']], which equals y₁y₂' - y₂y₁'. Think of it as asking whether the functions y₁ and y₂ are "pointing in different directions" in function space — independent in the same sense that two non-parallel vectors are geometrically independent.

If W[y₁, y₂](t₀) ≠ 0 at even a single point, the solutions are **linearly independent** and form a **fundamental set**: every solution to the ODE can be written as y = c₁y₁ + c₂y₂ for some constants c₁ and c₂. This is the ODE analogue of saying two independent vectors span a plane. If W = 0 everywhere, the solutions are **linearly dependent** — one is a constant multiple of the other, and they only span a one-dimensional family of solutions, which is not enough to capture the full solution space of a second-order equation.

The remarkable property specific to linear ODEs is Abel's theorem: the Wronskian satisfies W'(t) = -p(t)W(t) for a linear ODE y'' + p(t)y' + q(t)y = 0. Solving this first-order ODE gives W(t) = W(t₀)e^(-∫p dt), which is either always zero (if W(t₀) = 0) or never zero (if W(t₀) ≠ 0). There is no "sometimes zero, sometimes not." This means you only need to check the Wronskian at a single convenient point — usually t = 0 or t = 1 — to determine independence everywhere.

To use this in practice: whenever you have two candidate solutions y₁ and y₂, compute W[y₁, y₂] and verify it is nonzero before writing down the general solution c₁y₁ + c₂y₂. For example, y₁ = e^(2t) and y₂ = e^(-t): W = e^(2t)(-e^(-t)) - e^(-t)(2e^(2t)) = -e^t - 2e^t = -3e^t ≠ 0. So {e^(2t), e^(-t)} is a fundamental set and the general solution is y = c₁e^(2t) + c₂e^(-t). This structural verification — checking independence before asserting the general solution — prevents the error of writing a "general solution" that secretly misses an entire family of solutions.
