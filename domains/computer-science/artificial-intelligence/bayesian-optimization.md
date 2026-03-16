---
id: bayesian-optimization
title: Bayesian Optimization
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: hyperparameter-optimization
  type: hard
- id: bayes-theorem-and-inference
  type: soft
- id: expected-value-and-variance
  type: soft
builds-toward:
- hyperparameter-tuning
- acquisition-functions
tags:
- bayesian-optimization
- hyperparameter
- acquisition
stage: advanced
status: draft
---

# Bayesian Optimization

## Core Idea
Bayesian optimization efficiently searches hyperparameter spaces by modeling the objective as a Gaussian process and using acquisition functions to guide exploration. It balances exploration (trying unknown regions) and exploitation (refining good regions). This dramatically reduces function evaluations compared to grid or random search.

## Explainer

From your work with hyperparameter optimization, you know the basic problem: training a model with a given set of hyperparameters is expensive (minutes to hours per evaluation), and the search space can be large (learning rate, regularization strength, architecture choices, etc.). Grid search is exhaustive but wasteful; random search is better but still blind to the results of previous trials. **Bayesian optimization** is the principled alternative — it uses every past evaluation to decide where to look next.

The method has two components. First, a **surrogate model** — typically a **Gaussian process (GP)** — that approximates the unknown objective function (e.g., validation accuracy as a function of hyperparameters). After evaluating the objective at a few initial points, the GP fits a probabilistic model that provides not just a predicted value at any untried point, but also an uncertainty estimate. Where you have evaluated, the GP is confident and its predictions hug the observed values. Where you haven't evaluated, the GP is uncertain and its confidence bands widen. This uncertainty map is the key ingredient that grid and random search lack entirely.

Second, an **acquisition function** translates the GP's predictions and uncertainties into a score for each candidate point, answering "where should I evaluate next?" The most common acquisition function is **Expected Improvement (EI)**: given the best result observed so far, EI computes the expected amount by which a new point would improve upon it, integrating over the GP's uncertainty. Points where the GP predicts high performance score well (exploitation), but so do points where the GP is very uncertain, because they might harbor unexpectedly good results (exploration). This exploration-exploitation tradeoff is handled automatically — EI naturally favors uncertain regions when exploitation opportunities are exhausted and focuses on promising regions when they emerge.

The optimization loop is straightforward: (1) fit the GP to all observations so far, (2) maximize the acquisition function to select the next point to evaluate, (3) evaluate the true objective at that point, (4) add the result to the observation set, and repeat. Because maximizing the acquisition function is cheap (it's an analytical function of the GP, not a full model training run), the computational cost is dominated by the actual objective evaluations. In practice, Bayesian optimization typically finds near-optimal hyperparameters in 20–50 evaluations where random search might need hundreds, making it particularly valuable when each evaluation involves training a large model.

The approach does have limitations. Gaussian processes scale cubically with the number of observations, so they become unwieldy beyond a few thousand evaluations — though this rarely matters since the whole point is to minimize evaluations. High-dimensional search spaces (more than about 20 hyperparameters) challenge GPs because the surrogate model becomes too uncertain to guide search effectively. For these settings, variants like **Tree-structured Parzen Estimators (TPE)** used in Optuna, or random forest-based surrogates used in SMAC, provide scalable alternatives that maintain the Bayesian principle of learning from past evaluations without requiring a full GP.
