---
id: synthetic-control-methods
title: Synthetic Control Methods for Policy Evaluation
domain: economics
course: econometrics
prerequisites:
- id: causal-inference-econometrics
  type: hard
- id: difference-in-differences
  type: soft
tags:
- synthetic-control
- causal-inference
- policy-evaluation
stage: formal-systems
status: draft
---

# Synthetic Control Methods for Policy Evaluation

## Core Idea
Synthetic control constructs a weighted average of control units to form a counterfactual for a treated unit. This method is powerful when there is one treated unit and many potential controls but pre-treatment trends diverge.

## Explainer

You already know the core challenge of causal inference: to estimate the effect of a treatment, you need to know what would have happened to the treated unit if it had not been treated — the **counterfactual**. Difference-in-differences addresses this by assuming parallel trends: the untreated comparison group serves as the counterfactual because it was trending the same way as the treated group before treatment. But what happens when no single control unit tracks the treated unit's pre-treatment path? That is exactly the problem synthetic control methods solve.

The central idea is to build the counterfactual not from a single control unit but from a **weighted combination** of many control units — a "synthetic" version of the treated unit. The weights are chosen so that the synthetic control matches the treated unit as closely as possible on pre-treatment outcomes and relevant predictors. If California experienced an economic policy change in 2000, you might construct a synthetic California from a weighted average of Colorado, Nevada, Washington, and other states that together reproduce California's pre-2000 economic path. The post-treatment gap between California's actual outcome and its synthetic counterpart is the estimated policy effect.

The key identifying assumption is that the synthetic control — having matched the treated unit's pre-treatment trajectory — would have continued on the same path absent treatment. This is more credible than a single control unit if the pre-treatment match is tight, but it is impossible to verify directly (you cannot observe what the synthetic California would have done post-treatment). Researchers assess credibility through the quality of the pre-treatment fit: a synthetic control that closely tracks the treated unit for many pre-treatment periods provides a stronger counterfactual than one with substantial pre-treatment discrepancy.

**Placebo tests** are the workhorse of inference in synthetic control. Because you typically have only one treated unit, standard t-tests are uninformative. Instead, you run the same exercise for every control unit as if it had been treated: construct a synthetic version, measure the post-"treatment" gap, and compare it to the real gap for the actually treated unit. If the real treated unit's post-treatment gap is much larger than the placebo gaps, you have evidence that the effect is real rather than noise. This distribution of placebo gaps plays the role that the sampling distribution plays in conventional hypothesis testing.

Synthetic control is most powerful when the setting has a single treated unit (a country, state, or firm), many potential donors in the **donor pool**, a long pre-treatment period to build a good match, and an intervention that is sharply timed. It is less suited to settings with many treated units — difference-in-differences handles those better — or when pre-treatment data is sparse. The method has become standard in policy evaluation precisely because it makes the counterfactual visible: you can plot the treated unit and its synthetic twin over time and let readers judge the plausibility of the counterfactual directly, which is a transparency that regression-based approaches rarely offer.
