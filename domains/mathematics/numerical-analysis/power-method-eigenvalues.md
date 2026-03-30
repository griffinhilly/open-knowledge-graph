---
id: power-method-eigenvalues
title: Power Method for Eigenvalues
domain: mathematics
course: numerical-analysis
prerequisites:
- id: eigenvalues-and-eigenvectors
  type: hard
builds-toward:
- qr-algorithm
tags:
- power-method
- eigenvalues
- iteration
stage: advanced
status: validated
---

# Power Method for Eigenvalues

## Core Idea
The power method finds the largest (in absolute value) eigenvalue and its eigenvector by repeatedly multiplying a random vector by the matrix: v^{(k+1)} = Av^{(k)} / ‖Av^{(k)}‖. Convergence is geometric with rate determined by the ratio of the two largest eigenvalues. Simple to implement, the power method is practical for large sparse matrices but slow when eigenvalues are close.

## Questions

```yaml
- question: "A matrix has eigenvalues λ₁ = 10 and λ₂ = 9. After 50 iterations of the power method, the iterate has not converged to the dominant eigenvector. Which explanation is most accurate?"
  type: multiple-choice
  options:
    - "The power method only works for symmetric matrices, so this matrix is likely non-symmetric"
    - "Convergence is governed by |λ₂/λ₁| = 0.9; with the two largest eigenvalues so close, convergence is very slow and 50 iterations may not be enough"
    - "The iteration converged to the wrong eigenvalue because the starting vector must be chosen carefully"
    - "50 iterations is always sufficient for any matrix of reasonable size"
  answer: 1
  explanation: "The convergence rate of the power method is |λ₂/λ₁|. When this ratio is close to 1 (here 0.9), the component corresponding to v₂ decays only 10% per iteration, so convergence is very slow. The power method works for non-symmetric matrices and does not require special initialization (a random start is fine); 50 iterations is nowhere near a universal guarantee."

- question: "What is the mathematical role of the normalization step (dividing by the vector's norm) in each power method iteration?"
  type: multiple-choice
  options:
    - "It ensures the iteration finds the smallest eigenvalue by projecting out the dominant component"
    - "It prevents the vector from growing without bound or shrinking to zero, preserving the direction signal while keeping numerical values manageable"
    - "It accelerates convergence by directly projecting the vector onto the dominant eigenvector subspace"
    - "It eliminates components corresponding to all non-dominant eigenvectors in a single step"
  answer: 1
  explanation: "Without normalization, the vector magnitude grows as |λ₁|ᵏ (or shrinks if |λ₁| < 1), causing numerical overflow or underflow. Normalization keeps the magnitude at 1 so the direction converges visibly without arithmetic problems. It does not project out non-dominant components — those decay gradually through many iterations."

- question: "The power method converges to the eigenvector corresponding to the eigenvalue with the largest absolute value, not necessarily the algebraically largest eigenvalue."
  type: true-false
  answer: true
  explanation: "Absolute value is what matters. If a matrix has eigenvalues λ₁ = −10 and λ₂ = 5, the power method converges to the eigenvector for λ = −10 because |−10| = 10 > |5| = 5. Students often conflate 'dominant' with 'most positive,' but the method amplifies the direction with the fastest geometric growth, which is determined by magnitude."

- question: "If the initial vector v⁰ is chosen to be exactly orthogonal to the dominant eigenvector v₁ (so that the coefficient c₁ = 0 in the eigenvector expansion), the power method will still eventually converge to v₁ due to the normalization step."
  type: true-false
  answer: false
  explanation: "In exact arithmetic, if c₁ = 0, then Aᵏv⁰ has no v₁ component at all, and the iteration converges to whichever eigenvector is dominant in the remaining components. In floating-point arithmetic, rounding errors typically introduce a tiny v₁ component that eventually dominates, but this is a practical accident, not a guarantee. Correct initialization should not rely on this."

- question: "Why does the power method converge more slowly when the two largest eigenvalues are close in magnitude? Explain using the structure of the iteration."
  type: short-answer
  answer: "Convergence rate is |λ₂/λ₁|. When this ratio is close to 1, the v₂ component of the iterate decays only slightly per step, so many iterations are needed to wash it out. Conversely, when eigenvalues are well-separated (ratio close to 0), the v₂ component decays rapidly and the iterate quickly aligns with v₁."
  explanation: "Decompose v⁰ in the eigenvector basis: after k multiplications, Aᵏv⁰ = λ₁ᵏ(c₁v₁ + c₂(λ₂/λ₁)ᵏv₂ + ...). The second term vanishes at rate |λ₂/λ₁|ᵏ. If λ₁ = 100 and λ₂ = 1, the ratio is 0.01 and convergence is extremely fast. If λ₁ = 10 and λ₂ = 9, the ratio is 0.9 and each step removes only 10% of the contamination from the v₂ direction."
```

## Explainer

You already know that eigenvalues and eigenvectors satisfy Av = λv: multiplying a matrix by its eigenvector just scales that vector by λ. The power method exploits this property directly. Start with any random vector v⁰, multiply repeatedly by A, and normalize after each step. After many iterations, the direction of v^(k) converges to the **dominant eigenvector** — the eigenvector corresponding to the largest absolute eigenvalue λ₁.

The reason this works becomes clear when you decompose the starting vector in the eigenvector basis. Write v⁰ = c₁v₁ + c₂v₂ + ... + cₙvₙ. After k applications of A: Aᵏv⁰ = c₁λ₁ᵏv₁ + c₂λ₂ᵏv₂ + ... = λ₁ᵏ(c₁v₁ + c₂(λ₂/λ₁)ᵏv₂ + ...). Since |λ₂/λ₁| < 1 (λ₁ is strictly dominant), every term except the first shrinks to zero. The iteration is dominated by the v₁ component, which is exactly the eigenvector you want. The normalization at each step prevents the vector from growing to infinity or shrinking to zero — it keeps the direction visible.

The **convergence rate** is |λ₂/λ₁|: the ratio of the second-largest to the largest eigenvalue. If this ratio is small (eigenvalues well-separated), convergence is fast. If it is close to 1 (eigenvalues nearly equal), convergence is very slow — the second component decays slowly and the iteration must work longer to wash it out. The **Rayleigh quotient** μ = (v^(k))ᵀ A v^(k) / (v^(k))ᵀ v^(k) gives an estimate of λ₁ at each step and converges quadratically once the eigenvector direction is approximately right.

For large sparse matrices from real applications — finite element models, network graphs, Google's PageRank — A might be millions by millions, but applying A to a vector is cheap (only the nonzero entries matter). This is where the power method shines: each iteration requires only a single matrix-vector multiply. The method can be extended via **deflation**: once λ₁ and v₁ are found, project out v₁ from the matrix and apply the method again to find the next eigenvalue. The QR algorithm — a much more sophisticated technique — can be understood in part as a way of applying power-method logic to all eigenvalues simultaneously and efficiently.
