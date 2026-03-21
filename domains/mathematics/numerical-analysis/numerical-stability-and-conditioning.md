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

## Questions

```yaml
- question: "Computing f(x) = √(x²+1) − 1 near x = 0 with the naive formula gives terrible accuracy, but the algebraically equivalent reformulation x²/(√(x²+1)+1) gives full precision. What does this demonstrate?"
  type: multiple-choice
  options:
    - "The mathematical problem f(x) near x = 0 is ill-conditioned, so no algorithm can give accurate results"
    - "The naive formula contains an algebraic error — it does not correctly compute the intended function"
    - "The problem is well-conditioned but the naive algorithm is numerically unstable; the reformulation is a stable alternative"
    - "Both formulas are equally stable; the difference is caused by hardware-specific floating-point rounding modes"
  answer: 2
  explanation: "f(x) = √(x²+1) − 1 near x = 0 is a well-conditioned problem: the true answer ≈ x²/2 varies smoothly with x, so small input changes give small output changes. But the naive formula subtracts two nearly-equal numbers (√(x²+1) ≈ 1 and 1), causing catastrophic cancellation — all significant digits are lost. The reformulation avoids this subtraction and gives full precision. Same problem, dramatically different numerical behavior: this is numerical instability in the naive formula. Because the problem is well-conditioned, a stable algorithm can give an accurate answer."

- question: "An algorithm is proven to be backward stable. What does this guarantee, and under what additional condition does it ensure an accurate answer?"
  type: multiple-choice
  options:
    - "The output is the exact answer to the given input, with zero rounding error accumulated"
    - "The output is the exact answer to a slightly perturbed input; accuracy is further guaranteed when the problem is well-conditioned"
    - "The backward error is always smaller than the forward error, which is always sufficient for practical use"
    - "The algorithm avoids all floating-point cancellation, ensuring full machine-precision output"
  answer: 1
  explanation: "Backward stability means the computed output is exactly what you'd get by solving a slightly perturbed version of the original input (with perturbation of order ε_mach). This alone does not guarantee accuracy — if the problem is ill-conditioned, even a tiny input perturbation produces a large output change, so backward stability gives an accurate answer to the wrong problem. The combination of backward stability + well-conditioned problem guarantees an accurate answer. Option A is too strong (backward stability allows machine-precision perturbations, not exact output)."

- question: "The condition number of a mathematical problem is a property of the problem itself, independent of any particular algorithm used to solve it."
  type: true-false
  answer: true
  explanation: "Conditioning is inherent to the mathematics: it measures how sensitively the output responds to input perturbations, regardless of how the problem is solved. Computing the roots of a nearly-repeated polynomial is ill-conditioned — any algorithm will struggle because the mathematics itself amplifies input errors. By contrast, stability is algorithm-specific: Gaussian elimination with partial pivoting is stable for most linear systems, while naive Gaussian elimination without pivoting can be unstable on the same problem."

- question: "A numerically stable algorithm applied to an ill-conditioned problem will still produce an accurate answer, because stability compensates for poor conditioning."
  type: true-false
  answer: false
  explanation: "Stability and conditioning are independent properties that must both be favorable for accurate computation. A stable algorithm produces the exact answer to a slightly perturbed input — but if the problem is ill-conditioned, that slight perturbation causes a large output change, and the stable answer is still far from the true answer. Stability cannot fix ill-conditioning because the underlying mathematics is the problem. Correct diagnostic: poor accuracy = ill-conditioned problem (fix by reformulating the math) OR unstable algorithm (fix by choosing a better method) OR both."

- question: "When you observe poor numerical accuracy in a computation, why is it important to determine whether the cause is an unstable algorithm or an ill-conditioned problem?"
  type: short-answer
  answer: "The distinction directs where a fix is possible. An unstable algorithm can be replaced — a reformulation that avoids catastrophic cancellation gives full precision on the same well-conditioned problem. An ill-conditioned problem cannot be fixed by any algorithm, because the sensitivity to input error is inherent in the mathematics; addressing it requires reformulating the problem, changing variables, or accepting that the inputs lack sufficient precision for a meaningful answer. Treating an ill-conditioned problem as an algorithm failure leads to wasted effort; treating an unstable algorithm as an inherent limitation leads to incorrectly abandoning solvable problems."
  explanation: "This practical consequence is why the stability/conditioning framework is central to numerical analysis. It prevents two diagnostic errors: blaming an algorithm when the math is inherently sensitive, or accepting poor accuracy when a simple algorithmic improvement would solve it. The condition number quantifies the problem's inherent sensitivity; backward error analysis diagnoses the algorithm's contribution."
```

## Explainer

From your work on floating-point representation, you know that every real number is rounded to the nearest representable value, introducing a small relative error no larger than **machine epsilon** ε_mach (roughly 10⁻¹⁶ for double precision). Every number you feed into a computation is therefore already slightly wrong. The question numerical analysis asks is: does your algorithm make things better or worse?

**Conditioning** is a property of the mathematical problem, independent of how you solve it. A well-conditioned problem is forgiving: small input errors produce small output errors. An ill-conditioned problem is treacherous: tiny input errors can produce enormous output errors, not because of any computational mistake, but because of the mathematics itself. The classic example is **subtractive cancellation**: computing f(x) = (1 + x) − 1 near x = 0. The mathematical answer is just x, but in floating point, 1+x rounds to 1 when x < ε_mach, and you get 0. The entire significant content of x is lost. This is not an algorithm failure — it is the problem of subtraction near zero being ill-conditioned.

**Stability** is a property of a specific algorithm, not the problem. Two algorithms can solve the same well-conditioned problem with very different accuracy. Consider computing √(x² + 1) − 1 near x = 0. The problem is well-conditioned (the true answer ≈ x²/2 varies smoothly). But the naive formula subtracts two nearly-equal numbers (√(x²+1) ≈ 1 and 1), causing catastrophic cancellation. The **numerically stable** reformulation x²/(√(x²+1) + 1) avoids any subtraction of nearly-equal quantities and gives full precision. Same problem, same mathematical answer, wildly different numerical behavior.

The gold standard is **backward stability**: an algorithm is backward stable if its computed output is the exact answer to a slightly perturbed input (with perturbation of order ε_mach). If the problem is also well-conditioned, backward stability guarantees an accurate answer. Together, conditioning and stability let you diagnose numerical failures cleanly: poor accuracy is either a poorly conditioned problem (unavoidable without reformulating the math), an unstable algorithm (fixable by choosing a better method), or both. Knowing which is which directs where to invest effort.
