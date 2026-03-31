---
id: diagnostic-test-evaluation
title: Diagnostic Test Evaluation
domain: health-and-human-development
course: biostatistics
prerequisites:
- id: logistic-regression-biostatistics
  type: soft
- id: probability-theory
  type: hard
- id: study-design-biostatistics
  type: soft
builds-toward:
- roc-curves-biostatistics
tags:
- sensitivity
- specificity
- PPV
- NPV
- prevalence
- Bayes-theorem
stage: advanced
status: validated
---

# Diagnostic Test Evaluation

## Core Idea
Diagnostic test evaluation quantifies how well a test distinguishes between disease and non-disease. Sensitivity (true positive rate) is the probability that the test is positive given disease is present; specificity (true negative rate) is the probability that the test is negative given disease is absent. These are intrinsic properties of the test. Predictive values — positive predictive value (PPV: probability of disease given a positive test) and negative predictive value (NPV: probability of no disease given a negative test) — depend critically on disease prevalence in the tested population. A test with 99% sensitivity and 99% specificity has a PPV of only 50% when prevalence is 1%, because false positives outnumber true positives in low-prevalence populations. This prevalence dependence of predictive values, formalized by Bayes' theorem, is among the most counterintuitive and consequential results in clinical biostatistics.

## Questions

```yaml
- question: "A screening test for a rare cancer has 95% sensitivity and 90% specificity. In a population where the cancer prevalence is 0.1%, a patient tests positive. What is the approximate probability that this patient actually has cancer?"
  type: multiple-choice
  options:
    - "About 95%, because the test has 95% sensitivity"
    - "About 90%, because the test has 90% specificity"
    - "About 1%, because even with a good test, false positives vastly outnumber true positives when prevalence is very low"
    - "About 50%, because sensitivity and specificity are both high"
  answer: 2
  explanation: "In 100,000 people at 0.1% prevalence, 100 have cancer and 99,900 do not. Sensitivity of 95% detects 95 of 100 true cases. Specificity of 90% correctly rules out 89,910 of 99,900 non-cases, but misclassifies 9,990 as positive. Total positives: 95 + 9,990 = 10,085. PPV = 95/10,085 ≈ 0.94%, or about 1%. The overwhelming majority of positive tests are false positives because the non-diseased population is so much larger than the diseased population. This is why screening programs for rare diseases require confirmatory testing."

- question: "A test with high sensitivity is most useful for ruling out disease (SnNout: Sensitivity-Negative-rule Out), while a test with high specificity is most useful for ruling in disease (SpPin: Specificity-Positive-rule In)."
  type: true-false
  answer: true
  explanation: "A highly sensitive test rarely misses true cases, so a negative result effectively rules out the disease (if the test does not detect it, you almost certainly do not have it). A highly specific test rarely produces false positives, so a positive result effectively rules in the disease (if this stringent test says you have it, you almost certainly do). These mnemonics (SnNout and SpPin) capture the asymmetric clinical utility of sensitivity and specificity and guide the choice of test at different stages of the diagnostic workup."

- question: "A hospital administrator argues that because a test has 99% sensitivity and 99% specificity, it should be used for universal screening of all patients. Why might this be a poor decision for a disease with 0.01% prevalence?"
  type: multiple-choice
  options:
    - "The test is too expensive for universal use"
    - "At 0.01% prevalence, false positives will outnumber true positives by roughly 100:1, generating enormous numbers of unnecessary follow-up procedures"
    - "Sensitivity and specificity are unreliable metrics"
    - "Universal screening requires 100% sensitivity"
  answer: 1
  explanation: "In 1,000,000 screened patients at 0.01% prevalence, 100 have disease. Sensitivity of 99% detects 99. Specificity of 99% correctly clears 989,901 but produces 9,999 false positives. The PPV is 99/(99 + 9,999) ≈ 0.98%. For every true case found, roughly 101 healthy people receive a false alarm, each requiring expensive and potentially harmful follow-up (biopsies, imaging, anxiety). The cost-benefit calculus of screening depends on prevalence, not just test performance."

- question: "Explain why predictive values depend on prevalence but sensitivity and specificity do not."
  type: short-answer
  answer: "Sensitivity and specificity are conditional on true disease status — they measure test performance within the diseased and non-diseased groups separately, so they do not change with the proportion of diseased people in the population. Predictive values are conditional on test result — they ask 'given a positive test, what is the probability of disease?' This depends on the ratio of true positives to all positives, which changes with prevalence. As prevalence decreases, the non-diseased group grows, producing more false positives relative to true positives, and PPV drops even if sensitivity and specificity remain constant."
  explanation: "Bayes' theorem formalizes this relationship: PPV = (sensitivity × prevalence) / [(sensitivity × prevalence) + ((1-specificity) × (1-prevalence))]. The denominator includes both true positives and false positives. When prevalence is low, the false positive term dominates because it is multiplied by (1-prevalence), which is close to 1. This is why the same test can have a PPV of 95% in a high-risk clinic and 1% in a general screening program."
```

## Explainer

Every diagnostic test makes errors. It will occasionally miss true cases (false negatives) and occasionally flag healthy people as diseased (false positives). The question is how often, and — critically — how these error rates translate into clinical consequences for the patient sitting in front of you. **Sensitivity** and **specificity** quantify the test's intrinsic performance: sensitivity measures how well the test catches disease (P(positive | disease)), and specificity measures how well it rules it out (P(negative | no disease)). These are determined by the test's biology, threshold settings, and technical characteristics, and they remain the same regardless of who is being tested.

But the patient does not know their disease status — that is why they are being tested. The clinically relevant question is: given that the test came back positive, how likely is it that the patient actually has the disease? This is the **positive predictive value** (PPV), and it depends not just on the test's sensitivity and specificity but also on the **prevalence** of the disease in the population being tested. This dependence is counterintuitive and has profound implications for screening policy.

Consider a population of 10,000 where disease prevalence is 1% (100 have disease, 9,900 do not). A test with 95% sensitivity detects 95 of 100 true cases. A test with 95% specificity correctly clears 9,405 of 9,900 non-cases but produces 495 false positives. Total positives: 95 + 495 = 590. PPV = 95/590 = 16%. Even with a test that sounds excellent (95%/95%), more than 5 out of 6 positive results are wrong in a low-prevalence population. Drop prevalence to 0.1% and the PPV plummets further.

This is why clinical diagnosis uses a **sequential testing strategy**: start with sensitive tests to rule out disease cheaply (SnNout — Sensitivity, Negative result, rules Out), then confirm positives with specific tests to rule in disease (SpPin — Specificity, Positive result, rules In). The first step maximizes NPV (few false negatives among negative results); the second step maximizes PPV among the enriched population that screened positive. Understanding this Bayesian logic — that the meaning of a test result depends on the prior probability of disease — is essential for every clinical decision involving diagnostic testing.
