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
stage: abstract-reasoning
status: draft
---

# Lebesgue Integral for Simple Functions

## Core Idea
For a simple function φ = Σᵢ aᵢ 𝟙ₐᵢ, define ∫φ dμ = Σᵢ aᵢ μ(Aᵢ). This definition is well-defined (independent of representation) and linear. It extends to non-negative functions by taking limits of simple approximations.

## Explainer

From your study of simple functions and approximation, you know that a **simple function** is a finite linear combination of indicator functions of measurable sets: φ = Σᵢ aᵢ 𝟙_{Aᵢ}, where each Aᵢ is a measurable set and each aᵢ is a real number. Think of it as a staircase function — it takes finitely many values, each on a measurable region. The Lebesgue integral of such a function has a natural geometric meaning: it is the sum of (height × measure of base) over each step. That is, ∫φ dμ = Σᵢ aᵢ μ(Aᵢ), where μ(Aᵢ) is the measure (generalized "length" or "size") of the set where φ equals aᵢ.

The first technical hurdle is **well-definedness**: the same simple function can be written in many different ways. For instance, the function that equals 1 on [0, 1] can be split as 1 · 𝟙_{[0,½]} + 1 · 𝟙_{(½,1]}, or kept as 1 · 𝟙_{[0,1]}. You need the integral to give the same answer regardless of which representation you use. Proving well-definedness requires showing that the sum Σᵢ aᵢ μ(Aᵢ) is the same for any partition of the domain into measurable sets on which φ is constant — a consequence of the additivity of the measure μ you studied when learning measure spaces.

Linearity follows directly from the definition: ∫(αφ + βψ) dμ = α∫φ dμ + β∫ψ dμ for any simple functions φ, ψ and constants α, β. This is the key algebraic fact that makes the integral well-behaved. It also gives the first half of a crucial monotonicity property: if φ ≤ ψ everywhere, then ∫φ dμ ≤ ∫ψ dμ — larger functions integrate to larger values.

The reason for building the integral on simple functions first is strategic: every non-negative measurable function can be approximated from below by an increasing sequence of simple functions. You proved this in the simple-functions approximation topic. The Lebesgue integral for a general non-negative function is then defined as the supremum of the integrals of all simple functions lying beneath it. This construction — define on a tractable class, verify key properties, then extend by limits — is the central pattern of measure theory, and you will see it repeated when the integral is extended to signed and complex-valued functions.
