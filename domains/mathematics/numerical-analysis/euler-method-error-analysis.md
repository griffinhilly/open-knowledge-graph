---
id: euler-method-error-analysis
title: Euler's Method for ODEs (Error Analysis)
domain: mathematics
course: numerical-analysis
prerequisites:
- id: eulers-method
  type: hard
- id: taylor-series
  type: hard
builds-toward:
- runge-kutta-methods
tags:
- euler-method
- ode-solving
- truncation-error
stage: advanced
status: validated
---

# Euler's Method for ODEs (Error Analysis)

## Core Idea
Euler's method y_{n+1} = y_n + h*f(x_n, y_n) has local truncation error O(h²) and global error O(h) by Taylor expansion analysis. The local error at each step accumulates over the integration interval, and the total accumulated error grows linearly with integration length. Understanding this trade-off guides appropriate step size selection.

## Questions

```yaml
- question: "You use Euler's method to solve an ODE over [0, 1] with step size h = 0.1 and find the global error at x = 1 is approximately 0.08. If you repeat the computation with h = 0.05, what global error do you expect?"
  type: multiple-choice
  options:
    - "Approximately 0.04 — halving the step size halves the global error for a first-order method"
    - "Approximately 0.002 — halving the step size reduces the global error by a factor of 4 for a first-order method"
    - "Approximately 0.08 — the global error is determined by the ODE, not the step size"
    - "Approximately 0.016 — halving h reduces global error by a factor of 5 due to error cancellation"
  answer: 0
  explanation: "Euler's method is first-order globally: global error = O(h). Halving h halves the global error. Option B describes a second-order method (like classical Runge-Kutta), where halving h reduces error by a factor of 4. The first-order relationship O(h) is what defines Euler's method as first-order — it's the practical consequence of having O(h²) local error accumulated over O(1/h) steps."

- question: "Why is Euler's method called 'first-order' when its local truncation error at each step is O(h²)?"
  type: multiple-choice
  options:
    - "Because the method was first published in the first volume of Euler's collected works"
    - "Because the global error is O(h¹) — one power lower than the local error — due to accumulation of O(1/h) local errors over the integration interval"
    - "Because Euler's method uses only first-order Taylor expansion terms to compute f(x, y)"
    - "Because the method is only accurate to first decimal place regardless of step size"
  answer: 1
  explanation: "The 'order' of a method refers to its global error, not its local truncation error. Local error per step is O(h²), but over [0, T] there are N = T/h steps, so total accumulated error is approximately N × O(h²) = (T/h) × O(h²) = O(h). This one-order reduction is why global order = local order − 1 for Euler's method. The confusingly similar terminology (local truncation error vs. method order) is a common source of error."

- question: "The global error of Euler's method is the same order as its local truncation error: both are O(h²)."
  type: true-false
  answer: false
  explanation: "Local truncation error is O(h²), but global error is O(h) — one order lower. This is because local errors accumulate over approximately T/h steps. Each step contributes O(h²) error, and (T/h) × O(h²) = O(h). The method is thus called 'first-order globally,' not second-order. Confusing local and global error is one of the most common misconceptions in numerical ODE analysis."

- question: "Halving the step size in Euler's method approximately halves the global error at the end of the integration interval."
  type: true-false
  answer: true
  explanation: "Because Euler's method has O(h) global error, the relationship is linear: cutting h in half cuts global error in half. This contrasts with higher-order methods: classical fourth-order Runge-Kutta has O(h⁴) global error, so halving h reduces error by a factor of 16. The linear relationship in Euler's method makes it expensive for high accuracy — to reduce error by a factor of 1000, you need 1000× as many steps."

- question: "Explain why the global error of Euler's method is O(h) rather than O(h²), despite each individual step having local truncation error of O(h²). What happens to the local errors over the course of the integration?"
  type: short-answer
  answer: "Local truncation error at each step is O(h²) because the Taylor expansion of the true solution includes a (h²/2)y'' term that Euler's method omits. But over an integration interval [0, T] with step size h, there are N = T/h steps. If these local errors simply add without interaction, total error ≈ N × O(h²) = (T/h) × O(h²) = T × O(h) = O(h). Additionally, errors from early steps propagate and perturb subsequent steps, but for Lipschitz-continuous ODEs, this propagation does not cause exponential blowup — it remains bounded, and the net effect is still O(h) globally."
  explanation: "The practical implication is that to achieve global error ε with Euler's method, you need h ~ ε, meaning N ~ T/ε steps. For ε = 10⁻⁶, that's a million steps over [0,1]. This cost motivates higher-order methods: fourth-order Runge-Kutta achieves the same accuracy with only N ~ T/ε^(1/4) steps, requiring far fewer steps for the same precision."
```

## Explainer

You know Euler's method from practice: starting at y(x₀) = y₀, you step forward by yₙ₊₁ = yₙ + h·f(xₙ, yₙ), where h is the step size. The method produces numbers that approximate the true solution, but it makes errors at every step and those errors accumulate. To understand how reliable the method is, you need to quantify two distinct quantities: **local truncation error** (the mistake at a single step) and **global error** (the total accumulated mistake at the end of the integration interval).

The local truncation error comes directly from Taylor series. The true solution satisfies y(xₙ₊₁) = y(xₙ) + h·y'(xₙ) + (h²/2)·y''(xₙ) + O(h³). Euler's method keeps only the first two terms: yₙ₊₁ = yₙ + h·f(xₙ, yₙ) = yₙ + h·y'(xₙ). The discrepancy at one step is therefore (h²/2)·y''(xₙ) + O(h³), which is O(h²). This is the local truncation error. The "2" in the exponent gives Euler's method its classification as a **first-order method** — the global error is O(h¹), one power lower than the local error.

Why does the global error drop one order? Consider integrating from x = 0 to x = T with step size h. There are N = T/h steps, each contributing a local error of O(h²). If these errors simply added, the total would be N × O(h²) = (T/h) × O(h²) = O(h). Errors also propagate — an error introduced at step k perturbs the trajectory for all subsequent steps — but careful stability analysis shows that this propagation does not cause exponential blowup for ODEs satisfying a Lipschitz condition. The net effect is still O(h) global error. This means halving the step size halves the final error: the method is **first-order accurate globally**.

The practical consequence is significant. To achieve global error ε, you need h ~ ε, requiring N ~ T/ε steps. For high accuracy (ε = 10⁻⁶), you need a million steps. This cost motivates higher-order methods: the classical Runge-Kutta method of order 4 achieves O(h⁴) global error, requiring only N ~ T/ε^(1/4) steps for the same accuracy — a factor of ε^(3/4) fewer steps. Error analysis is not just bookkeeping; it tells you precisely when Euler's method is adequate and when the step-size cost makes it impractical.
