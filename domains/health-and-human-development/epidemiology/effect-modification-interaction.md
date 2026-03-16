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
stage: advanced
status: draft
---

# Effect Modification and Statistical Interaction

## Core Idea
Effect modification occurs when the association between exposure and disease differs across strata of a third variable (the effect modifier). Unlike confounding, effect modification is not bias—it reveals that the exposure effect is real but varies by context. Detecting effect modification requires stratified analysis and may reveal why interventions work differently in subpopulations.

## Explainer

From your study of confounding, you know that a confounder is a variable that creates a spurious or distorted association between exposure and outcome — it is a source of bias to be removed by stratification or adjustment. Effect modification is discovered using the same stratification procedure, which is exactly why the two concepts are so frequently confused. The key is to understand not just the mechanic (stratify and compare) but what the finding means and what you do next.

Begin with a concrete example. Suppose you are studying whether aspirin reduces the risk of myocardial infarction (MI). You stratify by sex and find two things: in men over 50, aspirin reduces MI risk by 35%; in pre-menopausal women, the protective effect is essentially zero. Sex is an **effect modifier** — the size of aspirin's effect on MI differs substantially across strata of sex. Crucially, this difference is not a bias. It is real biological heterogeneity: hormonal differences, baseline cardiovascular risk, and platelet physiology genuinely differ between these groups. The correct response is not to "adjust away" sex and report a pooled estimate — that single number would misrepresent what aspirin actually does for both groups. Instead, you report stratum-specific estimates and investigate why they differ.

Contrast this with confounding. Suppose age is associated with both aspirin use (older people take it more) and MI risk (older people have more MI events). If you fail to account for age, the crude aspirin-MI association is distorted. Stratify by age, and the within-stratum estimates agree with each other and with the adjusted estimate. Age was acting as a confounder. The practical rule is: **if stratum-specific estimates agree, check for confounding (compare crude vs. adjusted)**; **if stratum-specific estimates differ, you may have effect modification (report strata separately)**. Same tool, opposite action.

**Statistical interaction** is the formal modeling version of this concept: it is present when a product term (exposure × potential modifier) in a regression model has a non-zero coefficient. But there is an important distinction between statistical interaction and **biological interaction**. Statistical interaction is scale-dependent — an interaction that appears on the additive scale (risk differences) may disappear on the multiplicative scale (risk ratios), and vice versa. Biological interaction (true synergy or antagonism) implies that the joint effect of two factors exceeds or falls short of what either produces alone, regardless of scale. Whether you care about additive or multiplicative interaction depends on the scientific question, and the convention in epidemiology is to evaluate additive interaction when the goal is identifying subgroups at highest absolute risk — the groups that would benefit most from an intervention — while multiplicative interaction is more common in etiological research. Clarifying which question you are asking before stratifying prevents post-hoc rationalization of whichever scale produces the more dramatic result.
