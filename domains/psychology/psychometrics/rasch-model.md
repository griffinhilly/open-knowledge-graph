---
id: rasch-model
title: 'Rasch Model: One-Parameter Item Response Theory'
domain: psychology
course: psychometrics
prerequisites:
- id: item-response-functions
  type: hard
- id: probability-and-statistics
  type: hard
- id: exponential-functions-and-graphs
  type: hard
builds-toward:
- irt-model-fit-comparison
tags:
- rasch-model
- 1pl
- item-response-theory
- interval-scale
stage: advanced
status: draft
---

# Rasch Model: One-Parameter Item Response Theory

## Core Idea
The Rasch model is the simplest item response theory model, assuming item difficulty is the sole item parameter, with equal discrimination across items. It produces interval-scale scores and has desirable statistical properties. The model is most useful when sample size is limited or when simplicity is valued over model complexity.

## How It's Best Learned
Fit Rasch models to real assessment data using software (Winsteps, RUMM). Examine goodness-of-fit statistics and compare Rasch item parameters with classical item difficulty indices.

## Common Misconceptions
Perfect Rasch model fit guarantees good measurement or validity. Even perfect fit doesn't ensure the test measures the intended construct. The unidimensionality requirement is critical but sometimes overstated regarding what it means for practical application.

## Explainer

From your study of item response functions, you know that an **item characteristic curve** (ICC) maps person ability onto the probability of a correct response — an S-shaped curve that rises from near zero at the left (low ability) to near one at the right (high ability). Different IRT models differ in how many parameters they use to describe each item's ICC. The Rasch model, also called the **1-parameter logistic (1PL)** model, makes a radical simplifying claim: every item's ICC has exactly the same slope. The only thing that varies across items is where the curve is centered on the ability scale — how hard the item is. Easy items have their curve shifted left (most people of average ability get them right); hard items shift right.

This might seem overly restrictive, but the simplicity buys something important. When all ICCs have the same slope, a person's total raw score is a **sufficient statistic** for their ability estimate — you don't need any more information about which specific items they got right or wrong, only how many. This is a unique and mathematically remarkable property. It also means that under the Rasch model, item difficulty estimates do not depend on the particular sample of people you used to calibrate them, and person ability estimates do not depend on the particular set of items administered. This property is called **specific objectivity**, and it is what makes Rasch measurement feel more like physical measurement: you can measure a person's weight with different scales and get the same result, as long as the scales are calibrated on the same metric.

The interval-scale property follows from the log-odds transformation at the heart of the model. Raw scores on a classical test are ordinal — going from 0 to 1 correct might be a bigger ability jump than going from 9 to 10 correct, depending on item placement, but the raw score treats all increments as equal. Rasch converts raw scores to **logit** estimates (log-odds units) that are interval-scale: a one-logit difference in ability means the same increase in probability of success regardless of where on the scale you are. This matters for research that computes means, differences, and regression coefficients — arithmetic operations that assume interval measurement.

The model's limitation is the stringency of its assumptions. All items must discriminate equally well between people just above and just below the item's threshold — an assumption that real items frequently violate. Items also must show no **differential item functioning**: they should be equally fair across demographic subgroups (gender, ethnicity, language background) after controlling for ability. When data don't fit the Rasch model, researchers face a choice: remove misfitting items (sacrificing content) or move to a more flexible 2PL or 3PL model (sacrificing the specific-objectivity property). Neither option is free. Rasch fit statistics — infit and outfit mean-square statistics — diagnose which items are behaving inconsistently with the model, but fit statistics alone cannot tell you whether the violation is serious enough to invalidate the measurement for your purpose. That judgment requires content knowledge about what each item is measuring and why it might behave unexpectedly.
