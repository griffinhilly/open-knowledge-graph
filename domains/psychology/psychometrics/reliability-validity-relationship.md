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

## Explainer

Classical test theory, which you've studied, gives us a precise framework for thinking about scores: any observed score is the sum of a true score and measurement error. **Reliability** asks how much of the score variance is true score variance versus error variance. A highly reliable test produces scores that are consistent — test the same person again under the same conditions, and you get nearly the same score. This consistency reflects minimal random measurement error. Reliability is formally the ratio of true score variance to observed score variance, and all the specific reliability coefficients (test-retest, internal consistency, inter-rater) are different methods for estimating this underlying quantity.

**Validity** asks a different question entirely: does the score actually represent what you claim it represents? A test can be perfectly consistent — measuring the same thing every time — while measuring the wrong thing. The classic analogy is a miscalibrated scale that reads 5 lbs too heavy every time: highly reliable (consistent), but not valid for knowing your true weight. In psychological measurement, a test of "intelligence" that is actually measuring reading speed is reliable if reading speed is stable, but it is not a valid measure of the construct intelligence. Validity is about the *interpretation* and *use* of scores, not just their consistency.

The foundational asymmetric relationship is this: **reliability is necessary but not sufficient for validity**. The necessity follows from a mathematical fact. If a test is unreliable — if its scores are dominated by random error — then those scores cannot systematically reflect any construct, including the intended one. A test-retest correlation of 0.40 places a ceiling on the validity coefficient of roughly 0.63 (the square root of the reliability product), meaning no validity evidence can exceed that ceiling regardless of how well the test was designed. Unreliable scores are too noisy to correlate with anything meaningfully. So reliability is the precondition.

But reliability is not sufficient because a consistent measure can consistently track the wrong construct. A carefully standardized measure of head circumference is highly reliable; it is not a valid measure of intelligence, despite phrenologists once claiming otherwise. More subtle examples pervade psychology: a depression scale that reliably measures somatic complaints (fatigue, sleep, appetite) may have low validity as a measure of cognitive-affective depression in medically ill patients who have somatic symptoms from their illness, not their mood. High internal consistency (one form of reliability) can even work against validity by encouraging narrow item pools that over-represent easily measurable symptoms while omitting theoretically central aspects of the construct.

This relationship has direct consequences for test development strategy. Reliability should be established first and treated as a floor, not a goal in itself. Once acceptable reliability is achieved, validation work begins: accumulating evidence that scores relate to other measures in theoretically predicted ways (**convergent validity**), that they don't over-relate to measures of different constructs (**discriminant validity**), and that they predict outcomes they should predict (**criterion validity**). Modern validity theory — especially as articulated in the Standards for Educational and Psychological Testing — treats all these lines of evidence as contributing to a unified validity argument, not as separate types of validity. The question is always: do the accumulated evidence and theory support the proposed interpretation and use of this score?

