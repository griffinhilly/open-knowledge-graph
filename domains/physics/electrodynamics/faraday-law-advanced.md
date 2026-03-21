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

## Questions

```yaml
- question: "A solenoid carries an increasing current, so its magnetic field B is increasing inside. A circular conducting loop is placed outside the solenoid, where B = 0 at every point on the loop. What does Faraday's law predict?"
  type: multiple-choice
  options:
    - "No EMF is induced because B = 0 everywhere on the loop"
    - "No EMF is induced because the loop is outside the solenoid"
    - "An EMF is induced because the magnetic flux through the loop's interior is changing, even though B = 0 on the loop itself"
    - "An EMF is induced only if the loop is a conductor; the electric field outside is zero regardless"
  answer: 2
  explanation: "Faraday's law states EMF = −dΦ_B/dt, where Φ_B is the flux *through the surface bounded by the loop* — not the field at the loop itself. Even though B = 0 at every point on the loop, the flux through the loop's interior (which passes through the solenoid) is changing. This creates a circulating electric field in the space around the solenoid, including on the loop. This is one of the most counterintuitive results in electromagnetism: the source of EMF is the changing flux *through* the loop, not the field *at* the loop. Option A reflects the common misconception of confusing the field at the loop with the flux through it."

- question: "How does the electric field induced by a changing magnetic flux differ fundamentally from the electrostatic field produced by static charges?"
  type: multiple-choice
  options:
    - "The induced field is weaker but has the same field-line structure as the Coulomb field"
    - "The induced field points radially outward from its source; the Coulomb field curls in closed loops"
    - "The induced field has closed field lines with no source charges; the electrostatic field begins on positive and ends on negative charges"
    - "There is no fundamental difference — both are solutions to the same equation"
  answer: 2
  explanation: "The induced electric field is non-conservative: its field lines form closed loops, never beginning or ending on charges. This is the geometric signature of a curl (∇ × E = −∂B/∂t): field lines close on themselves. The electrostatic Coulomb field is conservative — field lines start on positive charges and end on negative charges, and ∮ E · dl = 0 around any closed path. The two kinds of electric field obey different equations and have different topologies. The induced field is fundamentally new — it is created by time-varying B, not by charges."

- question: "The induced electric field from a changing magnetic flux can be nonzero even in a region where the magnetic field itself is zero."
  type: true-false
  answer: true
  explanation: "Yes — this is one of the most important and counterintuitive consequences of Faraday's law. The induced E at a point depends not on B at that point but on the *rate of change of magnetic flux* through any surface bounded by a loop around that point. Outside a solenoid, B = 0, but the changing flux through loops that enclose the solenoid generates a circulating E in the surrounding region. This is directly analogous to the Aharonov-Bohm effect in quantum mechanics, where the magnetic vector potential affects particle phases in field-free regions."

- question: "In electrostatics, the line integral ∮ E · dl around any closed path is always nonzero, since the electric field points outward from charges."
  type: true-false
  answer: false
  explanation: "This is backwards. In electrostatics, ∮ E · dl = 0 around any closed loop — the electrostatic field is conservative, meaning it does zero net work on a charge taken around a closed path. This follows from the fact that the electrostatic field is the gradient of a scalar potential: ∮ ∇V · dl = 0 for any closed path. It is the *induced* electric field (from changing B) that can have a nonzero circulation. This is precisely what makes Faraday's law physically deep: it asserts that time-varying B creates a field with nonzero curl, unlike any electrostatic configuration."

- question: "Why is the induced electric field described as 'non-conservative,' and what does this mean physically?"
  type: short-answer
  answer: "A field is conservative if the work it does on a charge around any closed path is zero — equivalently, if the field can be described as the gradient of a potential. The induced electric field is non-conservative because ∮ E · dl = −dΦ_B/dt, which is generally nonzero. This means the field does net work on a charge traversing a closed loop — it can drive a persistent current in a conductor without any battery. Physically, the 'source' of the field is not separated charges (as in electrostatics) but the changing magnetic flux threading through the loop; the energy comes from whatever is changing the magnetic field."
  explanation: "This distinction matters for understanding why transformers and generators work: the induced EMF is not a potential difference between two points (there is no unique potential function) but a true circulation of the electric field around a loop. The concept of voltage loses its usual meaning in the presence of time-varying B, which is why circuit analysis involving inductors requires care."
```

## Explainer

From your study of Faraday's law and magnetic flux, you know that a changing magnetic flux through a loop induces an EMF: EMF = −dΦ_B/dt. This is the magnitude relationship. The advanced form expresses the *same* law in terms that reveal its deep structure. EMF is not a property of the loop itself — it is the work done per unit charge by the electric field as a test charge travels around the loop. In mathematical terms, EMF = ∮ E · dl, the **line integral** of the electric field around the closed path. Equating these gives Faraday's law in integral form: ∮ E · dl = −dΦ_B/dt.

The left side — a line integral of E around a closed loop — measures the **circulation** of the electric field. In electrostatics, this integral is always zero: conservative fields do zero net work around any closed path. But the equation says this integral equals −dΦ_B/dt, which is generally nonzero. The implication is profound: when a magnetic field changes in time, it creates an electric field whose field lines close on themselves — a **non-conservative** electric field with no starting or ending charges. This is qualitatively different from the Coulomb field, which always begins on positive charges and ends on negative ones.

A concrete example: imagine a long solenoid being turned on. Inside the solenoid, B increases. But even *outside* the solenoid, where B = 0, there is a circulating electric field induced by the changing flux inside. The field lines of this induced E form closed rings centered on the solenoid axis. A conducting loop placed anywhere in this region would experience an EMF and carry a current, even though it sits in zero magnetic field. The source of the EMF is not a local field — it is the changing flux threading through the loop's interior. This is the conceptual content the line integral form captures precisely.

Applying Stokes' theorem to the integral form converts ∮ E · dl = −dΦ_B/dt into the differential (local) form: **∇ × E = −∂B/∂t**. This is one of Maxwell's four equations. It makes a local statement: wherever and whenever B changes in time, the electric field curls at that location. Combined with the Ampère-Maxwell law (∇ × B = μ₀J + μ₀ε₀∂E/∂t), these two curl equations form a coupled system. A changing B creates a curling E; a changing E creates a curling B. This mutual induction is the engine of electromagnetic waves, which propagate through space at speed c = 1/√(μ₀ε₀) even in vacuum. Faraday's law, expressed in its advanced form, is not just an engineering tool for calculating transformer EMFs — it is one of the four pillars of classical electrodynamics.
