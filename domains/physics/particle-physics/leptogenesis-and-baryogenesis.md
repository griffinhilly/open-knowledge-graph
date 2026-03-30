---
id: leptogenesis-and-baryogenesis
title: Leptogenesis and Baryogenesis
domain: physics
course: particle-physics
prerequisites:
- id: cp-violation
  type: hard
- id: neutrino-masses-and-oscillations
  type: hard
- id: bsm-overview
  type: soft
tags:
- baryogenesis
- leptogenesis
- matter-antimatter-asymmetry
- sakharov-conditions
stage: expert
status: validated
---

# Leptogenesis and Baryogenesis

## Core Idea
The observed universe contains far more matter than antimatter (baryon-to-photon ratio eta ~ 6 x 10^{-10}), an asymmetry that cannot be explained by the Standard Model alone. Baryogenesis mechanisms must satisfy the three Sakharov conditions: baryon number violation, C and CP violation, and departure from thermal equilibrium. Leptogenesis -- generating a lepton asymmetry from the decay of heavy right-handed neutrinos, which is then partially converted to a baryon asymmetry by electroweak sphalerons -- is one of the most compelling scenarios.

## Questions

```yaml
- question: "The Sakharov conditions for generating a matter-antimatter asymmetry are: (1) baryon number violation, (2) C and CP violation, (3) departure from thermal equilibrium. The Standard Model satisfies all three conditions in principle. Why is the SM insufficient to explain the observed baryon asymmetry?"
  type: multiple-choice
  options:
    - "Because baryon number is exactly conserved in the Standard Model"
    - "Because while the SM has all three ingredients (sphaleron processes violate B+L, the CKM phase provides CP violation, and the electroweak phase transition provides departure from equilibrium), the amount of CP violation is too small by ~10 orders of magnitude, and for m_H = 125 GeV the electroweak phase transition is a smooth crossover rather than the required first-order transition"
    - "Because the SM predicts equal amounts of matter and antimatter"
    - "Because the Sakharov conditions require physics at the Planck scale"
  answer: 1
  explanation: "Electroweak sphalerons (non-perturbative field configurations) violate B+L but conserve B-L, satisfying condition (1). The CKM phase provides CP violation, but its contribution to the baryon asymmetry is proportional to a Jarlskog-like invariant that is tiny (~10^{-20}), failing condition (2) quantitatively. For condition (3), a first-order electroweak phase transition would provide the necessary departure from equilibrium, but the Higgs mass of 125 GeV makes the transition a smooth crossover. Both conditions (2) and (3) must be enhanced by new physics."

- question: "In thermal leptogenesis, the lightest right-handed neutrino N_1 decays to lepton-Higgs pairs (N_1 -> l H and N_1 -> l-bar H-bar). CP violation in the interference between tree and loop diagrams produces a lepton asymmetry. What is the Davidson-Ibarra bound?"
  type: short-answer
  answer: "The Davidson-Ibarra bound is an upper limit on the CP asymmetry epsilon_1 in the decay of N_1: |epsilon_1| <= (3 M_1 / (16 pi v^2)) * (m_3 - m_1), where M_1 is the mass of N_1, v = 246 GeV is the Higgs vev, and m_3, m_1 are the heaviest and lightest light neutrino masses. For hierarchical light neutrinos with m_3 ~ sqrt(Delta m^2_{atm}) ~ 0.05 eV, successful leptogenesis requires M_1 > ~10^9 GeV. This implies that the right-handed neutrinos must be very heavy, and the mechanism cannot be directly tested at colliders. However, the connection between leptogenesis and neutrino masses (through the seesaw mechanism) makes it a testable framework: the neutrino mass matrix parameters constrain the leptogenesis parameter space."
  explanation: "The Davidson-Ibarra bound is one of the most important results in leptogenesis because it sets a minimum scale for the mechanism. Alternative scenarios (resonant leptogenesis, where two right-handed neutrinos are nearly degenerate) can evade this bound and allow leptogenesis at lower scales, potentially within reach of collider experiments."

- question: "Electroweak sphalerons convert a lepton asymmetry into a baryon asymmetry. This conversion is described by the relation B = (28/79) * (B - L) in the SM (or B = (8/23) * (B - L) in the MSSM). Why is B - L the relevant quantity?"
  type: multiple-choice
  options:
    - "Because B - L is easier to measure than B or L separately"
    - "Because electroweak sphalerons violate B + L but conserve B - L — any primordial B + L asymmetry is washed out by sphalerons in thermal equilibrium, while the B - L asymmetry is preserved; leptogenesis generates a nonzero B - L (specifically L != 0 with initial B = 0), which sphalerons then redistribute into both B and L, creating the observed baryon asymmetry"
    - "Because B and L are not individually defined in the Standard Model"
    - "Because B - L is quantized while B + L is not"
  answer: 1
  explanation: "Sphalerons are non-perturbative electroweak processes that change B and L by multiples of 3 (one unit per generation) while keeping B - L fixed. At temperatures above ~100 GeV, sphalerons are in thermal equilibrium and efficiently erase any B + L asymmetry. Leptogenesis produces L != 0 (and B = 0), giving B - L = -L. Sphalerons then convert this to B = (28/79) * (B - L) and L = -(51/79) * (B - L), producing the observed baryon asymmetry. This is why B - L must be nonzero for any baryogenesis mechanism that operates above the electroweak scale."
```

## Explainer

The **matter-antimatter asymmetry** of the universe is one of the most profound puzzles in physics. The observed baryon-to-photon ratio eta ~ 6 x 10^{-10}, measured from Big Bang nucleosynthesis and the CMB, means that for every billion antiprotons in the early universe, there were one billion and one protons. This tiny excess survived after all the matter-antimatter pairs annihilated, leaving the residual baryons that make up all visible matter today. Generating this asymmetry dynamically (baryogenesis) requires physics beyond the Standard Model.

**Electroweak baryogenesis** attempts to generate the asymmetry at the electroweak phase transition (~100 GeV). If the transition were strongly first-order, expanding bubbles of the broken phase would provide the out-of-equilibrium condition, and CP-violating interactions of particles with the bubble walls would produce a baryon asymmetry through sphaleron processes. However, in the SM with m_H = 125 GeV, the transition is a smooth crossover, not first-order. Extensions of the Higgs sector (additional scalars, as in the two-Higgs-doublet model or NMSSM) can make the transition first-order, but these models are constrained by Higgs coupling measurements and direct searches. Electroweak baryogenesis also requires new sources of CP violation beyond the CKM phase.

**Leptogenesis** is the leading alternative, elegantly connecting the baryon asymmetry to neutrino physics. In the type-I seesaw mechanism, heavy right-handed Majorana neutrinos N_i with masses M_i ~ 10^{9-15} GeV generate tiny left-handed neutrino masses through m_nu ~ m_D^2/M_N. These same heavy neutrinos, decaying out of equilibrium in the early universe with CP-violating asymmetry, produce a lepton asymmetry that sphalerons partially convert to a baryon asymmetry. The elegance of leptogenesis is that it uses particles (right-handed neutrinos) already motivated by neutrino masses and requires CP violation already hinted at by neutrino oscillation data.

Testing leptogenesis is challenging because the right-handed neutrinos are typically too heavy to produce at colliders. However, the connection to low-energy neutrino parameters provides indirect tests: the CP phase delta_CP measured in oscillation experiments is related (though not identical) to the high-energy CP violation driving leptogenesis. **Resonant leptogenesis** (where M_1 ~ M_2, enhancing the CP asymmetry) and **ARS (Akhmedov-Rubakov-Smirnov) leptogenesis** (using GeV-scale sterile neutrinos) offer scenarios testable at the LHC or future experiments like SHiP. The discovery of neutrinoless double beta decay would confirm the Majorana nature of neutrinos, a necessary ingredient for the seesaw mechanism and standard leptogenesis.
