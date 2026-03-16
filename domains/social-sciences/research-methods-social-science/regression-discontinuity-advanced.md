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

## Explainer

You've already grasped the core logic of RDD: when treatment assignment depends on crossing a threshold, units just above and below the cutoff are as-good-as randomly assigned near that threshold, and the jump in outcomes at the cutoff estimates the causal effect of treatment. This is powerful because it demands only one credible assumption — that other outcome determinants vary smoothly across the cutoff — rather than the full ignorability required by observational regression. Advanced RDD extends this logic to harder identification problems and more demanding validity requirements.

**Bandwidth selection** is where estimation becomes technically non-trivial. The RDD estimator works locally: you use only observations near the cutoff, where the as-if-random assumption is most credible. Observations far from the cutoff are informative about the regression function's shape but are weaker counterfactuals for units right at the threshold. The bandwidth trades off bias (wider bandwidth = more extrapolation = more potential bias) against variance (narrower bandwidth = fewer observations = more noise). The **Calonico-Cattaneo-Titiunik (CCT)** optimal bandwidth selector formalizes this tradeoff using a mean squared error criterion. In practice, researchers report estimates at the optimal bandwidth and check sensitivity by varying bandwidth width — results that evaporate at different bandwidths are fragile.

**Validity diagnostics** are not formalities — they constitute the empirical argument that your design is identifying a causal effect. The **McCrary density test** checks whether there is a discontinuity in the density of the running variable at the cutoff. If units can manipulate precisely which side of the threshold they fall on, the as-if-random assumption fails: the density would show a suspicious spike just above a scholarship cutoff if administrators are nudging borderline students over. **Covariate continuity tests** check that pre-determined baseline characteristics are continuous at the cutoff — a jump in prior income or age at the threshold (absent a theoretical explanation) signals contamination. **Placebo cutoff tests** apply the design at other values of the running variable where no treatment discontinuity exists; finding effects at placebo cutoffs suggests the real result may be spurious.

**Multiple thresholds** arise when a policy applies different treatments at several cutoffs — income brackets for different subsidy levels, test score thresholds for different program tracks. Each threshold yields a **local average treatment effect** (LATE) for the subpopulation near that specific cutoff, and these estimates need not agree: treatment effects may vary by the level of the running variable. Comparing estimates across thresholds reveals treatment effect heterogeneity and can test whether the running variable moderates the effect. The discipline throughout advanced RDD is remembering what you are identifying: an effect for units at the margin, not a population average. Whether that local effect generalizes beyond the threshold is a substantive question about mechanism — and it cannot be answered by the design alone.
