---
id: regression-discontinuity-design
title: Regression Discontinuity Design
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: natural-experiments
  type: hard
- id: epidemiologic-study-designs
  type: soft
tags:
- quasi-experimental
- threshold-design
- causal-effects
stage: advanced
status: draft
---

# Regression Discontinuity Design

## Core Idea
Regression discontinuity (RD) exploits a known threshold in an assignment rule (e.g., patients above age 65 receive treatment) to estimate causal effects. Comparing individuals just above and below the threshold eliminates confounding from variables varying smoothly near the cutoff, though effects are local to the threshold.

## Explainer

From your study of natural experiments, you know that nature and policy sometimes create variation in treatment assignment that is as good as random — not because researchers designed it, but because of arbitrary rules or external events. **Regression discontinuity design** is the most elegant exploitation of a specific type of natural experiment: one where treatment is assigned based on whether a continuous variable (the **running variable**) crosses a known threshold. The design turns the arbitrariness of the cutoff into a source of valid causal inference.

The canonical example is age-based eligibility. Medicare eligibility in the United States triggers at age 65 precisely. Someone who is 64 years and 11 months old is not eligible; someone who just turned 65 is. These two people are, in every meaningful respect, nearly identical — their health, income, education, and prior medical history are distributed almost the same in the population near that boundary. The sharp jump in treatment probability at exactly 65 is therefore arguably unrelated to the factors that would confound a naive comparison between the insured and uninsured. RD compares outcomes just above and just below the threshold to estimate what the insurance itself caused.

The identifying assumption is that all other determinants of the outcome vary **smoothly** at the threshold — meaning any jump in the outcome at the cutoff must be caused by the treatment, not by some other variable also jumping there. In practice, you test this by checking whether observable covariates (baseline health, demographics) show any discontinuities at the cutoff; if they do, the design is compromised. You also check for **manipulation**: if people can precisely sort themselves above or below the cutoff (e.g., if doctors delay a diagnosis to get a patient over a threshold), the groups near the boundary are no longer comparable. The density of the running variable around the cutoff — tested with McCrary's density test — should be smooth. A suspicious spike just above the cutoff suggests sorting.

The critical limitation of RD is that its estimates are **local to the threshold**: the causal effect applies to people whose running variable is close to the cutoff, not to the entire population. In the Medicare example, the effect of insurance is estimated for near-65-year-olds — people who are about to age into eligibility. Whether that estimate generalizes to, say, 45-year-olds or 75-year-olds depends on substantive reasoning about treatment effect heterogeneity, not on the design itself. This local average treatment effect (LATE) is often exactly the policy-relevant quantity — policymakers are frequently asking what happens at the margin — but it must be interpreted carefully. When treatment is only probabilistically rather than deterministically assigned at the threshold (a "fuzzy" RD), instrumental variables methods are used to account for imperfect compliance, and the effect estimate is scaled by the change in the probability of treatment at the cutoff. The elegance of RD is that it extracts credible causal evidence from rules that were never designed for research — but that credibility is entirely contingent on the smoothness assumption holding.
