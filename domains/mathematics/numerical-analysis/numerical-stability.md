---
id: numerical-stability
title: Numerical Stability and Conditioning
domain: mathematics
course: numerical-analysis
prerequisites:
- id: catastrophic-cancellation
  type: hard
builds-toward:
- condition-number
tags:
- stability
- conditioning
- error-analysis
stage: abstract-reasoning
status: draft
---

# Numerical Stability and Conditioning

## Core Idea
A numerical algorithm is stable if small perturbations in inputs produce only small changes in outputs. Stability depends on both the problem (conditioning) and the algorithm (implementation). A well-conditioned problem solved with a stable algorithm yields accurate results; poor conditioning or instability can make even theoretically simple problems numerically unreliable.

## Explainer

From your study of catastrophic cancellation, you saw a concrete failure mode: subtracting two nearly-equal floating-point numbers can wipe out all significant digits, turning a tiny relative error into a massive one. Numerical stability is the broader framework that explains when and why such failures occur, and how to reason about algorithm quality systematically.

The central distinction is between **conditioning** and **stability**. Conditioning is a property of the mathematical *problem* — how much does the true answer change when the inputs change slightly? Stability is a property of the *algorithm* — does the sequence of floating-point operations amplify errors, or keep them bounded? A well-conditioned problem has answers that are insensitive to small input perturbations. A stable algorithm is one that doesn't introduce unnecessary amplification beyond what the problem itself requires. These are independent: an unstable algorithm can ruin a well-conditioned problem, and a stable algorithm cannot rescue an ill-conditioned one.

Consider evaluating the polynomial p(x) = (x − 2)² near x = 2. Expanded as x² − 4x + 4, the three-term version subtracts large numbers that nearly cancel, risking catastrophic cancellation — unstable for this input. The factored form (x − 2)² avoids this cancellation entirely — mathematically identical, but numerically stable. This is a clean example where algorithm choice, not the problem, determines accuracy. Both formulas compute the same function; only their numerical behavior differs.

A useful benchmark concept is **backward stability**: an algorithm is backward stable if it computes the exact answer to a slightly perturbed problem. This framing separates algorithm error from problem sensitivity. If the backward error is tiny (the perturbed input is close to the real input) and the problem is well-conditioned (small input changes produce small output changes), then the computed answer is close to the true answer. Most reliable numerical algorithms — Gaussian elimination with pivoting, QR decomposition, stable ODE solvers — are designed with backward stability in mind. When you encounter numerical results you distrust, the first diagnostic question is always: is this problem inherently ill-conditioned, or is the algorithm introducing avoidable error?
