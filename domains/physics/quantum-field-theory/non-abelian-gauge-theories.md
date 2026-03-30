---
id: non-abelian-gauge-theories
title: Non-Abelian Gauge Theories (Yang-Mills)
domain: physics
course: quantum-field-theory
prerequisites:
- id: electromagnetic-field-quantization
  type: hard
- id: gauge-transformations
  type: hard
- id: renormalization-of-qed
  type: soft
tags:
- yang-mills
- non-abelian
- gauge-theory
stage: expert
status: validated
---

# Non-Abelian Gauge Theories (Yang-Mills)

## Core Idea
Non-abelian (Yang-Mills) gauge theories generalize electromagnetism from the abelian group U(1) to non-abelian groups like SU(2) and SU(3). The crucial difference is that the gauge bosons themselves carry charge and interact with each other. This self-interaction is responsible for asymptotic freedom in QCD and for the rich structure of the Standard Model.

## Questions

```yaml
- question: "In QED, photons do not interact with each other at tree level. In a non-abelian gauge theory, gauge bosons do interact with each other. What is the mathematical origin of this difference?"
  type: multiple-choice
  options:
    - "Non-abelian gauge bosons are massive, and massive particles always interact"
    - "The field strength tensor F^a_{mu nu} for a non-abelian group contains a term g f^{abc} A^b_mu A^c_nu that is quadratic in the gauge field — when substituted into the kinetic term F^2, this produces cubic and quartic self-interaction vertices that have no analog in QED"
    - "Non-abelian gauge bosons have spin-2 instead of spin-1"
    - "The non-abelian gauge group has more generators, requiring more interaction terms"
  answer: 1
  explanation: "In QED, F_{mu nu} = partial_mu A_nu - partial_nu A_mu is linear in A, so F^2 contains only quadratic terms (free propagation) — no photon self-interactions. In a non-abelian theory, F^a_{mu nu} = partial_mu A^a_nu - partial_nu A^a_mu + g f^{abc} A^b_mu A^c_nu, where f^{abc} are the structure constants of the gauge group. The extra term is quadratic in A, so F^2 contains cubic (three-gluon vertex) and quartic (four-gluon vertex) interaction terms. These self-interactions exist because non-abelian gauge bosons carry charge under their own gauge group — gluons carry color charge, while photons carry no electric charge."

- question: "The number of gauge bosons in a Yang-Mills theory equals the number of generators of the gauge group. SU(N) has N^2 - 1 generators. How many gluons does QCD (SU(3) gauge theory) have?"
  type: multiple-choice
  options:
    - "3"
    - "6"
    - "8"
    - "9"
  answer: 2
  explanation: "SU(3) has 3^2 - 1 = 8 generators, so QCD has 8 gluons. Each gluon carries a color-anticolor combination (but not all 9 combinations — the color-singlet combination is removed, leaving 8). For comparison, SU(2) has 3 generators (the W+, W-, and Z bosons before electroweak symmetry breaking), and U(1) has 1 generator (the photon)."

- question: "Quantizing a non-abelian gauge theory requires introducing Faddeev-Popov ghost fields, which are scalar fields that obey Fermi statistics. Why are ghosts necessary, and why don't they appear in QED?"
  type: true-false
  answer: true
  explanation: "Ghost fields are necessary in non-abelian theories to maintain unitarity (conservation of probability) in covariant gauges. The gauge-fixing procedure overcounts gauge-equivalent field configurations, and ghosts cancel the contributions of unphysical longitudinal and timelike gauge boson polarizations in loops. In QED, the ghost fields decouple (they do not interact with photons because the abelian structure constants vanish) and can be ignored. In non-abelian theories, ghosts couple to gluons through the structure constants f^{abc} and must be included in all loop calculations. Ghosts are not physical particles — they are computational tools that appear as internal lines in Feynman diagrams but never as external states."

- question: "Explain why the self-interaction of non-abelian gauge bosons leads to qualitatively different physics from QED, giving at least two specific physical consequences."
  type: short-answer
  answer: "First, gluon self-interaction produces asymptotic freedom: the QCD beta function is negative (beta = -11 N_c/(48 pi^2) g^3 + ... for SU(N_c) with no fermions), meaning the coupling decreases at high energies. This is opposite to QED (where vacuum polarization from charged fermions makes beta positive) and occurs because gluon loops contribute to the vacuum polarization with the opposite sign to fermion loops, and dominate when the number of fermion flavors is not too large. Second, the strong coupling at low energies leads to confinement: quarks and gluons cannot exist as free particles but are permanently bound into color-neutral hadrons. This has no analog in QED, where the coupling is weak at all accessible energies."
  explanation: "Additional consequences include the existence of glueballs (bound states of pure glue, with no quarks), the rich spectrum of hadrons, jet production in high-energy collisions (reflecting the underlying quark-gluon dynamics), and the QCD phase transition at high temperature (deconfinement). All trace back to the non-abelian self-interaction."
```

## Explainer

Quantum electrodynamics is a gauge theory based on the abelian group U(1): the gauge transformation is multiplication by a phase e^{i alpha(x)}, and the single gauge boson (the photon) is electrically neutral. **Non-abelian gauge theories**, introduced by Yang and Mills in 1954, generalize this to non-commutative groups like SU(2) and SU(3). The gauge field A^a_mu now carries an index a labeling the generators of the group, and the gauge bosons themselves carry charge under the gauge group.

The key mathematical difference is in the **field strength tensor**. In QED, F_{mu nu} = partial_mu A_nu - partial_nu A_mu is linear in the gauge field. In a non-abelian theory, F^a_{mu nu} = partial_mu A^a_nu - partial_nu A^a_mu + g f^{abc} A^b_mu A^c_nu, where f^{abc} are the structure constants of the group (encoding the commutation relations of the generators). The extra term, quadratic in A, means that the kinetic energy -(1/4)F^a_{mu nu}F^{a mu nu} contains cubic and quartic terms in the gauge field. These are the **self-interaction vertices** of the gauge bosons -- a three-gluon vertex and a four-gluon vertex -- which have no counterpart in QED.

Quantization of non-abelian gauge theories introduces additional complications. The gauge freedom must be fixed to avoid integrating over physically equivalent field configurations. The standard method (Faddeev-Popov procedure) introduces **ghost fields** -- anticommuting scalar fields that are not physical particles but are needed to maintain unitarity in covariant gauges. In Feynman diagrams, ghosts appear as internal lines (drawn as dashed lines) in loop calculations, canceling the contributions of unphysical gauge boson polarizations. In abelian gauge theories, ghosts decouple and can be ignored.

The physical consequences of gluon self-interaction are profound. The most important is **asymptotic freedom**: unlike QED where the coupling grows at high energies, the QCD coupling decreases at high energies. This is because gluon loop contributions to the vacuum polarization (which come from the self-interaction) overwhelm the fermion loop contributions and have the opposite sign. Asymptotic freedom means QCD is perturbative at short distances (explaining the success of perturbative QCD in describing hard scattering) but strongly coupled at long distances (explaining confinement). The entire structure of the strong interaction -- from the proton mass to jet production -- follows from the non-abelian nature of SU(3).
