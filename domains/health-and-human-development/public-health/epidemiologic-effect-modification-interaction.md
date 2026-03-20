---
id: epidemiologic-effect-modification-interaction
title: Effect Modification and Interaction in Epidemiology
domain: health-and-human-development
course: public-health
prerequisites:
- id: measures-of-association
  type: hard
- id: epidemiology-foundations
  type: hard
builds-toward:
- subgroup-analysis-heterogeneity
tags:
- stratification
- heterogeneity
- interaction
- subgroup-analysis
stage: advanced
status: draft
---

# Effect Modification and Interaction in Epidemiology

## Core Idea
Effect modification occurs when the association between an exposure and disease outcome differs across strata of a third variable, reflecting true biologic or social heterogeneity rather than statistical artifact. Identifying effect modifiers reveals subgroups at highest risk and reveals mechanisms of disease causation. Effect modification is mechanistic and expected from a causal theory; interaction on different scales (additive vs. multiplicative) has different interpretations.

## Explainer

Your foundation in measures of association — risk ratios, odds ratios, and rate differences — and your grounding in epidemiologic foundations give you the tools to recognize when a single summary measure is misleading the whole story. Effect modification is the formal name for the situation where that happens: the association you are trying to measure genuinely differs depending on who you are measuring it in.

Start with a concrete case. Suppose you are studying the relationship between air pollution exposure and respiratory hospitalizations. Your overall relative risk is 1.4 — a 40% increase. Now you stratify by smoking status. In non-smokers, the RR is 1.2. In smokers, the RR is 2.8. These are not measurement errors or artifacts — they reflect genuine biological heterogeneity. Smoking damages airway defenses and makes the lung far more vulnerable to particulate matter. Smoking **modifies the effect** of pollution on hospitalization risk. The correct report is not a single summary RR but two stratum-specific estimates that together reveal the mechanism.

This is fundamentally different from confounding, which you have also studied. A **confounder** distorts the apparent association between exposure and outcome and should be controlled for — it is a nuisance. An **effect modifier** reveals real heterogeneity and should be reported separately — it is a finding. The practical test: if controlling for the third variable makes your exposure-outcome association more accurate, it was a confounder. If stratifying by it reveals that the association is genuinely larger in one group than another, it is an effect modifier.

The **additive versus multiplicative scale** distinction adds a layer of complexity that matters for public health policy. Effect modification can exist on one scale but not the other. Suppose two exposures each double disease risk independently (multiplicative RR of 2 for each). If they act independently, the joint RR is 4 — no multiplicative interaction. But the absolute risk difference produced by the combination may still be greater than the sum of each alone — that is additive interaction, and it is what matters for deciding how many hospitalizations you could prevent by addressing each exposure in combination. For public health planning, **additive interaction** is often the more relevant scale because it tells you about the number of cases attributable to the combination that would not occur if either exposure were removed.
