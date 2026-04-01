---
id: lebesgue-integral-general-definition
title: 'Lebesgue Integral: General Definition'
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: lebesgue-integral-non-negative
  type: hard
- id: introduction-lebesgue-integral
  type: soft
builds-toward:
- lebesgue-integral
- riemann-lebesgue-comparison
- dominated-convergence-theorem
tags:
- integration
- lebesgue-integral
stage: expert
status: validated
---
# Lebesgue Integral: General Definition

## Core Idea
For general measurable f, decompose f = f⁺ - f⁻ (positive and negative parts). If at least one of ∫f⁺ or ∫f⁻ is finite, define ∫f dμ = ∫f⁺ - ∫f⁻. Functions with ∫|f| < ∞ are integrable. This preserves linearity for signed functions.

## Questions

```yaml
- question: "Let f be a measurable function where ∫f⁺ dμ = +∞ and ∫f⁻ dμ = +∞. What is ∫f dμ?"
  type: multiple-choice
  options:
    - "∫f dμ = 0 — the positive and negative infinite parts cancel each other out"
    - "∫f dμ = +∞ — the positive part dominates when both parts are infinite"
    - "∫f dμ is undefined — ∞ − ∞ has no well-defined value in this context"
    - "∫f dμ = −∞ — the negative part subtracts from the positive, pulling the result to −∞"
  answer: 2
  explanation: "When both ∫f⁺ and ∫f⁻ are infinite, ∫f = ∫f⁺ − ∫f⁻ = ∞ − ∞, which is genuinely undefined — not zero, not infinite. Unlike a limit approaching ∞ − ∞ that might have a specific value, two separately infinite integrals have no well-defined net result. This is the exact problem the decomposition is designed to avoid: the definition of ∫f dμ = ∫f⁺ − ∫f⁻ only applies when at least one of the two integrals is finite."

- question: "A measurable function f satisfies ∫f⁺ dμ = 5 and ∫f⁻ dμ = +∞. Which statement correctly describes ∫f dμ and whether f is integrable?"
  type: multiple-choice
  options:
    - "f is integrable and ∫f dμ = 5, since only the finite part contributes"
    - "f is not integrable (∫|f| = ∞), but ∫f dμ = −∞ is still a well-defined extended real value"
    - "∫f dμ is undefined because one integral is infinite — any infinite integral prevents the Lebesgue integral from being defined"
    - "f is integrable and ∫f dμ = −∞, since the negative part dominates"
  answer: 1
  explanation: "Since ∫f⁺ = 5 (finite) and ∫f⁻ = +∞, the subtraction ∫f⁺ − ∫f⁻ = 5 − ∞ = −∞ is a well-defined extended real value (not the undefined ∞ − ∞). So ∫f dμ = −∞ exists. However, f is NOT integrable in the L¹ sense because ∫|f| = ∫f⁺ + ∫f⁻ = 5 + ∞ = +∞. Integrability (L¹) requires ∫|f| < ∞ — both parts must be individually finite. The integral can be defined as an extended real value without f being in L¹."

- question: "If ∫|f| dμ < ∞ (f is in L¹), then both ∫f⁺ dμ and ∫f⁻ dμ must individually be finite."
  type: true-false
  answer: true
  explanation: "Since |f| = f⁺ + f⁻, we have ∫|f| = ∫f⁺ + ∫f⁻. If this sum is finite, each non-negative term must be finite individually — a finite sum of non-negative quantities requires each summand to be finite. This is why L¹ integrability is the clean, useful condition: it guarantees ∫f = ∫f⁺ − ∫f⁻ is a well-defined, finite real number, enabling linearity, the dominated convergence theorem, and other essential tools."

- question: "The decomposition f = f⁺ − f⁻ is necessary because the Lebesgue integral cannot handle negative function values."
  type: true-false
  answer: false
  explanation: "The decomposition is not needed because the Lebesgue integral 'can't handle' negatives — it's needed to prevent the undefined form ∞ − ∞. If both f⁺ and f⁻ have finite integrals, signed values pose no difficulty whatsoever; ∫f = ∫f⁺ − ∫f⁻ is a straightforward finite subtraction. The problem arises only when both parts have infinite integrals, making the subtraction undefined. The decomposition is a mechanism to isolate and manage this specific ∞ − ∞ problem, not a restriction on negativity."

- question: "Why does ∞ − ∞ pose a specific problem for defining the integral of a signed function, and how does the f⁺/f⁻ decomposition resolve it?"
  type: short-answer
  answer: "The expression ∞ − ∞ is genuinely undefined — unlike a limit that approaches a specific value, two independently infinite quantities that 'cancel' cannot be assigned a consistent real value. For a signed function with infinite positive area above the x-axis and infinite negative area below, there is no consistent way to assign a net integral. The decomposition avoids this by integrating f⁺ and f⁻ separately using the non-negative Lebesgue integral (which is always well-defined in [0, +∞]). The subtraction ∫f⁺ − ∫f⁻ is only performed when at least one term is finite, ensuring the result is either a finite number or ±∞ — never the undefined ∞ − ∞."
  explanation: "This careful conditional definition is what distinguishes rigorous Lebesgue integration from a naive 'add up positive and negative areas' approach. The condition 'at least one of ∫f⁺ or ∫f⁻ is finite' is precisely the guard that prevents the undefined case."
```

## Explainer

You've already built the Lebesgue integral for non-negative measurable functions, starting with simple functions and taking monotone limits. That construction worked cleanly because all integrals were either finite non-negative numbers or +∞ — no cancellation issues. The challenge with a general function f is that it takes both positive and negative values, and subtracting two infinite quantities leads to the undefined expression ∞ − ∞.

The solution is a clean decomposition: define **f⁺(x) = max(f(x), 0)** (the positive part) and **f⁻(x) = max(−f(x), 0)** (the negative part, always non-negative). Then f = f⁺ − f⁻ everywhere, and |f| = f⁺ + f⁻. Both f⁺ and f⁻ are non-negative measurable functions, so the Lebesgue integral you already defined applies to each of them. The integral of f is then ∫f dμ = ∫f⁺ dμ − ∫f⁻ dμ, provided this subtraction is not ∞ − ∞.

The condition "at least one of ∫f⁺ or ∫f⁻ is finite" is exactly what prevents the ∞ − ∞ problem. If both are infinite, the integral is undefined — not zero, not infinite, but genuinely undefined, because the positive and negative contributions overwhelm each other with no well-defined net result. A function is called **integrable** (or in L¹) when the stronger condition ∫|f| dμ = ∫f⁺ dμ + ∫f⁻ dμ < ∞ holds, meaning both parts are individually finite. Integrability ensures well-defined, finite integrals with all the nice properties — linearity, dominated convergence — you'll use going forward.

This decomposition also reveals why linearity holds for signed functions. If f = f⁺ − f⁻ and g = g⁺ − g⁻, then (f + g) can be decomposed similarly, and the integral of the sum equals the sum of the integrals. The same argument fails to work cleanly with a direct Riemann-style definition for functions with complicated sign-change structure, which is one reason the Lebesgue theory is essential for handling functions that oscillate wildly or are defined on irregular domains.
