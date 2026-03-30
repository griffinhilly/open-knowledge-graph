---
id: cpt-theorem
title: CPT Theorem
domain: physics
course: quantum-field-theory
prerequisites:
- id: dirac-field-quantization
  type: hard
- id: s-matrix-scattering-amplitudes
  type: hard
tags:
- cpt
- discrete-symmetries
- antiunitary
stage: expert
status: validated
---

# CPT Theorem

## Core Idea
The CPT theorem states that any local, Lorentz-invariant quantum field theory with a Hermitian Hamiltonian is invariant under the combined operation of charge conjugation (C), parity (P), and time reversal (T). This is an exact symmetry -- not approximate -- and implies that particles and antiparticles have exactly equal masses, lifetimes, and (opposite) charges. No violation of CPT has ever been observed.

## Questions

```yaml
- question: "The weak interaction violates C, P, and CP individually. How is this consistent with the CPT theorem?"
  type: multiple-choice
  options:
    - "It is not consistent — the CPT theorem must be wrong"
    - "The CPT theorem says only the combined operation CPT is a symmetry — each individual operation (C, P, T, or any pair like CP) can be violated, as long as the triple product CPT is conserved"
    - "The weak interaction is not a local quantum field theory"
    - "CPT is only approximately conserved in the weak interaction"
  answer: 1
  explanation: "The CPT theorem constrains only the triple combination. The weak interaction maximally violates P (only left-handed fermions couple to W bosons) and C (particle and antiparticle couplings differ). It also violates CP (observed in kaon and B-meson decays). But CPT remains exact: if CP is violated, then T must also be violated in exactly the compensating way to preserve CPT. This has been verified experimentally — direct T violation in the kaon system matches the CP violation as predicted by CPT invariance."

- question: "The CPT theorem implies that a particle and its antiparticle have exactly the same mass. The most precise test of this is the comparison of the proton and antiproton masses, which agree to better than one part in 10^{10}."
  type: true-false
  answer: true
  explanation: "CPT transforms a particle at rest into its antiparticle at rest. Since CPT is a symmetry of the Hamiltonian, both states must have the same energy, which means the same mass. The CERN BASE experiment has measured the proton-to-antiproton charge-to-mass ratio to a precision of 16 parts per trillion. Any difference would signal CPT violation and require abandoning one of the axioms of quantum field theory (locality, Lorentz invariance, or Hermiticity of the Hamiltonian). No deviation has been found."

- question: "If CPT is violated, at least one of the foundational axioms of quantum field theory must be wrong. Which axioms does the CPT theorem depend on?"
  type: multiple-choice
  options:
    - "Only Lorentz invariance"
    - "Locality (interactions occur at spacetime points), Lorentz invariance (the theory is the same in all inertial frames), and unitarity (probability is conserved, equivalently the Hamiltonian is Hermitian)"
    - "Only unitarity and gauge invariance"
    - "Only the spin-statistics connection"
  answer: 1
  explanation: "The CPT theorem is derived from three axioms: (1) the theory is a local quantum field theory (fields at spacelike separations commute or anticommute), (2) the theory is Lorentz invariant, and (3) the Hamiltonian is Hermitian (ensuring unitary time evolution). If any of these fails, CPT invariance is not guaranteed. Some theories of quantum gravity suggest that Lorentz invariance or locality might be violated at the Planck scale, which would potentially allow CPT violation. This is why experimental tests of CPT are so important — they probe the deepest foundations of physics."

- question: "Explain why CPT invariance, combined with observed CP violation, implies that T (time reversal) must also be violated in nature."
  type: short-answer
  answer: "CPT invariance means the combined transformation is an exact symmetry: (CPT)^{-1} H (CPT) = H. If CP is violated, meaning (CP)^{-1} H (CP) != H, then T must also be violated to compensate: (CPT) = (CP)(T), so if CP is broken, T must be broken in precisely the way that makes the product CPT still a symmetry. Concretely, if a process has different rates under CP transformation (like certain kaon decays), then the time-reversed process must also show an asymmetry, and the two asymmetries must be equal. This has been confirmed experimentally: direct T violation has been observed in the kaon and B-meson systems, and it matches the CP violation as required by CPT."
  explanation: "This argument makes T violation a prediction, not just an observation. Given the measured CP violation in the CKM matrix of the Standard Model, the CPT theorem predicts exactly how much T violation there must be. The experimental confirmation of this predicted T violation is a stringent test of CPT."
```

## Explainer

The **CPT theorem** is one of the most fundamental results in quantum field theory. It states that any local, Lorentz-invariant quantum field theory with a Hermitian Hamiltonian is automatically invariant under the combined operation CPT: charge conjugation (replacing every particle with its antiparticle), parity (reflecting all spatial coordinates), and time reversal (reversing the direction of time). This is not an assumption or an observed symmetry -- it is a theorem, provable from the axioms of QFT.

The individual operations C, P, and T need not be symmetries. The weak interaction violates P maximally (only left-handed fermions feel the weak force) and violates C (the charge-conjugate process has a different rate). It even violates CP, as observed in kaon decays (1964) and B-meson decays (2001). But the CPT theorem guarantees that the triple product is always conserved. If CP is violated, then T must be violated in exactly the compensating way, and this prediction has been verified experimentally.

The physical consequences of CPT invariance are remarkably concrete. Particles and antiparticles must have: **exactly equal masses** (tested to parts per trillion for proton/antiproton and electron/positron), **exactly equal lifetimes** (tested to parts per thousand for muon/antimuon and kaon/antikaon), and **exactly equal and opposite charges** (tested to extraordinary precision for electron/positron). Any observed difference would signal CPT violation and would require abandoning locality, Lorentz invariance, or unitarity -- any of which would be revolutionary.

The theorem also connects to the **matter-antimatter asymmetry** of the universe. CPT invariance means the laws of physics do not prefer matter over antimatter in any absolute sense. The observed preponderance of matter must therefore be generated dynamically from an initially symmetric state, through processes that violate CP (and hence T, by CPT) -- the Sakharov conditions. The CP violation in the Standard Model (from the CKM matrix) is too small to account for the observed asymmetry, implying new sources of CP violation beyond the Standard Model.
