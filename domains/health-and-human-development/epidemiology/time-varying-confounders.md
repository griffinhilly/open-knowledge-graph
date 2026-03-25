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
- id: time-varying-exposures-and-covariates
  type: soft
builds-toward:
- marginal-structural-models
tags:
- longitudinal-analysis
- time-varying-confounding
- exposure-dynamics
stage: expert
status: validated
---
# Time-Varying Confounders and Longitudinal Exposure

## Core Idea
Time-varying confounding occurs when a variable is a confounder at some timepoint but is also affected by prior exposure. Standard regression adjustment introduces bias because adjusting for a mediator of prior exposure induces collider bias. Methods like marginal structural models or g-estimation handle this scenario.

## Questions

```yaml
- question: "A study of AZT and HIV survival includes CD4 count as a time-varying covariate in a Cox regression model. CD4 count is affected by prior AZT and also independently predicts mortality. What bias does this introduce?"
  type: multiple-choice
  options:
    - "No bias — including more covariates always reduces confounding"
    - "Upward bias only, because sicker patients received more AZT"
    - "Collider bias by conditioning on a mediator — blocking part of AZT's causal effect through CD4 improvement while still failing to fully adjust for confounding"
    - "Measurement error bias, because CD4 count is imprecisely measured"
  answer: 2
  explanation: "CD4 count at each follow-up visit is simultaneously a confounder for future treatment (sicker patients get more AZT) and an intermediate outcome of past treatment (AZT improves CD4). Conditioning on it in regression blocks the causal pathway from prior AZT through CD4 improvement to survival — this is conditioning on a mediator and biases the treatment effect estimate downward. But omitting it leaves the confounding by CD4 unaddressed, biasing upward. No choice in standard regression resolves both problems simultaneously."

- question: "Why does time-varying confounding create a structural problem that standard regression adjustment cannot solve, even in principle?"
  type: multiple-choice
  options:
    - "Because regression models cannot include more than one covariate measured at multiple time points"
    - "Because time-varying confounders are always unmeasured in practice"
    - "Because the same variable is both a confounder (for future exposure) and a mediator (of past exposure), so conditioning on it is simultaneously required and prohibited"
    - "Because survival analysis methods like Cox regression do not allow time-varying covariates"
  answer: 2
  explanation: "Standard regression divides variables into confounders (condition on them) and mediators (do not condition on them). A time-varying confounder that is also affected by prior exposure belongs to both categories sequentially: it must be conditioned on to remove confounding for future treatment assignments, but doing so blocks the causal effect of prior exposure. This is a structural, not technical, limitation. Cox regression can include time-varying covariates; the issue is not a modeling constraint but a causal identification problem."

- question: "Marginal structural models handle time-varying confounding by including all time-varying covariates directly as predictors in the outcome model."
  type: true-false
  answer: false
  explanation: "Marginal structural models solve the problem by *reweighting* observations rather than conditioning on time-varying covariates. Each subject is assigned an inverse probability of treatment weight (IPTW) based on their covariate history, creating a pseudo-population in which treatment assignment is independent of confounders. The outcome model is then fit in this reweighted pseudo-population without including the time-varying confounder as a covariate. Including the time-varying confounder as a predictor is precisely the mistake that standard regression makes."

- question: "A time-varying confounder is structurally different from a baseline confounder because it can simultaneously be a confounder for future exposure and an intermediate outcome of past exposure."
  type: true-false
  answer: true
  explanation: "This is the defining characteristic of time-varying confounding. A baseline confounder measured before any exposure begins can only be a confounder — it cannot be caused by the exposure. A time-varying covariate that changes during follow-up can be affected by prior exposure while also affecting future exposure and the outcome. It is this temporal dual role — caused by past exposure, causing future treatment decisions and the outcome — that standard regression cannot accommodate."

- question: "Why does marginal structural model estimation require correctly specifying a model for the *probability of treatment* rather than a model for the *outcome*, and what happens if this model is misspecified?"
  type: short-answer
  answer: "MSMs work by assigning inverse probability of treatment weights (IPTW) to each observation based on their probability of receiving their actual treatment given their covariate history. The weights are derived from a treatment probability model, not the outcome model. If this treatment model is misspecified, the weights are wrong: they fail to fully break the association between confounders and treatment in the pseudo-population, leaving residual confounding in the outcome estimate. The causal estimate then depends directly on how well the treatment model is specified."
  explanation: "This is a crucial practical point: MSMs shift the modeling burden from the outcome equation to the treatment equation. The analyst must correctly model how treatment was assigned given covariates at each time point. Misspecification of this propensity model propagates into the weights and thus into all downstream causal estimates. This is analogous to how standard regression requires correctly specifying the outcome model — you have traded one modeling assumption for another, though the MSM assumption is often more tractable when the causal structure is well-understood."
```

## Explainer

From your study of confounding, you know the three criteria: a confounder must be associated with the exposure, associated with the outcome independently of the exposure, and must not lie on the causal pathway between them. You also know the solution: measure the confounder and adjust for it using stratification or regression. This works well when confounders are stable baseline characteristics. Time-varying confounding is the complication that arises in longitudinal studies when a covariate changes during follow-up — and when its value at any point is partly caused by the prior exposure history.

The canonical example comes from HIV treatment research. Suppose you want to know whether early AZT treatment prolongs survival in HIV-positive patients. CD4 count (a measure of immune function) is a confounder: physicians prescribe AZT to patients with lower CD4 counts (indication bias — sicker patients get the drug), and lower CD4 count independently predicts mortality. But CD4 count is not a stable baseline characteristic — it changes over time, partly in response to AZT itself (the drug improves CD4). At any given follow-up visit, CD4 count is simultaneously: (a) a confounder for the effect of future treatment on mortality, because CD4 level at that visit will affect both whether more AZT is given and whether the patient dies; and (b) an intermediate outcome of prior AZT treatment, meaning it is partially on the causal pathway from earlier AZT exposure to the outcome. This dual status — **time-varying confounder that is also affected by prior exposure** — is what makes the problem structurally different from ordinary confounding.

The trap with standard regression is that it cannot resolve this duality. If you include current CD4 count as a covariate in a Cox regression model, you block part of the causal effect of AZT that works through improving CD4 — you are conditioning on a mediator, which biases the estimate of AZT's effect downward. But if you exclude it, the remaining confounding by CD4 biases the estimate upward (sicker patients got the drug). No choice in standard regression is correct. The problem is not technical but structural: standard regression assumes each variable is either a confounder (condition on it) or a mediator (don't), but time-varying confounders are both, sequentially, in the same dataset.

**Marginal structural models (MSMs)** solve this by reweighting observations rather than conditioning on the time-varying confounder directly. The logic: construct hypothetical pseudo-populations in which the probability of treatment at each visit is independent of the confounders. This is achieved by assigning **inverse probability of treatment weights (IPTW)** to each observation — a subject who was unlikely to receive treatment given their covariate history but did receive it gets up-weighted; one who was likely to receive treatment and did gets down-weighted. In the reweighted pseudo-population, the association between the time-varying confounder and treatment is broken, and the effect of treatment can be estimated without bias from a model that does not include the confounder at all. **G-estimation** provides an alternative using structural nested models that estimate counterfactual outcomes directly. Both methods require specifying a model for the probability of treatment given covariate history — a distinct modeling task from outcome modeling, and one that must be done carefully, as misspecification propagates directly into the causal estimate.