---
id: linear-transformation-matrix-representation
title: Matrix Representation of Linear Transformations
domain: mathematics
course: linear-algebra
prerequisites:
- id: linear-transformations
  type: hard
- id: basis-and-dimension
  type: hard
builds-toward:
- change-of-basis
- eigenvalues-and-eigenvectors
tags:
- matrix-representation
- coordinates
- bases
stage: formal-systems
status: validated
---

# Matrix Representation of Linear Transformations

## Core Idea
Every linear transformation T: Rⁿ → Rᵐ is represented by an m×n matrix A, where T(x) = Ax. To find A, compute T(eᵢ) for each standard basis vector and place the results as columns. For non-standard bases, the matrix is [T]_B = [T(b₁) ... T(bₙ)]_C in coordinates relative to bases B and C.

## Questions

```yaml
- question: "A linear transformation T: R² → R² sends e₁ = (1, 0) to (3, −1) and e₂ = (0, 1) to (2, 5). What is the matrix A representing T in the standard basis?"
  type: multiple-choice
  options:
    - "[[3, 2], [−1, 5]] — first column is T(e₁), second column is T(e₂)"
    - "[[3, −1], [2, 5]] — first row is T(e₁), second row is T(e₂)"
    - "[[−1, 5], [3, 2]] — columns are ordered by the output components"
    - "[[3, −1, 2, 5]] — the transformation is recorded as a single row"
  answer: 0
  explanation: "The columns of the matrix are the images of the standard basis vectors: the first column is T(e₁) = (3, −1) and the second column is T(e₂) = (2, 5), giving [[3, 2], [−1, 5]]. Option B is the most common error — placing T(e₁) as a row rather than a column. The column convention follows directly from how matrix-vector multiplication works: Ax = x₁(first column) + x₂(second column), which equals x₁T(e₁) + x₂T(e₂) = T(x₁e₁ + x₂e₂) = T(x)."

- question: "A student claims: 'To determine the matrix of a linear transformation T: Rⁿ → Rᵐ, I need to know how T acts on every possible input vector.' What is the flaw in this reasoning?"
  type: multiple-choice
  options:
    - "Linearity guarantees that T's behavior on any basis determines T's behavior on every vector in the space"
    - "The student is correct — you must test infinitely many inputs to fully characterize a transformation"
    - "You only need to know T on two vectors regardless of n, since all spaces are at most 2-dimensional in practice"
    - "The matrix only needs to encode T's behavior on the zero vector, since all other outputs follow from linearity"
  answer: 0
  explanation: "This is the key insight of the topic. Every vector x can be written as a linear combination of basis vectors: x = x₁b₁ + ... + xₙbₙ. Linearity then gives T(x) = x₁T(b₁) + ... + xₙT(bₙ). So knowing T on n basis vectors is exactly enough information to determine T on all of Rⁿ — the matrix records precisely this information column by column. You don't need to test infinite inputs; the finite basis is sufficient, and this is what makes the matrix representation so powerful."

- question: "Changing the basis used to represent a linear transformation T changes the matrix that represents T, even though the underlying transformation itself is unchanged."
  type: true-false
  answer: true
  explanation: "The same linear transformation can be represented by different matrices depending on the choice of bases for the domain and codomain. The matrix [T]_B^C encodes the transformation relative to a specific pair of bases B and C. Changing B or C changes the coordinates used, which changes the entries of the matrix — but T itself (as a function mapping vectors to vectors) remains the same geometric object. This is why 'change of basis' is such a fundamental operation: it lets you choose a basis that makes the matrix as simple as possible (e.g., diagonal for an eigendecomposition)."

- question: "If you know a linear transformation T sends two specific vectors u and v to their images T(u) and T(v), you can generally reconstruct the full matrix of T."
  type: true-false
  answer: false
  explanation: "You can reconstruct T from two vectors only if those two vectors form a basis for the domain. If u and v are linearly dependent (one is a scalar multiple of the other), they span only a line, and T's behavior on the rest of the space is completely unconstrained by what you know. For example, knowing T(e₁) tells you nothing about T(e₂). The key condition is that the vectors you evaluate T on must span the domain — which means they must form a basis. Linearity then guarantees the rest."

- question: "Explain why knowing a linear transformation's effect on a basis is sufficient to determine its effect on every vector in the space."
  type: short-answer
  answer: "Every vector in Rⁿ can be written uniquely as a linear combination of any basis vectors: x = c₁b₁ + c₂b₂ + ... + cₙbₙ. Because T is linear, it preserves this combination: T(x) = c₁T(b₁) + c₂T(b₂) + ... + cₙT(bₙ). So once we know T(b₁), T(b₂), ..., T(bₙ), we can compute T(x) for any x by expressing x in terms of the basis and applying linearity. The matrix simply stores T(b₁), ..., T(bₙ) as its columns, making this computation automatic via matrix-vector multiplication."
  explanation: "This argument combines two prerequisites — the uniqueness of coordinate representations relative to a basis, and the linearity of T — to show why a finite amount of information (n basis images) determines the transformation on an infinite-dimensional input space. It is the conceptual core of why matrices and linear transformations are literally the same object."
```

## Explainer

The core insight here is beautiful: a linear transformation is completely determined by what it does to any basis. You already know from your study of bases that every vector in Rⁿ can be written uniquely as a linear combination of basis vectors. And you know that linear transformations preserve those combinations — T(αu + βv) = αT(u) + βT(v). Combine these two facts: once you know where T sends each basis vector, you know where T sends every vector. The matrix is just a systematic way of recording that information.

For the standard basis in Rⁿ, this is especially clean. The standard basis vectors are e₁ = (1,0,...,0), e₂ = (0,1,...,0), and so on. To build the matrix for T: Rⁿ → Rᵐ, compute T(e₁), T(e₂), ..., T(eₙ). Each result is a vector in Rᵐ. Arrange them as columns: the first column is T(e₁), the second is T(e₂), and so on. You have your m×n matrix A. To verify it works: any x ∈ Rⁿ can be written as x = x₁e₁ + ... + xₙeₙ, so T(x) = x₁T(e₁) + ... + xₙT(eₙ) = Ax, where Ax is the standard matrix-vector product.

For non-standard bases, the same logic applies but coordinates change. If T maps from a space with basis B to a space with basis C, you compute T applied to each vector in B, then express each result in terms of C. The resulting coordinate vectors become the columns of the **change-of-basis matrix** [T]_B^C. This is the direct application of your prerequisite on basis and dimension: the matrix representation depends entirely on which bases you choose for the domain and codomain.

The payoff is that every theorem about matrices becomes a theorem about linear transformations, and vice versa. Composition of transformations corresponds to matrix multiplication. The rank of the matrix equals the dimension of the image. The nullity equals the dimension of the kernel. The abstract world of transformations and the computational world of matrices are not just analogous — they are literally the same object written in two different notations.
