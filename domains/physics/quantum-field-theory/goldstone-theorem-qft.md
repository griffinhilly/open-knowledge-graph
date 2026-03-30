---
id: goldstone-theorem-qft
title: Goldstone Theorem
domain: physics
course: quantum-field-theory
prerequisites:
- id: spontaneous-symmetry-breaking-qft
  type: hard
- id: goldstone-theorem
  type: soft
tags:
- goldstone-theorem
- goldstone-boson
- nambu
stage: expert
status: validated
---

# Goldstone Theorem

## Core Idea
Goldstone's theorem states that when a continuous global symmetry is spontaneously broken, one massless scalar boson (Goldstone boson) appears for each broken symmetry generator. These bosons correspond to excitations along the flat directions of the potential. The theorem is exact in relativistic field theory but is evaded when the broken symmetry is gauged (Higgs mechanism).

## Questions

```yaml
- question: "A theory has a global SU(3) symmetry that is spontaneously broken to SU(2). How many Goldstone bosons appear?"
  type: multiple-choice
  options:
    - "3"
    - "5"
    - "8"
    - "6"
  answer: 1
  explanation: "SU(3) has 8 generators and SU(2) has 3 generators. The number of broken generators is 8 - 3 = 5, so Goldstone's theorem predicts 5 massless scalar bosons. Each broken generator corresponds to a flat direction in the field space, and excitations along each flat direction produce one Goldstone boson. The unbroken SU(2) generators correspond to massive modes (or to the symmetry that still constrains the spectrum)."

- question: "Pions (pi+, pi-, pi0) are often called 'pseudo-Goldstone bosons' of QCD. They are very light (approximately 140 MeV) but not exactly massless. Why aren't they exactly massless as the Goldstone theorem would predict?"
  type: multiple-choice
  options:
    - "Because the pion is a composite particle, not an elementary scalar"
    - "Because the chiral symmetry SU(2)_L x SU(2)_R of QCD is not an exact symmetry — it is explicitly (though softly) broken by the small but nonzero up and down quark masses, making the Goldstone bosons 'pseudo' with small but nonzero masses proportional to sqrt(m_q)"
    - "Because confinement modifies the Goldstone theorem"
    - "Because pions interact with each other, which generates a mass"
  answer: 1
  explanation: "In the limit of zero quark masses, QCD has an exact SU(2)_L x SU(2)_R chiral symmetry that is spontaneously broken to SU(2)_V (isospin) by the quark condensate <q-bar q> != 0. This produces three exactly massless Goldstone bosons — the pions. The physical quark masses (m_u ~ 2 MeV, m_d ~ 5 MeV) explicitly break chiral symmetry, giving the pions small masses: m_pi^2 proportional to m_q. The pion mass (140 MeV) is much smaller than other hadron masses (proton: 938 MeV) because it is suppressed by the small quark masses. This is the most dramatic physical manifestation of the Goldstone theorem."

- question: "Goldstone's theorem applies only to global symmetries. When a local (gauge) symmetry is spontaneously broken, the would-be Goldstone bosons are 'eaten' by the gauge bosons."
  type: true-false
  answer: true
  explanation: "This is the Higgs mechanism. When a gauge symmetry is spontaneously broken, the Goldstone bosons do not appear as physical massless particles. Instead, they become the longitudinal polarization components of the gauge bosons, which thereby acquire mass. The gauge boson goes from two polarization states (transverse, massless) to three (two transverse plus one longitudinal, massive). The number of degrees of freedom is conserved: the Goldstone scalar becomes the third polarization of the gauge boson. This is sometimes described as the gauge boson 'eating' the Goldstone boson and getting 'fat' (massive)."

- question: "Prove that the Goldstone boson is massless by considering small fluctuations around the vacuum in a theory with spontaneously broken U(1) symmetry."
  type: short-answer
  answer: "Write phi = (v + rho(x)) e^{i theta(x)/v}, where v is the vacuum expectation value, rho is the radial fluctuation, and theta is the angular fluctuation. The potential V depends only on |phi|^2 = (v + rho)^2, so it is independent of theta entirely. Since V has no theta-dependence, the mass term for theta (which would be proportional to d^2V/d theta^2 at the vacuum) is exactly zero. The kinetic term for theta survives: |partial_mu phi|^2 contains (partial_mu theta)^2/2, which is the kinetic term of a massless scalar field. Therefore theta is a massless scalar — the Goldstone boson. The field rho has mass m_rho^2 = d^2V/d rho^2 |_{rho=0} = 2 mu^2 > 0."
  explanation: "This argument generalizes to any symmetry group: for each broken generator, there is a direction in field space along which the potential is flat (no restoring force), producing a massless excitation. The number of flat directions equals the number of broken generators. This is the intuitive content of Goldstone's theorem."
```

## Explainer

Goldstone's theorem, proved by Goldstone, Salam, and Weinberg in 1962, is one of the cornerstone results of quantum field theory. Its statement is precise: if a quantum field theory has a continuous global symmetry group G that is spontaneously broken to a subgroup H (meaning the vacuum is invariant under H but not under all of G), then the theory contains dim(G) - dim(H) massless scalar particles, one for each broken generator. These are the **Goldstone bosons** (or Nambu-Goldstone bosons, honoring Nambu's earlier work).

The proof is elegant. Consider the conserved Noether current j^mu associated with a broken symmetry generator. The charge Q = integral j^0 d^3x does not annihilate the vacuum: Q|0> != 0 (this is what "broken" means). This implies that Q|0> is a state with the same energy as the vacuum (because [H, Q] = 0 -- the Hamiltonian respects the symmetry) but different quantum numbers. Taking the Fourier transform shows that this state has zero momentum and zero mass -- it is a massless particle created by the current j^mu from the vacuum. The matrix element <0|j^mu(0)|pi(p)> = i f_pi p^mu is nonzero, where f_pi is the "decay constant" of the Goldstone boson.

The most important physical example is in **QCD**. The approximate chiral symmetry SU(2)_L x SU(2)_R (exact in the limit of massless up and down quarks) is spontaneously broken to SU(2)_V by the formation of a quark condensate <q-bar q> != 0. The three broken generators produce three Goldstone bosons: the pions (pi+, pi-, pi0). Because the quark masses are small but not zero, chiral symmetry is also explicitly broken, giving the pions small masses proportional to sqrt(m_q). The pion mass hierarchy (m_pi = 140 MeV << m_proton = 938 MeV) is a direct consequence of the Goldstone mechanism applied to the approximate chiral symmetry of QCD.

In the context of gauge theories, Goldstone's theorem is modified by the **Higgs mechanism**. When the broken symmetry is a local (gauge) symmetry rather than a global one, the Goldstone bosons do not appear as physical particles. Instead, they provide the longitudinal degree of freedom that a massless gauge boson needs to become massive. The counting works out: a massless gauge boson has 2 polarizations, a massive one has 3, and the extra polarization comes from the eaten Goldstone boson. This is how the W and Z bosons of the Standard Model acquire their masses.
