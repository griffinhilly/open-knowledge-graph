---
id: instrumental-variables-epidemiology
title: Instrumental Variables in Epidemiology
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: confounding-epidemiology
  type: hard
- id: counterfactual-framework
  type: hard
builds-toward:
- mendelian-randomization
tags:
- causal-inference
- unmeasured-confounding
- two-stage-regression
stage: advanced
status: draft
---

# Instrumental Variables in Epidemiology

## Core Idea
An instrumental variable (IV) is a variable that influences the exposure but does not directly affect the outcome except through the exposure. IV analysis can identify causal effects under unmeasured confounding if the IV satisfies relevance, exclusion, and monotonicity assumptions.

## How It's Best Learned
Begin with the conceptual framework (relevance, exclusion, monotonicity). Implement two-stage least squares and check IV strength using first-stage F-statistics. Examine sensitivity to violations of the exclusion restriction.

## Common Misconceptions
- Any variable correlated with exposure can serve as an IV (only variables unaffected by unmeasured confounders qualify). - IV analysis solves all confounding (it requires strong assumption about no direct effect on outcome). - Weak IVs are acceptable (weak IVs produce biased estimates; strong first-stage is essential).

## Explainer

From your study of confounding and the counterfactual framework, you know the central challenge of observational epidemiology: the people who receive an exposure are systematically different from those who do not, and those differences — not just the exposure — may explain differences in outcomes. Standard regression adjustment controls for measured confounders, but **unmeasured confounders** remain a fundamental threat. Suppose you want to estimate the effect of educational attainment on adult health outcomes. People who stay in school longer differ from school leavers in family background, neighborhood, cognitive ability, and motivation — factors that are hard to fully measure and adjust for. An instrumental variable offers an exit from this problem by finding a natural experiment embedded in your data.

An **instrumental variable (IV)** is a variable that meets three conditions. First, **relevance**: it must be associated with the exposure. Second, **exclusion restriction**: it must affect the outcome only through the exposure, not through any other pathway. Third, **independence** (sometimes called exogeneity): it must be unrelated to the unmeasured confounders. If all three hold, the IV acts as a natural randomizer — individuals with different values of the IV end up with different exposure levels for reasons unrelated to their confounding characteristics. In the education example, a classic IV is **compulsory schooling laws**: the legal minimum school-leaving age varies across states and birth cohorts, creating quasi-random variation in years of education that is unrelated to individual motivation or family background.

The estimation procedure is typically **two-stage least squares (2SLS)**. In the first stage, you regress the exposure on the IV (and any covariates), generating fitted values of the exposure that reflect only the variation driven by the IV. In the second stage, you regress the outcome on those fitted values. Because the fitted values contain only IV-driven variation — which is by assumption unconfounded — the second-stage coefficient recovers a causal estimate. The IV estimator identifies the **local average treatment effect (LATE)**: the causal effect specifically among **compliers**, individuals whose exposure actually changes in response to the IV. Non-compliers (people who would always receive the exposure or never receive it regardless of the IV) do not contribute to the estimate, which is why IV estimates can differ substantially from average treatment effects in the population.

The practical challenges of IV analysis are significant. **IV strength** — how strongly the instrument predicts the exposure — is critical. A weak IV (small first-stage F-statistic, conventionally < 10) produces highly imprecise estimates and, worse, estimates that are biased in the same direction as OLS. The exclusion restriction is the most vulnerable assumption, because it is fundamentally untestable: you cannot directly verify that the IV has no direct effect on the outcome, only argue for it from subject-matter knowledge. Sensitivity analyses that ask "how large would a violation of the exclusion restriction need to be to reverse our conclusion?" help communicate robustness. Despite these limitations, IV analysis remains one of the most powerful tools for causal inference from observational data, and its logic extends directly to its most prominent epidemiological application: **Mendelian randomization**, where genetic variants serve as instruments for modifiable exposures.
