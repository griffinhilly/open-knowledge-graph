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
stage: formal-systems
status: draft
---

# Numerical Stability and Conditioning

## Core Idea
A numerical algorithm is stable if small perturbations in inputs produce only small changes in outputs. Stability depends on both the problem (conditioning) and the algorithm (implementation). A well-conditioned problem solved with a stable algorithm yields accurate results; poor conditioning or instability can make even theoretically simple problems numerically unreliable.

## Questions

```yaml
- question: "A programmer evaluates p(x) = x² − 4x + 4 near x = 2 and gets a wildly inaccurate answer. They rewrite it as p(x) = (x − 2)² and the result is accurate. The underlying mathematical function is identical. What does this illustrate?"
  type: multiple-choice
  options:
    - "The problem was ill-conditioned — the answer is inherently sensitive to small input changes near x = 2"
    - "The algorithm choice determines numerical stability even for a well-conditioned problem"
    - "Floating-point arithmetic is always unreliable for polynomial evaluation"
    - "The rewritten form changes the mathematical function being computed"
  answer: 1
  explanation: "This is the central example of numerical stability: the same well-conditioned function can be computed accurately or inaccurately depending on algorithm choice. Near x = 2, p(x) = x² − 4x + 4 subtracts two nearly equal large numbers, causing catastrophic cancellation. The factored form (x − 2)² avoids this entirely. The problem is not ill-conditioned — small changes in x near 2 produce small changes in p(x). The instability is entirely an artifact of the expanded algorithm, not the problem itself."

- question: "An algorithm is called 'backward stable' if it:"
  type: multiple-choice
  options:
    - "Produces an output error smaller than machine epsilon"
    - "Computes the exact answer to a slightly perturbed version of the original input"
    - "Never amplifies rounding errors beyond the precision of the inputs"
    - "Always converges to the correct answer given enough iterations"
  answer: 1
  explanation: "Backward stability is a specific, technical concept: the algorithm computes the exact answer to a *slightly perturbed* problem. This separates algorithm error (backward error: how much did the input have to change?) from problem sensitivity (conditioning: how much does the output change for that input perturbation?). If the backward error is small and the problem is well-conditioned, the output is close to the true answer. Gaussian elimination with partial pivoting and QR decomposition are backward stable. The definition does not require output error smaller than machine epsilon, convergence, or bounded amplification in absolute terms."

- question: "A stable algorithm cannot save you from an ill-conditioned problem — if the problem amplifies small input errors into large output errors, no choice of algorithm can prevent inaccuracy."
  type: true-false
  answer: true
  explanation: "True. Conditioning is a property of the mathematical problem itself, independent of any algorithm. An ill-conditioned problem has a high condition number: small relative perturbations in input produce large relative perturbations in output. Even if an algorithm is backward stable (introducing only tiny backward error), the problem's own amplification factor magnifies that error into a large output error. Stability and conditioning are independent axes — both must be favorable for accurate results."

- question: "A numerically stable algorithm is one that produces the mathematically correct answer for every possible input."
  type: true-false
  answer: false
  explanation: "False. Stability does not mean correctness for all inputs — it means small perturbations in inputs produce proportionally small changes in outputs, and the algorithm does not amplify errors beyond what the problem requires. An algorithm can be stable yet produce large output errors when the *problem itself* is ill-conditioned (a large condition number). Stability is about controlling algorithmic error amplification relative to problem sensitivity, not about achieving exact answers."

- question: "Why is it useful to distinguish conditioning (a property of the problem) from stability (a property of the algorithm)? What does each concept tell you?"
  type: short-answer
  answer: "Conditioning tells you whether the problem is inherently sensitive to input perturbations — if the true answer changes a lot when inputs change slightly, the problem is ill-conditioned and no algorithm can produce reliable results. Stability tells you whether the algorithm avoids unnecessarily amplifying rounding errors introduced during computation. The distinction matters because it diagnoses the source of numerical failure: if you compute an inaccurate result, is it because the problem is fundamentally sensitive (ill-conditioned) or because the algorithm is introducing avoidable error (unstable)? Only the second cause can be fixed by redesigning the algorithm."
  explanation: "The practical payoff is diagnostic: when a numerical result seems wrong, the first question is 'is this ill-conditioned or is the algorithm bad?' For an ill-conditioned problem, the answer is inherently unreliable — you need more data, a reformulation, or to accept limited accuracy. For a stable problem with a bad algorithm, switching to a backward-stable method (pivoted Gaussian elimination, QR decomposition) can recover accuracy. Without the distinction, all numerical failures look the same and the fix is unclear."
```

## Explainer

From your study of catastrophic cancellation, you saw a concrete failure mode: subtracting two nearly-equal floating-point numbers can wipe out all significant digits, turning a tiny relative error into a massive one. Numerical stability is the broader framework that explains when and why such failures occur, and how to reason about algorithm quality systematically.

The central distinction is between **conditioning** and **stability**. Conditioning is a property of the mathematical *problem* — how much does the true answer change when the inputs change slightly? Stability is a property of the *algorithm* — does the sequence of floating-point operations amplify errors, or keep them bounded? A well-conditioned problem has answers that are insensitive to small input perturbations. A stable algorithm is one that doesn't introduce unnecessary amplification beyond what the problem itself requires. These are independent: an unstable algorithm can ruin a well-conditioned problem, and a stable algorithm cannot rescue an ill-conditioned one.

Consider evaluating the polynomial p(x) = (x − 2)² near x = 2. Expanded as x² − 4x + 4, the three-term version subtracts large numbers that nearly cancel, risking catastrophic cancellation — unstable for this input. The factored form (x − 2)² avoids this cancellation entirely — mathematically identical, but numerically stable. This is a clean example where algorithm choice, not the problem, determines accuracy. Both formulas compute the same function; only their numerical behavior differs.

A useful benchmark concept is **backward stability**: an algorithm is backward stable if it computes the exact answer to a slightly perturbed problem. This framing separates algorithm error from problem sensitivity. If the backward error is tiny (the perturbed input is close to the real input) and the problem is well-conditioned (small input changes produce small output changes), then the computed answer is close to the true answer. Most reliable numerical algorithms — Gaussian elimination with pivoting, QR decomposition, stable ODE solvers — are designed with backward stability in mind. When you encounter numerical results you distrust, the first diagnostic question is always: is this problem inherently ill-conditioned, or is the algorithm introducing avoidable error?
