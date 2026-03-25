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
- hyperparameter-optimization
tags:
- bayesian-optimization
- hyperparameter
- acquisition
stage: advanced
status: validated
---

# Bayesian Optimization

## Core Idea
Bayesian optimization efficiently searches hyperparameter spaces by modeling the objective as a Gaussian process and using acquisition functions to guide exploration. It balances exploration (trying unknown regions) and exploitation (refining good regions). This dramatically reduces function evaluations compared to grid or random search.

## Questions

```yaml
- question: "After 30 Bayesian optimization trials, the acquisition function assigns a high score to a point where the Gaussian process predicts only mediocre performance — lower than the current best. Why would Bayesian optimization choose to evaluate this point?"
  type: multiple-choice
  options:
    - "The acquisition function is malfunctioning — it should always select the point with the highest predicted mean"
    - "The point has high uncertainty, giving it high expected improvement potential even if the mean prediction is mediocre"
    - "Bayesian optimization ignores predicted means entirely and maximizes uncertainty only"
    - "The Gaussian process needs more evaluations before its predictions become reliable enough to trust"
  answer: 1
  explanation: "This is the exploration-exploitation tradeoff in action. Expected Improvement integrates over the GP's uncertainty: a point with mediocre predicted mean but high uncertainty has a meaningful probability of being much better than predicted, and thus high expected improvement. Maximizing the predicted mean alone (pure exploitation) would miss potentially good regions that haven't been explored. The acquisition function automatically handles this balance — it's not a bug but a core feature of why Bayesian optimization outperforms greedy search."

- question: "What does a Gaussian process contribute to Bayesian optimization that makes it fundamentally different from random search?"
  type: multiple-choice
  options:
    - "Predicted values at untried points, which random search also provides through interpolation"
    - "Both predicted values AND calibrated uncertainty estimates at every point, enabling principled exploration"
    - "Exact true values at untried points computed from the observed data analytically"
    - "A guarantee that the global optimum will be found within a fixed number of evaluations"
  answer: 1
  explanation: "The Gaussian process provides a probability distribution over function values at every untried point — not just a predicted value but also a confidence interval that widens where data is sparse and narrows where evaluations have occurred. This uncertainty map is what random search completely lacks. Without knowing where the function is well-explored versus unknown, random search cannot make informed decisions about where to look next. The uncertainty estimate is the key ingredient that allows the acquisition function to balance exploitation (high predicted value) and exploration (high uncertainty)."

- question: "Bayesian optimization is most valuable when each objective function evaluation is cheap, because the overhead of fitting and maximizing the Gaussian process is the main computational bottleneck."
  type: true-false
  answer: false
  explanation: "Bayesian optimization is most valuable when each evaluation is EXPENSIVE — training a large neural network, running a physical simulation, or conducting a wet-lab experiment. When evaluations are cheap, simpler methods like random search or grid search are perfectly adequate and have no GP overhead. The whole point of Bayesian optimization is to minimize the number of expensive evaluations by using every past result intelligently. The cost of fitting the GP (which scales cubically with observations) is trivial compared to the cost of model training runs measured in hours."

- question: "Expected Improvement (EI) as an acquisition function automatically handles the exploration-exploitation tradeoff without requiring a manually tuned exploration parameter."
  type: true-false
  answer: true
  explanation: "EI computes the expected amount by which a new point would surpass the current best observed value, integrating over the GP's uncertainty distribution. This formulation naturally produces exploration: where predictions are high and certain (good exploitation opportunity), EI is high. But where predictions are uncertain (unexplored territory), the probability of exceeding the current best through a lucky sample is also non-trivial, keeping EI high. As good regions become well-explored and their uncertainty drops, EI naturally shifts attention to uncertain regions — no manual temperature schedule or exploration parameter needed."

- question: "Explain why Bayesian optimization is more efficient than random search, focusing on how the surrogate model and acquisition function change where the algorithm looks next."
  type: short-answer
  answer: "Random search evaluates hyperparameter configurations blindly — each trial is independent of all previous results. Bayesian optimization instead fits a Gaussian process surrogate model to all past evaluations, giving it a probabilistic map of which regions look promising and which are uncertain. The acquisition function (e.g., Expected Improvement) then uses this map to select the single point most likely to improve on the best result so far, considering both predicted performance and prediction uncertainty. Each new evaluation updates the surrogate and refines the map, so later trials become increasingly targeted. The result is that Bayesian optimization concentrates evaluations in genuinely promising regions rather than sampling uniformly, typically finding near-optimal configurations in 20–50 trials where random search might need hundreds."
  explanation: "The efficiency gain is entirely due to the feedback loop: past observations inform future decisions, which is impossible in random or grid search. This matters most in regimes where evaluations are expensive (hours per trial) and budgets are limited (tens of trials total) — exactly the setting of deep learning hyperparameter tuning or drug discovery."
```

## Explainer

From your work with hyperparameter optimization, you know the basic problem: training a model with a given set of hyperparameters is expensive (minutes to hours per evaluation), and the search space can be large (learning rate, regularization strength, architecture choices, etc.). Grid search is exhaustive but wasteful; random search is better but still blind to the results of previous trials. **Bayesian optimization** is the principled alternative — it uses every past evaluation to decide where to look next.

The method has two components. First, a **surrogate model** — typically a **Gaussian process (GP)** — that approximates the unknown objective function (e.g., validation accuracy as a function of hyperparameters). After evaluating the objective at a few initial points, the GP fits a probabilistic model that provides not just a predicted value at any untried point, but also an uncertainty estimate. Where you have evaluated, the GP is confident and its predictions hug the observed values. Where you haven't evaluated, the GP is uncertain and its confidence bands widen. This uncertainty map is the key ingredient that grid and random search lack entirely.

Second, an **acquisition function** translates the GP's predictions and uncertainties into a score for each candidate point, answering "where should I evaluate next?" The most common acquisition function is **Expected Improvement (EI)**: given the best result observed so far, EI computes the expected amount by which a new point would improve upon it, integrating over the GP's uncertainty. Points where the GP predicts high performance score well (exploitation), but so do points where the GP is very uncertain, because they might harbor unexpectedly good results (exploration). This exploration-exploitation tradeoff is handled automatically — EI naturally favors uncertain regions when exploitation opportunities are exhausted and focuses on promising regions when they emerge.

The optimization loop is straightforward: (1) fit the GP to all observations so far, (2) maximize the acquisition function to select the next point to evaluate, (3) evaluate the true objective at that point, (4) add the result to the observation set, and repeat. Because maximizing the acquisition function is cheap (it's an analytical function of the GP, not a full model training run), the computational cost is dominated by the actual objective evaluations. In practice, Bayesian optimization typically finds near-optimal hyperparameters in 20–50 evaluations where random search might need hundreds, making it particularly valuable when each evaluation involves training a large model.

The approach does have limitations. Gaussian processes scale cubically with the number of observations, so they become unwieldy beyond a few thousand evaluations — though this rarely matters since the whole point is to minimize evaluations. High-dimensional search spaces (more than about 20 hyperparameters) challenge GPs because the surrogate model becomes too uncertain to guide search effectively. For these settings, variants like **Tree-structured Parzen Estimators (TPE)** used in Optuna, or random forest-based surrogates used in SMAC, provide scalable alternatives that maintain the Bayesian principle of learning from past evaluations without requiring a full GP.
