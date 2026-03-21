---
id: legendre-polynomials-and-equations
title: Legendre Polynomials and Legendre's Equation
domain: mathematics
course: differential-equations
prerequisites:
- id: frobenius-method
  type: hard
builds-toward:
- separation-of-variables-for-pdes
tags:
- special-functions
- legendre
- orthogonal
stage: advanced
status: draft
---

# Legendre Polynomials and Legendre's Equation

## Core Idea
Legendre's equation (1 - x²)y'' - 2xy' + n(n+1)y = 0 admits polynomial solutions P_n(x) when n is a non-negative integer. These Legendre polynomials form an orthogonal basis on [-1, 1] and arise in problems with spherical symmetry, particularly in solving Laplace's equation.

## How It's Best Learned
Compute the first few Legendre polynomials (P₀ = 1, P₁ = x, P₂ = (3x² - 1)/2) using the Frobenius method or Rodrigues' formula. Verify orthogonality: ∫₋₁¹ P_m(x)P_n(x) dx = 0 for m ≠ n.

## Questions

```yaml
- question: "When separating variables in Laplace's equation ∇²u = 0 in spherical coordinates with azimuthal symmetry, you obtain Legendre's equation for the polar angle part. What forces the angular solutions to be Legendre polynomials rather than the general (divergent) series solutions?"
  type: multiple-choice
  options:
    - "The Frobenius method automatically produces polynomial solutions for all values of the separation constant"
    - "The requirement that the solution remain finite at the poles (cos θ = ±1) forces the series to terminate, which only happens when n is a non-negative integer"
    - "Physical problems always require periodic solutions, and Legendre polynomials are the periodic solutions of the equation"
    - "Boundary conditions at large r select the polynomial solutions over the divergent ones"
  answer: 1
  explanation: "At the poles of the sphere, cos θ = ±1, which correspond to x = ±1 in Legendre's equation — the singular points. The general Frobenius series solution diverges at x = ±1 unless n is a non-negative integer, which causes the recurrence to terminate after finitely many terms, producing a polynomial. Physically, a divergent u at the poles is unacceptable (it would mean infinite potential at the north and south poles). This physical regularity condition discretizes the problem and selects only the Legendre polynomials P_n."

- question: "What happens when you attempt to solve Legendre's equation with n = 1/2 (not a non-negative integer)?"
  type: multiple-choice
  options:
    - "The equation has no solutions at all"
    - "The Frobenius method produces two polynomial solutions, but they don't satisfy orthogonality"
    - "The Frobenius method produces two infinite series solutions, both of which diverge at x = ±1"
    - "The solution is a trigonometric function rather than a polynomial"
  answer: 2
  explanation: "When n is not a non-negative integer, the recurrence relation never terminates — neither Frobenius series becomes a polynomial. Both solutions are infinite series, and both diverge at the singular points x = ±1. This is why non-integer n is physically inadmissible for problems on a closed interval [−1, 1]: there is no acceptable bounded solution. The discreteness of the eigenvalues n = 0, 1, 2, 3, … is not imposed artificially but arises from the requirement that solutions stay bounded at the endpoints."

- question: "The Legendre polynomial P₄(x) is an even function of x."
  type: true-false
  answer: true
  explanation: "Even-index Legendre polynomials contain only even powers of x and are therefore even functions: P_n(−x) = P_n(x) for even n. Odd-index polynomials contain only odd powers and are odd functions. This parity pattern follows directly from the structure of the recurrence relation, which links coefficients two steps apart, causing the series to separate into a part with only even powers and a part with only odd powers. P₄(x) = (35x⁴ − 30x² + 3)/8 contains only even powers, confirming even symmetry."

- question: "The orthogonality of Legendre polynomials — that ∫₋₁¹ P_m(x)P_n(x)dx = 0 for m ≠ n — must be verified by computing the integral directly for each pair."
  type: true-false
  answer: false
  explanation: "Orthogonality follows automatically from the Sturm-Liouville structure of the equation. Legendre's equation can be written as (d/dx)[(1−x²)y'] + n(n+1)y = 0, a self-adjoint eigenvalue problem. A general theorem guarantees that eigenfunctions of a self-adjoint operator corresponding to distinct eigenvalues are orthogonal. Since P_m and P_n correspond to eigenvalues m(m+1) ≠ n(n+1) for m ≠ n, their orthogonality is guaranteed by the theorem without any calculation. This is more powerful than case-by-case verification."

- question: "Why does the physical requirement that a solution to Laplace's equation be finite at the poles of a sphere force the separation constant n to be a non-negative integer, rather than allowing any real value?"
  type: short-answer
  answer: "The poles correspond to x = cos θ = ±1, the singular points of Legendre's equation. For general (non-integer) values of n, the Frobenius power series solution does not terminate and diverges at x = ±1. A divergent solution represents infinite potential at the poles, which is physically inadmissible. The only way to obtain a bounded solution at both endpoints is to choose n such that the recurrence terminates — and this happens precisely when n is a non-negative integer, yielding the Legendre polynomials. The physics selects the discrete eigenvalue sequence."
  explanation: "This is the conceptual core of why Legendre polynomials arise in physics: it is not that we 'choose' to use polynomials for convenience, but that polynomial solutions are the only mathematically acceptable ones given the physical boundary condition. The discretization of the eigenvalues (n = 0, 1, 2, …) is a consequence of the boundary condition, not an arbitrary restriction. The same pattern — boundary conditions quantizing a continuous parameter — recurs throughout mathematical physics."
```

## Explainer

You know the Frobenius method for ODEs near regular singular points. Legendre's equation (1−x²)y'' − 2xy' + n(n+1)y = 0 has a different structure: it is singular at x = ±1 but regular on the open interval (−1, 1) including at x = 0. Applying Frobenius at x = 0 produces a power series solution with a recurrence relation linking each coefficient to the one two steps back. The critical observation is that when n is a non-negative integer, the recurrence forces the coefficient of x^(n+2) to vanish — the series *terminates* after finitely many terms and becomes a polynomial. These terminating solutions, normalized so P_n(1) = 1, are the **Legendre polynomials**.

The first few are P₀ = 1, P₁ = x, P₂ = (3x²−1)/2, P₃ = (5x³−3x)/2. Notice the alternating parity: even-index P_n are even functions, odd-index are odd, directly reflecting the structure of the recurrence. When n is *not* a non-negative integer, neither Frobenius series terminates, and both solutions diverge at x = ±1 — making them unacceptable for physical problems on a closed interval. The requirement that solutions be finite at the endpoints *forces* n to be a non-negative integer, which is why the eigenvalues n(n+1) = 0, 2, 6, 12, 20, … form a discrete sequence.

The Legendre polynomials are **orthogonal on [−1, 1]**: ∫₋₁¹ P_m(x)P_n(x) dx = 0 for m ≠ n, and ∫₋₁¹ [P_n(x)]² dx = 2/(2n+1). This orthogonality is guaranteed by the **Sturm-Liouville structure** of Legendre's equation — it can be written as (d/dx)[(1−x²)y'] + n(n+1)y = 0, a self-adjoint eigenvalue problem. A general theorem says eigenfunctions of a self-adjoint operator with distinct eigenvalues are always orthogonal, so the P_n must be orthogonal without any computation. The result is that any "well-behaved" function f on [−1, 1] can be expanded as f(x) = Σ cₙ P_n(x), with cₙ = (2n+1)/2 ∫₋₁¹ f(x) P_n(x) dx.

The application that drives all of this is **Laplace's equation in spherical coordinates**. When you separate variables in ∇²u = 0, the angular part in the polar direction (colatitude θ) becomes Legendre's equation in x = cos θ. The demand that u be finite at the poles (cos θ = ±1, i.e., x = ±1) restricts solutions to the Legendre polynomials, and the general solution for problems with azimuthal symmetry is u(r, θ) = Σ (Aₙrⁿ + Bₙr^(−n−1)) P_n(cos θ). Legendre polynomials play the same role in spherical geometry that Fourier modes play in rectangular geometry: they are the natural "basis functions" for decomposing any spherically symmetric field.
