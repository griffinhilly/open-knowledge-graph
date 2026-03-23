---
id: measurement-validity-evidence
title: 'Measurement Validity: Construct and Criterion Evidence'
domain: psychology
course: research-methods-psychology
prerequisites:
- id: variable-definition-and-operational-measurement
  type: hard
- id: measurement-reliability-estimation
  type: soft
builds-toward:
- internal-validity-confounds-and-control
tags:
- validity
- construct-validity
- criterion-validity
- measurement-evidence
stage: formal-systems
status: validated
---

# Measurement Validity: Construct and Criterion Evidence

## Core Idea
Construct validity asks: Does the measure assess the intended construct? Evidence comes from content validity, convergent validity (correlates with related measures), discriminant validity (uncorrelated with unrelated measures), and factor structure. Criterion validity asks: Does the measure predict relevant outcomes? Both are integral to score interpretation and use.

## How It's Best Learned
Review validation studies for a psychological measure, extracting evidence of construct and criterion validity. Compare a measure with high internal consistency but low validity to understand that reliability ≠ validity. Practice evaluating whether a measure is valid for a new use.

## Common Misconceptions
- Validity is inherent to a test; - Validity is determined by a single correlate; - High internal consistency ensures validity; - Validity is about group means, not individual scores.

## Questions

```yaml
- question: "A researcher develops a new anxiety scale with Cronbach's α = 0.94, indicating very high internal consistency. They conclude the scale must be highly valid. What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Cronbach's α of 0.94 is too high — values above 0.90 indicate item redundancy, not validity"
    - "Reliability and validity are independent properties — a measure can be highly consistent while systematically measuring the wrong construct or measuring it only in specific populations"
    - "Internal consistency does provide evidence of validity, so the conclusion is correct"
    - "Validity requires test-retest reliability, not internal consistency"
  answer: 1
  explanation: "Reliability and validity are distinct. A scale can have high internal consistency (items correlate with each other) while measuring something other than the intended construct — or measuring the right construct only in the population it was developed in. The classic example: a bathroom scale that reads 10 lbs too heavy is perfectly consistent but systematically invalid. High Cronbach's α is necessary but not sufficient for validity; convergent, discriminant, and criterion evidence are also required."

- question: "A depression scale with strong validity evidence in adult U.S. clinical samples is to be administered to adolescents in East Africa. Which statement best reflects the validity concern?"
  type: multiple-choice
  options:
    - "The scale is valid because its psychometric properties were rigorously established in the original context"
    - "Validity is inherent to the test items, not the population, so the context change is irrelevant"
    - "Validity evidence from one population and context does not automatically transfer; new evidence must be gathered for the new use or the inferential gap must be acknowledged"
    - "The scale should be completely redeveloped from scratch for any new cultural context"
  answer: 2
  explanation: "This is the central practical implication of the validity-as-use-specific principle. Validity evidence is not a permanent property of the test — it is evidence for specific interpretations of specific score uses in specific populations. Cultural context affects item interpretation, construct meaning, and criterion relationships. Option D overstates the requirement: cross-cultural adaptation and validation studies are possible without full redevelopment. But using the test without any additional validation is an inferential leap the evidence doesn't support."

- question: "A measure can be highly reliable — producing consistent scores across administrations — while having poor validity for its intended purpose."
  type: true-false
  answer: true
  explanation: "Reliability is a necessary but not sufficient condition for validity. A measure can consistently assess something real, just not the thing it's supposed to measure. A test that reliably measures vocabulary knowledge might be consistently administered as an 'intelligence test' while having poor construct validity for intelligence. Reliability sets an upper bound on validity (an unreliable measure cannot be valid), but high reliability doesn't guarantee high validity."

- question: "A single study showing that a new personality measure correlates r = 0.75 with an established gold-standard measure is sufficient to establish the new measure's validity."
  type: true-false
  answer: false
  explanation: "Validity is cumulative and argument-based — it is assembled through multiple lines of evidence over time, not established in a single study. A high convergent validity coefficient is one piece of evidence, but you also need discriminant validity (the measure doesn't correlate too strongly with unrelated constructs), content coverage, criterion validity (it predicts relevant real-world outcomes), and evidence that the validation generalizes to the populations and uses intended. No single coefficient 'validates' a measure."

- question: "Why is the statement 'this test is valid' technically imprecise, and how should validity claims be framed instead?"
  type: short-answer
  answer: "Validity is not a fixed property of the test — it is a property of the interpretations and uses made from test scores in specific contexts. The same test can have strong validity evidence for one purpose (screening clinical adults for major depression) and weak or absent evidence for another (assessing adolescent depression across cultural contexts). A precise validity claim specifies: the score interpretation, the construct being measured, the population, and the purpose. For example: 'The interpretation of PHQ-9 scores as indicating depressive symptom severity in adult primary care patients in the U.S. has strong validity evidence across multiple populations and criterion outcomes.'"
  explanation: "This framing matters practically: when a test is used for high-stakes decisions (clinical diagnosis, employment, educational placement) in a population it was not validated for, the validity evidence does not transfer automatically. The user bears responsibility for ensuring adequate validity evidence exists for their specific use case."
```

## Explainer

Validity is often summarized as "does the test measure what it claims to measure?" but this framing obscures something important: validity is not a property of a test in isolation. It is a property of the **interpretations and uses** made from test scores. A depression measure might have strong validity evidence in clinical adult populations but poor validity when used with adolescents or in non-Western cultural contexts. From your study of reliability, you know that a measure can be highly consistent without measuring anything meaningful — a bathroom scale that consistently reads 10 pounds too heavy is reliable but systematically invalid.

**Construct validity** is the umbrella concept. It asks: does the pattern of relationships this measure forms with other variables make sense given our theoretical understanding of the construct? Evidence accumulates through multiple lines. **Content validity** evaluates whether the items cover the theoretical domain adequately — a math anxiety scale that only asks about algebra anxiety has poor content coverage if the construct is meant to encompass all mathematical domains. **Convergent validity** asks whether the measure correlates with other measures of the same or similar constructs; a new depression scale should correlate strongly with the BDI and PHQ-9. **Discriminant validity** (sometimes called divergent validity) asks the opposite: the measure should *not* correlate strongly with theoretically unrelated constructs. A depression scale with a .80 correlation with an anxiety scale raises questions about whether the two constructs are actually distinct.

**Criterion validity** is a separate but related question: does the measure predict relevant real-world outcomes? **Concurrent validity** examines correlation with a gold-standard criterion measured at the same time — does a new brief cognitive screening tool correlate with a full neuropsychological battery administered simultaneously? **Predictive validity** examines whether the measure predicts future outcomes — does a pre-employment personality scale predict actual job performance one year later? The distinction matters practically: a measure can have strong construct validity but weak predictive validity if the construct itself doesn't strongly cause the outcome you care about.

The unifying framework from contemporary psychometrics is that validity evidence is cumulative and argument-based. No single study "validates" a measure; rather, validation is an ongoing process of assembling a coherent **validity argument** — a chain of claims from test scores to interpretations to uses, with evidence supporting each link. When validity evidence is missing for a specific use case (a new population, a new purpose, a new context), the burden falls on the test user to either generate that evidence or acknowledge the inferential gap. This is why the phrase "this test is valid" is technically imprecise — the proper phrasing is always "the interpretation of these scores as measuring X in this population for this purpose has strong/weak validity evidence."
