---
id: synthetic-control-methods-epidemiology
title: Synthetic Control and Comparative Case Studies
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: natural-experiments
  type: hard
- id: difference-in-differences
  type: soft
builds-toward:
- interrupted-time-series-analysis
tags:
- quasi-experimental
- policy-evaluation
- case-study
stage: advanced
status: draft
---

# Synthetic Control and Comparative Case Studies

## Core Idea
Synthetic control methods construct a weighted combination of unexposed units to match pre-intervention characteristics of an exposed unit. Comparing the exposed unit's post-intervention trajectory to the synthetic control estimates the intervention effect. This approach is useful when few units are exposed and historical data are limited.

## Explainer

From your study of natural experiments and difference-in-differences (DiD), you know that quasi-experimental methods try to approximate the counterfactual: what would have happened to the treated unit if it had not received the intervention? Difference-in-differences achieves this by finding a control group with parallel pre-intervention trends and assuming those trends would have continued. But DiD requires multiple unexposed units that share a common trend with the treated unit — and it struggles when you have only a single treated unit (one city, one country, one hospital) and a heterogeneous pool of potential controls with diverging pre-treatment trends.

**Synthetic control** was developed precisely for this setting. The core idea is intuitive: rather than picking a single control unit that resembles the treated unit, why not build a tailor-made composite? You select a **donor pool** of unexposed units and find the weighted combination of those units — the synthetic control — that best reproduces the treated unit's pre-intervention trajectory across a vector of outcome and covariate values. The algorithm minimizes the distance between the treated unit and the weighted combination during the **pre-period**. If California is the treated unit (which implemented a policy), the synthetic control might be 40% Texas + 35% Florida + 15% Ohio + 10% Pennsylvania — whatever mix best matches California's pre-intervention smoking rates, demographics, and economic indicators. No single state needs to look like California; the composite does.

After the intervention, you simply compare the treated unit's actual post-intervention trajectory to what the synthetic control would have predicted. The gap between the two trajectories is your estimate of the **treatment effect**. The visual logic is compelling: if the synthetic control tracked the treated unit closely for ten years before the policy change and then diverged sharply afterward, the divergence is hard to attribute to anything other than the policy. This is an extension of the DiD intuition — instead of assuming parallel trends between real groups, you construct a control group whose trends are guaranteed to match by construction.

Inference in synthetic control is non-standard because you typically have very few treated units (often one) and standard frequentist assumptions break down. The conventional approach uses **placebo tests**: apply the synthetic control method to each unit in the donor pool as if it were treated, estimate its "placebo effect," and compare the treated unit's actual effect to the distribution of placebo effects. If the treated unit's post-intervention gap is large relative to the placebo gaps, that constitutes evidence against the null hypothesis. This permutation-based inference is honest about the small-sample nature of the analysis. The method has important limitations: it requires a rich pre-period for the matching algorithm to work; it cannot handle multiple treated units without extensions; and when the treated unit is an outlier that the donor pool cannot match well in the pre-period, the synthetic control is unreliable and that failure should be reported explicitly as a quality check.
