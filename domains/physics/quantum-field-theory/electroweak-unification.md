---
id: electroweak-unification
title: Electroweak Unification
domain: physics
course: quantum-field-theory
prerequisites:
- id: higgs-mechanism
  type: hard
- id: non-abelian-gauge-theories
  type: hard
tags:
- electroweak
- weinberg-salam
- weak-interaction
stage: expert
status: validated
---

# Electroweak Unification

## Core Idea
The Glashow-Weinberg-Salam model unifies electromagnetism and the weak interaction as different aspects of a single SU(2)_L x U(1)_Y gauge theory. Spontaneous symmetry breaking via the Higgs mechanism gives mass to the W+, W-, and Z bosons while leaving the photon massless. The weak and electromagnetic interactions appear different only because the symmetry is broken at the electroweak scale (approximately 246 GeV).

## Questions

```yaml
- question: "Before electroweak symmetry breaking, the theory has four massless gauge bosons: W1, W2, W3 (from SU(2)_L) and B (from U(1)_Y). After breaking, the physical states are W+, W-, Z, and the photon. How are the Z and the photon related to W3 and B?"
  type: multiple-choice
  options:
    - "Z = W3 and photon = B"
    - "The Z and photon are orthogonal linear combinations of W3 and B, mixed by the weak mixing angle theta_W: Z = cos(theta_W) W3 - sin(theta_W) B, and A (photon) = sin(theta_W) W3 + cos(theta_W) B"
    - "The Z is a bound state of W3 and B"
    - "W3 becomes the Z and B becomes the photon, with no mixing"
  answer: 1
  explanation: "Symmetry breaking mixes W3 and B because the Higgs doublet carries both SU(2) and U(1) charges. The physical photon and Z are the mass eigenstates — orthogonal rotations of W3 and B by the weak mixing angle theta_W (approximately 28.7 degrees). The photon is the combination that leaves the vacuum invariant (coupling to the unbroken U(1)_EM), and the Z is the orthogonal combination (which acquires mass). The mixing angle is determined by the ratio of the SU(2) and U(1) gauge couplings: tan(theta_W) = g'/g."

- question: "The weak interaction violates parity (it distinguishes left from right) because only left-handed fermions couple to the W boson. This parity violation is built into the gauge structure of SU(2)_L."
  type: true-false
  answer: true
  explanation: "The subscript L in SU(2)_L indicates that only left-handed fermion fields form doublets under SU(2) — right-handed fermions are singlets that do not couple to W bosons. This means the W boson couples only to left-handed particles (and right-handed antiparticles), violating parity maximally. This is not an incidental feature but is fundamental to the gauge structure: you cannot make the weak interaction parity-conserving without changing the gauge group. Parity violation was discovered experimentally by Wu in 1957 and explained theoretically by the V-A (vector minus axial vector) structure of the weak current."

- question: "At energies far above the electroweak scale (E >> 246 GeV), the distinction between the electromagnetic and weak interactions disappears."
  type: true-false
  answer: true
  explanation: "Above the electroweak scale, all four gauge bosons are effectively massless (their masses are negligible compared to the collision energy), and the full SU(2)_L x U(1)_Y symmetry is restored. Weak and electromagnetic interactions become comparable in strength (the apparent weakness of the weak force at low energies is due to the large W and Z masses suppressing the propagator, not an intrinsically smaller coupling). This is directly observed at the LHC, where W and Z production cross sections are large and the electroweak gauge structure is directly probed."

- question: "Explain why the photon remains massless after electroweak symmetry breaking, while the W and Z acquire masses. What symmetry protects the photon?"
  type: short-answer
  answer: "The Higgs doublet breaks SU(2)_L x U(1)_Y to U(1)_EM. The three broken generators (corresponding to W+, W-, and Z) give rise to three Goldstone bosons that are eaten by these gauge bosons, making them massive. The unbroken generator — the electric charge Q = T_3 + Y/2, a specific linear combination of the SU(2) generator T_3 and the hypercharge Y — corresponds to the photon. Because U(1)_EM remains an exact symmetry, the photon has no mass: gauge invariance of the residual U(1) forbids a photon mass term. The Higgs vacuum is electrically neutral (Q|vac> = 0), which is why it does not break electromagnetic gauge invariance."
  explanation: "This is a beautiful example of the general principle: the number of massive gauge bosons equals the number of broken generators. SU(2)_L x U(1)_Y has 4 generators, U(1)_EM has 1, so 3 generators are broken and 3 gauge bosons become massive. The one surviving gauge boson — the photon — remains massless because its symmetry is unbroken."
```

## Explainer

The **electroweak theory**, formulated by Glashow, Weinberg, and Salam (Nobel Prize 1979), unifies the electromagnetic and weak interactions into a single gauge theory based on the group SU(2)_L x U(1)_Y. The SU(2)_L factor acts only on left-handed fermions (explaining the parity violation of the weak force), and U(1)_Y is the hypercharge symmetry. Before symmetry breaking, the theory has four massless gauge bosons: three from SU(2)_L (W1, W2, W3) and one from U(1)_Y (B).

The Higgs mechanism breaks SU(2)_L x U(1)_Y to U(1)_EM, the gauge symmetry of electromagnetism. A complex scalar doublet phi with a Mexican hat potential acquires a vacuum expectation value v = 246 GeV. Three of the four scalar degrees of freedom become the longitudinal components of the W+, W-, and Z bosons, which acquire masses m_W = gv/2 approximately 80 GeV and m_Z = m_W/cos(theta_W) approximately 91 GeV. The fourth scalar is the physical Higgs boson (125 GeV). The photon, corresponding to the unbroken U(1)_EM generator Q = T_3 + Y/2, remains massless.

The **weak mixing angle** theta_W parametrizes the mixing between the SU(2)_L and U(1)_Y gauge bosons. The photon and Z are linear combinations of W3 and B, rotated by theta_W. The value sin^2(theta_W) approximately 0.23 is determined experimentally and relates the SU(2) coupling g, the U(1) coupling g', and the electromagnetic coupling e by e = g sin(theta_W) = g' cos(theta_W). This single parameter connects the strengths of the electromagnetic and weak interactions.

The apparent difference between electromagnetism and the weak force at everyday energies is entirely due to the large masses of the W and Z bosons. The weak interaction appears short-range (approximately 10^{-18} m) because the massive W and Z propagators fall off exponentially: the effective potential goes as e^{-M_W r}/r rather than 1/r. At energies above the electroweak scale, the boson masses become irrelevant and the full SU(2)_L x U(1)_Y symmetry is effectively restored. The electromagnetic and weak interactions become comparable in strength, as directly confirmed by high-energy experiments at the LHC.
