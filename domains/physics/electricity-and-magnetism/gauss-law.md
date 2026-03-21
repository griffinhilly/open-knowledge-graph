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

## Questions

```yaml
- question: "A point charge +Q sits inside a hollow metal shell that carries a charge of −2Q on its surface. A student wants to use Gauss's law with a spherical Gaussian surface between the shell and the inner charge to find E there. She argues the law gives the wrong answer because the E field on the surface is produced by both +Q and −2Q, not just +Q. What is wrong with her reasoning?"
  type: multiple-choice
  options:
    - "She is correct — Gauss's law cannot be applied when there are charges both inside and outside the Gaussian surface"
    - "She is correct — the total charge (Q − 2Q = −Q) must be used, not just the inner charge"
    - "She is confused: E on the surface is indeed produced by all charges, but the net flux through a closed surface depends only on the enclosed charge — the external −2Q shell contributes zero net flux because its field lines that enter the surface also exit it"
    - "She is correct — Gauss's law only applies to surfaces surrounding a single, isolated charge"
  answer: 2
  explanation: "The student has identified a real subtlety but drawn the wrong conclusion. The electric field E at each point on the Gaussian surface is indeed produced by all charges — both +Q inside and −2Q outside. But Gauss's law is about the *flux integral* over a closed surface, not the field at a single point. Any charge outside the closed surface contributes field lines that, over the entire surface, enter and exit in equal amounts, making their net contribution to flux exactly zero. Only the enclosed charge contributes net flux. So ∮ E · dA = Q_enc/ε₀ = +Q/ε₀, even though E itself is influenced by the outer shell."

- question: "Gauss's law is always true, but why can't it simplify the calculation of E for an irregular, non-symmetric charge distribution?"
  type: multiple-choice
  options:
    - "Gauss's law is only an approximation that becomes exact in the limit of high symmetry"
    - "For irregular distributions, E is not a well-defined quantity on any surface"
    - "Without symmetry, E varies in both magnitude and direction across any Gaussian surface you could draw, so the integral ∮ E · dA cannot be reduced to E × (area) — you must evaluate it numerically rather than algebraically"
    - "Gauss's law requires the Gaussian surface to coincide with a physical object"
  answer: 2
  explanation: "Gauss's law is exact and always holds: ∮ E · dA = Q_enc/ε₀, regardless of the charge distribution. The issue is not correctness but computability. The law gives you the value of the flux integral — but to extract E from the flux, you need to pull E out of the integral. You can only do this if E is constant in magnitude and either parallel or perpendicular to dA everywhere on the chosen surface. That requires symmetry. For an irregular distribution, no surface has this property, so the law gives you a constraint on the integral without allowing you to solve for E directly. Coulomb's law or numerical methods are then required."

- question: "The Gaussian surface you choose must be a real physical object — a conducting shell, an insulating boundary, or some material surface — in order for Gauss's law to apply correctly."
  type: true-false
  answer: false
  explanation: "A Gaussian surface is a purely mathematical construct — an imaginary closed surface you draw in space to exploit symmetry. It has no physical reality whatsoever. No charge accumulates on it, no current flows through it, and it does not need to coincide with any physical boundary. You choose its shape and location entirely based on what makes the math simple: a sphere around a point charge, a cylinder around a line charge, a pillbox straddling an infinite plane. The only requirement is that it be a closed surface so that the flux integral is well-defined."

- question: "For a spherically symmetric charge distribution (like a uniformly charged sphere), placing a spherical Gaussian surface outside the distribution gives an electric field at that radius identical to what a point charge of the same total magnitude would produce at that location."
  type: true-false
  answer: true
  explanation: "This is the shell theorem, recoverable directly from Gauss's law. For any spherically symmetric distribution — whether a shell, a solid sphere, or any radially varying density — a spherical Gaussian surface at radius r outside the distribution yields 4πr²E = Q_total/ε₀, giving E = Q_total/(4πε₀r²), exactly the Coulomb field of a point charge Q_total at the origin. The internal structure of the distribution is irrelevant to the external field. This is why planets and stars, which are (approximately) spherically symmetric, can be treated as point masses for gravitational purposes — and why Gauss's law is so powerful."

- question: "Why is it valid to read off Q_enc from the flux through a Gaussian surface even when external charges are present that also produce electric field on that surface?"
  type: short-answer
  answer: "External charges produce electric field lines that cross the Gaussian surface in both directions. Because the surface is closed, every field line from an external charge that enters the surface must exit it somewhere else — the net flux contribution of any charge outside the surface is exactly zero. Only charges inside the surface have field lines that originate within the enclosed volume and thread outward through the surface without returning, creating a net flux. So the total flux counts only what's inside."
  explanation: "This follows from the divergence theorem and the structure of Coulomb's law. Mathematically, the field from an external charge obeys ∇·E = 0 inside the closed volume (since the source is outside), so by the divergence theorem its contribution to the surface integral is zero. Physically, you can think of it as flux conservation: field lines from an external charge can't 'pile up' inside a region that has no source — whatever enters must exit. This is what makes Gauss's law so powerful: you can ignore all the complicated contributions from external charges and read the total enclosed charge directly from the net flux."
```

## Explainer

You already know that electric flux Φ = ∫∫ E⃗·dA⃗ measures how much electric field "threads through" a surface, and you know from Coulomb's law that charge creates a radially symmetric electric field. Gauss's law ties these together with a single powerful statement: the total flux through any closed surface equals the total enclosed charge divided by ε₀. This is not an approximation — it is an exact consequence of Coulomb's law, equivalent to it for static charges, but far easier to use whenever the charge distribution has sufficient symmetry.

The key to using Gauss's law is choosing the right **Gaussian surface** — a mathematical closed surface that you invent to exploit the symmetry of the problem. The surface isn't physical; no charge accumulates on it. You choose it so that E has the same magnitude everywhere on the surface and is either parallel to dA⃗ (so E⃗·dA⃗ = E dA, a constant you can pull out of the integral) or perpendicular to dA⃗ (so E⃗·dA⃗ = 0, contributing nothing). With the right choice, the surface integral collapses to E × (total surface area) = Q_enc/ε₀, which you solve in one step for E.

The three canonical geometries are worth mastering in sequence. For a **point charge** or any spherically symmetric distribution, choose a spherical Gaussian surface centered on the charge. Symmetry forces E to be radial and constant on the sphere, so 4πr²E = Q_enc/ε₀, giving E = Q_enc/(4πε₀r²) — Coulomb's law recovered immediately. For an **infinite line charge** with linear charge density λ, choose a co-axial cylindrical surface of radius r and length L. The curved side gives E × 2πrL = λL/ε₀, so E = λ/(2πε₀r). For an **infinite plane** with surface charge density σ, choose a pillbox — a squat cylinder straddling the plane. The two flat caps each contribute EA, and E × 2A = σA/ε₀, so E = σ/(2ε₀), uniform everywhere.

One subtle but important point: the electric field E on the Gaussian surface is produced by all charges in the universe, not just the enclosed ones. But the flux through the closed surface is determined only by the enclosed charge — contributions from external charges integrate to zero over a closed surface because the field lines that enter also exit. This is why you can read off Q_enc from the flux even in the presence of other charges. Gauss's law in differential form, ∇·E = ρ/ε₀ (one of Maxwell's equations), says the same thing locally: the divergence of E at a point equals the charge density at that point divided by ε₀. Your divergence theorem prerequisite connects these two forms: integrating ∇·E over a volume and converting to a surface integral of E yields the integral form of Gauss's law directly.
