---
id: item-information-function-test-precision
title: Item and Test Information Functions and Measurement Precision
domain: psychology
course: psychometrics
prerequisites:
- id: ability-parameter-estimation-theta-estimation
  type: hard
builds-toward:
- guessing-pseudo-guessing-irt-models
tags:
- item-information
- test-information
- irt-precision
stage: advanced
status: draft
---

# Item and Test Information Functions and Measurement Precision

## Core Idea
In IRT, item information quantifies precision at different ability levels; test information sums item information curves. Information peaks where item response function slopes most steeply (maximum discrimination) and relates inversely to standard error. This enables precise test tailoring to measure specific ability ranges optimally.

## How It's Best Learned
Graph item information curves for items with varying discrimination parameters. Overlay item curves to create test information curves and observe how test information varies across ability scale.

## Common Misconceptions
- Item information is constant across ability levels (information varies dramatically by ability)

## Explainer

From theta estimation, you know that ability estimates have **standard errors** that vary across the theta scale — some regions are measured precisely, others poorly — and that this variation depends on how well the available items are targeted to the examinee's ability. The item information function makes this intuition mathematically precise. **Information**, in the IRT sense, is the reciprocal of the squared standard error: I(θ) = 1 / SE(θ)². High information means low error means precise measurement. The item information function plots how much information a single item provides as a function of theta.

For a 2PL item with difficulty *b* and discrimination *a*, the information function peaks exactly at θ = *b* — the point where the examinee has a 50% chance of getting the item correct. The intuition: an item that is too easy (nearly everyone answers correctly regardless of theta) contributes almost nothing to distinguishing between examinees near that theta value, because the response is essentially predetermined. The same logic applies to items that are too hard. Maximum discrimination — and thus maximum information — occurs at the item's difficulty location, where the ICC slope is steepest. The *a* parameter controls the height and sharpness of the information peak: a high-discrimination item provides concentrated, large-magnitude information at its difficulty location; a low-discrimination item provides diffuse, low-magnitude information spread across the scale. This is why item discrimination is so critical to efficient measurement.

**Test information** is additive: the test information function is simply the sum of item information functions across all items at each theta value. This has a direct design implication — you can visualize the contribution of each item and see where the test is well-calibrated and where gaps exist. A test optimized for selection near a specific cut score (say, a licensure exam) should stack items with difficulty values near that cut, concentrating information where the pass/fail decision is made. A test aiming to measure ability across a broad range should spread item difficulties to produce a flatter, wider information curve. This mathematical framework is the foundation of **computerized adaptive testing (CAT)**: the algorithm selects at each step the item that maximizes information at the current theta estimate, assembling a customized test that is always optimally targeted to that particular examinee.

The practical output of test information is the **conditional standard error of measurement (CSEM)**: a function showing measurement precision at each theta level, rather than the single aggregate reliability coefficient that classical test theory provides. Two examinees who took the same test but scored at different points on the theta scale genuinely have different measurement precision — the one near the information peak is measured more accurately than the one at the tail. Communicating this conditional precision matters for high-stakes decisions: a score near the licensure cut deserves a narrow confidence interval before a pass/fail call is made, while a score far from the cut may be less precisely estimated without affecting the decision. Understanding the CSEM is what separates IRT-informed score reporting from the cruder single-reliability summary.
