---
id: validity-in-measurement
title: Validity in Psychological Measurement
domain: psychology
course: research-methods-psychology
prerequisites:
- id: reliability-in-measurement
  type: hard
- id: confounding-variables
  type: soft
- id: correlation-coefficient
  type: soft
- id: blinding-in-experiments
  type: soft
- id: case-study-method
  type: soft
- id: survey-research-methods
  type: soft
builds-toward:
- inferential-statistics-psychology
- replication-and-open-science
tags:
- validity
- construct-validity
- internal-validity
- external-validity
- ecological-validity
stage: formal-systems
status: validated
---
# Validity in Psychological Measurement

## Core Idea
Validity is the degree to which a measure or study captures what it intends to. Construct validity asks whether an instrument measures the theoretical construct of interest (assessed via convergent and discriminant validity). Internal validity concerns whether causal inferences within a study are justified. External validity (generalizability) concerns whether findings apply beyond the study context. These different types of validity can conflict — maximizing control for internal validity can reduce ecological validity.

## How It's Best Learned
Evaluate a published psychological measure for construct validity by examining what it correlates with (convergent) and what it doesn't (discriminant). Then discuss whether lab findings would replicate in field settings.

## Common Misconceptions
- A valid test is not necessarily fair across all cultural or demographic groups — measurement invariance must be separately established.
- High external validity requires more than a diverse sample; the setting, procedure, and stimuli must also reflect the real-world situation of interest.

## Questions

```yaml
- question: "A new social anxiety scale correlates strongly with clinician ratings of anxiety (r = .72) and weakly with IQ scores (r = .08). This pattern primarily supports which type of validity?"
  type: multiple-choice
  options: ["Internal validity", "External validity", "Construct validity", "Ecological validity"]
  answer: 2
  explanation: "Construct validity is supported by convergent evidence (strong correlation with a related measure — clinician ratings) and discriminant evidence (weak correlation with an unrelated construct — IQ). Internal validity concerns causal inference within a study, and external validity concerns generalizability — neither is assessed by correlational patterns of the measure itself."

- question: "A psychological test demonstrated to be valid for a U.S. college student sample is automatically valid for use with adults in other cultural contexts."
  type: true-false
  answer: false
  explanation: "Validity is not a fixed property of a test — it must be established for each population and context. Measurement invariance (whether the same items measure the same construct across groups) must be tested separately. A scale measuring 'depression' through Western symptom expressions may not capture equivalent constructs in cultures with different idioms of distress."

- question: "Describe the core tradeoff between internal validity and external validity in psychological research."
  type: short-answer
  answer: "Maximizing internal validity (e.g., tight lab controls, random assignment) often strips away the real-world complexity that determines whether findings generalize, reducing external validity. Conversely, naturalistic designs with high ecological realism sacrifice control, making causal inference harder."
  explanation: "A highly controlled lab experiment can definitively establish that X causes Y under those conditions, but those conditions may not match real-world settings. Field studies preserve ecological validity but cannot rule out confounds. Researchers must balance these tradeoffs based on their questions — and ideally replicate findings across both designs."
```

## Explainer

You have already learned about reliability — whether a measure produces consistent results. Validity is the next and deeper question: is the measure actually capturing what we think it is? A bathroom scale is reliable if it gives the same reading each time, but if it's miscalibrated by five kilograms, it's reliable but not valid. In psychology, the gap between "what we measured" and "what we meant to measure" is often the central methodological problem.

Construct validity is typically what researchers mean when they ask whether an instrument is valid. A psychological construct — like "working memory capacity" or "self-esteem" — is a theoretical entity we can't observe directly. We operationalize it as a set of test items or tasks, then ask whether those items track the construct faithfully. Convergent validity provides positive evidence: the instrument should correlate with other accepted measures of the same construct. Discriminant validity provides negative evidence: it should not correlate strongly with measures of different constructs. Both patterns together support the inference that the instrument is measuring the construct of interest.

Internal validity asks a different question: within a study, do the results support the causal claim? If participants who received the intervention improved more than controls, could that difference be explained by confounds (systematic differences between groups) or by the independent variable? Strong internal validity comes from random assignment, control groups, and careful experimental design. This is why reliability (from your prerequisite) matters here — an unreliable measure adds noise that makes causal detection harder.

External validity — generalizability — is often sacrificed when researchers optimize for internal validity. A tightly controlled lab paradigm that eliminates every confound may produce a real causal finding that nonetheless doesn't occur in natural settings. This tradeoff is not a flaw; it reflects the fact that different study designs answer different questions. A lab experiment establishes that an effect can happen; a field study tests whether it does happen in the wild. The two together are more powerful than either alone.

The critical insight about validity that surprises most students is that it is not a fixed property of a test but a property of a test used with a specific population for a specific purpose. A depression scale validated on U.S. adults is not automatically valid for adolescents or adults in other cultures. Measurement invariance — whether the factor structure and item relationships hold across groups — must be empirically demonstrated. This is why "the test was published and validated" does not settle questions about appropriate use; it only begins them.
