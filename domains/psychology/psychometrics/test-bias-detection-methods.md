---
id: test-bias-detection-methods
title: Test Bias Detection Methods and Statistical Approaches
domain: psychology
course: psychometrics
prerequisites:
- id: differential-item-functioning
  type: hard
- id: validity-in-measurement
  type: hard
tags:
- bias-detection
- fairness
- dif
- invariance
- equity
stage: expert
status: validated
---

# Test Bias Detection Methods and Statistical Approaches

## Core Idea
Beyond differential item functioning (DIF), psychometricians use multiple statistical methods to detect bias: Mantel-Haenszel and logistic regression for DIF, measurement invariance testing via confirmatory factor analysis, item response bias methods, and comparisons of latent means across groups. Understanding which statistical approaches target which types of bias helps practitioners identify and remediate sources of unfairness in testing.

## Questions

```yaml
- question: "A test developer applies the Mantel-Haenszel procedure to an item and finds no significant DIF. A measurement colleague argues the item could still be biased. Under what condition would the colleague be correct?"
  type: multiple-choice
  options:
    - "If the item has low test-retest reliability, MH produces inflated false-negative rates"
    - "If the DIF effect reverses direction across ability levels (non-uniform DIF), MH would not detect it"
    - "The colleague is wrong; a non-significant MH result establishes that the item is unbiased"
    - "MH cannot be trusted for items in the middle difficulty range"
  answer: 1
  explanation: "The Mantel-Haenszel procedure assumes the DIF effect is uniform — the same direction and magnitude at every point on the ability scale. It summarizes data into a single odds ratio across strata. If the item actually shows non-uniform DIF (favoring one group at low ability but the other at high ability), MH's averaging would obscure the effect. Logistic regression, which includes an interaction term between group and total score, can detect non-uniform DIF. This distinction matters practically because non-uniform DIF cannot be corrected by aggregate adjustments."

- question: "A research team wants to compare latent mean scores on a depression scale between British and Korean samples to determine whether one population is more depressed on average. What statistical requirement must be met for this comparison to be valid?"
  type: multiple-choice
  options:
    - "The scale must achieve Cronbach's alpha ≥ 0.80 in both samples"
    - "The samples must be matched on age, gender, and education"
    - "Scalar measurement invariance must hold — the same factor loadings and item intercepts across groups"
    - "No individual item should show significant DIF in either sample"
  answer: 2
  explanation: "Latent mean comparisons require scalar invariance: not only must the items load on the same factors with the same magnitudes (metric invariance), but the items' intercepts — their baseline response tendencies — must be the same across groups. If intercepts differ, group members at the same latent level of depression would respond differently to items, making the scales non-comparable. Scalar invariance is the specific, often-violated condition that licenses cross-group latent mean comparison. High reliability does not ensure invariance; matching on demographics does not replace measurement equivalence testing."

- question: "Non-uniform DIF is more problematic than uniform DIF because it cannot be corrected by simply adjusting total scores — the group difference changes direction or magnitude across the ability distribution."
  type: true-false
  answer: true
  explanation: "Uniform DIF produces a consistent advantage for one group at all ability levels — while unfair, it creates a predictable, constant offset that might be addressable through item removal or score adjustment. Non-uniform DIF is more insidious: the advantage switches direction (or varies substantially) across ability levels, meaning there is no single correction that equalizes group performance. It distorts the measurement relationship differentially, undermining the validity of the test for all score comparisons between groups."

- question: "Establishing that a scale has the same factor structure (configural invariance) in two groups is sufficient to support valid comparisons of latent means across those groups."
  type: true-false
  answer: false
  explanation: "Configural invariance only establishes that the same items load on the same factors in both groups — it says nothing about whether the loadings or intercepts are numerically equal. Metric invariance (equal loadings) is required before comparing relationships between latent variables. Scalar invariance (equal loadings AND equal intercepts) is required before comparing latent means. Each level of invariance is a stronger constraint; only scalar invariance licenses the specific claim that a given latent score represents the same standing across groups."

- question: "Why is test bias detection considered a form of validity evidence collection, rather than a separate psychometric concern?"
  type: short-answer
  answer: "Validity is the degree to which a test measures what it is intended to measure. If a test item or scale measures one construct for one group but a slightly different construct (or the same construct plus group-related noise) for another, the test is not valid for cross-group comparisons — regardless of its internal consistency. Detecting DIF and invariance violations is directly testing whether the measurement model holds across groups, which is a core validity question. Bias is a specific type of construct-irrelevant variance, and bias detection is the empirical process of identifying it."
  explanation: "The connection to validity is not just definitional — it has practical consequences. A test reported to be 'reliable and valid' in a general sense may still be invalid for specific comparisons (e.g., group mean differences) if measurement invariance has not been tested. Bias detection methods operationalize the validity inquiry: they turn the abstract question 'does this test mean the same thing for everyone?' into testable statistical hypotheses."
```

## Explainer

From your study of differential item functioning, you understand the basic definition: an item shows DIF when examinees from different groups who have the *same underlying ability* nonetheless have different probabilities of answering correctly. DIF is the statistical signal that something about the item — its wording, its cultural assumptions, its imagery — is creating group-related variance that should not be there. The detection methods you are learning now are the practical toolkit for finding and diagnosing that signal with confidence.

The **Mantel-Haenszel (MH) procedure** is the oldest and most widely used DIF detection method. It works by stratifying examinees into ability groups (usually by total score) and then comparing, within each stratum, the proportions of reference and focal group members who answered correctly. Because examinees in the same stratum have similar total scores, ability is held roughly constant — any remaining difference in item performance is a DIF signal. The MH statistic summarizes this across all strata as a common odds ratio. An odds ratio near 1.0 means no DIF; departures from 1.0 indicate that one group has systematically higher odds of success on this item even after matching on ability. MH is computationally simple and robust, but it assumes the DIF effect is uniform across ability levels — the same direction and magnitude at every point on the ability scale.

**Logistic regression DIF** relaxes this restriction. By regressing item response on group membership, total score, and their interaction, logistic regression can detect both **uniform DIF** (consistent group advantage at all ability levels) and **non-uniform DIF** (the group difference reverses or varies across ability levels). Non-uniform DIF is particularly problematic because it cannot be canceled out by aggregate-level adjustments; it distorts the measurement relationship differentially across the ability distribution.

These item-level methods catch item-specific bias, but **measurement invariance testing** via confirmatory factor analysis scales up to ask whether the *entire factor structure* is equivalent across groups. Testing invariance requires a sequence of increasingly constrained models: configural (same structure), metric (same factor loadings), and scalar (same item intercepts) invariance. Scalar invariance is required to meaningfully compare latent means across groups — the condition that is often violated when systematic bias exists. Connecting back to your validity training: any form of bias is a validity threat. An item or scale that measures one construct in one group but a slightly different construct in another group is not valid for cross-group comparisons, regardless of its reliability. Bias detection is validity evidence collection in action.
