---
id: electromagnetic-field-quantization
title: Electromagnetic Field Quantization (QED)
domain: physics
course: quantum-field-theory
prerequisites:
- id: klein-gordon-field-quantization
  type: hard
- id: gauge-transformations
  type: hard
- id: maxwell-equations-differential-form
  type: hard
tags:
- photon
- gauge-field
- qed
stage: expert
status: validated
---

# Electromagnetic Field Quantization (QED)

## Core Idea
Quantizing the electromagnetic field promotes the vector potential A^mu to an operator. Gauge invariance introduces complications: unphysical degrees of freedom must be removed or constrained. The result is a theory of photons -- massless spin-1 particles with two physical polarization states.

## Questions

```yaml
- question: "The photon has spin 1, which naively allows three polarization states (m = -1, 0, +1). Why does a physical photon have only two polarization states?"
  type: multiple-choice
  options:
    - "The third polarization state has negative energy and is excluded"
    - "Gauge invariance eliminates the longitudinal and timelike polarizations, leaving only two transverse physical states"
    - "The photon is massless, so it cannot be at rest and therefore spin projections are meaningless"
    - "Experimental evidence shows only two polarizations, but the theory actually predicts three"
  answer: 1
  explanation: "A massive spin-1 particle has three polarization states. The photon has only two because gauge invariance (the freedom to shift A^mu -> A^mu + partial^mu Lambda without changing the physics) makes the longitudinal and timelike components unphysical. In Coulomb gauge, this is manifest: only the two transverse components of A are dynamical. In covariant gauges, all four components appear in intermediate calculations but the unphysical ones cancel in any physical observable (this cancellation is guaranteed by Ward identities). Masslessness alone is not sufficient — it is gauge invariance that reduces the polarization count."

- question: "In Coulomb gauge (div A = 0), the quantized electromagnetic field has a clear physical interpretation but breaks manifest Lorentz covariance. In Lorentz gauge (partial_mu A^mu = 0), Lorentz covariance is manifest but unphysical ghost states appear. How is this resolved?"
  type: multiple-choice
  options:
    - "Ghost states are real particles that have been observed in accelerator experiments"
    - "The Gupta-Bleuler condition restricts the physical Hilbert space to states where the unphysical polarizations have zero expectation value, ensuring that only transverse photons contribute to physical processes"
    - "The Lorentz gauge is abandoned in favor of Coulomb gauge for all practical calculations"
    - "The ghost states cancel each other exactly due to supersymmetry"
  answer: 1
  explanation: "The Gupta-Bleuler quantization method works in Lorentz gauge by allowing all four polarization states in the full Hilbert space but imposing a subsidiary condition that defines the physical subspace. In this subspace, the contributions of timelike and longitudinal photons cancel in all matrix elements between physical states. The physical photon count is two transverse polarizations, consistent with Coulomb gauge. This tension between manifest Lorentz covariance and manifest unitarity (physical states only) is a recurring theme in gauge theory quantization."

- question: "The quantized electromagnetic field in the vacuum has zero electric and magnetic fields everywhere — it is completely empty and inert."
  type: true-false
  answer: false
  explanation: "The vacuum expectation values of E and B are zero: <0|E|0> = <0|B|0> = 0. But the expectation values of E^2 and B^2 are not zero — the vacuum has nonzero field fluctuations. These vacuum fluctuations are physically real: they cause the Lamb shift (a measurable energy difference between the 2S_{1/2} and 2P_{1/2} levels of hydrogen), the anomalous magnetic moment of the electron, and the Casimir effect (an attractive force between conducting plates in vacuum). The vacuum is not empty — it is the ground state of a quantum field, with zero average field but nonzero field fluctuations."

- question: "Explain why the masslessness of the photon is intimately connected to gauge invariance, and what would go wrong if you added a mass term (1/2)m^2 A_mu A^mu to the electromagnetic Lagrangian."
  type: short-answer
  answer: "The electromagnetic Lagrangian L = -(1/4)F_{mu nu}F^{mu nu} is invariant under gauge transformations A^mu -> A^mu + partial^mu Lambda. A mass term (1/2)m^2 A_mu A^mu is NOT gauge invariant because it changes under A^mu -> A^mu + partial^mu Lambda. Therefore, gauge invariance forbids the photon mass. Conversely, adding a mass term explicitly breaks gauge invariance, which would allow three polarization states instead of two (a massive spin-1 particle has a longitudinal mode) and would make the theory non-renormalizable in its naive form. The photon is massless because gauge invariance demands it."
  explanation: "This connection between gauge invariance and masslessness is central to the Standard Model. The W and Z bosons are massive spin-1 particles, which would seem to violate gauge invariance. The Higgs mechanism resolves this by breaking the gauge symmetry spontaneously rather than explicitly, generating mass while preserving the underlying gauge structure needed for renormalizability."
```

## Explainer

The classical electromagnetic field is described by the four-vector potential A^mu = (phi, A), with the electric and magnetic fields given by E = -grad phi - dA/dt and B = curl A. The Lagrangian density is L = -(1/4)F_{mu nu}F^{mu nu}, where F_{mu nu} = partial_mu A_nu - partial_nu A_mu is the field strength tensor. Gauge invariance -- the fact that A^mu and A^mu + partial^mu Lambda describe the same physics -- is both the defining feature of electrodynamics and the source of all technical complications in quantization.

The problem is that gauge invariance means A^mu has redundant degrees of freedom. A massive vector field would have three physical polarizations, but the massless photon has only two (the two transverse polarizations). You must somehow eliminate the unphysical degrees of freedom. In **Coulomb gauge** (div A = 0), the two transverse components of A are the dynamical variables, and quantization proceeds cleanly: each transverse mode with wave vector k and polarization lambda is a harmonic oscillator with creation operator a_{k,lambda}-dagger. The photon is a quantum of this oscillator. The drawback is that Coulomb gauge is not manifestly Lorentz covariant.

In **covariant gauges** (like Lorenz gauge, partial_mu A^mu = 0), all four components of A^mu participate, preserving manifest Lorentz invariance. But this introduces unphysical states -- timelike and longitudinal photons with negative norm. The **Gupta-Bleuler** method handles this by restricting the physical Hilbert space: only states satisfying the gauge condition (as an operator equation on kets) are physical, and the unphysical polarizations cancel in all physical matrix elements. More modern approaches use the BRST formalism, which introduces ghost fields that systematically cancel the unphysical contributions.

After quantization, the electromagnetic field describes **photons**: massless spin-1 particles with two polarization states (left and right circular, or equivalently, two linear polarizations). The field operator A^mu(x) creates and destroys photons at spacetime point x. The vacuum has no photons but is not empty -- quantum fluctuations of E and B produce measurable effects. Coupling the quantized photon field to the quantized Dirac field via the interaction term e psi-bar gamma^mu psi A_mu gives quantum electrodynamics (QED), the most precisely tested theory in all of physics.
