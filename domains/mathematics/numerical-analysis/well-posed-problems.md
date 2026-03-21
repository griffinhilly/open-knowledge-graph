---
id: well-posed-problems
title: Well-Posed Problems
domain: mathematics
course: numerical-analysis
prerequisites:
- id: condition-number
  type: hard
tags:
- well-posed
- hadamard
- existence-uniqueness
stage: formal-systems
status: draft
---

# Well-Posed Problems

## Core Idea
A problem is well-posed (Hadamard) if (1) a solution exists, (2) it is unique, and (3) it depends continuously on input data. Ill-posed problems violate one or more conditions and are numerically unstable. Understanding well-posedness guides method selection; ill-posed problems may require regularization to be numerically tractable.

## Questions

```yaml
- question: "Numerical differentiation of a noisy function produces wildly inaccurate results even when the input noise is tiny. Which Hadamard condition does this violate, and why?"
  type: multiple-choice
  options:
    - "Existence — the derivative may not exist for noisy functions"
    - "Uniqueness — there are infinitely many functions that match the noisy input"
    - "Continuous dependence — small perturbations in input produce unbounded changes in output"
    - "None — numerical differentiation is well-posed; the issue is floating-point precision"
  answer: 2
  explanation: "The derivative problem violates continuous dependence. Adding ε·sin(ωx) to f changes f by ε in sup-norm but changes f' by εω, which is unbounded as ω grows. This is not a floating-point artifact — it is a structural property of the differentiation operator. The problem is ill-posed regardless of numerical precision: the map from f to f' fails to be continuous in the relevant norms. Recognizing this explains why no choice of step size fully solves the problem."

- question: "A linear system Ax = b is presented where b lies outside the column space of A. Which Hadamard condition does this violate?"
  type: multiple-choice
  options:
    - "Uniqueness — infinitely many solutions exist"
    - "Continuous dependence — the solution is highly sensitive to perturbations in b"
    - "Existence — no exact solution exists"
    - "None — this is a well-posed problem solvable by least squares"
  answer: 2
  explanation: "If b is outside the column space of A, there is no vector x satisfying Ax = b exactly — the existence condition fails. The system is ill-posed in the strictest sense. Least squares finds a best approximation, but that is a different (and modified) problem, not a solution to the original one. Recognizing this as an existence failure rather than a precision or algorithm problem is the diagnostic value of well-posedness analysis."

- question: "A problem can satisfy both the existence and uniqueness conditions yet still be ill-posed if small changes in the input data produce large changes in the solution."
  type: true-false
  answer: true
  explanation: "This is exactly the continuous dependence condition — the third and often most practically critical of Hadamard's three requirements. A system like Ax = b might have a unique solution for every b, yet if A is nearly singular, tiny perturbations in b cause enormous swings in x. Existence and uniqueness are 'theoretical' conditions; continuous dependence is the 'numerical' condition. All three must hold for a problem to be well-posed."

- question: "An ill-posed problem cannot be solved numerically and should simply be abandoned in favor of a different problem formulation."
  type: true-false
  answer: false
  explanation: "Ill-posedness is a diagnosis, not a verdict. Once a problem is identified as ill-posed, regularization techniques — Tikhonov regularization, truncated SVD, smoothness priors — can restore continuous dependence by slightly modifying the problem (adding a constraint or penalty term). The modified problem is well-posed and numerically tractable, at the cost of a slight bias in the solution. Knowing the problem is ill-posed is the first step; regularization is the engineering response."

- question: "Explain why understanding well-posedness provides more useful diagnostic information than knowing the condition number alone."
  type: short-answer
  answer: "The condition number measures sensitivity — how much the solution amplifies perturbations in the input — but it presupposes that a unique solution exists and that continuous dependence holds in some form. Well-posedness analysis comes first: it identifies which of the three conditions (existence, uniqueness, continuous dependence) is violated and why. A large condition number diagnoses degree of ill-conditioning within an otherwise well-posed framework; an ill-posed problem may not even have a condition number that is meaningful. More importantly, knowing that continuous dependence is violated tells you *why* the problem is hard structurally and points directly to the cure: regularization, not algorithmic refinement."
  explanation: "This distinction matters practically: if you don't know your problem is ill-posed, you might spend weeks optimizing your algorithm when the issue is in the problem formulation itself. Numerical differentiation is the canonical example — no amount of algorithmic improvement fixes its instability, because the instability is intrinsic to the operator. Well-posedness analysis tells you to either change the problem (regularize) or accept approximate solutions."
```

## Explainer

Your study of the **condition number** gave you a way to measure how sensitive a problem's output is to small perturbations in its input — a large condition number flags a problem where tiny errors get amplified. Well-posedness is the conceptual layer beneath that: before asking *how much* a solution changes, you need to ask whether the solution framework is sound at all. Hadamard's three conditions define what it means for a mathematical problem to be "solvable in a meaningful sense."

The three conditions address three distinct failure modes. **Existence**: a solution to the problem must actually exist. If you pose a linear system Ax = b but b lies outside the column space of A, there is no exact solution — numerical methods will chase a mirage. **Uniqueness**: the solution must be the only one. A linear system with infinitely many solutions (underdetermined or rank-deficient) has no well-defined answer; any numerical method will find a different solution depending on its starting point or floating-point path. **Continuous dependence**: small changes in the problem data must produce only small changes in the solution. This is the condition that connects directly to what you know about condition numbers — if a problem lacks continuous dependence, it is inherently numerically unstable regardless of the method used.

The classic ill-posed example is **numerical differentiation**. The mathematical problem — find f'(x) given f — is perfectly well-defined for smooth functions, but as a numerical problem it violates continuous dependence. Adding a small high-frequency oscillation ε·sin(ωx) to f changes the function by ε in L∞ norm, but changes its derivative by εω, which can be enormous. No matter how carefully you implement a finite difference formula, the derivative amplifies measurement noise catastrophically. The problem is ill-posed in the sense that the map from f to f' is not continuously dependent on the data.

Understanding well-posedness tells you *why* certain numerical problems are hard, not just *that* they are hard. When a problem is ill-posed, the cure is usually **regularization**: modifying the problem by adding a constraint or penalty that restores continuous dependence, at the cost of slightly biasing the solution. Examples include Tikhonov regularization for ill-conditioned linear systems, truncated SVD for rank-deficient matrices, and smoothness priors in inverse problems. Recognizing that your problem is ill-posed is the first step; regularization is the engineering response. Without this conceptual diagnosis, you might keep refining your algorithm and never understand why convergence fails.
