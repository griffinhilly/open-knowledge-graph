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

## Explainer

When you applied separation of variables to Laplace's equation in Cartesian coordinates, the separated equations were simple — they produced sines, cosines, and exponentials, functions you already knew. Cylindrical coordinates produce a more exotic separated equation for the radial part. After separating out the φ (azimuthal) and z dependences — which give familiar trigonometric and exponential functions — the radial equation takes the form of **Bessel's equation**: r²R'' + rR' + (k²r² − n²)R = 0. The solutions to this equation are **Bessel functions** J_n(kr) and Y_n(kr), the cylindrical coordinate analogues of sines and cosines.

The intuition for Bessel functions is best built by analogy. In Cartesian coordinates, sin(kx) and cos(kx) oscillate uniformly with period 2π/k. Bessel functions J_n(r) also oscillate, but with slowly increasing period and slowly decreasing amplitude as r grows — like a sine wave that gradually spreads out and shrinks. The integer n is the **order** of the Bessel function, corresponding to the angular mode number from the φ-separation: J₀ describes cylindrically symmetric solutions, J₁ and J₂ describe azimuthal variations with one and two lobes around the cylinder. The Y_n functions (Neumann functions or Bessel functions of the second kind) diverge at r = 0, so they are excluded when the domain includes the cylinder axis — just as the 1/r term is dropped in regular spherical harmonics at the origin.

Boundary conditions select specific values of k through the zeros of Bessel functions. If you need a solution that vanishes at a conducting cylinder wall at radius a (say, the electric field tangential to a waveguide wall), you require J_n(ka) = 0. The zeros of J_n are tabulated and denoted j_{n,m} for the m-th zero of J_n — so k_{n,m} = j_{n,m}/a. Each pair (n, m) defines a distinct **mode** of the cylindrical cavity or waveguide. This is exactly the same logic as requiring sin(kL) = 0 for a Cartesian cavity of length L, but the zeros are no longer evenly spaced — they are the characteristic frequencies of the cylinder.

In waveguide analysis, these mode structures have direct physical meaning. The TE₁₁ mode of a circular waveguide has a single azimuthal oscillation (n = 1) and the first radial zero (m = 1), giving a particular cutoff frequency below which that mode cannot propagate. Mastering Bessel functions means being able to read mode labels, evaluate field patterns, and match boundary conditions at cylindrical interfaces — the core skills for circular waveguide design, resonant cavities, and scattering from cylindrical obstacles.
