---
id: laplace-transform-of-derivatives
title: Laplace Transform of Derivatives and Integrals
domain: mathematics
course: differential-equations
prerequisites:
- id: laplace-transform-definition
  type: hard
- id: integration-by-parts
  type: soft
builds-toward:
- solving-ivps-with-laplace-transforms
tags:
- laplace-transform
- derivative
- integral
stage: formal-systems
status: validated
---

# Laplace Transform of Derivatives and Integrals

## Core Idea
The key property L{f'(t)} = sF(s) - f(0) (and generalizations for higher derivatives) converts ODE initial value problems into algebraic problems. Similarly, L{∫₀ᵗ f(τ) dτ} = F(s)/s, converting integro-differential equations to algebraic form.

## Questions

```yaml
- question: "What does the formula L{f'(t)} = sF(s) − f(0) accomplish when applied to an ODE?"
  type: multiple-choice
  options:
    - "It replaces differentiation with division by s, simplifying integration"
    - "It converts differentiation in the time domain into multiplication by s in the s-domain, with initial conditions encoded algebraically"
    - "It eliminates the need for initial conditions by shifting them to a boundary term"
    - "It converts the ODE into a partial differential equation in s and t"
  answer: 1
  explanation: "The key transformation is that differentiation (an operation requiring calculus) becomes multiplication by s (a purely algebraic operation) in the s-domain. The initial condition f(0) is subtracted as a constant term. This means a differential equation — which requires solving for a function — becomes a polynomial equation in Y(s) that can be solved by algebra alone, then inverted."

- question: "For the ODE y'' + 3y' + 2y = eᵗ with y(0) = 0 and y'(0) = 1, what does the left side become after taking the Laplace transform?"
  type: multiple-choice
  options:
    - "(s² + 3s + 2)Y(s)"
    - "(s² + 3s + 2)Y(s) − 1"
    - "(s² + 3s + 2)Y(s) − s"
    - "s²Y(s) + 3sY(s) + 2Y(s) − s − 3"
  answer: 1
  explanation: "Applying the formulas: L{y''} = s²Y − sy(0) − y'(0) = s²Y − 0 − 1 = s²Y − 1. L{y'} = sY − y(0) = sY − 0 = sY. L{2y} = 2Y. Summing: s²Y − 1 + 3sY + 2Y = (s² + 3s + 2)Y − 1. The −1 comes entirely from the initial condition y'(0) = 1. Option A forgets this term; options C and D incorrectly apply the initial conditions."

- question: "The Laplace transform of f'(t) is derived using integration by parts."
  type: true-false
  answer: true
  explanation: "L{f'(t)} = ∫₀^∞ f'(t)e^{−st} dt is evaluated by integration by parts with u = e^{−st} and dv = f'(t)dt. This yields [f(t)e^{−st}]₀^∞ + s∫₀^∞ f(t)e^{−st} dt = −f(0) + sF(s). The integration by parts is the entire derivation — the formula is not a definition but a theorem proved this way."

- question: "Differentiating twice gives L{f''(t)} = s²F(s) − sf(0) − f'(0), which incorporates both initial conditions y(0) and y'(0)."
  type: true-false
  answer: true
  explanation: "Applying the first-derivative formula twice: L{f''} = L{(f')'} = sL{f'} − f'(0) = s(sF(s) − f(0)) − f'(0) = s²F(s) − sf(0) − f'(0). Each differentiation 'peels off' one initial condition. This is precisely why Laplace transforms are the natural tool for initial value problems: the initial conditions are automatically incorporated into the transformed equation."

- question: "Why do initial conditions appear in the Laplace transform of derivatives, and why is this advantageous for solving initial value problems?"
  type: short-answer
  answer: "Initial conditions appear because of the boundary term that arises from integration by parts: [f(t)e^{−st}]₀^∞ evaluates to −f(0) at the lower limit. Higher derivatives peel off successive initial conditions (f(0), f'(0), etc.) as additional terms. This is advantageous because, instead of first finding the general solution and then fitting constants to initial conditions in a separate step, the initial conditions are baked directly into the transformed algebraic equation — the solution automatically satisfies them."
  explanation: "This is the core payoff of the method. In standard ODE techniques (undetermined coefficients, variation of parameters), you find a general solution C₁y₁ + C₂y₂ + yₚ and then solve a system of equations to find C₁ and C₂ from initial conditions. The Laplace approach collapses these two steps: the transformed equation already incorporates the initial conditions as constants, so solving for Y(s) directly gives the specific (not general) solution."
```

## Explainer

From your study of the Laplace transform definition, you know that L{f(t)} = ∫₀^∞ f(t)e^{−st} dt = F(s). The transform converts a function of time t into a function of the complex parameter s. What you now need is: what happens when you apply the Laplace transform to a *derivative*? The answer, derived from **integration by parts** (your soft prerequisite), is the formula that makes Laplace transforms the workhorse of ODE solving.

Apply integration by parts to L{f'(t)} = ∫₀^∞ f'(t)e^{−st} dt, with u = e^{−st} and dv = f'(t) dt. Then du = −se^{−st} dt and v = f(t), giving: [f(t)e^{−st}]₀^∞ + s∫₀^∞ f(t)e^{−st} dt. The boundary term evaluates to 0 − f(0) (assuming f(t) doesn't grow too fast), and the integral is exactly F(s). Result: **L{f'(t)} = sF(s) − f(0)**. Differentiation in the time domain becomes multiplication by s in the s-domain, with an initial condition subtracted. Applying this formula a second time to f''(t) = (f')'(t) gives **L{f''(t)} = s²F(s) − sf(0) − f'(0)**, and the pattern continues: each differentiation adds a factor of s and "peels off" one more initial condition.

This is the core reason Laplace transforms are powerful for initial value problems. An ODE like y'' + 3y' + 2y = eˡ with y(0) = 0, y'(0) = 1 transforms into (s²Y − s·0 − 1) + 3(sY − 0) + 2Y = 1/(s−1). The left side, after collecting terms, is (s² + 3s + 2)Y − 1. Solving for Y(s) is now purely **algebra**: Y(s) = (1 + 1/(s−1)) / (s² + 3s + 2). Partial fraction decomposition followed by inverse transform gives the solution. The differential equation — previously requiring the method of undetermined coefficients or variation of parameters — reduces to polynomial arithmetic.

The integration formula L{∫₀ᵗ f(τ) dτ} = F(s)/s is the symmetric partner. Just as differentiation multiplies by s, integration divides by s. This duality (s ↔ multiplication, 1/s ↔ integration) is a formal parallel to the derivative/integral relationship from calculus, but now entirely algebraic in the s-domain. Together these formulas make the Laplace transform a full **operational calculus**: the operations of differentiation and integration on functions become multiplication and division on their transforms, letting you manipulate ODEs as if they were ordinary equations.
