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
stage: advanced
status: draft
---

# Diagnostic Test Properties: Sensitivity and Specificity

## Core Idea
Sensitivity (true positive rate) is the probability a test correctly identifies those with disease; specificity (true negative rate) is the probability it correctly identifies those without disease. Sensitivity and specificity are test properties determined by the cutoff used and do not depend on disease prevalence. Understanding both metrics is essential for selecting and evaluating diagnostic tests.

## Explainer

From your study of screening and disease frequency, you understand that tests are used in populations where most people do not have the disease, and that the goal is to separate the sick from the well as efficiently as possible. The fundamental challenge is that no test is perfect: any threshold you set will misclassify some people. **Sensitivity** and **specificity** give you a precise language for describing exactly where and how a test makes those errors.

Picture a 2×2 table: rows represent test result (positive/negative), columns represent true disease status (present/absent). The four cells are **true positives** (TP: sick, test positive), **false negatives** (FN: sick, test negative), **false positives** (FP: healthy, test positive), and **true negatives** (TN: healthy, test negative). **Sensitivity** = TP / (TP + FN): among everyone who *has* the disease, what fraction does the test catch? **Specificity** = TN / (TN + FP): among everyone who *does not* have the disease, what fraction does the test correctly clear? Sensitivity answers "how good is this test at not missing disease?" Specificity answers "how good is this test at not crying wolf?"

The trade-off between sensitivity and specificity is determined by where you set the diagnostic cutoff. Consider a blood glucose test for diabetes: if you lower the threshold from 126 to 100 mg/dL, you will catch more diabetics (higher sensitivity) but you will also flag more healthy people as positive (lower specificity). Raise the threshold and you do the reverse. This trade-off is visualized by the **ROC curve** — a topic you will encounter next — which plots sensitivity against (1 − specificity) across all possible cutoffs. The area under the ROC curve summarizes the test's overall discriminating power, independent of any particular threshold.

The most important conceptual point is that sensitivity and specificity are **properties of the test and its cutoff**, not of the population being tested. They do not change when prevalence changes. What does change with prevalence is the **predictive value**: in a low-prevalence population, even a highly specific test will generate many false positives relative to true positives, because the denominator of healthy people is enormous. A useful mnemonic: **SnOUT** — a test with high *Sen*sitivity, when *Negative*, rules *Out* disease (few false negatives, so a negative is reassuring); **SpIN** — a test with high *Spec*ificity, when *Positive*, rules *In* disease (few false positives, so a positive is convincing). Choosing which property to maximize depends on the clinical stakes: for a disease where missing cases is catastrophic (e.g., HIV screening, TB, some cancers), prioritize sensitivity. For a test where a false positive triggers a dangerous or expensive follow-up procedure, prioritize specificity.
