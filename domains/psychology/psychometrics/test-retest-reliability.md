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
stage: expert
status: validated
---

# Test-Retest Reliability and Temporal Stability

## Core Idea
Test-retest reliability assesses score stability over time by administering the same test at two time points and correlating results. This method assumes the construct being measured remains stable. It is most appropriate for stable traits (personality, intelligence) rather than knowledge or skills that improve with practice.

## How It's Best Learned
Compare test-retest correlations for different construct types (stable traits vs. abilities) and examine how retest intervals affect stability coefficients. Analyze when other reliability methods are more appropriate.

## Common Misconceptions
High test-retest reliability guarantees validity. A test can be stable but not measure the intended construct. Also, the time interval between administrations significantly affects obtained correlations, requiring careful documentation.

## Questions

```yaml
- question: "A researcher develops a measure of 'current anxiety level' and finds a test-retest correlation of 0.25 over a four-week interval. They conclude the measure is unreliable. What is the most important alternative interpretation?"
  type: multiple-choice
  options:
    - "The measure lacks internal consistency among its items"
    - "The low correlation may reflect genuine fluctuation in anxiety over four weeks rather than measurement error, because anxiety is a state, not a stable trait"
    - "The retest interval was too short to detect true reliability"
    - "The sample was too homogeneous to produce a meaningful correlation"
  answer: 1
  explanation: "Test-retest reliability is only the appropriate reliability index when the construct being measured is theorized to be stable across the interval. Anxiety state is explicitly designed to fluctuate with circumstances — a four-week drop in anxiety could reflect real life changes, treatment effects, or natural variation. Calling this 'unreliability' confounds measurement error with genuine construct change. The correct strategy for state measures is to use an interval short enough that real change is unlikely, or to use internal consistency (alpha) as the reliability estimate instead."

- question: "A personality scale administered to the same people six months apart yields a stability coefficient of 0.88. What can you confidently conclude from this result alone?"
  type: multiple-choice
  options:
    - "The scale measures the intended personality construct accurately (high validity)"
    - "The scale's items are highly intercorrelated (high internal consistency)"
    - "People's scores on this scale are highly stable across a six-month interval (high temporal stability)"
    - "The scale would show equally high stability over a six-year interval"
  answer: 2
  explanation: "A high stability coefficient tells you that scores are consistent over time — temporal stability. It says nothing about whether the test is measuring what it claims to measure (validity), whether the items cohere with each other (internal consistency), or whether stability generalizes to different intervals. A measure can be perfectly stable over six months while measuring the wrong construct entirely. Reliability, including test-retest reliability, is necessary but not sufficient for validity."

- question: "Very short retest intervals (hours or days) can artificially inflate stability coefficients because participants remember their previous responses and anchor to them."
  type: true-false
  answer: true
  explanation: "This carry-over effect is a major threat to validity in test-retest studies. When participants recall how they responded previously, they tend to give similar answers — not because the construct is stable, but because of memory. This produces inflated correlations that overestimate true temporal stability. The solution is to use intervals long enough for specific item responses to fade from memory, but not so long that genuine construct change becomes the dominant source of variance."

- question: "Demonstrating high test-retest reliability over six months is sufficient evidence that a psychological measure is both reliable and valid."
  type: true-false
  answer: false
  explanation: "High test-retest reliability proves only that the measure is stable over time — that it is consistently measuring *something*. It provides no evidence about whether that something is the intended construct. A scale claiming to measure extroversion might correlate 0.90 with itself over six months while correlating 0.10 with actual extroverted behavior. Reliability is a prerequisite for validity, not a proxy for it. Validity requires additional evidence — convergent, discriminant, and criterion-related — beyond stability alone."

- question: "Why does the length of the retest interval fundamentally affect the interpretation of a stability coefficient, and what principle should guide the choice of interval for a measure of a stable personality trait?"
  type: short-answer
  answer: "The stability coefficient conflates measurement error with genuine construct change — and the relative contribution of each depends entirely on the interval. Over a very short interval, memory effects inflate the coefficient while genuine change is minimal. Over a very long interval, real developmental or environmental change deflates it, even if the measurement itself is perfectly reliable. For a stable personality trait, the interval should be long enough that carry-over memory effects are negligible but short enough that true developmental change in the trait is not expected. For personality traits theorized to be stable across the adult lifespan, intervals of 6 months to 2 years are typical — long enough for memory to fade, short enough that life-stage change is modest for most individuals."
  explanation: "The key insight is that 'stability coefficient of 0.85' communicates entirely different information depending on whether the interval is two weeks or two years. Research must always report the interval and justify its selection relative to the theoretical rate of change in the construct. Without this, the coefficient cannot be meaningfully interpreted."
```

## Explainer

Classical test theory, your prerequisite, establishes that every observed score is a composite of true score plus random error. Reliability, in that framework, is the proportion of score variance that is true-score variance — a signal-to-noise ratio. But there are multiple ways that noise can enter measurement, and each reliability method targets a different source. Internal consistency (alpha) asks whether items are measuring the same thing right now. **Test-retest reliability** asks a different question entirely: does the measurement give the same answer at different points in time? It targets a specific noise source — temporal instability — and is the appropriate reliability estimate when the construct you are measuring is supposed to be stable.

The method is straightforward: administer the same instrument to the same people twice, separated by a time interval, then compute the correlation between the two sets of scores. This correlation coefficient is the **stability coefficient**. A coefficient of 0.85 means that 85% of score variance at time 2 is predictable from time 1 scores — the remaining 15% represents either random measurement error or genuine change in the construct. The interpretation hinges entirely on a theoretical claim: if you believe the construct is a stable trait, low test-retest reliability is a problem with the measurement. If you believe the construct changes over the interval, then low test-retest reliability may reflect real change rather than measurement failure.

This is why construct type determines whether test-retest is the right reliability strategy. Personality traits like extraversion or neuroticism are theorized to be stable across months and years — test-retest reliability over a six-month interval is a meaningful criterion for a personality measure. But a measure of current anxiety state, by design, should fluctuate as circumstances change — using test-retest over a two-week interval would not reveal measurement error so much as genuine temporal change. For skills that improve with practice — reading speed, arithmetic fluency — test-retest over any interval conflates reliability with learning, making the stability coefficient difficult to interpret. The safest approach for learning-sensitive constructs is to use alternative forms rather than identical retest.

The **retest interval** is the most consequential methodological decision in test-retest studies. Very short intervals (hours, days) inflate reliability estimates through **carry-over effects**: participants remember their previous responses and anchor to them, producing artificial consistency that does not reflect true stability. Very long intervals (years) deflate estimates through genuine developmental or environmental change. The "right" interval depends on the construct's theoretical rate of change. For intelligence tests, intervals of 1-6 months are common; for clinical state measures, 1-2 weeks is typical; for personality, 6 months to a year is informative. Research reports should always specify the interval, because a correlation of 0.85 over two weeks and 0.85 over two years communicate entirely different things about temporal stability.

A final subtlety connects test-retest to the broader reliability framework. Test-retest reliability and internal consistency can dissociate substantially, and both can be high while validity remains low. A personality scale might correlate 0.90 with itself over six months (highly stable) while correlating 0.20 with actual behavior in personality-relevant situations (low validity). Stability proves that the test measures something consistently over time; it does not prove that the something is the construct you intend to measure. Reliability is a necessary but not sufficient condition for validity — a lesson that applies with particular force to test-retest, where the seductive appeal of a high stability coefficient can mask a fundamentally mismeasured construct.

