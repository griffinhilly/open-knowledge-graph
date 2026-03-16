---
id: confidence-intervals-for-test-scores
title: Confidence Intervals and Score Reporting Uncertainty
domain: psychology
course: psychometrics
prerequisites:
- id: standard-error-of-measurement
  type: hard
- id: probability-and-statistics
  type: hard
tags:
- confidence-intervals
- score-uncertainty
- reporting
- measurement-error
- inference
stage: advanced
status: draft
---

# Confidence Intervals and Score Reporting Uncertainty

## Core Idea
Confidence intervals around test scores communicate score uncertainty more effectively than point estimates alone and are increasingly required in professional testing. Intervals can be constructed using the standard error of measurement for scores near the mean, or using item response theory to account for differential precision across ability ranges. Reporting confidence intervals with scores helps practitioners and test-takers understand the range within which true scores likely fall.

## Explainer

You already know that the **standard error of measurement (SEM)** quantifies how much an observed score is expected to deviate from the true score due to random measurement error. Now you can use that quantity directly to build a confidence interval around any observed score. The logic is the same as the confidence intervals from your statistics background: if errors are approximately normally distributed, you can say with 95% confidence that the true score lies within roughly ±1.96 SEM of the observed score. In practice, a 95% CI around a score of 75 with an SEM of 3 runs from approximately 69 to 81 — which is a meaningfully wide band that should temper any over-precise interpretation of that single number.

The construction is straightforward for **CTT-based intervals**: multiply the SEM by the appropriate z-score (1.65 for 90%, 1.96 for 95%, 2.58 for 99%) and add/subtract from the observed score. One subtlety worth knowing: the SEM is constant across the score range in classical test theory, which is an approximation. In reality, measurement precision varies — most tests are more precise near the middle of the score distribution (where most items are targeted) and less precise at the extremes. This matters enormously for high-stakes decisions at cut scores.

**IRT-based confidence intervals** solve this problem by using the **information function** — a curve that varies across the ability scale and peaks where the test items are most discriminating. The standard error at any ability level θ is the reciprocal of the square root of the information at that point: SE(θ) = 1/√I(θ). This produces intervals that are narrower where the test is well-targeted and wider where precision is low. For a test designed to make a cut at the 70th percentile, the IRT-based interval at that cut point will be tighter than the CTT-based interval, and appropriately wider at score extremes.

The practical importance of reporting confidence intervals is easiest to see in high-stakes contexts. A student scoring 1 point below a proficiency cut score should not automatically be classified as non-proficient if the SEM means their true score could plausibly be above the cut. Professional guidelines from the American Psychological Association and the Standards for Educational and Psychological Testing require that score reports for consequential assessments communicate score uncertainty, not just point estimates. Presenting a score as a band rather than a precise number models better epistemology — it reminds the user that a test score is an estimate, not a truth, and that decisions near any threshold deserve extra scrutiny.
