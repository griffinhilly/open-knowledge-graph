---
id: eigenfunction-expansions-sturm-liouville
title: Eigenfunction Expansions and Sturm-Liouville Theory
domain: mathematics
course: partial-differential-equations
prerequisites:
- id: separation-variables-pde
  type: hard
- id: fourier-series-definition
  type: hard
- id: eigenvalue-method-for-systems
  type: soft
tags: [pde, sturm-liouville, eigenfunction, spectral, orthogonal-expansion]
stage: advanced
status: validated
---
# Eigenfunction Expansions and Sturm-Liouville Theory

## Core Idea
Sturm-Liouville theory generalizes Fourier series by showing that a wide class of second-order boundary value problems -(p(x)y')' + q(x)y = λw(x)y produce an orthogonal basis of eigenfunctions for an appropriate function space. Any sufficiently well-behaved function can be expanded in this eigenbasis, just as functions can be expanded in sines and cosines. This framework unifies the separation of variables technique: when a PDE is separated, the spatial part typically yields a Sturm-Liouville problem whose eigenfunctions provide the building blocks for the solution.

## Questions
```yaml
- question: "In a regular Sturm-Liouville problem, what is guaranteed about the eigenvalues?"
  type: multiple-choice
  options:
    - "They form an increasing sequence tending to infinity, and are all real"
    - "They are all positive"
    - "They are complex conjugate pairs"
    - "There are finitely many"
  answer: 0
  explanation: "Regular Sturm-Liouville problems have countably many real eigenvalues λ₁ < λ₂ < λ₃ < ... → ∞. This follows from the self-adjointness of the Sturm-Liouville operator in a weighted L² space."
- question: "Eigenfunctions corresponding to distinct eigenvalues of a Sturm-Liouville problem are orthogonal with respect to the weight function w(x)."
  type: true-false
  answer: true
  explanation: "The orthogonality ∫ φ_m(x)φ_n(x)w(x)dx = 0 for m ≠ n follows from the self-adjointness of the operator. This generalizes the orthogonality of sin(nπx/L) that appears in Fourier series, which is the Sturm-Liouville problem y'' = -λy with w(x) = 1."
- question: "What classical special functions arise as eigenfunctions of Sturm-Liouville problems?"
  type: short-answer
  answer: "Legendre polynomials, Bessel functions, Hermite polynomials, Laguerre polynomials, and Chebyshev polynomials"
  explanation: "Each of these arises from a Sturm-Liouville problem on an appropriate interval with specific coefficient functions p(x), q(x), and w(x). They form orthogonal bases for function spaces relevant to problems with spherical, cylindrical, or other specific geometries."
- question: "The nth eigenfunction of a regular Sturm-Liouville problem has exactly n-1 zeros in the interior of the interval."
  type: true-false
  answer: true
  explanation: "This is the Sturm oscillation theorem: the eigenfunction φ_n corresponding to the nth eigenvalue λ_n has exactly n-1 interior zeros. Higher eigenvalues correspond to more oscillatory eigenfunctions, generalizing the fact that sin(nπx/L) has n-1 zeros in (0,L)."
```

## Explainer
Sturm-Liouville theory provides the spectral framework that underlies the separation of variables method for PDEs. When we separate variables in the heat equation on a finite interval, the spatial part satisfies X'' + λX = 0 with boundary conditions—the simplest Sturm-Liouville problem. Its eigenfunctions sin(nπx/L) form an orthogonal basis, and the solution is a Fourier sine series with time-dependent coefficients that decay exponentially. Sturm-Liouville theory shows this is not a coincidence but a general phenomenon.

A regular Sturm-Liouville problem has the form -(p(x)y')' + q(x)y = λw(x)y on [a,b] with separated boundary conditions, where p > 0, w > 0, and all coefficients are continuous. The operator L[y] = -(py')' + qy is self-adjoint with respect to the weighted inner product ⟨f,g⟩ = ∫f(x)g(x)w(x)dx. Self-adjointness guarantees that all eigenvalues are real, eigenfunctions for distinct eigenvalues are orthogonal, and the eigenvalues form an unbounded increasing sequence. The eigenfunctions form a complete orthonormal basis for L²([a,b], w).

The completeness of the eigenfunctions means that any square-integrable function f can be expanded as f(x) = Σ c_n φ_n(x), where the coefficients are c_n = ⟨f, φ_n⟩/⟨φ_n, φ_n⟩. This expansion converges in the L² sense, and under additional smoothness assumptions on f, it converges uniformly. This is the generalized Fourier series, and it reduces to ordinary Fourier series when p = w = 1 and q = 0. Different choices of p, q, and w yield expansions in Legendre polynomials (spherical geometry), Bessel functions (cylindrical geometry), and other classical families.

Singular Sturm-Liouville problems arise when p vanishes at an endpoint, the interval is infinite, or the coefficients are unbounded. These require more delicate analysis but remain tractable. The Bessel equation and Legendre equation are singular Sturm-Liouville problems, and their eigenfunction expansions (Fourier-Bessel series and Legendre series) are essential for solving PDEs in cylindrical and spherical coordinates. The general spectral theorem for unbounded self-adjoint operators in Hilbert spaces provides the rigorous foundation for these expansions, connecting Sturm-Liouville theory to functional analysis.
