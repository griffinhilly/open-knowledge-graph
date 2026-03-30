---
id: quark-model-hadron-spectroscopy
title: Quark Model and Hadron Spectroscopy
domain: physics
course: particle-physics
prerequisites:
- id: qcd-basics
  type: hard
- id: angular-momentum-quantum
  type: hard
- id: spin
  type: hard
tags:
- quark-model
- hadrons
- mesons
- baryons
- spectroscopy
stage: expert
status: validated
---

# Quark Model and Hadron Spectroscopy

## Core Idea
The quark model classifies all observed hadrons as bound states of quarks: mesons are quark-antiquark pairs and baryons are three-quark states. Combining quark flavors, spins, and orbital angular momenta using SU(3) flavor symmetry and angular momentum addition rules reproduces the observed hadron spectrum, including the pseudoscalar and vector meson octets, the baryon octet and decuplet, and their excited states.

## Questions

```yaml
- question: "The lightest mesons (pions, kaons, eta) form a nonet under SU(3) flavor symmetry. The nonet decomposes as 3 x 3-bar = 8 + 1: an octet plus a singlet. Why do we observe a nonet (nine particles) rather than separate octet and singlet multiplets?"
  type: multiple-choice
  options:
    - "Because the octet and singlet are exact eigenstates and all nine happen to have similar masses"
    - "Because SU(3) flavor symmetry is only approximate (broken by quark mass differences), so the physical eta and eta-prime are mixtures of the octet and singlet states — the mixing means all nine states are interrelated and best described together as a nonet"
    - "Because there are nine possible quark-antiquark combinations and each one is a separate particle"
    - "Because confinement forces all nine states to have the same mass"
  answer: 1
  explanation: "If SU(3) flavor were exact (m_u = m_d = m_s), the octet and singlet would be separate, non-mixing multiplets. But the strange quark is heavier (~95 MeV vs ~5 MeV for u,d), breaking SU(3) and allowing mixing between the I=0, S=0 members of the octet and singlet. For pseudoscalars, this produces the eta (~548 MeV, mostly octet) and eta-prime (~958 MeV, mostly singlet). The large eta-prime mass also receives a contribution from the axial anomaly. For vector mesons, the analogous mixing produces the omega and phi, where the phi is nearly pure s-sbar."

- question: "The Delta++ baryon has charge +2, spin 3/2, and is composed of three up quarks (uuu). In the quark model, this state appears to violate the Pauli exclusion principle because all three quarks are in the same state."
  type: true-false
  answer: false
  explanation: "This apparent paradox was one of the original motivations for introducing color charge. Three identical fermions in the same spatial and spin state would indeed violate the Pauli principle if there were no additional quantum number. But each quark carries one of three colors (red, green, blue), and the baryon wavefunction is totally antisymmetric in color (the color singlet epsilon_{ijk}). The full wavefunction is then antisymmetric: symmetric in space x spin x flavor (all u, all spin-up, ground state) times antisymmetric in color. The Pauli principle is satisfied, and the Delta++ is allowed."

- question: "The quark model predicts that no hadrons exist with quantum numbers that cannot be made from qqbar (mesons) or qqq (baryons). What are 'exotic' hadrons, and what is their current experimental status?"
  type: short-answer
  answer: "Exotic hadrons are states whose quantum numbers or quark content cannot be explained by the simple qqbar or qqq picture. These include tetraquarks (qqbar-qqbar), pentaquarks (qqqq-qbar), glueballs (bound states of gluons), and hybrid mesons (qqbar-g). QCD does not forbid these states — it only requires them to be color singlets. Since 2003, multiple exotic candidates have been observed: the X(3872), the Z_c and Z_b charged charmonium-like states, and the P_c pentaquark states discovered at LHCb. Their internal structure (compact multiquark state vs. loosely bound meson molecule) remains debated."
  explanation: "The existence of exotic hadrons does not contradict the quark model but extends it. The quark model's success in classifying the conventional hadron spectrum was so complete that exotics were long thought to be absent. Their discovery has reinvigorated hadron spectroscopy as a field."

- question: "In the quark model, the proton (uud) and neutron (udd) both have spin 1/2. How do three spin-1/2 quarks combine to give spin 1/2 for the nucleon ground state, and why isn't the ground state spin 3/2?"
  type: multiple-choice
  options:
    - "The quarks have orbital angular momentum that cancels some of the spin"
    - "Two of the three quarks form a spin-0 pair, and the third quark carries the nucleon's spin 1/2 — this configuration is energetically favored over the fully aligned spin-3/2 state (which is the Delta baryon, approximately 300 MeV heavier)"
    - "One of the quarks has its spin quantum number reduced by confinement"
    - "The nucleon is actually a mixture of spin-1/2 and spin-3/2 states"
  answer: 1
  explanation: "Three spin-1/2 quarks can couple to total spin S = 3/2 (all aligned) or S = 1/2 (one pair anti-aligned). In the ground state (L=0), the S=1/2 state is the nucleon (proton/neutron) and the S=3/2 state is the Delta. The mass difference (~300 MeV) is due to the color-magnetic interaction (the QCD analog of the spin-spin interaction), which is attractive for anti-aligned spins and repulsive for aligned spins. This hyperfine splitting is proportional to (sigma_i dot sigma_j)/(m_i m_j) and explains mass splittings throughout the hadron spectrum."
```

## Explainer

The **quark model**, developed by Gell-Mann and Zweig in 1964, organizes all known hadrons as composite states of quarks. Mesons are quark-antiquark (qqbar) pairs and baryons are three-quark (qqq) states, with each state required to be a color singlet under SU(3)_C. The quantum numbers of a hadron -- spin, parity, charge conjugation, isospin, strangeness -- follow from combining the quantum numbers of its constituent quarks using standard angular momentum addition rules.

The light hadron spectrum is organized by **SU(3) flavor symmetry**, which treats the up, down, and strange quarks as an approximate triplet. Mesons (qqbar) decompose as 3 x 3-bar = 8 + 1, giving octets and singlets. Baryons (qqq) decompose as 3 x 3 x 3 = 10 + 8 + 8 + 1, and the ground-state baryons fill the spin-1/2 octet (proton, neutron, Sigma, Xi, Lambda) and the spin-3/2 decuplet (Delta, Sigma*, Xi*, Omega-). The prediction and subsequent discovery of the Omega- baryon (sss, spin 3/2) in 1964 was a dramatic confirmation of the model.

Mass splittings within and between multiplets arise from two sources: the **quark mass differences** (m_s >> m_u, m_d breaks SU(3) flavor symmetry) and the **color-magnetic hyperfine interaction** (the spin-spin interaction between quarks mediated by one-gluon exchange). The hyperfine interaction explains why the Delta is heavier than the nucleon, why the rho is heavier than the pion, and why the Sigma is heavier than the Lambda -- in each case, the state with aligned quark spins is heavier. These splittings provide a window into the QCD dynamics inside hadrons.

Excited hadrons with nonzero orbital angular momentum L fill out additional multiplets: the L=1 mesons include the a_1, b_1, f_1 states, while L=1 baryons include the N(1520) and N(1535) resonances. The **Regge trajectories** -- plots of spin J versus mass-squared M^2 -- show remarkably linear relationships, reflecting the string-like behavior of the confining flux tube between quarks. While the quark model is not a rigorous derivation from QCD (it uses constituent quarks with effective masses of ~300 MeV, much larger than the current quark masses), it remains an indispensable organizing principle for hadron physics.
