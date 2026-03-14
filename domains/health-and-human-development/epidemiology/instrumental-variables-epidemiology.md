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
