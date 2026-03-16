---
id: natural-experiments-identification-strategy
title: 'Natural Experiments: Quasi-Random Assignment for Causal Identification'
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: causal-inference-from-observation
  type: hard
- id: natural-experiments-design
  type: soft
- id: conditional-probability
  type: soft
builds-toward:
- regression-discontinuity-sharp-fuzzy
tags:
- natural-experiments
- quasi-random
- causal-identification
stage: advanced
status: draft
---

# Natural Experiments: Quasi-Random Assignment for Causal Identification

## Core Idea
Natural experiments exploit quasi-random variation in treatment assignment from policy changes or institutional rules. When assignment is plausibly independent of unmeasured confounders, they identify causal effects. Credibility depends on the plausibility of independence.

## Explainer

From causal inference with observational data, you know the core problem: treatment and control groups in naturally occurring data usually differ in ways that are correlated with outcomes, making it impossible to isolate the effect of the treatment. Natural experiments don't solve this by randomizing — a researcher didn't design them. Instead, they find situations where the world, through chance or administrative rule, *effectively* randomized treatment. The causal credibility of the study rides entirely on the plausibility of that claim.

The canonical example is the Vietnam-era draft lottery. To study the effects of military service on later-life earnings, economists couldn't randomly assign men to serve — that happened decades ago. But the draft lottery in 1969 literally randomized eligibility by birth date. Men born on dates randomly drawn early were much more likely to serve than those drawn late. This lottery assignment is a natural experiment: men with low lottery numbers didn't choose to have low lottery numbers, so their pre-lottery characteristics should be statistically indistinguishable from men with high lottery numbers. Any difference in later outcomes can be attributed to the difference in military service exposure. The economist Joshua Angrist used exactly this design to estimate the earnings effect of Vietnam service.

What makes a natural experiment credible isn't just that assignment *happened* to look quasi-random — you have to argue it *was* quasi-random for reasons that don't also affect the outcome through other paths. This is the **exclusion restriction**: the quasi-random assignment affects outcomes *only through* the treatment channel you're studying. If lottery numbers had been correlated with geography, and geography affected earnings through other mechanisms, the design would be compromised. Researchers document this by showing that pre-treatment characteristics are balanced across treatment and control groups — exactly as you'd check in a randomized experiment.

Several institutional patterns reliably generate natural experiments. **Cutoff rules** — age eligibility for programs, test score thresholds for selective schools, income limits for benefits — create sharp discontinuities where people just above and just below a threshold are nearly identical except for treatment status. This is the logic of **regression discontinuity design**: estimate the treatment effect by comparing outcomes in a narrow band around the cutoff, where assignment is as good as random. **Policy rollouts** that are phased in across regions or time create quasi-experimental variation: regions treated earlier can be compared to those treated later on observable outcomes. **Geographic boundaries** sometimes generate natural experiments when similar populations face different policies on either side of a border.

The key distinction from standard observational analysis is that in a natural experiment you are not primarily controlling for observable confounders through regression — you are arguing that the quasi-random assignment mechanism has already eliminated confounding, observable and unobservable alike. This is a much stronger claim, and it requires a much more specific argument about the particular institutional or chance mechanism that generated the variation. The credibility of the identification strategy is the thing being defended, and it must be defended substantively, not just statistically. Strong natural experiments are rare and valuable precisely because the conditions for quasi-random assignment are hard to find in real social processes.
