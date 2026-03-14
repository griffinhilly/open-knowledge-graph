---
id: gauss-law
title: Gauss's Law
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: electric-flux
  type: hard
- id: electric-charge-and-coulombs-law
  type: hard
- id: divergence-theorem
  type: soft
- id: curl-and-divergence
  type: soft
builds-toward:
- maxwells-equations-overview
- conductors-in-electrostatics
tags:
- gauss-law
- symmetry
- electrostatics
- closed-surface
stage: formal-systems
status: validated
---

# Gauss's Law

## Core Idea
Gauss's law states that the net electric flux through any closed surface (a Gaussian surface) equals the total enclosed charge divided by ε₀: ∮ E · dA = Q_enc/ε₀. It is mathematically equivalent to Coulomb's law for static charges but is far more powerful for systems with high symmetry (spherical, cylindrical, or planar). Choosing the right Gaussian surface — one where E is constant and parallel to dA — reduces a surface integral to simple algebra.

## How It's Best Learned
Master three canonical problems: a point charge (spherical surface), an infinite line charge (cylindrical surface), and an infinite plane (pillbox surface). For each, identify the symmetry argument that justifies the Gaussian surface choice before evaluating the integral.

## Common Misconceptions
- Gauss's law is always true, but it only simplifies calculations when symmetry is present.
- The Gaussian surface is a mathematical construct, not a physical object.
- E on the Gaussian surface depends on all charges, not just the enclosed ones — but the flux through it depends only on Q_enc.
