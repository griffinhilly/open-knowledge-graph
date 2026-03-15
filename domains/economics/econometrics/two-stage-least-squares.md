---
id: two-stage-least-squares
title: Two-Stage Least Squares (2SLS)
domain: economics
course: econometrics
prerequisites:
- id: instrumental-variables
  type: hard
- id: multiple-regression-model
  type: hard
- id: linear-algebra
  type: hard
builds-toward: []
tags:
- 2SLS
- IV-estimation
- first-stage
- weak-instruments
stage: formal-systems
status: validated
---
# Two-Stage Least Squares (2SLS)

## Core Idea
Two-Stage Least Squares (2SLS) is the standard method for IV estimation with one or more instruments. In the first stage, regress the endogenous variable x on all instruments z and exogenous controls, obtaining fitted values x̂. In the second stage, regress y on x̂ and the controls — the coefficient on x̂ is the 2SLS estimate of the causal effect of x. The first-stage F-statistic (rule of thumb: F > 10) tests instrument relevance; a weak first stage inflates 2SLS standard errors severely. With multiple instruments, the overidentification J-test (Hansen-Sargan) provides a partial check on the exclusion restriction.

## How It's Best Learned
Implement 2SLS by hand (running two OLS regressions) and then compare to software IV output — note that the second-stage standard errors must be corrected and cannot be taken from the manual second-stage OLS.

## Common Misconceptions
- Manually running two OLS regressions gives the right point estimate but wrong standard errors; always use IV/2SLS software routines.
- Having more instruments than endogenous variables (overidentification) enables testing but not complete verification of validity.
