---
id: rounding-errors
title: Rounding Errors and Error Propagation
domain: mathematics
course: numerical-analysis
prerequisites:
- id: machine-epsilon
  type: hard
- id: machine-epsilon
  type: soft
builds-toward:
- catastrophic-cancellation
- numerical-stability
tags:
- rounding
- error
- propagation
stage: formal-systems
status: validated
---
# Rounding Errors and Error Propagation

## Core Idea
Every floating point operation introduces rounding error bounded by machine epsilon times the result's magnitude. As operations are chained, these errors accumulate unpredictably. Understanding error propagation through algorithms is essential for predicting and controlling overall numerical accuracy.

## Questions

```yaml
- question: "A program computes (1.0000001 − 1.0000000) in 64-bit floating-point. Both inputs are accurate to about 16 significant decimal digits, yet the result has far fewer significant digits. What phenomenon explains this?"
  type: multiple-choice
  options:
    - "Overflow: the result exceeds the maximum representable floating-point value"
    - "Catastrophic cancellation: subtracting nearly equal values destroys the leading significant digits, leaving only rounding-error residue"
    - "Underflow: the result is too small to be stored in normalized floating-point form"
    - "Truncation error: the values were stored as integers and rounded before subtraction"
  answer: 1
  explanation: "When two nearly equal numbers are subtracted, their leading significant digits cancel. What remains is dominated by the rounding errors introduced when each value was originally stored. Even though each input had 16-digit accuracy, the result can have only a handful of correct digits — relative error explodes. This is catastrophic cancellation. It is not overflow (the values are small), underflow (the representability issue is about significant digits, not magnitude), or truncation error."

- question: "An algorithm evaluates a function f whose condition number κ ≈ 10⁸. The inputs carry relative error ≈ 10⁻¹⁶ (one unit of machine epsilon). What relative error should you expect in the output?"
  type: multiple-choice
  options:
    - "About 10⁻¹⁶, because machine epsilon bounds all floating-point errors regardless of the function"
    - "About 10⁻⁸, because the condition number amplifies input relative error into output relative error"
    - "About 10⁸, because the condition number is larger than machine epsilon"
    - "Exactly zero, because the algorithm uses exact arithmetic internally"
  answer: 1
  explanation: "The condition number κ measures how much relative error is amplified: output relative error ≈ κ × input relative error ≈ 10⁸ × 10⁻¹⁶ = 10⁻⁸. About 8 digits of precision are lost. This is why ill-conditioned problems (large κ) lose significant digits even with a perfect, stable algorithm — the sensitivity is in the problem, not the code."

- question: "A numerically stable algorithm can still produce a result with large forward error if the problem itself is ill-conditioned."
  type: true-false
  answer: true
  explanation: "Numerical stability (in Wilkinson's backward-error sense) means the algorithm returns the exact answer to a slightly perturbed input. If the problem is ill-conditioned, that nearby input may map to a very different output — so large forward error is possible even for a stable algorithm. Stability is a property of the algorithm; ill-conditioning is a property of the problem. Both matter for final accuracy, and they must be diagnosed separately."

- question: "Floating-point rounding errors from chained operations tend to cancel out on average, so longer computations are generally as accurate as shorter ones."
  type: true-false
  answer: false
  explanation: "Rounding errors do not systematically cancel — they accumulate. For n sequential operations, relative error can grow as O(n × ε_mach). More importantly, specific operations such as subtraction of nearly equal quantities cause catastrophic local amplification. The order and structure of operations affects accuracy dramatically, which is why numerical analysts reformulate algebraically equivalent expressions and why algorithms like Kahan compensated summation exist."

- question: "What does it mean for an algorithm to be 'numerically stable' in terms of backward error analysis? Why is backward error analysis more useful than forward error analysis for judging algorithm quality?"
  type: short-answer
  answer: "A numerically stable algorithm is one whose backward error is small — the computed output is the exact result of applying the algorithm to a slightly perturbed input, where the perturbation is comparable in size to machine epsilon. This separates algorithm behavior from problem difficulty: small backward error means any inaccuracy in the output is due to the problem's own ill-conditioning, not a flaw in the algorithm."
  explanation: "Forward error analysis tracks how rounding errors at each step accumulate to the final result — but it often wildly overestimates actual errors because errors of opposite sign partially cancel. Backward error analysis sidesteps this by asking: 'What input would have produced this output exactly?' If the answer is 'an input very close to the actual input,' the algorithm is well-behaved. This lets us certify algorithms like Gaussian elimination with partial pivoting as stable even when forward error bounds look alarming."
```

## Explainer

You've learned that **machine epsilon** (ε_mach) is the smallest positive number such that 1 + ε_mach ≠ 1 in floating-point arithmetic — it measures the granularity of the number system. Every time you perform a floating-point operation like addition or multiplication, the result must be rounded to the nearest representable number. The rounding error introduced by a single operation is bounded by ε_mach × |result|, which is tiny on its own. The challenge is that algorithms chain thousands or millions of such operations, and these small errors accumulate.

**Error propagation** asks: if the inputs to a computation have small errors, how large are the errors in the output? For a function f(x), the absolute error in the output is approximately |f'(x)| × |Δx|, where Δx is the error in x. The **relative error** in the output is approximately |f'(x)| × |x/f(x)| × (relative error in x). The factor |f'(x)| × |x/f(x)| is the **condition number** of the function — it measures how much relative error is amplified. A condition number near 1 is benign; a large condition number means the function is ill-conditioned and tiny input errors explode into large output errors.

In multi-step algorithms, rounding errors accumulate through two distinct mechanisms. **Forward error analysis** tracks how errors introduced at each step propagate to the final result — it bounds the total error by summing contributions from each operation. **Backward error analysis** (Wilkinson's key insight) asks instead: for what slightly perturbed input would the algorithm have produced this exact output? If the backward error is small (of order ε_mach), the algorithm is **numerically stable**, even if the forward errors look alarming. Stable algorithms give the right answer to a nearby problem; unstable ones don't even achieve that.

A concrete example: summing n numbers in sequence accumulates O(n ε_mach) relative error. For n = 10⁶ and ε_mach ≈ 10⁻¹⁶, this gives relative error of about 10⁻¹⁰ — still small. But if some numbers nearly cancel (like summing 1.0000001 − 1.0000000), **catastrophic cancellation** can amplify the relative error dramatically, since you subtract two nearly equal quantities and the leading significant digits vanish, leaving only the rounded residue. This is why the order of operations matters in floating-point arithmetic, and why numerical analysts sometimes reformulate algebraically equivalent expressions to avoid cancellation.
