---
id: intelligence-test-interpretation
title: 'Intelligence Testing: Score Interpretation and Profile Analysis'
domain: psychology
course: psychometrics
prerequisites:
- id: intelligence-test-construction
  type: hard
- id: structural-equation-modeling-measurement
  type: soft
- id: standard-scores-transformations
  type: soft
- id: normal-distribution
  type: soft
tags:
- iq-testing
- cognitive-ability
- profile-analysis
- clinical-interpretation
- subtest-analysis
stage: expert
status: draft
---

# Intelligence Testing: Score Interpretation and Profile Analysis

## Core Idea
Intelligence tests (Wechsler scales, Stanford-Binet, etc.) yield overall composite scores and subtest profiles measuring constructs like verbal comprehension, working memory, processing speed, and perceptual reasoning. Sound interpretation requires understanding the construct measured by each subtest, identifying meaningful intra-individual differences in strength/weakness, evaluating the clinical significance of score differences, and avoiding over-pathologizing small variations. Context including effort, motivation, and cultural factors must be considered.

## How It's Best Learned
Score actual intelligence tests and compute composite scores, index scores, and subtest analyses. Practice identifying scatter patterns that are statistically significant and clinically meaningful. Compare profiles across different ability levels to understand how pathological patterns differ from normal variation.

## Questions

```yaml
- question: "A practitioner administering a Wechsler instrument notices a 7-point difference between a child's Verbal Comprehension and Working Memory index scores. What is the most appropriate interpretation?"
  type: multiple-choice
  options:
    - "It indicates a clinically significant strength in verbal comprehension relative to working memory"
    - "It likely falls within measurement error and should not be interpreted as a meaningful cognitive difference"
    - "It confirms a language-based processing advantage that should be reported as a clinical finding"
    - "The Full Scale IQ should be discarded since the index scores differ"
  answer: 1
  explanation: "Subtests and index scores have imperfect reliability, so any two scores from the same battery will differ somewhat by chance. A 7-point difference typically falls within normal measurement error for Wechsler instruments. Clinicians use pre-calculated tables of reliable change differences — derived from each instrument's reliability coefficients — to determine whether an observed discrepancy exceeds chance variation at a given confidence level. Over-interpreting small differences is one of the most common interpretation errors and leads to false diagnoses."

- question: "A child from an under-resourced educational environment scores 22 points lower on Verbal Comprehension than on Fluid Reasoning. A competent interpreter should consider which explanation first?"
  type: multiple-choice
  options:
    - "A specific language-based learning disability is present and should be diagnosed"
    - "Fluid Reasoning is not a valid construct for this population"
    - "The discrepancy likely reflects differential educational opportunity and cultural loading rather than a clinical deficit"
    - "The Full Scale IQ average of the two scores is what matters, not the index discrepancy"
  answer: 2
  explanation: "Cultural loading varies systematically by subtest: vocabulary and general knowledge items are highly sensitive to cultural and educational opportunity, while fluid reasoning items are somewhat less so. A large verbal-fluid discrepancy in a child from an under-resourced background may simply reflect that schooling has developed certain verbal skills less thoroughly — not a neurological deficit. Context is integral to interpretation; the score must be read against the full background of the child's history and circumstances."

- question: "The Full Scale IQ is the most reliable score an intelligence battery produces because it aggregates across the broadest sample of cognitive operations, increasing its stability compared to individual subtests."
  type: true-false
  answer: true
  explanation: "Reliability increases with test length — more items sampling more operations averages out item-level noise. The FSIQ or equivalent composite is therefore more stable across repeated testings and more predictive of real-world outcomes than any individual subtest or index score. When nothing else about a profile can be confidently interpreted, the composite is the most defensible anchor."

- question: "When a client's test score contradicts extensive behavioral observations and functional evidence from real-world settings, a competent interpreter should trust the test score as the more objective measure."
  type: true-false
  answer: false
  explanation: "Context and ecological validity are integral to interpretation, not supplementary caveats. A score reflects performance on one occasion under specific conditions. A client who is anxious, sleep-deprived, or from a cultural background that values caution over speed may produce scores that do not reflect maximum ability. A score that contradicts everything known about how a person actually functions deserves scrutiny, not blind acceptance. Test scores and broader contextual evidence must be interpreted together."

- question: "Why is the Full Scale IQ more useful as an interpretive anchor than individual subtest scores, and when should a practitioner look beyond it to index or subtest profiles?"
  type: short-answer
  answer: "The FSIQ is more reliable because it aggregates across a broader sample of cognitive operations, averaging out the measurement error inherent in any individual subtest. It is also the most predictive of real-world outcomes. However, FSIQ aggregation can mask clinically significant variability: a child with strong verbal abilities but severely impaired processing speed may have an average FSIQ that obscures a specific learning profile with real educational implications. Index and subtest profiles become informative when discrepancies exceed statistical noise thresholds — verified against reliable change tables — and are consistent with the client's functional presentation outside the test room."
  explanation: "This captures the core clinical tension: the composite is most defensible statistically but potentially least informative clinically. Profile analysis is powerful precisely when the composite-level interpretation would mislead treatment planning."
```

## Explainer

From intelligence test construction, you know how subtests are designed to load on latent factors, how items are calibrated, and how composite scores are derived by aggregating across component subscales. Score interpretation is the applied downstream skill: given an actual test profile, what does it tell you about this individual's cognitive abilities, and what are the limits of those inferences? The answer requires combining your understanding of standard scores, normal distributions, and the reliability principles that determine when observed differences are real.

Start with what you know about standard scores. Intelligence tests are designed to produce scores with mean 100 and standard deviation 15 on most major instruments (Wechsler, Stanford-Binet). A score of 115 is roughly the 84th percentile; 130 is roughly the 98th percentile; 70 is roughly the 2nd percentile. The **Full Scale IQ** or equivalent composite is the most statistically reliable number the test produces, because it aggregates across the broadest sampling of cognitive operations — reliability increases with test length. This means the composite is more stable across repeated testings and more predictive of real-world outcomes than any individual subtest. When nothing else about a score report can be trusted, the composite is the most defensible anchor.

More clinically interesting — and more easily misused — is information at the **index score** and **subtest** levels. Modern Wechsler instruments yield separate index scores for constructs like Verbal Comprehension, Fluid Reasoning, Working Memory, and Processing Speed, each reflecting a meaningfully distinct cognitive process with different neurological substrates and different real-world correlates. **Profile analysis** — examining the pattern of strengths and weaknesses across index scores — is how practitioners identify specific learning disabilities (e.g., strong verbal comprehension but severely depressed processing speed), characterize the profile of a traumatic brain injury, or distinguish general intellectual disability from focal deficits.

The critical skill separating competent from incompetent interpretation is knowing when a score difference is **clinically meaningful** versus **statistical noise**. Because subtests have imperfect reliability, any two scores from the same battery will differ somewhat by chance. A 5-point index score difference is usually within measurement error; a 20-point difference almost certainly reflects a real underlying pattern. Practitioners use tables of **reliable change differences** — pre-calculated from each instrument's reliability coefficients — to determine whether an observed discrepancy exceeds chance variation at a given confidence level. Over-interpreting small differences leads to false diagnoses; under-interpreting large ones misses genuine cognitive profiles that have treatment implications.

Context is not a footnote — it is integral to interpretation. Test scores reflect performance on one occasion, under specific conditions, with a specific examiner. A child who is anxious, sleep-deprived, from a cultural background that values caution over speed, or who has had differential schooling in the tested domains will produce scores that do not reflect maximum ability. **Cultural loading** varies systematically by subtest: vocabulary and general knowledge items are highly sensitive to cultural and educational opportunity; spatial reasoning and processing speed items are somewhat less so. A competent interpreter holds the profile against the full context — behavioral observations during testing, history, ecological validity — and asks whether the pattern is internally consistent and consistent with the client's functioning outside the test room. A score that contradicts everything known about how a person actually operates in the world deserves scrutiny, not blind acceptance.
