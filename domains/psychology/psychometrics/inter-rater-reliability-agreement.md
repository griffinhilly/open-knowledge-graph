---
id: inter-rater-reliability-agreement
title: Inter-Rater Reliability and Observer Agreement
domain: psychology
course: psychometrics
prerequisites:
- id: classical-test-theory
  type: hard
- id: probability-and-statistics
  type: soft
builds-toward:
- generalizability-theory-g-theory
tags:
- reliability
- rater-agreement
- observational-measures
stage: advanced
status: validated
---

# Inter-Rater Reliability and Observer Agreement

## Core Idea
Inter-rater reliability assesses agreement between independent judges or raters on the same set of observations or responses. Percent agreement, Cohen's kappa, and intraclass correlations are common metrics. This is critical for observational measures, clinical diagnoses, and subjective scoring methods.

## How It's Best Learned
Calculate kappa and ICC coefficients from contingency tables and continuous rating data. Compare agreement metrics under different base rate conditions (high vs. low prevalence).

## Common Misconceptions
Using simple percent agreement without accounting for chance agreement. Assuming kappa above .80 is universally acceptable; standards vary by measurement context. Different thresholds apply in high-stakes testing versus research applications.

## Questions

```yaml
- question: "Two clinical raters independently assess 100 patients for depression in a clinic where 95% of patients are not depressed. Both raters always code 'not depressed.' What are their percent agreement and Cohen's kappa?"
  type: multiple-choice
  options:
    - "Percent agreement = 95%, kappa ≈ 0"
    - "Percent agreement = 95%, kappa ≈ 0.95"
    - "Percent agreement = 100%, kappa = 1.0"
    - "Percent agreement = 100%, kappa ≈ 0"
  answer: 3
  explanation: "Both raters agree on every case (100% of cases), so percent agreement = 100%. But their entire agreement is explained by chance: given the 95% base rate of 'not depressed,' two raters independently assigning that category would agree nearly all the time by luck. Kappa corrects for this expected chance agreement, yielding a value near 0 — meaning their agreement provides essentially no evidence of true rater concordance. This is the base rate problem: high percent agreement can be meaningless when one category dominates."

- question: "A researcher uses percent agreement to report inter-rater reliability for a coding scheme with three behavioral categories used roughly equally (≈33% each). Compared to Cohen's kappa, what is most likely true?"
  type: multiple-choice
  options:
    - "Percent agreement will be lower than kappa, because it ignores systematic rater bias"
    - "Percent agreement will be higher than kappa, because kappa subtracts the expected chance agreement"
    - "Percent agreement and kappa will be equal, because equal base rates eliminate chance agreement"
    - "Percent agreement will be higher than kappa, because kappa penalizes raters for using more than two categories"
  answer: 1
  explanation: "Kappa always subtracts expected chance agreement from observed agreement: κ = (P_o − P_e) / (1 − P_e). When categories are roughly equally used, P_e (the expected agreement by chance) is about 1/3 for a three-category scheme, so a 70% percent agreement would yield a kappa of about (0.70 − 0.33) / (1 − 0.33) ≈ 0.55 — substantially lower than the raw 70%. Percent agreement never adjusts for chance and will therefore always be ≥ kappa."

- question: "Cohen's kappa can be 0 even when two raters show high percent agreement, if that agreement is entirely explained by the expected base rate."
  type: true-false
  answer: true
  explanation: "This is the central insight of kappa: it measures agreement *above and beyond* what would be expected by chance. When both raters systematically use the same dominant category (because it is very prevalent), their observed agreement P_o approaches P_e, making the numerator (P_o − P_e) approach 0. Kappa thus correctly reveals that the raters are not adding independent information — they are just reflecting the base rate. This is why percent agreement alone is an inadequate reliability metric."

- question: "A kappa of .80 is widely accepted as indicating good inter-rater reliability and can be applied as a universal threshold across most measurement contexts."
  type: true-false
  answer: false
  explanation: "Kappa thresholds are context-dependent. In high-stakes clinical or legal settings (e.g., psychiatric diagnosis, neuroimaging interpretation), a kappa of .80 might be inadequate. In exploratory research with complex behavioral coding, a kappa of .60 might be acceptable. Standards also vary by number of categories, prevalence of categories, and the consequences of rater disagreement. The common misconception is treating any single threshold as universal — a sign that the researcher hasn't thought through the specific demands of their measurement context."

- question: "Why does the prevalence of the categories being rated affect the interpretation of Cohen's kappa, and what problem does this create for researchers using binary diagnostic categories with rare conditions?"
  type: short-answer
  answer: "Kappa's denominator adjusts for expected chance agreement, which depends on the marginal distributions — how often each rater uses each category. When one category is very rare (e.g., 5% of cases have the target condition), two raters who always say 'absent' agree 95% of the time by chance. Their kappa approaches 0 despite high percent agreement, making kappa appear very low even if both raters are doing their jobs well. Conversely, when conditions are rare and only a few discordant cases exist, small differences in rater judgment can swing kappa dramatically. This creates the 'kappa paradox': reliability appears low for rare conditions not because raters are performing poorly, but because the chance agreement baseline is so high."
  explanation: "This is a known limitation that has generated substantial debate in psychometrics. For rare conditions, alternatives like prevalence-adjusted bias-adjusted kappa (PABAK) or the intraclass correlation coefficient (for continuous ratings) may be more informative. The key lesson is that no single reliability metric is appropriate for all measurement contexts — understanding what a metric does and does not capture is as important as computing it."
```

## Explainer

Classical test theory — your prerequisite — partitions an observed score into a true score and random error: X = T + E. When the measurement involves a human observer making a judgment (rating clinical severity, scoring an essay, coding a behavioral observation), a new source of error enters: the rater. Two raters observing the same behavior may code it differently because they attend to different features, apply the construct differently, or simply have different thresholds for categories. **Inter-rater reliability** quantifies how much of this rater-specific variance is present — it is, in CTT terms, an estimate of how much the error term inflates when the source of error is inconsistent human judgment rather than random noise in the measurement instrument.

The simplest metric is **percent agreement**: count how many items or cases the two raters coded identically, divide by total cases, express as a percentage. If two observers code 80 of 100 behavioral episodes identically, percent agreement = .80. This is intuitive but misleading, because some agreement will occur by chance. If both raters are randomly assigning one of two categories (50/50), you would expect them to agree 50% of the time even with no real relationship between their ratings. Percent agreement inflates reliability by ignoring this baseline.

**Cohen's kappa** corrects for chance agreement: κ = (P_o − P_e) / (1 − P_e), where P_o is observed agreement and P_e is expected agreement by chance. Kappa ranges from 0 (agreement no better than chance) to 1.0 (perfect agreement); negative values indicate agreement worse than chance. The calculation of P_e requires knowing the marginal distributions — how frequently each rater uses each category — which is why base rates matter. When one category is very rare, even very low kappa can accompany high percent agreement. This is the **base rate problem**: if 95% of cases are "not depressed," two raters who always say "not depressed" agree 95% of the time, but their kappa is 0.

For continuous ratings — where raters assign numerical scores rather than categories — the appropriate metric is the **intraclass correlation coefficient (ICC)**. ICC comes in several forms (one-way, two-way, agreement vs. consistency) depending on whether the raters are considered a fixed or random sample and whether systematic rater bias should count against reliability. Choosing the right ICC form requires thinking through your measurement design before running the analysis, which is why your prerequisite in probability and statistics — particularly variance partitioning — directly supports this topic.


