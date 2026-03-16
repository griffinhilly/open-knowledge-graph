---
id: split-half-reliability-spearman-brown
title: Split-Half Reliability and the Spearman-Brown Prophecy Formula
domain: psychology
course: psychometrics
prerequisites:
- id: test-retest-reliability
  type: hard
- id: alpha-reliability-internal-consistency
  type: soft
builds-toward:
- reliability-estimation-method-selection
tags:
- split-half
- spearman-brown
- reliability-estimation
stage: advanced
status: draft
---

# Split-Half Reliability and the Spearman-Brown Prophecy Formula

## Core Idea
Split-half reliability divides a test into two halves, correlates them, and applies the Spearman-Brown formula to estimate full-length reliability: r_xx = 2r / (1 + r). This method is computationally simple but sensitive to how items are split; odd-even splits are preferable to arbitrary divisions to control for fatigue and item-order effects.

## Explainer

From test-retest reliability — your hard prerequisite — you know that one way to estimate reliability is to administer the same test twice and correlate the scores. The problem is that retesting introduces real complications: participants remember their answers, they learn between sessions, or they simply become different people over time. What if you wanted to estimate reliability from a *single* administration? Split-half reliability is the answer: you give the test once, artificially divide it into two halves, and treat those halves like two separate test administrations.

The logic is straightforward: if the test is measuring a stable construct reliably, then a person's score on the odd-numbered items should correlate highly with their score on the even-numbered items. Both halves are being administered to the same people, at the same time, measuring the same thing — so the only reason the two halves would disagree is measurement error. The correlation between the two half-scores, r, is therefore an estimate of reliability. But there is a catch: it is the reliability of a test that is *half as long* as the actual test.

This is where the **Spearman-Brown prophecy formula** comes in. One of the most robust findings in psychometrics is that longer tests are more reliable than shorter ones — more items means more sampling of the construct and less sensitivity to any single item's quirks. The formula r_xx = 2r / (1 + r) "prophesies" the reliability of the full-length test from the reliability of a half-length test. If the two halves correlate at r = .70, the predicted full-test reliability is 2(.70) / (1 + .70) = 1.40 / 1.70 ≈ .82. The formula works because adding a parallel half to a test is equivalent to doubling its length, and Spearman-Brown generalizes to predict the effect of multiplying test length by any factor k, not just 2.

The connection to your other prerequisite — alpha reliability — is close: coefficient alpha can be understood as the mean of all possible split-half reliabilities for a test. Alpha is preferred when items are not parallel (they vary in difficulty, intercorrelation, or content), because it does not depend on any particular split. Split-half reliability is best understood as the precursor to alpha that is easier to compute by hand and useful for teaching the underlying logic. The practical choice of splitting items by odd-even positions rather than first-half vs. second-half addresses a real confound: if participants tire or change strategy as a test progresses, the first-half / second-half split would artificially deflate the correlation, not because the test is unreliable, but because the two halves were taken under different conditions.


