---
id: jordan-normal-form-intro
title: Jordan Normal Form and Generalized Eigenvectors
domain: mathematics
course: linear-algebra
prerequisites:
- id: diagonalization-similar-matrices
  type: hard
builds-toward:
- matrix-exponential
tags:
- jordan-form
- generalized-eigenvectors
- canonical-form
stage: formal-systems
status: validated
---

# Jordan Normal Form and Generalized Eigenvectors

## Core Idea
Not all matrices are diagonalizable. Jordan normal form J is block-diagonal with Jordan blocks (eigenvalue λ on diagonal, 1s on superdiagonal). Every matrix A is similar to its Jordan form: A = PJP⁻¹. Generalized eigenvectors extend eigenvectors to fill out Jordan blocks. Jordan form reveals algebraic and geometric multiplicities and enables computing matrix functions.

## Questions

```yaml
- question: "A student computes that matrix A has eigenvalue λ = 5 with algebraic multiplicity 3. She concludes that A must have a single 3×3 Jordan block for λ = 5. What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Algebraic multiplicity cannot exceed 2 in a real matrix"
    - "The sizes of Jordan blocks depend on the geometric multiplicity (dimension of the eigenspace), not just the algebraic multiplicity. If the eigenspace is three-dimensional, A is diagonalizable and all three blocks are 1×1. A single 3×3 block only arises when the eigenspace is one-dimensional."
    - "Jordan blocks can only appear for complex eigenvalues, not real ones"
    - "Algebraic multiplicity 3 guarantees exactly three separate 1×1 Jordan blocks"
  answer: 1
  explanation: "Algebraic multiplicity tells you the total 'size budget' for Jordan blocks of eigenvalue λ — their sizes must sum to it. The geometric multiplicity tells you how many blocks there are. One 3×3 block (geometric multiplicity 1), three 1×1 blocks (geometric multiplicity 3), or a 2×2 and a 1×1 block (geometric multiplicity 2) are all consistent with algebraic multiplicity 3. The student has conflated the two multiplicities."

- question: "What distinguishes a generalized eigenvector vᵢ from a true eigenvector v₁ in a Jordan chain for eigenvalue λ?"
  type: multiple-choice
  options:
    - "A generalized eigenvector satisfies Avᵢ = λvᵢ, just like a true eigenvector"
    - "A generalized eigenvector satisfies (A − λI)vᵢ = vᵢ₋₁ — applying (A − λI) to it yields the previous vector in the chain rather than zero"
    - "A generalized eigenvector must have unit length"
    - "A generalized eigenvector spans the same subspace as the true eigenvector for λ"
  answer: 1
  explanation: "A true eigenvector satisfies (A − λI)v₁ = 0 — it is annihilated by (A − λI). A generalized eigenvector at level i satisfies (A − λI)vᵢ = vᵢ₋₁: applying the defect operator maps it to the previous vector in the chain, not to zero. This chain structure is precisely what Jordan blocks encode — the 1s on the superdiagonal represent these 'shift' relationships between consecutive chain vectors."

- question: "A matrix is diagonalizable if and mainly if most of its eigenvalues are distinct (no repeated eigenvalues)."
  type: true-false
  answer: false
  explanation: "Distinct eigenvalues are sufficient but not necessary for diagonalizability. A matrix with repeated eigenvalues can still be diagonalizable if the geometric multiplicity equals the algebraic multiplicity for every eigenvalue — that is, if there are enough linearly independent eigenvectors to form a full basis. For example, the identity matrix has only one eigenvalue (λ = 1 with algebraic multiplicity n) but is trivially diagonalizable. The key test is the multiplicity comparison, not whether eigenvalues are distinct."

- question: "The number of distinct Jordan blocks for an eigenvalue λ in the Jordan normal form equals the geometric multiplicity of λ."
  type: true-false
  answer: true
  explanation: "Each Jordan block begins with a true eigenvector — you need one eigenvector to start each chain. Since the eigenvectors for λ are exactly the nonzero vectors in ker(A − λI), and the number of linearly independent eigenvectors is the geometric multiplicity, that equals the number of Jordan blocks. Their sizes sum to the algebraic multiplicity. This relationship between the two multiplicities completely determines the Jordan block structure."

- question: "Why does a defective matrix (one that cannot be diagonalized) produce solutions to differential equations y' = Ay that include polynomial terms like te^(λt), rather than pure exponentials?"
  type: short-answer
  answer: "When A has a Jordan block of size k for eigenvalue λ, computing the matrix exponential e^(At) requires raising the Jordan block to a power. The 1s on the superdiagonal, combined with the binomial theorem, generate polynomial terms: a 2×2 block produces t·e^(λt), a 3×3 block produces t·e^(λt) and t²·e^(λt), and so on. The polynomial factors arise because there are not enough true eigenvectors — the generalized eigenvectors fill the solution space, but they interact with the defect structure of A to produce polynomial-exponential solutions rather than pure exponentials."
  explanation: "This connects Jordan form to differential equations and explains why defective systems matter in applications. The polynomial growth from Jordan blocks is not a curiosity — it appears in critical phenomena like resonance in mechanics and repeated-pole behavior in control systems. Recognizing the Jordan block as the algebraic source of polynomial-exponential solutions is the payoff of the entire theory."
```

## Explainer

From diagonalization, you know the ideal situation: a matrix A is diagonalizable exactly when it has enough eigenvectors to form a basis. When that happens, A = PDP⁻¹ where D is diagonal, and everything simplifies — powers of A become powers of D, and the geometry is transparent. But many important matrices fail this test. The matrix [[2,1],[0,2]] has eigenvalue λ=2 with algebraic multiplicity 2, but only one linearly independent eigenvector. There is no invertible P that diagonalizes it. Jordan normal form is the structure theorem that salvages the situation: instead of a diagonal, you get something that is *almost* diagonal.

A **Jordan block** J_k(λ) is a k×k matrix with λ on every diagonal entry and 1 on every superdiagonal entry, and zeros everywhere else. A 2×2 Jordan block for λ=2 is exactly [[2,1],[0,2]]. Every square matrix A over ℂ is similar to a block-diagonal matrix built from Jordan blocks — this is its **Jordan normal form**. The sizes of the blocks are determined by the matrix itself, not by choice. Crucially, the number of distinct Jordan blocks for a given eigenvalue λ equals the geometric multiplicity (the dimension of the eigenspace), while the sum of their sizes equals the algebraic multiplicity. Diagonalizable matrices simply happen to have all Jordan blocks of size 1.

To fill out a Jordan block of size k, you need a chain of k vectors: a true eigenvector v₁ (satisfying (A − λI)v₁ = 0) together with **generalized eigenvectors** v₂, v₃, …, vₖ satisfying (A − λI)vᵢ = vᵢ₋₁. These generalized eigenvectors live in the **generalized eigenspace** — the kernel of (A − λI)^k for large enough k. They are not eigenvectors in the classical sense (applying A to them does not simply scale them), but they capture the "near-diagonal" action that the Jordan block encodes.

Jordan form unlocks matrix functions. To compute e^(At) or A^n, you write A = PJP⁻¹ and work with e^(Jt) or J^n. A Jordan block raised to a power produces a triangular matrix with polynomial entries — the 1s on the superdiagonal generate polynomial growth via the binomial theorem. This is why, for example, defective systems of differential equations (those without enough eigenvectors) produce solutions involving both exponentials and polynomial terms like te^(λt). The Jordan block is precisely the algebraic structure responsible for that behavior.

The key diagnostic numbers are the **algebraic multiplicity** (how often λ appears as a root of the characteristic polynomial) and the **geometric multiplicity** (the dimension of the eigenspace ker(A − λI)). If geometric = algebraic for every eigenvalue, the matrix is diagonalizable and all Jordan blocks are 1×1. If geometric < algebraic for any eigenvalue, at least one block has size ≥ 2, and you must use generalized eigenvectors. Finding the Jordan form of a specific matrix comes down to computing these multiplicities and solving the chain equations — a procedure that is conceptually clean once you understand what the blocks represent.
