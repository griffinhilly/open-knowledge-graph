---
id: diagnostic-sensitivity-specificity
title: 'Diagnostic Test Properties: Sensitivity and Specificity'
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: screening-and-early-detection
  type: hard
- id: disease-frequency-measures
  type: soft
builds-toward:
- predictive-values-diagnostics
- receiver-operating-characteristic
- screening-test-evaluation
tags:
- diagnostic-accuracy
- test-characteristics
- sensitivity
- specificity
stage: expert
status: validated
---

# Diagnostic Test Properties: Sensitivity and Specificity

## Core Idea
Sensitivity (true positive rate) is the probability a test correctly identifies those with disease; specificity (true negative rate) is the probability it correctly identifies those without disease. Sensitivity and specificity are test properties determined by the cutoff used and do not depend on disease prevalence. Understanding both metrics is essential for selecting and evaluating diagnostic tests.

## Questions

```yaml
- question: "A blood test for disease X has 90% sensitivity and 85% specificity. The test is used in Clinic A (disease prevalence 5%) and Clinic B (disease prevalence 40%). Which of the following changes between the two settings?"
  type: multiple-choice
  options:
    - "Sensitivity — it will be lower at Clinic A because fewer true positives are available to detect"
    - "Specificity — it will be higher at Clinic A because there are more healthy people to correctly clear"
    - "Both sensitivity and specificity — both metrics depend on the composition of the patient population"
    - "Neither sensitivity nor specificity — both are fixed properties of the test; what changes is the predictive value of a positive or negative result"
  answer: 3
  explanation: "Sensitivity and specificity are calculated within each disease-status group: sensitivity = TP/(TP+FN) among those *with* disease; specificity = TN/(TN+FP) among those *without* disease. These calculations are independent of how many diseased vs. healthy people are in the tested population — they describe the test's behavior conditional on disease status. What changes dramatically with prevalence is the positive predictive value (PPV): in a low-prevalence setting, even a highly specific test will generate many false positives relative to true positives, because the pool of healthy people is so large. This is a critical distinction: sensitivity/specificity are test properties; predictive values are population-dependent."

- question: "A physician is designing a screening protocol for a rapidly progressing infection where missing a case could be life-threatening. Which test property should she prioritize, and why?"
  type: multiple-choice
  options:
    - "Specificity — she needs to avoid false positives to prevent unnecessary treatment"
    - "Sensitivity — she needs to minimize false negatives so that no true cases are missed (SnOUT: high sensitivity rules out disease when negative)"
    - "Neither — she should use the test with the highest overall accuracy regardless of the sensitivity/specificity tradeoff"
    - "Specificity — because high specificity means fewer people need follow-up testing"
  answer: 1
  explanation: "When missing a case (false negative) is the primary danger — as with a rapidly progressing, life-threatening infection — the physician should maximize sensitivity. A highly sensitive test rarely misses true cases: a negative result from a highly sensitive test is highly reassuring (SnOUT mnemonic: high Sensitivity, when Negative, rules Out disease). The cost of low sensitivity here is missed diagnoses; the cost of low specificity is false alarms requiring follow-up. When a false negative is more dangerous than a false positive, optimize for sensitivity. Conversely, when a false positive triggers a dangerous or expensive intervention, prioritize specificity (SpIN: high Specificity, when Positive, rules In disease)."

- question: "Lowering the diagnostic cutoff for a continuous test (e.g., reducing the blood glucose threshold for diabetes diagnosis) will increase sensitivity and decrease specificity."
  type: true-false
  answer: true
  explanation: "True. Lowering the threshold means more people test positive, including some who genuinely have the disease who would have been missed at the higher threshold (more true positives, fewer false negatives → higher sensitivity). But it also means more healthy people cross the threshold and test positive (more false positives → lower specificity). The reverse happens when the threshold is raised. This trade-off is inescapable and is visualized by the ROC curve: moving along the curve represents changing the cutoff, and every point on the curve represents a different sensitivity/specificity combination. There is no setting that simultaneously maximizes both."

- question: "A test with 95% sensitivity correctly classifies 95% of most patients tested — both those with and without the disease."
  type: true-false
  answer: false
  explanation: "False. Sensitivity = TP / (TP + FN) — it is calculated only among patients *who have the disease*. It says nothing about how the test performs on healthy patients. A test with 95% sensitivity correctly identifies 95% of sick patients but could have very poor specificity, misclassifying most healthy patients as positive. Confusing sensitivity with overall accuracy is the most common misinterpretation of this metric. Overall accuracy = (TP + TN) / total patients, which weights both sensitivity and specificity by the prevalence of disease in the tested population. Sensitivity and specificity describe performance within each disease-status group, independently of each other."

- question: "Why can't you maximize both sensitivity and specificity simultaneously, and what determines the optimal tradeoff in a clinical setting?"
  type: short-answer
  answer: "Sensitivity and specificity are in inherent tension because they are determined by the same diagnostic cutoff. Lowering the cutoff increases sensitivity (catches more true cases) but also increases false positives, lowering specificity. Raising the cutoff improves specificity (fewer false alarms) but causes more true cases to be missed, lowering sensitivity. The two metrics measure performance on different populations (sick vs. healthy), and any single threshold divides the measurement distribution in a way that affects both simultaneously but in opposite directions. The optimal tradeoff depends on the clinical context: specifically, the relative costs of false negatives (missed cases) and false positives (unnecessary follow-up, treatment, or patient anxiety). For dangerous conditions where missing a case is catastrophic, accept lower specificity to achieve high sensitivity. For conditions where false positives lead to harmful interventions, accept lower sensitivity to protect specificity."
  explanation: "The core insight is that sensitivity and specificity are not independently adjustable — they are two sides of the same cutoff decision. Understanding why they trade off requires seeing that any threshold creates a boundary between two overlapping distributions (test values in sick vs. healthy patients). Moving the boundary in one direction always helps one metric and hurts the other. The clinical judgment is not 'which is more important in general' but 'what are the consequences of each type of error in this specific situation?'"
```

## Explainer

From your study of screening and disease frequency, you understand that tests are used in populations where most people do not have the disease, and that the goal is to separate the sick from the well as efficiently as possible. The fundamental challenge is that no test is perfect: any threshold you set will misclassify some people. **Sensitivity** and **specificity** give you a precise language for describing exactly where and how a test makes those errors.

Picture a 2×2 table: rows represent test result (positive/negative), columns represent true disease status (present/absent). The four cells are **true positives** (TP: sick, test positive), **false negatives** (FN: sick, test negative), **false positives** (FP: healthy, test positive), and **true negatives** (TN: healthy, test negative). **Sensitivity** = TP / (TP + FN): among everyone who *has* the disease, what fraction does the test catch? **Specificity** = TN / (TN + FP): among everyone who *does not* have the disease, what fraction does the test correctly clear? Sensitivity answers "how good is this test at not missing disease?" Specificity answers "how good is this test at not crying wolf?"

The trade-off between sensitivity and specificity is determined by where you set the diagnostic cutoff. Consider a blood glucose test for diabetes: if you lower the threshold from 126 to 100 mg/dL, you will catch more diabetics (higher sensitivity) but you will also flag more healthy people as positive (lower specificity). Raise the threshold and you do the reverse. This trade-off is visualized by the **ROC curve** — a topic you will encounter next — which plots sensitivity against (1 − specificity) across all possible cutoffs. The area under the ROC curve summarizes the test's overall discriminating power, independent of any particular threshold.

The most important conceptual point is that sensitivity and specificity are **properties of the test and its cutoff**, not of the population being tested. They do not change when prevalence changes. What does change with prevalence is the **predictive value**: in a low-prevalence population, even a highly specific test will generate many false positives relative to true positives, because the denominator of healthy people is enormous. A useful mnemonic: **SnOUT** — a test with high *Sen*sitivity, when *Negative*, rules *Out* disease (few false negatives, so a negative is reassuring); **SpIN** — a test with high *Spec*ificity, when *Positive*, rules *In* disease (few false positives, so a positive is convincing). Choosing which property to maximize depends on the clinical stakes: for a disease where missing cases is catastrophic (e.g., HIV screening, TB, some cancers), prioritize sensitivity. For a test where a false positive triggers a dangerous or expensive follow-up procedure, prioritize specificity.
