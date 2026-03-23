---
id: condition-number-of-a-problem
title: Condition Number of a Problem
domain: mathematics
course: numerical-analysis
prerequisites:
- id: numerical-stability-and-conditioning
  type: hard
builds-toward:
- condition-number-of-a-matrix
tags:
- condition-number
- ill-conditioning
- sensitivity
stage: formal-systems
status: validated
---

# Condition Number of a Problem

## Core Idea
The condition number of a problem quantifies how much the relative solution change is amplified by relative changes in the input data. A large condition number indicates an ill-conditioned problem where small input perturbations cause large solution changes. Condition numbers provide fundamental limits on achievable accuracy regardless of algorithm choice or precision used.

## Questions

```yaml
- question: "You are solving a problem in double-precision arithmetic (about 16 significant digits). Your analysis shows the problem has condition number κ ≈ 10⁸. What is the best accuracy you can realistically expect in the result?"
  type: multiple-choice
  options:
    - "16 significant digits — precision depends on the algorithm, not the problem"
    - "Approximately 8 correct digits — the condition number consumes roughly 8 digits of precision"
    - "0 correct digits — any condition number above 1 makes the result meaningless"
    - "It depends on which algorithm is used; a well-chosen method can recover all 16 digits"
  answer: 1
  explanation: "With double precision providing ~16 digits and condition number κ ≈ 10⁸, you lose about log₁₀(10⁸) = 8 digits to amplification of input errors, leaving roughly 8 correct digits. Options A and D are the key misconception: the condition number is a property of the *problem*, not the algorithm. No algorithm — however clever — can extract accuracy that the problem's conditioning has already destroyed. Option C is too pessimistic; ill-conditioning degrades accuracy by κ's order of magnitude, it doesn't automatically nullify all digits."

- question: "Wilkinson's polynomial (with roots 1, 2, ..., 20) has a famously large condition number. A tiny perturbation to one coefficient causes several roots to become complex. The best explanation is:"
  type: multiple-choice
  options:
    - "The root-finding algorithm made a numerical error during computation"
    - "The polynomial's root-finding problem is intrinsically ill-conditioned — small changes to the input (coefficients) cause enormous changes to the output (roots)"
    - "The perturbation algebraically transformed the polynomial into one with complex roots"
    - "Floating-point arithmetic cannot handle polynomials of degree 20"
  answer: 1
  explanation: "Wilkinson's example is a canonical illustration that the problem itself — finding roots of a degree-20 polynomial from its coefficients — is catastrophically ill-conditioned. A perturbation of 2⁻²³ to one coefficient produces huge root displacements, including complex roots. This has nothing to do with the algorithm: the same disaster occurs with any root-finder because the condition number sets a ceiling on achievable accuracy regardless of the method chosen."

- question: "Switching to a numerically stable algorithm (e.g., replacing Gaussian elimination without pivoting with partial-pivoting LU decomposition) reduces the condition number of the linear system Ax = b."
  type: true-false
  answer: false
  explanation: "The condition number κ(A) = ‖A‖ · ‖A⁻¹‖ is a property of the matrix A — of the *problem* — not of the algorithm. A stable algorithm avoids *unnecessary* amplification of rounding errors (good numerical stability), but it cannot improve the problem's intrinsic sensitivity to perturbations in b or A. An ill-conditioned system (large κ) will give inaccurate results regardless of which stable algorithm solves it, because the problem itself amplifies input errors."

- question: "A well-conditioned problem (κ ≈ 1) means that small relative changes in the input produce small relative changes in the output."
  type: true-false
  answer: true
  explanation: "This is precisely what the condition number measures: the worst-case ratio of relative output change to relative input change. κ ≈ 1 means inputs and outputs are perturbed by roughly the same relative amount — the problem neither amplifies nor suppresses errors. This is the ideal case, where the intrinsic difficulty of the problem does not constrain the achievable accuracy beyond what the arithmetic precision already provides."

- question: "A problem has condition number 10¹⁶ and you are working in double precision. Explain what this implies for the achievable accuracy of any solution, regardless of algorithm."
  type: short-answer
  answer: "With double precision providing about 16 significant digits and a condition number of 10¹⁶, the condition number alone consumes all 16 available digits of precision. The achievable accuracy is approximately 16 − 16 = 0 correct digits — the result may have no significant figures at all. No algorithm can fix this because the problem's own sensitivity to input errors, not the algorithm's behavior, is the binding constraint."
  explanation: "This illustrates the fundamental limit imposed by conditioning: you cannot compute more accurate answers than the problem itself allows. The condition number sets a ceiling that no algorithm can break through. The only remedy is to reformulate the problem — change the representation, use a different parameterization, or add additional constraints — so that the new formulation has a smaller condition number."
```

## Explainer

From your study of **numerical stability and conditioning**, you know that errors in computation come from two sources: the problem itself (how sensitive the answer is to input perturbations) and the algorithm (whether the method amplifies errors unnecessarily). The condition number formalizes the first source. For a problem f(x) — think of f as computing some output from some input — the **condition number** κ is the ratio of relative output change to relative input change in the worst case:

κ = (‖δf‖ / ‖f‖) / (‖δx‖ / ‖x‖)

Informally: if you perturb the input by 1% in relative terms, the output changes by at most κ% in relative terms. A condition number of 10 means the problem amplifies relative errors by a factor of 10 — annoying but manageable. A condition number of 10⁸ means a 1% input error can produce a 10⁸% output error — the answer is essentially meaningless. The condition number is a property of the **problem**, not of the algorithm used to solve it. This is the key conceptual distinction: a poorly conditioned problem cannot be rescued by a better algorithm. No matter how clever your code, if the problem amplifies errors by 10¹², you will not get 12 accurate decimal digits.

A classic example: computing f(x) = √x near x = 0. A small absolute change in x produces a large relative change in √x. Or consider the polynomial root-finding problem — the roots of a degree-n polynomial can be extraordinarily sensitive to tiny changes in coefficients. Wilkinson's polynomial, with roots 1, 2, ..., 20, has a condition number so large that perturbing one coefficient by 2⁻²³ causes roots to become complex. This is not a failing of the root-finding algorithm — it is a property of the problem.

Understanding condition numbers sets the bar for what accuracy is achievable and tells you when to seek a reformulation rather than a better solver. If you are working in double precision (about 16 significant digits) and your problem has condition number 10⁸, you can at best expect 16 − 8 = 8 correct digits in the result. If the condition number is 10¹⁶ or larger, you may get no correct digits at all. When you move to the **condition number of a matrix** in linear algebra, you will apply this same framework to the specific problem of solving Ax = b — where κ(A) = ‖A‖ · ‖A⁻¹‖ gives the amplification factor for that system's sensitivity to perturbations in b or A.
