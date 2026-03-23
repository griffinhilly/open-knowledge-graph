---
id: runge-kutta-methods
title: Runge-Kutta Methods
domain: mathematics
course: numerical-analysis
prerequisites:
- id: eulers-method-convergence
  type: hard
builds-toward:
- multistep-methods-adams
- stiff-equations
tags:
- runge-kutta
- ode
- high-order
stage: formal-systems
status: validated
---

# Runge-Kutta Methods

## Core Idea
Runge-Kutta methods use intermediate (stage) evaluations of f to improve accuracy. The classical 4th-order RK4 achieves error O(h⁵) with four function evaluations per step. RK methods are explicit (computing stages sequentially) or implicit (solving systems), with explicit methods simpler but sensitive to stiffness. RK methods are the workhorse of ODE solving due to their simplicity and effectiveness.

## Questions

```yaml
- question: "You halve the step size h when solving an ODE. How do the global errors of Euler's method and RK4 compare after this change?"
  type: multiple-choice
  options:
    - "Both errors reduce by roughly half"
    - "Euler's error reduces by half; RK4's error reduces by a factor of about 16"
    - "Euler's error reduces by a factor of 4; RK4's reduces by a factor of 16"
    - "RK4's error reduces by half; Euler's reduces by a factor of 16"
  answer: 1
  explanation: "Global error for Euler's method is O(h) — halving h halves the error. Global error for RK4 is O(h⁴) — halving h reduces error by 2⁴ = 16. This is the core advantage of high-order methods: the same reduction in step size yields dramatically more accuracy. A method's 'order' tells you the exponent: 4th-order means error scales as h⁴."

- question: "Why do engineers often prefer implicit Runge-Kutta methods over explicit methods for certain ODE problems?"
  type: multiple-choice
  options:
    - "Implicit methods require fewer function evaluations per step, making them faster"
    - "Implicit methods achieve higher-order accuracy with fewer stages than explicit methods"
    - "Implicit methods remain stable for stiff equations where explicit methods require prohibitively tiny step sizes"
    - "Implicit methods do not require initial conditions, simplifying setup"
  answer: 2
  explanation: "For stiff equations — those with components that vary on very different timescales — explicit methods like RK4 must use extremely small step sizes to remain numerically stable, making them computationally impractical. Implicit methods allow stages to depend on each other (requiring a small linear system to be solved at each step), which gives them much better stability properties. The extra cost per step is outweighed by the ability to take much larger steps."

- question: "In RK4, each subsequent stage uses results from earlier stages to refine the slope estimate, with the final update being a weighted average of all four slopes."
  type: true-false
  answer: true
  explanation: "This is exactly how RK4 works. k₁ is the slope at the start; k₂ uses k₁ to estimate the slope at the midpoint; k₃ refines the midpoint estimate using k₂; k₄ estimates the slope at the endpoint using k₃. The update yₙ₊₁ = yₙ + (h/6)(k₁ + 2k₂ + 2k₃ + k₄) is the weighted average, analogous to Simpson's rule, which achieves O(h⁵) local and O(h⁴) global accuracy."

- question: "The weights (1, 2, 2, 1)/6 in the RK4 update formula are arbitrary design choices that happen to produce good accuracy in practice."
  type: true-false
  answer: false
  explanation: "The weights are engineered, not arbitrary. RK4 is designed so that a Taylor expansion of yₙ₊₁ matches the true solution's Taylor series through the h⁴ term. The weights (1, 2, 2, 1)/6 are identical to those in Simpson's rule, reflecting that both are solving the same approximation problem — how to best combine samples at specified points to achieve a high-order estimate. The design ensures no coincidence: the weights are derived analytically to cancel error terms through fourth order."

- question: "Explain why RK4 achieves much higher accuracy than Euler's method without simply taking smaller steps."
  type: short-answer
  answer: "RK4 evaluates f at four intermediate points within each step interval and combines them with carefully chosen weights, analogous to how Simpson's rule improves on the rectangle rule in numerical integration. This sampling of f at multiple stages within [tₙ, tₙ + h] allows the method to approximate the true solution's behavior through the h⁴ term in its Taylor expansion, achieving O(h⁴) global error versus O(h) for Euler's method — so RK4 extracts much more accuracy from each step."
  explanation: "The analogy to numerical integration is precise: Euler's method is the rectangle rule (one sample at the left endpoint); RK4 is Simpson's rule (three samples with the correct weights). The key insight is that accuracy comes from how cleverly you sample f within the step interval, not just from how small the interval is."
```

## Explainer

From Euler's method, you know the simplest approach: take a step of size h, evaluate f at the current point, and move in that direction. The local truncation error is O(h²) — accuracy improves only linearly as you reduce the step size. Euler's method is easy to understand but slow to converge. Runge-Kutta methods use the same idea but squeeze much more accuracy out of each step by evaluating f at several intermediate points within the step interval.

The strategy is analogous to numerical integration. Euler's method is like the rectangle rule — it approximates the area under a curve using only the left endpoint. Higher-order methods sample f at more points within [tₙ, tₙ + h] and combine those samples with carefully chosen weights, like Simpson's rule uses three points for better accuracy. Each evaluation of f at an intermediate point is called a **stage**. The classical **RK4** method uses four stages:

- k₁ = f(tₙ, yₙ) — slope at the start
- k₂ = f(tₙ + h/2, yₙ + h·k₁/2) — slope at the midpoint, estimated using k₁
- k₃ = f(tₙ + h/2, yₙ + h·k₂/2) — slope at the midpoint, refined using k₂
- k₄ = f(tₙ + h, yₙ + h·k₃) — slope at the endpoint, estimated using k₃

The update is yₙ₊₁ = yₙ + (h/6)(k₁ + 2k₂ + 2k₃ + k₄). This weighted average of four slopes achieves local error O(h⁵) and global error O(h⁴) — hence "4th-order." Halving the step size reduces the error by a factor of 16, compared to a factor of 2 for Euler's method.

The design of RK4 is not arbitrary. It's engineered so that a Taylor expansion of yₙ₊₁ matches the true solution's Taylor series through the h⁴ term. The weights (1, 2, 2, 1)/6 echo Simpson's rule exactly — no coincidence, since both are solving the same approximation problem. **Explicit** RK methods (like RK4) compute each stage directly from previously computed stages. **Implicit** methods allow stages to depend on each other, requiring a small system to be solved at each step — more expensive, but essential for **stiff equations** where explicit methods require prohibitively small step sizes to remain stable. RK4 is the default tool for smooth, non-stiff ODEs: four evaluations per step, no linear algebra, and accuracy that handles most practical problems with reasonable step sizes.
