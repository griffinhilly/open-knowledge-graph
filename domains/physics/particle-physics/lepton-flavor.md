---
id: lepton-flavor
title: Lepton Flavor
domain: physics
course: particle-physics
prerequisites:
- id: neutrino-mixing-pmns-matrix
  type: hard
- id: standard-model-overview
  type: hard
tags:
- lepton-flavor
- lepton-universality
- charged-lepton-flavor-violation
- flavor-anomalies
stage: expert
status: validated
---

# Lepton Flavor

## Core Idea
In the Standard Model, lepton flavor (electron number, muon number, tau number) is conserved in charged-lepton interactions to extraordinary precision, with neutrino oscillations being the only observed lepton-flavor-violating process. Lepton flavor universality -- the principle that the gauge bosons couple identically to all three lepton generations -- is a fundamental prediction of the Standard Model. Tests of both conservation and universality are sensitive probes of new physics.

## Questions

```yaml
- question: "The branching ratio for mu -> e gamma (a charged lepton flavor violating process) is predicted to be less than 10^{-54} in the Standard Model with massive neutrinos, yet current experiments (MEG II) have sensitivity to branching ratios of ~10^{-13}. Why is there such an enormous gap, and why do experimentalists keep searching?"
  type: multiple-choice
  options:
    - "Because the experimental limit will eventually reach the Standard Model prediction"
    - "Because the SM rate is suppressed by (m_nu/M_W)^4 ~ 10^{-50}, making it unobservably small — but many BSM models (supersymmetry, leptoquarks, heavy neutral leptons) predict rates that could be as large as 10^{-13} to 10^{-15}, so any observation of mu -> e gamma would be unambiguous evidence for new physics"
    - "Because the Standard Model prediction is uncertain and could be much larger"
    - "Because the process is forbidden by a conservation law that might be approximate"
  answer: 1
  explanation: "In the SM with neutrino masses, mu -> e gamma occurs through a loop diagram with a W boson and a neutrino, but the amplitude is proportional to Delta m^2_nu / M_W^2 ~ 10^{-25}, giving a branching ratio ~ 10^{-54}. This is a consequence of the GIM mechanism in the lepton sector. BSM models with new particles at the TeV scale can generate rates many orders of magnitude larger because the loop particles are heavier and the couplings need not be aligned with the neutrino mass matrix. The current limit BR(mu -> e gamma) < 3.1 x 10^{-13} from MEG already constrains many BSM scenarios."

- question: "Lepton flavor universality (LFU) predicts that the W boson couples with equal strength to e*nu_e, mu*nu_mu, and tau*nu_tau. The most precise test comes from the ratios R(D(*)) = BR(B -> D(*) tau nu) / BR(B -> D(*) l nu) where l = e, mu. What has been the experimental status of R(D(*))?"
  type: short-answer
  answer: "Measurements of R(D) and R(D*) by BaBar, Belle, and LHCb have consistently shown values about 2-3 sigma above the Standard Model prediction, suggesting enhanced B -> D(*) tau nu rates relative to the light-lepton modes. The combined world average shows a tension at the ~3 sigma level. If confirmed, this would imply a violation of lepton flavor universality in b -> c tau nu transitions, possibly mediated by new particles (charged Higgs, leptoquarks, W') that couple preferentially to the third generation. However, the significance has fluctuated as new measurements are added, and no single measurement is definitive."
  explanation: "The R(D(*)) anomalies are among the most watched results in flavor physics. Unlike the neutral-current b -> s anomalies (which could be explained by form factor uncertainties), R(D(*)) involves tree-level decays with well-controlled hadronic uncertainties, making a new-physics explanation more compelling. Belle II and LHCb Run 3 will provide the data needed to resolve the question."

- question: "The tau lepton decays to hadrons about 65% of the time and to lighter leptons about 35% of the time. The ratio of tau -> mu nu nu to tau -> e nu nu branching ratios tests lepton universality between muons and electrons. The measured ratio is consistent with 1 to what precision?"
  type: multiple-choice
  options:
    - "About 50%"
    - "About 0.2% — after accounting for the phase space difference from the muon mass, the ratio g_mu/g_e = 1.0018 +/- 0.0014, consistent with universality at the permille level"
    - "About 10%"
    - "The ratio has never been measured"
  answer: 1
  explanation: "The tau decay rates to e*nu*nu and mu*nu*nu differ slightly due to the muon mass (phase space suppression), but the underlying coupling is predicted to be identical by LFU. After correcting for this, the ratio tests LFU at the 0.2% level. Similarly, the ratio of pi -> e*nu to pi -> mu*nu (helicity-suppressed for the electron channel) tests LFU at the 0.1% level. Any deviation from universality would signal new physics that distinguishes between lepton generations."
```

## Explainer

**Lepton flavor** in the Standard Model is structured by two key principles: conservation of individual lepton numbers (L_e, L_mu, L_tau) and universality of gauge couplings across generations. Conservation means that in any Standard Model process (ignoring neutrino oscillations), the number of electrons minus positrons, muons minus antimuons, and taus minus antitaus are separately conserved. Universality means the W, Z, and photon couple identically to all three charged lepton generations.

Neutrino oscillations demonstrate that **lepton flavor is not exactly conserved** -- a muon neutrino can become a tau neutrino. This is analogous to quark mixing via the CKM matrix but has a crucial difference: the resulting charged-lepton flavor violation (CLFV) in the SM is suppressed by (m_nu/M_W)^4 ~ 10^{-50}, rendering processes like mu -> e gamma, tau -> mu gamma, and mu -> e conversion in nuclei completely unobservable. This GIM-like suppression makes CLFV a "zero-background" probe: any observation would be unambiguous new physics. Experiments like MEG II (mu -> e gamma), Mu2e and COMET (mu -> e conversion), and Belle II (tau -> mu gamma) push sensitivity to branching ratios of 10^{-13} to 10^{-16}.

**Lepton flavor universality** is tested in multiple ways. In the charged-current sector, the ratios of W -> l nu partial widths (measured at LEP) are consistent with universality to 0.3%. In the tau sector, the ratios of leptonic decay rates test universality at 0.2%. In the B meson sector, the ratios R(K(*)) = BR(B -> K(*) mu mu) / BR(B -> K(*) ee) test universality in neutral-current b -> s transitions, and R(D(*)) tests it in charged-current b -> c transitions. Several of these measurements have shown tensions with SM predictions at the 2-3 sigma level, generating intense interest in possible new physics.

The theoretical implications of lepton flavor physics extend beyond the Standard Model. If CLFV is discovered, the pattern of rates (which channels are enhanced, the relative rates of mu vs tau processes) would point toward the type of new physics responsible. **Leptoquarks**, which couple quarks to leptons and naturally break lepton universality, are a leading candidate for explaining the B-physics anomalies. **Supersymmetric models** predict CLFV from slepton mixing. The interplay between CLFV searches, B-physics anomalies, and direct searches at the LHC forms a powerful multi-pronged test of the Standard Model's lepton sector.
