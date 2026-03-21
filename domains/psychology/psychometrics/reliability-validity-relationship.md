---
id: reliability-validity-relationship
title: 'Reliability and Validity: Foundational Relationship'
domain: psychology
course: psychometrics
prerequisites:
- id: classical-test-theory
  type: hard
- id: measurement-scales-psychology
  type: soft
builds-toward:
- test-retest-reliability
- construct-validity-multitrait
- validity-evidence-frameworks
tags:
- reliability
- validity
- measurement-quality
stage: advanced
status: draft
---

# Reliability and Validity: Foundational Relationship

## Core Idea
Reliability measures consistency and reproducibility of test scores; validity measures whether a test actually measures the construct it claims to measure. A test must be reliable to be valid, but high reliability does not guarantee validity. Both are essential prerequisites for meaningful psychological measurement.

## Questions

```yaml
- question: "A researcher develops an 'executive function' test with excellent test-retest reliability (r = 0.95). Validation studies show it correlates r = 0.90 with processing speed but only r = 0.30 with established executive function tasks. What does this demonstrate?"
  type: multiple-choice
  options:
    - "The test is both reliable and valid — high reliability proves it is measuring consistently"
    - "The test is reliable but not valid — it consistently measures processing speed, not executive function"
    - "The high reliability sets a ceiling on validity, mathematically explaining the low validity coefficient"
    - "Validity cannot be assessed without knowing the reliability of the criterion measures"
  answer: 1
  explanation: "This is the classic demonstration that reliability is not sufficient for validity. The test is highly consistent (r = 0.95 test-retest) but consistently measuring the wrong thing — processing speed, not executive function. A miscalibrated scale is analogous: it gives the same wrong reading every time. Option C misapplies the ceiling concept; the ceiling (√0.95 ≈ 0.97) is not what limits the validity — the test is simply measuring a different construct."

- question: "A cognitive ability test has a reliability coefficient of r_xx = 0.64. What is the theoretical maximum validity coefficient it could possibly achieve against any external criterion?"
  type: multiple-choice
  options:
    - "0.64, since validity cannot exceed reliability"
    - "0.80, the square root of the reliability coefficient"
    - "1.00, since validity is conceptually independent of reliability"
    - "0.41, the square of the reliability coefficient"
  answer: 1
  explanation: "The attenuation formula sets the validity ceiling at √(r_xx · r_yy), and with perfect criterion reliability (r_yy = 1.0), the ceiling is √r_xx = √0.64 = 0.80. Unreliable test scores are too noisy to correlate strongly with anything. Option A is wrong: reliability and validity are measured differently — a validity coefficient can in principle exceed the reliability coefficient in a narrow sense, but the ceiling is √r_xx, not r_xx itself. Option C is the common misconception: thinking reliability and validity are independent."

- question: "A test with near-zero test-retest reliability cannot be a valid measure of any stable psychological construct."
  type: true-false
  answer: true
  explanation: "If a test is unreliable, its scores are dominated by random measurement error. Such scores cannot systematically reflect any stable construct — including the intended one. A test-retest correlation near zero means the same person's score changes substantially from one measurement to the next, which cannot reflect stable variation in the underlying attribute. The reliability coefficient places a mathematical ceiling on validity: √(near zero) ≈ near zero. Reliability is the floor, not the goal, but without it, validity is impossible."

- question: "Achieving a very high internal consistency coefficient (e.g., Cronbach's α = 0.95) is sufficient evidence that a test is measuring the intended psychological construct."
  type: true-false
  answer: false
  explanation: "High alpha means the items are strongly intercorrelated — they all measure the same thing consistently. But 'the same thing' might not be the intended construct. A collection of highly intercorrelated questions about fatigue, sleep, and appetite will yield high alpha while potentially measuring the somatic side effects of a medical illness rather than depression itself. Internal consistency is one form of reliability, and reliability is necessary but not sufficient for validity. Validity requires external evidence: correlations with theoretically related measures, predictions of relevant outcomes, and the full validity argument."

- question: "Explain in your own words why reliability is a necessary condition for validity but not a sufficient one. Use a concrete analogy or example to illustrate the asymmetry."
  type: short-answer
  answer: "Reliability is necessary because unreliable scores (dominated by random error) cannot systematically reflect any construct — their ceiling on validity is near zero. But reliability is not sufficient because a test can consistently measure the wrong thing: e.g., a test of 'math ability' that reliably measures reading speed is useless for assessing math. High reliability tells you the test is measuring something stably; validity tells you whether that something is what you intended."
  explanation: "The classic analogy is a miscalibrated scale that reads 5 lbs too heavy on every weighing: highly reliable (same wrong answer every time) but not valid for knowing your true weight. In psychology, the head circumference example from phrenology illustrates this starkly — head size can be measured with excellent reliability but has essentially no validity as a measure of intelligence. Reliability is the floor; once achieved, validation work begins by examining whether scores relate to other measures in theoretically predicted ways."
```

## Explainer

Classical test theory, which you've studied, gives us a precise framework for thinking about scores: any observed score is the sum of a true score and measurement error. **Reliability** asks how much of the score variance is true score variance versus error variance. A highly reliable test produces scores that are consistent — test the same person again under the same conditions, and you get nearly the same score. This consistency reflects minimal random measurement error. Reliability is formally the ratio of true score variance to observed score variance, and all the specific reliability coefficients (test-retest, internal consistency, inter-rater) are different methods for estimating this underlying quantity.

**Validity** asks a different question entirely: does the score actually represent what you claim it represents? A test can be perfectly consistent — measuring the same thing every time — while measuring the wrong thing. The classic analogy is a miscalibrated scale that reads 5 lbs too heavy every time: highly reliable (consistent), but not valid for knowing your true weight. In psychological measurement, a test of "intelligence" that is actually measuring reading speed is reliable if reading speed is stable, but it is not a valid measure of the construct intelligence. Validity is about the *interpretation* and *use* of scores, not just their consistency.

The foundational asymmetric relationship is this: **reliability is necessary but not sufficient for validity**. The necessity follows from a mathematical fact. If a test is unreliable — if its scores are dominated by random error — then those scores cannot systematically reflect any construct, including the intended one. A test-retest correlation of 0.40 places a ceiling on the validity coefficient of roughly 0.63 (the square root of the reliability product), meaning no validity evidence can exceed that ceiling regardless of how well the test was designed. Unreliable scores are too noisy to correlate with anything meaningfully. So reliability is the precondition.

But reliability is not sufficient because a consistent measure can consistently track the wrong construct. A carefully standardized measure of head circumference is highly reliable; it is not a valid measure of intelligence, despite phrenologists once claiming otherwise. More subtle examples pervade psychology: a depression scale that reliably measures somatic complaints (fatigue, sleep, appetite) may have low validity as a measure of cognitive-affective depression in medically ill patients who have somatic symptoms from their illness, not their mood. High internal consistency (one form of reliability) can even work against validity by encouraging narrow item pools that over-represent easily measurable symptoms while omitting theoretically central aspects of the construct.

This relationship has direct consequences for test development strategy. Reliability should be established first and treated as a floor, not a goal in itself. Once acceptable reliability is achieved, validation work begins: accumulating evidence that scores relate to other measures in theoretically predicted ways (**convergent validity**), that they don't over-relate to measures of different constructs (**discriminant validity**), and that they predict outcomes they should predict (**criterion validity**). Modern validity theory — especially as articulated in the Standards for Educational and Psychological Testing — treats all these lines of evidence as contributing to a unified validity argument, not as separate types of validity. The question is always: do the accumulated evidence and theory support the proposed interpretation and use of this score?

