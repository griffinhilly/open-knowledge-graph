---
id: standard-scores-transformations
title: Standard Scores and Score Transformations
domain: psychology
course: psychometrics
prerequisites:
- id: norm-referenced-criterion-referenced-interpretation
  type: hard
- id: normal-distribution
  type: hard
builds-toward:
- diagnostic-cutoff-scores-classification-accuracy
tags:
- standard-scores
- z-scores
- t-scores
- transformation
stage: advanced
status: draft
---

# Standard Scores and Score Transformations

## Core Idea
Standard scores transform raw scores to a common metric with fixed mean and standard deviation. Z-scores (M=0, SD=1) are mathematically pure but have negative values; T-scores (M=50, SD=10) and IQ-type scores (M=100, SD=15) are more interpretable. Transformations preserve rank order and enable cross-test comparisons and form equating.

## Explainer

From your study of the normal distribution, you know that raw scores on a test have a mean and standard deviation specific to that test and that particular sample. From norm-referenced interpretation, you know that the raw number itself is less important than where it falls relative to others in the norm group. Standard scores formalize this insight: they transform raw scores into a common metric so that a score on one test can be directly compared to a score on another — and so that any score's meaning is immediately interpretable by anyone who knows the scale.

The foundational standard score is the **z-score**: z = (X − M) / SD. This expresses each score as a number of standard deviations above or below the mean. A z-score of 0 is exactly at the mean; +1 means one standard deviation above; −2 means two standard deviations below. Because you know the normal distribution, you can translate any z-score directly into a percentile: z = +1.65 is approximately the 95th percentile; z = −1 is approximately the 16th percentile. Z-scores are mathematically elegant but practically awkward — negative values and decimals confuse test-takers and the people interpreting reports, and a score of "−0.3" feels stigmatizing even when it means near-average performance.

The solution is a **linear transformation**: new score = M_new + z × SD_new. This maps the z-score to a more readable scale while preserving all information — the same rank, the same distance from the mean, just expressed differently. **T-scores** use M=50, SD=10: a T-score of 60 is exactly one standard deviation above average. **IQ-type scores** use M=100, SD=15: a score of 115 is one SD above average, the 84th percentile. **Stanines** use M=5, SD=2 with integer values 1-9. All of these carry identical information — they are the same z-score expressed in a different skin. A T-score of 70, an IQ-type score of 130, and a z-score of +2.00 are three ways of saying the same thing about a person's standing.

The critical practical skill is moving fluently between scales. If a student's cognitive assessment yields an IQ-type score of 130, you can immediately compute: z = (130−100)/15 = +2.00, which corresponds to the 97.7th percentile, and a T-score of 50 + (2.00 × 10) = 70. This fluency matters in clinical and educational contexts where different instruments report on different standard score scales. **Profile analysis** — comparing a student's scores across verbal, spatial, and processing speed domains — is one of the most common applications: without a shared scale, a raw score of 40 on one test and 75 on another is uninterpretable. Expressed as T-scores or IQ-type scores, the comparison becomes immediate.
