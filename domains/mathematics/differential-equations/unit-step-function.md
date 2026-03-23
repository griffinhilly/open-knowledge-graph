---
id: unit-step-function
title: Unit Step Function and Piecewise-Defined Forcing
domain: mathematics
course: differential-equations
prerequisites:
- id: laplace-transform-definition-and-properties
  type: hard
- id: piecewise-functions
  type: soft
builds-toward:
- convolution-theorem
tags:
- laplace-transform
- piecewise
- step-function
stage: formal-systems
status: validated
---

# Unit Step Function and Piecewise-Defined Forcing

## Core Idea
The unit step function u(t - a) is 0 for t < a and 1 for t ≥ a. Its Laplace transform L{u(t - a)} = e^{-as}/s handles piecewise-defined forcing terms. The shifting property L{f(t - a)u(t - a)} = e^{-as}F(s) simplifies solving ODEs with discontinuous inputs.

## Questions

```yaml
- question: "Using the second shifting theorem, what is the Laplace transform of f(t) = sin(t − 3) · u(t − 3)?"
  type: multiple-choice
  options:
    - "e^{−3s} / (s² + 1)"
    - "sin(3) · e^{−3s} / (s² + 1)"
    - "e^{3s} / (s² + 1)"
    - "1 / (s² + 1)"
  answer: 0
  explanation: "The second shifting theorem states L{f(t − a) · u(t − a)} = e^{−as} · F(s), where F(s) = L{f(t)}. Here f(t) = sin(t), so F(s) = 1/(s² + 1), and a = 3. The result is e^{−3s} · (1/(s² + 1)). The factor e^{−3s} encodes the time delay of 3 in the s-domain. Options B and C reflect common errors: confusing the time-shift with evaluating sin at the activation point, or getting the sign of the exponent wrong."

- question: "A student wants the Laplace transform of g(t) = sin(t) · u(t − 3) — a sine wave that switches on at t = 3 but continues as sin(t), not as sin(t − 3). They write e^{−3s} · L{sin(t)} = e^{−3s}/(s² + 1). Is this correct?"
  type: multiple-choice
  options:
    - "Yes — the step function u(t − 3) always contributes e^{−3s} regardless of the argument of sin"
    - "No — the second shifting theorem requires f(t − 3) · u(t − 3), not f(t) · u(t − 3). The student must rewrite sin(t) as sin((t − 3) + 3) and expand before applying the theorem"
    - "No — you cannot take the Laplace transform of a product involving a step function"
    - "Yes, but only for t > 3 where sin(t) is defined"
  answer: 1
  explanation: "This is the most common error with the second shifting theorem. The theorem applies to f(t − a) · u(t − a), where the argument of f and the activation point of u match. Writing f(t) · u(t − a) is a different function — it switches on at t = a but continues with the unshifted argument. To apply the theorem, the student must rewrite: sin(t) = sin((t − 3) + 3) = sin(t − 3)cos(3) + cos(t − 3)sin(3), then apply the theorem to each term."

- question: "The Laplace transform of u(t − a) is e^{−as}/s, which means a time delay of a in the time domain corresponds to multiplication by e^{−as} in the s-domain."
  type: true-false
  answer: true
  explanation: "This is correct and is the foundational fact behind the entire unit step / piecewise-forcing framework. The exponential e^{−as} is the s-domain signature of a time delay: any function that 'starts at time a' rather than time 0 will have its transform multiplied by e^{−as}. When you see e^{−as} · F(s) in the s-domain, you immediately know the inverse is f(t − a) · u(t − a) — a copy of f shifted right by a, active only for t ≥ a."

- question: "If e^{−2s} · F(s) appears in the s-domain, the inverse Laplace transform is f(t) · u(t − 2), where f(t) is the function whose transform is F(s)."
  type: true-false
  answer: false
  explanation: "This is false — the inverse is f(t − 2) · u(t − 2), not f(t) · u(t − 2). The time-shift must be applied to the argument of f as well. f(t − 2) · u(t − 2) is a copy of f shifted right by 2 units, turned on at t = 2. Writing f(t) · u(t − 2) would be f evaluated at the original t but switched on at t = 2 — a different function that does not correspond to e^{−2s} · F(s) under the second shifting theorem."

- question: "Why must a forcing term be written as f(t − a) · u(t − a) rather than f(t) · u(t − a) in order to directly apply the second shifting theorem? What goes wrong if you use f(t) · u(t − a) instead?"
  type: short-answer
  answer: "The second shifting theorem is L{f(t − a) · u(t − a)} = e^{−as} · F(s). The argument of f must be (t − a) to match the activation time of the step function. If you write f(t) · u(t − a), you are describing a genuinely different function — f with its original, unshifted argument, just switched on at t = a. This does not satisfy the hypothesis of the theorem, so applying it directly yields an incorrect result. To proceed, you must first rewrite f(t) in terms of (t − a) using algebra (e.g., expanding f((t − a) + a)), and only then can the theorem be applied to each resulting term."
  explanation: "The theorem is a precise statement about a specific form. Many errors in this topic come from treating u(t − a) as a generic 'delay operator' that can be applied to any expression, rather than as a function that shifts the entire expression including the argument. The mismatch between f(t) and u(t − a) is invisible to a student who isn't thinking carefully about what the two functions are actually computing."
```

## Explainer

You've learned the Laplace transform and its basic properties, and you know how to represent piecewise-defined functions by specifying different formulas on different intervals. The **unit step function** u(t − a) bridges these two ideas: it equals 0 for t < a and 1 for t ≥ a, acting like a switch that turns on at time t = a. By combining step functions, you can express any piecewise-defined forcing term as a single formula and take its Laplace transform in one calculation.

The key to writing piecewise functions cleanly is the following pattern: a function that equals g(t) for 0 ≤ t < a and h(t) for t ≥ a can be written as g(t) + [h(t) − g(t)] · u(t − a). Before the switch (t < a), the step function is 0, so you get g(t). After the switch (t ≥ a), the step function is 1, so you get g(t) + h(t) − g(t) = h(t). More complex piecewise functions, with multiple breakpoints, are assembled similarly by adding more step functions, one per switch. This turns a description with cases into a single algebraic expression that the Laplace transform can handle directly.

The Laplace transform of the unit step function is L{u(t − a)} = e^{−as}/s. The exponential factor e^{−as} is the signature of a time delay in the s-domain — it encodes "this feature arrives at time a." The **second shifting theorem** generalizes this: L{f(t − a) · u(t − a)} = e^{−as} · F(s), where F(s) = L{f(t)}. To apply it, you need the forcing term written as a function of (t − a) multiplied by u(t − a) — not f(t) · u(t − a), but f(t − a) · u(t − a), with the argument shifted to match the step function's activation time.

Inverting in the other direction: if you encounter e^{−as} · F(s) in the s-domain, the inverse transform is f(t − a) · u(t − a). Take the function whose transform is F(s), shift it right by a (replace t with t − a), and multiply by u(t − a) to indicate it only exists for t ≥ a. For example, e^{−2s}/(s + 1) inverts to e^{−(t−2)} · u(t − 2): an exponential decay that begins at t = 2. This combination — step functions for switching, time-shifting for delaying — makes the Laplace method directly applicable to discontinuous forcing, which arises constantly when modeling circuits being switched on, mechanical impulses starting at a fixed time, or any system responding to an input that begins at t = a rather than t = 0.
