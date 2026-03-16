---
id: nested-case-control-studies
title: Nested Case-Control and Case-Cohort Studies
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: epidemiologic-study-designs
  type: hard
- id: person-time-follow-up-studies
  type: hard
builds-toward:
- exposure-measurement-error-epi
tags:
- study-design
- efficiency
- cohort-substudies
stage: advanced
status: draft
---

# Nested Case-Control and Case-Cohort Studies

## Core Idea
Nested case-control and case-cohort designs select subcohorts from a parent cohort to measure expensive exposures, reducing cost while maintaining prospective strength. Both preserve person-time denominators and allow calculation of relative risk.

## Explainer

From your study of epidemiologic study designs and person-time follow-up studies, you know the basic tradeoffs: a full cohort study follows everyone from enrollment to outcome, giving you exposure data on all participants and precise estimates of incidence rates — but it is expensive when the exposure measurement is costly (a genetic assay, a stored biomarker, an expensive laboratory panel). A traditional case-control study is efficient — you only measure exposure in cases and selected controls — but it is retrospective and vulnerable to recall bias and selection bias. Nested case-control and case-cohort designs occupy a powerful middle ground: they extract efficiency savings from the case-control logic while retaining the prospective structure of a cohort.

In a **nested case-control study**, you begin with a defined parent cohort with baseline information collected at enrollment. As follow-up proceeds and cases (people who develop the outcome) emerge, you define **risk sets**: at the moment each case is diagnosed, the risk set consists of all cohort members who are still under follow-up and haven't yet had the outcome — they were "at risk" of being the case at that moment. You then randomly sample a small number of **controls** from the risk set for each case, and measure the expensive exposure only in the cases plus their matched controls. This sampling procedure is called **incidence density sampling**. Because controls are sampled from the risk set at the time of the case, the odds ratio from the nested case-control directly estimates the **rate ratio** (incidence rate ratio) — without the approximation assumptions required by traditional case-control studies. This is a major advantage: you recover the interpretive strength of a rate-based cohort analysis at a fraction of the cost.

The **case-cohort design** solves the same efficiency problem differently. Rather than matching controls to each case individually, you define a **subcohort** — a random sample of the full cohort selected at baseline — and measure the expensive exposure in everyone in the subcohort plus all cases (whether or not they are in the subcohort). The subcohort serves as the reference population for all cases throughout the study period, regardless of when they occur. This means a case-cohort design can support multiple outcomes analyzed against the same subcohort, making it highly efficient for studies with several endpoints. The analysis uses modified survival analysis methods (Prentice weighting) to account for the fact that subcohort members are sampled with known probability. The case-cohort design produces **hazard ratios** rather than odds ratios, and the subcohort members who later become cases contribute to both the case group and the subcohort, requiring care in the statistical analysis.

Both designs preserve the prospective exposure-before-outcome ordering that eliminates recall bias. Both allow you to calculate absolute risks and rates, not just odds ratios, because the parent cohort's person-time denominator is known. The key tradeoff between them is this: nested case-control designs are more statistically efficient when you have a single outcome and want to match on time-varying confounders, while case-cohort designs are more efficient when you want to study multiple outcomes against the same control pool. In either case, you are buying analytic power at a fraction of the cost of measuring the expensive exposure in the full cohort — which is why these designs are standard in large biobank studies where genetic or biomarker assays are the bottleneck.
