---
id: instrumental-variables-validity
title: 'Instrumental Variables: Validity Assumptions'
domain: economics
course: econometrics
prerequisites:
- id: instrumental-variables
  type: hard
- id: endogenous-regressors-bias
  type: hard
builds-toward:
- two-stage-least-squares-procedure
tags:
- instrumental-variables
- exogeneity
- relevance
stage: formal-systems
status: draft
---

# Instrumental Variables: Validity Assumptions

## Core Idea
A valid instrument Z must satisfy: (1) Relevance—Cov(Z, X) ≠ 0; (2) Exogeneity—E[Zu] = 0. Weak instruments (low correlation with X) yield biased 2SLS estimates even in large samples. Exogeneity is untestable; justification rests on theory or research design.

## Questions

```yaml
- question: "A researcher uses quarter of birth as an instrument for years of schooling in a wage regression. The first-stage F-statistic is 3.2. What is the core problem with proceeding to 2SLS estimation?"
  type: multiple-choice
  options:
    - "A weak instrument always violates the exclusion restriction, making 2SLS inconsistent"
    - "In finite samples, weak instruments cause 2SLS to inherit OLS's endogeneity bias, defeating the purpose of IV"
    - "The F-statistic must exceed 100 for valid IV estimation; 3.2 is marginally too low"
    - "Weak instruments only bias 2SLS in small samples; with large samples the problem disappears"
  answer: 1
  explanation: "Weak instruments (the rule of thumb is F > 10 in the first stage) cause 2SLS to be nearly as biased as OLS, even in large samples. The whole point of IV is to use a 'clean' source of variation in X that is uncorrelated with the error. If the instrument barely moves X, the first stage adds little information, and the second stage estimate is dominated by the same endogeneity contaminating OLS. The bias does not disappear asymptotically with truly weak instruments — it remains a finite-sample problem that scale cannot fix."

- question: "A researcher has two instruments for one endogenous variable and runs the Sargan-Hansen overidentification test, which they pass. What does passing this test establish?"
  type: multiple-choice
  options:
    - "Both instruments are exogenous — the test directly confirms the exclusion restriction holds for each"
    - "The instruments are mutually consistent, but this does not confirm that any single instrument is truly exogenous"
    - "The instruments are relevant — a passing overidentification test implies strong first-stage F-statistics"
    - "The 2SLS estimates are unbiased in finite samples for this specification"
  answer: 1
  explanation: "The Sargan-Hansen test checks whether multiple instruments give mutually consistent estimates. If two instruments disagree about the coefficient on X, at least one must be invalid. But if they agree, it only means they tell the same story — not that either story is correct. If both instruments share the same violation of the exclusion restriction (both affect Y through the same back door), they can be mutually consistent and both wrong. Passing the test is weak, indirect evidence for exogeneity, not a confirmation of it."

- question: "The relevance condition for an instrumental variable can be tested empirically using the first-stage regression, but the exogeneity condition (exclusion restriction) cannot be directly tested when there is only one instrument."
  type: true-false
  answer: true
  explanation: "True. Relevance — Cov(Z, X) ≠ 0 — is directly testable: regress X on Z and check the F-statistic. The exogeneity condition — that Z affects Y only through X — requires knowing the structural error u, which is unobservable. You can't regress Z on u to test correlation between them. This is why the credibility of an IV study depends heavily on institutional knowledge and theoretical reasoning: you must argue from first principles that there is no plausible back-door path from Z to Y other than through X."

- question: "An instrument with a strong first-stage relationship (high F-statistic) guarantees that the 2SLS estimator is consistent, regardless of whether the exclusion restriction holds."
  type: true-false
  answer: false
  explanation: "False. Relevance and exogeneity are both necessary conditions for IV validity; neither alone is sufficient. A strong but endogenous instrument — one that correlates with the error term u through some direct effect on Y — will produce an inconsistent 2SLS estimate that does not converge to the true causal effect even in infinite samples. In fact, a strongly endogenous instrument can produce estimates that are worse than OLS because it amplifies the bias from the exclusion restriction violation. Strength (relevance) makes the estimator precise; cleanliness (exogeneity) makes it accurate."

- question: "Explain why the exclusion restriction cannot be directly tested, and what kinds of evidence researchers typically use to argue that an instrument satisfies it."
  type: short-answer
  answer: "The exclusion restriction requires that Z has no direct effect on Y except through X — formally, E[Zu] = 0 where u is the structural error term. Since u is unobservable (it contains all unmeasured determinants of Y), you cannot directly estimate Cov(Z, u). Researchers argue for the exclusion restriction using: (1) institutional knowledge — a detailed story about the mechanism by which Z affects X, with no plausible back-door to Y; (2) falsification tests using outcomes that should not be affected by Z if the restriction holds; (3) comparing IV estimates across subsamples where the back-door pathway should differ in magnitude; (4) overidentification tests when multiple instruments are available (though these only test mutual consistency). The exclusion restriction is ultimately a theoretical, not a statistical, claim."
  explanation: "This is why IV credibility is heavily linked to the quality of the 'story' behind the instrument. The best IV studies use quasi-experimental variation — natural experiments, policy discontinuities, or lottery assignments — where the exclusion restriction is credible by design rather than just by assumption."
```

## Explainer

You already know that instrumental variables (IV) fix the endogeneity problem: when your regressor X is correlated with the error term u, OLS estimates are biased and inconsistent. The instrument Z works as a kind of surgical tool — it provides variation in X that is "clean" (uncorrelated with the error), allowing you to isolate the causal effect. But not every proposed instrument actually does this job. The two validity conditions are exactly the criteria that must hold for the surgery to work.

**Relevance** is the simpler condition to understand and test. It requires that Z actually moves X — that the instrument has real predictive power over the endogenous variable. Think of Angrist and Krueger's famous study of returns to education: they used quarter of birth as an instrument for years of schooling (because compulsory attendance laws interact with birth timing to create variation in how long you must stay in school). Quarter of birth must genuinely predict years of completed schooling, or it tells you nothing about education's effect on wages. You can test relevance directly with an F-statistic on the first stage regression of X on Z; the rule of thumb is F > 10. When instruments are **weak** (small F), 2SLS becomes badly behaved — in finite samples, it inherits OLS's bias, defeating the purpose of the whole exercise.

**Exogeneity** is the harder condition — and the one that cannot be formally tested with a single instrument. It requires that Z affects Y only through X, not through any back door. Quarter of birth must affect wages only by affecting education, not directly (say, because summer babies develop differently than winter babies in ways that independently affect earnings). This is called the **exclusion restriction**: Z is excluded from the structural equation for Y except via X. Exogeneity cannot be tested because the structural error u is unobservable — you're asserting a claim about something you can never directly see. This is why the strength of an IV study depends so heavily on the institutional knowledge and theoretical reasoning behind the instrument choice, not just statistics.

When you have more instruments than endogenous regressors, you can perform the **Sargan–Hansen overidentification test**, which checks whether the instruments give consistent estimates of each other. Passing this test is weak evidence for exogeneity — it only tells you the instruments are mutually consistent, not that any of them is truly exogenous. In practice, evaluating an IV study means scrutinizing the story: is there a credible reason why Z affects X but has no independent pathway to Y? The two conditions together define the narrow corridor through which valid causal inference with observational data must pass.
