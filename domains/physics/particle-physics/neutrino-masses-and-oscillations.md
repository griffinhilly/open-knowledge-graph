---
id: neutrino-masses-and-oscillations
title: Neutrino Masses and Oscillations
domain: physics
course: particle-physics
prerequisites:
- id: standard-model-overview
  type: hard
- id: special-relativity-postulates
  type: hard
tags:
- neutrino-oscillations
- neutrino-mass
- atmospheric-neutrinos
- solar-neutrinos
stage: expert
status: validated
---

# Neutrino Masses and Oscillations

## Core Idea
Neutrino oscillations -- the quantum mechanical transformation of one neutrino flavor into another during propagation -- provide direct evidence that neutrinos have nonzero masses, which is the first confirmed physics beyond the minimal Standard Model. The oscillation probability depends on the mass-squared differences Delta m^2, the mixing angles, and the baseline-to-energy ratio L/E, and the phenomenon has been observed in solar, atmospheric, reactor, and accelerator neutrinos.

## Questions

```yaml
- question: "A muon neutrino produced in the atmosphere with energy E = 1 GeV travels a distance L through the Earth. The probability of it being detected as a muon neutrino is approximately P(nu_mu -> nu_mu) = 1 - sin^2(2*theta_23) * sin^2(1.27 * Delta m^2_{32} * L/E), where Delta m^2 is in eV^2, L in km, and E in GeV. What physical effect causes this disappearance?"
  type: multiple-choice
  options:
    - "The neutrino decays into lighter particles during propagation"
    - "The neutrino flavor state nu_mu is a superposition of mass eigenstates nu_2 and nu_3, which propagate with slightly different phases (because they have different masses); after traveling distance L, the phase difference causes the flavor composition to change — the muon neutrino has partially transformed into a tau neutrino"
    - "The neutrino interacts with matter in the Earth and changes flavor"
    - "The neutrino loses energy and falls below the detection threshold"
  answer: 1
  explanation: "Neutrino oscillation is a quantum interference effect. The flavor state |nu_mu> = cos(theta_23)|nu_2> + sin(theta_23)|nu_3> evolves as each mass eigenstate accumulates a phase proportional to m_i^2 * L / (2E). The resulting phase difference is proportional to Delta m^2 * L/E. After propagation, the overlap with |nu_mu> is reduced and the overlap with |nu_tau> is enhanced. The Super-Kamiokande experiment observed this effect in 1998 for atmospheric neutrinos, finding a strong zenith-angle-dependent deficit of upward-going muon neutrinos (which travel ~13,000 km through the Earth) compared to downward-going ones (~15 km), consistent with oscillation with Delta m^2_{32} ~ 2.5 x 10^{-3} eV^2."

- question: "Neutrino oscillation experiments measure mass-squared differences (Delta m^2_{21} ~ 7.5 x 10^{-5} eV^2 and |Delta m^2_{32}| ~ 2.5 x 10^{-3} eV^2) but not the absolute mass scale. Why can't oscillation experiments determine the individual neutrino masses?"
  type: short-answer
  answer: "The oscillation probability depends on the phase difference between mass eigenstates, which is proportional to (m_i^2 - m_j^2) * L / (2E) = Delta m^2_{ij} * L / (2E). An overall shift of all masses by the same amount does not change any Delta m^2 and therefore does not affect oscillation. For example, m_1 = 0.1 eV, m_2 = 0.1005 eV and m_1 = 1.0 eV, m_2 = 1.0005 eV give the same Delta m^2 = 10^{-4} eV^2. The absolute mass scale must be determined by other methods: beta decay endpoint measurements (KATRIN, current limit m_beta < 0.45 eV), neutrinoless double beta decay (sensitive to the Majorana mass), or cosmological constraints from the CMB and large-scale structure (sum of masses < ~0.12 eV from Planck)."
  explanation: "The unknown absolute mass scale also means we don't know the 'mass ordering': whether m_3 is the heaviest (normal ordering) or lightest (inverted ordering). Determining the ordering is a primary goal of current experiments (JUNO, DUNE, Hyper-K) and has implications for neutrinoless double beta decay and cosmology."

- question: "The solar neutrino problem -- a deficit of electron neutrinos from the Sun compared to theoretical predictions -- was resolved by the SNO experiment in 2001. SNO detected all three neutrino flavors and found that the total neutrino flux agreed with the solar model prediction."
  type: true-false
  answer: true
  explanation: "Previous experiments (Homestake, Kamiokande, SAGE, GALLEX) detected only electron neutrinos and found about 1/3 to 1/2 of the expected flux. SNO used heavy water (D_2O), which enabled three detection channels: charged current (CC, sensitive only to nu_e), neutral current (NC, sensitive to all flavors equally), and elastic scattering (ES, sensitive to all flavors but enhanced for nu_e). The CC rate confirmed the deficit, but the NC rate showed the total flux agreed with the solar model. The missing electron neutrinos had oscillated into muon and tau neutrinos. This result, combined with the matter-enhanced oscillation (MSW effect) in the Sun, determined the solar oscillation parameters: Delta m^2_{21} ~ 7.5 x 10^{-5} eV^2 and theta_12 ~ 34 degrees."
```

## Explainer

**Neutrino oscillations** are the first and so far only confirmed phenomenon requiring physics beyond the minimal Standard Model. The Standard Model as originally formulated contains only left-handed neutrinos with zero mass (no right-handed neutrino fields, no Yukawa couplings, no mass terms). The discovery that neutrinos oscillate between flavors -- implying they have nonzero masses and mix -- was recognized with the 2015 Nobel Prize (Kajita and McDonald, for Super-Kamiokande and SNO).

The oscillation formalism is analogous to quark mixing but involves the **PMNS matrix** (Pontecorvo-Maki-Nakagawa-Sakata) relating the three flavor eigenstates (nu_e, nu_mu, nu_tau) to the three mass eigenstates (nu_1, nu_2, nu_3). The oscillation probability in vacuum for two flavors is P(nu_alpha -> nu_beta) = sin^2(2*theta) * sin^2(Delta m^2 * L / 4E). The full three-flavor case involves three mixing angles (theta_12, theta_13, theta_23), one CP-violating phase (delta_CP), and two mass-squared differences. All three angles have been measured: theta_12 ~ 34 degrees (solar, large), theta_23 ~ 49 degrees (atmospheric, near-maximal), theta_13 ~ 8.5 degrees (reactor, small but nonzero -- measured by Daya Bay, RENO, Double Chooz in 2012).

In matter, neutrino oscillations are modified by the **MSW effect** (Mikheyev-Smirnov-Wolfenstein): electron neutrinos experience an additional potential from coherent forward scattering on electrons (via W exchange), which modifies the effective mass-squared difference and mixing angle. In the Sun, this effect produces a resonant enhancement of oscillation that converts the majority of electron neutrinos to other flavors. The MSW effect is also what makes it possible to determine the neutrino mass ordering using long-baseline experiments or atmospheric neutrinos propagating through the Earth.

The major open questions in neutrino physics are: (1) the **mass ordering** -- is nu_3 the heaviest (normal) or lightest (inverted)? (2) the value of the **CP phase** delta_CP -- is there CP violation in the lepton sector, and if so, how much? (3) are neutrinos **Dirac or Majorana** particles -- do neutrinos have distinct antiparticles, or are they their own antiparticle? The first two will be addressed by DUNE, Hyper-Kamiokande, and JUNO in the coming decade. The third requires observing neutrinoless double beta decay, a process that violates lepton number and is possible only if neutrinos are Majorana fermions.
