---
id: integrating-factor-method
title: Integrating Factor Method for First-Order Linear ODEs
domain: mathematics
course: differential-equations
prerequisites:
- id: separable-differential-equations
  type: hard
builds-toward:
- exact-differential-equations
- first-order-linear-odes
tags:
- integrating-factor
- first-order
- linear
stage: formal-systems
status: draft
---

# Integrating Factor Method for First-Order Linear ODEs

## Core Idea
For a first-order linear ODE of the form dy/dx + P(x)y = Q(x), an integrating factor μ(x) = e^(∫P(x)dx) transforms the left side into the derivative of a product: d/dx[μ(x)y] = μ(x)Q(x). This makes the equation directly integrable, converting a challenging linear equation into a solvable form. The integrating factor is one of the most powerful techniques in differential equations.

## Questions

```yaml
- question: "A student correctly computes μ(x) = x³ for the ODE y′ + (3/x)y = x² and multiplies through to get x³y′ + 3x²y = x⁵. They then integrate x³y′ and 3x²y separately to get (x⁴/4)y and (3x³/3)y. What error did they make?"
  type: multiple-choice
  options:
    - "The integrating factor should be e^(−3/x), not x³"
    - "The right side x⁵ should have been integrated before multiplying by μ"
    - "After multiplying by the integrating factor, the left side x³y′ + 3x²y must be recognized as d/dx[x³y] and written as a single derivative before integrating — the two terms cannot be integrated separately"
    - "The constant of integration was omitted from the integrating factor"
  answer: 2
  explanation: "The entire purpose of the integrating factor is to convert the two-term left side into a single derivative d/dx[μy] via the product rule. Once you verify x³y′ + 3x²y = d/dx[x³y], you must write the equation as d/dx[x³y] = x⁵ before integrating both sides to get x³y = x⁶/6 + C. Integrating the terms separately is wrong because each term is not individually a complete derivative — the product rule collapse is the whole mechanism that makes the method work."

- question: "Why is the constant of integration dropped when computing the integrating factor μ(x) = e^(∫P(x)dx)?"
  type: multiple-choice
  options:
    - "Constants of integration are never needed in differential equations"
    - "Including the constant gives μ = e^C · e^(∫P dx); the extra factor e^C multiplies both sides of the equation and cancels, so any particular choice of the constant gives an equally valid integrating factor — the simplest (C = 0) is used"
    - "The integrating factor must equal 1 at x = 0, which forces the constant to be zero"
    - "Including the constant makes the resulting ODE nonlinear"
  answer: 1
  explanation: "Any nonzero multiple of μ works as an integrating factor. Including a constant of integration C gives μ_general = e^(∫P dx + C) = e^C · μ₀. Multiplying both sides of the ODE by e^C · μ₀ is the same as multiplying by μ₀ — the e^C cancels. Dropping the constant (taking C = 0) gives the simplest valid integrating factor, which is all we need. This is one of the few places in ODE solving where omitting the constant of integration is not an error."

- question: "The integrating factor method can solve any first-order ODE, including nonlinear equations like y′ = y²."
  type: true-false
  answer: false
  explanation: "The integrating factor method is specifically designed for first-order *linear* ODEs of the form y′ + P(x)y = Q(x). It works by exploiting the algebraic structure of linear equations: the left side can be made into a product-rule derivative after multiplication by a carefully chosen function. Nonlinear equations like y′ = y² lack this structure — you cannot convert their left side into d/dx[μy] for any μ. Separation of variables, substitution methods, or other techniques are needed for nonlinear equations."

- question: "After multiplying a first-order linear ODE by its integrating factor, the left side becomes the derivative of a product and can be directly integrated without further manipulation."
  type: true-false
  answer: true
  explanation: "This is the central mechanism of the method. The integrating factor μ(x) = e^(∫P dx) is derived precisely so that μ′ = μP. After multiplying y′ + P(x)y = Q(x) by μ, the left side becomes μy′ + μPy = μy′ + μ′y = d/dx[μy]. The equation is now d/dx[μy] = μQ, which integrates directly to μy = ∫μQ dx. The two-term left side collapses into a single derivative — this collapse is what makes the ODE solvable."

- question: "Explain why the integrating factor μ(x) = e^(∫P(x)dx) transforms the ODE y′ + P(x)y = Q(x) into a directly integrable form. Where does the formula for μ come from?"
  type: short-answer
  answer: "The goal is to find a function μ(x) such that μ(y′ + Py) equals d/dx[μy]. Expanding by the product rule: d/dx[μy] = μy′ + μ′y. For this to equal μy′ + μPy, we need μ′ = μP. This is a separable ODE for μ: dμ/μ = P dx, which integrates to ln|μ| = ∫P dx, giving μ = e^(∫P dx). With this choice, multiplying the ODE by μ makes the left side exactly d/dx[μy] = μQ, which integrates to μy = ∫μQ dx."
  explanation: "The integrating factor is not a formula to be memorized and applied mechanically — it is derived by asking 'what function would make the left side a product-rule derivative?' This question has a unique answer (up to a constant multiple), and that answer is e^(∫P dx). Understanding the derivation means you can reconstruct the formula if you forget it, adapt the method to related problems, and explain why it works to someone else — all hallmarks of genuine understanding rather than procedural fluency."
```

## Explainer

You've already solved separable differential equations by getting all the y-terms on one side and all the x-terms on the other, then integrating both sides. That works beautifully when the equation separates — but dy/dx + P(x)y = Q(x) generally cannot be separated if Q(x) ≠ 0. A different strategy is needed: rather than rearranging the equation, multiply both sides by a carefully chosen function to create a pattern you recognize.

The goal is to turn the left side y′ + P(x)y into the derivative of a product. Recall the product rule: d/dx[μ(x)y] = μ(x)y′ + μ′(x)y. Compare this to μ(x)·(y′ + P(x)y) = μ(x)y′ + μ(x)P(x)y. For these to be equal, you need μ′(x) = μ(x)P(x). This is itself a separable ODE: dμ/μ = P(x)dx. Integrating both sides gives ln|μ| = ∫P(x)dx, so **μ(x) = e^{∫P(x)dx}**. The constant of integration is dropped because any particular μ works — the simplest one suffices.

To see the method in action, consider y′ + (2/x)y = x². Here P(x) = 2/x, so μ(x) = e^{∫2/x dx} = e^{2 ln x} = x². Multiply both sides by x²: x²y′ + 2xy = x⁴. The left side is now d/dx[x²y] by the product rule. Integrate both sides: x²y = ∫x⁴ dx = x⁵/5 + C. Divide by x²: y = x³/5 + C/x². The integrating factor converted an unseparable equation into a straightforward integration.

The algorithm in full: (1) rewrite the equation in standard form y′ + P(x)y = Q(x), identifying P and Q. (2) Compute μ(x) = e^{∫P(x)dx}. (3) Multiply both sides by μ. (4) Recognize the left side as d/dx[μy] and write it that way. (5) Integrate both sides. (6) Solve for y. Each step has a clear mechanical purpose, and the method always works for first-order linear equations — unlike separation of variables, which only applies to a restricted class.
