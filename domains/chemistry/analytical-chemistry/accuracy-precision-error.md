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
stage: formal-systems
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
