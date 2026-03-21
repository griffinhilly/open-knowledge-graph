---
id: diagnostic-cutoff-scores-classification-accuracy
title: Diagnostic Cutoff Scores and Classification Accuracy
domain: psychology
course: psychometrics
prerequisites:
- id: standard-error-of-measurement-applications
  type: hard
- id: item-response-theory-assumptions
  type: soft
tags:
- cutoff-scores
- classification
- sensitivity-specificity
stage: advanced
status: draft
---

# Diagnostic Cutoff Scores and Classification Accuracy

## Core Idea
Clinical cutoff scores define pass/fail or disorder decisions. Optimal cutoffs balance sensitivity (true positive rate) and specificity (true negative rate), using receiver operating characteristic curves. A single cutoff reflects a chosen trade-off; raising cutoffs increases specificity but decreases sensitivity. Reporting confidence intervals and misclassification rates improves ethical use.

## How It's Best Learned
Generate ROC curves for actual test data, calculate sensitivity/specificity at various cutoffs, and discuss practical implications of different choices for stakeholders.

## Questions

```yaml
- question: "A hospital lowers the cutoff score on a depression screening test, so more people screen positive. What happens to sensitivity and specificity?"
  type: multiple-choice
  options:
    - "Both sensitivity and specificity increase — a lower cutoff is more accurate overall"
    - "Sensitivity increases and specificity decreases — more true cases are caught but more false alarms are generated"
    - "Specificity increases and sensitivity decreases — the stricter threshold catches only true cases"
    - "Neither changes — the AUC is fixed and cutoff placement does not affect classification accuracy"
  answer: 1
  explanation: "Lowering the cutoff means more people pass the threshold, which catches more true positives (higher sensitivity) but also flags more people who don't have the condition (lower specificity). This is the fundamental trade-off: sensitivity and specificity move in opposite directions as you shift the cutoff. Option D is a common misconception — the AUC is fixed (it summarizes the test's overall discriminatory ability), but sensitivity and specificity at any particular cutoff absolutely change with threshold placement."

- question: "A researcher compares two screening tests. Test A has AUC = 0.91; Test B has AUC = 0.64. Which conclusion is most accurate?"
  type: multiple-choice
  options:
    - "Test A has higher sensitivity than Test B at every possible cutoff"
    - "Test B should never be used clinically because it performs below 0.70"
    - "Test A is more discriminating overall — across all possible cutoffs it better separates true positives from true negatives"
    - "Test A is always the better choice regardless of the clinical context"
  answer: 2
  explanation: "AUC summarizes overall discriminatory accuracy across all possible cutoffs. A higher AUC means the test better separates cases from non-cases on average. However, AUC does not tell you which test has higher sensitivity at any specific cutoff (option A is wrong — high overall AUC doesn't mean dominance at every single threshold). Option B is overly rigid — a test with AUC 0.64 may still be useful in low-resource settings or for preliminary screening. Option D ignores that clinical context (costs of false positives vs. false negatives) should drive test and cutoff selection."

- question: "A test with high sensitivity will necessarily also have high specificity, since both indicate a well-performing test."
  type: true-false
  answer: false
  explanation: "Sensitivity and specificity trade off structurally. Sensitivity measures how well the test identifies true positives; specificity measures how well it excludes true negatives. Lowering the cutoff raises sensitivity (fewer missed cases) but lowers specificity (more false positives). A perfect test would have both, but real tests always sacrifice one for the other at any given cutoff. A useful mnemonic: high sensitivity means few false negatives (good for ruling out); high specificity means few false positives (good for ruling in)."

- question: "Choosing where to place a diagnostic cutoff score is a values judgment — not a purely statistical optimization — because different clinical contexts call for different tolerances for false positives versus false negatives."
  type: true-false
  answer: true
  explanation: "This is the central ethical insight of the topic. Statistics can tell you the sensitivity and specificity at every possible cutoff, but they cannot tell you which error is worse. For suicidality screening, missing a true case (false negative) is catastrophic — so you set a low threshold and accept more false alarms. For allocating scarce services, generating many false positives wastes resources and causes harm — so you set a higher threshold. The choice reflects values about harm, not just accuracy, and should be made explicitly rather than buried in a 'standard' cutoff."

- question: "Why is choosing a diagnostic cutoff score described as a values judgment rather than a purely statistical decision? Give an example of two clinical contexts that would warrant different cutoff placements for the same test."
  type: short-answer
  answer: "Any cutoff placement involves accepting more of one error type (false positives or false negatives) at the expense of the other. That trade-off cannot be resolved statistically — it depends on the relative costs of each error in context. For example, a cutoff for suicidality screening should be set low (high sensitivity) because missing a true case can be fatal, even at the cost of many false alarms that follow-up assessment can filter. A cutoff for allocating a scarce treatment resource should be set higher (high specificity) to avoid misallocating limited resources to people who don't need the treatment."
  explanation: "The ROC curve maps sensitivity against false positive rate at every possible threshold, but it cannot choose among them. That choice requires a values framework: who is harmed by each error type, how badly, and how recoverable is the harm? Ethical diagnostic practice requires making these assumptions explicit and transparent, and communicating confidence intervals and misclassification rates alongside any classification decision."
```

## Explainer

You already know from the standard error of measurement that no test score is a perfect reflection of true ability — every score is a sample from a distribution of possible scores, with measurement error around it. That measurement error matters enormously when you need to make a yes/no decision: does this person have a disorder? Do they qualify for services? A **diagnostic cutoff score** converts a continuous scale into a binary classification, and the central question is: at what point do you draw the line, and what are the consequences of being wrong?

There are two types of classification error. A **false positive** occurs when someone without the condition is classified as having it. A **false negative** occurs when someone with the condition is missed. Neither error is neutral: false positives may lead to unnecessary treatment and stigmatization; false negatives leave real conditions undetected and untreated. **Sensitivity** measures how well the test identifies true cases — formally, the proportion of actual positives correctly classified (high sensitivity means few false negatives). **Specificity** measures how well it excludes non-cases — the proportion of actual negatives correctly classified (high specificity means few false positives). These two quantities are structurally in tension: lowering the cutoff score lets more people through (higher sensitivity, lower specificity); raising it excludes more people (lower sensitivity, higher specificity).

The **ROC (Receiver Operating Characteristic) curve** visualizes this trade-off across all possible cutoff values. For each candidate cutoff, you plot sensitivity on the y-axis against the false positive rate (1 − specificity) on the x-axis. A test with no diagnostic value falls along the diagonal — at any sensitivity level, you achieve the same false positive rate by chance. A useful test curves toward the upper-left corner. The **area under the ROC curve (AUC)** summarizes overall diagnostic accuracy in a single number: 0.5 is chance performance, 1.0 is perfect discrimination, and values above 0.70 are generally considered clinically useful.

Choosing the optimal cutoff is a values judgment, not a purely statistical one. For a screening test aimed at a serious, treatable condition — suicidality, early-stage cancer — you prioritize sensitivity. You'd rather have false alarms than miss real cases, especially when false positives can be filtered by follow-up assessment. For a test used to allocate a scarce benefit, you might prioritize specificity. These priorities should be explicit and transparent — not hidden inside a number that appears neutral. Because measurement error creates a band of uncertainty around any score, cutoffs should never be applied mechanically; reporting confidence intervals around classification decisions and acknowledging the standard error of measurement are basic requirements for ethical diagnostic practice.
