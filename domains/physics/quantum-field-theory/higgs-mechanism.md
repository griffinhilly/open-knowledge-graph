---
id: higgs-mechanism
title: Higgs Mechanism
domain: physics
course: quantum-field-theory
prerequisites:
- id: goldstone-theorem-qft
  type: hard
- id: electromagnetic-field-quantization
  type: hard
tags:
- higgs
- mass-generation
- gauge-boson-mass
stage: expert
status: validated
---

# Higgs Mechanism

## Core Idea
The Higgs mechanism generates masses for gauge bosons through spontaneous breaking of a gauge symmetry. The would-be Goldstone bosons are "eaten" by the gauge bosons, becoming their longitudinal polarization components. The gauge bosons acquire mass while the theory remains renormalizable. The physical Higgs boson is the remaining massive scalar excitation.

## Questions

```yaml
- question: "In the abelian Higgs model (U(1) gauge field coupled to a complex scalar with a Mexican hat potential), the photon acquires a mass m_A = ev. Where does the longitudinal degree of freedom come from?"
  type: multiple-choice
  options:
    - "From the timelike component of the gauge field"
    - "From the Goldstone boson — the angular mode of the scalar field is absorbed into the gauge field, giving it the third polarization (longitudinal) needed for a massive vector boson"
    - "From the ghost fields introduced during gauge fixing"
    - "From vacuum fluctuations of the electromagnetic field"
  answer: 1
  explanation: "Before symmetry breaking, the theory has a massless gauge boson with 2 polarizations and a complex scalar with 2 degrees of freedom (4 total). After symmetry breaking, the gauge boson is massive with 3 polarizations and one real scalar (the Higgs boson) remains (4 total). The Goldstone boson has been absorbed: it provides the longitudinal polarization of the now-massive gauge boson. In unitary gauge, this is manifest — the Goldstone field disappears from the Lagrangian entirely, and the gauge field mass term appears explicitly."

- question: "The Higgs mechanism violates gauge invariance because a massive gauge boson is not gauge invariant."
  type: true-false
  answer: false
  explanation: "The Lagrangian of the Higgs mechanism is fully gauge invariant — the symmetry is spontaneously broken, not explicitly broken. The mass term arises from the gauge-covariant coupling of the gauge field to the scalar field with a nonzero vacuum expectation value: |D_mu phi|^2 evaluated at <phi> = v generates (ev)^2 A_mu A^mu/2. In the unitary gauge, this looks like an explicit mass term, but it originated from a gauge-invariant expression. This is crucial: explicit breaking of gauge invariance would destroy renormalizability, but spontaneous breaking preserves it. The proof of renormalizability of the Higgs mechanism (by 't Hooft and Veltman, Nobel Prize 1999) was one of the most important results in 20th century physics."

- question: "The Higgs boson was discovered at the LHC in 2012 with a mass of approximately 125 GeV. Why does the Standard Model not predict the Higgs mass, even though it predicts the W and Z masses?"
  type: multiple-choice
  options:
    - "Because the LHC was not precise enough to test the prediction"
    - "Because the Higgs mass depends on the self-coupling lambda in the Higgs potential, which is a free parameter of the Standard Model — unlike the W and Z masses (which are determined by the gauge couplings and the Higgs vacuum expectation value v = 246 GeV), the Higgs mass m_H = sqrt(2 lambda) v requires knowing lambda independently"
    - "Because the Higgs boson is a composite particle"
    - "Because quantum corrections make the Higgs mass incalculable"
  answer: 1
  explanation: "The W mass is m_W = gv/2 and the Z mass is m_Z = sqrt(g^2 + g'^2) v/2, where g and g' are the SU(2) and U(1) gauge couplings (measured independently) and v = 246 GeV is fixed by the Fermi constant. These are predictions. The Higgs mass m_H = sqrt(2 lambda) v depends on the quartic coupling lambda, which is a free parameter. Measuring m_H = 125 GeV determines lambda = m_H^2/(2v^2) approximately 0.13. The Standard Model has no mechanism to predict lambda from other parameters."

- question: "Explain how fermion masses are generated in the Standard Model through the Higgs mechanism, and why this is necessary given the chiral structure of the electroweak interaction."
  type: short-answer
  answer: "In the Standard Model, left-handed fermions form SU(2) doublets while right-handed fermions are SU(2) singlets. A Dirac mass term m psi-bar psi = m(psi-bar_L psi_R + psi-bar_R psi_L) couples left- and right-handed components, but since they transform differently under SU(2), this term is not gauge invariant. The Higgs mechanism solves this: a Yukawa coupling y psi-bar_L phi psi_R (where phi is the Higgs doublet) is gauge invariant. When phi acquires a vacuum expectation value <phi> = (0, v/sqrt(2))^T, this term becomes y v/sqrt(2) psi-bar_L psi_R, which is a mass term with m = yv/sqrt(2). Each fermion's mass is proportional to its Yukawa coupling y, which is a free parameter. This is why fermion masses span such a huge range (electron: 0.5 MeV; top quark: 173 GeV)."
  explanation: "The Yukawa couplings are among the most puzzling free parameters of the Standard Model. Why the top quark's Yukawa coupling is close to 1 while the electron's is 10^{-6} is the fermion mass hierarchy problem — one of the major open questions in particle physics."
```

## Explainer

The **Higgs mechanism** is the process by which gauge bosons acquire mass through spontaneous symmetry breaking, without destroying gauge invariance or renormalizability. The simplest example is the abelian Higgs model: a U(1) gauge field A_mu coupled to a complex scalar phi with a Mexican hat potential. The Lagrangian is L = -1/4 F^2 + |D_mu phi|^2 - V(phi), where D_mu = partial_mu - ieA_mu is the covariant derivative and V = -mu^2|phi|^2 + lambda|phi|^4.

When phi acquires a vacuum expectation value <phi> = v/sqrt(2), the covariant derivative term |D_mu phi|^2 evaluated at the vacuum generates e^2 v^2 A_mu A^mu / 2 -- a mass term for the gauge field with m_A = ev. The angular degree of freedom of phi (the would-be Goldstone boson) is absent from the physical spectrum in unitary gauge; it has been **absorbed** into the gauge field as its longitudinal polarization. The radial fluctuation remains as a massive scalar particle -- the **Higgs boson** with mass m_H = sqrt(2 lambda) v.

In the **Standard Model**, the electroweak gauge symmetry SU(2)_L x U(1)_Y is broken to U(1)_EM by a complex scalar doublet (four real components). Three Goldstone bosons are eaten by the W+, W-, and Z bosons, giving them masses. The fourth component remains as the physical Higgs boson, discovered at the LHC in 2012 with mass 125 GeV. The vacuum expectation value v = 246 GeV is fixed by the measured Fermi constant. The W and Z masses are then predictions: m_W = gv/2 approximately 80 GeV and m_Z approximately 91 GeV, in excellent agreement with experiment.

Fermion masses are also generated through the Higgs mechanism. Direct mass terms m psi-bar psi are forbidden by the chiral structure of the electroweak interaction (left- and right-handed fermions transform differently under SU(2)). Instead, **Yukawa couplings** y psi-bar_L phi psi_R connect the fermion fields to the Higgs doublet. When phi gets its vacuum expectation value, these become mass terms m_f = y_f v/sqrt(2). Each fermion's mass is proportional to its Yukawa coupling, which is a free parameter. The proof by 't Hooft and Veltman that theories with the Higgs mechanism are renormalizable was the theoretical foundation for the Standard Model.
