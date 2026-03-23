---
id: richardsons-extrapolation
title: Richardson's Extrapolation
domain: mathematics
course: numerical-analysis
prerequisites:
- id: taylor-series
  type: hard
builds-toward:
- romberg-integration
tags:
- richardson-extrapolation
- acceleration
- deferred-correction
stage: formal-systems
status: validated
---

# Richardson's Extrapolation

## Core Idea
Richardson's extrapolation accelerates convergence by combining approximations at different step sizes to cancel leading error terms. If an approximation has error A(h) = a₀ + a₁h^p + a₂h^{2p} + ..., linear combinations of A(h) and A(h/2) eliminate the a₁h^p term, increasing convergence order. This technique amplifies accuracy without more function evaluations.

## Questions

```yaml
- question: "A numerical method has O(h²) error. You compute approximations A(0.1) and A(0.05). What order of accuracy does Richardson extrapolation achieve using these two values?"
  type: multiple-choice
  options:
    - "O(h²) — you've just averaged two estimates of the same accuracy"
    - "O(h⁴) — the leading h² error term is cancelled by the linear combination"
    - "O(h) — the extrapolation introduces additional first-order error"
    - "Exact — the error cancels completely when two step sizes are combined"
  answer: 1
  explanation: "With p=2, Richardson extrapolation forms R = (4·A(h/2) − A(h))/3. The coefficients are chosen precisely to cancel the leading c₁h² error term, leaving residual error O(h⁴). Option 0 is wrong: simple averaging does not cancel error terms. Option 3 is wrong: only the *leading* term cancels; higher-order terms remain."

- question: "Richardson extrapolation is applied to an approximation near a jump discontinuity in the function. What happens?"
  type: multiple-choice
  options:
    - "It improves accuracy as usual — the formula doesn't depend on smoothness"
    - "It gives O(h⁴) accuracy on each side of the discontinuity separately"
    - "It may give wildly wrong results because the error power series assumed by the method breaks down"
    - "It reduces to simple averaging near discontinuities, giving O(h²) accuracy"
  answer: 2
  explanation: "Richardson extrapolation requires that the error expands as A(h) = L + c₁hᵖ + c₂h²ᵖ + ..., which follows from Taylor series and requires the function to be smooth. Near a discontinuity, the function isn't smooth enough to support this expansion, so the assumed error structure doesn't hold. The method then amplifies error rather than cancelling it. Understanding *when* the power series expansion is valid — which requires Taylor analysis — is essential for trusting the result."

- question: "Richardson extrapolation requires computing the function at additional points beyond those needed for the two base approximations."
  type: true-false
  answer: false
  explanation: "The power of Richardson extrapolation is precisely that it extracts higher accuracy from approximations already computed at two step sizes (h and h/2). No additional function evaluations are required. The accuracy gain — jumping from O(hᵖ) to O(h²ᵖ) — is 'free' in terms of function calls, which is why the method is so widely used."

- question: "Richardson extrapolation with p=2 transforms an O(h²) method into an O(h⁴) method by eliminating the leading error term."
  type: true-false
  answer: true
  explanation: "This is exactly what the extrapolation achieves. By forming the appropriate linear combination of A(h) and A(h/2), the c₁h² coefficient cancels, leaving the next term c₂h⁴ as the dominant error. Applying Richardson extrapolation again (as Romberg integration does) can then eliminate the h⁴ term, and so on."

- question: "Why does Richardson extrapolation fail near discontinuities, even though the algebraic formula is always well-defined?"
  type: short-answer
  answer: "Richardson extrapolation assumes the error expands as a power series A(h) = L + c₁hᵖ + c₂h²ᵖ + ..., which follows from Taylor series. Near a discontinuity, the function lacks the smoothness required for a Taylor expansion, so the actual error does NOT behave like this power series. The formula cancels what it assumes to be the leading error term — but since the actual error has a different structure, the subtraction amplifies error rather than reducing it."
  explanation: "The method is not merely algebraic; it is physical. It exploits a known structure in how the error depends on h. If that structure is absent (non-smooth functions, adaptive step-size changes, singularities), the extrapolation is being applied without its key precondition, and the result is unreliable."
```

## Explainer

Richardson's extrapolation is a clever trick that turns "two mediocre approximations" into "one much better one." To see why it works, start with what you know from Taylor series. Many numerical methods — finite difference derivatives, numerical integration rules, and others — produce approximations whose error can be expanded as a power series in the step size h: A(h) = L + c₁h^p + c₂h^{2p} + ... where L is the true answer, and the c₁h^p term is the dominant error. Halving h reduces this leading error by a factor of 2^p — which is good. But Richardson's idea is more radical: can we *eliminate* that leading error term entirely, rather than just shrinking it?

Yes. Compute A(h) and A(h/2). You have two equations: A(h) ≈ L + c₁h^p and A(h/2) ≈ L + c₁(h/2)^p = L + c₁h^p/2^p. Multiply the second equation by 2^p and subtract the first: 2^p · A(h/2) − A(h) ≈ (2^p − 1)L. Solving for L gives the **Richardson extrapolate**: R = (2^p · A(h/2) − A(h)) / (2^p − 1). The c₁h^p term cancels exactly, and the remaining error is O(h^{2p}) — a full order improvement. For a method that was O(h^2) accurate, Richardson extrapolation makes it O(h^4) with no extra function evaluations beyond computing A at two step sizes.

A concrete example makes this vivid. The centered difference formula approximates f'(x) ≈ (f(x+h) − f(x−h))/(2h) with error O(h²). Suppose h = 0.1 gives error ~0.01, and h = 0.05 gives error ~0.0025. You could just use h = 0.05 and accept the O(h²) accuracy. Or you could take both values, apply Richardson extrapolation with p = 2 (since the error series involves even powers of h), and get an approximation with error O(h⁴) — roughly 0.0000625. Same two function evaluations, dramatically better result.

The deeper reason Richardson extrapolation is so powerful is that it's not specific to any one method. Wherever you have an approximation with a known asymptotic error expansion, you can apply extrapolation. **Romberg integration** — the topic this leads into — applies Richardson extrapolation repeatedly to the trapezoidal rule, building a triangular table of increasingly accurate estimates. At each level, you eliminate one more error term, until floating-point roundoff dominates. This recursive application is the soul of Romberg's method.

One important caution: Richardson extrapolation requires that the error expansion A(h) = L + c₁h^p + c₂h^{2p} + ... actually holds — that the error truly behaves like a power series in h. If this assumption breaks down (for example, near a discontinuity, or when the function is not smooth enough to support a Taylor expansion), the extrapolation can give wildly wrong answers. The method amplifies accuracy when the expansion is valid, and amplifies error when it isn't. Understanding *why* the expansion holds for a given method — which comes from Taylor series analysis — is essential for knowing when to trust the result.
