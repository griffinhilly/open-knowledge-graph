---
id: effective-field-theory-particle-physics
title: Effective Field Theory in Particle Physics
domain: physics
course: particle-physics
prerequisites:
- id: effective-field-theory
  type: hard
- id: standard-model-overview
  type: hard
tags:
- eft
- smeft
- higher-dimensional-operators
- power-counting
stage: expert
status: validated
---

# Effective Field Theory in Particle Physics

## Core Idea
Effective field theory (EFT) provides a systematic framework for parameterizing the effects of unknown high-energy physics on low-energy observables. The Standard Model Effective Field Theory (SMEFT) extends the SM Lagrangian by adding higher-dimensional operators suppressed by powers of a new physics scale Lambda. This approach is model-independent: any UV-complete BSM theory can be matched onto the SMEFT at low energies, making it the lingua franca for interpreting precision measurements in terms of new physics constraints.

## Questions

```yaml
- question: "The SMEFT Lagrangian is L = L_SM + sum_i (C_i / Lambda^2) * O_i^{(6)} + sum_j (C_j / Lambda^4) * O_j^{(8)} + ..., where O_i^{(d)} are operators of dimension d built from SM fields. At dimension 6, there are 2499 independent operators (for one generation of fermions, 59 operators; for three generations, 2499). Why are dimension-6 operators the leading BSM effects?"
  type: multiple-choice
  options:
    - "Because there are no dimension-5 operators"
    - "Because there is exactly one dimension-5 operator (the Weinberg operator, which generates Majorana neutrino masses), and after accounting for it, the leading new effects come from dimension-6 operators suppressed by 1/Lambda^2 — dimension-7 and higher operators are further suppressed by additional powers of 1/Lambda and are typically negligible if Lambda >> v (the Higgs vev)"
    - "Because dimension-6 operators are renormalizable"
    - "Because only dimension-6 operators conserve gauge symmetry"
  answer: 1
  explanation: "The dimension-5 Weinberg operator L = (C_5/Lambda) * (LH)(LH) (where L is the lepton doublet and H is the Higgs) generates neutrino masses m_nu ~ C_5 * v^2/Lambda after electroweak symmetry breaking. For Lambda ~ 10^{14} GeV and C_5 ~ 1, this gives m_nu ~ 0.05 eV, consistent with oscillation data. Aside from this unique operator, the leading BSM effects are from dimension-6 operators, which modify Higgs couplings, gauge boson self-interactions, fermion couplings, and produce new 4-fermion interactions. Each operator has a Wilson coefficient C_i that encodes the strength and sign of the new physics contribution."

- question: "A specific BSM model (e.g., a heavy Z' boson) can be 'matched' onto the SMEFT by integrating out the heavy particle and expressing the resulting effects as Wilson coefficients of SMEFT operators. Why is this matching useful?"
  type: short-answer
  answer: "Matching separates the model-specific UV physics (the Z' mass, couplings, and quantum numbers) from the model-independent low-energy effects (shifts in SM observables). Once a BSM model is matched onto the SMEFT, its predictions for all low-energy observables are encoded in a finite set of Wilson coefficients. Conversely, experimental measurements can constrain the Wilson coefficients model-independently, and these constraints can then be translated to any specific BSM model. This factorization means that each experimental measurement needs to be interpreted only once (in terms of Wilson coefficients), and each BSM model needs to be matched only once, rather than confronting every model with every measurement individually."
  explanation: "The SMEFT framework has become the standard for LHC Higgs coupling measurements, electroweak precision tests, and top quark measurements. Global fits to SMEFT Wilson coefficients combine hundreds of measurements and constrain the new physics scale Lambda to be above ~1-10 TeV for O(1) couplings, depending on the operator."

- question: "The SMEFT is valid when the new physics scale Lambda is well above the energies being probed (E << Lambda). At the LHC, some processes probe energies of several TeV. Under what conditions does the SMEFT description break down?"
  type: multiple-choice
  options:
    - "When the number of operators becomes too large to fit"
    - "When E approaches Lambda, the expansion in E/Lambda converges poorly or breaks down entirely — dimension-8 operators become as important as dimension-6, the truncation is no longer valid, and one must use the full UV-complete model; additionally, if the new particles can be directly produced (E > M_new), they appear as resonances rather than contact interactions, and the SMEFT description misses this qualitatively different signature"
    - "When the Wilson coefficients become negative"
    - "When more than one operator contributes to the same observable"
  answer: 1
  explanation: "The SMEFT is a perturbative expansion in E/Lambda. If Lambda = 2 TeV and the LHC probes E = 1 TeV, then E/Lambda = 0.5 and higher-order terms may not be negligible. In practice, SMEFT analyses must check the validity of the truncation (e.g., by including dimension-8 operators and verifying that their contributions are small). For processes at the highest LHC energies (tails of distributions), the SMEFT may be unreliable, and dedicated searches for resonances are complementary."
```

## Explainer

**Effective field theory** is the modern framework for organizing physics at different energy scales. The key insight is that low-energy physics does not depend on the details of high-energy physics, only on its symmetries and the values of a few parameters. In particle physics, the Standard Model itself is best understood as an EFT: it is the most general renormalizable (dimension-4) Lagrangian consistent with its gauge symmetry and particle content. BSM physics enters through higher-dimensional operators that parameterize our ignorance of the UV completion.

The **Standard Model Effective Field Theory (SMEFT)** adds to the SM Lagrangian all operators of dimension 5 and higher that respect the SU(3) x SU(2) x U(1) gauge symmetry. At dimension 5, there is a single operator (the Weinberg operator for neutrino masses). At dimension 6, the Warsaw basis enumerates 59 independent operators for one generation (2499 for three generations), affecting Higgs couplings, triple and quartic gauge boson vertices, fermion-gauge interactions, four-fermion contact interactions, and dipole operators. Each operator has a Wilson coefficient C_i/Lambda^2 that can be constrained by experiment.

**Global SMEFT fits** combine measurements from the LHC (Higgs production and decay, diboson production, top quark properties), LEP (electroweak precision observables), and lower-energy experiments (flavor physics, low-energy precision tests). The fits determine or constrain the Wilson coefficients, which can then be interpreted in terms of BSM models. For example, a deviation in the Higgs coupling to Z bosons would point to specific operators (O_HB, O_HW, O_HD), which could be generated by extended Higgs sectors, composite Higgs models, or heavy vector-like fermions. The SMEFT provides a systematic, model-independent language for this interpretive chain.

A complementary framework, **HEFT** (Higgs Effective Field Theory), relaxes the assumption that the Higgs is part of an SU(2) doublet and parameterizes the Higgs sector more generally. HEFT is appropriate if the Higgs is a composite state or if electroweak symmetry is nonlinearly realized. The distinction between SMEFT and HEFT corresponds to the question of whether the discovered 125 GeV scalar is an elementary doublet component (SMEFT) or something more exotic (HEFT). Precision Higgs coupling measurements at the HL-LHC and future colliders will eventually distinguish these possibilities by measuring the pattern of deviations from SM predictions with percent-level or sub-percent-level precision.
