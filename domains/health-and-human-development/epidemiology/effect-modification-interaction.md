---
id: effect-modification-interaction
title: Effect Modification and Statistical Interaction
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: confounding-epidemiology
  type: hard
builds-toward:
- stratification-and-adjustment
- multivariable-regression-epi
tags:
- effect-modification
- heterogeneity
- subgroup-analysis
stage: expert
status: validated
---

# Effect Modification and Statistical Interaction

## Core Idea
Effect modification occurs when the association between exposure and disease differs across strata of a third variable (the effect modifier). Unlike confounding, effect modification is not bias—it reveals that the exposure effect is real but varies by context. Detecting effect modification requires stratified analysis and may reveal why interventions work differently in subpopulations.

## Questions

```yaml
- question: "A stratified analysis of aspirin and myocardial infarction risk shows RR = 0.65 in men over 50 and RR = 1.02 in pre-menopausal women. A colleague argues you should adjust for sex and report a single overall estimate. What is the correct response?"
  type: multiple-choice
  options:
    - "Agree — adjusting for sex removes the confounding and reveals the true aspirin effect"
    - "Agree — the stratum-specific estimates are too heterogeneous to be reliable individually"
    - "Disagree — the divergent stratum-specific estimates indicate effect modification, and collapsing them into a single adjusted estimate would obscure genuine biological heterogeneity"
    - "Disagree — adjustment is unnecessary since sex is not associated with aspirin use in this study"
  answer: 2
  explanation: "When stratum-specific estimates differ substantially, this is effect modification — the exposure effect genuinely varies across levels of the stratifying variable. Pooling or adjusting produces a meaningless average that misrepresents the truth in both groups: aspirin is protective in older men and neutral in pre-menopausal women. Adjusting to remove effect modification would be scientifically incorrect. The right action is to report stratum-specific estimates and investigate the biological mechanism (hormonal differences, cardiovascular risk profiles). This differs from confounding, where adjustment is appropriate because the stratum-specific estimates agree with each other."

- question: "A stratified analysis of physical activity and diabetes risk shows RR = 0.61 in men and RR = 0.60 in women, while the crude (unadjusted) RR = 0.76. This pattern most strongly suggests:"
  type: multiple-choice
  options:
    - "Effect modification by sex — physical activity protects men and women differently"
    - "Confounding by sex — sex is associated with both physical activity levels and diabetes risk, distorting the crude estimate"
    - "Neither confounding nor effect modification — the crude and adjusted estimates are similar enough to ignore"
    - "Effect modification that operates on the multiplicative but not the additive scale"
  answer: 1
  explanation: "The key diagnostic pattern: stratum-specific estimates agree with each other (0.61 ≈ 0.60) but both differ from the crude estimate (0.76). This is the fingerprint of confounding, not effect modification. Sex is acting as a confounder — it distorts the crude estimate because it is associated with both the exposure (men and women have different activity levels) and the outcome (sex differences in diabetes risk). Adjusting for sex corrects the crude estimate toward the true effect (~0.60–0.61). If there were effect modification, the stratum-specific estimates would diverge from each other."

- question: "Effect modification is a form of bias that distorts the true association between exposure and outcome and should be removed using statistical adjustment, just like confounding."
  type: true-false
  answer: false
  explanation: "This is the central conceptual error in the confounding/effect modification distinction. Effect modification is not bias — it reflects real, genuine heterogeneity in the exposure effect across subgroups. The 'distortion' is biological truth, not a statistical artifact. The appropriate response to effect modification is to preserve and report the stratum-specific estimates, not to eliminate them by adjustment. Adjustment in the presence of true effect modification produces a misleading single number that is literally incorrect for every subgroup it purports to summarize. Confounding is the concept where bias exists and adjustment is warranted."

- question: "A statistical interaction that appears significant on the additive scale (risk differences) may be absent or even reversed when examined on the multiplicative scale (risk ratios)."
  type: true-false
  answer: true
  explanation: "Statistical interaction is scale-dependent. Consider two groups with risks: A alone = 0.10, B alone = 0.20, A+B together = 0.30. On the additive scale, the joint effect equals the sum of individual effects (0.10 + 0.20 = 0.30), so no additive interaction. On the multiplicative scale, you might still find statistical interaction depending on how you parameterize the model. Conversely, the same data might show additive interaction without multiplicative interaction. This scale-dependence is why epidemiologists must specify which scale they are using: additive interaction is usually more relevant for identifying high-risk subgroups for intervention (absolute risk matters for public health), while multiplicative interaction is common in etiological research."

- question: "What is the key practical difference between how an epidemiologist should respond when stratified analysis reveals confounding versus when it reveals effect modification?"
  type: short-answer
  answer: "When stratified analysis reveals confounding: the stratum-specific estimates agree with each other but differ from the crude estimate. The crude estimate is biased, and the correct action is to report the adjusted (pooled) estimate that removes the confounder's distorting influence. When stratified analysis reveals effect modification: the stratum-specific estimates differ substantially from each other. The crude estimate is misleading not because of bias but because the exposure truly affects different subgroups differently. The correct action is to report stratum-specific estimates separately — pooling or adjusting would destroy the information. The same statistical tool (stratification) diagnoses both, but the response is opposite: for confounding, collapse; for effect modification, separate."
  explanation: "A useful memory aid: confounding says 'the crude estimate is wrong, fix it'; effect modification says 'no single estimate is right, report both.' The test is whether stratum-specific estimates agree. Agreement = confounding (compare crude vs. adjusted). Disagreement = effect modification (the variation is the result). Researchers who always pool results may hide important effect modification that could reveal who benefits from a treatment and who does not — information critical for clinical decision-making and targeted public health interventions."
```

## Explainer

From your study of confounding, you know that a confounder is a variable that creates a spurious or distorted association between exposure and outcome — it is a source of bias to be removed by stratification or adjustment. Effect modification is discovered using the same stratification procedure, which is exactly why the two concepts are so frequently confused. The key is to understand not just the mechanic (stratify and compare) but what the finding means and what you do next.

Begin with a concrete example. Suppose you are studying whether aspirin reduces the risk of myocardial infarction (MI). You stratify by sex and find two things: in men over 50, aspirin reduces MI risk by 35%; in pre-menopausal women, the protective effect is essentially zero. Sex is an **effect modifier** — the size of aspirin's effect on MI differs substantially across strata of sex. Crucially, this difference is not a bias. It is real biological heterogeneity: hormonal differences, baseline cardiovascular risk, and platelet physiology genuinely differ between these groups. The correct response is not to "adjust away" sex and report a pooled estimate — that single number would misrepresent what aspirin actually does for both groups. Instead, you report stratum-specific estimates and investigate why they differ.

Contrast this with confounding. Suppose age is associated with both aspirin use (older people take it more) and MI risk (older people have more MI events). If you fail to account for age, the crude aspirin-MI association is distorted. Stratify by age, and the within-stratum estimates agree with each other and with the adjusted estimate. Age was acting as a confounder. The practical rule is: **if stratum-specific estimates agree, check for confounding (compare crude vs. adjusted)**; **if stratum-specific estimates differ, you may have effect modification (report strata separately)**. Same tool, opposite action.

**Statistical interaction** is the formal modeling version of this concept: it is present when a product term (exposure × potential modifier) in a regression model has a non-zero coefficient. But there is an important distinction between statistical interaction and **biological interaction**. Statistical interaction is scale-dependent — an interaction that appears on the additive scale (risk differences) may disappear on the multiplicative scale (risk ratios), and vice versa. Biological interaction (true synergy or antagonism) implies that the joint effect of two factors exceeds or falls short of what either produces alone, regardless of scale. Whether you care about additive or multiplicative interaction depends on the scientific question, and the convention in epidemiology is to evaluate additive interaction when the goal is identifying subgroups at highest absolute risk — the groups that would benefit most from an intervention — while multiplicative interaction is more common in etiological research. Clarifying which question you are asking before stratifying prevents post-hoc rationalization of whichever scale produces the more dramatic result.
