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

## Explainer

From your study of disease frequency measures, you know how to calculate cumulative incidence (risk) — the proportion of a defined population that develops disease over a specified time period. From measures of association, you know the conceptual goal: comparing disease frequency between exposed and unexposed groups. **Relative risk** (also called the **risk ratio**) is the most direct expression of that comparison: RR = Risk(Exposed) / Risk(Unexposed). If 10% of smokers develop lung disease over 20 years and 1% of non-smokers do, the RR is 10/1 = 10 — smokers face ten times the risk. The ratio is interpretable on its own scale: an RR of 1.0 means identical risk in both groups (no association); above 1.0 means the exposure increases risk; below 1.0 means it decreases risk (a protective association).

The 2×2 table is the calculation engine. Label the rows exposed/unexposed and the columns diseased/not-diseased. The cells are conventionally called a (exposed and diseased), b (exposed and not diseased), c (unexposed and diseased), and d (unexposed and not diseased). Risk in the exposed group is a/(a+b); risk in the unexposed group is c/(c+d). RR = [a/(a+b)] / [c/(c+d)]. Notice what this requires: you need to know the denominator for each exposure group — how many people were at risk — which means RR is calculable in **cohort studies** (where you follow exposed and unexposed people forward in time) and randomized trials, but not in case-control studies (where cases and controls are sampled after the fact, destroying the natural denominators).

Understanding why RR differs from the **odds ratio** (OR) is critical for reading literature accurately. The OR compares odds rather than probabilities: OR = (a/b) / (c/d) = ad/bc. When disease is rare (incidence < 10%), odds ≈ probabilities, so OR ≈ RR — this is the **rare disease assumption** that makes OR from case-control studies a reasonable approximation of RR. When disease is common, OR diverges from RR substantially, and OR always exaggerates the association away from 1.0 relative to RR. An OR of 3.0 for a common outcome does not mean the same thing as an RR of 3.0. Many published meta-analyses and logistic regression studies report ORs — knowing when they approximate RR and when they don't is a foundational critical appraisal skill.

Interpreting a computed RR requires pairing it with a **confidence interval** and a **baseline risk**. Statistical significance (CI excluding 1.0) and clinical significance are separate questions. An RR of 1.5 with baseline risk of 0.01% means the absolute risk increase is 0.005% — clinically negligible despite the relative elevation. Conversely, an RR of 1.2 on a baseline risk of 30% means an absolute risk increase of 6 percentage points — clinically meaningful despite the modest ratio. The absolute risk reduction and **number needed to treat** (which you will study next) translate RR into the terms most useful for clinical and policy decisions.
