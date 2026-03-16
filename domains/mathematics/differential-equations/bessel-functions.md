---
id: bessel-functions
title: Bessel Functions and Their Properties
domain: mathematics
course: differential-equations
prerequisites:
- id: frobenius-method
  type: hard
builds-toward:
- fourier-series-definition
tags:
- bessel-functions
- special-functions
- orthogonal
stage: advanced
status: draft
---

# Bessel Functions and Their Properties

## Core Idea
Bessel's equation x²y'' + xy' + (x² - ν²)y = 0 arises in cylindrical symmetry. Solutions are Bessel functions J_ν (first kind) and Y_ν (second kind). These functions are orthogonal with respect to a weighted inner product, enabling Fourier-Bessel expansions. Tables, recursion relations, and asymptotic approximations make Bessel functions practical for engineering and physics applications.

## Explainer

The Frobenius method you mastered handles ODEs with regular singular points by assuming power series solutions of the form x^r Σ aₙxⁿ. Bessel's equation x²y'' + xy' + (x² − ν²)y = 0 is the most important example of this class, arising whenever a physical problem has **cylindrical symmetry** — the vibrating circular drumhead, heat conduction in a cylindrical rod, electromagnetic modes in a fiber-optic cable. In all these settings, the natural radial coordinate is distance r from the central axis, and separating variables in cylindrical coordinates produces Bessel's equation with x = r.

Applying the Frobenius method at x = 0 (a regular singular point) yields the **Bessel function of the first kind** J_ν(x), given by the series J_ν(x) = Σ_{k=0}^∞ (−1)^k / (k! Γ(ν+k+1)) · (x/2)^(2k+ν). The key intuition for its behavior: for large x, J_ν(x) ≈ √(2/πx) cos(x − νπ/2 − π/4) — a **damped oscillation** whose amplitude decays like 1/√x. This is why Bessel functions describe outward-spreading waves in cylindrical geometry: they oscillate like sin and cos but gradually decrease in amplitude as the wave spreads over a larger and larger circumference. Think of ripples on a circular pond.

The second linearly independent solution, **Y_ν(x)** (the Bessel function of the second kind, or Neumann function), diverges logarithmically as x → 0. This singularity at the origin determines which solutions are physically acceptable. For problems on a full disk including the center — like a drumhead clamped at its edge — the solution must remain finite at r = 0, so Y_ν is discarded and only J_ν appears. For an annular region that excludes the origin, both J_ν and Y_ν contribute to the general solution. The physical boundary condition, not abstract algebra, makes the choice.

The most practically important property is **orthogonality** with a weight function. If λ_{ν,m} and λ_{ν,n} are distinct zeros of J_ν(x), then ∫₀^a x J_ν(λ_{ν,m} x/a) J_ν(λ_{ν,n} x/a) dx = 0 for m ≠ n. The extra factor of x in the integrand comes from the cylindrical coordinate area element. This weighted orthogonality enables **Fourier-Bessel expansions**: any reasonable function on [0, a] can be written as a sum of Bessel functions, exactly as Fourier series expand functions in sines and cosines. In practice, recursion relations J_{ν−1}(x) + J_{ν+1}(x) = (2ν/x)J_ν(x) and tabulated zeros allow computation without rederiving the series every time.
