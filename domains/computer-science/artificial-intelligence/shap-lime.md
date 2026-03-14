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
