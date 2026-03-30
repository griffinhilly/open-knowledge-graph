---
id: standard-model-overview
title: Standard Model Overview
domain: physics
course: quantum-field-theory
prerequisites:
- id: electroweak-unification
  type: hard
- id: qcd-basics
  type: hard
- id: higgs-mechanism
  type: hard
tags:
- standard-model
- particle-physics
- gauge-theory
stage: expert
status: validated
---

# Standard Model Overview

## Core Idea
The Standard Model is the quantum field theory of all known fundamental interactions except gravity. It is based on the gauge group SU(3)_C x SU(2)_L x U(1)_Y, with matter content consisting of three generations of quarks and leptons, and the Higgs doublet. Its 19 free parameters are determined by experiment. Every prediction has been confirmed, including the Higgs boson discovery in 2012.

## Questions

```yaml
- question: "The Standard Model has 19 free parameters (or 26 if neutrino masses and mixing are included). These include gauge couplings, Yukawa couplings, the Higgs potential parameters, and the QCD vacuum angle. Why can't these parameters be derived from the theory itself?"
  type: multiple-choice
  options:
    - "Because computers are not powerful enough to solve the equations"
    - "Because the Standard Model specifies the structure of the interactions (which particles exist, how they couple) but not the numerical values of the couplings — these are inputs that must be measured experimentally, and a deeper theory would be needed to predict them"
    - "Because the parameters change with energy scale, so there is no single set of values"
    - "Because quantum mechanics introduces fundamental randomness into the parameters"
  answer: 1
  explanation: "The gauge group, the particle content, and the form of the Lagrangian are determined by symmetry and renormalizability, but the numerical values of the couplings are not. Why are there three generations? Why is the top quark 340,000 times heavier than the electron? Why is the strong coupling approximately 1 at the GeV scale? The Standard Model cannot answer these questions — they are its free parameters. A more fundamental theory (such as a grand unified theory or string theory) might derive some of these values from a smaller set of principles, but no such derivation exists today."

- question: "The Standard Model successfully describes the electromagnetic, weak, and strong interactions. Gravity is not included because it is too weak to matter at particle physics energies."
  type: true-false
  answer: false
  explanation: "The real reason gravity is not included is not its weakness but its non-renormalizability. General relativity, when quantized using standard QFT methods, produces ultraviolet divergences that cannot be absorbed into a finite number of counterterms — the theory requires infinitely many parameters and loses predictive power at energies near the Planck scale (~10^{19} GeV). At energies accessible to particle experiments (up to ~10^4 GeV), gravitational effects are indeed negligible (the ratio of gravitational to electromagnetic force between two protons is ~10^{-36}), so ignoring gravity is a practical success. But the theoretical exclusion is fundamental: we do not know how to consistently quantize gravity in the Standard Model framework."

- question: "Every prediction of the Standard Model has been confirmed experimentally, with no established deviations. Yet physicists are certain the Standard Model is incomplete. Give three reasons why."
  type: short-answer
  answer: "1) Neutrino masses: The Standard Model (in its minimal form) predicts massless neutrinos, but neutrino oscillation experiments prove that neutrinos have small but nonzero masses. 2) Dark matter: Astrophysical observations (galaxy rotation curves, gravitational lensing, CMB) show that approximately 27% of the universe's energy density is dark matter, which does not correspond to any Standard Model particle. 3) Matter-antimatter asymmetry: The observed universe contains far more matter than antimatter, but the CP violation in the Standard Model is insufficient to generate this asymmetry from an initially symmetric state. Additional issues include the hierarchy problem (why is the Higgs mass ~125 GeV rather than ~10^{19} GeV?), the strong CP problem, dark energy, and the absence of quantum gravity."
  explanation: "The Standard Model is simultaneously the most successful and the most obviously incomplete theory in physics. It works perfectly within its domain but clearly points to physics beyond itself. This is the situation in particle physics today: we know the Standard Model is not the final theory but do not yet know what replaces it."

- question: "The Standard Model Lagrangian, written out in full, fits on a single page. How can such a compact expression describe the enormous variety of physical phenomena we observe?"
  type: multiple-choice
  options:
    - "Because each term in the Lagrangian corresponds to many different physical processes through the Feynman diagram expansion — a single interaction vertex generates infinitely many scattering amplitudes at different orders in perturbation theory"
    - "Because the Standard Model only describes simple phenomena"
    - "Because most physical phenomena are described by the kinetic terms alone"
    - "Because the Lagrangian is written in shorthand notation that hides its true complexity"
  answer: 0
  explanation: "The Lagrangian encodes the fundamental interactions compactly, but the perturbative expansion generates an infinite hierarchy of processes. The single QED vertex (electron-photon coupling) generates Compton scattering, pair production, Bremsstrahlung, the Lamb shift, and countless other processes through different Feynman diagrams. Multiply this by the full particle content and three gauge interactions, and the combinatorial richness is enormous. The Standard Model Lagrangian is compact because it specifies the rules; the consequences of those rules fill volumes."
```

## Explainer

The **Standard Model** of particle physics is a quantum field theory based on the gauge group SU(3)_C x SU(2)_L x U(1)_Y. SU(3)_C is the color gauge group of QCD, mediating the strong interaction via 8 gluons. SU(2)_L x U(1)_Y is the electroweak gauge group, mediating the weak and electromagnetic interactions via the W+, W-, Z, and photon. The Higgs doublet breaks the electroweak symmetry to U(1)_EM, giving mass to the W, Z, and all charged fermions.

The matter content consists of three **generations** of quarks and leptons. Each generation contains an up-type quark, a down-type quark, a charged lepton, and a neutrino: (u, d, e, nu_e), (c, s, mu, nu_mu), (t, b, tau, nu_tau). Left-handed fermions form SU(2)_L doublets; right-handed fermions are singlets. Quarks carry color charge (SU(3) triplets); leptons do not (SU(3) singlets). The three generations are identical in their gauge quantum numbers but differ in their Yukawa couplings (and hence masses) -- why three generations exist, and why their masses span five orders of magnitude, is unexplained.

The Standard Model has **19 free parameters** (in its minimal form): 3 gauge couplings (g_s, g, g'), 6 quark masses, 3 lepton masses, 3 CKM mixing angles and 1 CP-violating phase, the Higgs vacuum expectation value v, the Higgs self-coupling lambda, and the QCD vacuum angle theta. Including neutrino masses and mixing adds 7 more (3 masses, 3 angles, 1 or 2 CP phases). All are measured experimentally; the theory does not predict their values.

The experimental success of the Standard Model is extraordinary. QED predictions agree with experiment to 12 significant figures (electron g-2). Electroweak precision measurements at LEP predicted the top quark mass before its discovery. The Higgs boson, predicted by the theory, was discovered at the LHC in 2012. QCD describes jet production, scaling violations, and the running of alpha_s with percent-level accuracy. Despite this, the Standard Model is known to be incomplete: neutrino oscillations require physics beyond the minimal model, dark matter and dark energy have no Standard Model explanation, and gravity is not included. The Standard Model is best understood as an extraordinarily successful **effective field theory** valid up to some energy scale, beyond which new physics must appear.
