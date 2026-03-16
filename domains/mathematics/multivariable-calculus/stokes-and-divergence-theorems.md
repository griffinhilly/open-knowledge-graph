---
id: stokes-and-divergence-theorems
title: Stokes' Theorem and the Divergence Theorem
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: surface-integrals-flux
  type: hard
tags:
- stokes-theorem
- divergence-theorem
- gauss-theorem
stage: formal-systems
status: draft
---

# Stokes' Theorem and the Divergence Theorem

## Core Idea
Stokes' theorem: ∮_C F · dr = ∬_S (∇ × F) · dS (line integral of F around a closed curve equals flux of curl through the surface). Divergence theorem: ∬_S F · dS = ∭_V ∇ · F dV (flux through a closed surface equals integral of divergence over the volume). These unify single, double, and triple integrals.

## Explainer

From your work with surface integrals and flux, you know how to compute ∬_S F · dS — the rate at which a vector field F flows through a surface S. Both Stokes' theorem and the Divergence theorem belong to a single grand pattern: an integral over the interior of a region equals an integral over the boundary of that region. The fundamental theorem of calculus is the simplest instance — ∫_a^b f′(x) dx = f(b) − f(a) says the integral of f′ over an interval equals f evaluated on the boundary (just two points). Green's theorem, Stokes' theorem, and the Divergence theorem are higher-dimensional versions of this same idea.

**Stokes' theorem** connects a line integral around a closed curve C to a surface integral over any surface S bounded by C. The integrand on the surface side is the **curl** ∇ × F, which measures the infinitesimal rotation of F — how much F "circulates" locally. Stokes says the total circulation around the boundary C equals the total accumulated local rotation through the surface. Physically: if F is a velocity field of a fluid, the work done going around C equals the sum of all the little whirlpools threading through the surface. Crucially, any surface with boundary C gives the same answer — the choice of surface doesn't matter, only its boundary does.

The **Divergence theorem** (also called Gauss's theorem) connects a surface integral over a closed surface S to a volume integral over the region V enclosed by S. The integrand inside is the **divergence** ∇ · F, which measures how much F is "spreading out" or "converging" at each point — positive where field lines originate, negative where they terminate. The theorem says total outward flux through the surface equals the total source strength inside the volume. In electrostatics, this is exactly Gauss's law: the flux of the electric field through a closed surface equals the total charge enclosed, divided by ε₀.

These theorems are powerful computational tools as much as conceptual unifications. If ∬_S F · dS is hard to compute directly on a complex surface, and V is simple, compute ∭_V ∇ · F dV instead — often much easier when the divergence is constant or simple. Similarly, if ∮_C F · dr is cumbersome, choose a convenient surface bounded by C and integrate the curl. The freedom to choose the surface (in Stokes) or convert between surface and volume integrals (in the Divergence theorem) is the key flexibility that makes these theorems indispensable in physics and engineering, from Maxwell's equations to fluid dynamics.
