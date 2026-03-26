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
stage: expert
status: validated
---

# Positive and Negative Predictive Values

## Core Idea
Positive predictive value (PPV) is the probability a positive test result indicates disease; negative predictive value (NPV) is the probability a negative result indicates absence of disease. Unlike sensitivity and specificity, PPV and NPV depend on disease prevalence. PPV decreases in low-prevalence populations; NPV decreases in high-prevalence populations, making these measures critical for clinical decision-making in real populations.

## Questions

```yaml
- question: "A test for a rare disease has 99% sensitivity and 99% specificity. In a population where 1 in 1,000 people have the disease, a patient receives a positive result. Approximately what is the probability the patient actually has the disease?"
  type: multiple-choice
  options:
    - "About 99% — the test is 99% accurate, so a positive result almost certainly indicates disease"
    - "About 50% — since sensitivity and specificity are equal, positive and negative results are equally informative"
    - "About 9% — at this prevalence, false positives vastly outnumber true positives"
    - "About 1% — the result provides no information beyond the base rate"
  answer: 2
  explanation: "PPV = (sensitivity × prevalence) / [(sensitivity × prevalence) + (1−specificity) × (1−prevalence)]. With prevalence = 0.001, sensitivity = 0.99, specificity = 0.99: PPV = (0.99 × 0.001) / [(0.99 × 0.001) + (0.01 × 0.999)] = 0.00099 / (0.00099 + 0.00999) ≈ 9%. There are roughly 10 false positives for every true positive at this prevalence, because even a 1% false-positive rate generates many false alarms when applied to 999 truly disease-free individuals. The test hasn't changed — only the population has — and PPV falls dramatically. Option 0 is the classic misconception: 'accuracy' conflates sensitivity/specificity with clinical predictive value."

- question: "A highly effective screening program detects early-stage cancer in a low-prevalence population. Many patients with positive screens turn out to be disease-free after confirmatory testing. The medical team proposes abandoning the screening program because of its low positive predictive value. The best response is:"
  type: multiple-choice
  options:
    - "The program should be abandoned — a low PPV means the test is not working correctly"
    - "The PPV should be interpreted in context: low PPV is expected and acceptable in low-prevalence screening when the cost of missing a case exceeds the cost of confirmatory testing"
    - "The sensitivity should be increased to raise PPV, even if specificity falls"
    - "The program should switch to a test with higher specificity to directly raise PPV without needing prevalence data"
  answer: 1
  explanation: "Low PPV in population screening is mathematically inevitable and clinically acceptable. Screening applies a test to a low-prevalence population to catch disease before symptoms, accepting false positives as the cost of not missing true cases. The standard response is two-stage design: positive screens advance to a more specific confirmatory test applied to a population now enriched for disease (high effective prevalence), yielding high PPV at the confirmation stage. Abandoning the program because of low first-stage PPV misunderstands the design intent of screening."

- question: "A test with 99% sensitivity and 99% specificity will generally have a PPV above 90% in any clinical setting where it is applied."
  type: true-false
  answer: false
  explanation: "PPV depends on prevalence, not just test characteristics. As shown by the Bayesian calculation, a 99%/99% test applied to a population with 1-in-1,000 prevalence has PPV ≈ 9%. The test's technical performance is excellent, but when false positives from 999 healthy people outnumber true positives from 1 diseased person, most positive results are false. PPV can range from near 0% (very low prevalence) to near 100% (very high prevalence) for the same test. Treating sensitivity and specificity as 'accuracy' is the most dangerous misconception in diagnostic test interpretation."

- question: "When a positive-screen population advances to confirmatory testing, the effective prevalence seen by the confirmatory test is much higher than the base population's prevalence, which substantially raises the confirmatory test's PPV."
  type: true-false
  answer: true
  explanation: "This is the mathematical rationale for two-stage screening designs. Suppose 1% of the general population has a disease. After a first-stage test (sensitivity 95%, specificity 90%), roughly 95 of 100 true cases and 990 of 9,900 healthy individuals test positive — about 1,085 positives total. Among these, 95/1085 ≈ 8.8% have disease: the effective prevalence for the confirmatory test is now ~9%, not 1%. Applying a highly specific confirmatory test to this enriched group yields much higher PPV. Each stage of testing reshapes the effective prevalence seen by the next."

- question: "A physician tells a patient: 'This test is 99% accurate, so your positive result means there is a 99% chance you have the disease.' Under what conditions would this reasoning be seriously wrong, and why?"
  type: short-answer
  answer: "The reasoning is seriously wrong when disease prevalence in the tested population is low. 'Accuracy' (sensitivity/specificity) describes how the test performs on people known to have or not have disease. PPV — the probability of disease given a positive result — depends critically on how common the disease is in the population being tested. In a low-prevalence setting, even a 99% accurate test produces many false positives relative to true positives, so PPV can be far below 99%. The physician should apply Bayes' theorem: PPV = (sensitivity × prevalence) / [(sensitivity × prevalence) + (1−specificity)(1−prevalence)]. The relevant question is not 'how good is the test?' but 'given this patient's prior probability of disease, what does this positive result mean?'"
  explanation: "This error is pervasive in clinical practice and patient communication. The fix requires explicitly stating the prevalence (or pre-test probability) being assumed. A positive rapid strep test in a child with sore throat and fever (high pre-test probability) has very different post-test meaning than the same positive in a routine screening of healthy adults (low pre-test probability). Sensitivity and specificity are fixed properties of the test; PPV is a property of the test applied to a specific clinical context."
```

## Explainer

From your prerequisite on sensitivity and specificity, you know that **sensitivity** is P(T+|D+) — the probability the test is positive given disease is present — and **specificity** is P(T−|D−) — the probability the test is negative given disease is absent. These are properties of the test itself, measured by selecting participants based on known disease status. The problem is that clinical decisions run in the opposite direction: a patient presents with a test result, and you need to know P(D+|T+) — the probability disease is present given a positive test. This is the **positive predictive value (PPV)**, and computing it requires something that sensitivity and specificity alone cannot provide: **prevalence**, the baseline probability of disease in the population being tested.

Bayes' theorem makes the relationship explicit: PPV = (sensitivity × prevalence) / [(sensitivity × prevalence) + (1 − specificity) × (1 − prevalence)]. The denominator is simply the total probability of a positive test — true positives plus false positives. Consider a test with 99% sensitivity and 99% specificity — nearly perfect by any conventional standard. Applied to a disease with 1% prevalence (1 in 100 people have it): PPV ≈ (0.99 × 0.01) / [(0.99 × 0.01) + (0.01 × 0.99)] = 0.5. Half of positive tests are false positives. Apply the same test to a high-risk population where prevalence is 50%: PPV ≈ 0.99. The test has not changed; the population has changed; and the PPV has transformed from clinically concerning to clinically reassuring. **Negative predictive value (NPV)** moves in the opposite direction: NPV = (specificity × (1 − prevalence)) / [(specificity × (1 − prevalence)) + (1 − sensitivity) × prevalence]. NPV is high when prevalence is low — a negative test in a low-risk population is nearly conclusive evidence against disease — and falls as prevalence rises, because there are more true cases to miss.

The clinical consequence is that the same test must be interpreted differently in different populations. **Screening** (applying a test to a low-risk population to detect disease before symptoms) produces low PPV — most positive screens will be false positives. This is expected and acceptable, not a flaw, because the cost of a missed case (false negative) exceeds the cost of follow-up testing. The standard response to low PPV in screening is **confirmatory testing**: positive screens advance to a more specific (and often more invasive) test applied to a population now enriched for disease. This two-stage design exploits the math: the second test's effective prevalence is dramatically higher than the base population's prevalence, so its PPV is also dramatically higher. The same principle explains why a positive rapid strep test in a child with sore throat and fever is highly actionable (high prior probability), while the same positive test in a healthy adult being screened for pharyngeal carriage is much less meaningful. Prevalence is not a property of the test — it is a property of the clinical context — and PPV and NPV make that context explicit.
