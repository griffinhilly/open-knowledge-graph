---
id: stratification-and-adjustment
title: Stratified Analysis and Adjustment for Confounding
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: confounding-epidemiology
  type: hard
- id: effect-modification-interaction
  type: soft
builds-toward:
- multivariable-regression-epi
tags:
- confounder-control
- stratification
- mantel-haenszel
stage: advanced
status: draft
---

# Stratified Analysis and Adjustment for Confounding

## Core Idea
Stratified analysis divides data by levels of a confounder to examine the exposure-outcome association within homogeneous strata, then combines stratum-specific estimates (e.g., via Mantel-Haenszel). This approach allows simultaneous control of confounding and detection of effect modification. Stratification is transparent and interpretable but becomes cumbersome with multiple confounders.

## Questions

```yaml
- question: "A study of aspirin use and stroke finds a crude OR = 0.5, suggesting strong protection. After stratifying by age, the OR is 0.85 in younger adults and 0.80 in older adults. What does this pattern indicate?"
  type: multiple-choice
  options:
    - "Age is an effect modifier; stratum-specific ORs must be reported separately"
    - "The crude OR is still the most valid estimate because it reflects the real-world distribution of age"
    - "Negative confounding was present — age made aspirin appear more protective than it is; the adjusted estimate near 0.82 is more valid"
    - "The study should be discarded because the crude and adjusted estimates disagree"
  answer: 2
  explanation: "The stratum-specific ORs (0.85, 0.80) are homogeneous — no effect modification — but both differ from the crude OR (0.5). This is classic negative confounding: age was associated with both aspirin use and stroke risk in a way that exaggerated aspirin's protective effect. Within strata, age cannot confound because it does not vary. The Mantel-Haenszel adjusted OR near 0.82 is the valid, confounder-controlled estimate."

- question: "A study of a new drug finds OR = 0.5 among women and OR = 3.0 among men. A researcher computes a Mantel-Haenszel summary OR of 1.1 and plans to report it as the confounder-adjusted estimate. What is wrong with this approach?"
  type: multiple-choice
  options:
    - "The Mantel-Haenszel method requires at least three strata to be valid"
    - "The large difference between stratum-specific ORs indicates effect modification; combining them into a single summary obscures a real and clinically important difference"
    - "A summary OR of 1.1 is too close to the null and therefore meaningless"
    - "Nothing is wrong; combining stratum-specific estimates via Mantel-Haenszel is always appropriate after stratification"
  answer: 1
  explanation: "Substantial heterogeneity across strata — OR = 0.5 versus OR = 3.0 — signals effect modification, not simple confounding. Sex is not just distorting the overall estimate; the drug's effect is genuinely different in men and women. A summary OR of 1.1 would falsely suggest near-null association and hide both the benefit in women and the harm in men. When effect modification is present, stratum-specific estimates must be reported."

- question: "Within a stratum defined by a single level of a confounder (e.g., all current smokers), that confounder cannot distort the exposure-outcome association because it does not vary within the stratum."
  type: true-false
  answer: true
  explanation: "Confounding requires the confounder to be associated with both the exposure and the outcome. Inside a stratum where everyone has the same confounder value, there is no variation — so there is no association between the confounder and exposure or outcome within that stratum. The distortion disappears, and the stratum-specific exposure-outcome estimate reflects the true association."

- question: "When stratum-specific effect estimates differ substantially across strata, the Mantel-Haenszel method should be used to pool them into a single confounder-adjusted summary estimate."
  type: true-false
  answer: false
  explanation: "Substantial heterogeneity across strata means the stratifying variable is an effect modifier, not merely a confounder. The Mantel-Haenszel estimator assumes homogeneity — that a single underlying effect exists across strata. Pooling heterogeneous estimates produces a misleading average that correctly describes no subgroup. The right response is to report stratum-specific estimates and describe the interaction."

- question: "Stratified analysis simultaneously controls for confounding and tests for effect modification. Explain why these two goals lead to different decisions about how to report results."
  type: short-answer
  answer: "If stratum-specific estimates are homogeneous (similar across strata), the stratifying variable is a confounder and a single Mantel-Haenszel adjusted estimate is appropriate — it removes the distortion while efficiently summarizing the exposure effect. If stratum-specific estimates differ substantially, the variable modifies the effect — the association is genuinely different across groups. In that case, a combined summary misrepresents reality and stratum-specific estimates must be reported separately to capture who benefits and who is harmed."
  explanation: "The decision hinge is heterogeneity: homogeneous strata → confounding → combine; heterogeneous strata → effect modification → report separately. Failing to distinguish these leads either to spurious summary estimates or to missed interactions that are central to clinical and public health decisions."
```

## Explainer

You already understand confounding: a variable associated with both the exposure and the outcome distorts the apparent exposure–outcome relationship. The intuitive fix is simple — look at the exposure–outcome association *separately* within groups that are homogeneous with respect to the confounder. Within each stratum, the confounder cannot confound because it does not vary. If the crude (unstratified) association differs from the stratum-specific associations, confounding was present and the stratum-specific estimates are the valid ones.

To make this concrete: suppose you observe a crude odds ratio of 2.0 for the association between coffee drinking and myocardial infarction (MI). But coffee drinkers also smoke more than non-drinkers. When you stratify by smoking status, you find an odds ratio of 1.0 in smokers and 1.0 in non-smokers. The stratum-specific estimates are homogeneous (both null) and differ from the crude estimate — classic positive confounding. Smoking was making coffee look harmful because it was associated with both the exposure (coffee) and the outcome (MI). Within strata of smoking status, that distortion disappears.

If the stratum-specific estimates are similar across strata, you can combine them into a single summary estimate that is adjusted for the stratifying variable. The **Mantel-Haenszel (MH) estimator** is the standard approach for 2×2 tables: it computes a weighted average of stratum-specific odds ratios (or risk ratios), where the weights reflect the amount of information in each stratum. The MH estimator is computationally simple, statistically efficient when homogeneity holds, and interpretable as the confounder-adjusted association. You can also use the **Woolf method** (variance-based weighting) as an alternative.

The same analysis that controls for confounding also detects **effect modification**: if stratum-specific estimates *differ* substantially across strata, the variable you stratified on is not merely a confounder — it is a modifier of the exposure effect. For example, if the coffee–MI odds ratio is 2.0 among smokers but 0.8 among non-smokers, the effect is genuinely different in the two groups. In this case, combining the estimates into a single adjusted summary would be misleading — the correct report is stratum-specific. The decision to report separate estimates versus a combined estimate hinges on whether heterogeneity is present. This is why stratified analysis is not merely a confounding-control tool but also the foundational method for identifying who benefits or is harmed differently — a question central to clinical and public health decision-making.

Stratification's limitation is the **sparse data problem**: each additional stratifying variable divides the dataset into more cells, many of which may have too few observations to produce stable estimates. Two binary confounders require four strata; three binary confounders require eight. This is why stratification gives way to multivariable regression — logistic, Poisson, Cox — when there are several confounders to control simultaneously. Regression can be understood as a generalization of stratification that handles sparse data through model-based smoothing, trading the transparency of stratification for the capacity to adjust for many variables at once.
