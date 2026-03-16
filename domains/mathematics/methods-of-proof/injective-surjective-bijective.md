---
id: injective-surjective-bijective
title: Injective, Surjective, and Bijective Functions
domain: mathematics
course: methods-of-proof
prerequisites:
- id: equivalence-relations
  type: soft
builds-toward:
- cardinality-and-countability
tags:
- functions
- injective
- surjective
stage: formal-systems
status: draft
---

# Injective, Surjective, and Bijective Functions

## Core Idea
A function f: A → B is injective (one-to-one) if distinct inputs give distinct outputs; surjective (onto) if every element of B is mapped to; bijective if both. Bijections establish correspondences and are essential for comparing cardinalities.

## Explainer

A function f: A → B assigns each element of A (the domain) exactly one element of B (the codomain). But the same definition allows very different behaviors: multiple inputs might map to the same output, or some outputs might never be hit at all. The properties of injectivity, surjectivity, and bijectivity classify functions by how thoroughly they respect the structure of their domain and codomain.

A function is **injective** (one-to-one) if no two distinct inputs produce the same output: if f(a₁) = f(a₂) then a₁ = a₂. Injectivity is a statement about the domain — the function doesn't "collapse" any distinct elements together. The contrapositive form is often used in proofs: to show injectivity, assume f(a₁) = f(a₂) and derive a₁ = a₂. For example, f(x) = 2x from ℝ to ℝ is injective: 2x₁ = 2x₂ immediately gives x₁ = x₂. The function f(x) = x² is not injective over ℝ because f(2) = f(−2) = 4.

A function is **surjective** (onto) if every element b ∈ B is the image of at least one element a ∈ A: for every b there exists a with f(a) = b. Surjectivity is a statement about the codomain — the function hits everything. Notice that surjectivity depends critically on how the codomain is defined. The function f(x) = x² is not surjective from ℝ to ℝ (negative numbers are never hit), but it is surjective from ℝ to [0, ∞). This is why the codomain is part of the function's definition.

A function is **bijective** if it is both injective and surjective — a perfect one-to-one correspondence between domain and codomain. Every element of B is hit by exactly one element of A. Bijections are the right notion of "same size" for sets: if a bijection exists between A and B, they have the same cardinality. This works even for infinite sets — the existence of a bijection between the natural numbers and the even numbers shows they have the same cardinality despite one being a proper subset of the other. A bijection is also exactly the condition under which the inverse function f⁻¹: B → A exists as a function.
