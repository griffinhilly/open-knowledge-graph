---
id: linear-transformations-definition
title: Linear Transformations and Their Properties
domain: mathematics
course: linear-algebra
prerequisites:
- id: function-notation-review
  type: soft
- id: basis-and-dimension
  type: hard
builds-toward:
- linear-transformation-matrix-representation
- kernel-and-image
tags:
- linear-transformations
- mappings
- functions
stage: formal-systems
status: draft
---

# Linear Transformations and Their Properties

## Core Idea
A linear transformation T: V → W is a function satisfying T(u + v) = T(u) + T(v) and T(cu) = cT(u). Examples: rotation, projection, differentiation, matrix multiplication. Linear transformations preserve vector space structure, making them natural maps between vector spaces. The kernel and image determine injectivity and surjectivity.

## How It's Best Learned
Check linearity carefully: verify both additivity and homogeneity. Explore examples: derivatives T(p) = p', rotations, projections onto a line. Visualize in R² and R³.

## Questions

```yaml
- question: "Is the function T: ℝ² → ℝ² defined by T(x, y) = (x + 1, y) a linear transformation?"
  type: multiple-choice
  options:
    - "Yes — it maps ℝ² to ℝ², which is the definition of a linear transformation"
    - "Yes — it is a simple and natural operation on vectors"
    - "No — it fails to map the zero vector to the zero vector, which is required for linearity"
    - "No — linear transformations must only involve multiplication, not addition of constants"
  answer: 2
  explanation: "A necessary condition for any linear transformation is T(0) = 0. Setting (x, y) = (0, 0): T(0, 0) = (1, 0) ≠ (0, 0). This immediately disqualifies T. This is a translation — shifting the entire plane — and translations do not preserve the origin or vector addition. Option D gives the right verdict but wrong reason; the issue is not that addition is used, but that the constant shift breaks the linearity conditions."

- question: "If T: V → W is a linear transformation and {v₁, v₂, v₃} is a basis for V, and you know T(v₁), T(v₂), and T(v₃), how much of T do you know?"
  type: multiple-choice
  options:
    - "Only T's behavior on those three specific vectors — you need to check all other vectors separately"
    - "T completely — linearity forces T(c₁v₁ + c₂v₂ + c₃v₃) = c₁T(v₁) + c₂T(v₂) + c₃T(v₃) for any coefficients"
    - "T's behavior on linear combinations of two basis vectors at a time, but not all three simultaneously"
    - "Enough to determine whether T is invertible, but not the full transformation"
  answer: 1
  explanation: "Since every vector v in V can be written as a unique linear combination of basis vectors, linearity extends T to all of V: T(c₁v₁ + c₂v₂ + c₃v₃) = c₁T(v₁) + c₂T(v₂) + c₃T(v₃). Specifying T on a basis completely determines T everywhere. This is why a linear transformation T: ℝⁿ → ℝᵐ is represented by a matrix whose columns are exactly the images of the standard basis vectors."

- question: "A function T satisfying T(cu) = cT(u) for all scalars c and vectors u is automatically a linear transformation."
  type: true-false
  answer: false
  explanation: "Homogeneity (T(cu) = cT(u)) is only one of two required conditions. Linearity also requires additivity: T(u + v) = T(u) + T(v). Together they define a linear transformation; neither condition alone is sufficient. Both must hold to ensure T preserves linear combinations, which is the fundamental requirement."

- question: "If ker(T) = {0}, the linear transformation T is injective — no two different inputs produce the same output."
  type: true-false
  answer: true
  explanation: "The kernel is the set of all inputs that map to zero. If the only input mapping to zero is zero itself, T cannot map two different vectors to the same output: if T(u) = T(v), then T(u − v) = 0, so u − v ∈ ker(T) = {0}, meaning u = v. A trivial kernel is both necessary and sufficient for injectivity."

- question: "Why is 'T(0) = 0' a necessary condition for linearity, and what kind of common geometric operation does this rule out?"
  type: short-answer
  answer: "Setting u = v = 0 in the additivity condition gives T(0) = T(0 + 0) = T(0) + T(0), so T(0) = 0. Any function that doesn't map the origin to the origin fails this test. This rules out translations — functions of the form T(v) = Av + b for nonzero b — which shift the origin and fail linearity even though they look 'linear' in everyday language."
  explanation: "This quick test is a useful first check: before verifying both linearity conditions, simply check whether T maps 0 to 0. If not, you're done — it's not linear. Translations are the most common geometric example students mistakenly classify as linear. The distinction matters: affine functions (linear + constant) are not linear transformations in the vector space sense."
```

## Explainer

A linear transformation is a function with special structure — it respects the two core operations of a vector space: addition and scalar multiplication. From your work with bases and dimensions, you know that a vector space is characterized by these operations. A linear transformation T: V → W preserves them, meaning T(u + v) = T(u) + T(v) and T(cu) = cT(u). This is called **linearity** — two conditions that together say "T doesn't disturb the algebraic structure of V." Together, the two conditions imply T(c₁u + c₂v) = c₁T(u) + c₂T(v), meaning T preserves any linear combination.

Consider rotation in R² by angle θ. If you rotate two vectors and add, or add first and then rotate, you get the same result — rotation is linear. Now consider the function T(v) = v + c for some fixed nonzero c (a **translation**). T(u + v) = u + v + c, but T(u) + T(v) = (u + c) + (v + c) = u + v + 2c. These differ, so translations are not linear. A quick check: linear transformations must always map 0 to 0. Setting u = v = 0 in the additivity condition gives T(0) = T(0 + 0) = T(0) + T(0), so T(0) = 0. If a function doesn't map 0 to 0, it's immediately disqualified.

Here is the most powerful consequence of linearity, connecting directly back to your prerequisite on basis and dimension. Once you know where T sends every basis vector, you know T completely. If {v₁, v₂, ..., vₙ} is a basis for V, then any vector v = c₁v₁ + ... + cₙvₙ, and linearity forces T(v) = c₁T(v₁) + ... + cₙT(vₙ). Specifying T on a finite set — the basis — determines T on all of V. This is why, in the next topic, you will represent T by a matrix: the columns of that matrix are exactly the images of the basis vectors.

Two subspaces characterize every linear transformation. The **kernel** of T is ker(T) = {v ∈ V : T(v) = 0} — the set of all inputs that collapse to zero. The **image** of T is im(T) = {T(v) : v ∈ V} — the set of all outputs. The kernel measures how much T "collapses": if ker(T) = {0}, then T is injective (no two inputs produce the same output). The image measures how much of W T reaches: if im(T) = W, then T is surjective. Both are subspaces, and their dimensions are linked by the rank-nullity theorem — a direct generalization of ideas you already know from column space and null space in matrix algebra.
