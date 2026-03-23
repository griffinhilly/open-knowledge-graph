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
status: validated
---

# Solving Linear Recurrence Relations

## Core Idea
Linear homogeneous recurrences like aₙ = c₁aₙ₋₁ + c₂aₙ₋₂ + ... + cₖaₙ₋ₖ have closed-form solutions via the characteristic equation rᵏ − c₁rᵏ⁻¹ − ... − cₖ = 0. The roots determine the general form; initial conditions pin down constants.

## How It's Best Learned
Solve Fibonacci step-by-step: characteristic equation r² = r + 1 gives roots (1±√5)/2; express aₙ as a linear combination scaled by these roots. Verify by computing initial terms.

## Common Misconceptions
The characteristic equation is rᵏ = c₁rᵏ⁻¹ + ... + cₖ, not rᵏ⁻¹ etc. Repeated roots require adjusted forms (terms multiplied by n).

## Questions

```yaml
- question: "For the recurrence aₙ = 5aₙ₋₁ − 6aₙ₋₂, what is the characteristic equation?"
  type: multiple-choice
  options:
    - "r² − 5r + 6 = 0"
    - "r² + 5r − 6 = 0"
    - "r³ − 5r² + 6r = 0"
    - "r = 5r − 6"
  answer: 0
  explanation: "Substituting aₙ = rⁿ gives rⁿ = 5rⁿ⁻¹ − 6rⁿ⁻². Dividing both sides by rⁿ⁻²: r² = 5r − 6, which rearranges to r² − 5r + 6 = 0. The coefficients in the characteristic polynomial match the recurrence coefficients with alternating signs. Option B has wrong signs; option C has wrong degree; option D is just the recurrence restated, not a polynomial in r."

- question: "The characteristic equation of a recurrence has two distinct roots r₁ = 2 and r₂ = 3. What is the general solution?"
  type: multiple-choice
  options:
    - "aₙ = A · 2ⁿ + B · 3ⁿ"
    - "aₙ = A · 2 + B · 3"
    - "aₙ = (A + B) · 5ⁿ"
    - "aₙ = A · 2ⁿ · B · 3ⁿ"
  answer: 0
  explanation: "When the characteristic equation has k distinct roots r₁, r₂, …, rₖ, the general solution is a linear combination aₙ = A₁r₁ⁿ + A₂r₂ⁿ + … + Aₖrₖⁿ. The constants A and B are determined by initial conditions. Option B forgets the exponent n entirely; option C incorrectly adds the bases (you cannot combine exponentials that way); option D multiplies instead of adding — exponential solutions superpose, they don't multiply."

- question: "If the characteristic equation of a recurrence has a repeated root r = 2 (multiplicity 2), the general solution is aₙ = (A + Bn) · 2ⁿ."
  type: true-false
  answer: true
  explanation: "Repeated roots require a modified solution. When r is a root of multiplicity m, the general solution includes terms rⁿ, n·rⁿ, n²·rⁿ, …, nᵐ⁻¹·rⁿ. For a double root r = 2, this gives aₙ = A·2ⁿ + Bn·2ⁿ = (A + Bn)·2ⁿ. This modification is necessary because simply writing aₙ = A·2ⁿ + B·2ⁿ = (A+B)·2ⁿ only gives one free constant, which is insufficient to satisfy two initial conditions."

- question: "The Fibonacci sequence cannot be expressed as a closed-form formula because its characteristic equation has irrational roots."
  type: true-false
  answer: false
  explanation: "Binet's formula Fₙ = (φⁿ − ψⁿ)/√5, where φ = (1+√5)/2 and ψ = (1−√5)/2, IS a valid closed-form despite the irrational numbers. The irrationals cancel perfectly at every integer n, always producing an integer result. The existence of irrational roots does not prevent a closed-form — it just means the formula contains irrational constants that happen to combine to integers."

- question: "Why is the substitution aₙ = rⁿ the key trick for solving linear homogeneous recurrences? What does this assumption accomplish?"
  type: short-answer
  answer: "Substituting aₙ = rⁿ into the recurrence converts a functional equation (a rule connecting sequence terms) into a polynomial equation in r. Every rⁿ factor can be divided out, leaving a polynomial whose roots tell you exactly which exponential bases appear in the solution. The trick works because exponential sequences are the natural eigenfunctions of the shift operator — just as e^(rx) solves linear ODEs with constant coefficients, rⁿ solves linear recurrences with constant coefficients."
  explanation: "This is the discrete analogue of solving differential equations by guessing e^(rx). The reason it works is that linear recurrences are linear maps on sequences, and exponential sequences are eigenvectors of the shift operation. Once you have the roots, the general solution is a linear combination — satisfying superposition — and initial conditions pin down the constants. Without this substitution, converting a recursive definition to a direct formula would require much more complex techniques."
```

## Explainer

You already know from recurrence relations that a sequence can be defined by a rule connecting each term to earlier ones. The challenge is converting that recursive rule into a direct formula — one that gives you the 100th term without computing the first 99. For **linear homogeneous recurrences**, there is a systematic method that works every time, and it reduces the problem to polynomial algebra you already know.

The key insight is to guess that solutions look like powers: try aₙ = rⁿ for some constant r. Substitute into the recurrence aₙ = c₁aₙ₋₁ + c₂aₙ₋₂ to get rⁿ = c₁rⁿ⁻¹ + c₂rⁿ⁻². Dividing through by rⁿ⁻² gives r² = c₁r + c₂, the **characteristic equation**. This is the polynomial whose roots tell you what exponentials appear in the solution. If the roots r₁ and r₂ are distinct, the general solution is aₙ = Ar₁ⁿ + Br₂ⁿ for constants A and B determined by initial conditions.

The Fibonacci sequence, defined by Fₙ = Fₙ₋₁ + Fₙ₋₂ with F₀ = 0, F₁ = 1, is the standard worked example. The characteristic equation r² = r + 1 has roots φ = (1 + √5)/2 ≈ 1.618 (the golden ratio) and ψ = (1 − √5)/2 ≈ −0.618. So Fₙ = Aφⁿ + Bψⁿ. Plugging in F₀ = 0 and F₁ = 1 gives A = 1/√5 and B = −1/√5, yielding the closed-form **Binet's formula**: Fₙ = (φⁿ − ψⁿ)/√5. Despite containing irrational numbers, this formula always produces integers — a remarkable consequence of the algebra.

The method extends gracefully to higher-order recurrences (more previous terms) and to **repeated roots**. If the characteristic equation has a root r of multiplicity m, then the solution includes terms rⁿ, n·rⁿ, n²·rⁿ, …, nᵐ⁻¹·rⁿ — each power of n attached to the same exponential base. The initial conditions still uniquely determine all constants. The connection to your prerequisite on characteristic polynomials is direct: the characteristic polynomial of a recurrence plays exactly the same structural role as the characteristic polynomial of a matrix, and both encode the same idea — find the exponential rates at which the system grows or decays.
