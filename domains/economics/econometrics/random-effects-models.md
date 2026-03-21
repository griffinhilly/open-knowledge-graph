---
id: random-effects-models
title: Random Effects Models
domain: economics
course: econometrics
prerequisites:
- id: fixed-effects-models
  type: hard
tags:
- random-effects
- GLS
- Hausman-test
- panel
stage: formal-systems
status: validated
---

# Random Effects Models

## Core Idea
The random effects (RE) model treats the unit-specific component α_i as a random variable drawn from a distribution, rather than a fixed unknown parameter. RE estimation uses Generalized Least Squares (GLS), which exploits both within-unit and between-unit variation, yielding more efficient estimates than FE when the key assumption holds: the individual effect α_i must be uncorrelated with the regressors. Unlike FE, RE can estimate the effects of time-invariant covariates. The Hausman test compares FE and RE estimates — a significant difference indicates the RE assumption is violated and FE is preferred.

## How It's Best Learned
Apply the Hausman test to a panel dataset, interpret the test result, and explain why FE is preferred when the null is rejected. Understanding what 'correlation between α_i and x_it' means economically is the key insight.

## Common Misconceptions
- Random effects does not mean the effects are random in a colloquial sense — it is a modeling assumption about the distribution of unit heterogeneity.
- The Hausman test rejects the null when RE is inconsistent, but a failure to reject does not guarantee RE is correct — it may just be low-powered.

## Questions

```yaml
- question: "A researcher studies wages with panel data and includes education as a regressor. More able workers tend to both earn more and get more education. Should the researcher use fixed or random effects, and why?"
  type: multiple-choice
  options:
    - "Random effects — education is correlated with wages, which is expected and not a problem"
    - "Fixed effects — individual ability (an unobserved unit characteristic) is likely correlated with education, violating the RE assumption and making RE inconsistent"
    - "Random effects — the Hausman test will confirm RE is consistent whenever education is included as a regressor"
    - "Fixed effects — because only FE can estimate the effect of education, which RE cannot"
  answer: 1
  explanation: "Individual ability is an unobserved unit-level characteristic (α_i). If more able workers get more education, then α_i (ability) is correlated with the education regressor — directly violating the RE assumption that α_i is uncorrelated with all regressors. RE would be inconsistent, absorbing ability into the error term that correlates with education, producing bias analogous to omitted variable bias in OLS. FE differences away α_i and remains consistent. Option D is wrong: FE cannot estimate time-invariant variables like gender, but education often does vary within-person over time."

- question: "The Hausman test produces a statistically significant result (rejecting the null). What does this imply?"
  type: multiple-choice
  options:
    - "Random effects is more efficient than fixed effects and should be preferred"
    - "The random effects assumption is violated — α_i is likely correlated with the regressors — and fixed effects should be preferred"
    - "Both estimators are biased and the model should be re-specified"
    - "The panel has too few time periods for random effects to be valid"
  answer: 1
  explanation: "Under the null hypothesis, both FE and RE are consistent but RE is more efficient — they should produce similar estimates. Under the alternative, RE is inconsistent (biased) because α_i correlates with regressors, while FE remains consistent. A significant divergence between the two estimates signals that RE is picking up correlated heterogeneity. Rejection means the RE assumption likely fails and FE is the correct choice. The test does not imply that both are biased."

- question: "Random effects models can estimate the coefficients of time-invariant variables (like country legal system or a person's gender), whereas fixed effects models cannot."
  type: true-false
  answer: true
  explanation: "Fixed effects works by absorbing unit-specific constants — any variable that doesn't change within a unit over time gets absorbed along with α_i and cannot be separately identified. Random effects treats α_i as part of the error term, leaving time-invariant regressors as separate covariates that can be estimated. This is a genuine practical advantage of RE: many important variables (legal origins, geographic features, demographic characteristics) don't vary within units over time."

- question: "Failing to reject the null in the Hausman test proves that the random effects assumption holds and RE is the correct estimator."
  type: true-false
  answer: false
  explanation: "A failure to reject does not prove RE is correctly specified — the test may simply be underpowered. The Hausman test detects large systematic divergences between FE and RE; subtle violations of the RE assumption may not produce a statistically significant test statistic. The test only tells you whether the data show strong evidence against RE; absence of evidence is not evidence of absence. As the literature notes, failure to reject may mean low power, not correct specification."

- question: "Explain in economic terms why the assumption that α_i is uncorrelated with the regressors is often implausible when studying people or firms."
  type: short-answer
  answer: "α_i captures stable, unobserved characteristics of each unit — ability, motivation, firm culture, management quality. These are often precisely the factors that drive observable choices: more able workers get more education, more motivated workers work longer hours, better-managed firms invest more. If unobservables and covariates co-evolve through individual decisions, α_i and the regressors are correlated, violating the RE assumption."
  explanation: "The RE assumption essentially requires that unit-level unobservables are as good as randomly assigned with respect to the covariates — ruling out selection effects. Most economic decisions involve agents acting on private information (their own ability, preferences, circumstances), which is precisely what α_i captures. Since people and firms choose their covariates partly based on their unobservables, the independence assumption fails in most economic applications. This is why FE, which makes no such assumption, is generally preferred when unobserved heterogeneity is a concern."
```

## Explainer

You already know fixed effects (FE) models, which handle unit heterogeneity by absorbing α_i — the stable, unobserved characteristics of each unit — as unit-specific constants that get differenced away. FE is consistent regardless of whether those unobserved characteristics are correlated with your regressors, and that is its great virtue. Its great cost is that it discards all between-unit variation and cannot estimate coefficients on time-invariant variables (like a country's legal system or a person's gender). The **random effects model** is the alternative that attempts to recover that lost efficiency and information, at the price of an additional assumption.

Where FE treats α_i as a fixed constant to be estimated, RE treats it as a **random draw from a distribution** — specifically, as part of a composite error term vᵢₜ = α_i + uᵢₜ. Because α_i is now in the error, the estimator uses **Generalized Least Squares (GLS)**, which accounts for the fact that observations on the same unit share a common component (α_i) and are therefore correlated. GLS is more efficient than OLS or the within-estimator when the model is correctly specified, using both the variation within units over time and the variation between units across the sample.

The critical assumption that unlocks this efficiency gain is that **α_i is uncorrelated with all regressors**. Think about what this requires economically. If you are studying wages and include education as a regressor, RE assumes that unobserved individual ability (the α_i) is uncorrelated with education. That is a strong claim — more able people typically get more education, so ability and education are correlated. When this assumption fails, the RE estimator is inconsistent for the same reason that omitting a variable correlated with the regressor biases OLS. FE does not make this assumption and remains consistent.

The **Hausman test** operationalizes this comparison. Under the null hypothesis, RE is correctly specified — α_i is uncorrelated with regressors — and both FE and RE estimates converge to the same true parameter, but RE is more efficient. Under the alternative, RE is misspecified and its estimates are biased, while FE remains consistent. The test statistic measures the systematic divergence between the two estimators: if they differ substantially, RE is likely picking up correlated heterogeneity and FE should be preferred. A practical heuristic: use FE when you are worried about unobserved individual characteristics influencing your regressors (most economic applications involving people or firms), and use RE when panel structure is primarily a statistical efficiency consideration and unit effects are plausibly independent of the covariates.
