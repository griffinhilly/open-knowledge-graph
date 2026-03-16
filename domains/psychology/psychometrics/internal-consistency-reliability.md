---
id: internal-consistency-reliability
title: Internal Consistency and Homogeneity
domain: psychology
course: psychometrics
prerequisites:
- id: classical-test-theory
  type: hard
- id: covariance-correlation-theory
  type: soft
builds-toward:
- confirmatory-factor-analysis
tags:
- reliability
- alpha-coefficient
- internal-structure
stage: advanced
status: draft
---

# Internal Consistency and Homogeneity

## Core Idea
Internal consistency evaluates whether items within a test correlate with each other, indicating they measure a common construct. Cronbach's alpha and KR-20 are common indices. High internal consistency suggests item coherence but does not guarantee the test is unidimensional or valid.

## How It's Best Learned
Calculate alpha coefficients for sample datasets and examine item-total correlations. Explore how item redundancy artificially inflates alpha and understand why multidimensional tests have lower alphas despite validity.

## Common Misconceptions
Internal consistency equals unidimensionality. A scale can have high alpha while measuring multiple factors. Also, alpha can be artificially inflated by item redundancy without improving construct representation or validity.

## Explainer

From Classical Test Theory, you know that an observed score is the sum of a true score and random error, and that reliability is the proportion of observed-score variance attributable to true-score variance. **Internal consistency** is a specific strategy for estimating that proportion — one that uses the pattern of relationships among items within a single test administration, rather than requiring you to test the same people twice (test-retest) or administer two parallel forms.

The intuition is straightforward: if a set of items all measure the same underlying construct, they should correlate with each other. A student with high mathematical reasoning ability should score well across multiple math items, not just one, because the same latent trait drives performance on each. **Cronbach's alpha** formalizes this: it is equivalent to the average correlation among all possible ways of splitting the test into two halves, corrected upward for test length using the Spearman-Brown formula. Algebraically, alpha depends on the number of items, the variance of each item, and the total test variance. More inter-item covariance relative to total variance means higher alpha.

The critical limitation — and the most common misconception — is that high alpha does not imply **unidimensionality**. A test with two distinct but internally correlated subscales can produce a high overall alpha coefficient even though the items measure two different constructs. Imagine a "wellbeing" scale with 10 items measuring positive affect and 10 measuring life satisfaction. If those two dimensions are moderately correlated (as they typically are), the overall 20-item alpha may be quite high — but the scale is not measuring a single thing. To test unidimensionality, you need factor analysis; alpha alone cannot tell you whether one factor or five factors is the right description of your item set.

There is also a manipulation risk worth understanding from your covariance background: you can inflate alpha by adding items that are nearly redundant with existing items. Alpha increases with item count when average inter-item correlation is held constant — so a 50-item scale with wordy, repetitive items will have higher alpha than a 10-item scale measuring the same construct more efficiently. But item redundancy does not add measurement precision or construct coverage; it adds administrative burden and can produce **construct underrepresentation** by over-sampling a narrow facet while neglecting others. Use alpha as a lower-bound reliability estimate, but look to factor analysis and validity evidence for conclusions about construct structure.
