---
id: characteristic-equation-method
title: Characteristic Equation Method for Linear ODEs
domain: mathematics
course: differential-equations
prerequisites:
- id: second-order-linear-homogeneous-odes
  type: hard
- id: quadratic-formula
  type: hard
builds-toward:
- complex-roots-oscillatory-solutions
- repeated-roots-reduction-of-order
tags:
- characteristic-equation
- constant-coefficients
- solution-method
stage: formal-systems
status: validated
---

# Characteristic Equation Method for Linear ODEs

## Core Idea
For constant-coefficient linear ODEs, assume a solution y = e^(rx) and substitute to obtain a characteristic equation. For y'' + py' + qy = 0, the characteristic equation is r² + pr + q = 0. The roots r determine the solution form: distinct real roots give y = c₁e^(r₁x) + c₂e^(r₂x); complex roots give oscillatory solutions; repeated roots require x factors. This algebraic approach elegantly solves a wide class of equations.

## Questions

```yaml
- question: "The characteristic equation of a 2nd-order ODE has a repeated root r = -3. What is the general solution?"
  type: multiple-choice
  options:
    - "y = c₁e^(-3x) + c₂e^(-3x), since both roots are -3"
    - "y = (c₁ + c₂x)e^(-3x), since repeated roots require an x factor in the second solution"
    - "y = e^(-3x)(c₁cos(3x) + c₂sin(3x)), since repeated roots produce oscillatory behavior"
    - "y = c₁e^(-3x) alone, since the two identical roots yield only one independent solution"
  answer: 1
  explanation: "Two copies of e^(-3x) are linearly dependent — they are the same function and cannot span the solution space. The fix is to multiply one by x: xe^(-3x) is linearly independent from e^(-3x) and still satisfies the ODE. Option A writes two identical terms, which is just c₁+c₂ times one solution. Option C incorrectly applies the complex-root formula. Option D is incomplete — a 2nd-order ODE always needs two independent solutions."

- question: "A characteristic equation has roots r = 2 ± 3i. What will the solution look like for large x?"
  type: multiple-choice
  options:
    - "It will oscillate with constant amplitude, like a pure undamped sine wave"
    - "It will decay to zero, since complex roots always produce damped oscillations"
    - "It will oscillate with exponentially growing amplitude"
    - "It will approach a constant steady-state value"
  answer: 2
  explanation: "Complex roots α ± βi give solutions e^(αx)(c₁cos(βx) + c₂sin(βx)). Here α = 2 > 0, so the amplitude grows as e^(2x) — without bound. Constant amplitude (option A) requires α = 0; decay (option B) requires α < 0. The imaginary part β = 3 controls oscillation frequency only."

- question: "The characteristic equation method works by substituting y = e^(rx) into the ODE, which allows e^(rx) to be divided out, leaving a polynomial equation in r alone."
  type: true-false
  answer: true
  explanation: "Substituting y = e^(rx) gives (r² + pr + q)e^(rx) = 0. Since e^(rx) is never zero, we divide both sides by it, reducing the differential equation to the algebraic characteristic equation r² + pr + q = 0. This is how the method converts a calculus problem into an algebra problem solvable with the quadratic formula."

- question: "If the characteristic equation of a 2nd-order ODE with real coefficients has complex roots, the ODE has no real-valued solutions."
  type: true-false
  answer: false
  explanation: "Complex roots always come in conjugate pairs (α ± βi) when the ODE has real coefficients. Euler's formula lets us combine the complex exponentials into real-valued solutions: e^(αx)cos(βx) and e^(αx)sin(βx). Complex roots indicate oscillatory behavior, not the absence of real solutions."

- question: "What is the key insight that allows the characteristic equation method to turn a differential equation into an algebra problem?"
  type: short-answer
  answer: "The exponential function e^(rx) is the only function whose derivatives are scalar multiples of itself: y′ = re^(rx), y″ = r²e^(rx). Substituting collapses all differentiation into scalar multiplication, so e^(rx) factors out completely, leaving a polynomial in r."
  explanation: "This is what makes e^(rx) the right ansatz. Any other function guess — a polynomial, sin, etc. — would not collapse the equation so cleanly. Because exponents compose multiplicatively under differentiation, the characteristic equation method reduces the hardest part (solving a differential equation) to something you already know: the quadratic formula."
```

## Explainer

You know from second-order linear ODEs that the general solution to y″ + py′ + qy = 0 is a linear combination of two independent solutions. The characteristic equation method is the systematic algorithm for finding those two solutions when p and q are constants. The key insight is an inspired guess, or **ansatz**: if we try y = e^(rx), then y′ = re^(rx) and y″ = r²e^(rx). Substituting into the equation gives r²e^(rx) + pre^(rx) + qe^(rx) = 0. Factor out e^(rx) — which is never zero — and you get r² + pr + q = 0. The differential equation has become a quadratic.

This quadratic, called the **characteristic equation**, is solved with the quadratic formula you already know. The roots r₁ and r₂ determine the solution form, and there are three cases based on the discriminant p² − 4q:

- **Two distinct real roots** (p² − 4q > 0): The two independent solutions are e^(r₁x) and e^(r₂x), giving y = c₁e^(r₁x) + c₂e^(r₂x). Each root contributes its own exponential.
- **Complex conjugate roots** r = α ± βi (p² − 4q < 0): The complex exponentials e^((α+βi)x) and e^((α−βi)x) are valid, but we can use Euler's formula to rewrite them in real form: y = e^(αx)(c₁cos(βx) + c₂sin(βx)). This is the oscillatory case — the solution is a sinusoid with exponentially growing or decaying amplitude.
- **Repeated root** r₁ = r₂ = r (p² − 4q = 0): Two copies of e^(rx) are not independent, so e^(rx) alone cannot span the solution space. The second independent solution is xe^(rx), giving y = (c₁ + c₂x)e^(rx).

The elegance of this method is that it converts a calculus problem into a purely algebraic one. The structure of the ODE's solutions — exponential growth or decay, oscillation, polynomial growth — is entirely encoded in the location of the characteristic roots in the complex plane. Roots with large negative real parts decay fast; purely imaginary roots oscillate without damping; roots with positive real parts grow without bound. This geometric picture of roots predicting behavior is the foundation for understanding stability in differential equations and control systems.
