---
id: predictive-values-diagnostics
title: Positive and Negative Predictive Values
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: diagnostic-sensitivity-specificity
  type: hard
builds-toward:
- screening-test-evaluation
tags:
- predictive-value
- positive-predictive-value
- negative-predictive-value
- prevalence-dependence
stage: advanced
status: draft
---

# Positive and Negative Predictive Values

## Core Idea
Positive predictive value (PPV) is the probability a positive test result indicates disease; negative predictive value (NPV) is the probability a negative result indicates absence of disease. Unlike sensitivity and specificity, PPV and NPV depend on disease prevalence. PPV decreases in low-prevalence populations; NPV decreases in high-prevalence populations, making these measures critical for clinical decision-making in real populations.

## Explainer

From your prerequisite on sensitivity and specificity, you know that **sensitivity** is P(T+|D+) — the probability the test is positive given disease is present — and **specificity** is P(T−|D−) — the probability the test is negative given disease is absent. These are properties of the test itself, measured by selecting participants based on known disease status. The problem is that clinical decisions run in the opposite direction: a patient presents with a test result, and you need to know P(D+|T+) — the probability disease is present given a positive test. This is the **positive predictive value (PPV)**, and computing it requires something that sensitivity and specificity alone cannot provide: **prevalence**, the baseline probability of disease in the population being tested.

Bayes' theorem makes the relationship explicit: PPV = (sensitivity × prevalence) / [(sensitivity × prevalence) + (1 − specificity) × (1 − prevalence)]. The denominator is simply the total probability of a positive test — true positives plus false positives. Consider a test with 99% sensitivity and 99% specificity — nearly perfect by any conventional standard. Applied to a disease with 1% prevalence (1 in 100 people have it): PPV ≈ (0.99 × 0.01) / [(0.99 × 0.01) + (0.01 × 0.99)] = 0.5. Half of positive tests are false positives. Apply the same test to a high-risk population where prevalence is 50%: PPV ≈ 0.99. The test has not changed; the population has changed; and the PPV has transformed from clinically concerning to clinically reassuring. **Negative predictive value (NPV)** moves in the opposite direction: NPV = (specificity × (1 − prevalence)) / [(specificity × (1 − prevalence)) + (1 − sensitivity) × prevalence]. NPV is high when prevalence is low — a negative test in a low-risk population is nearly conclusive evidence against disease — and falls as prevalence rises, because there are more true cases to miss.

The clinical consequence is that the same test must be interpreted differently in different populations. **Screening** (applying a test to a low-risk population to detect disease before symptoms) produces low PPV — most positive screens will be false positives. This is expected and acceptable, not a flaw, because the cost of a missed case (false negative) exceeds the cost of follow-up testing. The standard response to low PPV in screening is **confirmatory testing**: positive screens advance to a more specific (and often more invasive) test applied to a population now enriched for disease. This two-stage design exploits the math: the second test's effective prevalence is dramatically higher than the base population's prevalence, so its PPV is also dramatically higher. The same principle explains why a positive rapid strep test in a child with sore throat and fever is highly actionable (high prior probability), while the same positive test in a healthy adult being screened for pharyngeal carriage is much less meaningful. Prevalence is not a property of the test — it is a property of the clinical context — and PPV and NPV make that context explicit.
