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

## Explainer

You already know what a recurrence relation is — a formula that defines each term of a sequence in terms of earlier terms, like the Fibonacci sequence where F(n) = F(n-1) + F(n-2). You also know the quadratic formula from algebra. The characteristic equation method combines these tools to convert a recursive definition into a **closed-form expression**: a direct formula for the nth term that requires no prior terms to compute.

The core idea is an educated guess. Suppose the solution has the form aₙ = rⁿ for some constant r. Substitute into the recurrence aₙ = c₁aₙ₋₁ + c₂aₙ₋₂: this gives rⁿ = c₁rⁿ⁻¹ + c₂rⁿ⁻², and dividing through by rⁿ⁻² yields r² = c₁r + c₂, or r² − c₁r − c₂ = 0. This is the **characteristic equation**, and its roots r₁ and r₂ are the building blocks of the general solution. If the roots are distinct, the general solution is aₙ = Ar₁ⁿ + Br₂ⁿ — a linear combination of the two basis solutions. The constants A and B are then determined by substituting the initial conditions (two initial values give two equations for two unknowns).

Applying this to Fibonacci — F(n) = F(n-1) + F(n-2), F(0)=0, F(1)=1 — gives the characteristic equation r² − r − 1 = 0. The quadratic formula yields roots φ = (1+√5)/2 (the **golden ratio**) and ψ = (1−√5)/2. The general solution is Fₙ = Aφⁿ + Bψⁿ. Substituting F(0)=0 and F(1)=1 gives a 2×2 linear system whose solution is A = 1/√5 and B = −1/√5. The closed form Fₙ = (φⁿ − ψⁿ)/√5 is remarkable: an expression involving irrational numbers and the golden ratio produces an integer for every non-negative integer n. You can verify this numerically — it's a useful sanity check after any closed-form derivation.

Two complications extend the method. First, **repeated roots**: if the characteristic equation has a repeated root r (discriminant = 0), the two "basis solutions" rⁿ and rⁿ are identical and cannot independently combine to cover all initial conditions. The fix is to multiply the second basis solution by n: the general solution becomes aₙ = Arⁿ + Bnrⁿ. Second, the method extends naturally to higher-order recurrences — a degree-k recurrence has a degree-k characteristic polynomial with k roots, giving a general solution as a linear combination of k basis solutions determined by k initial conditions. Non-homogeneous recurrences (with a non-zero right-hand side like nˢ or cⁿ) require an additional **particular solution**, found by guessing a form that matches the right-hand side — directly analogous to the method of undetermined coefficients in differential equations.
