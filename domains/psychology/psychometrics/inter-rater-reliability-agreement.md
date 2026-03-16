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
status: draft
---

# Inter-Rater Reliability and Observer Agreement

## Core Idea
Inter-rater reliability assesses agreement between independent judges or raters on the same set of observations or responses. Percent agreement, Cohen's kappa, and intraclass correlations are common metrics. This is critical for observational measures, clinical diagnoses, and subjective scoring methods.

## How It's Best Learned
Calculate kappa and ICC coefficients from contingency tables and continuous rating data. Compare agreement metrics under different base rate conditions (high vs. low prevalence).

## Common Misconceptions
Using simple percent agreement without accounting for chance agreement. Assuming kappa above .80 is universally acceptable; standards vary by measurement context. Different thresholds apply in high-stakes testing versus research applications.

## Explainer

Classical test theory — your prerequisite — partitions an observed score into a true score and random error: X = T + E. When the measurement involves a human observer making a judgment (rating clinical severity, scoring an essay, coding a behavioral observation), a new source of error enters: the rater. Two raters observing the same behavior may code it differently because they attend to different features, apply the construct differently, or simply have different thresholds for categories. **Inter-rater reliability** quantifies how much of this rater-specific variance is present — it is, in CTT terms, an estimate of how much the error term inflates when the source of error is inconsistent human judgment rather than random noise in the measurement instrument.

The simplest metric is **percent agreement**: count how many items or cases the two raters coded identically, divide by total cases, express as a percentage. If two observers code 80 of 100 behavioral episodes identically, percent agreement = .80. This is intuitive but misleading, because some agreement will occur by chance. If both raters are randomly assigning one of two categories (50/50), you would expect them to agree 50% of the time even with no real relationship between their ratings. Percent agreement inflates reliability by ignoring this baseline.

**Cohen's kappa** corrects for chance agreement: κ = (P_o − P_e) / (1 − P_e), where P_o is observed agreement and P_e is expected agreement by chance. Kappa ranges from 0 (agreement no better than chance) to 1.0 (perfect agreement); negative values indicate agreement worse than chance. The calculation of P_e requires knowing the marginal distributions — how frequently each rater uses each category — which is why base rates matter. When one category is very rare, even very low kappa can accompany high percent agreement. This is the **base rate problem**: if 95% of cases are "not depressed," two raters who always say "not depressed" agree 95% of the time, but their kappa is 0.

For continuous ratings — where raters assign numerical scores rather than categories — the appropriate metric is the **intraclass correlation coefficient (ICC)**. ICC comes in several forms (one-way, two-way, agreement vs. consistency) depending on whether the raters are considered a fixed or random sample and whether systematic rater bias should count against reliability. Choosing the right ICC form requires thinking through your measurement design before running the analysis, which is why your prerequisite in probability and statistics — particularly variance partitioning — directly supports this topic.


