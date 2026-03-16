---
id: faraday-law-advanced
title: Faraday's Law of Induction
domain: physics
course: electrodynamics
prerequisites:
- id: faradays-law
  type: hard
- id: magnetic-flux-and-induction
  type: hard
- id: line-integrals-vector-fields
  type: hard
builds-toward:
- maxwell-equations-integral-form
- electromagnetic-induction-applications
tags:
- faraday-law
- induction
- emf
stage: advanced
status: draft
---

# Faraday's Law of Induction

## Core Idea
Faraday's law states that the induced electric field (and EMF) around a closed loop equals the negative rate of change of magnetic flux through the loop. This law is fundamental to understanding electromagnetic induction, AC generators, transformers, and the interaction between time-varying magnetic and electric fields. It reveals the deep coupling between electricity and magnetism.

## Explainer

From your study of Faraday's law and magnetic flux, you know that a changing magnetic flux through a loop induces an EMF: EMF = −dΦ_B/dt. This is the magnitude relationship. The advanced form expresses the *same* law in terms that reveal its deep structure. EMF is not a property of the loop itself — it is the work done per unit charge by the electric field as a test charge travels around the loop. In mathematical terms, EMF = ∮ E · dl, the **line integral** of the electric field around the closed path. Equating these gives Faraday's law in integral form: ∮ E · dl = −dΦ_B/dt.

The left side — a line integral of E around a closed loop — measures the **circulation** of the electric field. In electrostatics, this integral is always zero: conservative fields do zero net work around any closed path. But the equation says this integral equals −dΦ_B/dt, which is generally nonzero. The implication is profound: when a magnetic field changes in time, it creates an electric field whose field lines close on themselves — a **non-conservative** electric field with no starting or ending charges. This is qualitatively different from the Coulomb field, which always begins on positive charges and ends on negative ones.

A concrete example: imagine a long solenoid being turned on. Inside the solenoid, B increases. But even *outside* the solenoid, where B = 0, there is a circulating electric field induced by the changing flux inside. The field lines of this induced E form closed rings centered on the solenoid axis. A conducting loop placed anywhere in this region would experience an EMF and carry a current, even though it sits in zero magnetic field. The source of the EMF is not a local field — it is the changing flux threading through the loop's interior. This is the conceptual content the line integral form captures precisely.

Applying Stokes' theorem to the integral form converts ∮ E · dl = −dΦ_B/dt into the differential (local) form: **∇ × E = −∂B/∂t**. This is one of Maxwell's four equations. It makes a local statement: wherever and whenever B changes in time, the electric field curls at that location. Combined with the Ampère-Maxwell law (∇ × B = μ₀J + μ₀ε₀∂E/∂t), these two curl equations form a coupled system. A changing B creates a curling E; a changing E creates a curling B. This mutual induction is the engine of electromagnetic waves, which propagate through space at speed c = 1/√(μ₀ε₀) even in vacuum. Faraday's law, expressed in its advanced form, is not just an engineering tool for calculating transformer EMFs — it is one of the four pillars of classical electrodynamics.
