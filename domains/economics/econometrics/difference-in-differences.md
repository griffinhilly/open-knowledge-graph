---
id: difference-in-differences
title: Difference-in-Differences
domain: economics
course: econometrics
prerequisites:
- id: causal-inference-econometrics
  type: hard
- id: potential-outcomes-framework
  type: hard
- id: dummy-variables-regression
  type: hard
- id: fixed-effects-models
  type: soft
- id: selection-bias-econometrics
  type: soft
tags:
- DiD
- difference-in-differences
- parallel-trends
- policy-evaluation
stage: formal-systems
status: validated
---
# Difference-in-Differences

## Core Idea
Difference-in-differences (DiD) estimates causal treatment effects by comparing the pre-to-post change in the treatment group to the pre-to-post change in a comparison group. The estimator is β̂_DiD = (Ȳ_treated,post − Ȳ_treated,pre) − (Ȳ_control,post − Ȳ_control,pre), which differences out both pre-existing differences and aggregate time trends. The critical identifying assumption is parallel trends: in the absence of treatment, the treatment and control groups would have followed the same trajectory. This assumption is untestable at the exact period of treatment but is supported by showing parallel pre-trends in the data.

## How It's Best Learned
Replicate Card and Krueger's (1994) minimum wage study using New Jersey and Pennsylvania as treatment and control — this is the canonical DiD application in labor economics.

## Common Misconceptions
- Parallel trends is an assumption about counterfactual outcomes, not about the levels of outcomes before treatment — groups can differ in levels.
- With staggered treatment timing across units, simple two-way FE DiD can be biased; recent 'heterogeneous treatment effects' literature addresses this.

## Explainer

You already know from the potential outcomes framework that the fundamental problem of causal inference is that we can never observe the same unit in both the treated and untreated states at the same time. The naive fix — compare treated units to untreated units after treatment — fails because the groups may differ for reasons unrelated to treatment. Difference-in-differences solves this by using time to construct the missing counterfactual. Instead of asking "what would the treated group have looked like untreated?", DiD asks "how did the treated group's trajectory differ from the control group's trajectory during the same period?"

The estimator is literally two differences stacked. First, you difference within each group: compute the before-to-after change for the treatment group and the before-to-after change for the control group. Then you difference the two differences. This **double-differencing** cancels out anything that was stable over time within each group (fixed differences in levels) and anything that affected both groups equally across time (common time trends). What remains is the portion of the treated group's change that cannot be explained by the time trend alone — the treatment effect.

The identifying assumption — **parallel trends** — is the load-bearing pillar of every DiD study. It says that in the absence of treatment, the treatment and control groups would have moved in parallel over time. This is explicitly a claim about a counterfactual you cannot observe. What you can do is check pre-treatment periods: if the two groups were trending in parallel before treatment, it is more plausible they would have continued to do so. The canonical example, Card and Krueger (1994), compared fast-food employment in New Jersey (raised minimum wage) and Pennsylvania (did not) before and after the policy change. The DiD estimate found no negative employment effect — a landmark result precisely because the research design was credible.

In practice, DiD is implemented as a regression. You create a **treatment dummy** (1 = treatment group), a **post dummy** (1 = after treatment), and their interaction. The coefficient on the interaction term is the DiD estimate. This connects directly to your dummy variable knowledge: the interaction isolates the group-period cell where treatment occurred. Adding additional covariates and unit fixed effects (which you know from fixed effects models) further controls for confounders and absorbs unit-level heterogeneity, strengthening the design. The key caution from the misconceptions is worth internalizing: parallel trends is a claim about counterfactual *trends*, not about levels — the groups can be very different in absolute terms before treatment begins.
