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

## Questions

```yaml
- question: "After applying the characteristic equation method to a recurrence, a student finds the general solution aₙ = A(2ⁿ) + B(3ⁿ) and immediately announces that A = 1 and B = 1 without using the initial conditions. This is:"
  type: multiple-choice
  options:
    - "Correct — for homogeneous recurrences, the constants are always 1 unless the roots are complex"
    - "Wrong — the constants A and B must be determined by substituting the initial conditions into the general solution and solving the resulting linear system"
    - "A valid shortcut when the characteristic roots are distinct positive integers"
    - "Correct only if the initial conditions happen to be a₀ = 1 and a₁ = 5"
  answer: 1
  explanation: "The general solution contains undetermined constants that represent all solutions to the recurrence. The specific constants satisfying the given initial conditions are found by substituting those conditions (e.g., a₀ and a₁) into the general solution, producing a system of equations. Skipping this step means the solution does not match the actual sequence defined by the recurrence — it is a formula for the wrong sequence."

- question: "The characteristic equation of a linear recurrence has a repeated root r = 4 (multiplicity 2). The general solution is:"
  type: multiple-choice
  options:
    - "aₙ = A(4ⁿ), since both basis solutions are the same"
    - "aₙ = A(4ⁿ) + B(n · 4ⁿ)"
    - "aₙ = A(4ⁿ) + B(4²ⁿ), using the root and its square"
    - "aₙ = A(4ⁿ) + B(4ⁿ⁻¹), shifting by one index"
  answer: 1
  explanation: "When the characteristic polynomial has a repeated root r, the two 'basis solutions' rⁿ and rⁿ are identical and cannot span all solutions — you cannot independently tune two constants if they always appear in the same ratio. The fix is to multiply the second basis solution by n, giving rⁿ and n·rⁿ as two linearly independent solutions. The general solution is then aₙ = Arⁿ + Bnrⁿ. This mirrors the method of undetermined coefficients for repeated roots in differential equations."

- question: "The closed-form expression for the Fibonacci sequence, Fₙ = (φⁿ − ψⁿ)/√5, involves irrational numbers but produces an integer for every non-negative integer n."
  type: true-false
  answer: true
  explanation: "This is one of the most striking facts about the Fibonacci closed form. φ = (1+√5)/2 and ψ = (1−√5)/2 are both irrational, yet their combination (φⁿ − ψⁿ)/√5 is always an integer. The irrational parts cancel exactly because A = 1/√5 and B = −1/√5 were determined by the initial conditions in a way that forces integer output. Verifying this numerically for the first several terms is a useful sanity check after deriving any closed form."

- question: "The characteristic equation method only applies to second-order recurrences (those defined by the two previous terms)."
  type: true-false
  answer: false
  explanation: "The method extends naturally to any order. A degree-k linear homogeneous recurrence with constant coefficients yields a degree-k characteristic polynomial with k roots. The general solution is a linear combination of k basis solutions (one per root, with polynomial multipliers for repeated roots), and k initial conditions determine the k constants. The second-order case is simply the most commonly taught, not a fundamental limitation."

- question: "Explain why assuming aₙ = rⁿ is the right starting point for solving a linear recurrence — why does this 'guess' lead to an exact method rather than just an approximation?"
  type: short-answer
  answer: "Linear recurrences with constant coefficients shift and scale sequences in a way that preserves exponential form. If aₙ = rⁿ, then aₙ₋₁ = rⁿ⁻¹ and aₙ₋₂ = rⁿ⁻², so substituting into cₙ = c₁aₙ₋₁ + c₂aₙ₋₂ gives rⁿ = c₁rⁿ⁻¹ + c₂rⁿ⁻², which factors completely into a polynomial equation in r. Exponentials are eigenfunctions of the shift operator, so substituting one never introduces new terms — it just yields a polynomial whose roots are the exact building blocks of all solutions."
  explanation: "The reason the method is exact (not approximate) is that exponentials are closed under the operations the recurrence applies: scaling and shifting. Any function with this property would work. The characteristic equation approach turns a functional equation (the recurrence) into an algebraic equation (the polynomial), which can then be solved exactly with standard tools like the quadratic formula."
```

## Explainer

You already know what a recurrence relation is — a formula that defines each term of a sequence in terms of earlier terms, like the Fibonacci sequence where F(n) = F(n-1) + F(n-2). You also know the quadratic formula from algebra. The characteristic equation method combines these tools to convert a recursive definition into a **closed-form expression**: a direct formula for the nth term that requires no prior terms to compute.

The core idea is an educated guess. Suppose the solution has the form aₙ = rⁿ for some constant r. Substitute into the recurrence aₙ = c₁aₙ₋₁ + c₂aₙ₋₂: this gives rⁿ = c₁rⁿ⁻¹ + c₂rⁿ⁻², and dividing through by rⁿ⁻² yields r² = c₁r + c₂, or r² − c₁r − c₂ = 0. This is the **characteristic equation**, and its roots r₁ and r₂ are the building blocks of the general solution. If the roots are distinct, the general solution is aₙ = Ar₁ⁿ + Br₂ⁿ — a linear combination of the two basis solutions. The constants A and B are then determined by substituting the initial conditions (two initial values give two equations for two unknowns).

Applying this to Fibonacci — F(n) = F(n-1) + F(n-2), F(0)=0, F(1)=1 — gives the characteristic equation r² − r − 1 = 0. The quadratic formula yields roots φ = (1+√5)/2 (the **golden ratio**) and ψ = (1−√5)/2. The general solution is Fₙ = Aφⁿ + Bψⁿ. Substituting F(0)=0 and F(1)=1 gives a 2×2 linear system whose solution is A = 1/√5 and B = −1/√5. The closed form Fₙ = (φⁿ − ψⁿ)/√5 is remarkable: an expression involving irrational numbers and the golden ratio produces an integer for every non-negative integer n. You can verify this numerically — it's a useful sanity check after any closed-form derivation.

Two complications extend the method. First, **repeated roots**: if the characteristic equation has a repeated root r (discriminant = 0), the two "basis solutions" rⁿ and rⁿ are identical and cannot independently combine to cover all initial conditions. The fix is to multiply the second basis solution by n: the general solution becomes aₙ = Arⁿ + Bnrⁿ. Second, the method extends naturally to higher-order recurrences — a degree-k recurrence has a degree-k characteristic polynomial with k roots, giving a general solution as a linear combination of k basis solutions determined by k initial conditions. Non-homogeneous recurrences (with a non-zero right-hand side like nˢ or cⁿ) require an additional **particular solution**, found by guessing a form that matches the right-hand side — directly analogous to the method of undetermined coefficients in differential equations.
