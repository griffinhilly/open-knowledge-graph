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

## Questions

```yaml
- question: "A researcher compares employed-at-follow-up rates between job training program participants and non-participants, and finds participants have higher employment. Why can't they conclude the program caused the difference?"
  type: multiple-choice
  options:
    - "Employment is too volatile to measure accurately at a single point in time"
    - "The groups may have differed in employment motivation or qualifications before the program — selection bias means the comparison confounds the treatment effect with pre-existing differences"
    - "The sample size is probably too small to detect a real causal effect"
    - "They need regression adjustment for age and education before any comparison is valid"
  answer: 1
  explanation: "People who seek out job training may be more motivated or better-connected than those who don't — the groups differ for reasons unrelated to the program itself. This is selection bias: the naive comparison captures both the treatment effect (if any) and these pre-existing differences. DiD solves this by using the control group's over-time change to estimate what the treatment group's trajectory would have looked like absent the program, removing the confound."

- question: "In a DiD study: the treatment group averages $80 pre-treatment and $90 post-treatment. The control group averages $60 pre-treatment and $65 post-treatment. What is the DiD estimate of the treatment effect?"
  type: multiple-choice
  options:
    - "$10 — the treated group's pre-to-post change"
    - "$25 — the post-treatment difference between the groups"
    - "$5 — the treated group's change ($10) minus the control group's change ($5)"
    - "$20 — the pre-treatment difference between the groups"
  answer: 2
  explanation: "DiD = (Ȳ_treated,post − Ȳ_treated,pre) − (Ȳ_control,post − Ȳ_control,pre) = (90 − 80) − (65 − 60) = 10 − 5 = $5. The control group's $5 change represents what would have happened to the treatment group over the same period without the treatment (under parallel trends). Subtracting it removes the common time trend, leaving only the treatment effect. The $10 and $25 figures are both biased — they fail to remove the underlying time trend."

- question: "For a DiD design to be valid, the treatment and control groups must have similar outcome levels before the treatment period."
  type: true-false
  answer: false
  explanation: "This is the most important misconception about the parallel trends assumption. Parallel trends requires only that the two groups would have moved in parallel over time absent treatment — they can have very different absolute levels. A high-unemployment state and a low-unemployment state can satisfy parallel trends as long as their trends (changes over time) are similar. Differences in levels are removed by the first differencing step; they don't threaten the design."

- question: "The DiD estimator removes the bias from any time-constant difference between the treatment and control groups, because taking pre-to-post changes within each group eliminates stable between-group differences."
  type: true-false
  answer: true
  explanation: "This is the core identifying power of DiD. Any stable difference between groups — whether from selection, geography, demographics, or other confounders — is differenced out when you compute the pre-to-post change within each group. What remains after the double-difference is only the portion of the treated group's change that exceeds the control group's change over the same period, which under parallel trends reflects the treatment effect."

- question: "What is the parallel trends assumption in DiD, and why can it not be directly tested at the exact time of treatment?"
  type: short-answer
  answer: "Parallel trends assumes that absent treatment, the treatment and control groups would have followed the same trajectory over the treatment period — changed by the same amount. It cannot be directly tested at the treatment time because we never observe what the treatment group would have done without treatment — that is the fundamental counterfactual problem. We can support it by verifying parallel pre-treatment trends and arguing by analogy that this would have continued, but we cannot prove it for the treatment period itself."
  explanation: "This untestability is not a defect unique to DiD — it is the fundamental problem of causal inference. All causal identification strategies rest on untestable assumptions about counterfactuals. DiD's strength is that parallel pre-trends provide visible, testable support for the assumption, making violations detectable if the groups were already diverging before treatment."
```

## Explainer

You already know from the potential outcomes framework that the fundamental problem of causal inference is that we can never observe the same unit in both the treated and untreated states at the same time. The naive fix — compare treated units to untreated units after treatment — fails because the groups may differ for reasons unrelated to treatment. Difference-in-differences solves this by using time to construct the missing counterfactual. Instead of asking "what would the treated group have looked like untreated?", DiD asks "how did the treated group's trajectory differ from the control group's trajectory during the same period?"

The estimator is literally two differences stacked. First, you difference within each group: compute the before-to-after change for the treatment group and the before-to-after change for the control group. Then you difference the two differences. This **double-differencing** cancels out anything that was stable over time within each group (fixed differences in levels) and anything that affected both groups equally across time (common time trends). What remains is the portion of the treated group's change that cannot be explained by the time trend alone — the treatment effect.

The identifying assumption — **parallel trends** — is the load-bearing pillar of every DiD study. It says that in the absence of treatment, the treatment and control groups would have moved in parallel over time. This is explicitly a claim about a counterfactual you cannot observe. What you can do is check pre-treatment periods: if the two groups were trending in parallel before treatment, it is more plausible they would have continued to do so. The canonical example, Card and Krueger (1994), compared fast-food employment in New Jersey (raised minimum wage) and Pennsylvania (did not) before and after the policy change. The DiD estimate found no negative employment effect — a landmark result precisely because the research design was credible.

In practice, DiD is implemented as a regression. You create a **treatment dummy** (1 = treatment group), a **post dummy** (1 = after treatment), and their interaction. The coefficient on the interaction term is the DiD estimate. This connects directly to your dummy variable knowledge: the interaction isolates the group-period cell where treatment occurred. Adding additional covariates and unit fixed effects (which you know from fixed effects models) further controls for confounders and absorbs unit-level heterogeneity, strengthening the design. The key caution from the misconceptions is worth internalizing: parallel trends is a claim about counterfactual *trends*, not about levels — the groups can be very different in absolute terms before treatment begins.
