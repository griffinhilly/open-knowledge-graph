---
id: frobenius-method
title: Frobenius Method and Equations with Singular Points
domain: mathematics
course: differential-equations
prerequisites:
- id: power-series-solutions
  type: hard
- id: continuity-definition
  type: soft
builds-toward:
- bessel-functions
- legendre-equations
tags:
- frobenius-method
- singular-points
- series-solution
stage: advanced
status: draft
---

# Frobenius Method and Equations with Singular Points

## Core Idea
For regular singular points where (x-x₀)p and (x-x₀)²q are analytic in y'' + p(x)y' + q(x)y = 0, the Frobenius method seeks y = (x-x₀)^r Σ aₙ(x-x₀)^n. Substituting yields an indicial equation for r and a recurrence relation for coefficients. Two independent solutions typically arise from different indicial roots. This method extends power series to a broader class of important equations.

## Questions

```yaml
- question: "You apply the Frobenius method to a second-order ODE with a regular singular point at x = 0 and find indicial roots r₁ = 3 and r₂ = 1/2. What can you conclude about the structure of the general solution near x = 0?"
  type: multiple-choice
  options:
    - "Only r₁ = 3 yields a valid solution; r₂ = 1/2 must be discarded since non-integer exponents are not permitted"
    - "Both r₁ = 3 and r₂ = 1/2 yield independent Frobenius series solutions, since their difference (5/2) is not a non-negative integer"
    - "The solution for r₂ = 1/2 requires a logarithmic factor because it is a fractional exponent"
    - "Both roots must be combined into a single series of the form x^(7/2) Σ aₙxⁿ"
  answer: 1
  explanation: "The key theorem: when r₁ − r₂ is NOT a non-negative integer, both indicial roots independently produce valid, independent Frobenius series solutions. Here r₁ − r₂ = 5/2, which is not a non-negative integer, so both y₁ = x³ Σ aₙxⁿ and y₂ = x^(1/2) Σ bₙxⁿ are valid solutions. Non-integer exponents are perfectly allowed — the Frobenius method exists precisely to handle cases where r is not a whole number. Logarithmic terms arise only when r₁ = r₂ (equal roots), or when r₁ − r₂ is a positive integer AND the recurrence for r₂ breaks down. Fractional exponents alone (option C) do not require logarithms."

- question: "A second-order ODE y'' + p(x)y' + q(x)y = 0 has a singular point at x = 2. Which condition makes x = 2 a regular (rather than irregular) singular point?"
  type: multiple-choice
  options:
    - "(x−2)p(x) and (x−2)²q(x) are both analytic (expandable as convergent power series) near x = 2"
    - "p(x) and q(x) are both analytic at x = 2, meaning they have no singularity there"
    - "The indicial roots at x = 2 are both non-negative integers"
    - "The solution y is bounded near x = 2"
  answer: 0
  explanation: "A singular point x₀ is regular if the singularities in p(x) and q(x) are 'mild enough': specifically, (x − x₀)p(x) must be analytic and (x − x₀)²q(x) must be analytic near x₀. This means p(x) can blow up at most like 1/(x − x₀) and q(x) at most like 1/(x − x₀)². If the singularities are worse (p(x) blowing up faster than 1/(x − x₀)), the point is an irregular singular point, and the Frobenius method does not apply. If p and q were analytic at x₀ (option B), it would be an ordinary point, not a singular point at all — the standard power series method would apply directly."

- question: "The Frobenius method can be applied at any singular point of a second-order linear ODE to find series solutions."
  type: true-false
  answer: false
  explanation: "The Frobenius method applies only at regular singular points, not at irregular (essential) singular points. At an irregular singular point, the coefficients blow up too severely for the Frobenius ansatz y = (x − x₀)^r Σ aₙ(x − x₀)^n to produce a valid series solution. Solutions near irregular singular points may involve essential singularities, Stokes phenomena, and divergent asymptotic series — topics in advanced analysis far beyond the Frobenius framework. The classification of singular points (ordinary, regular singular, irregular singular) is the first step in any series solution strategy, since it determines which method applies."

- question: "The indicial equation in the Frobenius method arises by substituting the series ansatz into the ODE and collecting the coefficient of the lowest-power term, yielding a quadratic equation whose roots determine the allowed values of the leading exponent r."
  type: true-false
  answer: true
  explanation: "When the Frobenius series y = Σ aₙx^(n+r) is substituted into the ODE, the coefficient of the lowest-power term (typically x^(r−2) for a second-order equation with a regular singular point at 0) involves only the leading coefficient a₀ and r itself. Setting this coefficient to zero with a₀ ≠ 0 gives the indicial equation — a quadratic in r. Its two roots r₁ and r₂ (conventionally r₁ ≥ r₂) determine the possible leading behaviors of solutions near the singular point. This is fundamentally different from ordinary-point power series, where r = 0 is forced and no such equation arises."

- question: "What makes a singular point 'regular' rather than 'irregular,' and why does this classification determine whether the Frobenius method can be applied?"
  type: short-answer
  answer: "A singular point x₀ is regular if (x − x₀)p(x) and (x − x₀)²q(x) are both analytic near x₀ — meaning the coefficient functions blow up no faster than 1/(x − x₀) and 1/(x − x₀)² respectively. This growth condition guarantees that when you multiply through by (x − x₀)², the equation takes a form amenable to series expansion with a fractional power leading behavior. At an irregular singular point, the coefficients grow too fast, and the Frobenius ansatz — a power series multiplied by a single power (x − x₀)^r — cannot capture the full solution behavior, which may involve essential singularities or exponentially diverging terms. The Frobenius theorem provides a guarantee of convergence and completeness of solutions only at regular singular points."
  explanation: "The intuition is that regular singular points have 'manageable' bad behavior — the singularity in p or q is at worst a simple pole. The (x − x₀)² factor in the definition of regularity for q(x) comes from the ODE structure: multiplying y'' + p(x)y' + q(x)y = 0 by (x − x₀)² gives (x − x₀)²y'' + [(x − x₀)²p(x)]y' + [(x − x₀)²q(x)]y = 0. If both bracketed quantities are analytic, you have a regular singular equation whose series behavior is well-controlled. Bessel's equation x²y'' + xy' + (x² − ν²)y = 0 is the archetypal example: dividing by x² gives p(x) = 1/x and q(x) = 1 − ν²/x², and xp(x) = 1 and x²q(x) = x² − ν² are both analytic at x = 0."
```

## Explainer

You've already learned to solve ODEs near ordinary points using power series: substitute y = Σ aₙ(x - x₀)^n, plug into the equation, and match coefficients to find a recurrence. But many of the most important equations in physics — Bessel's equation, Legendre's equation, the hypergeometric equation — have **singular points** where p(x) or q(x) blow up and the plain power series method fails. The Frobenius method extends the idea to handle a special, well-behaved class of singularities called **regular singular points**.

A singular point x₀ is **regular** if the coefficients satisfy a specific growth condition: (x - x₀)p(x) and (x - x₀)²q(x) must both be analytic (expandable as convergent power series) near x₀. Intuitively, the singularity can't be too bad — p(x) can blow up like 1/(x - x₀) and q(x) like 1/(x - x₀)², but not faster. When this condition holds, you're guaranteed at least one solution of the **Frobenius form**: y = (x - x₀)^r Σₙ₌₀^∞ aₙ(x - x₀)^n. The exponent r is now a free parameter — not necessarily an integer — that the equation itself will determine. Plain power series correspond to r = 0; the Frobenius method lets r be any real (or even complex) number.

The procedure starts by substituting the Frobenius series into the ODE. Collecting the lowest-power term gives you the **indicial equation**: a quadratic in r whose roots r₁ ≥ r₂ are the two candidate exponents. The larger root r₁ always yields a valid Frobenius series. Whether the smaller root r₂ gives a second independent Frobenius series or requires a logarithmic term depends on r₁ - r₂: if it is not a non-negative integer, both roots give distinct Frobenius series; if r₁ = r₂ or r₁ - r₂ is a positive integer, the second solution involves ln(x - x₀) multiplied by a Frobenius series. Once r is fixed, the coefficients aₙ satisfy a recurrence relation obtained by equating each power's coefficient to zero.

The Frobenius method reveals why Bessel's equation x²y'' + xy' + (x² - ν²)y = 0 has solutions of the form x^ν times a power series: x = 0 is a regular singular point with indicial roots r = ±ν. The **Bessel functions** Jₙ(x) you'll encounter next are precisely these Frobenius solutions, built coefficient-by-coefficient from the recurrence. The method acts as a bridge — it explains the unusual non-integer power behavior of important special functions and provides a systematic algorithm for computing them to any desired order, making it indispensable across mathematical physics and engineering.
