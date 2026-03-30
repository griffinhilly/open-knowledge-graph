---
id: renormalization-of-qed
title: Renormalization of QED
domain: physics
course: quantum-field-theory
prerequisites:
- id: regularization-techniques-qft
  type: hard
- id: loop-diagrams-divergences
  type: hard
- id: qed-vertex-basic-processes
  type: hard
tags:
- renormalization
- qed
- counterterms
stage: expert
status: validated
---

# Renormalization of QED

## Core Idea
Renormalization of QED absorbs ultraviolet divergences into redefinitions of the electron mass, the electric charge, and the field normalizations. Only three types of divergent diagrams exist in QED (self-energy, vacuum polarization, vertex correction), making the theory renormalizable: all divergences at every order are absorbed by a finite number of counterterms.

## Questions

```yaml
- question: "QED has three types of divergent diagrams: the electron self-energy, the vacuum polarization, and the vertex correction. A student asks: 'What if I compute a two-loop diagram and find a new type of divergence not related to these three?' Why can't this happen?"
  type: multiple-choice
  options:
    - "Because two-loop diagrams are always finite in QED"
    - "Because any divergent subdiagram in a higher-order graph must itself be one of these three types — higher-order divergences are nested combinations of the same three primitive divergences, and the counterterms that cancel them at one loop also cancel them at all loops"
    - "Because QED only has one coupling constant"
    - "Because gauge invariance forbids any new divergent structures"
  answer: 1
  explanation: "This is the content of renormalizability. In QED, power counting shows that only three superficially divergent Green's functions exist: the fermion two-point function (self-energy), the photon two-point function (vacuum polarization), and the fermion-photon three-point function (vertex). Any higher-order diagram either is convergent or contains one of these three as a divergent subdiagram. The counterterms (delta_m for mass, delta_Z for field renormalization, delta_e for charge) introduced at one loop absorb the corresponding divergences at every order. This is proven rigorously by the BPHZ theorem."

- question: "The bare electric charge e_0 in the QED Lagrangian is infinite, and only the renormalized charge e_R (defined at a specific momentum scale) is finite and measurable."
  type: true-false
  answer: true
  explanation: "The bare charge e_0 absorbs the ultraviolet divergence from the vacuum polarization. It is formally infinite (or cutoff-dependent if you use a regulator), and it is not directly measurable. The physical charge e_R is defined by a renormalization condition — typically the value of the photon-fermion vertex at a specific momentum transfer. The relation is e_0 = Z_3^{-1/2} e_R, where Z_3 contains the divergent vacuum polarization contribution. All physical predictions depend only on e_R (which equals the measured value of the fine structure constant at the chosen scale), not on e_0."

- question: "The electron's anomalous magnetic moment a_e = (g-2)/2 is one of the most precisely tested predictions in physics. The leading QED correction (Schwinger's result) gives a_e = alpha/(2 pi). What makes this prediction so remarkable?"
  type: multiple-choice
  options:
    - "It is the only prediction that does not require renormalization"
    - "It is a finite, unambiguous prediction from a single one-loop diagram (the vertex correction) that agrees with experiment to extraordinary precision — and the agreement improves as higher-order corrections are included, validating the entire renormalization program"
    - "It was the first prediction of quantum mechanics"
    - "It shows that the electron is a point particle"
  answer: 1
  explanation: "The anomalous magnetic moment is computed from the vertex correction diagram. After renormalization, the result alpha/(2pi) approximately 0.00116 is finite and parameter-free (it depends only on the already-measured value of alpha). The current theoretical value includes contributions through five-loop order (tenth order in alpha) and agrees with the experimental measurement to better than one part in 10^12. This agreement validates not just the one-loop calculation but the entire perturbative framework and renormalization procedure at extraordinary precision."

- question: "Explain the physical meaning of wave function renormalization Z_2 for the electron field, and why it is necessary even though it is not directly observable."
  type: short-answer
  answer: "Z_2 is the field strength renormalization factor: psi_0 = sqrt(Z_2) psi_R, where psi_0 is the bare field and psi_R is the renormalized field. Physically, Z_2 accounts for the fact that a bare electron continuously emits and reabsorbs virtual photons — the 'physical electron' is dressed by a cloud of virtual photons. The probability of finding the bare electron inside the physical electron is Z_2 (which is less than 1 and divergent in perturbation theory). Z_2 is not directly observable because it cancels between the LSZ reduction formula and the vertex renormalization (this cancellation is guaranteed by the Ward identity Z_1 = Z_2). However, it must be included for intermediate calculations to be consistent."
  explanation: "The Ward identity Z_1 = Z_2 is a consequence of gauge invariance and is one of the most important relations in QED. It ensures that the electric charge is renormalized only by the vacuum polarization (Z_3), not by the vertex or self-energy corrections. This is why all charged particles (regardless of spin or mass) have their charges renormalized by the same factor — the universality of charge renormalization."
```

## Explainer

The three divergent diagrams of QED -- the electron **self-energy**, the **vacuum polarization**, and the **vertex correction** -- each modify one of the basic elements of the theory. The self-energy shifts the electron mass and normalizes the electron field. The vacuum polarization modifies the photon propagator and renormalizes the electric charge. The vertex correction modifies the electron-photon coupling. Renormalization absorbs these divergences into redefinitions of the bare parameters.

The procedure is systematic. Start with the bare Lagrangian L = psi_0-bar(i gamma^mu partial_mu - m_0)psi_0 - e_0 psi_0-bar gamma^mu psi_0 A_0_mu - (1/4)F_0^2. Introduce renormalized fields and parameters: psi_0 = sqrt(Z_2) psi_R, A_0 = sqrt(Z_3) A_R, m_0 = m_R + delta_m, e_0 = Z_1 Z_2^{-1} Z_3^{-1/2} e_R. Rewrite the Lagrangian in terms of renormalized quantities; the leftover pieces are **counterterms** that exactly cancel the divergences from loop diagrams. The counterterms delta_m, delta_Z2 = Z_2 - 1, delta_Z3 = Z_3 - 1, and delta_Z1 = Z_1 - 1 are fixed by renormalization conditions that specify the physical mass, charge, and field normalization.

The **Ward identity** Z_1 = Z_2, a consequence of gauge invariance, is crucial. It ensures that the charge renormalization comes entirely from the vacuum polarization (Z_3), so the renormalized charge is e_R = e_0 Z_3^{1/2}. This means the electric charge of every particle is renormalized by the same factor, regardless of the particle's mass or spin -- the universality of charge that we observe experimentally. Without the Ward identity, different particles could have different charge renormalizations, and the equality of the proton and electron charges would be an unexplained coincidence.

The triumph of renormalized QED is its predictive power. Once three quantities are measured (the electron mass, the fine structure constant, and the field normalization convention), every other prediction of QED is determined. The anomalous magnetic moment of the electron, the Lamb shift, the hyperfine splitting of hydrogen, photon-photon scattering -- all are computed as power series in alpha with no free parameters. The agreement with experiment (to 12 significant figures for the electron g-2) is the most stringent test of any physical theory ever performed.
