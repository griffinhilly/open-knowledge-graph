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

## Explainer

You already know from the standard error of measurement that no test score is a perfect reflection of true ability — every score is a sample from a distribution of possible scores, with measurement error around it. That measurement error matters enormously when you need to make a yes/no decision: does this person have a disorder? Do they qualify for services? A **diagnostic cutoff score** converts a continuous scale into a binary classification, and the central question is: at what point do you draw the line, and what are the consequences of being wrong?

There are two types of classification error. A **false positive** occurs when someone without the condition is classified as having it. A **false negative** occurs when someone with the condition is missed. Neither error is neutral: false positives may lead to unnecessary treatment and stigmatization; false negatives leave real conditions undetected and untreated. **Sensitivity** measures how well the test identifies true cases — formally, the proportion of actual positives correctly classified (high sensitivity means few false negatives). **Specificity** measures how well it excludes non-cases — the proportion of actual negatives correctly classified (high specificity means few false positives). These two quantities are structurally in tension: lowering the cutoff score lets more people through (higher sensitivity, lower specificity); raising it excludes more people (lower sensitivity, higher specificity).

The **ROC (Receiver Operating Characteristic) curve** visualizes this trade-off across all possible cutoff values. For each candidate cutoff, you plot sensitivity on the y-axis against the false positive rate (1 − specificity) on the x-axis. A test with no diagnostic value falls along the diagonal — at any sensitivity level, you achieve the same false positive rate by chance. A useful test curves toward the upper-left corner. The **area under the ROC curve (AUC)** summarizes overall diagnostic accuracy in a single number: 0.5 is chance performance, 1.0 is perfect discrimination, and values above 0.70 are generally considered clinically useful.

Choosing the optimal cutoff is a values judgment, not a purely statistical one. For a screening test aimed at a serious, treatable condition — suicidality, early-stage cancer — you prioritize sensitivity. You'd rather have false alarms than miss real cases, especially when false positives can be filtered by follow-up assessment. For a test used to allocate a scarce benefit, you might prioritize specificity. These priorities should be explicit and transparent — not hidden inside a number that appears neutral. Because measurement error creates a band of uncertainty around any score, cutoffs should never be applied mechanically; reporting confidence intervals around classification decisions and acknowledging the standard error of measurement are basic requirements for ethical diagnostic practice.
