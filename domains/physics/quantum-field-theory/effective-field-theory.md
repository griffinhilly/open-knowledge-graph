---
id: effective-field-theory
title: Effective Field Theory
domain: physics
course: quantum-field-theory
prerequisites:
- id: renormalization-group-qft
  type: hard
- id: renormalization-of-qed
  type: soft
tags:
- effective-field-theory
- eft
- power-counting
stage: expert
status: validated
---

# Effective Field Theory

## Core Idea
Effective field theory (EFT) is the framework for describing physics at a given energy scale without knowing the complete theory at higher energies. You write the most general Lagrangian consistent with the symmetries, organized by operator dimension. Higher-dimension operators are suppressed by powers of the high-energy scale Lambda, making their effects systematically small at low energies.

## Questions

```yaml
- question: "Fermi's theory of weak interactions describes beta decay using a four-fermion interaction G_F (psi-bar psi)(psi-bar psi), with Fermi constant G_F ~ 10^{-5} GeV^{-2}. This is an effective field theory. What is the 'UV completion' that Fermi's theory approximates?"
  type: multiple-choice
  options:
    - "QED with virtual photon exchange"
    - "The electroweak theory with W boson exchange — at energies much below M_W ~ 80 GeV, the W propagator 1/(q^2 - M_W^2) reduces to -1/M_W^2, collapsing the exchange to a point-like four-fermion vertex with G_F ~ g^2/M_W^2"
    - "QCD with gluon exchange"
    - "String theory"
  answer: 1
  explanation: "Fermi's theory is the low-energy limit of the electroweak theory. When the momentum transfer q is much less than M_W, the W boson propagator becomes approximately constant: 1/(q^2 - M_W^2) -> -1/M_W^2. The W exchange diagram then looks like a contact interaction between four fermions, with coupling G_F/sqrt(2) = g^2/(8M_W^2). Fermi's theory works beautifully for beta decay (q ~ MeV << M_W ~ 80 GeV) but fails at energies approaching M_W, where the momentum dependence of the W propagator matters and eventually the W boson appears as a real particle."

- question: "In EFT, higher-dimension operators are suppressed by powers of 1/Lambda (where Lambda is the high-energy scale). A dimension-6 operator is suppressed by 1/Lambda^2 relative to a dimension-4 operator. Why does this make EFT a systematic expansion?"
  type: multiple-choice
  options:
    - "Because Lambda is always infinite"
    - "Because at energies E << Lambda, the ratio (E/Lambda)^n decreases rapidly with n — dimension-6 operators contribute corrections of order (E/Lambda)^2, dimension-8 operators of order (E/Lambda)^4, and so on, giving a controlled perturbative expansion in powers of E/Lambda"
    - "Because higher-dimension operators are always zero"
    - "Because the EFT Lagrangian contains only finitely many operators"
  answer: 1
  explanation: "This is the power of EFT: at low energies, you can achieve any desired precision by including operators up to a finite dimension. For E/Lambda = 0.1, dimension-6 operators give 1% corrections, dimension-8 give 0.01% corrections, etc. The unknown high-energy physics affects low-energy observables only through these suppressed operators, and the leading effects can be parameterized by a finite number of Wilson coefficients. The EFT breaks down when E approaches Lambda — at that scale, all operators contribute equally and the expansion is no longer useful."

- question: "The Standard Model itself is now widely regarded as an effective field theory valid up to some unknown scale Lambda. This is not a failure but a feature."
  type: true-false
  answer: true
  explanation: "Treating the Standard Model as an EFT (the 'Standard Model Effective Field Theory' or SMEFT) means adding all gauge-invariant higher-dimension operators to the Standard Model Lagrangian, suppressed by powers of a new physics scale Lambda. The leading new-physics effects come from dimension-6 operators. This framework allows systematic, model-independent searches for deviations from the Standard Model without committing to a specific beyond-the-Standard-Model theory. Current LHC data constrain many dimension-6 Wilson coefficients, pushing Lambda above several TeV for most operators."

- question: "Explain why non-renormalizable theories are not 'sick' but are perfectly well-defined effective field theories, and what changes about their predictive power compared to renormalizable theories."
  type: short-answer
  answer: "A non-renormalizable theory contains operators of dimension > 4 whose couplings have negative mass dimension (e.g., G_F ~ 1/M_W^2 in Fermi theory). These couplings introduce new divergences at each loop order that require new counterterms, so the theory has infinitely many parameters in principle. However, at energies E << Lambda, operators of dimension 4+n contribute at order (E/Lambda)^n, so only finitely many operators contribute at any given precision. The theory is predictive to any specified accuracy — you just need more measured parameters for higher precision. A renormalizable theory is the special case where the leading-order Lagrangian alone (dimension <= 4) suffices for all-orders predictions. The EFT framework is strictly more general and includes renormalizable theories as a special case."
  explanation: "This perspective, developed by Wilson and others in the 1970s-80s, revolutionized how physicists think about quantum field theory. Rather than dividing theories into 'renormalizable (good)' and 'non-renormalizable (bad),' the modern view is that all theories are effective, and renormalizability is a feature of the leading-order Lagrangian, not a requirement for consistency."
```

## Explainer

**Effective field theory** is perhaps the most important conceptual framework in modern theoretical physics. The central idea is that you do not need to know the complete theory of everything to make precise predictions at a given energy scale. You need only write down the most general Lagrangian consistent with the symmetries of the problem, organized by the dimension of the operators. Low-dimension operators dominate at low energies; high-dimension operators are suppressed and can be neglected to any desired precision.

The classic example is **Fermi's theory of the weak interaction**. At energies far below the W boson mass (80 GeV), the W propagator is effectively a constant, and W exchange looks like a local four-fermion interaction with coupling G_F approximately 10^{-5} GeV^{-2}. Fermi's theory is non-renormalizable (the four-fermion operator has dimension 6), but it makes excellent predictions for nuclear beta decay, muon decay, and neutrino scattering -- all processes at energies well below M_W. At energies approaching M_W, Fermi's theory breaks down and must be replaced by the full electroweak theory. The EFT tells you its own domain of validity.

The organizing principle is **dimensional analysis**. In four spacetime dimensions, the Lagrangian density has mass dimension 4. An operator of dimension d is multiplied by a coefficient of dimension 4 - d. For d > 4, this coefficient has negative mass dimension and is suppressed by powers of a high scale Lambda: c ~ 1/Lambda^{d-4}. At energies E << Lambda, the contribution of a dimension-d operator is suppressed by (E/Lambda)^{d-4}. This is why the Standard Model (which contains only dimension-4 operators at leading order) works so well: any new physics at a high scale Lambda manifests only through tiny corrections of order (E/Lambda)^2.

The modern view is that **all quantum field theories are effective**. The Standard Model is an EFT valid up to some unknown scale. General relativity is an EFT of gravity valid below the Planck scale. Chiral perturbation theory is an EFT of low-energy QCD. In each case, the theory makes precise, testable predictions within its domain of validity, and its breakdown signals the onset of new physics. The EFT framework converts what was once seen as a deficiency (non-renormalizability, ignorance of high-energy physics) into a virtue: systematic, controlled approximation with quantifiable uncertainties.
