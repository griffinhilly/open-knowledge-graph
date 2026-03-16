---
id: overidentification-test
title: 'Test of Overidentification: Hansen J-Test'
domain: economics
course: econometrics
prerequisites:
- id: two-stage-least-squares-procedure
  type: hard
- id: reduced-form-equations
  type: soft
tags:
- instrumental-variables
- overidentification
- hypothesis-testing
stage: formal-systems
status: draft
---

# Test of Overidentification: Hansen J-Test

## Core Idea
The Hansen J-test checks whether extra instruments are exogenous. Under H₀ that E[Zᵢuᵢ] = 0, the statistic J = n · gₙ'Ŵ⁻¹gₙ ~ χ²₍ₘ₋ₖ₎, where m is the number of instruments and k is the number of endogenous regressors. Rejection suggests at least one instrument is invalid.

## Explainer

From your 2SLS prerequisite, you know the fundamental challenge: when regressor X is endogenous (correlated with the error u), OLS is biased. Instrumental variables solve this by finding Z that shifts X but affects outcome Y only through X — the **exclusion restriction**. The core identification challenge is that the exclusion restriction is an untestable assumption when you have exactly as many instruments as endogenous regressors (the **just-identified** case): you've used all your instruments to identify the coefficients, leaving no degrees of freedom to verify validity.

The **overidentified case** creates a testable implication. When you have more instruments than endogenous regressors (m > k), you have redundant instruments. If all instruments are truly valid — satisfying the exclusion restriction — they should each be uncorrelated with the structural error u and should all point toward the same estimate of β. The Hansen J-test exploits this: it takes the 2SLS residuals and tests whether the instruments help predict them. If instruments are valid, they should be uncorrelated with the residuals; if any instrument correlates with u, it will also correlate with the residuals, and the test detects this.

The **J-statistic** is computed as n times the R² from regressing 2SLS residuals on all instruments. Under the null that all instruments are valid, J ~ χ²(m − k), where the degrees of freedom equal the number of overidentifying restrictions — the excess instruments beyond what is needed for identification. With exactly one instrument and one endogenous variable, there are zero overidentifying restrictions and the J-test cannot be computed. Each additional instrument adds one testable restriction. Rejection at conventional significance levels is evidence that at least one instrument violates exogeneity.

The critical limitation is that **rejection identifies a problem but not the culprit**. The J-test tells you the set of instruments is collectively inconsistent with all being valid; it cannot tell you which instrument is the bad one. This matters because researchers sometimes respond to rejection by searching over instrument sets until the test passes — a form of specification search that exploits the in-sample correlation structure rather than testing a genuine prior. The correct response to rejection is to reconsider the economic argument for each instrument and potentially abandon the approach.

A concrete example: suppose you estimate the earnings return to education using both quarter of birth and distance to college as instruments. Both predict schooling in the first stage. If both are valid (exclusion restriction holds for both), J should not reject. But if distance to college reflects regional economic conditions that independently affect wages — a violation of the exclusion restriction — and quarter of birth is valid, the two instruments imply different estimates of the wage-education relationship. J detects this inconsistency. Passing the J-test is consistent with validity but does not prove it; the test only has power against deviations that differ across instruments.
