---
id: lebesgue-integral-simple-functions
title: Lebesgue Integral for Simple Functions
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: simple-functions-approximation
  type: hard
- id: measure-spaces-definition
  type: hard
builds-toward:
- lebesgue-integral-non-negative
tags:
- integration
- lebesgue-integral
stage: advanced
status: draft
---

# Lebesgue Integral for Simple Functions

## Core Idea
For a simple function φ = Σᵢ aᵢ 𝟙ₐᵢ, define ∫φ dμ = Σᵢ aᵢ μ(Aᵢ). This definition is well-defined (independent of representation) and linear. It extends to non-negative functions by taking limits of simple approximations.

## Questions

```yaml
- question: "A simple function φ equals 3 on set A (μ(A) = 2) and also equals 3 on set B (μ(B) = 1), where A and B are disjoint. You could write φ as 3·𝟙_A + 3·𝟙_B or equivalently as 3·𝟙_{A∪B}. The Lebesgue integral ∫φ dμ is:"
  type: multiple-choice
  options:
    - "6 using the two-piece representation, 9 using the single-piece representation — the integral depends on the representation chosen"
    - "9 under both representations, confirming the integral is well-defined regardless of how the function is written"
    - "3 under both representations, because the function value is 3 throughout its support"
    - "Undefined because the same value appears twice in the representation"
  answer: 1
  explanation: "Well-definedness is the first and most important property to verify: 3·2 + 3·1 = 9 using the two-piece form; 3·(2+1) = 3·3 = 9 using the single-piece form. The additivity of the measure μ guarantees these agree. The point of verifying well-definedness is that the same simple function can always be written multiple ways, and the integral must be representation-independent. Option A is the classic misconception that the formula Σ aᵢμ(Aᵢ) depends on which partition you choose — it does not."

- question: "Why is the Lebesgue integral for general non-negative measurable functions defined as the supremum of integrals of simple functions lying beneath the function?"
  type: multiple-choice
  options:
    - "Because general measurable functions may be unbounded and the supremum construction handles infinite values gracefully"
    - "Because approximating from below by simple functions is a standard convention inherited from the Riemann integral"
    - "Because every non-negative measurable function can be approximated from below by an increasing sequence of simple functions, and this extends linearity and monotonicity from the simple case to the general case"
    - "Because the supremum guarantees the Lebesgue integral equals the Riemann integral whenever both are defined"
  answer: 2
  explanation: "The deep reason is structural: simple functions are the class on which the integral is easy to define and on which all key properties (well-definedness, linearity, monotonicity) are verifiable directly. The approximation theorem guarantees that every non-negative measurable function is the pointwise limit of an increasing sequence of simple functions. Taking the supremum of simple-function integrals below the target function extends the integral to the general case while preserving its properties. This 'define on a tractable class, then extend by limits' is the central pattern of the entire theory."

- question: "The Lebesgue integral ∫φ dμ of a simple function φ = Σᵢ aᵢ 𝟙_{Aᵢ} can give different numerical values depending on which partition of the domain is used to represent φ."
  type: true-false
  answer: false
  explanation: "This is the well-definedness property, and it is false: the value Σᵢ aᵢμ(Aᵢ) is the same regardless of which representation of φ you use. The proof uses the additivity of the measure μ — when a single set is split into sub-pieces, the sum of their measures equals the measure of the whole. This independence of representation is what makes the definition meaningful; without it, '∫φ dμ' would not be a property of the function φ but of how you chose to write it."

- question: "Linearity of the Lebesgue integral for simple functions — ∫(αφ + βψ) dμ = α∫φ dμ + β∫ψ dμ — follows from the algebraic properties of finite sums and the additivity of the measure μ."
  type: true-false
  answer: true
  explanation: "Linearity at the simple-function level is a direct consequence of the definition: ∫φ dμ = Σᵢ aᵢμ(Aᵢ) is just a weighted sum, and weighted sums are linear. Scaling a function by α scales all aᵢ by α, scaling the integral by α. Adding two simple functions (after finding a common refinement of their partitions) gives a new simple function whose integral is the sum of the original integrals, using additivity of μ. This linearity is then inherited — unchanged — by the extension to general non-negative functions."

- question: "Why does the construction of the Lebesgue integral begin with simple functions rather than defining the integral directly for all measurable functions at once?"
  type: short-answer
  answer: "Simple functions are the most tractable class: they take finitely many values on measurable sets, so the integral has an immediate geometric meaning (sum of height × measure of base, Σ aᵢμ(Aᵢ)) and key properties — well-definedness, linearity, monotonicity — can be verified directly using finite sums and measure additivity. Once these properties are established on the simple class, the integral extends to general non-negative functions by taking the supremum over all simple functions lying below, inheriting all established properties. This 'define on a tractable class, verify properties, extend by limits' strategy is the central pattern repeated throughout measure theory."
  explanation: "The pedagogical and mathematical point is the same: building upward from simple cases ensures you know exactly which properties the integral has and why. Trying to define the integral for all measurable functions at once would make verification of properties much harder and obscure the source of the integral's good behavior."
```

## Explainer

From your study of simple functions and approximation, you know that a **simple function** is a finite linear combination of indicator functions of measurable sets: φ = Σᵢ aᵢ 𝟙_{Aᵢ}, where each Aᵢ is a measurable set and each aᵢ is a real number. Think of it as a staircase function — it takes finitely many values, each on a measurable region. The Lebesgue integral of such a function has a natural geometric meaning: it is the sum of (height × measure of base) over each step. That is, ∫φ dμ = Σᵢ aᵢ μ(Aᵢ), where μ(Aᵢ) is the measure (generalized "length" or "size") of the set where φ equals aᵢ.

The first technical hurdle is **well-definedness**: the same simple function can be written in many different ways. For instance, the function that equals 1 on [0, 1] can be split as 1 · 𝟙_{[0,½]} + 1 · 𝟙_{(½,1]}, or kept as 1 · 𝟙_{[0,1]}. You need the integral to give the same answer regardless of which representation you use. Proving well-definedness requires showing that the sum Σᵢ aᵢ μ(Aᵢ) is the same for any partition of the domain into measurable sets on which φ is constant — a consequence of the additivity of the measure μ you studied when learning measure spaces.

Linearity follows directly from the definition: ∫(αφ + βψ) dμ = α∫φ dμ + β∫ψ dμ for any simple functions φ, ψ and constants α, β. This is the key algebraic fact that makes the integral well-behaved. It also gives the first half of a crucial monotonicity property: if φ ≤ ψ everywhere, then ∫φ dμ ≤ ∫ψ dμ — larger functions integrate to larger values.

The reason for building the integral on simple functions first is strategic: every non-negative measurable function can be approximated from below by an increasing sequence of simple functions. You proved this in the simple-functions approximation topic. The Lebesgue integral for a general non-negative function is then defined as the supremum of the integrals of all simple functions lying beneath it. This construction — define on a tractable class, verify key properties, then extend by limits — is the central pattern of measure theory, and you will see it repeated when the integral is extended to signed and complex-valued functions.
