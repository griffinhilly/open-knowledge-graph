---
id: causal-inference-observational-data
title: Causal Inference from Observational Data
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: research-design-advanced
  type: hard
- id: linear-regression-social-science
  type: hard
- id: conditional-probability-fundamentals
  type: hard
- id: probability-distributions
  type: hard
- id: conditional-probability
  type: soft
- id: covariance-between-random-variables
  type: soft
builds-toward:
- instrumental-variables-methods
- difference-in-differences
- regression-discontinuity-sharp-fuzzy
- propensity-score-methods
tags:
- causal-inference
- potential-outcomes
- confounding
- identification
stage: formal-systems
status: validated
---

# Causal Inference from Observational Data

## Core Idea
Synthesizes strategies for inferring causation from observational data when randomization is impossible or unethical. Covers the causal hierarchy (association, experimental, natural experiment), potential outcomes framework, confounding, backdoor and frontdoor criteria, and conditions for causal identification.

## How It's Best Learned
Draw directed acyclic graphs (DAGs) for research questions, identify confounders, write causal models, discuss identification assumptions, evaluate whether different designs meet assumptions.

## Common Misconceptions
- Correlation never implies causation
- More controls always improve causal inference
- Unconfoundedness can be tested with data

## Questions

```yaml
- question: "A researcher adds a new control variable to a regression model. The variable is a collider — it is caused by both the treatment variable and the outcome variable. What happens to the causal estimate?"
  type: multiple-choice
  options: ["It improves, because more variance is explained", "It is unaffected, because colliders are neutral controls", "It becomes biased, because conditioning on a collider opens a previously blocked non-causal path", "The standard errors decrease, making the estimate more reliable"]
  answer: 2
  explanation: "Conditioning on a collider opens a backdoor path between treatment and outcome that was previously blocked, inducing a spurious correlation and biasing the causal estimate. This is the key reason 'add more controls' is not always the right strategy. Proper causal analysis requires mapping the data-generating process (via a DAG) before deciding what to condition on."

- question: "If a study finds a statistically significant association between X and Y after controlling for all available observed confounders, we can conclude that X causes Y."
  type: true-false
  answer: false
  explanation: "Unconfoundedness — the assumption that no unmeasured confounders exist — cannot be verified from data alone. Even after controlling for every observed covariate, unmeasured variables may still confound the relationship. Causal identification requires a credible design argument about the data-generating process, not just statistical significance after observed controls."

- question: "What is the potential outcomes framework, and why is the fundamental problem of causal inference called 'fundamental'?"
  type: short-answer
  answer: "The potential outcomes framework defines the causal effect of treatment T on unit i as Y_i(1) − Y_i(0): what would happen if treated minus what would happen if untreated. It is called fundamental because we can only ever observe one of these two outcomes for any individual — the other is an unobservable counterfactual. This is a logical impossibility, not a data limitation, and cannot be solved by collecting more observations on the same unit."
  explanation: "The impossibility of observing both potential outcomes simultaneously is not a measurement problem — it is a structural fact about causality. All causal inference strategies (randomization, instrumental variables, difference-in-differences, regression discontinuity) are attempts to credibly estimate the missing counterfactual under different sets of identifying assumptions. Understanding this frames why each design requires its own specific assumptions."
```

## Explainer

You have learned to run regressions and interpret correlations. But correlation is not causation — and more usefully, there is now a rigorous mathematical framework for specifying exactly when and why an observed correlation can and cannot be interpreted causally. That framework is the subject of this topic.

The foundation is the potential outcomes framework, developed by Donald Rubin and extended by Judea Pearl and others. For any unit i and a binary treatment T, we define two potential outcomes: Y_i(1), what would happen to unit i if assigned to treatment, and Y_i(0), what would happen if not. The individual causal effect is the difference Y_i(1) − Y_i(0). The problem is that we observe only one of these — whichever treatment state actually occurred. The other is a counterfactual: what would have happened in a world that did not occur. This is the fundamental problem of causal inference: it is a logical impossibility, not a data gap. No sample size, no matter how large, allows you to observe both potential outcomes for the same unit at the same time.

Randomization solves this problem in expectation. If treatment assignment is truly random, then the treated and untreated groups are identical in expectation across all observed and unobserved characteristics. The observed difference in outcomes is then an unbiased estimate of the average treatment effect. But randomization is often impossible — you cannot randomly assign people to smoke, grow up poor, or experience a policy implemented everywhere simultaneously. Most data is observational, and observational data requires you to defend causal identification through explicit design arguments.

Directed acyclic graphs (DAGs) are the tool for making those arguments transparent. In a DAG, variables are nodes and causal relationships are directed arrows. A confounder is a common cause of both treatment and outcome that creates a non-causal association between them; it must be blocked by conditioning. A mediator lies on the causal path from treatment to outcome; conditioning on it blocks part of the effect you are trying to measure. A collider is caused by both treatment and outcome; conditioning on it opens a spurious path that was previously blocked — making the estimate worse, not better. The backdoor criterion formalizes which sets of variables, when conditioned on, close all non-causal paths without opening new ones. Getting this right requires understanding the data-generating process, not just running variable-selection algorithms.

Three common misconceptions are worth internalizing directly. First, "correlation never implies causation" is too strong a rule — under the right design assumptions, observational correlations can be interpreted causally. The question is always whether those assumptions are defensible, not whether causation is categorically off the table. Second, "add more controls" is not always better — colliders are the clearest counterexample, and there are others. Third, "unconfoundedness can be tested" is wrong by construction: unconfoundedness is an assumption about unmeasured variables, and unmeasured variables cannot be used to test assumptions about themselves. What can be done is sensitivity analysis — testing how large an unmeasured confounder would need to be to overturn your conclusion. Honest causal work states assumptions clearly, defends them on substantive grounds, and reports what would falsify them.
