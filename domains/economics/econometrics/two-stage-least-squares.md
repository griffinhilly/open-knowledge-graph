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

## Explainer

You already know from instrumental variables that when the key regressor x is endogenous — correlated with the error term because of omitted variables, reverse causality, or measurement error — OLS produces biased and inconsistent estimates. An instrument z provides a solution: a variable that affects x (relevance) but affects the outcome y only through x (exclusion restriction). Two-stage least squares is the mechanical procedure for implementing this idea when you have one or more instruments in hand.

The **first stage** is an ordinary OLS regression: regress x on the instrument z (and all exogenous controls). This isolates the variation in x that is driven purely by the instrument — call it x̂. Because z is exogenous (uncorrelated with the error term by the exclusion restriction), x̂ is also exogenous. You have essentially purged x of its endogenous component, keeping only the "clean" variation attributable to z.

The **second stage** is another OLS regression: regress y on x̂ (plus the same controls). The coefficient on x̂ is your 2SLS estimate of the causal effect. The logic is clean: x̂ has been stripped of the problematic correlation with the error term, so regressing y on x̂ recovers an unbiased estimate of how x causally affects y. With multiple endogenous variables, you need at least as many instruments as endogenous regressors — the order condition for identification.

Two diagnostics are essential. First, the **first-stage F-statistic** tests instrument relevance: a weak instrument — one that explains little of the variation in x — creates a "weak instruments" problem where 2SLS estimates are severely biased toward OLS and standard errors explode. The rule of thumb F > 10 is a minimum threshold, not a guarantee of strength. Second, when you have more instruments than endogenous variables (overidentification), the **Hansen-Sargan J-test** provides a partial check on exclusion: if the instruments are valid, they should produce the same coefficient estimate regardless of which instrument you use. A significant J-test statistic suggests at least one instrument violates the exclusion restriction — though it cannot tell you which one, and a passing J-test does not prove validity.

The critical implementation note: if you run the two regressions manually in software, the point estimate in the second stage is correct, but the standard errors are wrong. The manual second-stage OLS ignores the sampling variability introduced in the first stage. Always use your software's dedicated IV or 2SLS estimation routine, which computes the correct asymptotic standard errors from the full 2SLS formula.
