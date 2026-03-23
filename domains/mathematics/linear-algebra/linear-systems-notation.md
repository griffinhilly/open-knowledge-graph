---
id: linear-systems-notation
title: 'Linear Systems: Notation and Solution Existence'
domain: mathematics
course: linear-algebra
prerequisites:
- id: systems-of-three-variables
  type: hard
- id: matrices-intro
  type: hard
builds-toward:
- gaussian-elimination-method
- rank-nullity-theorem
- linear-systems-consistency
tags:
- systems
- Ax=b
- notation
- existence
stage: formal-systems
status: validated
---

# Linear Systems: Notation and Solution Existence

## Core Idea
A system of m linear equations in n unknowns is written as Ax = b, where A is m×n, x is the unknown vector, and b is the right-hand side. Solutions exist if and only if b is in the column space of A. The solution set is either empty, a single point, or an affine subspace (infinite solutions). Augmented matrices [A | b] encode the system compactly.

## Questions

```yaml
- question: "A 3×2 matrix A has columns v₁ = [1, 0, 0] and v₂ = [0, 1, 0]. For which right-hand side b does the system Ax = b have a solution?"
  type: multiple-choice
  options:
    - "b = [3, 5, 0] — because b is a linear combination of A's columns"
    - "b = [3, 5, 7] — because b has three components matching A's three rows"
    - "b = [0, 0, 0] — because only the trivial solution is guaranteed"
    - "Any b — a 3×2 system always has at least one solution"
  answer: 0
  explanation: "A solution exists if and only if b lies in the column space of A — the set of all linear combinations of A's columns. Here col(A) = span{[1,0,0], [0,1,0]}, which is the xy-plane in ℝ³. b = [3, 5, 0] = 3v₁ + 5v₂ is in this span, so x = [3, 5] is the unique solution. b = [3, 5, 7] has a nonzero z-component that no combination of A's columns can produce, so there is no solution."

- question: "A homogeneous system Ax = 0 where A is 4×6 is solved. What can you conclude about the number of solutions?"
  type: multiple-choice
  options:
    - "There are infinitely many solutions, since the null space of a 4×6 matrix is nontrivial"
    - "There is exactly one solution: x = 0"
    - "There may be zero, one, or infinitely many solutions"
    - "There are exactly 2 solutions: x = 0 and one nonzero vector"
  answer: 0
  explanation: "For Ax = 0 (homogeneous system), x = 0 is always a solution — so there is never 'no solution.' A 4×6 matrix has 6 unknowns and at most 4 independent equations, so the null space has dimension at least 6 − 4 = 2. This means there are infinitely many solutions parameterized by a 2-dimensional subspace. The key fact: solution sets are always empty, a single point, or an infinite affine subspace — never exactly 2."

- question: "If the system Ax = b has more than one solution, it must have infinitely many solutions."
  type: true-false
  answer: true
  explanation: "Any two solutions x₁ and x₂ differ by a vector in the null space of A: x₁ − x₂ ∈ null(A). If the null space contains a nonzero vector v, then x₁ + tv is a solution for every scalar t, generating infinitely many. There is no way to have exactly 2 solutions: once you have 2, you have infinitely many by taking all scalar multiples of the difference in the null space direction."

- question: "The system Ax = b has no solution if and only if A has more rows than columns."
  type: true-false
  answer: false
  explanation: "The existence of solutions depends on whether b lies in the column space of A, not on whether the system is overdetermined. A tall (m > n) system may be consistent if b happens to lie in col(A). Conversely, even a square system (m = n) can have no solution if A is singular and b is not in the column space. Shape alone does not determine consistency."

- question: "Explain what it means geometrically for the system Ax = b to have no solution, exactly one solution, or infinitely many. What linear-algebraic condition determines which case applies?"
  type: short-answer
  answer: "A solution exists if and only if b is in the column space of A (the span of A's columns). If b is not in col(A), no solution exists. If b is in col(A), the number of solutions depends on the null space of A: if null(A) = {0}, the solution is unique; if null(A) contains nonzero vectors, there are infinitely many solutions parameterized by the null space."
  explanation: "The product Ax is a linear combination of A's columns using entries of x as weights. So 'does Ax = b have a solution?' is exactly 'can b be written as a weighted sum of A's columns?' Once we know a solution x₀ exists, any other solution must differ from x₀ by something in the null space. If null(A) = {0}, x₀ is the only solution. If null(A) is nontrivial, every x₀ + v (for v in null(A)) is also a solution, giving infinitely many. These are the only three possibilities for any linear system."
```

## Explainer

You already know how to solve a system of three equations in three unknowns by hand — substitution, elimination, back-substitution. You also know what a matrix is. The notation Ax = b packages everything you already know into a single symbolic object, and that packaging has enormous power.

In the system Ax = b, **A** is the **coefficient matrix** (m rows for equations, n columns for unknowns), **x** is the **unknown vector** (the column of variables you are solving for), and **b** is the **right-hand side vector** (the constants). The product Ax is a weighted sum of A's columns — specifically, the ith entry of Ax is the dot product of the ith row of A with x. Writing a system this way makes it easy to discuss systems of any size, not just 2×2 or 3×3.

The **augmented matrix** [A | b] is a further shorthand: you stack the coefficient matrix and the right-hand side together, separated by a vertical bar. This is the object you actually row-reduce. Writing [A | b] captures the entire system without writing out variables, making manipulations purely mechanical — you work with numbers and rows, not algebraic expressions.

The deepest idea in this topic is the **column space interpretation**. The product Ax is a linear combination of A's columns, using the entries of x as coefficients. So the question "does the system Ax = b have a solution?" becomes: "can b be written as a linear combination of A's columns?" If b lies in the column space of A, a solution exists. If not, there is no solution. Once a solution exists, there are exactly two cases: the solution is unique (if the null space of A contains only the zero vector) or there are infinitely many solutions (parameterized by the null space). These three outcomes — no solution, one solution, infinitely many — are the only possibilities for any linear system.
