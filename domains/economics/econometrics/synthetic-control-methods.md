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

## Questions

```yaml
- question: "A researcher wants to estimate the effect of a tax reform implemented in one state in 2010, using 40 other states as potential controls. Pre-treatment trends in the treated state are not well matched by any single control state. Which method is most appropriate?"
  type: multiple-choice
  options:
    - "Difference-in-differences using the single most similar state as the control"
    - "A synthetic control constructed as a weighted average of control states that together match the treated state's pre-reform path"
    - "A randomized controlled trial comparing the treated state to randomly assigned controls"
    - "Ordinary least squares regression with state fixed effects, ignoring the pre-trend mismatch"
  answer: 1
  explanation: "When no single control unit matches the treated unit's pre-treatment trajectory, synthetic control constructs a counterfactual from a weighted combination of multiple donor units. The weights are chosen to minimize pre-treatment discrepancy. This is precisely the setting synthetic control is designed for: one treated unit, many potential controls, poor single-unit match. Difference-in-differences would be inappropriate here because the parallel trends assumption fails when pre-treatment trends diverge. A randomized trial is impossible since the policy already happened."

- question: "In a synthetic control study, the pre-treatment fit between the treated unit and its synthetic counterpart is very poor. What does this imply?"
  type: multiple-choice
  options:
    - "The post-treatment gap is likely to overestimate the true effect, since the synthetic control overshoots"
    - "The counterfactual is less credible — if the synthetic control could not track the treated unit before treatment, there is less reason to trust it afterward"
    - "The method failed; the researcher should add more pre-treatment periods until the fit improves"
    - "The policy had no effect, since the poor fit shows the treated and control units were fundamentally different"
  answer: 1
  explanation: "The credibility of synthetic control rests entirely on the quality of the pre-treatment fit. The identifying assumption is that the synthetic control would have continued on the same path as the treated unit absent treatment. If the synthetic control could not replicate the pre-treatment path — despite being specifically optimized to do so — there is no basis for trusting that it captures the counterfactual trajectory post-treatment. A poor fit does not mean there was no effect; it means the evidence for any estimated effect is weak. The researcher should report this honestly and be cautious about causal claims."

- question: "Synthetic control inference typically uses placebo tests rather than standard t-tests because there is only one treated unit."
  type: true-false
  answer: true
  explanation: "A t-test requires estimating the sampling distribution of the estimated effect — which requires multiple treated units to see how much the estimate would vary across samples. With a single treated unit, there is no sampling variation to estimate. Placebo tests solve this by running the same synthetic control exercise for every control unit as if it had been treated. The resulting distribution of 'fake' gaps provides a reference: if the real treated unit's post-treatment gap is much larger than the placebo gaps, it is unlikely to be noise. This is conceptually analogous to computing a p-value, but derived entirely from the data at hand."

- question: "A tight pre-treatment fit in a synthetic control study proves that the estimated post-treatment gap reflects a real causal effect."
  type: true-false
  answer: false
  explanation: "Pre-treatment fit is necessary for credibility but not sufficient for proof. A tight pre-treatment match increases confidence that the synthetic control is a valid counterfactual, but the causal inference still rests on the untestable assumption that the match would have continued absent treatment. Confounding events that affected the treated unit but not the donor pool, extrapolation risk, and violations of the 'no interference' assumption can all produce misleading estimates despite perfect pre-treatment fit. Inference is strengthened by combining tight pre-treatment fit with placebo tests and qualitative reasoning about alternative explanations."

- question: "Why do synthetic control researchers use placebo tests for inference, and how do these tests work?"
  type: short-answer
  answer: "Placebo tests substitute each control unit as if it were the treated unit: a synthetic version is constructed for it using the remaining controls, and the post-'treatment' gap is measured. This generates a distribution of gaps under the null hypothesis of no effect. If the actual treated unit's post-treatment gap is much larger than almost all of the placebo gaps, this is evidence that the effect is real rather than noise. Placebo tests work because the distribution of gaps for units that were never treated captures how large gaps can be due to chance alone."
  explanation: "The key insight is that placebo tests use the structure of the data itself to simulate a null distribution — which is exactly what a p-value does in frequentist testing, but derived from the donor pool rather than from repeated sampling. This is necessary because with one treated unit, there is nothing to compute a standard error from. Researchers typically display all placebo and real gaps in a single time-series plot, making the inference transparent and visual rather than reduced to a single p-value."
```

## Explainer

You already know the core challenge of causal inference: to estimate the effect of a treatment, you need to know what would have happened to the treated unit if it had not been treated — the **counterfactual**. Difference-in-differences addresses this by assuming parallel trends: the untreated comparison group serves as the counterfactual because it was trending the same way as the treated group before treatment. But what happens when no single control unit tracks the treated unit's pre-treatment path? That is exactly the problem synthetic control methods solve.

The central idea is to build the counterfactual not from a single control unit but from a **weighted combination** of many control units — a "synthetic" version of the treated unit. The weights are chosen so that the synthetic control matches the treated unit as closely as possible on pre-treatment outcomes and relevant predictors. If California experienced an economic policy change in 2000, you might construct a synthetic California from a weighted average of Colorado, Nevada, Washington, and other states that together reproduce California's pre-2000 economic path. The post-treatment gap between California's actual outcome and its synthetic counterpart is the estimated policy effect.

The key identifying assumption is that the synthetic control — having matched the treated unit's pre-treatment trajectory — would have continued on the same path absent treatment. This is more credible than a single control unit if the pre-treatment match is tight, but it is impossible to verify directly (you cannot observe what the synthetic California would have done post-treatment). Researchers assess credibility through the quality of the pre-treatment fit: a synthetic control that closely tracks the treated unit for many pre-treatment periods provides a stronger counterfactual than one with substantial pre-treatment discrepancy.

**Placebo tests** are the workhorse of inference in synthetic control. Because you typically have only one treated unit, standard t-tests are uninformative. Instead, you run the same exercise for every control unit as if it had been treated: construct a synthetic version, measure the post-"treatment" gap, and compare it to the real gap for the actually treated unit. If the real treated unit's post-treatment gap is much larger than the placebo gaps, you have evidence that the effect is real rather than noise. This distribution of placebo gaps plays the role that the sampling distribution plays in conventional hypothesis testing.

Synthetic control is most powerful when the setting has a single treated unit (a country, state, or firm), many potential donors in the **donor pool**, a long pre-treatment period to build a good match, and an intervention that is sharply timed. It is less suited to settings with many treated units — difference-in-differences handles those better — or when pre-treatment data is sparse. The method has become standard in policy evaluation precisely because it makes the counterfactual visible: you can plot the treated unit and its synthetic twin over time and let readers judge the plausibility of the counterfactual directly, which is a transparency that regression-based approaches rarely offer.
