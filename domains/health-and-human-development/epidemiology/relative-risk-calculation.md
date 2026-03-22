---
id: relative-risk-calculation
title: Relative Risk Calculation and Interpretation
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: measures-of-association
  type: hard
- id: disease-frequency-measures
  type: hard
builds-toward:
- attributable-risk-calculation
- number-needed-to-treat
tags:
- measures-of-association
- effect-size
- risk-ratio
- cohort-studies
stage: advanced
status: draft
---

# Relative Risk Calculation and Interpretation

## Core Idea
Relative risk (RR) compares the probability of disease in an exposed group versus an unexposed group: RR = Risk(Exposed) / Risk(Unexposed). An RR > 1 indicates increased risk, RR = 1 indicates no association, and RR < 1 indicates decreased risk. It is the primary measure of effect in cohort and experimental studies.

## How It's Best Learned
Work with 2×2 tables from published cohort studies, calculating incidence in each exposure group, then compute and interpret the ratio. Practice with various RR values and confidence intervals to understand clinical significance.

## Common Misconceptions
RR ≠ OR; RR of 2 does not mean twice as many people will develop disease, only that the rate is twice as high; CI not crossing 1 indicates statistical significance but not necessarily clinical importance.

## Questions

```yaml
- question: "A case-control study reports an odds ratio of 4.0 for the association between a dietary exposure and a disease. A colleague says this means exposed people have 4 times the risk. Why is this claim potentially incorrect?"
  type: multiple-choice
  options:
    - "The OR should be divided by the baseline prevalence to convert it to a risk ratio"
    - "Case-control studies sample participants after disease occurrence, so natural denominators are absent and OR cannot be directly read as RR"
    - "An OR of 4.0 always understates the true relative risk due to selection bias"
    - "The claim is correct whenever the confidence interval excludes 1.0"
  answer: 1
  explanation: "Relative risk requires knowing how many people in each exposure group were at risk — the denominators. In a case-control study, cases and controls are selected by disease status after the fact, so the natural proportions of exposed and unexposed people who developed disease are not preserved. The OR approximates RR only when disease is rare (rare disease assumption); for common outcomes, OR exaggerates away from 1.0 and cannot be interpreted as 'times the risk.'"

- question: "A cohort study reports RR = 1.8 (95% CI: 1.6–2.0) for an exposure with a baseline (unexposed) disease risk of 0.1%. Which conclusion is most accurate?"
  type: multiple-choice
  options:
    - "The exposure is both statistically and clinically significant because RR exceeds 1.5"
    - "The exposure is statistically significant but the absolute risk increase is only 0.08 percentage points — likely clinically negligible"
    - "The confidence interval indicates the true RR might be as low as 1.6, suggesting the exposure may be protective"
    - "An RR below 2.0 is never clinically meaningful regardless of baseline risk"
  answer: 1
  explanation: "Statistical significance (CI excludes 1.0) and clinical significance are separate judgments. Absolute risk increase = RR × baseline risk − baseline risk = 0.8 × 0.1% = 0.08%. Even though the relative elevation is 80%, adding 0.08 percentage points to an already tiny risk is unlikely to influence clinical decisions. Option C misreads the CI: 1.6 is still above 1.0, indicating increased (not protective) risk throughout the interval."

- question: "The odds ratio from a case-control study is always a valid substitute for relative risk, regardless of disease frequency in the population."
  type: true-false
  answer: false
  explanation: "The OR approximates RR only when disease incidence is low (roughly < 10%), under the rare disease assumption. When disease is common, odds and probabilities diverge substantially, and the OR exaggerates the association away from 1.0 compared to RR. An OR of 3.0 for a common outcome overstates the true relative risk — treating it as RR leads to inflated effect size estimates."

- question: "Relative risk can be calculated from cohort studies but cannot be directly calculated from case-control studies."
  type: true-false
  answer: true
  explanation: "RR = Risk(exposed) / Risk(unexposed) requires knowing the denominators — how many exposed and unexposed people were initially at risk. Cohort studies follow defined groups forward in time, preserving these denominators. Case-control studies select participants based on outcome status after the fact, destroying the natural denominators. The calculable measure from case-control data is the odds ratio, which approximates RR only under the rare disease assumption."

- question: "Explain why an RR of 2.0 might be clinically important in one context but clinically trivial in another, using the concept of absolute risk."
  type: short-answer
  answer: "RR is a ratio that says nothing about the baseline level of risk. If baseline risk is 30%, an RR of 2.0 means absolute risk increases by 30 percentage points — a massive, clinically critical difference. If baseline risk is 0.01%, an RR of 2.0 adds only 0.01 percentage points — negligible in practice. Clinical decisions depend on absolute risk change, not relative elevation alone."
  explanation: "This is one of the most important critical appraisal skills in epidemiology. Absolute risk increase (ARI) = (RR − 1) × baseline risk. The same RR can justify urgent intervention in a high-risk population and be irrelevant in a low-risk one. This is also why number needed to treat (NNT = 1/ARI) is often more useful for clinical decision-making than RR alone."
```

## Explainer

From your study of disease frequency measures, you know how to calculate cumulative incidence (risk) — the proportion of a defined population that develops disease over a specified time period. From measures of association, you know the conceptual goal: comparing disease frequency between exposed and unexposed groups. **Relative risk** (also called the **risk ratio**) is the most direct expression of that comparison: RR = Risk(Exposed) / Risk(Unexposed). If 10% of smokers develop lung disease over 20 years and 1% of non-smokers do, the RR is 10/1 = 10 — smokers face ten times the risk. The ratio is interpretable on its own scale: an RR of 1.0 means identical risk in both groups (no association); above 1.0 means the exposure increases risk; below 1.0 means it decreases risk (a protective association).

The 2×2 table is the calculation engine. Label the rows exposed/unexposed and the columns diseased/not-diseased. The cells are conventionally called a (exposed and diseased), b (exposed and not diseased), c (unexposed and diseased), and d (unexposed and not diseased). Risk in the exposed group is a/(a+b); risk in the unexposed group is c/(c+d). RR = [a/(a+b)] / [c/(c+d)]. Notice what this requires: you need to know the denominator for each exposure group — how many people were at risk — which means RR is calculable in **cohort studies** (where you follow exposed and unexposed people forward in time) and randomized trials, but not in case-control studies (where cases and controls are sampled after the fact, destroying the natural denominators).

Understanding why RR differs from the **odds ratio** (OR) is critical for reading literature accurately. The OR compares odds rather than probabilities: OR = (a/b) / (c/d) = ad/bc. When disease is rare (incidence < 10%), odds ≈ probabilities, so OR ≈ RR — this is the **rare disease assumption** that makes OR from case-control studies a reasonable approximation of RR. When disease is common, OR diverges from RR substantially, and OR always exaggerates the association away from 1.0 relative to RR. An OR of 3.0 for a common outcome does not mean the same thing as an RR of 3.0. Many published meta-analyses and logistic regression studies report ORs — knowing when they approximate RR and when they don't is a foundational critical appraisal skill.

Interpreting a computed RR requires pairing it with a **confidence interval** and a **baseline risk**. Statistical significance (CI excluding 1.0) and clinical significance are separate questions. An RR of 1.5 with baseline risk of 0.01% means the absolute risk increase is 0.005% — clinically negligible despite the relative elevation. Conversely, an RR of 1.2 on a baseline risk of 30% means an absolute risk increase of 6 percentage points — clinically meaningful despite the modest ratio. The absolute risk reduction and **number needed to treat** (which you will study next) translate RR into the terms most useful for clinical and policy decisions.
