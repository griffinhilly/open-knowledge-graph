---
id: operator-norm
title: The Operator Norm
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: bounded-linear-operators
  type: hard
builds-toward:
- linear-functionals-dual-spaces
tags:
- functional-analysis
- operators
stage: expert
status: validated
---

# The Operator Norm

## Core Idea
For a bounded linear operator T: X → Y, the operator norm is ‖T‖ = sup{‖T(x)‖_Y : ‖x‖_X ≤ 1}. The space ℒ(X,Y) of bounded operators is itself a normed space (Banach if Y is Banach).

## Questions

```yaml
- question: "A linear operator T: ℝ² → ℝ² is represented by a matrix whose largest singular value is 5. With respect to the standard Euclidean norm, what is ‖T‖ and what does it mean geometrically?"
  type: multiple-choice
  options:
    - "25 — the operator norm squares the largest singular value to account for area distortion"
    - "5 — the operator norm equals the largest singular value, measuring the maximum stretching of any unit vector"
    - "√5 — singular values appear under a square root in the norm computation"
    - "The operator norm cannot be determined from singular values without knowing T's nullspace"
  answer: 1
  explanation: "For a matrix with standard Euclidean norms, ‖T‖ equals its largest singular value. Geometrically, T maps the unit sphere to an ellipsoid; the largest singular value is the length of the longest axis of that ellipsoid — the worst-case stretching factor. The operator norm answers 'by at most how much can T amplify a vector?' The answer is σ₁ = 5 directly, with no squaring or square-rooting. This worst-case amplification is exactly what the definition sup{‖T(x)‖ : ‖x‖ ≤ 1} computes."

- question: "Suppose ‖S‖ = 3 and ‖T‖ = 4. A student calculates ‖ST‖ = 12, claiming the composition stretches exactly as much as the two operators combined. What is the correct statement?"
  type: multiple-choice
  options:
    - "The student is correct: ‖ST‖ = ‖S‖‖T‖ = 12 always holds for composed operators"
    - "Submultiplicativity gives only an upper bound: ‖ST‖ ≤ 12, and the actual norm could be strictly less"
    - "Composition reverses the order, so the student should compute ‖TS‖ = 12 instead"
    - "Submultiplicativity only applies to self-adjoint operators, not arbitrary S and T"
  answer: 1
  explanation: "Submultiplicativity states ‖ST‖ ≤ ‖S‖‖T‖ — an inequality, not an equality. The composition ST may stretch less than 12 because S might contract in the direction that T stretched: for example, if T expands along the x-axis and S contracts along the x-axis, their composition could have a much smaller norm. Equality holds in special cases (e.g., both diagonal with aligned extremal directions) but not in general. The inequality is all that is guaranteed — and it is exactly what is needed for ℒ(X,X) to be a Banach algebra."

- question: "‖T‖ = 0 if and only if T is the zero operator."
  type: true-false
  answer: true
  explanation: "This is the definiteness axiom of a norm applied to ℒ(X,Y). If ‖T‖ = 0, then sup{‖T(x)‖_Y : ‖x‖_X ≤ 1} = 0, so ‖T(x)‖_Y = 0 for every x in the unit ball, hence for every x by linearity (scaling x to lie in the unit ball). Therefore T(x) = 0 for all x, meaning T is the zero operator. The converse is immediate. This verification — along with the triangle inequality and homogeneity — is what makes ‖·‖ a genuine norm on ℒ(X,Y)."

- question: "If Y is a Banach space, then ℒ(X,Y) is also a Banach space for any normed space X, because completeness of the codomain is sufficient for completeness of the operator space."
  type: true-false
  answer: true
  explanation: "This is the theorem: ℒ(X,Y) is Banach whenever Y is Banach, regardless of whether X is complete. The key is that Cauchy sequences of operators {Tₙ} in ℒ(X,Y) produce, for each fixed x, Cauchy sequences {Tₙ(x)} in Y. Since Y is complete, these converge to some T(x) ∈ Y. One then verifies that T is linear and bounded, and that Tₙ → T in operator norm. The completeness of X plays no role in this argument — what matters is that the values Tₙ(x) live in a complete space."

- question: "Why is the operator norm defined as a supremum over the unit ball, and what does this reveal about the relationship between an operator being bounded and having a finite operator norm?"
  type: short-answer
  answer: "The supremum over the unit ball efficiently captures worst-case stretching because linear operators scale predictably: ‖T(αx)‖ = |α|‖T(x)‖, so the 'worst direction' is the same at every scale. By normalizing to unit vectors, we extract a scale-free amplification factor. An operator is bounded precisely when this supremum is finite — i.e., when there exists a uniform constant C with ‖T(x)‖ ≤ C‖x‖ for all x. The operator norm is the tightest such C: the infimum of all valid constants, realized as the actual supremum. Boundedness and finite operator norm are equivalent characterizations of the same property."
  explanation: "The equivalence ‖T‖ = sup{‖T(x)‖/‖x‖ : x ≠ 0} makes the 'worst-case ratio' interpretation explicit. The operator norm is not just any bound — it is the sharp bound, the actual maximum amplification achieved (or approached) by T."
```

## Explainer

From bounded linear operators, you know that T: X → Y is bounded if there exists a constant C such that ‖T(x)‖_Y ≤ C‖x‖_X for every x ∈ X. Many constants C work — the **operator norm** ‖T‖ is the smallest one that does. Formally, ‖T‖ = sup{‖T(x)‖_Y : ‖x‖_X ≤ 1}, which is the supremum of ‖T(x)‖ over the unit ball. Equivalently, ‖T‖ = sup{‖T(x)‖ / ‖x‖ : x ≠ 0}, the worst-case stretching factor. The operator norm answers: "by at most how much can T amplify a vector?"

In finite dimensions — when X = Rⁿ and Y = Rᵐ with their standard norms — every linear map is a matrix multiplication and every matrix is bounded. The operator norm of a matrix A (with respect to Euclidean norms) equals its largest singular value, which you might have seen as the square root of the largest eigenvalue of AᵀA. The unit ball in Rⁿ is a round sphere; T maps it to an ellipsoid in Rᵐ; the operator norm is the length of the longest axis of that ellipsoid. This geometric picture carries over to infinite dimensions, though "ellipsoid" becomes an abstract image.

The deeper significance of the operator norm is that it makes ℒ(X, Y) — the set of all bounded linear operators from X to Y — into a **normed space**. The norm axioms all check out: ‖T‖ = 0 if and only if T is the zero operator, ‖αT‖ = |α|‖T‖, and the triangle inequality ‖S + T‖ ≤ ‖S‖ + ‖T‖ holds. This means you can add operators, scale them, and take limits within ℒ(X, Y) using the operator norm as the notion of convergence. When Y is a Banach space (complete with respect to its norm), ℒ(X, Y) is also Banach — Cauchy sequences of operators converge to operators.

The operator norm also satisfies the submultiplicativity property ‖ST‖ ≤ ‖S‖‖T‖ whenever the composition makes sense. This is the operator analog of the scalar inequality |ab| = |a||b|, but it is an *inequality* rather than equality because composing two operators may not stretch as much as each would alone. Submultiplicativity is what makes the operator norm a **Banach algebra norm** on ℒ(X, X), the square case. This structure underpins the theory of functional calculus and the spectral theory of operators you will encounter next — the norm controls how analytic functions of operators (like eᵀ or (T − λI)⁻¹) behave.
