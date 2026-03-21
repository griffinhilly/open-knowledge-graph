---
id: construct-validity-and-measurement
title: Construct Validity and Measurement Validity
domain: psychology
course: research-methods-psychology
prerequisites:
- id: construct-definition-and-measurement
  type: hard
- id: validity-in-measurement
  type: soft
builds-toward:
- external-validity-generalization
tags:
- validity
- measurement
- constructs
stage: formal-systems
status: draft
---

# Construct Validity and Measurement Validity

## Core Idea
Construct validity addresses whether your measures and manipulations actually represent the constructs you intend to study. A measure with poor construct validity may correlate with your outcomes due to method variance, item ambiguity, or shared confounds rather than the intended construct. Establishing construct validity requires convergent evidence (correlating with other indicators of the same construct) and discriminant evidence (not over-correlating with different constructs).

## How It's Best Learned
Create a multitrait-multimethod matrix comparing your measure with alternative measures of the same construct and measures of related but distinct constructs. Conduct confirmatory factor analysis to verify dimensional structure. Analyze whether your effects replicate with different operationalizations and measures.

## Common Misconceptions
- High internal consistency (Cronbach's alpha) ensures construct validity; internal consistency measures homogeneity, not construct validity.
- Validity evidence is general and permanent; validity is specific to populations, contexts, and uses—evidence must be accumulated across studies.
- A single validation study establishes validity; construct validity is an ongoing process accumulating evidence across multiple studies with different samples.

## Questions

```yaml
- question: "A researcher develops a new 'grit' scale with Cronbach's alpha of .92 and concludes it has strong construct validity. What is the critical flaw in this reasoning?"
  type: multiple-choice
  options:
    - "High alpha indicates the items are homogeneous, but the shared dimension they measure might be conscientiousness or general self-efficacy rather than grit"
    - "Alpha above .90 is excessively high and indicates the items are too redundant to be useful"
    - "Construct validity applies only to experimental manipulations, not self-report scales"
    - "High alpha directly proves discriminant validity from related traits like perseverance"
  answer: 0
  explanation: "Cronbach's alpha measures internal consistency — how much the items correlate with each other — not what they are measuring. A scale measuring 'the tendency to agree with any negative statement' could have alpha of .95 and still not measure grit. Construct validity requires evidence that the measure captures the intended construct and not something else. That requires convergent validity (does it correlate with other grit indicators?) and discriminant validity (does it fail to over-correlate with conscientiousness, self-efficacy, and other distinct constructs?)."

- question: "A new depression scale correlates r = .78 with two existing depression measures, but also correlates r = .74 with anxiety scales and r = .71 with neuroticism scales. This pattern suggests:"
  type: multiple-choice
  options:
    - "Strong construct validity, because the depression correlations are slightly higher than the anxiety and neuroticism correlations"
    - "Weak convergent validity, since correlations with existing depression measures should exceed .90"
    - "Weak discriminant validity — the scale likely measures general negative affect rather than depression specifically"
    - "Strong construct validity, because correlating with related constructs is expected and desirable"
  answer: 2
  explanation: "In the Campbell-Fiske framework, valid measurement requires that same-trait correlations (convergent validity) substantially exceed different-trait correlations (discriminant validity). Here, the depression correlations (.78) are barely higher than anxiety (.74) and neuroticism (.71) correlations — the measure cannot discriminate depression from related negative-affect constructs. This is the classic signature of poor discriminant validity: the scale is probably measuring a broader dimension like general negative affect, not depression specifically."

- question: "Method variance can inflate correlations between psychological constructs when all measures are collected using the same method — for example, all self-report Likert scales administered in the same session."
  type: true-false
  answer: true
  explanation: "When multiple constructs are all measured via self-report in a single session, their intercorrelations are inflated by shared variance that belongs to the measurement method rather than the constructs themselves. Sources include acquiescence bias, extreme response tendencies, and momentary mood affecting all ratings simultaneously. This is why the multitrait-multimethod approach — using behavioral observation, physiological measures, or informant ratings alongside self-report — is the gold standard for establishing construct validity."

- question: "A measure that has been validated on a college student sample can generally be considered valid for use with clinical populations, because the statistical relationships between constructs should hold across groups."
  type: true-false
  answer: false
  explanation: "Validity is specific to populations, contexts, and uses — not general or permanent. A construct like 'depression' may have different manifestations, different factor structures, or different relationships to criterion variables in clinical populations compared to undergraduates. Validity generalization — whether evidence from one context transfers to another — is itself an empirical question. Calling a measure 'validated' without specifying for whom and for what purpose is misleading."

- question: "Why isn't it enough to show that a new anxiety measure has high internal consistency and correlates well with other anxiety measures? What additional evidence is needed, and why?"
  type: short-answer
  answer: "High internal consistency and convergent validity (correlating with other anxiety measures) are necessary but not sufficient. Discriminant validity evidence is also required: the scale must not over-correlate with distinct constructs like depression, neuroticism, or general negative affect. Without discriminant evidence, you cannot rule out that the measure captures a broader shared dimension rather than anxiety specifically. Construct validity requires triangulating the construct from multiple directions — what the measure relates to AND what it does not relate to."
  explanation: "A measure that correlates equally with anxiety, depression, and neuroticism probably isn't measuring any of them specifically. The multitrait-multimethod logic requires both convergent validity (high correlations with other indicators of the same construct) and discriminant validity (lower correlations with different constructs). Only when both patterns are present can you be confident the measure is operationalizing the intended construct and not a broader, theoretically uninteresting dimension."
```

## Explainer

From your earlier work on construct definition, you know that a psychological construct — anxiety, working memory, self-efficacy — is an unobservable theoretical entity that must be made measurable through **operationalization**: choosing or designing indicators that stand in for it. Construct validity is the question that follows naturally: does your operationalization actually capture the construct, or does it capture something else? A scale purporting to measure "depression" might actually be measuring response fatigue, social desirability, or the tendency to endorse any negative statement. The construct validity problem is real whenever you cannot directly observe what you claim to measure — which in psychology is almost always.

The classic framework for evaluating construct validity uses two complementary types of evidence. **Convergent validity** asks whether your measure correlates substantially with other indicators of the same construct: does your new anxiety scale correlate with existing anxiety measures, with observer-rated anxiety, with physiological stress markers? If it doesn't correlate with any of these, it is probably not measuring anxiety. **Discriminant validity** asks the complementary question: does your measure *not* over-correlate with measures of different constructs? If your anxiety scale correlates just as strongly with depression measures as with other anxiety measures, you may be measuring general negative affect or neuroticism rather than anxiety specifically. Campbell and Fiske's **multitrait-multimethod matrix** formalizes both tests: you measure multiple traits using multiple methods and examine the pattern of correlations. Valid measurement produces high same-trait/different-method correlations (convergent) and low different-trait/same-method correlations (discriminant).

**Method variance** is the construct validity threat most often overlooked by beginning researchers. If you measure self-esteem, depression, and loneliness all with self-report Likert scales administered in the same session, their intercorrelations will be inflated by shared method — the systematic tendency for people to be more or less acquiescent, more or less extreme in their responses, more or less influenced by mood at the moment of testing. None of this variance belongs to the constructs; it belongs to the measurement method. The solution is to vary methods across constructs: use behavioral observation, physiological measures, or informant ratings alongside self-report. When a correlation holds across methods, you can be more confident it reflects the constructs rather than the measurement apparatus.

Because construct validity is established by evidence accumulated across multiple studies, it is a property that can erode or improve over time. A measure validated on college students in the 1980s may have poor construct validity with clinical populations, older adults, or non-Western samples where the construct has different meanings or manifestations. **Validity generalization** — asking whether validity evidence from one context transfers to another — is itself a research question, not an assumption. This is why calling a measure "validated" without specifying for whom and for what purpose is misleading. Validity is always validity for a particular interpretation, in a particular population, for a particular use.
