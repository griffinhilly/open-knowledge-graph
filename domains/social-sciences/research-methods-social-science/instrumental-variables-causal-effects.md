---
id: instrumental-variables-causal-effects
title: 'Instrumental Variables: Exogenous Variation for Causal Estimation'
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: instrumental-variables-methods
  type: hard
- id: causal-inference-from-observation
  type: soft
tags:
- instrumental-variables
- iv
- endogeneity
- 2sls
stage: advanced
status: draft
---

# Instrumental Variables: Exogenous Variation for Causal Estimation

## Core Idea
Instrumental variable estimation addresses endogeneity—when predictors correlate with errors due to omitted variables, simultaneity, or measurement error. An instrument correlates with treatment but affects outcomes only through the treatment. IV produces consistent estimates under strict assumptions.

## Questions

```yaml
- question: "A researcher uses distance to college as an instrument to estimate the returns to education on wages. The IV estimate is 12% per year of schooling; the OLS estimate is 9%. The IV estimate is best interpreted as:"
  type: multiple-choice
  options:
    - "The average causal effect of education on wages for the full population"
    - "An upper bound on the true effect, since IV estimates are always larger than OLS when there is positive selection"
    - "The local average treatment effect (LATE) — the causal effect for compliers: people whose education was actually affected by their distance to college"
    - "A biased estimate, since the difference from OLS indicates the exclusion restriction has been violated"
  answer: 2
  explanation: "IV identifies the LATE — the causal effect specifically for compliers, those whose treatment (education) was changed by the instrument (distance to college). People who would always or never attend college regardless of distance don't contribute to identification. This subpopulation may have different returns to education than the general population, explaining why IV and OLS can differ. The IV estimate is not biased for its own estimand (LATE); it simply answers a narrower question. Options A and B mischaracterize what IV identifies; option D confuses the IV-OLS gap (which can be legitimate) with exclusion restriction violation."

- question: "Which condition for a valid instrument can be empirically tested, and which must be justified on theoretical grounds alone?"
  type: multiple-choice
  options:
    - "The exclusion restriction can be tested via the first-stage F-statistic; relevance requires theoretical justification"
    - "Both relevance and the exclusion restriction can be tested if enough instruments are available"
    - "Relevance can be tested empirically (first-stage F-statistic and regression); the exclusion restriction cannot be tested with data and requires theoretical justification"
    - "Neither condition can be empirically tested; both require prior theoretical commitment"
  answer: 2
  explanation: "Relevance — that the instrument predicts the treatment — is straightforwardly testable: run the first-stage regression and check the F-statistic on the excluded instrument (≥10 is the conventional threshold). The exclusion restriction — that the instrument affects the outcome *only* through the treatment — cannot be tested with data because it is an assertion about a counterfactual path. You cannot observe whether distance to college has any direct effect on wages independent of education. The Sargan-Hansen test provides partial evidence when multiple instruments are available (they should all point to the same estimate), but it still doesn't directly test exclusion."

- question: "IV estimates identify the causal effect of the treatment for compliers only — the subpopulation of people whose treatment status was actually changed by the instrument."
  type: true-false
  answer: true
  explanation: "This is the LATE (Local Average Treatment Effect) result. The instrument only moves the treatment for compliers — people who respond to variation in the instrument. Always-takers (who get the treatment regardless of the instrument) and never-takers (who don't, regardless) contribute no identification because their treatment status doesn't change. This means IV answers a specific, potentially narrow question about a specific subpopulation, and its estimate can differ substantially from ATE (average treatment effect) for the full population."

- question: "A high first-stage F-statistic (e.g., F = 25) on the excluded instrument confirms that the exclusion restriction holds, validating the instrument."
  type: true-false
  answer: false
  explanation: "The first-stage F-statistic tests only *relevance* — whether the instrument is a strong predictor of the treatment. A strong first stage says nothing about whether the exclusion restriction holds. An instrument can be highly relevant (strongly predicts treatment) while still violating the exclusion restriction (having a direct path to the outcome that bypasses the treatment). These are independent conditions. Confusing them is one of the most common errors in IV application."

- question: "Why can the exclusion restriction not be tested with data alone, and what does this imply about how researchers must justify their choice of instrument?"
  type: short-answer
  answer: "The exclusion restriction asserts that the instrument affects the outcome *only* through the treatment — there is no direct path from instrument to outcome. This is a claim about a counterfactual world: what would happen to wages if distance to college were changed but education were somehow held fixed? Since we cannot observe this counterfactual, no data analysis can directly test whether the direct path exists. Researchers must justify the exclusion restriction using prior knowledge, institutional logic, or domain theory — arguing why it is implausible that the instrument could affect the outcome through any other pathway. This is why instrument validity is an argumentative exercise, not a statistical one."
  explanation: "This is the fundamental epistemological constraint on IV. The identification strategy depends on an untestable assumption. Good IV papers spend substantial effort defending the exclusion restriction with contextual knowledge, placebo tests, and falsification exercises — not because these fully test exclusion, but because they make violations less plausible. The credibility of an IV estimate is only as good as this theoretical argument."
```

## Explainer

You already understand from causal inference that observational data is plagued by **endogeneity** — situations where the treatment variable correlates with the error term of the regression, making OLS estimates biased and inconsistent. The most common cause is an **omitted variable**: something that affects both who receives the treatment and what the outcome is. If you want to estimate the effect of education on wages but smarter people both get more education and earn more, a simple regression confounds the education effect with the ability effect. Instrumental variables offer a surgical solution to this problem.

The core intuition is to find a variable — the **instrument** — that provides a source of variation in the treatment that is unrelated to the confound. A valid instrument must satisfy two conditions. First, **relevance**: the instrument must actually affect the treatment (it must predict who gets more or less education). Second, **exclusion restriction**: the instrument must affect the outcome *only* through the treatment — it has no direct effect on wages except by changing education. The exclusion restriction is the harder condition, and it cannot be tested with data alone; it must be justified on theoretical grounds. A classic instrument for education is distance to college: students who grew up near colleges got more education (relevance), and distance to college affects earnings only because it affected educational attainment (exclusion restriction — at least plausibly).

**Two-stage least squares (2SLS)** is the standard estimation procedure. In the first stage, you regress the endogenous treatment variable on the instrument (and any controls), extracting the portion of treatment variation that is driven purely by the instrument. In the second stage, you use the predicted values from stage one — the "clean" variation — as the regressor in the outcome equation. The key insight is that this predicted treatment is, by construction, uncorrelated with the error term, because the instrument is uncorrelated with it. You have effectively purged the endogeneity.

IV estimates should be interpreted carefully. When the instrument only moves some people's treatment — those who comply with the instrument — the IV estimate identifies a **local average treatment effect (LATE)**: the causal effect for compliers, not for the full population. Someone who would get a college degree regardless of distance (always-taker) or would never get one regardless (never-taker) doesn't contribute identification. This means IV estimates can differ substantially from OLS even when OLS is valid for a different estimand — the estimates answer different questions about different subpopulations.

Practical IV application also faces the **weak instruments problem**: if the instrument only weakly predicts the treatment, the first-stage is noisy and second-stage estimates become very imprecise and can even be biased. The F-statistic on the excluded instrument in the first stage (conventionally ≥10 as a rule of thumb) is the primary diagnostic. When multiple instruments are available, overidentification tests like the Sargan-Hansen test provide some purchase on whether the exclusion restriction holds — if instruments are valid, they should all point to the same estimate. Together, these diagnostics discipline the application of what is one of the most powerful but also most assumption-dependent tools in the causal inference toolkit.
