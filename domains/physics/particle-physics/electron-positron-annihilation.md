---
id: electron-positron-annihilation
title: Electron-Positron Annihilation
domain: physics
course: particle-physics
prerequisites:
- id: feynman-diagrams-systematic
  type: hard
- id: qcd-basics
  type: hard
- id: cross-sections-decay-rates
  type: hard
tags:
- electron-positron
- r-ratio
- three-jet-events
- color-factor
stage: expert
status: validated
---

# Electron-Positron Annihilation

## Core Idea
Electron-positron annihilation into hadrons provides the cleanest probe of QCD because the initial state is purely leptonic (no PDFs). The ratio R = sigma(e+e- -> hadrons)/sigma(e+e- -> mu+mu-) directly counts quark colors and flavors, providing evidence for three colors. Multi-jet events in e+e- collisions provided the first direct evidence for the gluon and precision measurements of the strong coupling alpha_s.

## Questions

```yaml
- question: "The ratio R = sigma(e+e- -> hadrons)/sigma(e+e- -> mu+mu-) at center-of-mass energies well above quark thresholds but below the Z pole is predicted by the quark model. For five quark flavors (u, d, s, c, b), what value does the quark model predict, and what does it tell us about color?"
  type: multiple-choice
  options:
    - "R = 5 (one for each quark flavor)"
    - "R = N_c * sum of e_q^2 = 3 * (4/9 + 1/9 + 1/9 + 4/9 + 1/9) = 3 * 11/9 = 11/3 -- the factor of 3 comes from color, and the charges-squared sum over the five active flavors"
    - "R = 1 because all quarks produce the same final state (hadrons)"
    - "R = 3 (one for each color)"
  answer: 1
  explanation: "Each quark flavor contributes e_q^2 to the cross section (from the photon-quark coupling), multiplied by N_c = 3 for color. The sum over u, d, s, c, b gives (4/9 + 1/9 + 1/9 + 4/9 + 1/9) = 11/9, times 3 = 11/3 approximately 3.67. QCD corrections modify this to R = 11/3 * (1 + alpha_s/pi + ...). The measurement of R = 3.67 +/- small corrections, rather than R = 11/9 = 1.22 (which would result without color), was direct evidence for three colors."

- question: "In 1979, the TASSO experiment at PETRA observed three-jet events in e+e- annihilation. These events were the first direct evidence for the gluon. How does a third jet arise from the process e+e- -> hadrons?"
  type: short-answer
  answer: "At leading order, e+e- -> qqbar produces a quark-antiquark pair that hadronizes into two back-to-back jets. At next-to-leading order in QCD, one of the quarks can radiate a hard gluon: e+e- -> qqbar-g. If the gluon has sufficient energy and is emitted at a large angle, it hadronizes into a third jet distinct from the quark and antiquark jets. The rate and angular distribution of three-jet events are predicted by QCD (proportional to alpha_s) and confirmed the gluon as a spin-1 particle. The angular correlations between the three jets distinguish a spin-1 gluon from hypothetical spin-0 gluons."
  explanation: "The discovery of three-jet events was a landmark in particle physics. It confirmed not only the existence of the gluon but also its vector (spin-1) nature, consistent with being the gauge boson of SU(3). The four-jet rate (e+e- -> qqbar-gg or qqbar-qqbar) provided additional tests of the non-abelian structure of QCD."

- question: "At center-of-mass energy equal to the Z boson mass (91.2 GeV), the ratio R increases dramatically to approximately 20. Why?"
  type: multiple-choice
  options:
    - "New quark flavors become accessible at this energy"
    - "The Z boson resonance enhances the cross section enormously -- e+e- -> Z -> qqbar dominates over the photon diagram, and the Z couples to quarks with both vector and axial-vector couplings that are larger than the photon's electromagnetic coupling"
    - "QCD corrections become very large at 91 GeV"
    - "The quarks become asymptotically free and the cross section diverges"
  answer: 1
  explanation: "At the Z pole, the process e+e- -> Z -> hadrons dominates. The Z couples to all quarks (including qqbar pairs with charge 0 total), and its coupling strength (proportional to the weak mixing angle and the quark quantum numbers) greatly exceeds the electromagnetic coupling. The Z pole cross section is sigma ~ 12*pi/M_Z^2 * Gamma_e*Gamma_had/Gamma_tot^2. The LEP experiments at CERN made precision measurements of the Z lineshape, extracting the number of light neutrino species (N_nu = 2.984 +/- 0.008) from the total width."
```

## Explainer

**Electron-positron annihilation** is the theoretically cleanest process in particle physics. The initial state is completely specified -- two point-like leptons with known energy -- so there are no parton distribution functions and no beam remnants. This makes e+e- collisions ideal for precision tests of QCD and electroweak physics. The major e+e- facilities have included SPEAR, PETRA, PEP, TRISTAN, LEP, and SLC, with center-of-mass energies ranging from a few GeV to 209 GeV.

The **R ratio** is the most fundamental QCD observable in e+e- physics. At energies far from resonances, R = sigma(e+e- -> hadrons)/sigma(e+e- -> mu+mu-) = N_c * sum(e_q^2) * (1 + alpha_s/pi + ...), where the sum runs over quark flavors kinematically accessible at that energy. The step-like increase of R as new quark thresholds are crossed (charm at ~3 GeV, bottom at ~10 GeV) maps out the quark spectrum, and the overall normalization (factor of 3 from N_c) confirms three colors. QCD corrections to R, calculated to order alpha_s^4, provide one of the most precise determinations of the strong coupling constant.

The study of **jet production** in e+e- annihilation has been central to establishing QCD. Two-jet events (e+e- -> qqbar) confirm the quark fragmentation picture. Three-jet events (e+e- -> qqbar-g) provided the first direct evidence for gluons at PETRA in 1979. The angular distributions and rates of multi-jet events test the SU(3) gauge structure: the ratio of four-jet to three-jet rates measures the ratio of color factors C_A/C_F, confirming the gauge group. Event shape variables -- thrust, sphericity, C-parameter, jet broadening -- quantify the degree of "jettiness" of events and allow precision extraction of alpha_s from their distributions.

At the **Z pole**, the LEP and SLC experiments collected millions of Z decays, enabling percent-level measurements of electroweak parameters and permille-level tests of QCD. The Z hadronic width, normalized to the leptonic width, gives a precise measurement of alpha_s(M_Z). The angular distributions of quarks (measured using jet directions) determine the Z couplings to individual flavors. Heavy-quark tagging (b and c quarks identified by displaced vertices from their long lifetimes) allows separate measurement of the Z couplings to each quark generation. These electroweak precision measurements form the core dataset for constraining the Standard Model.
