---
id: regression-discontinuity-advanced
title: Advanced Regression Discontinuity Design
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: regression-discontinuity-sharp-fuzzy
  type: hard
- id: causal-inference-observational-data
  type: soft
builds-toward:
- multi-dimensional-rdd
- spatial-discontinuity
tags:
- regression-discontinuity
- quasi-experimental
- causal
- nonparametric
stage: advanced
status: draft
---

# Advanced Regression Discontinuity Design

## Core Idea
Regression discontinuity design exploits threshold rules in policy assignment to estimate causal effects. When eligibility for treatment depends on crossing a cutoff (income threshold, test score, age), units just above and below the threshold are comparable except for treatment status. RDD requires no assumption of ignorability; instead, identification relies on the assumption that other determinants of the outcome vary smoothly across the threshold. Advanced RDD addresses multiple thresholds, bandwidth selection, and validity checks (density tests, covariate continuity).

## Questions

```yaml
- question: "An RDD study finds that students who just barely scored above a scholarship threshold (score ≥ 70) have significantly better 10-year earnings than students who just barely scored below it. A policy advisor argues this proves scholarships improve earnings for all students. The most important methodological objection is:"
  type: multiple-choice
  options:
    - "The running variable (test score) may have measurement error near the threshold"
    - "RDD identifies a local average treatment effect at the margin, which may not generalize to students far from the threshold"
    - "The bandwidth used was probably too narrow, causing high variance in the estimate"
    - "RDD cannot be used with continuous outcomes like earnings"
  answer: 1
  explanation: "The core limitation of RDD is that it identifies the treatment effect *only* for units near the cutoff — those on the margin of qualifying. Students who scored 70 vs. 69 are very similar to each other but may be very different from students who scored 50 or 90. The scholarship effect for marginal students need not equal the effect for strong students (who might have thrived without the scholarship) or very weak students (who might lack the preparation to benefit). Generalizing a local estimate to a population average requires strong additional assumptions that the design alone cannot support."

- question: "A researcher runs the McCrary density test on their RDD and finds a sharp spike in the density of the running variable just above the cutoff. What is the most concerning interpretation of this finding?"
  type: multiple-choice
  options:
    - "The outcome variable has a nonlinear relationship with the running variable near the threshold"
    - "The bandwidth is too wide, including observations where the treatment effect varies"
    - "Administrators or applicants may have manipulated the running variable to place units just above the threshold"
    - "The cutoff was chosen after the data were collected, introducing researcher degrees of freedom"
  answer: 2
  explanation: "A density spike just above the cutoff — but not below — is the signature of manipulation: someone has been sorting units to land just above the qualifying threshold (e.g., administrators rounding up test scores for borderline scholarship applicants). When this happens, units just above and below the cutoff are no longer comparable — those above have been selected for above-cutoff placement, while those below have not. This violates the as-if-random assignment assumption that makes RDD credible. The density test is specifically designed to detect this threat, which is why it is a core validity diagnostic rather than a formality."

- question: "In RDD, using a wider bandwidth always produces more accurate treatment effect estimates because more observations reduce sampling noise."
  type: true-false
  answer: false
  explanation: "Bandwidth involves a bias-variance tradeoff, not a monotonic improvement. Narrower bandwidths include only observations closest to the cutoff (where the as-if-random assumption is most credible) but use fewer data points, producing higher variance. Wider bandwidths add observations further from the cutoff, reducing variance but increasing bias — observations far from the threshold are weaker counterfactuals and require more extrapolation across the regression function. The optimal bandwidth minimizes mean squared error by balancing these two forces. Neither extreme is 'always better,' which is why the CCT bandwidth selector and sensitivity checks across bandwidths are standard practice."

- question: "RDD requires only that potential outcomes vary smoothly across the threshold — it does not require the full ignorability assumption needed by standard observational regression."
  type: true-false
  answer: true
  explanation: "This is RDD's key advantage over observational regression. Standard regression requires ignorability (no unobserved confounders), which is almost never fully credible. RDD requires only that the distribution of all other outcome-relevant variables changes smoothly at the cutoff — that there is no simultaneous jump in covariates at exactly the threshold. If this holds, any discontinuous jump in outcomes at the cutoff must be caused by the treatment, since everything else is varying smoothly. This is a weaker and more defensible assumption in many policy contexts, which is why RDD is considered a strong quasi-experimental design when implemented well."

- question: "Why might finding a statistically significant 'effect' at placebo cutoffs undermine confidence in a genuine RDD result at the true cutoff?"
  type: short-answer
  answer: "Placebo cutoff tests apply the RDD estimation at values of the running variable where no treatment discontinuity exists. Under a valid design, you should find no effect at these placebo values, because there is nothing at those points to cause a jump in outcomes. If effects appear at multiple placebo cutoffs, it suggests the outcome variable is inherently discontinuous or lumpy near those values — perhaps for unrelated reasons — and that the apparent 'effect' at the true cutoff may just reflect that underlying pattern rather than treatment. Strong RDD results should be accompanied by flat placebo distributions, which build the evidential case that the discontinuity at the true cutoff is genuinely caused by the treatment assignment rule."
  explanation: "Placebo tests belong to a broader class of validity diagnostics that build the 'no other explanation' argument for causal inference. Along with covariate continuity checks (verifying pre-determined baseline characteristics don't jump at the cutoff) and density tests (verifying no manipulation), they constitute the empirical argument that the design is identifying a causal effect rather than a coincidental pattern in noisy data. Running only the main estimate without validity diagnostics is considered inadequate practice in modern applied econometrics."
```

## Explainer

You've already grasped the core logic of RDD: when treatment assignment depends on crossing a threshold, units just above and below the cutoff are as-good-as randomly assigned near that threshold, and the jump in outcomes at the cutoff estimates the causal effect of treatment. This is powerful because it demands only one credible assumption — that other outcome determinants vary smoothly across the cutoff — rather than the full ignorability required by observational regression. Advanced RDD extends this logic to harder identification problems and more demanding validity requirements.

**Bandwidth selection** is where estimation becomes technically non-trivial. The RDD estimator works locally: you use only observations near the cutoff, where the as-if-random assumption is most credible. Observations far from the cutoff are informative about the regression function's shape but are weaker counterfactuals for units right at the threshold. The bandwidth trades off bias (wider bandwidth = more extrapolation = more potential bias) against variance (narrower bandwidth = fewer observations = more noise). The **Calonico-Cattaneo-Titiunik (CCT)** optimal bandwidth selector formalizes this tradeoff using a mean squared error criterion. In practice, researchers report estimates at the optimal bandwidth and check sensitivity by varying bandwidth width — results that evaporate at different bandwidths are fragile.

**Validity diagnostics** are not formalities — they constitute the empirical argument that your design is identifying a causal effect. The **McCrary density test** checks whether there is a discontinuity in the density of the running variable at the cutoff. If units can manipulate precisely which side of the threshold they fall on, the as-if-random assumption fails: the density would show a suspicious spike just above a scholarship cutoff if administrators are nudging borderline students over. **Covariate continuity tests** check that pre-determined baseline characteristics are continuous at the cutoff — a jump in prior income or age at the threshold (absent a theoretical explanation) signals contamination. **Placebo cutoff tests** apply the design at other values of the running variable where no treatment discontinuity exists; finding effects at placebo cutoffs suggests the real result may be spurious.

**Multiple thresholds** arise when a policy applies different treatments at several cutoffs — income brackets for different subsidy levels, test score thresholds for different program tracks. Each threshold yields a **local average treatment effect** (LATE) for the subpopulation near that specific cutoff, and these estimates need not agree: treatment effects may vary by the level of the running variable. Comparing estimates across thresholds reveals treatment effect heterogeneity and can test whether the running variable moderates the effect. The discipline throughout advanced RDD is remembering what you are identifying: an effect for units at the margin, not a population average. Whether that local effect generalizes beyond the threshold is a substantive question about mechanism — and it cannot be answered by the design alone.
