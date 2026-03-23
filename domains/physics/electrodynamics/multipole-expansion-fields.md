---
id: multipole-expansion-fields
title: Multipole Expansion of Electromagnetic Fields
domain: physics
course: electrodynamics
prerequisites:
- id: scalar-vector-potentials
  type: hard
- id: laplace-poisson-equations-electrostatics
  type: soft
- id: taylor-series
  type: soft
- id: spherical-coordinates
  type: soft
builds-toward:
- radiation-accelerating-charges
tags:
- multipole-expansion
- systematic-expansion
stage: expert
status: draft
---

# Multipole Expansion of Electromagnetic Fields

## Core Idea
Multipole expansion systematically expresses electromagnetic fields far from localized sources as a series of monopole, dipole, quadrupole, and higher moments. Each term falls off as a higher power of 1/r, allowing truncation at low order for distant observation points. This expansion reveals which multipoles dominate in different frequency regimes and provides physical insight into radiation mechanisms.

## Questions

```yaml
- question: "A physicist is calculating the electric potential far from a water molecule (which is electrically neutral). Which term in the multipole expansion will dominate, and why?"
  type: multiple-choice
  options:
    - "The monopole term, because it falls off most slowly as 1/r"
    - "The dipole term, because the monopole vanishes for a neutral molecule and water has a non-zero dipole moment"
    - "The quadrupole term, because molecular charge distributions are always quadrupolar"
    - "All terms contribute equally at large distances"
  answer: 1
  explanation: "The monopole term is proportional to the total charge Q. Since water is electrically neutral (Q = 0), the monopole term vanishes exactly. The dipole term is proportional to the first moment of the charge distribution p = ∫ρ r dV. Water is a highly polar molecule — the oxygen carries partial negative charge and the hydrogens carry partial positive charge, giving a large permanent dipole moment. For a neutral polar molecule, the dipole is the leading non-vanishing term. This is why the 'dipole approximation' is standard in molecular electrostatics and spectroscopy."

- question: "In the multipole expansion, why does each successive multipole term (monopole → dipole → quadrupole → ...) fall off more rapidly with distance r?"
  type: multiple-choice
  options:
    - "Higher multipoles involve smaller charges, so they are inherently weaker"
    - "The expansion is a Taylor series in r'/r where r' is source size; each higher-order term gains an additional factor of r'/r, which is small in the far field"
    - "Higher multipoles involve more complicated charge arrangements that cancel more at large distances"
    - "This is an empirical fact with no simple mathematical explanation"
  answer: 1
  explanation: "The multipole expansion comes from expanding 1/|r − r'| in powers of r'/r using Legendre polynomials. Each multipole of order ℓ corresponds to P_ℓ(cos θ)/r^(ℓ+1): the monopole (ℓ=0) goes as 1/r, dipole (ℓ=1) as 1/r², quadrupole (ℓ=2) as 1/r³. Each successive term gains one more factor of 1/r. In the far field (r ≫ r'), each successive term gains a factor of r'/r ≪ 1 — making it negligible compared to the previous. This is why truncating at low order is valid far from the source."

- question: "For a system with zero net charge (electric monopole = 0), the dipole term is guaranteed to be the leading contribution to the electrostatic potential at large distances."
  type: true-false
  answer: false
  explanation: "The monopole term vanishes for a neutral system, making the dipole the next candidate — but the dipole moment can also be zero. CO₂ (linear, symmetric) and CH₄ (tetrahedral) are neutral AND have zero dipole moment. In such cases the quadrupole term leads. A charge distribution with zero total charge AND zero dipole moment will have its potential dominated by the quadrupole. The multipole expansion is a hierarchy: each term leads only if all lower-order terms vanish."

- question: "The multipole expansion is most useful close to the source, where the source's detailed structure matters and the higher multipole moments are significant."
  type: true-false
  answer: false
  explanation: "This is exactly backwards. The multipole expansion is valid in the FAR FIELD — when the observation point distance r is much larger than the source size r'. In this regime, each successive multipole term is smaller by a factor of r'/r ≪ 1, so truncating at low order is a controlled approximation. Close to the source, higher multipoles are significant and the series requires many terms. The whole point of the expansion is that it organizes what the field looks like from far away, where the source's fine structure is irrelevant and only the lowest non-vanishing multipoles matter."

- question: "Why is truncating the multipole expansion at low order justified in the far-field regime? What determines which multipole term dominates in a given situation?"
  type: short-answer
  answer: "Truncation is justified because the expansion is in powers of (r'/r), where r' characterizes the source size and r is the observation distance. In the far field (r ≫ r'), each successive term is smaller by r'/r ≪ 1 — so the dipole is r'/r times smaller than the monopole, the quadrupole (r'/r)² times smaller, etc. Which term dominates is determined by the lowest-order non-vanishing moment: if total charge Q ≠ 0, the monopole dominates; if Q = 0 but dipole moment p ≠ 0, the dipole dominates; if both vanish, the quadrupole leads. The expansion provides systematic control over exactly what you are neglecting."
  explanation: "The multipole expansion organizes the physics of distant fields by separating 'how quickly does it fall off?' (multipole order) from 'how large is the relevant quantity?' (multipole moment value). The framework is powerful because it reduces an arbitrary source distribution to a small number of numbers (monopole, dipole moment, quadrupole tensor, ...) that capture all the distant field behavior."
```

## Explainer

From your study of scalar and vector potentials you know that once you have the charge and current distribution, the fields follow from the potentials via differential operations. The difficulty is that real sources are always extended — a molecule, an antenna, a nucleus — not a single point. The **multipole expansion** is a systematic way to describe what such a source looks like from far away, by expanding the potential in powers of (r'/r), where r' is the size of the source and r is your distance from it. When r ≫ r', each successive term in the expansion is smaller by a factor of r'/r.

The first term is the **monopole**: it depends only on the total charge Q and falls off as Q/r. An electrically neutral system — any atom or molecule — has zero monopole, so this term vanishes. The next term is the **dipole**: it depends on the charge distribution's first moment **p** = Σ qᵢ **r**ᵢ (or ∫ρ **r** dV for a continuous distribution) and falls off as 1/r². A water molecule has a permanent electric dipole moment; two charges ±q separated by distance d form a dipole with p = qd. Because most neutral objects have non-zero dipole moments, the dipole term often dominates at large distances. The next term is the **quadrupole**, falling off as 1/r³, followed by octupole at 1/r⁴, and so on. Each higher multipole requires finer spatial structure in the source to be nonzero, and each falls off faster with distance.

The Taylor series prerequisite makes the mathematical structure transparent. You expand 1/|**r** − **r**'| in Legendre polynomials (using spherical coordinates), and each Legendre polynomial P_ℓ(cos θ) corresponds to one multipole order: ℓ=0 is monopole, ℓ=1 is dipole, ℓ=2 is quadrupole. The physical content is that the source contributes to distant fields through an infinite hierarchy of shape descriptors — moments — and the hierarchy is ordered by how quickly each contribution decays with distance. Truncating at low order is valid whenever r ≫ r', which is precisely the far-field regime.

For radiation (time-varying sources), the same hierarchy applies but with important differences: all radiation fields fall off as 1/r (they must, to carry finite power through a sphere of any radius), but the radiated power from each multipole scales differently with frequency. **Electric dipole radiation** power scales as ω⁴; electric quadrupole scales as ω⁶; magnetic dipole as ω⁴ but suppressed by (v/c)². This is why the dipole approximation dominates in antenna theory and molecular spectroscopy: for slowly varying sources at large distances, the monopole and dipole terms tell you nearly everything, and the expansion provides the systematic framework to know exactly what you are neglecting when you stop there.
