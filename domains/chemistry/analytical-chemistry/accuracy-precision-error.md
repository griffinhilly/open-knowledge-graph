---
id: accuracy-precision-error
title: Accuracy, Precision, and Error
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: statistical-methods-analytical
  type: hard
- id: statistics-descriptive
  type: soft
- id: standard-normal-z-scores-theory
  type: soft
- id: standard-deviation
  type: soft
- id: variance-of-random-variables
  type: soft
tags:
- accuracy
- precision
- systematic error
- random error
- bias
- trueness
- determinate error
- indeterminate error
stage: advanced
status: draft
---

# Accuracy, Precision, and Error

## Core Idea
Every analytical measurement carries error, which divides into systematic (determinate) and random (indeterminate) components. Systematic errors — such as an uncalibrated balance, a reagent impurity, or a consistent procedural bias — shift all results in the same direction and affect accuracy (closeness to the true value, also called trueness). Random errors — arising from uncontrollable fluctuations in temperature, operator technique, or detector noise — scatter results around a mean and affect precision (reproducibility). A method can be precise without being accurate (tight grouping, wrong center) or accurate on average without being precise (scattered around the true value), and the analytical goal is to minimize both.

## How It's Best Learned
Weigh a certified reference weight repeatedly on an analytical balance, compute the mean (to assess accuracy/bias) and standard deviation (to assess precision), then deliberately introduce a systematic error (e.g., not taring properly) and observe how the mean shifts while the spread stays similar. This concrete demonstration makes the distinction visceral.

## Common Misconceptions
- High precision does not imply high accuracy; a well-calibrated but contaminated reagent can give beautifully reproducible yet consistently wrong results.
- Systematic errors cannot be reduced by averaging more replicates — they require identification and elimination of the root cause, whereas random errors do shrink with increased replicate count.

## Explainer

Every measurement you take in the lab is wrong. That sounds alarming, but it is the starting point of analytical chemistry: no measurement perfectly captures the true value of the quantity being measured. The question is never whether error exists, but what kind of error dominates and how to manage it. From your work with descriptive statistics, you already know how to characterize a set of measurements using the mean and standard deviation. Those two summary statistics map directly onto the two fundamental dimensions of measurement quality — **accuracy** (how close the mean is to the true value) and **precision** (how tightly the individual measurements cluster around their own mean).

Think of it like throwing darts at a target. A precise but inaccurate thrower groups all darts tightly together, but the cluster lands away from the bullseye. An accurate but imprecise thrower scatters darts all around the board, yet their average position happens to be near the center. The ideal is both precise and accurate — a tight cluster centered on the target. **Systematic error** (also called **determinate error** or **bias**) is what shifts the cluster off-center: a balance that reads 0.003 g too high, a reagent contaminated with trace analyte, or a consistent procedural mistake. **Random error** (also called **indeterminate error**) is what spreads the cluster: uncontrollable fluctuations in temperature, slight variations in how you pipette, electrical noise in the detector. These two error types have fundamentally different statistical signatures and require fundamentally different corrective strategies.

The critical distinction between the two is how they respond to replication. When you take more measurements and average them, the standard deviation of the mean decreases by a factor of 1/√n — your z-score calculations from statistics confirm this. Random errors, being equally likely to push a measurement high or low, progressively cancel out with more replicates. Systematic errors do not cancel because they push every measurement in the same direction. Averaging a hundred biased measurements gives you a very precise — but still biased — mean. This is why identifying and eliminating systematic errors requires a different toolkit entirely: running certified reference materials, comparing results across independent methods, calibrating instruments against traceable standards, and performing blank corrections.

In practice, analytical chemists assess accuracy by comparing measured values against a known standard (a certified reference material or a spiked recovery experiment) and assess precision through replicate measurements reported as standard deviation or relative standard deviation. A method is only fit for purpose when both dimensions meet the required specification. Regulatory and quality frameworks demand that you demonstrate both, because a method that is reproducible but consistently wrong is just as dangerous as one that occasionally gets lucky. The discipline of separating, quantifying, and controlling these two kinds of error is the foundation on which every reliable analytical result rests.
