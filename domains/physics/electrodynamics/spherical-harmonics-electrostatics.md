---
id: spherical-harmonics-electrostatics
title: Spherical Harmonics in Electrostatics
domain: physics
course: electrodynamics
prerequisites:
- id: boundary-value-problems-electrostatics
  type: hard
- id: separation-variables-elliptic-equations
  type: hard
- id: laplace-poisson-equations-electrostatics
  type: hard
- id: legendre-polynomials-and-equations
  type: hard
builds-toward:
- green-function-method-electrostatics
- boundary-value-problem-types
tags:
- special-functions
- boundary-value-problems
- legendre-polynomials
stage: advanced
status: draft
---

# Spherical Harmonics in Electrostatics

## Core Idea
Spherical harmonics form a complete orthonormal basis for solving Laplace's equation in spherical coordinates. Expansions in Legendre polynomials and associated Legendre functions allow systematic solution of electrostatic problems with spherical symmetry, including multipole expansions.

## How It's Best Learned
Start with Legendre polynomials for azimuthally symmetric problems, then generalize to full angular dependence. Apply to conducting sphere and dielectric sphere problems to verify orthogonality and convergence.

## Common Misconceptions
Spherical harmonics are specific to electrostatics (they apply to any Laplacian problem). Assuming convergence without checking domain of validity.
