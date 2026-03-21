---
id: legendre-equations
title: Legendre Equations and Legendre Polynomials
domain: mathematics
course: differential-equations
prerequisites:
- id: frobenius-method
  type: hard
builds-toward:
- fourier-series-definition
tags:
- legendre-polynomials
- special-functions
- orthogonal
stage: advanced
status: draft
---

# Legendre Equations and Legendre Polynomials

## Core Idea
Legendre's equation (1-x²)y'' - 2xy' + n(n+1)y = 0 has polynomial solutions P_n(x) for non-negative integers n. These arise in spherically symmetric problems and are orthogonal on [-1,1] with respect to the standard inner product. Legendre polynomials have generating functions, recurrence relations, and explicit formulas, forming the basis for Legendre expansions.

## Questions

```yaml
- question: "A student applies the Frobenius method to Legendre's equation with n = 1.5 (a non-integer) and finds a convergent power series solution on (−1, 1). Why is this solution problematic for physical applications in spherical geometry?"
  type: multiple-choice
  options:
    - "The series diverges everywhere because the Frobenius method requires integer parameters"
    - "A non-integer n produces an infinite series that diverges at x = ±1, making it unsuitable for spherical boundary conditions where solutions must remain bounded at the poles (θ = 0, π)"
    - "The recurrence relation cannot be applied when n is non-integer, so no solution can be computed"
    - "The solution is valid but cannot be orthogonalized, making expansion impossible"
  answer: 1
  explanation: "The endpoints x = ±1 correspond to the poles of a sphere (cos θ = ±1). Physical solutions must be bounded there. When n is a non-integer, the Frobenius series does not terminate — it continues as an infinite series that diverges at x = ±1. Only when n is a non-negative integer does the recurrence terminate (the coefficient aₙ₊₂ = 0 makes all subsequent terms vanish), producing a polynomial that is automatically bounded everywhere on [−1, 1]. This is why Legendre polynomials, not the general series solutions, appear in physical problems with spherical symmetry."

- question: "Why are Legendre polynomials useful for expanding arbitrary functions on [−1, 1]?"
  type: multiple-choice
  options:
    - "They are simple low-degree polynomials that approximate any smooth function accurately by Taylor's theorem"
    - "They satisfy the orthogonality condition ∫₋₁¹ Pₘ(x)Pₙ(x) dx = 0 for m ≠ n, which allows each expansion coefficient to be determined independently via the inner product without solving a coupled system"
    - "They form a complete basis only for polynomial functions, making them useful for polynomial interpolation"
    - "Their recurrence relation guarantees convergence of any partial sum to the target function"
  answer: 1
  explanation: "Orthogonality is the property that makes expansions tractable. If you write f(x) = Σ cₙ Pₙ(x) and multiply both sides by Pₘ(x) and integrate, all cross terms ∫ Pₙ Pₘ dx vanish for n ≠ m. Only the n = m term survives, giving an explicit formula: cₘ = [(2m+1)/2] ∫₋₁¹ f(x) Pₘ(x) dx. Each coefficient is determined independently. This is identical in structure to how Fourier coefficients work for trigonometric expansions. Without orthogonality, extracting individual coefficients would require solving an infinite coupled system."

- question: "Legendre polynomials arise as solutions to Legendre's equation specifically when n is a non-negative integer, because only then does the Frobenius power series terminate to give a polynomial."
  type: true-false
  answer: true
  explanation: "The recurrence relation for coefficients is aₖ₊₂ = −[n(n+1) − k(k+1)] / [(k+2)(k+1)] · aₖ. When n is a non-negative integer, the numerator n(n+1) − n(n+1) = 0 at k = n, making aₙ₊₂ = 0 and all subsequent coefficients vanish. The series terminates after n+1 terms, yielding a polynomial. For non-integer or negative n, no such termination occurs, and the general solution is an infinite series that diverges at the endpoints. The polynomial property is therefore not a convenient feature but a direct consequence of integer n."

- question: "The recurrence relation (n+1)Pₙ₊₁(x) = (2n+1)x Pₙ(x) − n Pₙ₋₁(x) requires re-deriving each Legendre polynomial from the power series in order to apply it correctly."
  type: true-false
  answer: false
  explanation: "The recurrence relation is precisely the tool that makes re-derivation unnecessary. Given P₀(x) = 1 and P₁(x) = x, you can compute any subsequent Pₙ algebraically: P₂ = (3x² − 1)/2, P₃ = (5x³ − 3x)/2, and so on, by applying the recurrence repeatedly. This is far more efficient than re-running the Frobenius series each time. The recurrence relation is one of Legendre polynomials' most practically useful properties, enabling rapid computation of arbitrarily high-degree polynomials from the initial two."

- question: "Explain why the termination of the Frobenius power series is critical to Legendre polynomials' usefulness, and what happens when n is not a non-negative integer."
  type: short-answer
  answer: "When n is a non-negative integer, the recurrence relation forces the coefficient aₙ₊₂ to zero, causing the infinite series to truncate into a polynomial of degree n. Polynomials are bounded everywhere on [−1, 1], including at the endpoints x = ±1 (the poles of a sphere). This boundedness is physically required — solutions to Laplace's equation in spherical coordinates must not diverge at the poles. When n is not a non-negative integer, the series does not terminate, remains an infinite series, and diverges at x = ±1, making it physically inadmissible for spherical problems. Termination is therefore the selection mechanism that picks out the physically meaningful solutions."
  explanation: "The deeper point is that the physical boundary condition (boundedness at the poles) and the mathematical property (series termination at integer n) are not independent — they are two descriptions of the same constraint. The mathematical structure of the Frobenius solution embeds the physics: only when n(n+1) is an eigenvalue of the Legendre operator do bounded solutions exist. This connection between eigenvalue problems and orthogonal polynomial families is the central pattern that recurs throughout mathematical physics (Hermite polynomials for the harmonic oscillator, Laguerre for the hydrogen atom, etc.)."
```

## Explainer

The Legendre equation arises naturally when you solve Laplace's equation ∇²φ = 0 in spherical coordinates and separate variables. The angular part of the solution leads to (1−x²)y'' − 2xy' + n(n+1)y = 0, where x = cos(θ) is the polar angle variable. This is a second-order linear ODE with non-constant coefficients and ordinary points everywhere on (−1, 1), so the **Frobenius method** you learned tells you to seek a power series solution y = Σ aₖxᵏ around x = 0.

Substituting into the equation and collecting powers of x gives a **recurrence relation**: aₖ₊₂ = −[n(n+1) − k(k+1)] / [(k+2)(k+1)] · aₖ. The series is determined by the choice of a₀ and a₁ (giving two independent solutions). Here is the key observation: if n is a non-negative integer, the recurrence terminates — the coefficient aₙ₊₂ = 0, and all subsequent coefficients vanish. The series becomes a **polynomial** of degree n. These terminating solutions are the **Legendre polynomials** P_n(x), normalized so P_n(1) = 1. The first few are: P₀(x) = 1, P₁(x) = x, P₂(x) = (3x²−1)/2, P₃(x) = (5x³−3x)/2.

The **orthogonality** of Legendre polynomials is what makes them useful: ∫₋₁¹ Pₘ(x)Pₙ(x) dx = 0 whenever m ≠ n. This mirrors how sine and cosine functions are orthogonal on [−π, π] — the key property that makes Fourier series work. Because Legendre polynomials are orthogonal, any reasonable function f on [−1, 1] can be expanded as f(x) = Σ cₙ Pₙ(x), where the coefficients are extracted by the inner product: cₙ = [(2n+1)/2] ∫₋₁¹ f(x) Pₙ(x) dx. This is a **Legendre expansion** — the spherical analogue of a Fourier series.

A practical tool is the **recurrence relation** between consecutive polynomials: (n+1)Pₙ₊₁(x) = (2n+1)x Pₙ(x) − n Pₙ₋₁(x). This lets you compute any Pₙ efficiently without re-deriving the series. Legendre polynomials appear throughout mathematical physics — gravitational and electrostatic potentials in spherical geometry, quantum mechanics of the hydrogen atom, and heat conduction on spheres — wherever physical symmetry makes spherical coordinates natural.
