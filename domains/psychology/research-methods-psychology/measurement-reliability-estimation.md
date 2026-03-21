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
stage: formal-systems
status: draft
---

# Measurement Reliability: Types and Estimation

## Core Idea
Reliability is consistency of measurement across items (internal consistency), raters (inter-rater), time (test-retest), or forms (parallel). Each type addresses different sources of error. Coefficient alpha, intraclass correlations, and test-retest correlations quantify reliability. Unreliable measurement attenuates relationships and reduces statistical power; reliability sets an upper bound on validity.

## How It's Best Learned
Calculate Cronbach's alpha for a published scale. Review reliability coefficients in research papers and interpret their magnitude. Discuss which type of reliability (internal, test-retest, inter-rater) is most important for different measurement contexts.

## Common Misconceptions
- Reliability and validity are the same; - High internal consistency always indicates unidimensionality; - Alpha > 0.7 is sufficient for all uses; - One reliability estimate applies to all samples and times.

## Questions

```yaml
- question: "A researcher develops a new anxiety scale and finds that Cronbach's alpha = 0.62. The scale correlates r = 0.45 with a clinician-rated anxiety measure. What is the most accurate interpretation?"
  type: multiple-choice
  options:
    - "The scale is valid because r = 0.45 is a respectable correlation"
    - "The observed correlation is likely attenuated by measurement error; the true relationship could be considerably stronger"
    - "The scale must be invalid since alpha is below 0.70"
    - "Alpha and the validity correlation are unrelated — reliability and validity measure different things independently"
  answer: 1
  explanation: "Low reliability attenuates observed correlations toward zero — the correction for attenuation formula shows that the maximum possible correlation with a perfectly reliable criterion is √(alpha) ≈ 0.79 for alpha = 0.62. The observed r = 0.45 likely understates the true relationship because measurement noise in the scale is diluting the signal. This illustrates why reliability sets a ceiling on validity: an unreliable scale cannot reveal the true strength of relationships even if the construct itself is theoretically sound."

- question: "A researcher administers the same depression scale to participants twice, three weeks apart, and correlates the two sets of scores. What source of measurement error is this procedure designed to assess?"
  type: multiple-choice
  options:
    - "Error from sampling items — whether different items would produce the same scores"
    - "Error from rater subjectivity — whether different observers score the same behavior consistently"
    - "Error from temporal inconsistency — whether scores are stable over time in the absence of real change"
    - "Error from social desirability — whether participants answer honestly"
  answer: 2
  explanation: "Test-retest reliability specifically targets temporal instability as a source of measurement error. If the construct is stable (depression levels haven't changed in three weeks), any score difference reflects error — fluctuations in attention, mood on the test day, memory of prior responses, etc. This is distinct from internal consistency (alpha), which asks whether items within a single administration agree with each other, and inter-rater reliability, which targets observer disagreement. Each type of reliability isolates a different error source."

- question: "Reliability sets a ceiling on validity: a measure cannot correlate more strongly with external criteria than its own reliability coefficient allows."
  type: true-false
  answer: true
  explanation: "The correction for attenuation makes this mathematically explicit. The maximum possible correlation between two measures equals √(r_xx × r_yy), where r_xx and r_yy are the reliabilities of each measure. If a scale has alpha = 0.70, it can correlate at most √0.70 ≈ 0.84 with a perfectly reliable criterion. Measurement error in the scores systematically dilutes observed correlations toward zero. This is why reliability is prerequisite to validity — you must first establish that your measure is consistent before asking whether it measures what it should."

- question: "A scale with high internal consistency (Cronbach's alpha = 0.92) is measuring a single, unified psychological construct."
  type: true-false
  answer: false
  explanation: "High alpha reflects high average inter-item correlations, which can occur even when items tap multiple related but distinct factors — a condition called multidimensionality. Alpha is a measure of consistency, not unidimensionality. For example, a 20-item scale might have two clusters of 10 items each measuring different but correlated facets; the overall alpha could be high while the scale is actually bidimensional. Establishing unidimensionality requires factor analysis or other structural methods, not just inspecting alpha."

- question: "Why does unreliable measurement systematically undermine scientific conclusions about whether a construct predicts outcomes, rather than simply making estimates less precise?"
  type: short-answer
  answer: "Unreliable measurement introduces random error that attenuates observed correlations toward zero — it does not just add noise around the true value, it biases estimates of relationships downward. The correction for attenuation formula shows the true correlation is the observed correlation divided by the square root of the product of the two measures' reliabilities. This means a researcher using unreliable measures will routinely conclude that constructs are less related than they truly are, leading to false negatives and underestimates of effect sizes. Unreliability does not produce random over- and under-estimates that average out — it systematically suppresses observed relationships."
  explanation: "The asymmetry is crucial: random measurement error does average out for individual scores (the mean is unbiased), but it does NOT average out for correlations and regression coefficients. Those statistics are based on covariance, and random error in one or both measures reduces observed covariance. The practical implication is that any field using unreliable measures will systematically underestimate the predictive validity of its constructs, potentially dismissing theoretically sound variables as empirically weak when the problem is actually the measurement tool."
```

## Explainer

From your work on operational measurement, you know that every construct must be defined in terms of observable indicators — the behaviors, responses, or outcomes that stand in for the underlying theoretical variable. The moment you operationalize, you introduce the possibility of **measurement error**: the gap between your observed score and the true score you are trying to capture. Reliability is the study of that gap — specifically, how consistent the observed score is across different conditions under which you would expect it to stay the same.

The most important conceptual anchor is **Classical Test Theory's** decomposition: Observed Score = True Score + Error. If you administer the same test to the same person twice under identical conditions, the true score should be the same both times. Any difference in observed score is error. **Reliability** is the proportion of variance in observed scores that reflects true score variance — formally, σ²_T / σ²_X. A reliability of 0.80 means 80% of the observed score variance is true variance and 20% is error. Different types of reliability target different sources of error.

**Internal consistency** (measured by **Cronbach's alpha**) asks: do the items on this scale all pull in the same direction? It targets error from sampling items — if you replaced half the items with other items measuring the same construct, would the scores stay the same? Alpha is computed from the average inter-item correlation and the number of items: longer scales with higher inter-item correlations yield higher alpha. The connection to your knowledge of correlations is direct — alpha is essentially a function of the average pairwise item correlation. The target of α > 0.70 is a rough heuristic; for high-stakes clinical decisions, you want α > 0.90 because lower reliability means individual scores could be far off. **Test-retest reliability** asks about stability over time — error from temporal inconsistency in measurement. **Inter-rater reliability** asks whether two independent judges produce the same score — error from observer subjectivity.

The most critical practical implication is that **reliability sets a ceiling on validity**. If a scale measures with error, the correlation between that scale and any external criterion is mathematically attenuated — reduced toward zero by the noise in the scores. The correction for attenuation formula makes this explicit: the maximum possible correlation between two measures equals the square root of the product of their reliabilities. A scale with alpha = 0.60 can correlate at most about 0.77 with a perfectly reliable criterion. Before asking "does this measure predict what it should predict?", you must ask "is this measure consistent enough that it could even detect a real relationship?" Unreliable measurement is not just imprecise — it systematically undermines the scientific conclusions you can draw.
