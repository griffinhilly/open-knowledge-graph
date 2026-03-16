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
status: draft
---

# Nonhomogeneous Recurrence Relations and Particular Solutions

## Core Idea
For nonhomogeneous recurrences a(n) = c₁a(n-1) + ⋯ + f(n), the solution is the sum of the homogeneous solution and a particular solution. The particular solution has specific forms depending on f(n) (polynomial, exponential, trigonometric, etc.), determined by the method of undetermined coefficients.

## Explainer

From your work with linear recurrence relations, you know how to solve **homogeneous** recurrences — those where the right-hand side is zero after moving all terms to one side. The general solution to a homogeneous recurrence is a linear combination of solutions like rⁿ, where r is a characteristic root. A **nonhomogeneous** recurrence adds a forcing function f(n) to the right-hand side, such as a(n) = 3a(n−1) + 2ⁿ or a(n) = a(n−1) + a(n−2) + n². The extra term means the homogeneous solution alone cannot satisfy the recurrence.

The key insight is superposition: the **general solution** to a nonhomogeneous recurrence is the sum of (1) the general solution to the associated homogeneous recurrence, and (2) any single **particular solution** to the nonhomogeneous recurrence. The homogeneous part absorbs the initial conditions; the particular solution handles the forcing term. You have already mastered step 1, so the new skill is finding the particular solution.

The **method of undetermined coefficients** gives you a systematic guess based on the form of f(n). If f(n) is a polynomial of degree k, guess a polynomial of degree k: Aₖnᵏ + Aₖ₋₁nᵏ⁻¹ + ⋯ + A₀. If f(n) = Cαⁿ, guess Aαⁿ. If f(n) combines both (like 3n · 2ⁿ), guess a polynomial times the exponential (An + B)2ⁿ. Plug the guess into the recurrence, match coefficients on both sides, and solve for the unknowns A, B, etc. The one trap: if your particular guess has the same form as a homogeneous solution (because αⁿ is already a characteristic root), multiply your guess by nⁱ where i is the smallest positive integer that makes it linearly independent from the homogeneous solutions.

Once you have the particular solution aₚ(n) and the homogeneous solution aₕ(n), the general solution is a(n) = aₕ(n) + aₚ(n). Apply the initial conditions to determine the free constants in aₕ(n). The method mirrors what you may know from differential equations — and for good reason: linear recurrences are the discrete analog of linear ODEs, and the two theories are nearly identical in structure.
