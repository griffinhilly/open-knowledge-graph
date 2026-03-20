---
id: rounding-errors
title: Rounding Errors and Error Propagation
domain: mathematics
course: numerical-analysis
prerequisites:
- id: machine-epsilon
  type: hard
builds-toward:
- catastrophic-cancellation
- numerical-stability
tags:
- rounding
- error
- propagation
stage: formal-systems
status: draft
---

# Rounding Errors and Error Propagation

## Core Idea
Every floating point operation introduces rounding error bounded by machine epsilon times the result's magnitude. As operations are chained, these errors accumulate unpredictably. Understanding error propagation through algorithms is essential for predicting and controlling overall numerical accuracy.

## Explainer

You've learned that **machine epsilon** (ε_mach) is the smallest positive number such that 1 + ε_mach ≠ 1 in floating-point arithmetic — it measures the granularity of the number system. Every time you perform a floating-point operation like addition or multiplication, the result must be rounded to the nearest representable number. The rounding error introduced by a single operation is bounded by ε_mach × |result|, which is tiny on its own. The challenge is that algorithms chain thousands or millions of such operations, and these small errors accumulate.

**Error propagation** asks: if the inputs to a computation have small errors, how large are the errors in the output? For a function f(x), the absolute error in the output is approximately |f'(x)| × |Δx|, where Δx is the error in x. The **relative error** in the output is approximately |f'(x)| × |x/f(x)| × (relative error in x). The factor |f'(x)| × |x/f(x)| is the **condition number** of the function — it measures how much relative error is amplified. A condition number near 1 is benign; a large condition number means the function is ill-conditioned and tiny input errors explode into large output errors.

In multi-step algorithms, rounding errors accumulate through two distinct mechanisms. **Forward error analysis** tracks how errors introduced at each step propagate to the final result — it bounds the total error by summing contributions from each operation. **Backward error analysis** (Wilkinson's key insight) asks instead: for what slightly perturbed input would the algorithm have produced this exact output? If the backward error is small (of order ε_mach), the algorithm is **numerically stable**, even if the forward errors look alarming. Stable algorithms give the right answer to a nearby problem; unstable ones don't even achieve that.

A concrete example: summing n numbers in sequence accumulates O(n ε_mach) relative error. For n = 10⁶ and ε_mach ≈ 10⁻¹⁶, this gives relative error of about 10⁻¹⁰ — still small. But if some numbers nearly cancel (like summing 1.0000001 − 1.0000000), **catastrophic cancellation** can amplify the relative error dramatically, since you subtract two nearly equal quantities and the leading significant digits vanish, leaving only the rounded residue. This is why the order of operations matters in floating-point arithmetic, and why numerical analysts sometimes reformulate algebraically equivalent expressions to avoid cancellation.
