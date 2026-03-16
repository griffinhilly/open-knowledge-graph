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

## Explainer

From model interpretability, you know that understanding *why* a model made a specific prediction is essential for trust, debugging, and compliance. **SHAP** and **LIME** are two of the most widely used tools for producing those explanations, and both share a crucial property: they are **model-agnostic**, meaning they work with any model — neural networks, random forests, gradient boosting — by treating the model as a black box and probing its behavior from the outside.

**LIME** (Local Interpretable Model-agnostic Explanations) explains a single prediction by building a simple, interpretable model that approximates the complex model's behavior *in the neighborhood of that prediction*. Here is the intuition: even if a model's global decision boundary is hopelessly complex, the boundary near any single point is approximately linear. LIME generates perturbed versions of the input (slightly modified copies), feeds them through the black-box model, and fits a weighted linear model to the results — weighting nearby perturbations more heavily. The coefficients of that linear model tell you which features pushed the prediction up or down. For example, when explaining why a text classifier labeled a review as negative, LIME might show that the words "disappointing" and "broken" contributed most to the negative classification, while "arrived quickly" pushed toward positive.

**SHAP** (SHapley Additive exPlanations) takes a different, more principled approach grounded in cooperative game theory. The core idea comes from **Shapley values**, a concept from economics that fairly distributes a team's total payoff among its members based on each member's marginal contribution. In the SHAP framework, the "team" is the set of features, and the "payoff" is the model's prediction. For each feature, SHAP computes its average marginal contribution across all possible subsets of features — how much does adding this feature change the prediction, averaged over every possible combination of the other features? This produces a unique set of attribution values with strong theoretical guarantees: the feature contributions sum exactly to the difference between the model's prediction and its average prediction, and features that contribute nothing always receive zero attribution.

The practical tradeoff between the two methods is cost versus rigor. LIME is fast and intuitive but its explanations can vary between runs (different perturbation samples yield slightly different linear fits), and it makes assumptions about what "local" means that may not suit every problem. SHAP provides theoretically grounded, consistent attributions, but computing exact Shapley values requires evaluating the model on exponentially many feature subsets — making it expensive for high-dimensional inputs unless you use optimized variants like TreeSHAP (for tree-based models) or KernelSHAP (a sampling approximation). In practice, many practitioners use both: LIME for quick, per-prediction explanations during development, and SHAP for rigorous feature importance analysis and global summaries that aggregate local explanations across the entire dataset.
