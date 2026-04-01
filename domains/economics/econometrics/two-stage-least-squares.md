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
- id: linear-transformations
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

## Questions

```yaml
- question: "A researcher manually runs two OLS regressions to implement 2SLS: first regressing x on instrument z to get x̂, then regressing y on x̂. She reports the standard errors from the second OLS regression as her 2SLS standard errors. What is wrong with this procedure?"
  type: multiple-choice
  options:
    - "The point estimate of the causal effect is also biased when 2SLS is run manually"
    - "The second-stage OLS standard errors are correct only if the first-stage R² exceeds 0.5"
    - "The standard errors from manual second-stage OLS are incorrect — they ignore the sampling variability introduced in the first stage and will typically be too small"
    - "The second stage should regress y on the original x, not on x̂"
  answer: 2
  explanation: "The point estimate is actually correct when 2SLS is run manually — that is why this error is so dangerous. The standard errors, however, are wrong. Manual second-stage OLS treats x̂ as if it were a fixed, known quantity, but x̂ itself was estimated from data in the first stage. Ignoring that estimation uncertainty understates the true standard errors, leading to t-statistics that are too large and confidence intervals that are too narrow — making results appear more precise than they are. Always use dedicated IV/2SLS software routines that compute the correct asymptotic standard errors."

- question: "A researcher reports a first-stage F-statistic of 4.2 when using a single instrument for an endogenous regressor. What is the key concern about the 2SLS estimates?"
  type: multiple-choice
  options:
    - "The instrument may violate the exclusion restriction, as indicated by the low F-statistic"
    - "The instrument is weak — it explains too little variation in x, so 2SLS estimates are severely biased toward OLS with inflated standard errors"
    - "The overidentification test will necessarily fail with a low first-stage F-statistic"
    - "The second stage cannot be run if the first-stage F-statistic falls below 10"
  answer: 1
  explanation: "The first-stage F-statistic tests instrument relevance — how much variation in the endogenous variable x does the instrument explain? With F = 4.2 (well below the rule-of-thumb threshold of 10), the instrument is weak. Weak instruments cause 2SLS to perform poorly in finite samples: estimates are biased toward OLS (which has the original endogeneity problem), and standard errors become unreliable. Note that a low F-statistic does not indicate exclusion restriction violation — that is a separate issue that F-stat cannot detect."

- question: "Having more instruments than endogenous variables (overidentification) allows the researcher to fully verify that most instruments satisfy the exclusion restriction via the Hansen-Sargan J-test."
  type: true-false
  answer: false
  explanation: "The J-test provides only a partial check. It tests whether all instruments yield the same coefficient estimate — if one instrument is invalid (correlated with the error), using it alone would produce a different estimate than using the others. A significant J-test flags inconsistency among instruments. However, the test cannot identify which instrument is invalid, and crucially, if all instruments are invalid in the same direction, the J-test may not detect the problem at all. A passing J-test is not proof of validity — it is merely absence of detected inconsistency."

- question: "The first stage of 2SLS isolates the exogenous variation in the endogenous variable x by regressing x on the instrument z, producing fitted values x̂ that are uncorrelated with the error term."
  type: true-false
  answer: true
  explanation: "This is the core logic of 2SLS. The endogenous variable x is contaminated — it is correlated with the error term through omitted variables or reverse causality. By regressing x on the exogenous instrument z, the fitted values x̂ contain only the variation in x that is attributable to z. Since z is assumed exogenous (uncorrelated with the error term, by the exclusion restriction), x̂ inherits that exogeneity. The second stage then uses x̂ as if it were a clean, exogenous regressor."

- question: "Why does 2SLS produce unbiased causal estimates when OLS does not, and what role does the first stage play?"
  type: short-answer
  answer: "OLS regresses y on the endogenous x, which is correlated with the error term — so OLS picks up both the causal effect of x and the confounding relationship. The first stage purges the problem by regressing x on the exogenous instrument z; the fitted values x̂ contain only the variation in x driven by z, which is uncorrelated with the error term (by the exclusion restriction). When the second stage regresses y on x̂, it uses only this clean variation, recovering the causal effect of x without confounding. The endogenous component of x is left behind in the first-stage residuals."
  explanation: "The key intuition: z shifts x for reasons unrelated to the omitted confounders. By 'following' only the variation in x caused by z, 2SLS recovers the effect of x on y through a channel that is free of the bias afflicting OLS. This is why instrument relevance (z actually moves x) and the exclusion restriction (z affects y only through x) are both necessary conditions."
```

## Explainer

You already know from instrumental variables that when the key regressor x is endogenous — correlated with the error term because of omitted variables, reverse causality, or measurement error — OLS produces biased and inconsistent estimates. An instrument z provides a solution: a variable that affects x (relevance) but affects the outcome y only through x (exclusion restriction). Two-stage least squares is the mechanical procedure for implementing this idea when you have one or more instruments in hand.

The **first stage** is an ordinary OLS regression: regress x on the instrument z (and all exogenous controls). This isolates the variation in x that is driven purely by the instrument — call it x̂. Because z is exogenous (uncorrelated with the error term by the exclusion restriction), x̂ is also exogenous. You have essentially purged x of its endogenous component, keeping only the "clean" variation attributable to z.

The **second stage** is another OLS regression: regress y on x̂ (plus the same controls). The coefficient on x̂ is your 2SLS estimate of the causal effect. The logic is clean: x̂ has been stripped of the problematic correlation with the error term, so regressing y on x̂ recovers an unbiased estimate of how x causally affects y. With multiple endogenous variables, you need at least as many instruments as endogenous regressors — the order condition for identification.

Two diagnostics are essential. First, the **first-stage F-statistic** tests instrument relevance: a weak instrument — one that explains little of the variation in x — creates a "weak instruments" problem where 2SLS estimates are severely biased toward OLS and standard errors explode. The rule of thumb F > 10 is a minimum threshold, not a guarantee of strength. Second, when you have more instruments than endogenous variables (overidentification), the **Hansen-Sargan J-test** provides a partial check on exclusion: if the instruments are valid, they should produce the same coefficient estimate regardless of which instrument you use. A significant J-test statistic suggests at least one instrument violates the exclusion restriction — though it cannot tell you which one, and a passing J-test does not prove validity.

The critical implementation note: if you run the two regressions manually in software, the point estimate in the second stage is correct, but the standard errors are wrong. The manual second-stage OLS ignores the sampling variability introduced in the first stage. Always use your software's dedicated IV or 2SLS estimation routine, which computes the correct asymptotic standard errors from the full 2SLS formula.
