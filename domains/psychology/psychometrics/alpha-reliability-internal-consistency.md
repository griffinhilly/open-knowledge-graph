---
id: alpha-reliability-internal-consistency
title: Cronbach's Alpha and Internal Consistency Reliability
domain: psychology
course: psychometrics
prerequisites:
- id: internal-consistency-reliability
  type: hard
- id: domain-sampling-theory-reliability-generalization
  type: hard
builds-toward:
- split-half-reliability-spearman-brown
- reliability-estimation-method-selection
tags:
- alpha
- internal-consistency
- reliability-coefficient
stage: advanced
status: draft
---

# Cronbach's Alpha and Internal Consistency Reliability

## Core Idea
Cronbach's alpha is the average of all possible split-half reliabilities and estimates internal consistency for scales measuring a single construct. It depends on both number of items and average inter-item correlation, making it sensitive to item homogeneity. Acceptable alpha ranges from .70 (research) to .90+ (clinical diagnosis), though values above .90 may indicate redundancy.

## How It's Best Learned
Calculate alpha by hand for small datasets using the formula α = (k / k-1) × [1 - (Σσ_i² / σ_total²)] to understand the relationship between item variance, covariance, and total variance.

## Common Misconceptions
- Alpha measures unidimensionality (it measures internal consistency only)
- Higher alpha is always better (alpha is scale-length dependent)

## Explainer

From your study of internal consistency and domain sampling theory, you know that a test is a sample of items drawn from a larger conceptual domain, and that reliability depends on how representative and coherent that sample is. **Cronbach's alpha** is the formal measure that quantifies this coherence. Its mathematical identity is instructive: alpha equals the average of *all possible split-half reliability coefficients* for a given scale. Instead of splitting a test once into odd and even items and computing one correlation, alpha performs every possible split and averages the results. This makes it a stable, comprehensive estimate of internal consistency rather than an artifact of how you happened to divide the items.

The formula α = (k / k−1) × [1 − (Σσᵢ² / σ_total²)] has two components worth understanding separately. The term Σσᵢ² is the sum of individual item variances — how much each item varies across respondents on its own. σ_total² is the variance of the total score. If items are highly intercorrelated, much of the individual item variance is shared: people who score high on one item tend to score high on the others. That shared variance inflates total score variance relative to the sum of item variances, so the ratio Σσᵢ²/σ_total² is small, and alpha is high. Conversely, if items are unrelated, each contributes unique variance without contributing to shared variance — the ratio is large, and alpha is low. The k/(k−1) multiplier is a correction for the number of items: more items always raise alpha, even holding average inter-item correlation constant, because longer tests sample the domain more thoroughly.

This two-factor structure — **item homogeneity** and **scale length** — is the key to interpreting alpha intelligently. The widely cited thresholds (≥.70 for research, ≥.90 for clinical decisions affecting individuals) are guidelines, not laws. A short five-item scale with strong inter-item correlations may produce an alpha of .75, which is perfectly adequate. A 40-item scale that includes redundant paraphrases of the same item can reach .95 — but the apparent precision is illusory, because the scale is not measuring a richer construct, only repeating the same narrow question many times. **Alpha above .90 often signals item redundancy** rather than superior measurement, and the practical consequence is that the scale provides little additional information per item.

Finally, alpha addresses only one question: do the items tend to rise and fall together? It says nothing about whether they are measuring the *right thing* — a unidimensional construct, not a mix of two or three different factors. You can construct a scale with items drawn from two unrelated dimensions and still observe a moderate alpha if the factors happen to correlate. Conversely, a perfectly valid scale measuring a genuinely multidimensional construct may show low alpha. This is why alpha is best read alongside factor analysis, not instead of it: alpha assesses internal consistency, factor analysis assesses dimensionality.
