---
id: condition-number-of-matrix
title: Condition Number of a Matrix
domain: mathematics
course: numerical-analysis
prerequisites:
- id: condition-number
  type: hard
- id: matrix-operations
  type: hard
builds-toward:
- jacobi-iterative-method
tags:
- condition-number
- matrix
- ill-conditioning
stage: formal-systems
status: draft
---

# Condition Number of a Matrix

## Core Idea
The condition number of a matrix A is κ(A) = ‖A‖ ‖A⁻¹‖, measuring how much small perturbations in A or b affect the solution x to Ax = b. If κ(A) is large, the system is ill-conditioned: small changes in inputs produce large changes in outputs. The condition number depends on the chosen norm; large κ(A) indicates potential numerical difficulties regardless of algorithm.

## Questions

```yaml
- question: "You are solving Ax = b where κ(A) ≈ 10¹⁰ using double-precision arithmetic (about 15–16 significant digits). You switch from Gaussian elimination to an advanced iterative solver. What should you expect?"
  type: multiple-choice
  options:
    - "The iterative solver will overcome the ill-conditioning and achieve full 15-digit accuracy"
    - "The result will still have only about 5–6 reliable digits, regardless of the algorithm — the condition number characterizes the problem, not the method"
    - "The condition number decreases as the iterative method converges"
    - "The advanced solver reduces the effective condition number by preconditioning the matrix automatically"
  answer: 1
  explanation: "The condition number κ(A) characterizes the problem's inherent sensitivity — it tells you how much relative input error is amplified into output error. If κ(A) ≈ 10^k, you lose roughly k digits of precision regardless of the algorithm. With κ ≈ 10¹⁰ and 15 available digits, about 10 are consumed by ill-conditioning, leaving only 5–6 reliable digits. No algorithm can recover lost precision; a better algorithm achieves the best possible result given the problem's condition, but cannot surpass what the problem allows. (Note: preconditioning can change the effective condition number, but that's a different operation — it reformulates the problem, not just the algorithm.)"

- question: "Geometrically, what does a large condition number κ₂(A) = σ_max/σ_min indicate about the transformation A performs on vectors?"
  type: multiple-choice
  options:
    - "A scales every vector by a uniformly large factor, making all outputs large"
    - "A maps the unit sphere to a highly elongated ellipsoid — it stretches some directions enormously while nearly collapsing others to near-zero length"
    - "A is nearly orthogonal and preserves the length of most vectors"
    - "A has many eigenvalues clustered near a single value"
  answer: 1
  explanation: "The singular values σ_max and σ_min are the lengths of the longest and shortest semi-axes of the ellipsoid that A maps the unit sphere to. A large ratio σ_max/σ_min means the ellipsoid is very elongated — nearly flat in some directions. The inverse A⁻¹ must reverse this, enormously amplifying the nearly-collapsed directions. When the input b (or floating-point rounding errors in b) has any component in those nearly-collapsed directions, that component blows up in the solution x = A⁻¹b. This is the geometric mechanism of ill-conditioning."

- question: "A numerically stable algorithm can accurately solve a linear system even when the coefficient matrix has a very large condition number."
  type: true-false
  answer: false
  explanation: "Numerical stability describes an algorithm's ability to avoid introducing its own errors during computation. Even a perfectly stable algorithm cannot recover information lost due to ill-conditioning. The condition number κ(A) measures the problem's intrinsic sensitivity to perturbations — including the rounding errors inherent in floating-point arithmetic. If κ(A) ≈ 10^k, approximately k digits of precision are unavoidably lost, regardless of the algorithm. Stability prevents making things worse; it cannot make them better than the problem allows."

- question: "If κ(A) ≈ 10⁵ and you are computing with double-precision arithmetic (approximately 15–16 significant decimal digits), you can expect about 10–11 reliable digits in the solution to Ax = b."
  type: true-false
  answer: true
  explanation: "The rule of thumb is: if κ(A) ≈ 10^k, solving Ax = b costs roughly k decimal digits of accuracy. Starting with 15–16 digits of double precision and losing 5 digits to a condition number of 10⁵ leaves approximately 10–11 reliable digits. This is a practical upper bound — the actual result may be slightly better or worse depending on the specific structure of b and x, but the order of magnitude is reliable."

- question: "Explain why a nearly singular matrix has a large condition number, and what this implies about solving Ax = b numerically."
  type: short-answer
  answer: "A nearly singular matrix A has a determinant close to zero, meaning A⁻¹ exists but has very large entries (on the order of 1/det(A)). The condition number κ(A) = ‖A‖ · ‖A⁻¹‖ is therefore large. Geometrically, A nearly collapses some directions of the input space — its smallest singular value σ_min is very small. A⁻¹ must reverse this near-collapse, enormously amplifying any errors in those directions. For solving Ax = b numerically, this means small changes in b (or small rounding errors in the floating-point representation of b) are amplified into large changes in the computed x, destroying accuracy even with a perfect algorithm."
  explanation: "Near-singularity and ill-conditioning are two descriptions of the same geometric reality. The key insight is that the condition number characterizes the problem itself, not the solver. Changing the algorithm cannot improve beyond what κ(A) allows. This is why condition number analysis is the first step in assessing whether a linear system is reliably solvable with a given precision."
```

## Explainer

You know from your prerequisite work that the general condition number of a problem measures relative output sensitivity to relative input perturbation. The condition number of a matrix specializes this idea to linear systems Ax = b, where the "problem" is "given b, find x = A⁻¹b." You also know matrix operations well enough to manipulate A and its inverse. Now the question becomes: how does a small change in the right-hand side b affect the solution x?

If b is perturbed to b + δb, the solution changes to x + δx = A⁻¹(b + δb), giving δx = A⁻¹δb. Taking norms: ‖δx‖ ≤ ‖A⁻¹‖ ‖δb‖. To convert this to a relative error bound, divide both sides and use ‖b‖ ≤ ‖A‖ ‖x‖ to get ‖δx‖/‖x‖ ≤ ‖A‖ ‖A⁻¹‖ · ‖δb‖/‖b‖. The factor ‖A‖ ‖A⁻¹‖ = κ(A) is the **condition number** — it amplifies relative input error into relative output error.

For the 2-norm (Euclidean), κ₂(A) = σ_max/σ_min, the ratio of the largest to smallest singular value. Geometrically, A transforms the unit sphere into an ellipsoid; σ_max and σ_min are the longest and shortest semi-axes. A large condition number means the ellipsoid is very elongated — A stretches some directions enormously while nearly collapsing others. The inverse A⁻¹ must reverse this, enormously amplifying the nearly-collapsed directions. When b has any component in those directions (and floating-point b always will, due to rounding), that component blows up in the solution.

A nearly singular matrix illustrates this concretely. Consider A = [[1, 1], [1, 1+ε]] for small ε. The determinant is ε, so A⁻¹ has entries of order 1/ε, giving κ(A) ≈ 4/ε². For ε = 0.001, κ ≈ 4×10⁶. A useful rule of thumb: if κ(A) ≈ 10^k, solving Ax = b costs you roughly k decimal digits of accuracy. Starting with double-precision arithmetic (about 15–16 digits), a condition number of 10¹⁰ leaves only 5–6 reliable digits in the solution — even if your algorithm is perfect. The condition number characterizes what is achievable, not how well you solved it.
