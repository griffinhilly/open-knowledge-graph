---
id: bsm-overview
title: Beyond Standard Model (BSM) Overview
domain: physics
course: particle-physics
prerequisites:
- id: standard-model-overview
  type: hard
- id: higgs-boson-discovery-and-properties
  type: hard
tags:
- bsm
- new-physics
- hierarchy-problem
- naturalness
stage: expert
status: validated
---

# Beyond Standard Model (BSM) Overview

## Core Idea
Despite its extraordinary success, the Standard Model leaves fundamental questions unanswered: the origin of neutrino masses, the nature of dark matter, the matter-antimatter asymmetry, the hierarchy problem (why the Higgs mass is so much lighter than the Planck scale), the strong CP problem, the pattern of fermion masses and mixing angles, and the absence of quantum gravity. BSM physics encompasses the theoretical frameworks and experimental searches aimed at addressing these shortcomings.

## Questions

```yaml
- question: "The hierarchy problem asks why the Higgs boson mass (~125 GeV) is so much smaller than the Planck mass (~10^{19} GeV). At the quantum level, the Higgs mass receives radiative corrections from loops of all particles that couple to it. Why is this a problem?"
  type: multiple-choice
  options:
    - "Because the Higgs mass cannot be measured precisely enough"
    - "Because the loop corrections to the Higgs mass-squared are proportional to Lambda^2, where Lambda is the UV cutoff (the highest energy scale at which the Standard Model is valid) — if Lambda is near the Planck scale, the corrections are ~10^{34} times larger than the observed Higgs mass-squared, requiring an extraordinary fine-tuning cancellation between the bare mass and the corrections to produce m_H = 125 GeV"
    - "Because the Planck mass is not well-defined"
    - "Because fermion masses are all much smaller than the Planck mass, not just the Higgs"
  answer: 1
  explanation: "Fermion masses are protected from large corrections by chiral symmetry (setting m_f = 0 enhances the symmetry), and gauge boson masses are protected by gauge symmetry. The Higgs scalar mass has no such protection — it is quadratically sensitive to UV physics. This is not a mathematical inconsistency (the SM is perfectly consistent as an effective field theory), but it requires that the bare mass parameter be tuned to ~34 decimal places to cancel the loop corrections, which many physicists find unnatural. Solutions include supersymmetry (which cancels the quadratic divergences), composite Higgs models (where the Higgs is not fundamental), and extra dimensions (which lower the effective Planck scale)."

- question: "The Standard Model has been tested at the LHC up to energy scales of several TeV with no deviations found. Does this mean there is no new physics below ~10 TeV?"
  type: true-false
  answer: false
  explanation: "The LHC has strong sensitivity to new colored particles (which would be copiously produced by the strong interaction) and to new particles with large couplings to SM particles, but it has much weaker sensitivity to particles that are weakly coupled, produced only in rare processes, or nearly degenerate in mass with SM particles (compressed spectra). Dark matter candidates with only electroweak interactions (e.g., pure higgsinos or winos with mass ~100-300 GeV) are very difficult to see at the LHC because their production cross sections are small and their decay products are soft. Similarly, light BSM particles that couple very weakly (axion-like particles, dark photons, long-lived particles) may have evaded detection. The absence of new physics at the LHC constrains specific models but does not exclude new physics at the TeV scale in general."

- question: "What are the three strongest experimental motivations for BSM physics?"
  type: short-answer
  answer: "1) Neutrino masses: Neutrino oscillations prove neutrinos have mass, but the minimal SM predicts massless neutrinos. Generating neutrino masses requires new fields (right-handed neutrinos, a Majorana mass term, or new scalars). 2) Dark matter: ~27% of the universe's energy density is dark matter, which has no SM candidate. Weakly interacting massive particles (WIMPs), axions, and sterile neutrinos are leading candidates. 3) Baryon asymmetry: The universe contains much more matter than antimatter, but the SM's CP violation is insufficient to generate this asymmetry. Additional CP-violating phases and a strong first-order electroweak phase transition (or leptogenesis) are needed. Other motivations include the hierarchy problem, the strong CP problem, dark energy, and the lack of quantum gravity."
  explanation: "These three motivations are particularly compelling because they involve concrete experimental observations that the SM fails to explain, not just aesthetic concerns about fine-tuning or unexplained patterns. They guarantee that new physics exists, even if its energy scale is unknown."
```

## Explainer

The **Standard Model's incompleteness** is established by observation, not just theoretical preference. Neutrino oscillations, dark matter, and the baryon asymmetry are three experimental facts that require new physics. The theoretical motivations -- the hierarchy problem, the strong CP problem, the flavor puzzle, the cosmological constant problem, and quantum gravity -- add urgency but are less definitive (the SM could simply be fine-tuned).

The **hierarchy problem** has driven much of BSM model building. If the Standard Model is valid up to the Planck scale (~10^{19} GeV), the Higgs mass requires cancellation between the bare mass and radiative corrections at the level of one part in 10^{34}. Three broad classes of solutions have been proposed: (1) **supersymmetry** introduces partner particles for every SM particle, whose loop contributions cancel the quadratic divergences; (2) **composite Higgs models** replace the fundamental scalar with a bound state of a new confining interaction, analogous to pions in QCD; (3) **extra dimensions** lower the fundamental gravitational scale from the Planck scale to the TeV scale, eliminating the large hierarchy. The LHC has not found evidence for any of these, pushing the parameter space of each framework and prompting reconsideration of the naturalness criterion.

**Experimental BSM searches** at the LHC cover an enormous range of signatures. Direct searches look for resonances (new particles decaying to known particles, producing bumps in invariant mass distributions), missing energy (dark matter or other invisible particles produced in association with jets, photons, or W/Z), displaced vertices (long-lived particles traveling millimeters to meters before decaying), and anomalous production rates (deviations from SM predictions in precision observables). The null results from Run 1 and Run 2 have excluded many natural BSM scenarios: squarks and gluinos below ~2 TeV, Z' bosons below ~5 TeV, and certain dark matter mediators below ~2 TeV.

The **future BSM program** combines direct searches at the HL-LHC and potential future colliders (FCC-hh at 100 TeV, muon collider) with indirect searches through precision measurements (Higgs coupling deviations, electroweak precision, flavor anomalies, g-2, EDMs) and dedicated experiments (dark matter direct detection, neutrinoless double beta decay, axion searches, beam dump experiments for light weakly-coupled particles). The breadth of the search program reflects the theoretical uncertainty about where and how new physics will appear.
