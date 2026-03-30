---
id: cross-section-measurements
title: Cross Section Measurements
domain: physics
course: particle-physics
prerequisites:
- id: cross-sections-decay-rates
  type: hard
- id: collider-physics-methods
  type: hard
tags:
- cross-section
- fiducial
- unfolding
- acceptance
stage: expert
status: validated
---

# Cross Section Measurements

## Core Idea
Cross section measurements at colliders translate observed event counts into fundamental quantities that can be compared with theoretical predictions. The measured cross section sigma = (N_signal - N_background) / (efficiency * luminosity) must be corrected for detector acceptance, efficiency, and resolution effects. Fiducial and differential cross sections, corrected through unfolding, provide the most model-independent comparisons with theory.

## Questions

```yaml
- question: "The formula for a total cross section measurement is sigma = N_obs / (epsilon * L), where N_obs is the background-subtracted event count, epsilon is the overall efficiency (trigger * reconstruction * selection), and L is the integrated luminosity. Which of these quantities typically carries the largest systematic uncertainty at the LHC?"
  type: multiple-choice
  options:
    - "N_obs, because counting is imprecise"
    - "The answer depends on the process: for inclusive W/Z production, the luminosity uncertainty (~1-2%) dominates; for rare processes with complex final states, the efficiency uncertainty (from lepton identification, jet calibration, trigger efficiency) often dominates; and for processes with large backgrounds, the background subtraction uncertainty may dominate"
    - "epsilon, because detectors are unreliable"
    - "L, because luminosity is always the dominant uncertainty"
  answer: 1
  explanation: "The luminosity is measured by dedicated detectors (LUCID, BCM in ATLAS; PLT, HF in CMS) calibrated using van der Meer scans, achieving ~1-2% precision. The efficiency is measured using tag-and-probe methods on standard candle processes. For well-measured processes like Z -> ll, the luminosity uncertainty dominates. For top quark pair production, jet energy scale and b-tagging efficiency are comparable. For searches with few events, the statistical uncertainty dominates everything."

- question: "A 'fiducial' cross section is measured within a restricted kinematic region defined by the experimental acceptance (e.g., lepton p_T > 25 GeV, |eta| < 2.5). Why is a fiducial measurement preferred over a total cross section measurement for comparison with theory?"
  type: short-answer
  answer: "A total cross section measurement requires extrapolating from the measured fiducial region to the full phase space using Monte Carlo simulation. This extrapolation introduces model dependence: different generators may predict different fractions of events outside the acceptance. A fiducial measurement avoids this by reporting the cross section only within the experimentally accessible region, where detector effects are well-understood. Theorists can then calculate the predicted cross section in the same fiducial region and compare directly. This approach minimizes model dependence and provides the cleanest comparison between data and theory."
  explanation: "Modern LHC measurements increasingly report fiducial and differential cross sections rather than total cross sections. This philosophy ('measure what you measure, don't extrapolate') has been widely adopted because it provides the most transparent and reproducible results."

- question: "Differential cross section measurements (d sigma/d p_T, d sigma/d y, etc.) are presented as 'unfolded' distributions that correct for detector resolution and efficiency effects. The standard unfolding methods include matrix inversion, iterative Bayesian unfolding, and SVD regularization. What problem do these methods solve?"
  type: multiple-choice
  options:
    - "They remove statistical fluctuations from the data"
    - "They correct for the fact that the measured (detector-level) distribution differs from the true (particle-level) distribution due to finite detector resolution (events migrate between bins), limited efficiency (some events are lost), and background contamination — unfolding inverts the response matrix to recover the true distribution"
    - "They combine data from multiple experiments"
    - "They extrapolate the data to higher energies"
  answer: 1
  explanation: "The detector smears the true distribution through a response matrix R: N_measured = R * N_true + N_background. Simply inverting R amplifies statistical fluctuations (the problem is mathematically ill-conditioned), so regularization techniques are needed to suppress unphysical oscillations while preserving the physics content. Iterative Bayesian unfolding (D'Agostini method) and SVD regularization with a tuneable regularization parameter are the most common approaches. The result is a corrected distribution at 'particle level' (stable particles before detector interaction) that can be directly compared with theory predictions."
```

## Explainer

**Cross section measurements** are the primary quantitative output of collider experiments. A cross section sigma has units of area (typically picobarns or femtobarns at the LHC) and represents the effective target area for a particular process. Multiplied by the integrated luminosity (the total amount of data collected, in units of inverse cross section), it gives the expected number of events: N = sigma * L. The reverse -- extracting sigma from the observed N after correcting for efficiency and backgrounds -- is the measurement.

The **measurement chain** proceeds as follows. Events are selected by the trigger and offline analysis cuts. The efficiency of each selection step (trigger, reconstruction, identification, isolation, kinematic cuts) is measured in data using tag-and-probe techniques on known processes. The background is estimated from data-driven methods or simulation and subtracted. The remaining signal event count is divided by the efficiency and luminosity to give the cross section. Systematic uncertainties from each step (efficiency correction, background estimation, luminosity, and theory modeling) are propagated and combined.

**Fiducial cross sections** restrict the measurement to the kinematic region directly accessible to the detector, avoiding model-dependent extrapolations. A fiducial region is defined at particle level (using stable particles with lifetime > 10 ps) with cuts that closely mirror the detector-level selection. Differential fiducial cross sections -- binned in kinematic variables like p_T, rapidity, jet multiplicity, or angular correlations -- provide the most detailed comparison with theory. They test not just the total rate but the shape of distributions, probing QCD dynamics, PDF effects, and electroweak corrections.

**Unfolding** is the mathematical procedure that corrects a measured distribution for detector effects. The detector response is encoded in a migration matrix that maps particle-level bins to detector-level bins. Inverting this matrix is ill-conditioned (small statistical fluctuations are amplified into large oscillations), so regularized methods are used. The result is a distribution at particle level that can be compared with any theoretical prediction without passing the prediction through detector simulation. This separation of measurement (corrected to particle level) and theory comparison is a key principle of modern collider physics, ensuring measurements remain useful long after the experiments that produced them.
