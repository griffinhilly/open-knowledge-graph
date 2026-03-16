---
id: reliability-estimation-method-selection
title: Reliability Estimation Methods and Method Selection
domain: psychology
course: psychometrics
prerequisites:
- id: alpha-reliability-internal-consistency
  type: hard
- id: inter-rater-reliability-agreement
  type: soft
- id: correlation-coefficient
  type: soft
builds-toward:
- standard-error-of-measurement-applications
tags:
- reliability-types
- method-selection
- measurement-error
stage: advanced
status: draft
---

# Reliability Estimation Methods and Method Selection

## Core Idea
Different reliability methods estimate different error sources: test-retest measures temporal stability, internal consistency measures item homogeneity, and inter-rater reliability measures judge agreement. Choosing a method depends on construct and context; personality traits prioritize test-retest stability, ability measures prioritize internal consistency. Rarely is a single estimate sufficient for comprehensive reliability evidence.

## How It's Best Learned
Review published scales and identify what reliability evidence was reported. Compare studies that used different methods on the same construct and discuss why methods might differ.

## Common Misconceptions
- Assuming one reliability coefficient describes a test across all contexts (reliability is context- and population-specific)

## Explainer

From your work on Cronbach's alpha and inter-rater reliability, you know that reliability quantifies consistency in measurement. But "consistency" is not a single thing — it can mean stability over time, agreement across raters, or homogeneity across items. Different reliability methods answer different questions, and a thoughtful psychometrician chooses the method that matches the specific source of error most relevant to their construct and use case. Getting this wrong doesn't just produce a misleading number — it can lead you to conclude a measure is reliable when it isn't, or to apply a measure in contexts for which it was never validated.

**Test-retest reliability** measures temporal stability: administer the same measure to the same people twice, and correlate the two sets of scores. A high correlation (r = .85+) tells you the measure is picking up something stable rather than something that fluctuates moment to moment. This is the right method when your construct is a stable trait — personality, intellectual ability, chronic pain — because a "reliable" measure of a trait should produce similar scores when nothing about the person has changed. But test-retest is inappropriate when the construct *should* change (mood today vs. mood next week) or when practice effects contaminate the second administration. The **retest interval** matters enormously: too short, and participants remember their previous answers; too long, and true change contaminates the estimate.

**Internal consistency** — of which Cronbach's alpha is the most common index — measures whether items that are supposed to be measuring the same construct actually intercorrelate as expected. Alpha treats a multi-item scale as though all items were parallel forms, estimating reliability from item correlations at a single time point. This makes it ideal for ability tests and attitude scales, where you want items to converge on the same underlying construct. But alpha is insensitive to temporal stability (a scale with high alpha could still produce very different scores a week later if mood fluctuates) and it is inflated by simply adding more items. Alpha should be understood as a lower bound on reliability, not a direct estimate — and it tells you nothing about whether the items measure the *right* thing (that's validity, not reliability).

**Inter-rater reliability** applies when human judgment is involved in scoring: coding behavioral observations, rating interview responses, diagnosing clinical cases. Here the error source is not time or items but rater variability — different judges applying the same criteria may still score differently. The appropriate statistic depends on the measurement level: percent agreement is simple but doesn't correct for chance; **Cohen's kappa** corrects for chance agreement in categorical judgments; **intraclass correlation coefficients (ICCs)** extend this logic to continuous ratings and distinguish whether raters agree in their relative rankings (order) versus their absolute levels.

The key decision rule: **identify the primary source of error in your measurement context, then choose the method that directly estimates that error source**. For a personality scale used across sessions: test-retest. For a cognitive ability test with 30 items: internal consistency. For a structured clinical interview scored by two clinicians: inter-rater. In practice, a complete reliability case often requires multiple estimates. A clinical interview might need both inter-rater reliability (do two raters agree?) and test-retest reliability (does a patient's score remain stable if no true change occurred?). Reporting only one, as if it covers all bases, is the most common mistake in applied psychometrics.
