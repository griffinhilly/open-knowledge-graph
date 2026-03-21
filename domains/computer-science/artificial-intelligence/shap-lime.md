---
id: shap-lime
title: SHAP and LIME Explanations
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: model-interpretability
  type: hard
builds-toward:
- fairness-machine-learning
- feature-importance
tags:
- shap
- lime
- explanation
stage: advanced
status: draft
---

# SHAP and LIME Explanations

## Core Idea
SHAP (SHapley Additive exPlanations) and LIME (Local Interpretable Model-agnostic Explanations) explain individual predictions model-agnostically. SHAP uses game-theoretic Shapley values assigning feature contributions; LIME fits local linear approximations. SHAP enables both local explanations and global summaries across predictions.

## Questions

```yaml
- question: "A data scientist uses LIME to explain why a loan application was denied: 'income' contributes –0.3 and 'debt' contributes –0.4. She reruns LIME on the same prediction and gets slightly different numbers. What explains this?"
  type: multiple-choice
  options:
    - "LIME is broken; explanations for the same prediction must always be identical"
    - "LIME generates perturbed samples randomly, so different sampling runs produce slightly different local linear fits"
    - "SHAP was accidentally used instead; SHAP produces variable results between runs"
    - "The model changed between runs, producing different predictions"
  answer: 1
  explanation: "LIME works by randomly perturbing the input, feeding perturbations through the black-box model, and fitting a local linear model weighted by proximity. Because perturbations are sampled randomly, different runs yield different datasets and thus slightly different linear fits — a known limitation. SHAP, by contrast, has a unique deterministic solution grounded in Shapley values, making its attributions consistent across runs."

- question: "A credit scoring model uses 50 features. SHAP's feature attributions for a given prediction will always sum to the model's prediction minus the average prediction across all training examples."
  type: true-false
  answer: true
  explanation: "This is SHAP's 'efficiency' axiom from Shapley value theory: the sum of all SHAP values for a prediction equals the difference between that specific prediction and the model's baseline (typically the average prediction). This means the explanation accounts for the full prediction with no unexplained residual — a theoretical guarantee that LIME does not provide."

- question: "LIME and SHAP both explain individual model predictions, so they can be used interchangeably for any explanation task."
  type: true-false
  answer: false
  explanation: "While both are model-agnostic local explanation methods, they differ importantly. LIME can vary between runs (different perturbation samples) and has no global consistency guarantee. SHAP provides theoretically grounded, consistent attributions that can be aggregated across predictions for global summaries (e.g., SHAP summary plots). For high-stakes or global feature importance analysis, SHAP is preferable; for quick exploratory explanations, LIME may suffice."

- question: "What is the key idea behind Shapley values, and why does it make SHAP's attribution more principled than a model's internal feature weights?"
  type: short-answer
  answer: "Shapley values compute each feature's average marginal contribution across all possible subsets of features — not just when all features are present simultaneously. This correctly handles feature interactions and redundancies. A model's internal weight measures a feature's contribution given all other features, which can be unstable or misleading when features are correlated. Shapley values distribute credit fairly among all features by averaging over every possible ordering of feature inclusion."
  explanation: "If two features are highly correlated, internal weights can split arbitrarily between them. Shapley values solve this by considering every possible coalition: how much does feature A contribute when only it is present? When it and B are present? All three? Averaging over these coalitions gives stable, fair attributions even with correlated features."

- question: "TreeSHAP is preferred over KernelSHAP for gradient-boosted tree models primarily because:"
  type: multiple-choice
  options:
    - "TreeSHAP uses LIME's local approximation approach, which is faster for tree-structured models"
    - "TreeSHAP exploits the tree structure to compute exact Shapley values in polynomial time, while KernelSHAP requires sampling and is approximate"
    - "KernelSHAP cannot handle categorical features, which tree models commonly use"
    - "TreeSHAP produces higher attribution magnitudes, making features appear more important"
  answer: 1
  explanation: "Exact Shapley values require evaluating the model on exponentially many feature subsets — infeasible for high-dimensional inputs. KernelSHAP approximates this by sampling. TreeSHAP exploits the tree data structure to compute exact Shapley values in polynomial time (O(TLD²) for T trees, L leaves, D depth). This makes TreeSHAP both faster and exact for tree-based models like XGBoost or random forests."
```

## Explainer

From model interpretability, you know that understanding *why* a model made a specific prediction is essential for trust, debugging, and compliance. **SHAP** and **LIME** are two of the most widely used tools for producing those explanations, and both share a crucial property: they are **model-agnostic**, meaning they work with any model — neural networks, random forests, gradient boosting — by treating the model as a black box and probing its behavior from the outside.

**LIME** (Local Interpretable Model-agnostic Explanations) explains a single prediction by building a simple, interpretable model that approximates the complex model's behavior *in the neighborhood of that prediction*. Here is the intuition: even if a model's global decision boundary is hopelessly complex, the boundary near any single point is approximately linear. LIME generates perturbed versions of the input (slightly modified copies), feeds them through the black-box model, and fits a weighted linear model to the results — weighting nearby perturbations more heavily. The coefficients of that linear model tell you which features pushed the prediction up or down. For example, when explaining why a text classifier labeled a review as negative, LIME might show that the words "disappointing" and "broken" contributed most to the negative classification, while "arrived quickly" pushed toward positive.

**SHAP** (SHapley Additive exPlanations) takes a different, more principled approach grounded in cooperative game theory. The core idea comes from **Shapley values**, a concept from economics that fairly distributes a team's total payoff among its members based on each member's marginal contribution. In the SHAP framework, the "team" is the set of features, and the "payoff" is the model's prediction. For each feature, SHAP computes its average marginal contribution across all possible subsets of features — how much does adding this feature change the prediction, averaged over every possible combination of the other features? This produces a unique set of attribution values with strong theoretical guarantees: the feature contributions sum exactly to the difference between the model's prediction and its average prediction, and features that contribute nothing always receive zero attribution.

The practical tradeoff between the two methods is cost versus rigor. LIME is fast and intuitive but its explanations can vary between runs (different perturbation samples yield slightly different linear fits), and it makes assumptions about what "local" means that may not suit every problem. SHAP provides theoretically grounded, consistent attributions, but computing exact Shapley values requires evaluating the model on exponentially many feature subsets — making it expensive for high-dimensional inputs unless you use optimized variants like TreeSHAP (for tree-based models) or KernelSHAP (a sampling approximation). In practice, many practitioners use both: LIME for quick, per-prediction explanations during development, and SHAP for rigorous feature importance analysis and global summaries that aggregate local explanations across the entire dataset.
