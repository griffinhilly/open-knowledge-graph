---
id: true-score-theory-and-measurement-error
title: True Score Theory and Measurement Error
domain: psychology
course: psychometrics
prerequisites:
- id: classical-test-theory
  type: hard
builds-toward:
- domain-sampling-theory-reliability-generalization
- standard-error-of-measurement-applications
tags:
- classical-test-theory
- measurement-error
- reliability
stage: expert
status: validated
---

# True Score Theory and Measurement Error

## Core Idea
In classical test theory, an observed score equals the true score plus random error: X = T + E. True scores represent the expected value of measurements across infinite replications, while error is assumed random, uncorrelated with true scores, and independent across administrations. This foundational model underlies all reliability theory and score interpretation.

## Questions

```yaml
- question: "A student scores 85 on a standardized test with a reliability of .84 and a standard deviation of 15 (giving a standard error of measurement of 6). A psychologist interprets this result. Which interpretation is most consistent with classical test theory?"
  type: multiple-choice
  options:
    - "The student's true ability is exactly 85, with the reliability coefficient confirming the score's accuracy"
    - "The student would score 85 on every retest, since 84% of the variance is reliable"
    - "The observed score of 85 is an estimate of the true score, with uncertainty of roughly ±6 points — best interpreted as a range"
    - "The student's score is above average; the error term is irrelevant since the test is reliable enough"
  answer: 2
  explanation: "Classical test theory holds that X = T + E: the observed score is the true score plus random error. No single observed score can be equated with the true score. The SEM of 6 means that if the same person were tested many times, their scores would form a distribution with a standard deviation of about 6 points around their true score. The correct interpretation is a confidence interval (e.g., 85 ± 6), not a point estimate. High reliability reduces error but does not eliminate it — the error term always remains nonzero in practice."

- question: "If measurement error in a test is truly random and uncorrelated with true scores, what does this imply about the average error term across many administrations of the test to the same person?"
  type: multiple-choice
  options:
    - "The average error will equal the reliability coefficient"
    - "The average error will systematically inflate observed scores toward the population mean"
    - "The average error will approach zero, because random errors cancel out across repeated measurements"
    - "The average error will equal the standard deviation of the observed scores"
  answer: 2
  explanation: "Random error, by definition, has an expected value of zero. Positive errors (lucky guesses, momentary focus) and negative errors (distractions, fatigue) are equally likely and cancel out on average. This is why averaging many measurements gives a better estimate of the true score — the error term shrinks toward zero while the true score component accumulates. This is also why reliability can be improved by adding more items: more items average out more error."

- question: "A person's 'true score' in classical test theory refers to the actual, hidden ability level that the test is trying to uncover — a fixed, real quantity the person possesses."
  type: true-false
  answer: false
  explanation: "The true score is a statistical construct, not a metaphysical reality. It is defined as the expected value — the mathematical average — of a person's observed scores across hypothetical infinite replications under identical conditions. It is what their scores would converge to with unlimited measurement, not a 'real' ability stored somewhere in their brain. This distinction matters because it frames reliability and error as properties of the measurement process, not of the person's 'actual' ability."

- question: "Increasing the reliability of a test reduces the standard error of measurement, meaning individual scores become more precise estimates of the true score."
  type: true-false
  answer: true
  explanation: "The formula SEM = SD × √(1 − r) makes this relationship explicit. As reliability (r) increases toward 1.0, the term √(1 − r) decreases toward zero, and the SEM decreases. A perfectly reliable test (r = 1) would have SEM = 0, meaning every observed score perfectly equals the true score. In practice, as reliability increases from .80 to .90, the SEM decreases by about 30% (for the same SD), substantially tightening the confidence interval around each observed score."

- question: "Why is it incorrect to interpret an observed test score as a precise point estimate of ability, and what does the standard error of measurement tell us instead?"
  type: short-answer
  answer: "An observed score always contains random error (X = T + E), so it is an imprecise sample from a distribution of scores the person could obtain. The true score is the center of that distribution, but any single observation may deviate from it. The SEM quantifies how spread that distribution is: it tells you how much a person's observed scores would vary across retests due to error alone, and it enables constructing a confidence interval (e.g., observed score ± 1 SEM for ~68% confidence). The score should be reported as a range, not a single number."
  explanation: "This has direct clinical and educational consequences. Reporting an IQ of 112 as a precise number suggests a precision the test cannot deliver. Best practice is to report it as a range (e.g., 107–117) and make decisions only when scores are meaningfully above or below a cutoff — not near the boundary where error could flip the classification. The SEM is also the basis for evaluating whether a change in score from one testing to the next reflects genuine change or just measurement fluctuation."
```

## Explainer

Classical test theory begins with a deceptively simple equation: **X = T + E**. The observed score (X) is the number you actually get when someone takes a test. The true score (T) is the theoretical value that the person "really" has — the average they would obtain if you could give them the same test infinitely many times under identical conditions. The error (E) is everything else: guessing, momentary distraction, misread instructions, how the person happened to sleep the night before. This decomposition is so fundamental that nearly all of psychometrics is an elaboration of its implications.

The model makes several critical assumptions. **Error is random**: it is uncorrelated with the true score, so high-ability people don't have systematically higher or lower errors than low-ability people. This is why averaging helps — random errors cancel out, while the true score accumulates. **Errors across items and occasions are uncorrelated**: knowing that you got one item wrong by guessing doesn't tell you anything about the next item's error. And the true score is defined as the **expected value** of observed scores across repeated measurement — not a score the person "really has" in some metaphysical sense, but a statistical limit toward which their scores would converge with more measurement.

These assumptions have direct practical consequences. Because error is random and uncorrelated with T, the variance of observed scores equals the variance of true scores plus the variance of error: Var(X) = Var(T) + Var(E). **Reliability** is simply the proportion of observed-score variance that is true-score variance: r = Var(T) / Var(X). A perfectly reliable test would have no error variance; all variability in observed scores would reflect real differences between people. In practice, reliability coefficients of .80–.90 are considered good for psychological measures, meaning 10–20% of observed score variance is measurement error.

The practical payoff is **the standard error of measurement** (SEM): SEM = SD × √(1 − r), where SD is the standard deviation of observed scores. The SEM tells you how much an individual's score might fluctuate from measurement to measurement due to error alone, and it enables you to construct confidence intervals around observed scores. Crucially, this means no single test score should be interpreted as a precise point estimate — it is always an estimate with uncertainty. When a psychologist reports that a person has an IQ of 112, best practice is to interpret this as a range (perhaps 107–117) rather than a precise number, because the observed score contains error and the true score is never directly observed.
