---
id: linear-recurrence-solutions
title: Solving Linear Recurrence Relations via Characteristic Equations
domain: mathematics
course: discrete-math
prerequisites:
- id: recurrence-relations-definition
  type: hard
builds-toward:
- nonhomogeneous-recurrence-solutions
tags:
- recurrence-relations
- characteristic-equations
stage: formal-systems
status: draft
---

# Solving Linear Recurrence Relations via Characteristic Equations

## Core Idea
For homogeneous linear recurrences a(n) = c₁a(n-1) + ⋯ + cₖa(n-k), the characteristic equation is xᵏ - c₁xᵏ⁻¹ - ⋯ - cₖ = 0. The general solution is a linear combination of terms r^n where r are roots of the characteristic equation. Repeated roots yield polynomial factors in the solution.

## Explainer

You already know what a recurrence relation is — a rule that defines each term of a sequence in terms of earlier terms. The Fibonacci sequence is the classic example: F(n) = F(n−1) + F(n−2). The challenge is going from this recursive rule to an explicit **closed-form formula** — an expression that gives F(n) directly, without computing all previous terms. The **characteristic equation** method provides this.

The key insight is to guess that the solution has the form a(n) = r^n for some constant r, then determine which values of r work. Substituting into F(n) = F(n−1) + F(n−2) gives r^n = r^(n−1) + r^(n−2). Dividing through by r^(n−2) yields r² = r + 1, or equivalently r² − r − 1 = 0. This is the **characteristic equation** of the recurrence. Solving gives r = (1 ± √5)/2 — the golden ratio φ and its conjugate ψ. Because the recurrence is linear, any linear combination of valid solutions is also a solution, so the general solution is F(n) = Aφ^n + Bψ^n, where the constants A and B are determined by the initial conditions F(0) = 0 and F(1) = 1.

For a k-th order linear recurrence a(n) = c₁a(n−1) + ⋯ + cₖa(n−k), the **characteristic polynomial** is x^k − c₁x^(k−1) − ⋯ − cₖ = 0. If it has k distinct roots r₁, r₂, …, rₖ, the general solution is a(n) = A₁r₁^n + A₂r₂^n + ⋯ + Aₖrₖ^n. The k initial conditions a(0), a(1), …, a(k−1) give you k equations to solve for A₁, …, Aₖ — a linear system you can solve by substitution or matrix methods.

**Repeated roots** require a modification. If r is a root of multiplicity m, then r^n, n·r^n, n²·r^n, …, n^(m−1)·r^n are all linearly independent solutions that must be included in the general solution. This parallels the treatment of repeated roots in differential equations, and for the same reason: both involve solving linear equations over a space of exponential-type basis functions. The underlying reason this all works is that the set of all solutions to a homogeneous k-th order linear recurrence forms a k-dimensional vector space, and the characteristic root terms (with polynomial factors for repeated roots) form a basis for that space.
