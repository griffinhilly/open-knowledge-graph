---
id: synthetic-control-methods-research-methods-social-science
title: Synthetic Control Methods
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: natural-experiments-identification-strategy
  type: hard
- id: time-series-cross-section
  type: soft
- id: linear-regression
  type: soft
builds-toward:
- generalized-synthetic-control
- augmented-synthetic-control
tags:
- causal-inference
- comparative
- counterfactual
- policy-evaluation
stage: advanced
status: draft
---

# Synthetic Control Methods

## Core Idea
Synthetic control constructs a counterfactual for a treated unit by taking a weighted combination of untreated units. When a single unit (country, region, organization) experiences an intervention, its pre-intervention trends may not match any single control unit, but a weighted average may. The method estimates the treatment effect as the post-intervention difference between the treated unit and its synthetic control. It is particularly useful for policy evaluation when aggregate data is available but individual randomization is infeasible.

## Explainer

From natural experiments, you know that causal identification requires a credible counterfactual: what would have happened to the treated unit if it had not been treated? The challenge in many policy contexts is that the unit of treatment is a whole country, state, or city — you cannot randomize, and no single comparison unit may look much like it. Synthetic control addresses exactly this problem by constructing an artificial comparison unit from a weighted combination of untreated units.

The canonical example is Abadie, Diamond, and Hainmueller's study of the effect of California's 1988 tobacco control program on per-capita cigarette sales. No single state looks quite like California in the pre-1988 period — not in terms of economic conditions, demographics, and pre-existing cigarette consumption trends. But a **synthetic California** — a weighted average of Colorado (58.9%), Utah (8.6%), Nevada (23.3%), and a few others — tracks California's pre-intervention trajectory extremely well over the prior 17 years. After 1988, observed California diverges below synthetic California. That gap is the estimated treatment effect.

The weights are chosen to minimize the discrepancy between the treated unit and the synthetic control on pre-intervention outcomes and predictors. This is a transparent, data-driven process: you see exactly which donor units contribute to the synthetic control and in what proportions. The pre-intervention fit is directly verifiable — you plot both series and inspect how closely they track. This is a significant advantage over regression-based approaches where the counterfactual is implicit. If the pre-intervention fit is poor, the synthetic control is not credible, and you know it.

Inference in synthetic control is done through **placebo tests** rather than classical standard errors. The idea: apply the same method to each untreated unit in the donor pool, pretending it received the treatment. Each untreated unit generates its own synthetic control and its own estimated "effect." The distribution of these placebo estimates tells you how unusual your actual estimated effect is. If California's post-intervention gap is much larger than any of the placebo gaps, that is evidence the effect is real. If many placebos show similar gaps, the California result is unexceptional. This permutation-based inference is appropriate because you have one treated unit — asymptotic theory is irrelevant.

The method has important limitations. It requires a reasonably long pre-intervention period to construct and validate the synthetic control. It requires a **donor pool** of untreated units that are genuinely comparable — if the treated unit is an outlier (e.g., the United States as a whole), there may be no good synthetic. It also assumes that the untreated donor units are not themselves affected by the intervention (the **stable unit treatment value assumption**). Despite these constraints, synthetic control has become a standard tool in comparative policy analysis precisely because it makes the counterfactual construction transparent and the credibility of the identification directly inspectable.
