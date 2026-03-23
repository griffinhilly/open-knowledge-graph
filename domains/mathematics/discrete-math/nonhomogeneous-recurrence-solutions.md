---
id: nonhomogeneous-recurrence-solutions
title: Nonhomogeneous Recurrence Relations and Particular Solutions
domain: mathematics
course: discrete-math
prerequisites:
- id: linear-recurrence-solutions
  type: hard
builds-toward:
- divide-conquer-recurrence-analysis
tags:
- recurrence-relations
- nonhomogeneous
stage: formal-systems
status: validated
---

# Nonhomogeneous Recurrence Relations and Particular Solutions

## Core Idea
For nonhomogeneous recurrences a(n) = c₁a(n-1) + ⋯ + f(n), the solution is the sum of the homogeneous solution and a particular solution. The particular solution has specific forms depending on f(n) (polynomial, exponential, trigonometric, etc.), determined by the method of undetermined coefficients.

## Questions

```yaml
- question: "The recurrence a(n) = 2a(n−1) + 3ⁿ has characteristic root r = 2. To find a particular solution using undetermined coefficients, which guess is correct?"
  type: multiple-choice
  options:
    - "A·2ⁿ, matching the form of the homogeneous solution"
    - "A·3ⁿ, since 3 is not a characteristic root"
    - "An + B, since 3ⁿ grows like a polynomial eventually"
    - "A·n·2ⁿ, multiplying by n to handle the repeated root"
  answer: 1
  explanation: "When f(n) = C·αⁿ, you guess A·αⁿ — provided αⁿ is not already a homogeneous solution. Here f(n) = 3ⁿ and the characteristic root is r = 2, so 3ⁿ is not a homogeneous solution. The correct guess is A·3ⁿ. Option A fails because 2ⁿ is the homogeneous solution — substituting it into the recurrence would make both sides cancel the homogeneous part, leaving an impossible equation. Option D (A·n·2ⁿ) is the fix for *that* problem, but it's not needed here since 3 ≠ 2."

- question: "For the recurrence a(n) = 3a(n−1) + 3ⁿ, the characteristic root is r = 3. What is the correct form for a particular solution guess?"
  type: multiple-choice
  options:
    - "A·3ⁿ — match the form of the forcing function directly"
    - "A·n·3ⁿ — multiply by n since 3ⁿ matches the homogeneous solution"
    - "An + B — use a polynomial since 3ⁿ and 3ⁿ cancel"
    - "A·n² — escalate to a quadratic when the standard guess fails"
  answer: 1
  explanation: "When the natural guess (A·αⁿ) has the same form as a homogeneous solution, substituting it in causes complete cancellation, making it impossible to match the nonzero right-hand side. The fix is to multiply by n: guess A·n·3ⁿ. In general, multiply by nⁱ where i is the smallest positive integer making the guess linearly independent from all homogeneous solutions. If 3ⁿ were a repeated homogeneous root, you'd need A·n²·3ⁿ, and so on."

- question: "The general solution to a nonhomogeneous recurrence is found by subtracting the particular solution from the homogeneous solution."
  type: true-false
  answer: false
  explanation: "The general solution is the *sum* of the homogeneous solution and the particular solution: a(n) = aₕ(n) + aₚ(n). The homogeneous part absorbs the initial conditions (its free constants are set by them); the particular part handles the forcing function. Subtracting would give a function that satisfies neither the recurrence nor the initial conditions correctly. This mirrors the structure of linear ODEs exactly."

- question: "After finding the general solution a(n) = aₕ(n) + aₚ(n), the initial conditions are applied only to the homogeneous part aₕ(n) to determine its free constants."
  type: true-false
  answer: true
  explanation: "The particular solution aₚ(n) is a *specific* function with no free constants — it was fully determined by matching coefficients to the forcing function. The homogeneous solution aₕ(n) contains the free constants (e.g., C₁r₁ⁿ + C₂r₂ⁿ). You substitute the initial conditions into the full general solution a(n) = aₕ(n) + aₚ(n) to get equations for C₁, C₂, etc. The particular solution's contribution at those initial points is a known, fixed number."

- question: "Why must you multiply your particular-solution guess by n when the natural guess has the same form as a homogeneous solution?"
  type: short-answer
  answer: "A homogeneous solution already satisfies the recurrence with right-hand side zero. If you plug a particular guess of the same form into the nonhomogeneous recurrence, both sides reduce the guess to zero (the homogeneous solution 'absorbs' it), making it impossible to match the nonzero forcing function f(n). Multiplying by n produces a function in the same family (e.g., n·αⁿ instead of αⁿ) that is linearly independent from the homogeneous solutions, so it does not cancel out when substituted, and its unknown coefficient can be determined by matching f(n)."
  explanation: "This is the discrete analog of the identical situation in solving linear ODEs with constant coefficients — when the forcing function matches a homogeneous solution, reduction of order (or the analogous n-multiplication here) is required. The mathematical reason is always the same: the operator applied to a homogeneous solution gives zero, so you must step outside that solution space."
```

## Explainer

From your work with linear recurrence relations, you know how to solve **homogeneous** recurrences — those where the right-hand side is zero after moving all terms to one side. The general solution to a homogeneous recurrence is a linear combination of solutions like rⁿ, where r is a characteristic root. A **nonhomogeneous** recurrence adds a forcing function f(n) to the right-hand side, such as a(n) = 3a(n−1) + 2ⁿ or a(n) = a(n−1) + a(n−2) + n². The extra term means the homogeneous solution alone cannot satisfy the recurrence.

The key insight is superposition: the **general solution** to a nonhomogeneous recurrence is the sum of (1) the general solution to the associated homogeneous recurrence, and (2) any single **particular solution** to the nonhomogeneous recurrence. The homogeneous part absorbs the initial conditions; the particular solution handles the forcing term. You have already mastered step 1, so the new skill is finding the particular solution.

The **method of undetermined coefficients** gives you a systematic guess based on the form of f(n). If f(n) is a polynomial of degree k, guess a polynomial of degree k: Aₖnᵏ + Aₖ₋₁nᵏ⁻¹ + ⋯ + A₀. If f(n) = Cαⁿ, guess Aαⁿ. If f(n) combines both (like 3n · 2ⁿ), guess a polynomial times the exponential (An + B)2ⁿ. Plug the guess into the recurrence, match coefficients on both sides, and solve for the unknowns A, B, etc. The one trap: if your particular guess has the same form as a homogeneous solution (because αⁿ is already a characteristic root), multiply your guess by nⁱ where i is the smallest positive integer that makes it linearly independent from the homogeneous solutions.

Once you have the particular solution aₚ(n) and the homogeneous solution aₕ(n), the general solution is a(n) = aₕ(n) + aₚ(n). Apply the initial conditions to determine the free constants in aₕ(n). The method mirrors what you may know from differential equations — and for good reason: linear recurrences are the discrete analog of linear ODEs, and the two theories are nearly identical in structure.
