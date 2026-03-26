---
id: overidentification-test
title: 'Test of Overidentification: Hansen J-Test'
domain: economics
course: econometrics
prerequisites:
- id: two-stage-least-squares
  type: hard
- id: reduced-form-equations
  type: soft
tags:
- instrumental-variables
- overidentification
- hypothesis-testing
stage: formal-systems
status: validated
---

# Test of Overidentification: Hansen J-Test

## Core Idea
The Hansen J-test checks whether extra instruments are exogenous. Under H₀ that E[Zᵢuᵢ] = 0, the statistic J = n · gₙ'Ŵ⁻¹gₙ ~ χ²₍ₘ₋ₖ₎, where m is the number of instruments and k is the number of endogenous regressors. Rejection suggests at least one instrument is invalid.

## Questions

```yaml
- question: "A researcher has one endogenous regressor and one instrument. They attempt to run the Hansen J-test. What happens?"
  type: multiple-choice
  options:
    - "The test runs normally with 1 degree of freedom"
    - "The test cannot be computed — there are zero overidentifying restrictions when m = k"
    - "The test runs but requires a heteroskedasticity correction"
    - "The test is equivalent to a standard t-test on the first-stage coefficient"
  answer: 1
  explanation: "The J-statistic has χ²(m − k) degrees of freedom. When m = k (just-identified), m − k = 0 — there are no surplus instruments to test. Every instrument has been used for identification and none remain as free restrictions to check against. The test is undefined in the just-identified case; overidentification is the prerequisite for running it."

- question: "A researcher uses quarter-of-birth and distance-to-college as instruments for education and finds the J-test rejects at the 5% level. What can they conclude?"
  type: multiple-choice
  options:
    - "Both instruments violate the exclusion restriction"
    - "The first stage is too weak to support IV estimation"
    - "At least one instrument correlates with the structural error, but the test cannot identify which one"
    - "The two instruments are collinear and cannot be used together"
  answer: 2
  explanation: "Rejection indicates that the instruments imply inconsistent estimates of β — a sign that at least one is correlated with the error term. But the J-test cannot decompose this into 'which instrument is the culprit.' Searching over instrument subsets until the test passes exploits in-sample correlation structure and is a form of specification search, not a solution."

- question: "Passing the J-test is sufficient evidence that most instruments satisfy the exclusion restriction."
  type: true-false
  answer: false
  explanation: "Passing the J-test is consistent with all instruments being valid, but it does not prove validity. The test only has power to detect deviations that produce inconsistency *between* instruments. If all instruments are biased in the same direction — for example, all correlated with omitted ability in a wage regression — the J-test will pass even though every instrument violates the exclusion restriction. The exclusion restriction remains untestable for the component shared by all instruments."

- question: "The Hansen J-test detects instrument invalidity by checking whether the 2SLS residuals are correlated with the instruments."
  type: true-false
  answer: true
  explanation: "If all instruments are valid (uncorrelated with the structural error u), they should be uncorrelated with the residuals from a consistent 2SLS estimator. The J-statistic is computed as n × R² from regressing 2SLS residuals on all instruments. If any instrument is invalid — correlated with u — it will also correlate with the residuals, inflating this R² and pushing J above the χ²(m − k) critical value."

- question: "Why can the J-test only be run in the overidentified case, and what does each additional instrument add to the test?"
  type: short-answer
  answer: "In the just-identified case (m = k), all instruments are used up to estimate the structural coefficients and there are no remaining degrees of freedom to test anything. Each additional instrument beyond the number of endogenous regressors adds one overidentifying restriction — one testable implication of joint instrument validity. A second instrument means you can check whether both instruments imply the same β estimate; if they don't, at least one is invalid. The J-test's power therefore grows with the number of extra instruments."
  explanation: "This is the fundamental tension in IV: you need instruments to achieve identification, but identification exhausts the instruments. Only surplus instruments can be tested. This is why researchers often seek more instruments than strictly necessary — overidentification allows at least a partial check on validity, which the just-identified case forbids entirely."
```

## Explainer

From your 2SLS prerequisite, you know the fundamental challenge: when regressor X is endogenous (correlated with the error u), OLS is biased. Instrumental variables solve this by finding Z that shifts X but affects outcome Y only through X — the **exclusion restriction**. The core identification challenge is that the exclusion restriction is an untestable assumption when you have exactly as many instruments as endogenous regressors (the **just-identified** case): you've used all your instruments to identify the coefficients, leaving no degrees of freedom to verify validity.

The **overidentified case** creates a testable implication. When you have more instruments than endogenous regressors (m > k), you have redundant instruments. If all instruments are truly valid — satisfying the exclusion restriction — they should each be uncorrelated with the structural error u and should all point toward the same estimate of β. The Hansen J-test exploits this: it takes the 2SLS residuals and tests whether the instruments help predict them. If instruments are valid, they should be uncorrelated with the residuals; if any instrument correlates with u, it will also correlate with the residuals, and the test detects this.

The **J-statistic** is computed as n times the R² from regressing 2SLS residuals on all instruments. Under the null that all instruments are valid, J ~ χ²(m − k), where the degrees of freedom equal the number of overidentifying restrictions — the excess instruments beyond what is needed for identification. With exactly one instrument and one endogenous variable, there are zero overidentifying restrictions and the J-test cannot be computed. Each additional instrument adds one testable restriction. Rejection at conventional significance levels is evidence that at least one instrument violates exogeneity.

The critical limitation is that **rejection identifies a problem but not the culprit**. The J-test tells you the set of instruments is collectively inconsistent with all being valid; it cannot tell you which instrument is the bad one. This matters because researchers sometimes respond to rejection by searching over instrument sets until the test passes — a form of specification search that exploits the in-sample correlation structure rather than testing a genuine prior. The correct response to rejection is to reconsider the economic argument for each instrument and potentially abandon the approach.

A concrete example: suppose you estimate the earnings return to education using both quarter of birth and distance to college as instruments. Both predict schooling in the first stage. If both are valid (exclusion restriction holds for both), J should not reject. But if distance to college reflects regional economic conditions that independently affect wages — a violation of the exclusion restriction — and quarter of birth is valid, the two instruments imply different estimates of the wage-education relationship. J detects this inconsistency. Passing the J-test is consistent with validity but does not prove it; the test only has power against deviations that differ across instruments.
