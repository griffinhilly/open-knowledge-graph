---
id: power-series-solutions-to-odes
title: Power Series Solutions to Differential Equations
domain: mathematics
course: differential-equations
prerequisites:
- id: power-series
  type: hard
- id: second-order-linear-homogeneous-odes
  type: hard
builds-toward:
- ordinary-and-singular-points
- frobenius-method
tags:
- series
- method
- special-functions
stage: formal-systems
status: validated
---

# Power Series Solutions to Differential Equations

## Core Idea
For ODEs that don't have elementary closed-form solutions, assume a power series solution y = Σ(a_n·x^n) and substitute into the ODE to find a recurrence relation for coefficients a_n. This yields convergent power series solutions valid near x = 0.

## How It's Best Learned
Work through Airy's equation or Bessel's equation. Substitute y = Σ(a_n·x^n) and y' = Σ(n·a_n·x^{n-1}), then collect powers of x and equate coefficients to zero.

## Common Misconceptions
- Confusing power series solutions with Taylor series approximations; they are exact within their radius of convergence. - Not recognizing the radius of convergence limitations. - Making algebra errors when equating coefficients of like powers.

## Questions

```yaml
- question: "A student solves y'' + y = 0 using the power series method and obtains an infinite series solution. They conclude: 'This is just an approximation — it gets more accurate as you include more terms.' What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "The student should have recognized the series as exactly cos(x) and sin(x) without generating additional terms"
    - "Within the radius of convergence, the power series satisfies the ODE exactly at every point — it is not an approximation but an exact solution expressed in series form"
    - "The student needs to prove convergence before making any accuracy claim"
    - "The series only becomes exact after infinitely many terms, making it approximate for any finite computation"
  answer: 1
  explanation: "A power series solution is exact within its radius of convergence, not an approximation. The confusion arises from Taylor series truncation, where you cut off terms to get a finite approximation. The power series method is different: the full infinite series satisfies the ODE at every x within the convergence interval. Truncating it for numerical computation introduces approximation error, but the method itself yields an exact solution — in this case, the Taylor series for cos(x) and sin(x)."

- question: "After substituting y = Σa_n·x^n into an ODE and collecting terms by power of x, a student arrives at the condition (m+2)(m+1)a_{m+2} + a_m = 0 for each non-negative integer m. What is this equation, and what does it enable?"
  type: multiple-choice
  options:
    - "It is the characteristic equation; solving for m gives the two independent solutions directly"
    - "It is a recurrence relation; it expresses each coefficient a_{m+2} in terms of a_m, allowing the entire solution to be built coefficient by coefficient from two free parameters a₀ and a₁"
    - "It is a convergence condition; verifying it for all m proves the series converges"
    - "It is an error bound; it tells you how many terms are needed before the series is accurate enough"
  answer: 1
  explanation: "The recurrence relation is the heart of the power series method. Setting each coefficient of x^m equal to zero (since a power series is identically zero only when all its coefficients vanish) gives a formula expressing each new coefficient in terms of earlier ones. The two free parameters a₀ and a₁ play the role of initial conditions, and the recurrence determines every subsequent coefficient from them. This is why a second-order ODE always generates two linearly independent power series solutions."

- question: "The power series method provides an exact solution to a differential equation within the radius of convergence — not a finite approximation that improves with more terms."
  type: true-false
  answer: true
  explanation: "Within the radius of convergence, the full infinite series satisfies the ODE at every point. This is distinct from truncated Taylor approximations, which are approximations by design. The power series method identifies the exact solution and represents it as an infinite series; it happens that for y'' + y = 0 this series is the familiar cos(x) and sin(x). For equations like Airy's y'' − xy = 0, no simpler form exists — the infinite series is the solution."

- question: "The power series method only applies to ODEs with variable coefficients; it cannot be used for equations like y'' − 4y = 0 that have constant coefficients."
  type: true-false
  answer: false
  explanation: "The power series method works on constant-coefficient ODEs just as well as variable-coefficient ones — it simply produces more work than the characteristic equation method, which is the efficient approach for constant coefficients. Applying the power series method to y'' − 4y = 0 correctly recovers the solutions as the Taylor series for e^(2x) and e^(-2x). The method is general; its distinctive value is for equations where the characteristic equation trick does not apply, such as Airy's equation or Bessel's equation."

- question: "Why does the power series method require x = 0 to be an ordinary point of the ODE, and what goes wrong at a singular point?"
  type: short-answer
  answer: "At an ordinary point, the coefficient functions are analytic (have valid Taylor series), so the ODE behaves regularly and a solution of the form y = Σa_n·x^n converges. The substitution, re-indexing, and coefficient-matching all work cleanly. At a singular point, the leading coefficient of y'' vanishes, making the equation degenerate — the solution may require fractional powers of x, logarithmic terms, or may not converge at all in the standard power series form. The Frobenius method generalizes the approach by assuming y = x^r·Σa_n·x^n and determining the indicial exponent r from the equation."
  explanation: "The radius of convergence of the power series solution is determined by the distance to the nearest singular point of the ODE's coefficients. Near an ordinary point, everything is analytic and the series machinery works. Near a singular point, the solution's behavior changes qualitatively — it may blow up, oscillate faster and faster, or have a branch-point structure — and the simple Σa_n·x^n ansatz cannot capture this. Identifying ordinary versus singular points before applying the method is the first step in any power series analysis."
```

## Explainer

You know how to solve second-order linear ODEs with constant coefficients using the characteristic equation — assuming exponential solutions works because eˣ is its own derivative. But many important ODEs have **variable coefficients**, where the multipliers on y'', y', and y depend on x. An example is Airy's equation y'' − xy = 0, which governs quantum tunneling and optics. The characteristic equation trick doesn't apply. The **power series method** is the systematic approach: assume the solution is an infinite polynomial and determine the coefficients by substituting into the ODE.

The assumption is y = a₀ + a₁x + a₂x² + a₃x³ + ... = Σₙ₌₀^∞ aₙxⁿ. Within its radius of convergence, a power series can be differentiated term by term: y' = Σₙ₌₁^∞ naₙxⁿ⁻¹ and y'' = Σₙ₌₂^∞ n(n−1)aₙxⁿ⁻². You substitute these series into the ODE, collect all terms containing the same power of x, and require each coefficient to be zero (since a power series is identically zero only if all its coefficients vanish). This produces a **recurrence relation**: a formula expressing each aₙ in terms of earlier coefficients, letting you compute the solution one coefficient at a time.

As a worked example, consider y'' + y = 0. Substituting gives Σₙ₌₂^∞ n(n−1)aₙxⁿ⁻² + Σₙ₌₀^∞ aₙxⁿ = 0. Re-index the first sum with m = n−2 so both sums run over xᵐ: Σₘ₌₀^∞ [(m+2)(m+1)aₘ₊₂ + aₘ] xᵐ = 0. Setting each bracket to zero gives the recurrence aₘ₊₂ = −aₘ / [(m+2)(m+1)]. Starting from free parameters a₀ and a₁, this generates two independent series: one involving only even powers (the Taylor series for cos x) and one involving only odd powers (the Taylor series for sin x). The power series method has re-derived a result you already know — but it works equally well on equations like Airy's where no closed form in elementary functions exists.

The series solution is exact, not an approximation: within its **radius of convergence**, the power series satisfies the ODE at every point. The radius of convergence is determined by the nearest singularity of the coefficient functions — if the variable coefficients are analytic everywhere (like a polynomial), the series may converge for all x. The method fails at **singular points** of the ODE — values of x where the leading coefficient vanishes or the equation becomes irregular. Handling those cases requires the Frobenius method, where you generalize the power series assumption to allow non-integer powers of x. For now, the ordinary point case (coefficients analytic near x = 0) is the foundation you need.
