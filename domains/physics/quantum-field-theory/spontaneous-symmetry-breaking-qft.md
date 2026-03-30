---
id: spontaneous-symmetry-breaking-qft
title: Spontaneous Symmetry Breaking
domain: physics
course: quantum-field-theory
prerequisites:
- id: classical-field-theory-lagrangian-density
  type: hard
- id: noethers-theorem-fields
  type: hard
- id: spontaneous-symmetry-breaking
  type: soft
tags:
- symmetry-breaking
- vacuum
- mexican-hat
stage: expert
status: validated
---

# Spontaneous Symmetry Breaking

## Core Idea
Spontaneous symmetry breaking occurs when the Lagrangian of a field theory has a symmetry that is not shared by the ground state (vacuum). The classic example is the Mexican hat potential, where the Lagrangian has rotational symmetry but the vacuum state picks a definite direction. This mechanism generates massless Goldstone bosons and, when combined with gauge invariance, gives mass to gauge bosons via the Higgs mechanism.

## Questions

```yaml
- question: "A real scalar field has the potential V(phi) = -mu^2 phi^2/2 + lambda phi^4/4. The Lagrangian is invariant under phi -> -phi (Z_2 symmetry). However, the minima of V are at phi = +/- mu/sqrt(lambda), not at phi = 0. Why is phi = 0 not the vacuum?"
  type: multiple-choice
  options:
    - "Quantum fluctuations destabilize the phi = 0 state"
    - "The phi = 0 configuration is a local maximum of V, not a minimum — the system rolls to one of the degenerate minima at +/- mu/sqrt(lambda), and whichever minimum is chosen breaks the Z_2 symmetry"
    - "The Z_2 symmetry is explicitly broken by higher-order terms"
    - "The phi = 0 vacuum is forbidden by the uncertainty principle"
  answer: 1
  explanation: "The potential V(phi) = -mu^2 phi^2/2 + lambda phi^4/4 has V''(0) = -mu^2 < 0, so phi = 0 is a local maximum (unstable). The true minima are at phi_0 = +/- mu/sqrt(lambda), where V'' > 0. The system settles into one of these minima, say phi_0 = +mu/sqrt(lambda). This ground state is NOT invariant under phi -> -phi (which would map phi_0 to -phi_0), so the Z_2 symmetry is spontaneously broken. The Lagrangian retains the full symmetry, but the vacuum does not."

- question: "For a complex scalar field with the Mexican hat potential V = -mu^2 |phi|^2 + lambda |phi|^4, the vacuum manifold is a circle |phi| = v = mu/sqrt(2 lambda). Fluctuations along the circle cost no energy. What do these zero-energy excitations correspond to?"
  type: multiple-choice
  options:
    - "Photons"
    - "Goldstone bosons — massless scalar particles that are the quantum excitations along the flat direction of the potential, one for each spontaneously broken continuous symmetry generator"
    - "Ghost particles required for gauge fixing"
    - "Tachyons"
  answer: 1
  explanation: "The potential is flat along the bottom of the Mexican hat (the circular valley at |phi| = v). Excitations along this flat direction require no energy to excite, so they correspond to massless particles — the Goldstone bosons. For the U(1) symmetry of a complex scalar field, there is one broken generator and one Goldstone boson. In contrast, excitations in the radial direction (perpendicular to the valley) have a restoring force and correspond to a massive particle. This is the content of Goldstone's theorem: each spontaneously broken continuous symmetry generator produces one massless scalar boson."

- question: "Spontaneous symmetry breaking means the symmetry is gone from the theory entirely — neither the Lagrangian nor the vacuum state respects it."
  type: true-false
  answer: false
  explanation: "In spontaneous symmetry breaking, the Lagrangian retains the full symmetry — it is the vacuum (ground state) that does not. This is a crucial distinction from explicit symmetry breaking (where a term in the Lagrangian violates the symmetry). Because the Lagrangian is symmetric, Ward identities and other consequences of the symmetry still hold, even though the vacuum picks a preferred direction. The symmetry is 'hidden' rather than 'gone.' The Goldstone theorem, the Higgs mechanism, and the structure of the particle spectrum all follow from the interplay between the symmetric Lagrangian and the asymmetric vacuum."

- question: "Explain why spontaneous symmetry breaking is necessary for the Standard Model to describe massive particles, and what goes wrong without it."
  type: short-answer
  answer: "The Standard Model is based on the gauge group SU(3) x SU(2) x U(1). Gauge invariance forbids explicit mass terms for the gauge bosons (a term m^2 A_mu A^mu is not gauge invariant) and for fermions with chiral couplings (a Dirac mass term m psi-bar psi mixes left- and right-handed components that transform differently under SU(2)). Without symmetry breaking, all gauge bosons and fermions would be massless. Spontaneous symmetry breaking (via the Higgs mechanism) generates masses while preserving the gauge structure of the Lagrangian, which is necessary for renormalizability. The W and Z bosons acquire mass by 'eating' three Goldstone bosons, and fermions acquire mass through Yukawa couplings to the Higgs field."
  explanation: "This is why the Higgs mechanism is essential, not optional, in the Standard Model. A world without spontaneous symmetry breaking would have massless W and Z bosons (making the weak force long-range), massless electrons (making atoms impossible), and a radically different universe."
```

## Explainer

**Spontaneous symmetry breaking** is one of the most important concepts in modern physics. The idea is simple but profound: a system's ground state can have less symmetry than the laws governing it. A ball at the top of a Mexican hat has rotational symmetry, but it must roll down to some point on the brim, picking a direction and breaking the symmetry. The potential is symmetric; the state is not.

In quantum field theory, the "ball" is a scalar field and the "hat" is its potential energy. Consider a complex scalar field phi with potential V = -mu^2 |phi|^2 + lambda |phi|^4 (with mu^2, lambda > 0). This potential has U(1) symmetry (invariance under phi -> e^{i alpha} phi) and its minimum is not at phi = 0 but on a circle |phi| = v = mu/sqrt(2 lambda). The field settles into a vacuum expectation value <phi> = v, breaking the U(1) symmetry. Small fluctuations around the vacuum decompose into a radial mode (massive, with mass sqrt(2) mu) and an angular mode (massless, the **Goldstone boson**).

**Goldstone's theorem** states that for each spontaneously broken continuous symmetry generator, there is one massless scalar particle. For a global U(1) symmetry, one generator is broken, producing one Goldstone boson. For a global SU(2) symmetry broken completely, three generators are broken, producing three Goldstone bosons. These massless excitations correspond to the "flat directions" of the potential -- rotations along the vacuum manifold that cost no energy. In condensed matter physics, Goldstone bosons appear as phonons (broken translation symmetry), magnons (broken rotation symmetry), and superfluidity modes (broken U(1) symmetry).

The power of spontaneous symmetry breaking in particle physics comes from combining it with **gauge invariance**. In a gauge theory, the Goldstone bosons are not physical particles -- they are "eaten" by the gauge bosons, which acquire mass. This is the Higgs mechanism, which gives mass to the W and Z bosons while keeping the photon massless. The essential point is that the Lagrangian remains gauge-invariant (ensuring renormalizability and theoretical consistency), but the vacuum state is not invariant, generating masses for the particles that interact with the broken-symmetry sector.
