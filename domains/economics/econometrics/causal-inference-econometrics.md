---
id: causal-inference-econometrics
title: Causal Inference and the Identification Problem
domain: economics
course: econometrics
prerequisites:
- id: econometrics-intro
  type: hard
- id: omitted-variable-bias
  type: hard
- id: conditional-probability
  type: soft
builds-toward:
- potential-outcomes-framework
- difference-in-differences
- regression-discontinuity
tags:
- causality
- identification
- natural-experiment
- selection-bias
stage: formal-systems
status: validated
---

# Causal Inference and the Identification Problem

## Core Idea
Causal inference asks what would have happened to unit i had treatment status been different — the fundamental problem being that we only ever observe one potential outcome per unit. In economics, randomized controlled trials are rarely feasible, so identification relies on 'natural experiments': institutional rules, policy changes, or geographic discontinuities that create quasi-random variation in treatment. The identification strategy is the researcher's argument for why variation in the regressor of interest is as-good-as-random conditional on observables. All credible empirical economics papers lead with their identification strategy.

## How It's Best Learned
Read landmark natural experiment papers (Card-Krueger minimum wage, Angrist Vietnam draft lottery) to understand how economists construct identification arguments from non-experimental settings.

## Common Misconceptions
- Controlling for more covariates does not solve selection bias if the controls themselves are endogenous.
- 'As-good-as-random' does not mean literally random — it means the remaining variation in x is uncorrelated with potential outcomes.

## Questions

```yaml
- question: "A study finds a strong positive correlation between the number of hospitals in a city and its death rate. A researcher controls for city size and still finds the relationship. What is the most likely explanation?"
  type: multiple-choice
  options:
    - "Hospitals cause death — patients should avoid them"
    - "Selection bias: sicker people travel to cities with more hospitals, so the correlation reflects who chooses to go there, not the effect of hospitals on health"
    - "The regression controls have solved the identification problem"
    - "City size is the only confounder, so the controlled estimate is causal"
  answer: 1
  explanation: "This is a classic selection bias example. People who are severely ill seek out cities with major medical centers. The association picks up who selects into treatment (going to a hospital-dense city), not the causal effect of hospitals. Even with controls, if unobserved illness severity drives both location choice and death risk, the estimate remains confounded."

- question: "Adding more control variables to a regression always gets you closer to estimating a causal effect."
  type: true-false
  answer: false
  explanation: "Controls help only when they block backdoor paths between treatment and outcome. Controlling for a 'bad control' — a variable that is itself caused by the treatment, or a collider — can introduce new bias and move the estimate further from the truth. Identification is about the source of variation in the regressor, not the number of variables in the model."

- question: "Why do economists rely on 'natural experiments' rather than simply adding more control variables to estimate causal effects?"
  type: short-answer
  answer: "Natural experiments provide quasi-random variation in the treatment — like a policy that affected only one group — which breaks the link between treatment and unobserved confounders. Controls alone cannot eliminate bias from variables that were never measured."
  explanation: "The fundamental identification problem is that unobserved variables may simultaneously affect treatment status and the outcome. No set of observed controls can block these unobserved backdoor paths. A natural experiment (e.g., a lottery, a policy cutoff, a geographic boundary) generates variation in treatment that is, by design or circumstance, unrelated to potential outcomes — making the 'as-good-as-random' assumption defensible."
```

## Explainer

The fundamental problem of causal inference is a problem of missing data. When you ask whether a job training program raised someone's wages, you are really asking: what would that person's wages have been *without* the program? You can never observe both outcomes for the same person at the same time — they either took the program or they didn't. This is the potential outcomes framework: each unit has two potential outcomes (treated and untreated), but you only ever see one. The causal effect is the difference between these two outcomes, and it is fundamentally unobservable at the individual level.

The naive approach is to compare wages of program participants to wages of non-participants. But participants may differ from non-participants in countless ways before the program — they may be more motivated, better connected, or from wealthier backgrounds. This is selection bias: the people who select into treatment are not a random draw from the population. When you studied omitted variable bias, you learned that OLS estimates are biased when a variable that affects both treatment assignment and the outcome is left out of the model. Causal inference is largely the problem of dealing with this bias when the omitted variable cannot be measured or controlled for.

The gold standard solution is a randomized controlled trial: randomly assign treatment, so that treated and control groups are identical on average in all characteristics, observed and unobserved. But randomization is rarely feasible in economics — you cannot randomly assign someone to grow up in poverty, attend a particular school, or serve in a war. Economists therefore search for *natural experiments*: real-world situations that create quasi-random variation in treatment. The Vietnam draft lottery assigned men to military service based on birth dates drawn randomly — this gave economists as-good-as-random variation in military service to study its effects on earnings. Geographic borders, policy cutoffs, and sudden rule changes all create similar opportunities.

The identification strategy is the researcher's argument for why the variation they are exploiting is as-good-as-random. It is not enough to have a clever instrument or discontinuity — you must argue persuasively that the variation is uncorrelated with potential outcomes conditional on observables. Every credible empirical economics paper leads with this argument, and the quality of the identification strategy is the primary criterion on which the paper is judged.

A key subtlety: 'as-good-as-random' does not mean literally random. It means that, after conditioning on the variables you can observe, the remaining variation in treatment is unrelated to unobserved factors that affect the outcome. This is a substantive assumption about the world, not a statistical one — it cannot be tested directly, only argued on institutional or theoretical grounds. Learning to evaluate these arguments is the central skill of applied econometrics.

