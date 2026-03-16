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

## Explainer

You already know that instrumental variables (IV) fix the endogeneity problem: when your regressor X is correlated with the error term u, OLS estimates are biased and inconsistent. The instrument Z works as a kind of surgical tool — it provides variation in X that is "clean" (uncorrelated with the error), allowing you to isolate the causal effect. But not every proposed instrument actually does this job. The two validity conditions are exactly the criteria that must hold for the surgery to work.

**Relevance** is the simpler condition to understand and test. It requires that Z actually moves X — that the instrument has real predictive power over the endogenous variable. Think of Angrist and Krueger's famous study of returns to education: they used quarter of birth as an instrument for years of schooling (because compulsory attendance laws interact with birth timing to create variation in how long you must stay in school). Quarter of birth must genuinely predict years of completed schooling, or it tells you nothing about education's effect on wages. You can test relevance directly with an F-statistic on the first stage regression of X on Z; the rule of thumb is F > 10. When instruments are **weak** (small F), 2SLS becomes badly behaved — in finite samples, it inherits OLS's bias, defeating the purpose of the whole exercise.

**Exogeneity** is the harder condition — and the one that cannot be formally tested with a single instrument. It requires that Z affects Y only through X, not through any back door. Quarter of birth must affect wages only by affecting education, not directly (say, because summer babies develop differently than winter babies in ways that independently affect earnings). This is called the **exclusion restriction**: Z is excluded from the structural equation for Y except via X. Exogeneity cannot be tested because the structural error u is unobservable — you're asserting a claim about something you can never directly see. This is why the strength of an IV study depends so heavily on the institutional knowledge and theoretical reasoning behind the instrument choice, not just statistics.

When you have more instruments than endogenous regressors, you can perform the **Sargan–Hansen overidentification test**, which checks whether the instruments give consistent estimates of each other. Passing this test is weak evidence for exogeneity — it only tells you the instruments are mutually consistent, not that any of them is truly exogenous. In practice, evaluating an IV study means scrutinizing the story: is there a credible reason why Z affects X but has no independent pathway to Y? The two conditions together define the narrow corridor through which valid causal inference with observational data must pass.
