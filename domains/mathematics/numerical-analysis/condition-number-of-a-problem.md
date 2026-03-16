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
stage: advanced
status: draft
---

# Condition Number of a Problem

## Core Idea
The condition number of a problem quantifies how much the relative solution change is amplified by relative changes in the input data. A large condition number indicates an ill-conditioned problem where small input perturbations cause large solution changes. Condition numbers provide fundamental limits on achievable accuracy regardless of algorithm choice or precision used.

## Explainer

From your study of **numerical stability and conditioning**, you know that errors in computation come from two sources: the problem itself (how sensitive the answer is to input perturbations) and the algorithm (whether the method amplifies errors unnecessarily). The condition number formalizes the first source. For a problem f(x) — think of f as computing some output from some input — the **condition number** κ is the ratio of relative output change to relative input change in the worst case:

κ = (‖δf‖ / ‖f‖) / (‖δx‖ / ‖x‖)

Informally: if you perturb the input by 1% in relative terms, the output changes by at most κ% in relative terms. A condition number of 10 means the problem amplifies relative errors by a factor of 10 — annoying but manageable. A condition number of 10⁸ means a 1% input error can produce a 10⁸% output error — the answer is essentially meaningless. The condition number is a property of the **problem**, not of the algorithm used to solve it. This is the key conceptual distinction: a poorly conditioned problem cannot be rescued by a better algorithm. No matter how clever your code, if the problem amplifies errors by 10¹², you will not get 12 accurate decimal digits.

A classic example: computing f(x) = √x near x = 0. A small absolute change in x produces a large relative change in √x. Or consider the polynomial root-finding problem — the roots of a degree-n polynomial can be extraordinarily sensitive to tiny changes in coefficients. Wilkinson's polynomial, with roots 1, 2, ..., 20, has a condition number so large that perturbing one coefficient by 2⁻²³ causes roots to become complex. This is not a failing of the root-finding algorithm — it is a property of the problem.

Understanding condition numbers sets the bar for what accuracy is achievable and tells you when to seek a reformulation rather than a better solver. If you are working in double precision (about 16 significant digits) and your problem has condition number 10⁸, you can at best expect 16 − 8 = 8 correct digits in the result. If the condition number is 10¹⁶ or larger, you may get no correct digits at all. When you move to the **condition number of a matrix** in linear algebra, you will apply this same framework to the specific problem of solving Ax = b — where κ(A) = ‖A‖ · ‖A⁻¹‖ gives the amplification factor for that system's sensitivity to perturbations in b or A.
