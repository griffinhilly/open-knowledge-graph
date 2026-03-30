---
id: classical-test-theory
title: Classical Test Theory Foundations
domain: psychology
course: psychometrics
prerequisites:
- id: research-methods-psychology
  type: hard
- id: probability-and-statistics
  type: hard
- id: normal-distribution
  type: soft
- id: hypothesis-testing-framework
  type: soft
- id: correlation-coefficient
  type: soft
builds-toward:
- reliability-validity-relationship
- item-difficulty-discrimination
tags:
- test-theory
- measurement-error
- score-variance
stage: advanced
status: validated
---

# Classical Test Theory Foundations

## Core Idea
Classical test theory posits that an observed score comprises a true score plus random error. This framework provides methods to estimate reliability and understand score variance distributions. CTT focuses on total test score analysis and is foundational for understanding measurement precision and error.

## Questions

```yaml
- question: "According to CTT, if you could administer the same test to the same person an infinite number of times under identical conditions, their average observed score would converge to what?"
  type: multiple-choice
  options: ["Their score on the first administration", "Their true score", "The population mean on that test", "Zero, because errors accumulate"]
  answer: 1
  explanation: "The true score is formally defined in CTT as the expected value (mean) of observed scores over an infinite number of independent administrations. Because measurement errors are assumed to be random with a mean of zero, they cancel out over many trials, leaving only the true score. This definition makes the true score a theoretical construct — never directly observable."

- question: "In CTT, measurement error is assumed to be systematic — it consistently pushes a person's observed score in the same direction across repeated testings."
  type: true-false
  answer: false
  explanation: "CTT assumes errors are *random*, not systematic. Each testing occasion produces an independent error value drawn from a distribution with mean zero. Systematic errors (e.g., a test that is always too easy for a particular group) violate CTT assumptions and represent validity problems, not mere unreliability. This distinction between random error (reliability) and systematic error (bias/validity) is fundamental to measurement theory."

- question: "A test has a reliability coefficient of 0.90. What does this tell you about the relationship between observed scores and true scores on this test?"
  type: short-answer
  answer: "A reliability of 0.90 means that 90% of the variance in observed scores is attributable to true score variance, while 10% is measurement error variance. Equivalently, observed scores on this test are highly consistent — a person who takes it twice under similar conditions will likely get very similar scores. High reliability is necessary (but not sufficient) for a test to be useful."
  explanation: "In CTT, reliability is defined as the ratio of true score variance to observed score variance: r = σ²_T / σ²_X. Since σ²_X = σ²_T + σ²_E, a reliability of 0.90 means error accounts for only 10% of score variance. This is important because a test can only be valid if it is first reliable — you cannot measure what you intend to measure if scores are dominated by random noise."
```

## Explainer

Every time a person takes a test, their score is influenced by more than just what they actually know or how able they actually are. They may be tired, distracted by a question's wording, lucky on a guess, or unlucky on a difficult problem that they would usually solve. Classical test theory (CTT) is a mathematical framework that formally acknowledges this and gives us tools to reason about measurement precision despite it.

The central model is elegantly simple: **X = T + E**, where X is the observed score, T is the true score, and E is the random error. The true score is a theoretical construct — the score a person would get if measurement error averaged out completely, which you can think of as the long-run average over infinitely many independent testings. The error term E captures all the random, unsystematic factors that make any single administration noisy. Crucially, CTT assumes E has a mean of zero across repeated measurements: positive and negative errors cancel. This means your observed score on any given day is an unbiased estimate of your true score, just with noise added.

The practical payoff of this framework is the concept of **reliability**: the proportion of observed score variance that reflects true score variance rather than error. Formally, reliability ρ = σ²_T / σ²_X. A reliability of 1.0 would mean every observed score perfectly reflects the true score (no error at all). A reliability of 0 would mean observed scores are pure noise. In practice, well-constructed psychological tests aim for reliabilities of 0.80 or higher. Your statistics background is directly relevant here: variance decomposition (σ²_X = σ²_T + σ²_E) is the mathematical engine underlying CTT.

A critical distinction — one that CTT specifically cannot handle well — is between *random* error (which CTT models) and *systematic* error (which it does not). If a test is consistently harder for one demographic group due to biased item content, CTT's reliability coefficient will not detect this; the test may appear reliable while being systematically unfair. This limitation motivates more modern approaches like item response theory (IRT), but CTT remains the essential starting point for understanding what measurement precision means and how to quantify it.

The concepts you will encounter next — reliability-validity relationships and item difficulty/discrimination — extend directly from this foundation. Reliability is a necessary condition for validity (a noisy test cannot measure anything well), but not sufficient (a consistent test could still measure the wrong thing). Item-level analysis then lets you diagnose *which* specific questions contribute to error and which ones are doing the most work in distinguishing true score differences among test-takers.
