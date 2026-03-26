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
status: validated
---

# Hyperparameter Optimization

## Core Idea
Hyperparameter optimization finds model hyperparameters (learning rate, regularization strength, tree depth) that maximize validation performance. Grid search exhaustively evaluates a preset grid; random search samples randomly; Bayesian optimization uses a probabilistic model to focus evaluation on promising regions, achieving better results with fewer evaluations.

## How It's Best Learned
Implement grid search and Bayesian optimization for hyperparameter tuning on a classification problem and compare efficiency in finding good hyperparameters.

## Questions

```yaml
- question: "A model has 6 hyperparameters, but only learning rate and batch size meaningfully affect performance. A researcher runs 50 evaluations. Compared to grid search over all 6 parameters, random search would most likely:"
  type: multiple-choice
  options:
    - "Perform worse because it does not evaluate every combination systematically"
    - "Perform comparably because both methods sample the same number of configurations"
    - "Find better learning rate and batch size values because it explores more distinct values of those important dimensions per evaluation"
    - "Only outperform grid search for deep learning models, not other model types"
  answer: 2
  explanation: "When only a subset of hyperparameters truly matters, grid search wastes most of its budget varying the unimportant ones. With 6 hyperparameters at 5 values each, a grid has 15,625 points — most varying hyperparameters that don't matter. Random search with 50 evaluations will hit many more distinct values of the 2 critical hyperparameters across their full range. Bergstra and Bengio (2012) demonstrated this empirically: random search often finds good configurations faster than grid search of the same budget."

- question: "What distinguishes Bayesian optimization from both grid and random search in how it selects configurations to evaluate?"
  type: multiple-choice
  options:
    - "It evaluates every combination in the hyperparameter space exhaustively before reporting results"
    - "It samples configurations randomly but then applies a filter to remove obviously bad ones"
    - "It builds a probabilistic surrogate model of the performance landscape and uses an acquisition function to direct evaluations toward promising regions"
    - "It fixes the least important hyperparameters first and then exhaustively searches the remaining ones"
  answer: 2
  explanation: "Bayesian optimization uses a surrogate model (typically a Gaussian process) that represents current beliefs about how hyperparameters map to validation performance. After each evaluation, the model updates its beliefs, and an acquisition function (such as expected improvement) selects the next most informative configuration — balancing exploitation (near known good regions) and exploration (uncertain regions). This directed search is fundamentally different from the blind sampling of grid and random search."

- question: "Random search is almost seldom better than grid search for hyperparameter optimization because grid search is exhaustive and therefore expected to find the optimal combination."
  type: true-false
  answer: false
  explanation: "Grid search is exhaustive only within the discrete grid you define — it cannot be practically exhaustive for continuous hyperparameter spaces. More importantly, random search consistently outperforms grid search when hyperparameters have unequal importance (which is typical). For the same evaluation budget, random search explores more distinct values of the important hyperparameters. Grid search wastes evaluations on combinations that vary only unimportant hyperparameters while holding important ones fixed at the same few grid values."

- question: "Bayesian optimization uses an acquisition function to balance exploring uncertain regions of the hyperparameter space against exploiting regions already known to perform well."
  type: true-false
  answer: true
  explanation: "The acquisition function (e.g., expected improvement, upper confidence bound) operationalizes the exploration-exploitation tradeoff. Regions of the hyperparameter space that the surrogate model is uncertain about (high variance) have high exploration value; regions near previously good configurations have high exploitation value. By weighing both, Bayesian optimization avoids both excessive exploitation (getting stuck at a local optimum) and excessive exploration (evaluating configurations that are unlikely to be good)."

- question: "Why does Bayesian optimization typically require fewer training runs than random search to find a high-performing hyperparameter configuration, and when is this advantage most valuable?"
  type: short-answer
  answer: "Bayesian optimization builds a surrogate model that learns the shape of the performance landscape — which regions of hyperparameter space tend to produce high validation scores — and uses this learned model to direct future evaluations. Rather than sampling blindly, it concentrates evaluations where the acquisition function predicts the most gain. This is most valuable when each training run is expensive (hours or days), such as large deep learning models. For cheap models where 1,000 random evaluations are feasible in minutes, the overhead of maintaining the surrogate may not justify the complexity."
  explanation: "The computational overhead of Bayesian optimization (fitting and querying the surrogate model) is negligible compared to training runs that take hours. For a model where each run takes 4 hours, 50 Bayesian evaluations (~8 days) may find better hyperparameters than 200 random evaluations (~33 days). For a model that trains in seconds, random search over thousands of configurations is simpler and nearly as effective."
```

## Explainer

When you train a supervised learning model, the algorithm learns **parameters** — weights, coefficients, splits — directly from data. But there is another class of settings you must choose *before* training begins: the learning rate, the strength of regularization, the depth of a decision tree, the number of hidden units. These are **hyperparameters**, and they control *how* the model learns rather than *what* it learns. Hyperparameter optimization is the systematic search for the combination of these settings that yields the best validation performance, using the cross-validation techniques you already know to honestly estimate generalization.

The simplest approach is **grid search**: you define a discrete set of values for each hyperparameter and evaluate every combination. If you have three hyperparameters with five values each, that is 125 training runs. Grid search is exhaustive and easy to parallelize, but it scales poorly — the number of combinations grows exponentially with the number of hyperparameters, a phenomenon called the curse of dimensionality. Worse, grid search wastes evaluations in regions of the space that clearly perform badly, because it must complete the entire grid regardless.

**Random search** offers a surprisingly effective alternative. Instead of evaluating every point on a grid, you sample hyperparameter combinations randomly from specified distributions. Research by Bergstra and Bengio showed that random search often finds good configurations faster than grid search, because most hyperparameters have unequal importance. If only one or two hyperparameters truly matter, random search explores more distinct values of those critical dimensions than a grid of the same budget would.

**Bayesian optimization** goes further by building a probabilistic surrogate model — typically a Gaussian process — that predicts validation performance as a function of hyperparameters. After each evaluation, the surrogate updates its beliefs about which regions are promising. An **acquisition function** (such as expected improvement) then selects the next point to evaluate, balancing exploration of uncertain regions against exploitation of known good regions. This directed search concentrates evaluations where they matter most, often finding strong configurations in far fewer trials than grid or random search. The trade-off is computational overhead per iteration and the complexity of implementing the surrogate, but for expensive models where each training run takes hours, the savings are substantial.
