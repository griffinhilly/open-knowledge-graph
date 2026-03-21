---
id: construct-validity-multitrait
title: Construct Validity and Convergent-Discriminant Evidence
domain: psychology
course: psychometrics
prerequisites:
- id: reliability-validity-relationship
  type: hard
- id: validity-in-measurement
  type: soft
builds-toward:
- confirmatory-factor-analysis
- validity-evidence-frameworks
tags:
- construct-validity
- convergent-validity
- discriminant-validity
stage: advanced
status: draft
---

# Construct Validity and Convergent-Discriminant Evidence

## Core Idea
Construct validity examines whether a test truly measures the psychological construct it purports to measure. Multitrait-multimethod matrices provide evidence by showing correlations between different measures of the same construct (convergent) and low correlations with measures of different constructs (discriminant).

## Questions

```yaml
- question: "A researcher measures anxiety and depression using self-report and behavioral observation. Self-report anxiety correlates r = .72 with behavioral anxiety (convergent). But self-report anxiety also correlates r = .88 with self-report depression. What does this pattern most likely indicate?"
  type: multiple-choice
  options:
    - "Excellent construct validity — high convergent evidence is the most important criterion"
    - "Poor convergent validity — the cross-method correlation for anxiety should be higher than .72"
    - "Poor discriminant validity — self-report method variance inflates same-method correlations, suggesting the measures capture method effects as much as distinct constructs"
    - "The constructs of anxiety and depression are identical and should be merged into one scale"
  answer: 2
  explanation: "The r = .88 correlation between self-report anxiety and self-report depression is the red flag. If method variance (the shared response style from using the same format and instructions) drives correlations up to .88 between supposedly different constructs, the test is measuring 'how someone responds to self-report items' at least as much as it's measuring distinct psychological constructs. Good discriminant validity requires that same-method, different-trait correlations be substantially lower than different-method, same-trait correlations."

- question: "In a multitrait-multimethod matrix, which pattern provides the strongest evidence for construct validity?"
  type: multiple-choice
  options:
    - "High correlations throughout the entire matrix, showing all measures are capturing something real"
    - "High correlations between different methods measuring the same trait, AND low correlations between same-method measures of different traits"
    - "Low correlations throughout the matrix, showing each measure is uniquely specific"
    - "High correlations between measures from the same method, confirming measurement consistency"
  answer: 1
  explanation: "Construct validity in the MTMM framework requires two simultaneous patterns: convergent validity (same trait, different methods → high correlations) and discriminant validity (different traits, same method → lower correlations than same-trait cross-method correlations). High correlations everywhere (option A) would actually suggest method effects dominate. Low correlations everywhere (option C) would suggest no convergent validity. Only the specific pattern of option B satisfies both criteria simultaneously."

- question: "In MTMM analysis, if same-method correlations between different traits consistently exceed cross-method correlations for the same trait, this suggests that method variance is larger than trait variance — evidence against construct validity."
  type: true-false
  answer: true
  explanation: "This is the central diagnostic in MTMM analysis. If the shared measurement approach (same questionnaire format, same rater, same context) produces stronger correlations than the shared psychological construct, your instrument is measuring how people respond to the measurement method more than it's measuring the construct itself. Self-report measures of personality traits are particularly prone to this: social desirability, acquiescence, and response style systematically inflate same-method correlations regardless of what construct is being measured."

- question: "Demonstrating high convergent validity — that different methods measuring the same construct correlate strongly — is sufficient to establish construct validity."
  type: true-false
  answer: false
  explanation: "Convergent validity is necessary but not sufficient. Construct validity also requires discriminant validity: evidence that the measure does NOT correlate too highly with measures of different constructs. Without discriminant evidence, you cannot rule out the possibility that your 'anxiety' measure is really measuring general negative affect, distress, or neuroticism — constructs that would also converge with any other negatively valenced measure. Both halves of the MTMM logic — convergence and divergence — must be satisfied."

- question: "Why is multi-method measurement necessary for establishing construct validity, rather than simply demonstrating that different items on the same questionnaire correlate well with each other?"
  type: short-answer
  answer: "Items on the same questionnaire share method variance: the same format, instructions, response scale, and participant mindset. High inter-item correlations might reflect consistency in how a person responds to that type of item (social desirability, acquiescence bias) rather than convergence on the underlying construct. To separate trait variance from method variance, you need measures from genuinely different methodological approaches. Only when measures that differ completely in surface form (self-report vs. behavioral observation vs. physiological index) still converge on the same scores can you be confident they are tracking a psychological reality rather than a measurement artifact."
  explanation: "Campbell and Fiske's MTMM logic was specifically designed to solve this problem. The matrix structure forces you to compare same-method/different-trait correlations against different-method/same-trait correlations, making method effects visible. A single-method instrument, no matter how internally consistent, cannot provide this discriminant evidence — it has no way to distinguish 'trait variance' from 'method variance.'"
```

## Explainer

You already know from your study of validity that a test being reliable doesn't guarantee it measures what it claims to measure. **Construct validity** asks the deeper question: does the test actually capture the psychological reality it's supposed to represent? A test of "anxiety" might reliably produce scores, but if those scores reflect social desirability, attention, or willingness to self-disclose more than anxiety itself, the construct validity is poor. Establishing construct validity requires accumulating a body of evidence — and the **multitrait-multimethod (MTMM) matrix** is the most systematic approach to gathering that evidence simultaneously.

The MTMM framework, introduced by Campbell and Fiske (1959), rests on a simple but powerful design: measure multiple psychological traits using multiple different methods. For example, you might measure three traits — anxiety, depression, and hostility — using three methods: self-report questionnaire, peer rating, and behavioral observation. This gives you a 9×9 correlation matrix. Within this matrix, you can identify two critical patterns. **Convergent validity** is demonstrated when two different methods measuring the same trait correlate highly — a self-report anxiety score should correlate well with peer-rated anxiety, because both are trying to capture the same construct. If they don't, something is wrong: either the construct is method-bound, or the different methods are measuring different things.

**Discriminant validity** is demonstrated when measures of different traits, even using the same method, do not correlate too highly. Anxiety and depression should correlate somewhat (they often co-occur) but not so highly that the scores are interchangeable. If self-report anxiety and self-report depression correlate at .90, you haven't measured two distinct constructs — you've created two labels for the same score. The key logic is this: if method variance (the shared variance from using the same measurement approach) exceeds trait variance (the shared variance from measuring the same construct across methods), the instrument is measuring the measurement method more than it's measuring the construct.

In practice, MTMM analysis shows that both threats are real. Self-report measures of different personality traits often correlate too highly with each other simply because they share the same method — people who are defensive or socially desirable respond similarly to any self-report item, regardless of what construct it targets. The corrective implication is that strong construct validity evidence requires converging on a construct from multiple methodological angles. When a behavioral observation, a peer rating, and a physiological index all point in the same direction, confidence in the construct increases substantially. This multi-method logic underpins the entire enterprise of psychological construct validation.
