---
id: jets-and-jet-algorithms
title: Jets and Jet Algorithms
domain: physics
course: particle-physics
prerequisites:
- id: qcd-basics
  type: hard
- id: parton-distribution-functions
  type: soft
tags:
- jets
- jet-algorithms
- anti-kt
- hadronization
stage: expert
status: validated
---

# Jets and Jet Algorithms

## Core Idea
Jets are collimated sprays of hadrons produced when high-energy quarks or gluons from a hard scattering undergo fragmentation and hadronization. Because free quarks and gluons cannot be observed (confinement), jets are the experimental proxies for partons. Jet algorithms define systematic procedures for clustering final-state particles into jets, and their design must be infrared and collinear (IRC) safe to allow meaningful comparison with perturbative QCD calculations.

## Questions

```yaml
- question: "The anti-k_T algorithm is the default jet clustering algorithm at the LHC. It clusters particles based on distance measures d_{ij} = min(1/p_{Ti}^2, 1/p_{Tj}^2) * Delta R_{ij}^2 / R^2 and d_{iB} = 1/p_{Ti}^2. What property makes it preferred over earlier algorithms like the k_T algorithm?"
  type: multiple-choice
  options:
    - "It runs faster computationally"
    - "It produces perfectly circular, cone-like jets with hard particles at the center, while being IRC safe — soft particles at the jet boundary do not distort the jet shape, making jet calibration and comparison with theory straightforward"
    - "It always produces exactly two jets"
    - "It eliminates the need for jet energy corrections"
  answer: 1
  explanation: "The anti-k_T algorithm preferentially clusters soft particles with nearby hard particles (because the 1/p_T^2 weighting favors high-p_T seeds). This produces jets with regular, circular boundaries around hard cores. The k_T algorithm (which uses p_T^2 instead of 1/p_T^2) clusters soft particles first, producing irregular jet shapes. Both are IRC safe and give the same inclusive cross sections, but anti-k_T jets are experimentally easier to calibrate and correct."

- question: "A jet algorithm must be 'infrared and collinear (IRC) safe' to be useful for QCD calculations. What does this requirement mean physically?"
  type: short-answer
  answer: "IRC safety means the set of jets found by the algorithm does not change when a soft (zero-energy) particle is added to the event (infrared safety) or when a particle is split into two collinear particles sharing its momentum (collinear safety). Perturbative QCD calculations contain infrared and collinear divergences that cancel between real-emission and virtual-correction diagrams — but this cancellation works only if the observable (here, the jet definition) is insensitive to soft and collinear emissions. An IRC-unsafe algorithm would give different jet multiplicities or momenta in the presence of soft radiation, making the perturbative calculation divergent and the observable ill-defined."
  explanation: "The requirement of IRC safety eliminated many early cone-based jet algorithms that used seed-based iterative procedures. The sequential recombination algorithms (k_T, Cambridge/Aachen, anti-k_T) are all IRC safe by construction."

- question: "The parameter R in jet algorithms sets the jet 'radius' in eta-phi space. At the LHC, typical choices are R = 0.4 for resolved jets and R = 0.8 or 1.0 for 'fat jets.' Why do analyses of boosted heavy particles (top quarks, W/Z/H bosons) use large-R jets?"
  type: multiple-choice
  options:
    - "Because heavy particles produce more particles in their decay"
    - "When a heavy particle is produced with transverse momentum much larger than its mass, its decay products are collimated into a cone of angular size approximately 2m/p_T — a large-R jet captures the entire decay, and jet substructure techniques can then identify the decay pattern inside the single jet"
    - "Because large-R jets have better energy resolution"
    - "Because QCD background is lower for large-R jets"
  answer: 1
  explanation: "A top quark with p_T = 500 GeV decaying to Wb -> qqb produces three quarks separated by Delta R ~ 2*m_t/p_T ~ 0.7. A small-R jet (R=0.4) would resolve these as separate jets, while a large-R jet (R=1.0) captures them all. Jet substructure techniques (trimming, pruning, soft-drop, N-subjettiness) then analyze the internal structure of the fat jet to distinguish boosted top quarks from QCD background. This 'boosted object tagging' has become a major tool at the LHC."
```

## Explainer

When a quark or gluon is produced in a hard collision, it cannot propagate freely because of color confinement. Instead, it undergoes a cascade of gluon radiation (parton shower) followed by **hadronization** -- the non-perturbative process of forming color-neutral hadrons. The result is a collimated spray of particles, a **jet**, roughly aligned with the original parton's direction. Jets are the most common high-energy objects at hadron colliders: most LHC events with large transverse energy contain multiple jets.

**Jet algorithms** are the rules for grouping final-state particles into jets. Modern algorithms are sequential recombination algorithms that iteratively merge the closest pair of particles (or declare a particle as a jet) based on a distance measure. The three standard algorithms -- k_T, Cambridge/Aachen, and anti-k_T -- differ only in the power of the momentum weighting: p = 1 (k_T), p = 0 (C/A), or p = -1 (anti-k_T). The anti-k_T algorithm, which produces clean cone-like jets centered on hard particles, has been the default at ATLAS and CMS since the start of LHC operations. All three are infrared and collinear safe, meaning they give stable results when soft or collinear particles are added.

The **jet energy scale** -- the relationship between the measured jet energy and the true parton energy -- is one of the most important calibrations at a hadron collider. Jets lose energy to particles outside the cone, neutrinos from heavy-flavor decays, and detector effects (calorimeter response, dead material, pileup from additional proton-proton interactions). Jet energy corrections are typically 5-20% and are calibrated using gamma+jet and Z+jet events where the photon or Z provides a precise momentum reference. The residual jet energy scale uncertainty (1-3% at the LHC) is often the dominant systematic in jet-based measurements.

**Jet substructure** has emerged as a powerful tool for identifying boosted heavy particles at the LHC. When a W boson, top quark, or Higgs boson is produced with transverse momentum much greater than its mass, its decay products merge into a single large-radius jet. Substructure techniques -- grooming algorithms that remove soft wide-angle radiation, and shape variables like N-subjettiness that characterize the internal energy flow -- can distinguish these signal jets from QCD background jets. This has enabled searches for heavy new particles decaying to boosted tops and vector bosons in kinematic regimes that were previously inaccessible.
