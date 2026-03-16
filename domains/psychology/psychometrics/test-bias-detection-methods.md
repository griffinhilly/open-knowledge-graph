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
stage: advanced
status: draft
---

# Test Bias Detection Methods and Statistical Approaches

## Core Idea
Beyond differential item functioning (DIF), psychometricians use multiple statistical methods to detect bias: Mantel-Haenszel and logistic regression for DIF, measurement invariance testing via confirmatory factor analysis, item response bias methods, and comparisons of latent means across groups. Understanding which statistical approaches target which types of bias helps practitioners identify and remediate sources of unfairness in testing.

## Explainer

From your study of differential item functioning, you understand the basic definition: an item shows DIF when examinees from different groups who have the *same underlying ability* nonetheless have different probabilities of answering correctly. DIF is the statistical signal that something about the item — its wording, its cultural assumptions, its imagery — is creating group-related variance that should not be there. The detection methods you are learning now are the practical toolkit for finding and diagnosing that signal with confidence.

The **Mantel-Haenszel (MH) procedure** is the oldest and most widely used DIF detection method. It works by stratifying examinees into ability groups (usually by total score) and then comparing, within each stratum, the proportions of reference and focal group members who answered correctly. Because examinees in the same stratum have similar total scores, ability is held roughly constant — any remaining difference in item performance is a DIF signal. The MH statistic summarizes this across all strata as a common odds ratio. An odds ratio near 1.0 means no DIF; departures from 1.0 indicate that one group has systematically higher odds of success on this item even after matching on ability. MH is computationally simple and robust, but it assumes the DIF effect is uniform across ability levels — the same direction and magnitude at every point on the ability scale.

**Logistic regression DIF** relaxes this restriction. By regressing item response on group membership, total score, and their interaction, logistic regression can detect both **uniform DIF** (consistent group advantage at all ability levels) and **non-uniform DIF** (the group difference reverses or varies across ability levels). Non-uniform DIF is particularly problematic because it cannot be canceled out by aggregate-level adjustments; it distorts the measurement relationship differentially across the ability distribution.

These item-level methods catch item-specific bias, but **measurement invariance testing** via confirmatory factor analysis scales up to ask whether the *entire factor structure* is equivalent across groups. Testing invariance requires a sequence of increasingly constrained models: configural (same structure), metric (same factor loadings), and scalar (same item intercepts) invariance. Scalar invariance is required to meaningfully compare latent means across groups — the condition that is often violated when systematic bias exists. Connecting back to your validity training: any form of bias is a validity threat. An item or scale that measures one construct in one group but a slightly different construct in another group is not valid for cross-group comparisons, regardless of its reliability. Bias detection is validity evidence collection in action.
