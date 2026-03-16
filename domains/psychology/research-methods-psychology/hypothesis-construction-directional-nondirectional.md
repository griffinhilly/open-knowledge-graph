---
id: hypothesis-construction-directional-nondirectional
title: 'Hypothesis Construction: Directional and Nondirectional Predictions'
domain: psychology
course: research-methods-psychology
prerequisites:
- id: research-question-formulation-specificity
  type: hard
- id: literature-review-and-synthesis
  type: soft
- id: probability-axioms
  type: soft
- id: bayes-theorem
  type: soft
builds-toward:
- operationalization-iv-and-dv
- analysis-plan-preregistration-commitment
tags:
- planning
- hypothesis
- prediction
stage: abstract-reasoning
status: draft
---

# Hypothesis Construction: Directional and Nondirectional Predictions

## Core Idea
Hypotheses translate research questions into specific, testable predictions about relationships between variables. Directional hypotheses predict the specific direction of effects (e.g., 'increased stress reduces memory performance'), while nondirectional hypotheses predict only that relationships exist without specifying direction. The choice reflects theoretical confidence and has statistical consequences for power and interpretation.

## How It's Best Learned
Examine meta-analyses or effect size estimates from prior research to build directional hypotheses with confidence. Write hypotheses as conditional statements: 'If [IV changes], then [DV changes] in [direction].' Compare statistical power for directional vs. nondirectional tests using power calculators.

## Common Misconceptions
- Directional hypotheses are always more sophisticated or preferable; they require stronger prior evidence and commitment.
- One-tailed tests (directional) are always more powerful; they only gain power if you're truly willing to ignore effects in the opposite direction.
- Posthoc directional hypotheses after seeing data are equivalent to preregistered ones; all directional inferences require prior specification.

## Explainer

A research question asks what is happening in the world: "Is there a relationship between sleep deprivation and working memory?" A hypothesis converts that question into a specific, falsifiable claim about what will happen in your study. The distinction between **directional** and **nondirectional** hypotheses is about how specific that claim is — and the specificity has real statistical and scientific consequences.

A **nondirectional hypothesis** (also called a two-tailed hypothesis) predicts that an effect exists without committing to its sign: "Sleep deprivation will affect working memory performance." This is appropriate when theory is silent about direction, when you're exploring a new phenomenon, or when the literature is genuinely mixed. A **directional hypothesis** (one-tailed) predicts both existence and direction: "Sleep deprivation will reduce working memory performance." From your prerequisite on probability, recall that a *p*-value represents the probability of observing data as extreme as yours if the null hypothesis were true. A two-tailed test splits that probability across both tails of the sampling distribution; a one-tailed test concentrates all of it in one tail. This is why directional tests have higher **statistical power** for detecting effects in the predicted direction — you're using your entire Type I error budget on one side.

But that power gain comes with a commitment you must take seriously. If you run a one-tailed test and observe a large effect in the *opposite* direction, the correct one-tailed result is non-significant (p > 0.05), even if a two-tailed test would have rejected the null. You have agreed to treat opposing-direction effects as chance results. If you're genuinely willing to make that agreement — because theory makes the opposite direction implausible or because you'd never act on an opposite-direction effect — then directional testing is scientifically defensible. If you're using directional tests opportunistically to squeeze significance out of marginal data, you've committed a form of *p*-hacking.

This is where your prerequisite on Bayes' theorem provides important context. The evidential weight of a directional hypothesis depends on how specific and prior-grounded it was. A directional prediction made *before* seeing any data, grounded in a solid meta-analytic literature, and preregistered carries far more evidential weight than one that looks directional in retrospect. The prior literature review (your soft prerequisite here) is not just scaffolding — it is the justification for the direction itself. Without that justification, a directional hypothesis is an assertion, not a prediction. Preregistration formalizes the commitment: once you've specified direction before data collection, you can't retroactively claim you predicted the opposite when the data come in pointing elsewhere.
