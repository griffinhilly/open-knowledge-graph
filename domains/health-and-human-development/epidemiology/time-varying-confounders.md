---
id: time-varying-confounders
title: Time-Varying Confounders and Longitudinal Exposure
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: person-time-follow-up-studies
  type: hard
- id: confounding-epidemiology
  type: hard
builds-toward:
- marginal-structural-models
- g-estimation-causal-effects
tags:
- longitudinal-analysis
- time-varying-confounding
- exposure-dynamics
stage: advanced
status: draft
---

# Time-Varying Confounders and Longitudinal Exposure

## Core Idea
Time-varying confounding occurs when a variable is a confounder at some timepoint but is also affected by prior exposure. Standard regression adjustment introduces bias because adjusting for a mediator of prior exposure induces collider bias. Methods like marginal structural models or g-estimation handle this scenario.

## Explainer

From your study of confounding, you know the three criteria: a confounder must be associated with the exposure, associated with the outcome independently of the exposure, and must not lie on the causal pathway between them. You also know the solution: measure the confounder and adjust for it using stratification or regression. This works well when confounders are stable baseline characteristics. Time-varying confounding is the complication that arises in longitudinal studies when a covariate changes during follow-up — and when its value at any point is partly caused by the prior exposure history.

The canonical example comes from HIV treatment research. Suppose you want to know whether early AZT treatment prolongs survival in HIV-positive patients. CD4 count (a measure of immune function) is a confounder: physicians prescribe AZT to patients with lower CD4 counts (indication bias — sicker patients get the drug), and lower CD4 count independently predicts mortality. But CD4 count is not a stable baseline characteristic — it changes over time, partly in response to AZT itself (the drug improves CD4). At any given follow-up visit, CD4 count is simultaneously: (a) a confounder for the effect of future treatment on mortality, because CD4 level at that visit will affect both whether more AZT is given and whether the patient dies; and (b) an intermediate outcome of prior AZT treatment, meaning it is partially on the causal pathway from earlier AZT exposure to the outcome. This dual status — **time-varying confounder that is also affected by prior exposure** — is what makes the problem structurally different from ordinary confounding.

The trap with standard regression is that it cannot resolve this duality. If you include current CD4 count as a covariate in a Cox regression model, you block part of the causal effect of AZT that works through improving CD4 — you are conditioning on a mediator, which biases the estimate of AZT's effect downward. But if you exclude it, the remaining confounding by CD4 biases the estimate upward (sicker patients got the drug). No choice in standard regression is correct. The problem is not technical but structural: standard regression assumes each variable is either a confounder (condition on it) or a mediator (don't), but time-varying confounders are both, sequentially, in the same dataset.

**Marginal structural models (MSMs)** solve this by reweighting observations rather than conditioning on the time-varying confounder directly. The logic: construct hypothetical pseudo-populations in which the probability of treatment at each visit is independent of the confounders. This is achieved by assigning **inverse probability of treatment weights (IPTW)** to each observation — a subject who was unlikely to receive treatment given their covariate history but did receive it gets up-weighted; one who was likely to receive treatment and did gets down-weighted. In the reweighted pseudo-population, the association between the time-varying confounder and treatment is broken, and the effect of treatment can be estimated without bias from a model that does not include the confounder at all. **G-estimation** provides an alternative using structural nested models that estimate counterfactual outcomes directly. Both methods require specifying a model for the probability of treatment given covariate history — a distinct modeling task from outcome modeling, and one that must be done carefully, as misspecification propagates directly into the causal estimate.