---
id: composition-linear-transformations
title: Composition of Linear Transformations
domain: mathematics
course: linear-algebra
prerequisites:
- id: matrix-representation-linear-transformations
  type: hard
builds-toward:
- eigenvalues-and-eigenvectors
- diagonalization
tags:
- composition
- matrix-multiplication
- invertible
stage: formal-systems
status: draft
---

# Composition of Linear Transformations

## Core Idea
The composition of linear transformations S ∘ T is linear, and its matrix representation is the product [S][T]. Invertible transformations form a group under composition (the general linear group GL_n). Composition of matrices directly corresponds to sequential application of transformations.

## Questions

```yaml
- question: "Transformation T is a 90° counterclockwise rotation and S is a horizontal reflection. You apply T first, then S. Which matrix represents this composite transformation?"
  type: multiple-choice
  options:
    - "[T][S] — the first transformation goes on the left"
    - "[S][T] — the first transformation goes on the right"
    - "[T] + [S] — transformations combine by addition"
    - "[S]⁻¹[T] — you invert the second transformation before composing"
  answer: 1
  explanation: "The matrix of S ∘ T (apply T first, then S) is [S][T]. The first transformation applied temporally (T) has its matrix on the right; the second (S) goes on the left. This follows from how matrix-vector multiplication works: [S][T]v = [S]([T]v) — v is first multiplied by [T] (apply T), then by [S] (apply S). Option A reverses the order, which would mean S is applied first. This reversal between temporal order and matrix order is the central confusion in this topic."

- question: "A student sets up the matrix product for 'scale by 2, then rotate by 45°' as [Scale][Rotate]. What error has the student made?"
  type: multiple-choice
  options:
    - "Nothing — the first operation always goes on the left in matrix products"
    - "The operations should be added, not multiplied"
    - "The order is reversed: if scaling happens first (temporally), its matrix goes on the right. The correct product is [Rotate][Scale]"
    - "Matrix products require both transformations to have the same dimensions"
  answer: 2
  explanation: "The fundamental rule: in the product [A][B], transformation B is applied first and A second. 'First temporally = rightmost in the product.' The student has put the first operation (Scale) on the left, which encodes 'scale second.' The correct product is [Rotate][Scale]v = [Rotate]([Scale]v): first scale, then rotate. This reversal consistently trips up students because English reads left to right, but transformations are applied right to left in matrix notation."

- question: "Matrix multiplication is non-commutative in general because function composition is non-commutative — rotating then reflecting gives a different result than reflecting then rotating."
  type: true-false
  answer: true
  explanation: "This is the geometric root of matrix non-commutativity. Since [S][T] represents 'do T then S' and [T][S] represents 'do S then T,' and applying two geometric operations in different orders generally produces different results, these are typically different matrices. The non-commutativity of matrix multiplication is not an arbitrary algebraic quirk — it directly mirrors the fact that the order of operations matters for transformations."

- question: "The matrix of the composition S ∘ T is [T][S] — you write the matrices in the same left-to-right order as you read the composition notation (S first, then T)."
  type: true-false
  answer: false
  explanation: "The correct formula is [S][T], not [T][S]. In the notation S ∘ T, T is applied first — but its matrix goes on the right. There is a systematic reversal between the way you write/read the composition and the order of the matrix product. S ∘ T means 'apply T, then apply S,' and [S][T] encodes this: reading right to left gives the temporal order. This confusion — reading left to right and writing [T][S] — is one of the most persistent errors in linear algebra."

- question: "Why is matrix multiplication defined using dot products of rows with columns? What does this computational rule have to do with composing linear transformations?"
  type: short-answer
  answer: "Matrix multiplication is defined to encode the composition of linear transformations. The (i, j) entry of [S][T] must capture what happens to the j-th basis vector when first sent by T and then by S. T maps eⱼ to the j-th column of [T]. Then S maps that vector to [S] times that column — which is exactly the dot product of each row of [S] with the j-th column of [T]. So the row-times-column rule is not an arbitrary algorithm; it is the unique definition that makes [S][T] represent 'do T first, then S.' Matrix multiplication was invented to capture this composition structure — understanding this makes the definition feel inevitable rather than arbitrary."
  explanation: "The theorem that [S∘T] = [S][T] explains why matrix multiplication is defined the way it is. The formula isn't defined and then applied to transformations; it was derived from the requirement that matrix products represent composed transformations."
```

## Explainer

From your work on **matrix representations of linear transformations**, you know that every linear transformation T: ℝⁿ → ℝᵐ can be represented by a matrix [T], and applying T to a vector v is the same as computing [T]v. Now suppose you have two linear transformations: T: ℝⁿ → ℝᵐ and S: ℝᵐ → ℝᵖ. The **composition** S ∘ T maps ℝⁿ → ℝᵖ by first applying T, then applying S: (S ∘ T)(v) = S(T(v)). The central fact of this topic is that the matrix of S ∘ T is the product [S][T]. This is not a definition — it's a theorem, and it explains why matrix multiplication is defined the way it is.

To see why the formula is right, trace through what happens to a basis vector eⱼ. First, T sends eⱼ to the j-th column of [T]. Then S sends that vector to [S] times the j-th column of [T] — which is the j-th column of [S][T]. Since the matrix of S ∘ T is determined by where it sends basis vectors, and those columns match the columns of [S][T], the matrices are equal. Matrix multiplication is defined precisely so that this correspondence holds. This is why the product [S][T] is computed by taking dot products of rows of [S] with columns of [T] — it's encoding how the two successive transformations interact on each coordinate.

Order matters. S ∘ T means "do T first, then S" — but the matrix product is written [S][T], with [S] on the left. This reversal (the last transformation written first) is a persistent source of confusion. Think of it this way: if you read a composition from right to left, you get the temporal order of operations. The same applies to reading matrix products: [A][B][C]v means apply C first, then B, then A.

When a transformation T is **invertible** — meaning there exists T⁻¹ with T⁻¹ ∘ T = identity — the corresponding matrix [T] is invertible, and [T⁻¹] = [T]⁻¹. The collection of all invertible n×n matrices (equivalently, invertible linear transformations on ℝⁿ) forms a structure called the **general linear group** GL_n under matrix multiplication. "Group" here means: composition of two invertible maps is invertible, composition is associative, the identity map is an element, and every element has an inverse. This group structure is what makes linear algebra interact with symmetry and geometry — rotations, reflections, and shears all live in GL_n, and composing them corresponds to multiplying their matrices.
