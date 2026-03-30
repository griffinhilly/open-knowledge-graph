---
id: electroweak-precision-measurements
title: Electroweak Precision Measurements
domain: physics
course: particle-physics
prerequisites:
- id: electroweak-unification
  type: hard
- id: standard-model-overview
  type: hard
tags:
- electroweak
- precision-tests
- lep
- radiative-corrections
stage: expert
status: validated
---

# Electroweak Precision Measurements

## Core Idea
Electroweak precision measurements test the Standard Model at the quantum loop level. Quantities like the W mass, the effective weak mixing angle sin^2(theta_eff), and the Z decay widths are measured with permille-level precision and compared to predictions that include radiative corrections sensitive to virtual top quarks and the Higgs boson. These measurements predicted the top quark mass before its discovery and constrain possible new physics beyond the Standard Model.

## Questions

```yaml
- question: "The Z boson mass (91.1876 +/- 0.0021 GeV) and width (2.4952 +/- 0.0023 GeV) were measured with extraordinary precision at LEP. The total width depends on the number of light neutrino species N_nu. How does this measurement work?"
  type: multiple-choice
  options:
    - "Each neutrino species is directly detected and counted"
    - "The total Z width Gamma_Z = Gamma_had + 3*Gamma_l + N_nu*Gamma_nu, where Gamma_had and Gamma_l are measured from visible decays; the invisible width Gamma_inv = Gamma_Z - Gamma_had - 3*Gamma_l then determines N_nu = Gamma_inv/Gamma_nu, where Gamma_nu is the Standard Model prediction for one neutrino species"
    - "The Z lineshape is narrower for fewer neutrinos because there are fewer decay channels"
    - "Neutrinos produce missing energy events that are directly counted"
  answer: 1
  explanation: "LEP measured the Z lineshape (cross section vs. center-of-mass energy) with extreme precision. The visible decays (hadrons and charged leptons) determine Gamma_had and Gamma_l. Subtracting these from the total width gives the invisible width. Dividing by the Standard Model prediction for Z -> nu nu-bar gives N_nu = 2.984 +/- 0.008, consistent with exactly 3 and ruling out a fourth light neutrino. This is one of the most precise counting experiments in physics."

- question: "Before the top quark was discovered in 1995 at the Tevatron, electroweak precision data from LEP and SLD predicted its mass to be approximately 170-180 GeV. How could virtual particles that had never been directly observed be 'weighed'?"
  type: short-answer
  answer: "Radiative corrections from virtual top quarks in loop diagrams affect electroweak observables. The top quark appears in W and Z self-energy corrections, and its contribution depends on m_t^2 (quadratic sensitivity, unlike the Higgs which enters logarithmically). For example, the rho parameter rho = M_W^2/(M_Z^2 * cos^2(theta_W)) receives a correction delta-rho proportional to G_F * m_t^2. By measuring M_W, M_Z, sin^2(theta_eff), and other observables to high precision, and computing the loop corrections as functions of m_t and m_H, a global fit determines the preferred values of m_t and m_H. The prediction m_t = 173 +/- 13 GeV (before discovery) was confirmed when the top quark was found at 173.1 GeV."
  explanation: "This predictive success demonstrated that the Standard Model is not just a tree-level theory but a precision quantum field theory whose loop structure is quantitatively correct. It also showed the power of indirect constraints: virtual particles modify measurable quantities through quantum corrections."

- question: "The W boson mass is one of the most important electroweak precision observables. At tree level, M_W = M_Z * cos(theta_W). Loop corrections shift M_W by several hundred MeV. These corrections are dominated by the top quark and, to a lesser extent, the Higgs boson."
  type: true-false
  answer: true
  explanation: "At tree level, the relationship M_W = M_Z * cos(theta_W) is exact, giving M_W approximately 79.8 GeV. Radiative corrections, dominated by top quark loops (delta M_W ~ +290 MeV from the top) and Higgs boson loops (delta M_W ~ -40 MeV for m_H = 125 GeV), shift this to M_W approximately 80.36 GeV. The current experimental world average (80.3692 +/- 0.0133 GeV) agrees with the Standard Model prediction at the level of a few MeV. Any discrepancy would be evidence for new physics contributing to the loop corrections. A 2022 CDF measurement claiming M_W = 80.4335 +/- 0.0094 GeV was in tension with the SM but has not been confirmed by other experiments."
```

## Explainer

**Electroweak precision measurements** represent the Standard Model's most stringent quantitative tests. The key observables -- M_Z, Gamma_Z, M_W, sin^2(theta_eff), asymmetries at the Z pole, the W and top quark masses -- are measured to permille-level precision and compared with theoretical predictions that include radiative corrections computed to multi-loop accuracy. The agreement between measurement and prediction is typically at the level of a few standard deviations across dozens of observables, a remarkable success for a theory with 19 parameters.

The **global electroweak fit** combines all precision observables into a chi-squared minimization that determines the Standard Model parameters and tests for internal consistency. The key inputs are: the Z lineshape parameters from LEP (M_Z, Gamma_Z, sigma_had^0, R_l, A_FB), the W mass and width from LEP-2 and the Tevatron, the effective mixing angle from LEP/SLD asymmetries, and the top quark mass from the Tevatron and LHC. The fit has impressive predictive power: before the top quark discovery, it predicted m_t within 15 GeV; before the Higgs discovery, it predicted m_H within a factor of 2. The post-Higgs fit has no remaining free parameters and provides an overconstrained test of the theory.

The sensitivity to virtual particles arises through **radiative corrections** -- loop diagrams involving particles too heavy to produce directly. The top quark contributes to the W and Z self-energies through loops like W -> t bbar -> W, and these corrections are proportional to m_t^2 (quadratic sensitivity from the large Yukawa coupling). The Higgs contributes proportional to ln(m_H), a weaker dependence. New physics (supersymmetric particles, extra gauge bosons, composite Higgs) would add additional loop contributions that shift the precision observables, so the agreement with the Standard Model constrains the mass scale and coupling strength of possible new particles.

The precision of these tests continues to improve. The LHC has measured M_W and m_t with increasing precision, and the FCC-ee (Future Circular Collider) proposes to run at the Z pole, WW threshold, and top threshold with luminosities 10^4-10^5 times higher than LEP. This would improve the precision on sin^2(theta_eff) by an order of magnitude, providing sensitivity to new physics at mass scales well beyond direct LHC reach. Electroweak precision measurements remain one of the most powerful indirect probes of physics beyond the Standard Model.
