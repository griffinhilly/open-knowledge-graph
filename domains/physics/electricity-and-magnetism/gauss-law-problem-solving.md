---
id: gauss-law-problem-solving
title: Solving Problems with Gauss's Law
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: gauss-law-integral-form
  type: hard
- id: divergence-theorem
  type: hard
builds-toward:
- electric-potential-definition
- conductors-electrostatic-behavior
tags:
- problem-solving
- symmetry
- applications
stage: formal-systems
status: draft
---

# Solving Problems with Gauss's Law

## Core Idea
Gauss's law is most powerful when charge distributions have high symmetry (spherical, cylindrical, planar). Choose a Gaussian surface matching the symmetry so E is constant on the surface and parallel/perpendicular to dA.

## How It's Best Learned
Solve problems in sequence: sphere, cylinder, plane. Sketch symmetry and identify where E is constant before setting up the integral.

## Explainer

Gauss's law in integral form — ∮ E⃗ · dA⃗ = Q_enc/ε₀ — is always true, but it is only *useful* as a calculation tool when you can pull E outside the integral. This requires the electric field to be constant in magnitude and either parallel or perpendicular to the surface element everywhere on your chosen surface. The art of Gauss's law problems is choosing a **Gaussian surface** — an imaginary closed surface — that matches the symmetry of the charge distribution so perfectly that the dot product E⃗ · dA⃗ simplifies. The divergence theorem you've studied provides the mathematical underpinning: it connects the total flux through a closed surface to the source strength inside.

The three canonical symmetries each demand a different Gaussian surface. For **spherical symmetry** (a point charge, uniformly charged sphere, or spherically symmetric shell), use a concentric sphere. By symmetry, E must point radially and have the same magnitude at every point on the sphere — the integral becomes simply E(4πr²) = Q_enc/ε₀. For **cylindrical symmetry** (an infinite line charge or long cylindrical conductor), use a coaxial cylinder capped with flat ends. The field is radially outward through the curved surface but perpendicular to the flat end-caps, contributing nothing there. The curved surface gives E(2πrL) = Q_enc/ε₀. For **planar symmetry** (an infinite plane of charge), use a pillbox — a cylinder whose axis is perpendicular to the plane. Flux only passes through the two flat faces (parallel to E), giving 2EA = σA/ε₀, so E = σ/(2ε₀).

The step that trips students up most is correctly computing Q_enc — the charge actually *inside* the Gaussian surface, not the total charge of the object. For a solid sphere with uniform volume charge density ρ, a Gaussian sphere of radius r < R encloses only a fraction (r/R)³ of the total charge. For a conducting sphere, all charge sits on the surface, so a Gaussian surface inside the conductor encloses zero charge and E = 0 inside. Drawing the Gaussian surface first, then thinking carefully about what charge sits inside it, prevents most errors.

Once you have E from Gauss's law, you can compute the electric potential by integrating. You can also check for consistency: the divergence theorem guarantees that any surface enclosing the same charge gives the same total flux — useful for verifying that your surface choice didn't introduce an error. Practice builds the ability to recognize symmetry instantly and to pick the right surface without hesitation, which is the prerequisite for tackling conductors, dielectrics, and the full Maxwell equation set.
