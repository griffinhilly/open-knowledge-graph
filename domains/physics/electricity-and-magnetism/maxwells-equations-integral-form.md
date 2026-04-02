---
id: maxwells-equations-integral-form
title: Maxwell's Equations in Integral Form
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: maxwells-equations-differential-form
  type: hard
- id: partial-derivatives
  type: hard
builds-toward:
- boundary-conditions-em-fields
- electromagnetic-waves-in-media
tags:
- maxwell-equations
- flux
- circulation
stage: expert
status: validated
---

# Maxwell's Equations in Integral Form

## Core Idea
The integral forms relate fluxes and circulations to their sources: Gauss's law (flux = enclosed charge), Ampère-Maxwell law (circulation = enclosed current plus displacement current). These forms apply the divergence and Stokes theorems and often simplify problems with high symmetry.

## Questions

```yaml
- question: "To find the electric field at distance r from a uniformly charged sphere, a physicist chooses a spherical Gaussian surface centered on the sphere. Why is this the right choice?"
  type: multiple-choice
  options:
    - "The divergence theorem only applies to spherical surfaces"
    - "The electric field is always strongest on a sphere, maximizing the flux integral"
    - "By symmetry, E is radial and uniform in magnitude on the sphere, so it factors out of the flux integral, reducing ∯ E·dA to E · 4πr²"
    - "A sphere encloses the maximum possible charge for a given radius"
  answer: 2
  explanation: "The power of Gauss's law in integral form is that it lets you factor E out of the integral when symmetry guarantees E is constant in magnitude and perpendicular to the surface everywhere. A concentric sphere achieves this for a spherically symmetric charge distribution. Without this symmetry, the integral form is harder to use than the differential form — you cannot simply 'pull E outside the integral.'"

- question: "Why did Maxwell add the displacement current term (ε₀ ∂E/∂t) to Ampère's law?"
  type: multiple-choice
  options:
    - "To account for current flowing through the dielectric material of a capacitor"
    - "To correct for the magnetic permeability of free space"
    - "So that Ampère's law gives the same result regardless of which surface bounded by the same Amperian loop is chosen — without it, a charging capacitor produces contradictory answers"
    - "To include the contribution of magnetic monopoles to the circulation of B"
  answer: 2
  explanation: "When a capacitor charges, current flows in the wire but not through the gap. If you compute the Amperian circulation using a flat surface cutting through the wire, you get μ₀I. If you use a bulging surface that passes through the capacitor gap (no conduction current passes through it), you get zero — a contradiction for the same loop. Maxwell resolved this by adding ε₀ ∂E/∂t, which is nonzero in the gap during charging and restores consistency regardless of surface choice."

- question: "Maxwell's equations in integral form contain additional physical laws beyond those expressed in the differential forms."
  type: true-false
  answer: false
  explanation: "The integral and differential forms are mathematically equivalent — they express exactly the same physics. The integral forms are derived from the differential forms by applying the divergence theorem (to Gauss's laws) and Stokes' theorem (to Faraday's and Ampère-Maxwell's laws). No new physics enters; you are simply converting local point-by-point relationships into global statements about finite surfaces and loops."

- question: "For Gauss's law in integral form to be a practical tool for calculating electric field strength, the charge distribution must have enough symmetry that E is constant in magnitude over a well-chosen Gaussian surface."
  type: true-false
  answer: true
  explanation: "This is the key condition. When E is constant and perpendicular to the surface everywhere, ∯ E·dA simplifies to E · A (total surface area), and you can immediately solve for E. Without this symmetry, E varies over the surface and the integral cannot be evaluated without knowing E in advance — defeating the purpose. This is why Gauss's law in integral form is most useful for spherical, cylindrical, and planar symmetry."

- question: "Why are the integral forms of Maxwell's equations more practically useful than the differential forms for high-symmetry problems, and which two theorems connect the two forms?"
  type: short-answer
  answer: "The integral forms are more useful in symmetric problems because symmetry allows you to choose a Gaussian surface or Amperian loop where the field is constant in magnitude and either parallel or perpendicular to the surface/path element everywhere — letting you pull the field outside the integral and solve in one algebraic step. The two connecting theorems are the divergence theorem (converts the divergence equations ∇·E = ρ/ε₀ and ∇·B = 0 into surface flux integrals) and Stokes' theorem (converts the curl equations for E and B into line integrals around closed loops)."
  explanation: "The differential forms are more general — they apply at every point in arbitrary geometries and are the starting point for deriving wave equations. But for textbook problems involving a point charge, an infinite wire, or a solenoid, integral forms with a smart surface choice turn a PDE problem into a single equation."
```

## Explainer

You already know Maxwell's equations in differential form — four partial differential equations governing how E⃗ and B⃗ vary point by point in space and time. Those equations are the most compact and general statement. The integral forms are not new physics; they are the same equations viewed through the lens of two theorems from your multivariable calculus prerequisite: the **divergence theorem** (∫∫∫ ∇·F dV = ∯ F·dA) and **Stokes' theorem** (∫∫ (∇×F)·dA = ∮ F·dl). Applying these transforms the local, derivative statements into global statements about fluxes and circulations over finite surfaces and volumes.

Gauss's law for E⃗ starts from ∇·E⃗ = ρ/ε₀. Integrating both sides over any closed volume and applying the divergence theorem converts the left side into the **total electric flux** ∯ E⃗·dA⃗ through the bounding surface, and the right side into Q_enc/ε₀. Result: the total outward electric flux through any closed surface equals the total enclosed charge divided by ε₀. For a point charge, choosing a sphere centered on the charge makes the integral trivial — E⃗ is radial and uniform in magnitude on the sphere, so the flux is just 4πr²E, immediately giving Coulomb's law. Gauss's magnetic law ∇·B⃗ = 0 similarly integrates to ∯ B⃗·dA⃗ = 0 — no magnetic monopoles, so every field line that enters a closed surface must exit it.

Faraday's law (∇×E⃗ = −∂B⃗/∂t) and the Ampère-Maxwell law (∇×B⃗ = μ₀J⃗ + μ₀ε₀∂E⃗/∂t) become circulation integrals via Stokes' theorem. Integrating Faraday's law over an open surface and applying Stokes converts ∫∫(∇×E⃗)·dA⃗ into the **EMF** ∮ E⃗·dl⃗ around the boundary loop, while the right side becomes −dΦ_B/dt — the rate of change of magnetic flux. This is the mathematical statement of electromagnetic induction. The Ampère-Maxwell integral form says the circulation of B⃗ around a closed loop equals μ₀ times the total current (conduction plus displacement) passing through any surface bounded by that loop. The freedom to choose "any surface" is what forced Maxwell to add the displacement current term — without it, the two choices of surface for the same loop would give contradictory answers when a capacitor is charging.

The integral forms are often more practical than the differential forms when a problem has a symmetry that makes the integrands nearly constant over a chosen surface or loop. Gauss's law in integral form is the standard tool for finding E⃗ near a sphere, cylinder, or plane of charge. Ampère's law is the standard tool for the field of an infinite wire or inside a solenoid. The strategy is always the same: exploit symmetry to pull the field outside the integral, then solve for its magnitude in one line. The differential forms are more powerful for arbitrary geometries and for deriving wave equations, but the integral forms are what you reach for when symmetry is on your side.
