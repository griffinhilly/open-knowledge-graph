---
id: standard-scores-transformations
title: Standard Scores and Score Transformations
domain: psychology
course: psychometrics
prerequisites:
- id: norm-referenced-criterion-referenced-interpretation
  type: hard
- id: normal-distribution
  type: hard
builds-toward:
- diagnostic-cutoff-scores-classification-accuracy
tags:
- standard-scores
- z-scores
- t-scores
- transformation
stage: advanced
status: validated
---

# Standard Scores and Score Transformations

## Core Idea
Standard scores transform raw scores to a common metric with fixed mean and standard deviation. Z-scores (M=0, SD=1) are mathematically pure but have negative values; T-scores (M=50, SD=10) and IQ-type scores (M=100, SD=15) are more interpretable. Transformations preserve rank order and enable cross-test comparisons and form equating.

## Questions

```yaml
- question: "A student scores at the 84th percentile on a language assessment, reported as a T-score of 60. The same student's math score is reported as an IQ-type score of 115. A teacher says the math score is higher because 115 is a bigger number than 60. What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "The teacher is correct — 115 indicates stronger performance than 60 regardless of scale"
    - "T-scores and IQ-type scores are on different scales but both represent exactly one standard deviation above the mean, so the student performs equally above average in both areas"
    - "IQ-type scores are inherently more accurate, so the math score should be weighted more heavily"
    - "T-scores cannot be compared to IQ-type scores because they measure different psychological constructs"
  answer: 1
  explanation: "Both scores encode the same standing: T=60 means z=+1.00 (one SD above mean), and IQ=115 also means z=(115-100)/15=+1.00. A student who confuses the raw scale values is treating the number as meaningful in isolation rather than understanding it as a transformed expression of a z-score. The entire point of standard score systems is that they are linear transformations of one another — they carry identical information about relative standing, just expressed on different scales."

- question: "A z-score of +2.00 is equivalent to which set of standard scores?"
  type: multiple-choice
  options:
    - "T-score = 60, IQ-type score = 115"
    - "T-score = 70, IQ-type score = 130"
    - "T-score = 75, IQ-type score = 125"
    - "T-score = 65, IQ-type score = 120"
  answer: 1
  explanation: "The formula is: new score = M_new + (z × SD_new). For T-scores: 50 + (2.00 × 10) = 70. For IQ-type scores: 100 + (2.00 × 15) = 130. These correspond to the 97.7th percentile. Option A (T=60, IQ=115) represents z=+1.00, not z=+2.00 — a common confusion when students memorize isolated score values without internalizing the transformation formula."

- question: "Converting raw scores to T-scores or IQ-type scores changes students' rank order relative to their norm group."
  type: true-false
  answer: false
  explanation: "Standard score transformations are strictly linear: new score = M_new + z × SD_new. Linear transformations preserve rank order exactly. A student who scores at the 72nd percentile on raw scores will still be at the 72nd percentile after conversion to T-scores or IQ-type scores. This is why these scales can be meaningfully compared — the transformation changes the metric but not the relative ordering of scores."

- question: "A T-score of 70 and an IQ-type score of 130 convey identical information about a test-taker's standing in the norm group."
  type: true-false
  answer: true
  explanation: "Both scores equal z=+2.00. T=70 because 50+(2×10)=70; IQ=130 because 100+(2×15)=130. They are simply different skins on the same underlying z-score. This is the core insight of standard score transformations: the scale is chosen for communicability and convention, not because it encodes different or more precise information. Either score tells you the person is at approximately the 97.7th percentile."

- question: "Why do clinicians and educators prefer T-scores or IQ-type scores over z-scores when reporting test results, even though z-scores contain exactly the same information?"
  type: short-answer
  answer: "Z-scores have negative values and decimals that are confusing and potentially stigmatizing in applied contexts. A score of '-0.3' feels alarming to a parent even though it means near-average performance. T-scores and IQ-type scores eliminate negatives and use familiar integer-based scales, making scores easier to interpret and communicate. The choice is purely about practical communicability — the mathematical information content is identical across all standard score systems."
  explanation: "This is a case where the form of presentation matters for real-world use even when the content is identical. Psychometricians choose scales based on who will read the reports. T-scores (M=50, SD=10) are common in clinical and personality assessment; IQ-type scores (M=100, SD=15) are used in cognitive and ability testing. Neither is more 'accurate' — they are interchangeable via the z-score formula. Understanding this prevents clinicians from treating scores on different scales as if they measure different quantities."
```

## Explainer

From your study of the normal distribution, you know that raw scores on a test have a mean and standard deviation specific to that test and that particular sample. From norm-referenced interpretation, you know that the raw number itself is less important than where it falls relative to others in the norm group. Standard scores formalize this insight: they transform raw scores into a common metric so that a score on one test can be directly compared to a score on another — and so that any score's meaning is immediately interpretable by anyone who knows the scale.

The foundational standard score is the **z-score**: z = (X − M) / SD. This expresses each score as a number of standard deviations above or below the mean. A z-score of 0 is exactly at the mean; +1 means one standard deviation above; −2 means two standard deviations below. Because you know the normal distribution, you can translate any z-score directly into a percentile: z = +1.65 is approximately the 95th percentile; z = −1 is approximately the 16th percentile. Z-scores are mathematically elegant but practically awkward — negative values and decimals confuse test-takers and the people interpreting reports, and a score of "−0.3" feels stigmatizing even when it means near-average performance.

The solution is a **linear transformation**: new score = M_new + z × SD_new. This maps the z-score to a more readable scale while preserving all information — the same rank, the same distance from the mean, just expressed differently. **T-scores** use M=50, SD=10: a T-score of 60 is exactly one standard deviation above average. **IQ-type scores** use M=100, SD=15: a score of 115 is one SD above average, the 84th percentile. **Stanines** use M=5, SD=2 with integer values 1-9. All of these carry identical information — they are the same z-score expressed in a different skin. A T-score of 70, an IQ-type score of 130, and a z-score of +2.00 are three ways of saying the same thing about a person's standing.

The critical practical skill is moving fluently between scales. If a student's cognitive assessment yields an IQ-type score of 130, you can immediately compute: z = (130−100)/15 = +2.00, which corresponds to the 97.7th percentile, and a T-score of 50 + (2.00 × 10) = 70. This fluency matters in clinical and educational contexts where different instruments report on different standard score scales. **Profile analysis** — comparing a student's scores across verbal, spatial, and processing speed domains — is one of the most common applications: without a shared scale, a raw score of 40 on one test and 75 on another is uninterpretable. Expressed as T-scores or IQ-type scores, the comparison becomes immediate.
