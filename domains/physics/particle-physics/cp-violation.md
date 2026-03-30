---
id: cp-violation
title: CP Violation
domain: physics
course: particle-physics
prerequisites:
- id: ckm-matrix-quark-mixing
  type: hard
- id: cpt-theorem
  type: soft
tags:
- cp-violation
- matter-antimatter
- kaon-system
- baryogenesis
stage: expert
status: validated
---

# CP Violation

## Core Idea
CP violation -- the non-invariance of physical laws under the combined transformation of charge conjugation (C, swapping particle and antiparticle) and parity (P, mirror reflection) -- was discovered in 1964 in the neutral kaon system. In the Standard Model, CP violation arises from the complex phase in the CKM matrix. It is a necessary condition for generating the matter-antimatter asymmetry of the universe (one of the Sakharov conditions), though the amount of CP violation in the Standard Model appears insufficient to explain the observed asymmetry.

## Questions

```yaml
- question: "In 1964, Christenson, Cronin, Fitch, and Turlay observed that the long-lived neutral kaon (K_L, which should be CP-odd) decays to two pions (a CP-even state) at a rate of about 2 x 10^{-3}. What does this observation imply?"
  type: multiple-choice
  options:
    - "That pions are not CP eigenstates"
    - "That the weak interaction violates CP symmetry -- the physical K_L state is not a pure CP eigenstate but contains a small admixture of the CP-even component, parameterized by epsilon ~ 2.2 x 10^{-3}, and the decay K_L -> pi pi proceeds through this admixture (indirect CP violation) and/or through a direct CP-violating decay amplitude (epsilon-prime)"
    - "That the strong interaction violates CP"
    - "That the kaon mass measurement was incorrect"
  answer: 1
  explanation: "In the absence of CP violation, the neutral kaon mass eigenstates would be exact CP eigenstates: K_1 (CP-even, decaying to 2 pions) and K_2 (CP-odd, decaying to 3 pions). The observation of K_L -> 2 pions means K_L is not purely CP-odd. The parameter epsilon measures the CP impurity in the K_L state (indirect CP violation from K-Kbar mixing), while epsilon-prime measures CP violation directly in the decay amplitude. Both have been measured: |epsilon| ~ 2.2 x 10^{-3} and Re(epsilon'/epsilon) ~ 1.7 x 10^{-3}."

- question: "There are three types of CP violation: (1) in mixing, (2) in decay (direct), and (3) in the interference between mixing and decay. The golden measurement of CP violation in B physics is the asymmetry in B_d -> J/psi K_S, which measures sin(2*beta). Which type is this?"
  type: short-answer
  answer: "This is type (3): CP violation in the interference between B_d -> J/psi K_S (direct decay) and B_d -> B_d-bar -> J/psi K_S (mixing followed by decay). The time-dependent CP asymmetry is A_CP(t) = sin(2*beta) * sin(Delta m * t), where beta is an angle of the unitarity triangle and Delta m is the B_d mixing frequency. This measurement is theoretically clean because the J/psi K_S final state is accessible to both B and B-bar, and the hadronic uncertainties cancel in the asymmetry. The BaBar and Belle experiments measured sin(2*beta) = 0.699 +/- 0.017, establishing CP violation in the B system and confirming the CKM mechanism."
  explanation: "The measurement of sin(2*beta) was the primary physics goal of the B factory program. Its agreement with the CKM prediction (from the sides of the unitarity triangle measured independently) was a major validation of the three-generation Standard Model. This earned Kobayashi and Maskawa a share of the 2008 Nobel Prize."

- question: "The Standard Model predicts CP violation from the CKM phase, but the amount is far too small to explain the observed matter-antimatter asymmetry of the universe."
  type: true-false
  answer: true
  explanation: "The Sakharov conditions for baryogenesis require: (1) baryon number violation, (2) C and CP violation, and (3) departure from thermal equilibrium. The Standard Model satisfies all three in principle (baryon number violation from electroweak sphalerons, CP violation from the CKM phase, non-equilibrium from the electroweak phase transition). However, quantitative calculations show that the CP violation from the CKM matrix produces a baryon asymmetry roughly 10 orders of magnitude too small. Additionally, for m_H = 125 GeV, the electroweak phase transition is a smooth crossover rather than the first-order transition needed for departure from equilibrium. New sources of CP violation beyond the Standard Model are therefore required."
```

## Explainer

**CP violation** is one of the most profound features of the weak interaction and one of the deepest unsolved problems in physics. Discovered in 1964 in the decay K_L -> pi+ pi- (Cronin and Fitch, Nobel Prize 1980), it means that the laws of physics distinguish between matter and antimatter -- a universe made of antimatter would evolve differently from ours. In the Standard Model, CP violation is encoded in the single complex phase of the CKM matrix, predicted by Kobayashi and Maskawa in 1973 as a consequence of having three or more generations of quarks.

The neutral kaon system exhibits CP violation in two distinct ways. **Indirect CP violation** (parameterized by epsilon) arises from the slight CP impurity in the K_L mass eigenstate due to K-Kbar mixing. The mass eigenstates K_S and K_L are not exactly the CP eigenstates K_1 and K_2 but are rotated by an angle epsilon in the complex plane. **Direct CP violation** (parameterized by epsilon-prime) occurs when the decay amplitudes themselves violate CP. The ratio Re(epsilon'/epsilon) ~ 1.7 x 10^{-3} was measured after decades of effort by the NA48 and KTeV experiments, confirming that CP violation exists in the decay amplitude itself, not just in mixing.

The B meson system provides the most precise tests of the CKM mechanism of CP violation. The B_d and B_s mesons undergo rapid matter-antimatter oscillation, and the interference between mixing and decay produces time-dependent CP asymmetries that are directly related to angles of the unitarity triangle. The B factory experiments (BaBar, Belle) and LHCb have measured: sin(2*beta) from B -> J/psi K_S with 2% precision, the angle alpha from B -> pi pi and rho rho, and the angle gamma from B -> DK. All measurements are consistent with a single CKM phase, confirming the Standard Model picture to high accuracy.

Despite the success of the CKM description, the **cosmological matter-antimatter asymmetry** requires CP violation beyond the Standard Model. The observed baryon-to-photon ratio (~6 x 10^{-10}) is about 10 orders of magnitude larger than what CKM CP violation can produce. New sources of CP violation might exist in the lepton sector (leptogenesis via the neutrino mixing matrix), in extended Higgs sectors (additional scalar phases), or in supersymmetric models (new complex phases in squark and gaugino sectors). Searches for CP violation in the Higgs sector, in neutrino oscillations, and in electric dipole moments of fundamental particles are among the highest-priority experiments in particle physics.
