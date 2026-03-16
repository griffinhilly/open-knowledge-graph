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
- id: surface-integrals-flux
  type: hard
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

## Explainer

You already know that electric flux Φ = ∫∫ E⃗·dA⃗ measures how much electric field "threads through" a surface, and you know from Coulomb's law that charge creates a radially symmetric electric field. Gauss's law ties these together with a single powerful statement: the total flux through any closed surface equals the total enclosed charge divided by ε₀. This is not an approximation — it is an exact consequence of Coulomb's law, equivalent to it for static charges, but far easier to use whenever the charge distribution has sufficient symmetry.

The key to using Gauss's law is choosing the right **Gaussian surface** — a mathematical closed surface that you invent to exploit the symmetry of the problem. The surface isn't physical; no charge accumulates on it. You choose it so that E has the same magnitude everywhere on the surface and is either parallel to dA⃗ (so E⃗·dA⃗ = E dA, a constant you can pull out of the integral) or perpendicular to dA⃗ (so E⃗·dA⃗ = 0, contributing nothing). With the right choice, the surface integral collapses to E × (total surface area) = Q_enc/ε₀, which you solve in one step for E.

The three canonical geometries are worth mastering in sequence. For a **point charge** or any spherically symmetric distribution, choose a spherical Gaussian surface centered on the charge. Symmetry forces E to be radial and constant on the sphere, so 4πr²E = Q_enc/ε₀, giving E = Q_enc/(4πε₀r²) — Coulomb's law recovered immediately. For an **infinite line charge** with linear charge density λ, choose a co-axial cylindrical surface of radius r and length L. The curved side gives E × 2πrL = λL/ε₀, so E = λ/(2πε₀r). For an **infinite plane** with surface charge density σ, choose a pillbox — a squat cylinder straddling the plane. The two flat caps each contribute EA, and E × 2A = σA/ε₀, so E = σ/(2ε₀), uniform everywhere.

One subtle but important point: the electric field E on the Gaussian surface is produced by all charges in the universe, not just the enclosed ones. But the flux through the closed surface is determined only by the enclosed charge — contributions from external charges integrate to zero over a closed surface because the field lines that enter also exit. This is why you can read off Q_enc from the flux even in the presence of other charges. Gauss's law in differential form, ∇·E = ρ/ε₀ (one of Maxwell's equations), says the same thing locally: the divergence of E at a point equals the charge density at that point divided by ε₀. Your divergence theorem prerequisite connects these two forms: integrating ∇·E over a volume and converting to a surface integral of E yields the integral form of Gauss's law directly.
