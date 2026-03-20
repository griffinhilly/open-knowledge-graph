---
id: maxwell-equations-integral-form
title: Maxwell's Equations in Integral Form
domain: physics
course: electrodynamics
prerequisites:
- id: gauss-law
  type: hard
- id: faradays-law
  type: hard
- id: amperes-law
  type: hard
- id: divergence-theorem
  type: hard
- id: stokes-theorem
  type: hard
builds-toward:
  - maxwell-equations-differential-form
  - ampere-maxwell-law
tags:
- maxwell-equations
- vector-calculus
- foundations
stage: advanced
status: draft
---
# Maxwell's Equations in Integral Form

## Core Idea
Maxwell's four integral equations relate electric and magnetic fields to charges and currents through flux and circulation relationships. These equations—Gauss's law, Ampère's law with Maxwell's correction, Faraday's law, and the absence of magnetic monopoles—form the complete description of classical electromagnetism. The integral form is particularly useful for problems with symmetry and for understanding the physical meaning of each equation.

## How It's Best Learned
Begin by reviewing each equation's physical meaning: Gauss's law (charges produce electric flux), Ampère-Maxwell law (currents and changing E-fields produce circulation of B), Faraday's law (changing B-flux produces E), and the monopole equation. Work problems with spherical, cylindrical, and planar symmetry to develop intuition.

## Common Misconceptions
- Assuming Maxwell's equations only apply in vacuum; they generalize to matter with D and H fields.
- Forgetting the displacement current term (∂E/∂t) in Ampère's law.
- Confusing the integral form (fluxes through surfaces) with local field values at a point.

## Explainer

You already know each of Maxwell's four equations individually from prior study. What is new here is seeing them as a unified system and understanding how they interact. The four equations are: Gauss's law for E (electric flux through a closed surface equals enclosed charge / ε₀), Gauss's law for B (magnetic flux through any closed surface is zero — no magnetic monopoles), Faraday's law (circulation of E around a closed loop equals minus the rate of change of magnetic flux), and the Ampère-Maxwell law (circulation of B equals μ₀ times enclosed current plus μ₀ε₀ times rate of change of electric flux). Together they completely determine how electric and magnetic fields are produced and how they evolve.

The most important equation to understand deeply is the **Ampère-Maxwell law** with Maxwell's key addition: the displacement current term μ₀ε₀ ∂Φ_E/∂t. The original Ampère's law related B circulation only to conduction current. Maxwell noticed this was inconsistent: if you draw an Amperian surface that passes through a capacitor gap (where there is no conduction current but a changing E field), the original law gives zero while a surface that doesn't pass through the gap gives a non-zero result. The same Amperian loop cannot give two different answers. Maxwell's fix was to add the displacement current term, making the law self-consistent. This addition was not just a mathematical patch — it predicted that changing electric fields produce magnetic fields, just as changing magnetic fields produce electric fields (Faraday's law). The symmetric coupling between E and B is what enables self-sustaining electromagnetic waves.

The **integral form** of Maxwell's equations is physically transparent because it speaks in terms of total flux and total circulation — measurable quantities on finite surfaces and loops. Gauss's law says that charges create field lines that diverge outward; if you enclose a charge, more field lines exit than enter. Gauss's law for B says that magnetic field lines always form closed loops — they never start or stop, which means you can never isolate a magnetic "charge." Faraday's law says that a time-varying magnetic field drives E in a closed ring around it; this is the principle of the transformer. The Ampère-Maxwell law says that currents and time-varying electric fields drive B in closed rings around them; this is the principle of the electromagnet and the propagating electromagnetic wave.

The power of writing all four together is that you can see, at a glance, what can generate fields: charges generate E flux, currents and changing E generate B circulation, and changing B generates E circulation. Nothing else creates fields. Every electromagnetic phenomenon — from the static field of a charged sphere to the propagation of a WiFi signal across a room — follows from these four relationships. The divergence theorem and Stokes' theorem (your mathematical prerequisites) translate these integral statements into the differential form ∇·E = ρ/ε₀, ∇·B = 0, ∇×E = −∂B/∂t, ∇×B = μ₀J + μ₀ε₀ ∂E/∂t, which are the forms most useful for deriving wave equations and solving field problems in continuous media.
