---
id: reliability-in-measurement
title: Reliability in Psychological Measurement
domain: psychology
course: research-methods-psychology
prerequisites:
- id: operational-definitions
  type: hard
- id: measurement-scales-psychology
  type: soft
- id: correlation-coefficient
  type: soft
- id: measures-of-spread
  type: soft
- id: survey-research-methods
  type: soft
builds-toward:
- validity-in-measurement
tags:
- reliability
- test-retest
- inter-rater
- internal-consistency
- Cronbach-alpha
stage: formal-systems
status: validated
---
# Reliability in Psychological Measurement

## Core Idea
Reliability is the consistency of a measurement — the degree to which it produces the same result under the same conditions. Types include test-retest reliability (consistency over time), inter-rater reliability (consistency across observers), and internal consistency (coherence among items in a scale, assessed with Cronbach's alpha). Reliability is a necessary but not sufficient condition for validity: a measure can be reliably wrong. High reliability puts a ceiling on how valid a measure can be — an unreliable measure cannot be valid.

## How It's Best Learned
Compute Cronbach's alpha for a simple 5-item scale dataset. Then compare a reliable and unreliable measure of the same construct and explain how each would affect a study's conclusions.

## Common Misconceptions
- Reliability does not mean accuracy — a bathroom scale consistently reading 5 kg too heavy is reliable but not valid.
- Cronbach's alpha above .70 is often cited as 'acceptable,' but context matters — clinical measures may require .90+.

## Questions

```yaml
- question: "A bathroom scale consistently reads 5 kg heavier than your true weight, every single time. How should this scale be characterized?"
  type: multiple-choice
  options: ["Neither reliable nor valid", "Both reliable and valid", "Reliable but not valid", "Valid but not reliable"]
  answer: 2
  explanation: "Reliability is about consistency — the scale produces the same result every time, so it is reliable. Validity is about accuracy — the scale does not measure your true weight, so it is not valid. This example illustrates that reliability is necessary but not sufficient for validity."

- question: "A psychological measure with high reliability is necessarily also high in validity."
  type: true-false
  answer: false
  explanation: "Reliability puts a ceiling on validity — an unreliable measure cannot be valid — but a reliable measure can still measure the wrong thing entirely. A scale reliably measuring wrist circumference is not a valid measure of intelligence, no matter how consistent its readings."

- question: "What is internal consistency, and why is it important for multi-item psychological scales?"
  type: short-answer
  answer: "Internal consistency is the degree to which items on a scale correlate with one another — indicating they are measuring the same underlying construct. It is typically assessed with Cronbach's alpha. It matters because if scale items are not intercorrelated, the total score is an incoherent mixture of different things rather than a consistent measure of one construct."
  explanation: "A depression scale should have items that all tap into depression. If some items measure anxiety and others measure fatigue without any shared variance, the composite score loses interpretability. Cronbach's alpha captures this by measuring the average inter-item correlation, adjusted for scale length."
```

## Explainer

Before you can trust the conclusions of any psychological study, you need to ask a foundational question: is the measurement actually measuring what it claims to measure, and is it doing so consistently? Reliability addresses the second part — consistency — and it is a prerequisite for the first.

Think of reliability as the spread of measurement error. Every measurement contains some true score and some random error. If you repeat a measurement under identical conditions and get widely different results, the instrument has low reliability: most of the variance is error, not signal. Three types of reliability capture different sources of inconsistency. *Test-retest reliability* checks whether scores are stable over time (important for traits like personality, less important for states like mood). *Inter-rater reliability* checks whether different judges or observers score the same behavior consistently — critical in clinical diagnosis or behavioral observation research. *Internal consistency* checks whether items within a scale all tap the same underlying construct.

Cronbach's alpha, the standard measure of internal consistency, ranges from 0 to 1. It is mathematically equivalent to the average of all possible split-half correlations for the scale. An alpha of .80 means the items are moderately intercorrelated and likely measuring a coherent construct. The commonly cited cutoff of .70 is a rough rule for exploratory research; clinical tools that inform treatment decisions typically require .90 or higher, because low reliability means individual patients could score very differently on retesting through no real change in their condition.

The most important conceptual point is the relationship between reliability and validity. Reliability is a *necessary but not sufficient condition* for validity. A measure can be perfectly reliable — consistent, stable, precise — yet completely wrong. A thermometer that consistently reads 5°C too high is reliable; a personality questionnaire that consistently measures neuroticism when you think it's measuring extraversion is reliable. Neither is valid. In formula terms: validity ≤ √reliability. An unreliable measure cannot be valid because measurement error attenuates correlations with external criteria; a reliable measure might still be invalid because it is consistently measuring the wrong construct.

When you encounter a published scale, look at how reliability was assessed and in what population. Reliability is not a fixed property of an instrument — it depends on the range and homogeneity of scores in the sample. A scale with excellent reliability in a diverse community sample may show much lower reliability in a clinically homogeneous group, simply because there is less true-score variance for the items to capture. Understanding this context-dependence is essential for evaluating whether a measure is fit for purpose in a new research setting.
