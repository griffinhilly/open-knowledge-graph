---
id: numerical-stability-and-conditioning
title: Numerical Stability and Conditioning
domain: mathematics
course: numerical-analysis
prerequisites:
- id: floating-point-representation
  type: soft
builds-toward:
- condition-number-of-a-problem
- condition-number-of-a-matrix
tags:
- stability
- conditioning
- well-posed-problems
stage: advanced
status: draft
---

# Numerical Stability and Conditioning

## Core Idea
An algorithm is numerically stable if small perturbations in input produce small perturbations in output. A problem is well-conditioned if small input changes lead to small output changes, and ill-conditioned if they lead to large output changes. Stability is a property of algorithms, while conditioning is a property of problems themselves.

## Explainer

From your work on floating-point representation, you know that every real number is rounded to the nearest representable value, introducing a small relative error no larger than **machine epsilon** ε_mach (roughly 10⁻¹⁶ for double precision). Every number you feed into a computation is therefore already slightly wrong. The question numerical analysis asks is: does your algorithm make things better or worse?

**Conditioning** is a property of the mathematical problem, independent of how you solve it. A well-conditioned problem is forgiving: small input errors produce small output errors. An ill-conditioned problem is treacherous: tiny input errors can produce enormous output errors, not because of any computational mistake, but because of the mathematics itself. The classic example is **subtractive cancellation**: computing f(x) = (1 + x) − 1 near x = 0. The mathematical answer is just x, but in floating point, 1+x rounds to 1 when x < ε_mach, and you get 0. The entire significant content of x is lost. This is not an algorithm failure — it is the problem of subtraction near zero being ill-conditioned.

**Stability** is a property of a specific algorithm, not the problem. Two algorithms can solve the same well-conditioned problem with very different accuracy. Consider computing √(x² + 1) − 1 near x = 0. The problem is well-conditioned (the true answer ≈ x²/2 varies smoothly). But the naive formula subtracts two nearly-equal numbers (√(x²+1) ≈ 1 and 1), causing catastrophic cancellation. The **numerically stable** reformulation x²/(√(x²+1) + 1) avoids any subtraction of nearly-equal quantities and gives full precision. Same problem, same mathematical answer, wildly different numerical behavior.

The gold standard is **backward stability**: an algorithm is backward stable if its computed output is the exact answer to a slightly perturbed input (with perturbation of order ε_mach). If the problem is also well-conditioned, backward stability guarantees an accurate answer. Together, conditioning and stability let you diagnose numerical failures cleanly: poor accuracy is either a poorly conditioned problem (unavoidable without reformulating the math), an unstable algorithm (fixable by choosing a better method), or both. Knowing which is which directs where to invest effort.
