---
id: convergent-discriminant-validity
title: 'Convergent and Discriminant Validity: Multitrait Analysis'
domain: psychology
course: psychometrics
prerequisites:
- id: construct-validity-multitrait
  type: hard
- id: factor-analysis-measurement
  type: soft
builds-toward:
- confirmatory-factor-analysis
tags:
- construct-validity
- convergent
- discriminant
- measurement-model
stage: expert
status: validated
---

# Convergent and Discriminant Validity: Multitrait Analysis

## Core Idea
Convergent validity demonstrates that measures of the same construct correlate substantially with each other. Discriminant validity shows that measures of theoretically distinct constructs do not highly correlate. Together, they establish the distinctiveness and appropriateness of a construct's conceptualization.

## Questions

```yaml
- question: "A researcher develops a new measure of 'resilience' and finds it correlates r = .78 with established resilience scales, but also correlates r = .74 with measures of optimism, r = .71 with extraversion, and r = .69 with self-efficacy. What validity problem does this pattern reveal?"
  type: multiple-choice
  options:
    - "Poor convergent validity — the new measure does not correlate strongly enough with established resilience scales"
    - "Poor discriminant validity — the measure fails to distinguish resilience from conceptually distinct constructs"
    - "Poor face validity — the items do not look like they measure resilience"
    - "Poor test-retest reliability — correlations with other measures will change over time"
  answer: 1
  explanation: "The pattern shows strong convergent validity (high correlation with similar constructs) but poor discriminant validity. If resilience is supposed to be a distinct construct from optimism and extraversion, those correlations should be substantially lower than the convergent ones. When a measure correlates nearly equally with theoretically distinct constructs, it may be measuring something broad like general positive affect or social desirability — or the construct boundaries are poorly defined. Convergent evidence alone is not sufficient; you need the pattern of correlations to be selectively high for related measures and lower for unrelated ones."

- question: "What is the primary purpose of the multitrait-multimethod (MTMM) matrix in establishing construct validity?"
  type: multiple-choice
  options:
    - "To test whether a measure has high internal consistency across its items"
    - "To simultaneously assess convergent and discriminant validity across multiple constructs measured by multiple methods, separating construct variance from method variance"
    - "To identify which factor structure best describes the items in a psychological scale"
    - "To compare the predictive validity of two different measures against the same external criterion"
  answer: 1
  explanation: "The MTMM matrix, developed by Campbell and Fiske, measures multiple constructs using multiple methods (e.g., self-report, observer rating, physiological measure). This design allows you to check whether high correlations reflect shared construct (good convergent validity) or merely shared method (two self-report measures inflating each other through method variance). Discriminant validity is supported when measures of different constructs using the same method correlate less than measures of the same construct using different methods. Internal consistency, factor analysis, and predictive validity are separate forms of validity evidence."

- question: "A new anxiety scale that correlates r = .82 with an established anxiety measure has demonstrated sufficient construct validity to use in research."
  type: true-false
  answer: false
  explanation: "High convergent validity is necessary but not sufficient for construct validity. Demonstrating that the new scale correlates with an existing anxiety measure shows it measures something similar — but without discriminant validity evidence, we cannot rule out that it is simply measuring general distress, negative affect, or neuroticism. A measure that correlates equally with anxiety, depression, and worry scales has strong convergent but poor discriminant validity, undermining the claim that it specifically captures anxiety as a distinct construct. Both forms of evidence are required."

- question: "Method variance can inflate convergent validity correlations between two self-report measures even when the measures are designed to assess distinct psychological constructs."
  type: true-false
  answer: true
  explanation: "This is a core insight motivating the MTMM framework. Two self-report questionnaires share systematic response tendencies — acquiescence bias, social desirability, positive self-presentation — that inflate their intercorrelations regardless of construct content. If a 'resilience' scale and a 'well-being' scale are both self-report, they will correlate partly because of what they share as method, not purely because the constructs overlap. This is why using multiple methods (behavioral observation, physiological measures, informant report) is important: convergent validity across methods provides stronger evidence than convergence within a single method."

- question: "Why is it problematic if a psychological measure correlates just as highly with theoretically unrelated constructs as it does with the construct it is supposed to measure?"
  type: short-answer
  answer: "If a measure correlates equally with related and unrelated constructs, it fails to demonstrate discriminant validity — meaning it cannot distinguish between distinct psychological entities. This suggests the measure is capturing something broad (e.g., general distress, response bias) rather than the specific construct it claims to assess. Without discriminant evidence, the construct itself is empirically undefined: if 'resilience' predicts everything equally well, it is not a specific, distinct psychological reality but merely a label for a diffuse pattern."
  explanation: "This question targets the logical structure of construct validation: a construct is meaningful only insofar as it is distinguishable from other constructs. Convergent validity shows that a construct is real; discriminant validity shows that it is distinct. A measure that converges with everything proves that something is being measured but not what. The scientific value of a construct depends on its discriminant boundary being as real and empirically supported as its convergent core."
```

## Explainer

From your work with construct validity and factor analysis, you know that a psychological construct like "anxiety" or "conscientiousness" is a theoretical entity — it does not exist in the world the way weight or temperature do. To argue that a test actually measures the construct it claims to measure, you need a body of evidence showing how scores relate to other measures. Convergent and discriminant validity are the two sides of that evidence: one shows that your measure *agrees* with other measures of the same thing; the other shows that it *disagrees* with measures of different things. You need both.

**Convergent validity** is demonstrated when scores on your measure correlate substantially with scores on other instruments that are theoretically supposed to tap the same construct. If you have developed a new measure of depression, it should correlate strongly with the Beck Depression Inventory and the PHQ-9. If it does not, one of two things is wrong: either your measure isn't capturing depression, or the existing measures aren't either. High convergent correlations provide evidence that multiple independent operationalizations are converging on the same underlying reality. The logic is triangulation — if different methods (self-report, behavioral observation, physiological measure) all point to the same construct, confidence grows that the construct is real and that each measure is capturing it.

**Discriminant validity** is demonstrated when your measure does *not* correlate highly with measures of theoretically distinct constructs. Your depression measure should correlate moderately with anxiety (the constructs are related but distinct) but should not correlate as highly with extraversion or intelligence. If two supposedly distinct constructs correlate near 1.0, they are empirically indistinguishable — which means either the constructs are the same thing, or the measures are so blunt that they cannot separate them. Discriminant validity failures often reveal **method variance**: two self-report measures will correlate partly because they share the method, not because they share a construct. This is why Campbell and Fiske's **multitrait-multimethod matrix** (MTMM) — which your factor analysis background prepares you to interpret — examines convergent and discriminant patterns across multiple constructs measured by multiple methods simultaneously.

The practical implication is that both forms of validity evidence are necessary and neither is sufficient alone. A measure that converges with everything (including unrelated constructs) demonstrates only that it captures something broad, perhaps acquiescence or social desirability. A measure that discriminates sharply from everything (including theoretically related constructs) may be too narrow or poorly operationalized. The sweet spot — strong convergence with the same construct, modest correlation with related constructs, and low correlation with unrelated ones — is what distinguishes a well-validated instrument from one that merely looks face-valid.
