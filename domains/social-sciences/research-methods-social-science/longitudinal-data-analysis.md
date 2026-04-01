---
id: longitudinal-data-analysis
title: Longitudinal and Panel Data Analysis
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: linear-regression-social-science
  type: hard
- id: matrices-intro
  type: soft
- id: covariance-between-random-variables
  type: soft
builds-toward:
- panel-data-fixed-effects
- time-series-cross-section
tags:
- longitudinal
- panel
- temporal
- multilevel
stage: advanced
status: validated
---

# Longitudinal and Panel Data Analysis

## Core Idea
Longitudinal analysis studies change within individuals or units over time, using data collected at multiple waves. Panel data combines the time-series dimension (same units measured repeatedly) with cross-sectional breadth (many units). These designs enable causal inference about within-unit change, lag effects, and dynamic feedback. Fixed-effects models eliminate time-invariant confounds; growth curve models characterize trajectories of change.

## Questions

```yaml
- question: "A researcher uses cross-sectional data to compare wages of job-training participants vs. non-participants. Her colleague argues that people who seek training may already be more motivated — and that this motivation independently raises wages. What does this critique identify?"
  type: multiple-choice
  options:
    - "A sampling error that can be fixed by collecting a larger cross-sectional sample"
    - "Selection bias: unmeasured stable traits may simultaneously cause training participation and higher wages"
    - "A measurement problem — wages are not accurately captured in cross-sectional surveys"
    - "Reverse causation — higher wages lead people to seek training, not the other way around"
  answer: 1
  explanation: "This is exactly why longitudinal data is needed. If motivated workers both seek training AND earn more, a cross-sectional comparison confounds the training effect with unmeasured motivation. A fixed-effects longitudinal analysis would compare each person's wages before vs. after training, eliminating stable traits like motivation — since they don't change over time — from the comparison. The fundamental issue is time-invariant confounding, not sample size or measurement error."

- question: "A researcher uses a fixed-effects panel model to study the effect of marriage on personal income. Which finding would NOT be estimable with this approach?"
  type: multiple-choice
  options:
    - "The average change in income that occurs in the years immediately after marriage"
    - "Whether the income boost from marriage differs by employment sector"
    - "Whether men earn more than women on average"
    - "Whether the income effect of marriage grows or shrinks over time"
  answer: 2
  explanation: "Fixed effects absorb all time-invariant unit-level characteristics — including sex, which does not change over time for a given person. Sex is perfectly collinear with the unit fixed effect and is therefore inestimable. This is the fundamental tradeoff of fixed-effects modeling: in exchange for eliminating all unmeasured stable confounders, you lose the ability to estimate the effects of any stable characteristic. The approach answers 'what changes when something changes within a person,' not 'how do stable traits relate to outcomes.'"

- question: "A fixed-effects model eliminates the need to control for any confounding variables when estimating a causal effect from panel data."
  type: true-false
  answer: false
  explanation: "False. Fixed effects only eliminate TIME-INVARIANT confounders — characteristics that remain constant for each unit across the observation period. Time-varying confounders (events that coincide with the treatment and change over time, such as job changes, health shocks, or policy shifts) are not absorbed by the fixed effect and must still be controlled for explicitly. The model controls for stable between-unit differences, not all possible confounding."

- question: "Non-random attrition from a longitudinal study can bias effect estimates even when the initial sample was randomly selected from the population."
  type: true-false
  answer: true
  explanation: "True. If participants who drop out of the study differ systematically from those who remain — especially if their likely outcome trajectories differ — then analyses based only on completers will not represent the original population. A study of a medical treatment where sicker patients are more likely to die or withdraw will leave a surviving sample that appears healthier than the true population, biasing estimates of treatment effectiveness. Random initial selection does not protect against this post-randomization bias; it must be addressed through modeling dropout or using inverse probability weighting."

- question: "What is the key advantage of a fixed-effects model over a cross-sectional regression for causal inference, and what is the cost of that advantage?"
  type: short-answer
  answer: "The advantage is that fixed effects eliminate all time-invariant unobserved confounders by comparing each unit to itself across time — the unit-specific intercept absorbs any stable characteristic, measured or not. The cost is that you cannot estimate the effect of any time-invariant predictor (such as sex, race, or country of birth), because these are perfectly collinear with the fixed effects and are differenced out of the estimation."
  explanation: "Cross-sectional regression can only control for observed covariates, leaving unmeasured stable traits as potential confounders. Fixed effects sidestep this by using within-unit variation as the identification strategy — mathematically equivalent to de-meaning each variable by the unit's own time-average before running OLS. The tradeoff defines when fixed effects are appropriate: when the research question concerns within-unit change and when unmeasured stable confounders are the primary threat to causal inference. Questions about stable between-unit differences (e.g., does gender affect wages?) require different designs."
```

## Explainer

Cross-sectional data — a single snapshot of many units — leaves an important question unanswered: when we observe differences between individuals, are those differences caused by the factors we measure, or do they reflect stable underlying characteristics we have not observed? A student who reads more may score higher on vocabulary tests, but is this because reading *causes* vocabulary growth, or because students who are already more intellectually capable do both? Cross-sectional data cannot distinguish these stories. Longitudinal data addresses this by following the same units across time, enabling you to observe *change* within individuals — and within-unit change eliminates everything stable about a person from the comparison.

The workhorse of panel causal inference is the **fixed-effects model**. The logic extends directly from your understanding of linear regression: instead of comparing individuals to each other, you compare each individual to themselves across time. Formally, a unit-specific intercept (the "fixed effect") absorbs all time-invariant unobserved characteristics. If person A is always more productive than person B due to some unmeasured trait — intelligence, conscientiousness, social capital — the fixed effect captures this and removes it from the estimation. What remains is within-unit variation over time, and it is this variation that identifies the causal effect of time-varying predictors. The tradeoff is that you cannot estimate the effect of stable variables (race, sex, country of birth) since these are perfectly collinear with the fixed effects. The fixed-effects estimator is mathematically equivalent to de-meaning each variable by the unit's own time-average before running OLS — a connection your regression background makes tractable.

**Growth curve models** (also called latent trajectory or random-effects growth models) approach the panel structure differently. Rather than eliminating between-unit variation, they model it explicitly. Each unit follows its own trajectory over time, described by a linear or polynomial function: an intercept (initial status) and one or more slopes (rates of change). These individual-level parameters are treated as random variables drawn from a population distribution — hence "random effects." This lets you ask richer questions: not just "what is the average effect of X?" but "do different subgroups follow different trajectories?" and "what predicts who has a steeper growth curve?" Growth curve models require stronger distributional assumptions than fixed-effects models but yield far more information about heterogeneous change processes. Your understanding of covariance between random variables becomes essential here: the model must specify how intercepts and slopes covary across individuals, and the structure of that covariance encodes substantively important assumptions about how trajectories are organized.

The practical challenge that distinguishes longitudinal analysis from cross-sectional work is **attrition** — units that leave the study over time. If dropout is random (completely unrelated to the variables in the model), estimates remain unbiased though precision declines. If dropout is related to the outcome trajectory — sicker patients die and leave, students who are struggling drop out of school — the survivors are systematically unrepresentative, and analyses based only on completers produce biased estimates. Handling non-random attrition requires either modeling the dropout process explicitly (using variables that predict departure) or using inverse probability weighting to upweight units whose characteristics resemble those who left. This connects back to the core logic of causal inference: the key question is always whether the comparison group represents the counterfactual, and attrition can undermine this just as badly as cross-sectional confounding can.
