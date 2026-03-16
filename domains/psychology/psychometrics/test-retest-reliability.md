---
id: test-retest-reliability
title: Test-Retest Reliability and Temporal Stability
domain: psychology
course: psychometrics
prerequisites:
- id: classical-test-theory
  type: hard
- id: correlation-coefficient
  type: soft
builds-toward:
- generalizability-theory-g-theory
tags:
- reliability
- stability
- trait-measurement
stage: advanced
status: draft
---

# Test-Retest Reliability and Temporal Stability

## Core Idea
Test-retest reliability assesses score stability over time by administering the same test at two time points and correlating results. This method assumes the construct being measured remains stable. It is most appropriate for stable traits (personality, intelligence) rather than knowledge or skills that improve with practice.

## How It's Best Learned
Compare test-retest correlations for different construct types (stable traits vs. abilities) and examine how retest intervals affect stability coefficients. Analyze when other reliability methods are more appropriate.

## Common Misconceptions
High test-retest reliability guarantees validity. A test can be stable but not measure the intended construct. Also, the time interval between administrations significantly affects obtained correlations, requiring careful documentation.

## Explainer

Classical test theory, your prerequisite, establishes that every observed score is a composite of true score plus random error. Reliability, in that framework, is the proportion of score variance that is true-score variance — a signal-to-noise ratio. But there are multiple ways that noise can enter measurement, and each reliability method targets a different source. Internal consistency (alpha) asks whether items are measuring the same thing right now. **Test-retest reliability** asks a different question entirely: does the measurement give the same answer at different points in time? It targets a specific noise source — temporal instability — and is the appropriate reliability estimate when the construct you are measuring is supposed to be stable.

The method is straightforward: administer the same instrument to the same people twice, separated by a time interval, then compute the correlation between the two sets of scores. This correlation coefficient is the **stability coefficient**. A coefficient of 0.85 means that 85% of score variance at time 2 is predictable from time 1 scores — the remaining 15% represents either random measurement error or genuine change in the construct. The interpretation hinges entirely on a theoretical claim: if you believe the construct is a stable trait, low test-retest reliability is a problem with the measurement. If you believe the construct changes over the interval, then low test-retest reliability may reflect real change rather than measurement failure.

This is why construct type determines whether test-retest is the right reliability strategy. Personality traits like extraversion or neuroticism are theorized to be stable across months and years — test-retest reliability over a six-month interval is a meaningful criterion for a personality measure. But a measure of current anxiety state, by design, should fluctuate as circumstances change — using test-retest over a two-week interval would not reveal measurement error so much as genuine temporal change. For skills that improve with practice — reading speed, arithmetic fluency — test-retest over any interval conflates reliability with learning, making the stability coefficient difficult to interpret. The safest approach for learning-sensitive constructs is to use alternative forms rather than identical retest.

The **retest interval** is the most consequential methodological decision in test-retest studies. Very short intervals (hours, days) inflate reliability estimates through **carry-over effects**: participants remember their previous responses and anchor to them, producing artificial consistency that does not reflect true stability. Very long intervals (years) deflate estimates through genuine developmental or environmental change. The "right" interval depends on the construct's theoretical rate of change. For intelligence tests, intervals of 1-6 months are common; for clinical state measures, 1-2 weeks is typical; for personality, 6 months to a year is informative. Research reports should always specify the interval, because a correlation of 0.85 over two weeks and 0.85 over two years communicate entirely different things about temporal stability.

A final subtlety connects test-retest to the broader reliability framework. Test-retest reliability and internal consistency can dissociate substantially, and both can be high while validity remains low. A personality scale might correlate 0.90 with itself over six months (highly stable) while correlating 0.20 with actual behavior in personality-relevant situations (low validity). Stability proves that the test measures something consistently over time; it does not prove that the something is the construct you intend to measure. Reliability is a necessary but not sufficient condition for validity — a lesson that applies with particular force to test-retest, where the seductive appeal of a high stability coefficient can mask a fundamentally mismeasured construct.

