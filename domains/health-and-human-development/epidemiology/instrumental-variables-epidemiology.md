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
- id: reproducibility-in-epidemiology
  type: soft
- id: causal-inference-in-epidemiology
  type: soft
builds-toward:
- mendelian-randomization
tags:
- causal-inference
- unmeasured-confounding
- two-stage-regression
stage: expert
status: validated
---
# Instrumental Variables in Epidemiology

## Core Idea
An instrumental variable (IV) is a variable that influences the exposure but does not directly affect the outcome except through the exposure. IV analysis can identify causal effects under unmeasured confounding if the IV satisfies relevance, exclusion, and monotonicity assumptions.

## How It's Best Learned
Begin with the conceptual framework (relevance, exclusion, monotonicity). Implement two-stage least squares and check IV strength using first-stage F-statistics. Examine sensitivity to violations of the exclusion restriction.

## Common Misconceptions
- Any variable correlated with exposure can serve as an IV (only variables unaffected by unmeasured confounders qualify). - IV analysis solves all confounding (it requires strong assumption about no direct effect on outcome). - Weak IVs are acceptable (weak IVs produce biased estimates; strong first-stage is essential).

## Questions

```yaml
- question: "A researcher uses proximity to a hospital as an IV for whether patients receive a particular surgery. This IV is invalid if:"
  type: multiple-choice
  options:
    - "Proximity to a hospital is only weakly correlated with receiving surgery"
    - "Living near a hospital also improves health outcomes through better access to emergency care, preventive services, and specialists — independent of the surgery"
    - "Some patients would always or never choose surgery regardless of proximity"
    - "The IV is too strongly correlated with the exposure, making the first-stage F-statistic too large"
  answer: 1
  explanation: "This violates the exclusion restriction: the IV must affect the outcome *only through the exposure*, not via any other pathway. If proximity to a hospital improves health through channels other than the specific surgery (better general care access), then the IV has a 'direct effect' on outcomes bypassing the exposure. This makes the IV estimate conflate the effect of surgery with the effect of broader hospital access. Option A describes a weak IV (problematic but a different failure); option C describes non-monotonicity (a separate assumption); option D is not a real problem."

- question: "A lottery randomly assigns job-seekers to a training program. Not all winners attend (some 'always-takers' would have found training elsewhere; some 'never-takers' refuse). An IV analysis using lottery assignment estimates the causal effect of training for:"
  type: multiple-choice
  options:
    - "The entire population of job-seekers who could benefit from training"
    - "Everyone assigned to training by the lottery, regardless of whether they attended"
    - "Compliers — those who attend training when assigned but would not otherwise"
    - "Never-takers, since their outcomes are unaffected by the lottery and serve as the control group"
  answer: 2
  explanation: "IV analysis identifies the Local Average Treatment Effect (LATE): the causal effect for compliers — those whose treatment status actually changes in response to the instrument. Always-takers (attend regardless) and never-takers (never attend regardless) do not contribute to the IV estimate because their behavior is unchanged by the instrument. This is a crucial distinction: the IV estimate may not generalize to the full population if compliers are systematically different from non-compliers."

- question: "The exclusion restriction — that the IV affects the outcome primarily through the exposure — is empirically testable using standard statistical methods."
  type: true-false
  answer: false
  explanation: "The exclusion restriction is fundamentally untestable from the data alone. It is an assumption about a counterfactual: what would happen to outcomes if the IV changed but the exposure did not? Since the exposure does change with the IV in the data, we cannot directly observe outcomes under the counterfactual condition. The assumption must be defended on subject-matter grounds — by arguing from theory and context that no direct pathway exists. Sensitivity analyses can probe how sensitive conclusions are to violations, but cannot verify the assumption itself."

- question: "A weak instrumental variable (low first-stage F-statistic) produces IV estimates that are biased toward the OLS estimate and highly imprecise."
  type: true-false
  answer: true
  explanation: "This is a critical practical limitation. A weak IV — one only loosely correlated with the exposure — isolates very little variation in the exposure. In finite samples, even small violations of the IV assumptions or chance correlations with confounders can dominate the estimate, pulling it toward the confounded OLS result. The first-stage F-statistic < 10 is a conventional warning sign. Strong relevance (high F-statistic) does not guarantee the IV is valid (exclusion restriction could still fail), but weakness guarantees problems."

- question: "Why does IV analysis typically estimate the Local Average Treatment Effect (LATE) rather than the Average Treatment Effect (ATE), and why does this distinction matter for interpreting results?"
  type: short-answer
  answer: "IV analysis estimates LATE because the instrument only creates variation in treatment for compliers — people whose exposure status changes in response to the instrument. Always-takers (who receive the treatment regardless) and never-takers (who never receive it regardless) are unaffected by the instrument, so their counterfactual outcomes are not identified. LATE is the effect among this specific subgroup. The distinction matters because compliers may be systematically different from the full population: if a schooling law IV only changes behavior for marginal students near the minimum age threshold, the estimated return to education applies to that group and may not generalize to students who would have stayed in school regardless."
  explanation: "The LATE vs. ATE distinction is one of the most important interpretive issues in IV analysis. Policy-makers often want the ATE — what would happen if we universally applied the treatment — but IV gives LATE, which applies only to those whose behavior the instrument actually shifts. The complier subgroup is often not directly observed and may be smaller or different from the broader population. Recognizing this limits the scope of causal claims from IV studies and motivates thinking carefully about external validity."
```

## Explainer

From your study of confounding and the counterfactual framework, you know the central challenge of observational epidemiology: the people who receive an exposure are systematically different from those who do not, and those differences — not just the exposure — may explain differences in outcomes. Standard regression adjustment controls for measured confounders, but **unmeasured confounders** remain a fundamental threat. Suppose you want to estimate the effect of educational attainment on adult health outcomes. People who stay in school longer differ from school leavers in family background, neighborhood, cognitive ability, and motivation — factors that are hard to fully measure and adjust for. An instrumental variable offers an exit from this problem by finding a natural experiment embedded in your data.

An **instrumental variable (IV)** is a variable that meets three conditions. First, **relevance**: it must be associated with the exposure. Second, **exclusion restriction**: it must affect the outcome only through the exposure, not through any other pathway. Third, **independence** (sometimes called exogeneity): it must be unrelated to the unmeasured confounders. If all three hold, the IV acts as a natural randomizer — individuals with different values of the IV end up with different exposure levels for reasons unrelated to their confounding characteristics. In the education example, a classic IV is **compulsory schooling laws**: the legal minimum school-leaving age varies across states and birth cohorts, creating quasi-random variation in years of education that is unrelated to individual motivation or family background.

The estimation procedure is typically **two-stage least squares (2SLS)**. In the first stage, you regress the exposure on the IV (and any covariates), generating fitted values of the exposure that reflect only the variation driven by the IV. In the second stage, you regress the outcome on those fitted values. Because the fitted values contain only IV-driven variation — which is by assumption unconfounded — the second-stage coefficient recovers a causal estimate. The IV estimator identifies the **local average treatment effect (LATE)**: the causal effect specifically among **compliers**, individuals whose exposure actually changes in response to the IV. Non-compliers (people who would always receive the exposure or never receive it regardless of the IV) do not contribute to the estimate, which is why IV estimates can differ substantially from average treatment effects in the population.

The practical challenges of IV analysis are significant. **IV strength** — how strongly the instrument predicts the exposure — is critical. A weak IV (small first-stage F-statistic, conventionally < 10) produces highly imprecise estimates and, worse, estimates that are biased in the same direction as OLS. The exclusion restriction is the most vulnerable assumption, because it is fundamentally untestable: you cannot directly verify that the IV has no direct effect on the outcome, only argue for it from subject-matter knowledge. Sensitivity analyses that ask "how large would a violation of the exclusion restriction need to be to reverse our conclusion?" help communicate robustness. Despite these limitations, IV analysis remains one of the most powerful tools for causal inference from observational data, and its logic extends directly to its most prominent epidemiological application: **Mendelian randomization**, where genetic variants serve as instruments for modifiable exposures.
