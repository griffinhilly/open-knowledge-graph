---
id: kernel-image-rank
title: Kernel, Image, and Rank of Linear Transformations
domain: mathematics
course: linear-algebra
prerequisites:
- id: linear-transformation-definition
  type: hard
- id: vector-subspaces
  type: hard
builds-toward:
- rank-nullity-theorem
tags:
- transformations
- kernel
- image
- rank
stage: formal-systems
status: validated
---

# Kernel, Image, and Rank of Linear Transformations

## Core Idea
For a linear transformation T: V → W, the kernel ker(T) = {x : T(x) = 0} and image im(T) = {T(x) : x ∈ V} are subspaces. Rank is dim(im(T)); nullity is dim(ker(T)). These are the column space and null space for matrix representations.

## Questions

```yaml
- question: "Let T: ℝ³ → ℝ³ have rank 2. A student claims the equation T(x) = w is solvable for every w ∈ ℝ³. Is this correct, and why?"
  type: multiple-choice
  options:
    - "Yes — T maps ℝ³ to ℝ³, so every output vector is reachable"
    - "No — rank 2 means im(T) is only a 2-dimensional plane in ℝ³, so vectors outside that plane have no preimage"
    - "Yes — as long as rank is nonzero, any equation T(x) = w has a solution"
    - "No — rank 2 means the kernel is trivial, so solutions are unique but not guaranteed to exist"
  answer: 1
  explanation: "Solvability of T(x) = w requires w ∈ im(T). If T has rank 2, its image is a 2-dimensional subspace of ℝ³ — a plane through the origin. Any w not lying on that plane cannot be hit by T, so T(x) = w has no solution. Full rank (rank 3 for T: ℝ³ → ℝ³) is required for T to reach every possible output. Option A confuses the domain and codomain being the same dimension with T being surjective — these are not the same thing."

- question: "Suppose T: ℝ⁴ → ℝ³ and ker(T) = {0}. A student finds one solution x₀ to T(x) = w. How many solutions exist?"
  type: multiple-choice
  options:
    - "Infinitely many — the kernel always contributes free solutions"
    - "Exactly one — since ker(T) is trivial, x₀ is the unique solution"
    - "At most one — but we need the rank-nullity theorem to be sure"
    - "None — a 4 × 3 system always has a trivial kernel"
  answer: 1
  explanation: "Whenever T(x₀) = w, every other solution has the form x₀ + k where k ∈ ker(T). If ker(T) = {0}, the only vector in the kernel is zero, so the only solution is x₀ + 0 = x₀. The kernel parameterizes the ambiguity: a trivial kernel means no ambiguity. Note also that ker(T) = {0} for T: ℝ⁴ → ℝ³ is possible — it would mean T is injective even though the codomain has smaller dimension than the domain (rank-nullity would give rank = 4, but im(T) ⊆ ℝ³ has dimension at most 3, so actually ker(T) = {0} is impossible here — but the logic of the question still holds for general T)."

- question: "If T(x₀) = w and ker(T) is trivial (contains only the zero vector), then x₀ is the unique solution to T(x) = w."
  type: true-false
  answer: true
  explanation: "Every solution to T(x) = w has the form x₀ + k for some k ∈ ker(T). When ker(T) = {0}, the only possibility is k = 0, giving x₀ as the only solution. A trivial kernel means T is injective — it never maps two distinct inputs to the same output — so distinct inputs have distinct outputs and x₀ is unique. This is why checking the kernel is the key to uniqueness: a non-trivial kernel introduces infinitely many solutions by adding any kernel element to a particular solution."

- question: "The image of a linear transformation T: V → W is the set of all vectors in V that T maps to zero."
  type: true-false
  answer: false
  explanation: "This describes the kernel, not the image. The image (or range) of T is the set of all possible outputs: im(T) = {T(x) : x ∈ V} ⊆ W. The kernel is the set of inputs that land on zero: ker(T) = {x ∈ V : T(x) = 0} ⊆ V. Confusing kernel and image is one of the most common errors in linear algebra — note they live in different spaces: the kernel is a subspace of the domain V, while the image is a subspace of the codomain W."

- question: "Explain the relationship between the kernel of a linear transformation T and the uniqueness of solutions to the equation T(x) = w."
  type: short-answer
  answer: "If x₀ is any particular solution to T(x) = w, then every other solution has the form x₀ + k where k ∈ ker(T). The kernel therefore parameterizes the non-uniqueness: if ker(T) = {0}, there is exactly one solution; if ker(T) is non-trivial, there are infinitely many solutions (one for each kernel element added to x₀)."
  explanation: "This connection is fundamental. The existence question (does any solution exist?) depends on whether w ∈ im(T). The uniqueness question (is there at most one solution?) depends on whether ker(T) is trivial. These are independent: T can be injective but not surjective (trivial kernel, not full image), surjective but not injective (full image, non-trivial kernel), both (bijective), or neither. The rank-nullity theorem then ties both dimensions together: rank + nullity = dim(V)."
```

## Explainer

Think of a linear transformation T: V → W as a machine that takes vectors from one space and sends them to another. The **kernel** of T is the set of all inputs that the machine "crushes" to zero — the vectors that T cannot distinguish from the zero vector. Every linear transformation sends zero to zero, so the kernel always contains at least the zero vector. But if other vectors land on zero too, those vectors are genuinely lost by T: T has no way to tell them apart from 0.

The **image** of T is what the machine can actually produce — all possible outputs. You already know from your study of vector subspaces that both ker(T) and im(T) are subspaces (closed under addition and scalar multiplication). The image tells you how much of W that T can reach. If T: ℝ³ → ℝ³ is a projection onto a plane, the image is a 2-dimensional plane inside ℝ³, and the kernel is the 1-dimensional line perpendicular to that plane.

**Rank** is the dimension of the image — it measures how much of the output space T actually covers. **Nullity** is the dimension of the kernel — it measures how much information T destroys. For a matrix, rank counts the number of linearly independent columns (the column space), while nullity counts the degrees of freedom in the solution set of Ax = 0 (the null space). These two quantities are not independent: the rank-nullity theorem (your next topic) establishes that rank + nullity = dim(V), meaning that every dimension of the input space is accounted for — it either contributes to the image or is swallowed by the kernel.

The practical payoff is understanding solvability. The equation T(x) = w has a solution if and only if w ∈ im(T). If T has full rank — im(T) = W — then T hits every target and every equation is solvable. If the kernel is non-trivial, solutions are not unique: whenever T(x₀) = w, then T(x₀ + k) = w for any k ∈ ker(T). The kernel parameterizes the ambiguity in solutions, the image determines which equations can be solved at all.
