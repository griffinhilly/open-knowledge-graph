---
id: instrumental-variables
title: Instrumental Variables
domain: economics
course: econometrics
prerequisites:
- id: endogeneity
  type: hard
- id: causal-inference-econometrics
  type: soft
builds-toward:
- two-stage-least-squares
tags:
- IV
- instrument
- exclusion-restriction
- relevance
stage: formal-systems
status: draft
---

# Instrumental Variables

## Core Idea
An instrumental variable (IV) is a variable z that is correlated with the endogenous regressor x (relevance: Cov(z,x)≠0) but affects y only through x and not directly (exclusion restriction: Cov(z,u)=0). When both conditions hold, IV consistently estimates the causal effect of x on y even when OLS is biased. The IV estimator in the bivariate case is β̂ᵢᵥ = Cov(z,y)/Cov(z,x). Classic instruments include distance to college (for education), quarter of birth (for schooling), and rainfall (for agricultural income). The exclusion restriction is the unverifiable — and hence controversial — assumption; its plausibility must be argued on economic grounds.

## How It's Best Learned
Study the Angrist-Krueger (1991) quarter-of-birth instrument for education. Discuss why it is (arguably) excluded from the wage equation and what economic story justifies it.

## Common Misconceptions
- The exclusion restriction cannot be tested directly — it requires theoretical justification, not statistical proof.
- A 'weak instrument' (low Cov(z,x)) produces IV estimates that are biased toward OLS and have very wide confidence intervals.
