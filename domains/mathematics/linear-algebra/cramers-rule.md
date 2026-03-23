---
id: cramers-rule
title: Cramer's Rule for Solving Systems
domain: mathematics
course: linear-algebra
prerequisites:
- id: determinant-properties
  type: hard
- id: systems-of-linear-equations
  type: hard
tags:
- systems
- cramers rule
- determinants
stage: formal-systems
status: validated
---

# Cramer's Rule for Solving Systems

## Core Idea
For a square system Ax = b with det(A) ≠ 0, Cramer's rule gives x_i = det(A_i) / det(A), where A_i is A with column i replaced by b. This provides an explicit formula for solutions but is computationally inefficient compared to Gaussian elimination.

## Questions

```yaml
- question: "A student wants to solve a 10×10 system of linear equations numerically and suggests using Cramer's rule because 'it gives an exact answer directly.' What is the key problem with this reasoning?"
  type: multiple-choice
  options:
    - "Cramer's rule only works for 2×2 and 3×3 systems"
    - "Cramer's rule requires the determinant of A to equal exactly 1"
    - "Cramer's rule requires computing 11 determinants of 10×10 matrices, making it far more expensive than Gaussian elimination, which would give the exact same answer far more efficiently"
    - "There is no problem — Cramer's rule is the standard method for any square system"
  answer: 2
  explanation: "Gaussian elimination solves an n×n system in O(n³) operations. Cramer's rule requires computing n+1 determinants, each costing O(n³), for a total of O(n⁴). For n=10, Cramer's rule does roughly 10× more work for the same result. Cramer's rule does give an exact answer — but so does Gaussian elimination, much faster. The 'exact' framing is a red herring; the real issue is computational cost."

- question: "In which situation is Cramer's rule most appropriately used?"
  type: multiple-choice
  options:
    - "Solving a large sparse system of equations numerically on a computer"
    - "Deriving a closed-form symbolic expression for how a solution variable depends on the parameters of a system"
    - "Checking whether a square system has a unique solution"
    - "Computing a numerical solution when Gaussian elimination fails to converge"
  answer: 1
  explanation: "Cramer's rule's value is theoretical: it gives explicit, closed-form expressions xᵢ = det(Aᵢ)/det(A). This is useful when you need to analyze how solutions vary with parameters, prove structural results, or compute matrix inverses symbolically. For numerical computation — especially large systems — Gaussian elimination is the right tool. Checking for a unique solution just requires checking det(A) ≠ 0, not Cramer's rule."

- question: "Cramer's rule and Gaussian elimination produce the same solution for any square system with a nonzero determinant; the only difference is computational cost."
  type: true-false
  answer: true
  explanation: "Both methods solve the same mathematical problem and yield the same exact solution. Cramer's rule is not more accurate or more 'exact' than Gaussian elimination — they are algebraically equivalent. The difference is purely in efficiency: Cramer's rule is O(n⁴), Gaussian elimination is O(n³)."

- question: "Cramer's rule can be applied to any system of linear equations, including underdetermined systems (more unknowns than equations) and overdetermined systems (more equations than unknowns)."
  type: true-false
  answer: false
  explanation: "Cramer's rule requires a square system (n equations, n unknowns) with det(A) ≠ 0, guaranteeing a unique solution. Underdetermined systems have infinitely many solutions; overdetermined systems are typically inconsistent or have no unique solution. In both cases, the coefficient matrix is not square and has no determinant in the relevant sense."

- question: "Why is Cramer's rule described as 'theoretically elegant but computationally expensive'? Explain both sides of this claim."
  type: short-answer
  answer: "It is theoretically elegant because it gives an explicit closed-form formula for each solution variable as a ratio of determinants — xᵢ = det(Aᵢ)/det(A) — making solutions analyzable symbolically without performing elimination. It is computationally expensive because solving an n-variable system requires computing n+1 determinants, each costing O(n³), for O(n⁴) total — far slower than Gaussian elimination's O(n³)."
  explanation: "The elegance of an explicit formula is exactly what makes Cramer's rule valuable in proofs and theoretical analysis, where you want to see how the solution depends on the parameters rather than just compute a number. The inverse of a matrix, for instance, can be derived symbolically using Cramer's rule applied to each column of the identity. But for numerical computation, especially as n grows, the O(n⁴) cost is prohibitive."
```

## Explainer

You already know two things that Cramer's rule combines: how to solve a system of linear equations Ax = b, and how to compute the determinant of a matrix. From systems of equations, you know that a square system has a unique solution exactly when det(A) ≠ 0. From determinant properties, you know that the determinant measures how a linear transformation scales volume. Cramer's rule connects these ideas by expressing each solution variable as a ratio of determinants — giving you an explicit formula without any elimination steps.

Here is the rule: to solve Ax = b for x₁, x₂, ..., xₙ, compute x_i = det(A_i) / det(A), where **A_i** is the matrix formed by taking A and replacing column i with the vector b. For a 2×2 system, this is easy to verify by hand. Take the system 2x + y = 5, x + 3y = 7. The coefficient matrix A has det(A) = 2·3 − 1·1 = 5. To find x₁, replace the first column with [5, 7] to get A₁; det(A₁) = 5·3 − 1·7 = 8, so x₁ = 8/5. To find x₂, replace the second column with [5, 7] to get A₂; det(A₂) = 2·7 − 5·1 = 9, so x₂ = 9/5. You can verify these values satisfy both equations.

Why does this work? Here is the geometric intuition. The vector b is a linear combination of the columns of A: b = x₁a₁ + x₂a₂ + ... + xₙaₙ, where aᵢ is column i of A. The matrix A_i replaces column i with b, which can be written as the original matrix A but with column i "contaminated" by the weighted sum. When you take the determinant of A_i, the multilinearity of the determinant isolates the xᵢ coefficient (all other terms vanish because they introduce repeated columns), leaving det(A_i) = xᵢ · det(A). Dividing by det(A) recovers xᵢ.

Cramer's rule is theoretically elegant but **computationally expensive**. Computing a single n×n determinant takes O(n³) work (or O(n!) via cofactor expansion). Cramer's rule requires n+1 determinants, so solving a full n-variable system costs O(n⁴) — far worse than Gaussian elimination's O(n³). For n = 100, that's 100 times more work. In practice, nobody uses Cramer's rule to actually solve large systems. Its value is theoretical: it gives explicit, closed-form expressions for solutions, which are useful when deriving formulas in proofs, studying how solutions depend on parameters, or computing the inverse of a matrix symbolically. You will encounter Cramer's rule again whenever exact symbolic solutions matter more than computational speed.
