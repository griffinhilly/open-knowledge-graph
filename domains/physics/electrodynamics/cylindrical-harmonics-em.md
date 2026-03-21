---
id: cylindrical-harmonics-em
title: Cylindrical Harmonics and Bessel Functions
domain: physics
course: electrodynamics
prerequisites:
- id: separation-variables-elliptic-equations
  type: hard
- id: boundary-value-problems-electrostatics
  type: hard
builds-toward:
- circular-waveguide-propagation
- waveguide-equations-general
tags:
- bessel-functions
- cylindrical-coordinates
- boundary-value-problems
stage: advanced
status: draft
---

# Cylindrical Harmonics and Bessel Functions

## Core Idea
Solutions to Laplace's equation in cylindrical coordinates involve Bessel functions of integer and half-integer order. These provide the natural eigenfunctions for cylindrical boundary value problems and waveguide mode analysis.

## Questions

```yaml
- question: "When solving Laplace's equation inside a solid cylinder (including the axis r = 0), why is the Neumann function Y_n(kr) discarded as a basis function?"
  type: multiple-choice
  options:
    - "Y_n oscillates too rapidly near the center, violating the boundary condition at r = 0"
    - "Y_n diverges as r → 0, making the field infinite at the cylinder axis, which has no physical justification"
    - "Y_n fails to satisfy Bessel's equation at nonzero radii"
    - "Y_n is not square-integrable and cannot be normalized"
  answer: 1
  explanation: "Y_n(kr) → −∞ as r → 0, so including it in the solution would imply an infinite field on the cylinder axis — physically unacceptable unless there is an actual singularity (like a line charge) located on the axis. This is directly analogous to dropping the 1/r^{l+1} term in spherical solutions when the domain includes the origin. If the domain is an annular region not including r = 0 (e.g., between two coaxial cylinders), both J_n and Y_n must be kept, because neither boundary contains the axis."

- question: "A circular waveguide has inner radius a. The TM₀₂ mode requires J₀(ka) = 0, where j_{0,2} ≈ 5.52 is the second zero of J₀. If the radius is doubled to 2a, what happens to the cutoff wavenumber k for this mode?"
  type: multiple-choice
  options:
    - "k doubles — the larger cylinder supports higher wavenumbers"
    - "k is halved — since k = j_{0,2}/a and a has doubled, k = j_{0,2}/(2a)"
    - "k stays the same — the Bessel zero j_{0,2} is fixed, so k is independent of a"
    - "k changes by a factor of √2 — waveguide cutoff scales with the square root of area"
  answer: 1
  explanation: "The boundary condition at the wall requires J_n(ka) = 0, so the allowed values of k are k_{n,m} = j_{n,m}/a, where j_{n,m} is the m-th zero of J_n. If a doubles to 2a, then k = j_{0,2}/(2a), which is half the original value. Physically, a larger cylinder supports the same mode shape but at a lower frequency (longer wavelength). This is exactly analogous to a Cartesian cavity of length L having k = nπ/L — doubling the length halves the wavenumber."

- question: "The zeros of Bessel functions J_n are not evenly spaced, unlike the evenly-spaced zeros of sin(kx)."
  type: true-false
  answer: true
  explanation: "The zeros of sin(kx) are evenly spaced at multiples of π/k. Bessel functions also oscillate and have infinitely many zeros, but their zeros are not evenly spaced — they asymptotically approach equal spacing (≈ π apart for large arguments), but the early zeros are irregularly distributed and must be tabulated. This is one reason cylindrical problems are more complex than Cartesian ones: you cannot write a simple formula for the n-th zero of J_n the way you can for sin."

- question: "In cylindrical coordinates, the azimuthal part of the separated solution to Laplace's equation (the φ-dependence) is a Bessel function."
  type: true-false
  answer: false
  explanation: "Bessel functions arise from the *radial* separated equation, not the azimuthal one. When Laplace's equation is separated in cylindrical coordinates (R, Φ, Z), the azimuthal Φ equation is simply Φ'' + n²Φ = 0, whose solutions are familiar trigonometric functions sin(nφ) and cos(nφ) (or e^{inφ}), with n an integer required by single-valuedness around the full angle. The radial equation is what produces Bessel's equation and its Bessel function solutions. The z-equation gives exponentials or trigonometric functions depending on boundary conditions."

- question: "Explain why Bessel functions appear in cylindrical boundary value problems instead of sines and cosines, and what determines which order J_n is needed for a given problem."
  type: short-answer
  answer: "In Cartesian coordinates, the separated Laplace equation in x is simply f'' + k²f = 0, yielding sines and cosines. In cylindrical coordinates, the radial equation acquires extra terms from the coordinate geometry: r²R'' + rR' + (k²r² − n²)R = 0. This is Bessel's equation, and its solutions J_n(kr) and Y_n(kr) are the appropriate 'sines and cosines' for radial oscillations in a cylindrical geometry. The order n is determined by the azimuthal mode number: if the solution has e^{inφ} azimuthal dependence (n lobes around the cylinder), the corresponding radial function is J_n. Cylindrically symmetric problems (no φ-dependence) use J₀; one-lobe variations use J₁; and so on."
  explanation: "The geometric origin of Bessel functions is the radial Laplacian in cylindrical coordinates, which differs from the flat Cartesian Laplacian by curvature terms. These curvature terms change the eigenvalue equation from constant-coefficient (yielding exponentials/trig) to variable-coefficient (yielding Bessel functions). The analogy to sines/cosines is exact: J_n oscillates, has zeros that determine allowed wavenumbers, and forms a complete orthogonal basis for radial functions on an interval."
```

## Explainer

When you applied separation of variables to Laplace's equation in Cartesian coordinates, the separated equations were simple — they produced sines, cosines, and exponentials, functions you already knew. Cylindrical coordinates produce a more exotic separated equation for the radial part. After separating out the φ (azimuthal) and z dependences — which give familiar trigonometric and exponential functions — the radial equation takes the form of **Bessel's equation**: r²R'' + rR' + (k²r² − n²)R = 0. The solutions to this equation are **Bessel functions** J_n(kr) and Y_n(kr), the cylindrical coordinate analogues of sines and cosines.

The intuition for Bessel functions is best built by analogy. In Cartesian coordinates, sin(kx) and cos(kx) oscillate uniformly with period 2π/k. Bessel functions J_n(r) also oscillate, but with slowly increasing period and slowly decreasing amplitude as r grows — like a sine wave that gradually spreads out and shrinks. The integer n is the **order** of the Bessel function, corresponding to the angular mode number from the φ-separation: J₀ describes cylindrically symmetric solutions, J₁ and J₂ describe azimuthal variations with one and two lobes around the cylinder. The Y_n functions (Neumann functions or Bessel functions of the second kind) diverge at r = 0, so they are excluded when the domain includes the cylinder axis — just as the 1/r term is dropped in regular spherical harmonics at the origin.

Boundary conditions select specific values of k through the zeros of Bessel functions. If you need a solution that vanishes at a conducting cylinder wall at radius a (say, the electric field tangential to a waveguide wall), you require J_n(ka) = 0. The zeros of J_n are tabulated and denoted j_{n,m} for the m-th zero of J_n — so k_{n,m} = j_{n,m}/a. Each pair (n, m) defines a distinct **mode** of the cylindrical cavity or waveguide. This is exactly the same logic as requiring sin(kL) = 0 for a Cartesian cavity of length L, but the zeros are no longer evenly spaced — they are the characteristic frequencies of the cylinder.

In waveguide analysis, these mode structures have direct physical meaning. The TE₁₁ mode of a circular waveguide has a single azimuthal oscillation (n = 1) and the first radial zero (m = 1), giving a particular cutoff frequency below which that mode cannot propagate. Mastering Bessel functions means being able to read mode labels, evaluate field patterns, and match boundary conditions at cylindrical interfaces — the core skills for circular waveguide design, resonant cavities, and scattering from cylindrical obstacles.
