---
id: higgs-boson-discovery-and-properties
title: Higgs Boson Discovery and Properties
domain: physics
course: particle-physics
prerequisites:
- id: higgs-mechanism
  type: hard
- id: standard-model-overview
  type: hard
- id: cross-section-measurements
  type: soft
tags:
- higgs-boson
- lhc
- higgs-discovery
- higgs-couplings
stage: expert
status: validated
---

# Higgs Boson Discovery and Properties

## Core Idea
The Higgs boson was discovered at the LHC in 2012 by the ATLAS and CMS experiments, with a mass of 125.1 GeV. Its production and decay rates are consistent with Standard Model predictions: it is a spin-0, CP-even scalar whose couplings to other particles are proportional to their masses. Measuring the Higgs couplings with increasing precision is the central goal of the LHC program and future colliders.

## Questions

```yaml
- question: "The Higgs boson was discovered primarily in two channels: H -> gamma gamma and H -> ZZ* -> 4 leptons. Neither of these is the dominant Higgs decay mode (which is H -> bb at 58%). Why were these rare channels the discovery modes?"
  type: multiple-choice
  options:
    - "Because H -> bb has too low a cross section"
    - "Because H -> gamma gamma (branching ratio ~0.2%) has excellent mass resolution from the two photon energies, and H -> ZZ* -> 4l (branching ratio ~0.01%) has very low background and excellent mass resolution from the four lepton momenta — despite their low rates, the signal-to-background ratio is far superior to H -> bb, which is overwhelmed by the enormous QCD bb-bar production background at the LHC"
    - "Because photons and leptons are easier to detect than b quarks"
    - "Because only these channels were predicted by the Standard Model"
  answer: 1
  explanation: "At the LHC, the QCD production of b-quark pairs has a cross section about 10^7 times larger than Higgs production, making H -> bb nearly invisible in the inclusive channel. The diphoton channel benefits from the excellent electromagnetic calorimeter resolution of ATLAS and CMS (mass resolution ~1-2 GeV), producing a narrow peak above a smooth continuum background. The four-lepton channel has the best signal-to-background ratio of any Higgs channel (S/B ~ 2:1 near the peak) because requiring four isolated leptons with the right invariant mass is extremely selective."

- question: "The Standard Model predicts that the Higgs coupling to a particle is proportional to its mass (for fermions: g_Hff = m_f/v; for gauge bosons: g_HVV proportional to M_V^2/v). This has been tested by measuring Higgs production and decay rates. The agreement with the mass-proportional prediction is at the 10-20% level for the measured couplings."
  type: true-false
  answer: true
  explanation: "The LHC has measured Higgs couplings to W, Z, top, bottom, tau, and muon. The coupling-mass relationship follows the predicted pattern: the largest couplings are to the top quark (y_t ~ 1) and W/Z bosons, with progressively smaller couplings to bottom, tau, charm, and muon. Signal strength measurements (mu = observed rate / SM prediction) are consistent with 1 for all measured channels. The precision is currently 10-20% for most couplings and will improve to a few percent at the HL-LHC, which is where deviations from the SM prediction would indicate new physics in the Higgs sector."

- question: "The Higgs boson has spin 0 and CP-even (scalar) quantum numbers. How were these quantum numbers determined experimentally?"
  type: short-answer
  answer: "The spin and CP properties were determined from angular distributions of the Higgs decay products. In H -> ZZ* -> 4l, the angles between the two Z decay planes and the Z production angles are sensitive to the Higgs spin and parity. A spin-0 CP-even particle (J^P = 0+) produces a specific pattern of angular correlations that differs from spin-0 CP-odd (0-), spin-1, or spin-2 hypotheses. The observed distributions at both ATLAS and CMS strongly favor 0+ over all alternatives, with the 0- hypothesis excluded at more than 99.9% confidence level. The H -> gamma gamma channel also constrains the spin: the Landau-Yang theorem forbids a massive spin-1 particle from decaying to two photons, so the observation of H -> gamma gamma rules out spin 1."
  explanation: "Determining the Higgs quantum numbers was essential for confirming that the discovered particle is indeed the Standard Model Higgs boson and not an impostor with different spin or parity. Ongoing measurements search for small CP-odd admixtures, which would indicate CP violation in the Higgs sector -- a beyond-SM effect."

- question: "The dominant Higgs production mechanism at the LHC is gluon-gluon fusion (gg -> H), even though the Higgs does not couple directly to gluons. How does this process occur?"
  type: multiple-choice
  options:
    - "Through tree-level quark exchange in the s-channel"
    - "Through a top quark loop — two gluons couple to a virtual top quark loop, which couples to the Higgs through the large top Yukawa coupling; the cross section is proportional to alpha_s^2 * y_t^2 and the top loop gives an effective ggH coupling"
    - "Through W boson fusion"
    - "Through direct Higgs-gluon coupling from higher-dimensional operators"
  answer: 1
  explanation: "The ggH process proceeds through a fermion triangle loop, dominated by the top quark (because y_t ~ 1). Despite being loop-induced, it is the dominant production mechanism (~87% of Higgs production at 13 TeV) because the gluon PDFs are very large at the LHC. The next-largest production modes are vector boson fusion (VBF, ~7%), associated production with W/Z (VH, ~4%), and associated production with top quarks (ttH, ~1%). Each production mode provides complementary information about the Higgs couplings."
```

## Explainer

The discovery of the **Higgs boson** on July 4, 2012, by the ATLAS and CMS experiments at the LHC was the culmination of a nearly 50-year search. The particle was predicted in 1964 by Brout, Englert, and Higgs as a consequence of the mechanism that gives mass to the W and Z bosons. Its mass of 125.1 GeV, while not predicted by the Standard Model, turns out to be in a theoretically interesting range: heavy enough to be discovered at the LHC but light enough to leave the Standard Model perturbative up to very high energy scales.

The **production mechanisms** at the LHC reflect the Higgs coupling structure. Gluon fusion (gg -> H via a top loop) dominates because of the large gluon luminosity and the strong top Yukawa coupling. Vector boson fusion (qq -> qqH via W/Z exchange) has a distinctive signature of two forward jets with a rapidity gap. Associated production (WH, ZH, ttH) provides direct access to the HWW, HZZ, and Htt couplings. Each production mode has been observed and measured, confirming the expected coupling pattern.

The **decay modes** span a wide range of branching ratios. The dominant decay is H -> bb (58%), followed by H -> WW* (21%), H -> gg (8.2%), H -> tau tau (6.3%), H -> cc (2.9%), H -> ZZ* (2.6%), H -> gamma gamma (0.23%), H -> Z gamma (0.15%), and H -> mu mu (0.02%). The hierarchy of branching ratios directly reflects the mass-proportional coupling: the Higgs decays predominantly to the heaviest particles that are kinematically accessible. The rare decays H -> gamma gamma and H -> Z gamma are loop-induced (like gg -> H) and are sensitive to virtual particles in the loop, including potential new charged particles beyond the Standard Model.

The **future Higgs program** aims to measure all couplings at the percent level or better and to observe the Higgs self-coupling (the trilinear HHH coupling, which determines the shape of the Higgs potential). The HL-LHC (High-Luminosity LHC, starting ~2029) will collect 20 times more data, enabling 3-5% coupling measurements and a first look at Higgs pair production. Proposed future colliders -- the FCC-ee (e+e- at 240 GeV), ILC, CLIC, CEPC, and the FCC-hh (100 TeV pp) -- could measure couplings to sub-percent precision and determine the Higgs self-coupling to 5-10%. Any deviation from the Standard Model prediction would point to new physics in the Higgs sector, such as additional scalar fields, compositeness, or supersymmetry.
