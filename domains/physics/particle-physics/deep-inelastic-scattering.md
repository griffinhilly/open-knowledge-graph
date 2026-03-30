---
id: deep-inelastic-scattering
title: Deep Inelastic Scattering
domain: physics
course: particle-physics
prerequisites:
- id: quark-model-hadron-spectroscopy
  type: hard
- id: feynman-diagrams-systematic
  type: hard
- id: cross-sections-decay-rates
  type: hard
tags:
- deep-inelastic-scattering
- dis
- structure-functions
- scaling
stage: expert
status: validated
---

# Deep Inelastic Scattering

## Core Idea
Deep inelastic scattering (DIS) is the process of probing the internal structure of nucleons by scattering high-energy leptons off them. The observation of Bjorken scaling -- that structure functions depend on the dimensionless ratio x = Q^2/(2M*nu) rather than on Q^2 and nu independently -- provided the first direct evidence that protons contain point-like constituents (partons), confirming the quark model.

## Questions

```yaml
- question: "In deep inelastic electron-proton scattering, the structure function F_2(x) measures the momentum distribution of charged partons inside the proton. If the proton contained only three free quarks (uud), what would F_2(x) look like?"
  type: multiple-choice
  options:
    - "Three delta functions at x = 1/3, each carrying one-third of the proton momentum"
    - "A smooth distribution peaked at x = 1/3, because the quarks share momentum equally"
    - "A broad distribution peaked at moderate x, because the quarks are bound and exchange momentum through gluon interactions — but the integral of F_2 over x would equal the sum of e_i^2 times the momentum fractions, which for three valence quarks would account for all the proton's momentum"
    - "A flat distribution from x = 0 to x = 1"
  answer: 2
  explanation: "If quarks were non-interacting, each would carry exactly 1/3 of the proton momentum and F_2(x) would have delta-function peaks. In reality, gluon exchange smears the momentum distribution. The valence quarks produce a broad distribution peaked around x ~ 0.15-0.3. Crucially, integrating x*f(x) for all quarks gives only about 50% of the proton momentum -- the other 50% is carried by gluons, which are electrically neutral and invisible to photon exchange. This 'momentum sum rule' violation was key evidence for gluons."

- question: "Bjorken scaling states that the proton structure functions F_1(x,Q^2) and F_2(x,Q^2) depend only on x and not on Q^2 at high Q^2. This scaling is exact in QCD."
  type: true-false
  answer: false
  explanation: "Bjorken scaling holds at leading order in the parton model (non-interacting point-like quarks), but QCD corrections produce logarithmic violations: the structure functions depend weakly on Q^2 through terms proportional to alpha_s * ln(Q^2/mu^2). As Q^2 increases, gluon radiation produces more sea quarks at low x and depletes quarks at high x. These scaling violations are described by the DGLAP evolution equations and are one of the most precise tests of QCD. The violations were observed experimentally and their agreement with QCD predictions earned Gross, Politzer, and Wilczek the 2004 Nobel Prize."

- question: "DIS experiments measure the ratio R = sigma_L/sigma_T of longitudinal to transverse virtual photon cross sections. The Callan-Gross relation predicts R = 0 for spin-1/2 partons. Why?"
  type: short-answer
  answer: "A massless spin-1/2 particle conserves helicity, so it cannot absorb a longitudinally polarized virtual photon (which would require a helicity flip). This gives sigma_L = 0 and hence R = 0, or equivalently F_2 = 2xF_1 (the Callan-Gross relation). Experimentally, R is small but nonzero (a few percent), consistent with QCD corrections from gluon radiation and nonzero quark masses. If partons were spin-0 (scalar), sigma_T would vanish instead. The measurement of R ~ 0 at SLAC was direct evidence that partons have spin 1/2 and are therefore quarks."
  explanation: "The Callan-Gross relation connects the spin of the partons to a measurable ratio of cross sections. Its approximate validity was among the first confirmations that the point-like partons observed in DIS were indeed quarks."

- question: "The kinematic variable x in DIS is often called 'Bjorken x.' In the infinite-momentum frame, x has a simple physical interpretation. What is it?"
  type: multiple-choice
  options:
    - "The scattering angle of the electron"
    - "The fraction of the proton's momentum carried by the struck parton"
    - "The energy of the virtual photon divided by the proton mass"
    - "The number of quarks participating in the interaction"
  answer: 1
  explanation: "In a frame where the proton has very large momentum P, a parton carrying momentum fraction x has 4-momentum xP. The virtual photon with 4-momentum q strikes this parton elastically, and the kinematics require x = Q^2/(2P*q) = Q^2/(2M*nu). This identification of x as the parton momentum fraction is exact in the parton model and receives small corrections in QCD. The distribution of partons as a function of x is encoded in the parton distribution functions f_i(x)."
```

## Explainer

**Deep inelastic scattering** was the experimental breakthrough that revealed the quark substructure of the proton. In the late 1960s, experiments at SLAC scattered high-energy electrons off protons and observed that the cross section remained large even at high momentum transfer Q^2 -- behavior characteristic of scattering off point-like objects, not a diffuse charge distribution. This was the proton analog of Rutherford scattering: just as alpha particles revealed the nucleus inside the atom, high-energy electrons revealed quarks inside the proton.

The kinematics of DIS are described by two independent variables: the momentum transfer squared Q^2 = -q^2 (the "resolution" of the virtual photon probe) and the energy transfer nu = E - E' (the energy lost by the electron). Bjorken's insight was that at large Q^2, the structure functions depend only on the dimensionless ratio x = Q^2/(2M*nu), not on Q^2 and nu independently. This **Bjorken scaling** implies that the electron is scattering elastically off point-like constituents -- partons -- each carrying a fraction x of the proton's momentum. The structure functions then measure the parton distribution functions: F_2(x) = sum_i e_i^2 x f_i(x), where f_i(x) is the probability of finding parton i with momentum fraction x and e_i is its charge.

The parton model reveals that the proton is far more complex than three valence quarks. At low x, the proton contains a "sea" of virtual quark-antiquark pairs and gluons, continuously created and annihilated by QCD interactions. Gluons carry about half the proton's momentum but are invisible to the electromagnetic probe (they are neutral). The evidence for gluons came from the momentum sum rule: integrating x*f(x) over all quark flavors gives only ~50% of the proton momentum, with the remainder attributed to gluons. Direct evidence for gluons followed from three-jet events at PETRA in 1979.

QCD predicts specific **scaling violations** -- logarithmic Q^2 dependence of the structure functions described by the DGLAP (Dokshitzer-Gribov-Lipatov-Altarelli-Parisi) evolution equations. As Q^2 increases, the virtual photon resolves finer structure: gluon radiation produces more quark-antiquark pairs at low x while depleting quarks at high x. The quantitative agreement between measured scaling violations and DGLAP predictions over four decades in Q^2 is one of the most precise tests of QCD and earned the 2004 Nobel Prize for the discovery of asymptotic freedom.
