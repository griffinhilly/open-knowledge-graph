---
id: hyperparameter-optimization
title: Hyperparameter Optimization
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: supervised-learning-intro
  type: hard
- id: cross-validation-techniques
  type: hard
- id: constrained-optimization
  type: soft
tags:
- hyperparameter-tuning
- optimization
- model-selection
- bayesian-optimization
stage: advanced
status: draft
---

# Hyperparameter Optimization

## Core Idea
Hyperparameter optimization finds model hyperparameters (learning rate, regularization strength, tree depth) that maximize validation performance. Grid search exhaustively evaluates a preset grid; random search samples randomly; Bayesian optimization uses a probabilistic model to focus evaluation on promising regions, achieving better results with fewer evaluations.

## How It's Best Learned
Implement grid search and Bayesian optimization for hyperparameter tuning on a classification problem and compare efficiency in finding good hyperparameters.

## Explainer

When you train a supervised learning model, the algorithm learns **parameters** — weights, coefficients, splits — directly from data. But there is another class of settings you must choose *before* training begins: the learning rate, the strength of regularization, the depth of a decision tree, the number of hidden units. These are **hyperparameters**, and they control *how* the model learns rather than *what* it learns. Hyperparameter optimization is the systematic search for the combination of these settings that yields the best validation performance, using the cross-validation techniques you already know to honestly estimate generalization.

The simplest approach is **grid search**: you define a discrete set of values for each hyperparameter and evaluate every combination. If you have three hyperparameters with five values each, that is 125 training runs. Grid search is exhaustive and easy to parallelize, but it scales poorly — the number of combinations grows exponentially with the number of hyperparameters, a phenomenon called the curse of dimensionality. Worse, grid search wastes evaluations in regions of the space that clearly perform badly, because it must complete the entire grid regardless.

**Random search** offers a surprisingly effective alternative. Instead of evaluating every point on a grid, you sample hyperparameter combinations randomly from specified distributions. Research by Bergstra and Bengio showed that random search often finds good configurations faster than grid search, because most hyperparameters have unequal importance. If only one or two hyperparameters truly matter, random search explores more distinct values of those critical dimensions than a grid of the same budget would.

**Bayesian optimization** goes further by building a probabilistic surrogate model — typically a Gaussian process — that predicts validation performance as a function of hyperparameters. After each evaluation, the surrogate updates its beliefs about which regions are promising. An **acquisition function** (such as expected improvement) then selects the next point to evaluate, balancing exploration of uncertain regions against exploitation of known good regions. This directed search concentrates evaluations where they matter most, often finding strong configurations in far fewer trials than grid or random search. The trade-off is computational overhead per iteration and the complexity of implementing the surrogate, but for expensive models where each training run takes hours, the savings are substantial.
