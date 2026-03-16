---
id: measurement-reliability-estimation
title: 'Measurement Reliability: Types and Estimation'
domain: psychology
course: research-methods-psychology
prerequisites:
- id: variable-definition-and-operational-measurement
  type: hard
- id: correlation-coefficient
  type: soft
builds-toward:
- measurement-validity-evidence
tags:
- reliability
- consistency
- measurement-error
stage: abstract-reasoning
status: draft
---

# Measurement Reliability: Types and Estimation

## Core Idea
Reliability is consistency of measurement across items (internal consistency), raters (inter-rater), time (test-retest), or forms (parallel). Each type addresses different sources of error. Coefficient alpha, intraclass correlations, and test-retest correlations quantify reliability. Unreliable measurement attenuates relationships and reduces statistical power; reliability sets an upper bound on validity.

## How It's Best Learned
Calculate Cronbach's alpha for a published scale. Review reliability coefficients in research papers and interpret their magnitude. Discuss which type of reliability (internal, test-retest, inter-rater) is most important for different measurement contexts.

## Common Misconceptions
- Reliability and validity are the same; - High internal consistency always indicates unidimensionality; - Alpha > 0.7 is sufficient for all uses; - One reliability estimate applies to all samples and times.

## Explainer

From your work on operational measurement, you know that every construct must be defined in terms of observable indicators — the behaviors, responses, or outcomes that stand in for the underlying theoretical variable. The moment you operationalize, you introduce the possibility of **measurement error**: the gap between your observed score and the true score you are trying to capture. Reliability is the study of that gap — specifically, how consistent the observed score is across different conditions under which you would expect it to stay the same.

The most important conceptual anchor is **Classical Test Theory's** decomposition: Observed Score = True Score + Error. If you administer the same test to the same person twice under identical conditions, the true score should be the same both times. Any difference in observed score is error. **Reliability** is the proportion of variance in observed scores that reflects true score variance — formally, σ²_T / σ²_X. A reliability of 0.80 means 80% of the observed score variance is true variance and 20% is error. Different types of reliability target different sources of error.

**Internal consistency** (measured by **Cronbach's alpha**) asks: do the items on this scale all pull in the same direction? It targets error from sampling items — if you replaced half the items with other items measuring the same construct, would the scores stay the same? Alpha is computed from the average inter-item correlation and the number of items: longer scales with higher inter-item correlations yield higher alpha. The connection to your knowledge of correlations is direct — alpha is essentially a function of the average pairwise item correlation. The target of α > 0.70 is a rough heuristic; for high-stakes clinical decisions, you want α > 0.90 because lower reliability means individual scores could be far off. **Test-retest reliability** asks about stability over time — error from temporal inconsistency in measurement. **Inter-rater reliability** asks whether two independent judges produce the same score — error from observer subjectivity.

The most critical practical implication is that **reliability sets a ceiling on validity**. If a scale measures with error, the correlation between that scale and any external criterion is mathematically attenuated — reduced toward zero by the noise in the scores. The correction for attenuation formula makes this explicit: the maximum possible correlation between two measures equals the square root of the product of their reliabilities. A scale with alpha = 0.60 can correlate at most about 0.77 with a perfectly reliable criterion. Before asking "does this measure predict what it should predict?", you must ask "is this measure consistent enough that it could even detect a real relationship?" Unreliable measurement is not just imprecise — it systematically undermines the scientific conclusions you can draw.
