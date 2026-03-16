---
id: model-interpretability
title: Model Interpretability and Explainability
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: neural-networks-intro
  type: soft
builds-toward:
- shap-lime
- feature-importance
tags:
- interpretability
- explainability
- transparency
stage: advanced
status: draft
---

# Model Interpretability and Explainability

## Core Idea
Model interpretability answers why models make specific predictions, enabling debugging, building trust, and meeting regulatory requirements. Approaches include saliency maps (highlighting important input regions), attention visualization, and feature importance measures. Both global (model-wide) and local (per-prediction) explanations are valuable.

## Explainer

From your introduction to neural networks, you know that deep models can learn powerful mappings from inputs to outputs — but that power comes at a cost. A neural network with millions of parameters produces predictions through a chain of nonlinear transformations that no human can trace by hand. **Model interpretability** is the discipline of opening that black box: understanding not just *what* a model predicts, but *why* it predicts it.

The need for interpretability goes beyond intellectual curiosity. If a medical imaging model flags a scan as cancerous, a doctor needs to know whether it is responding to actual tumor features or to an artifact like a ruler left in the image. If a loan approval model rejects an applicant, regulations in many jurisdictions require an explanation. And during development, interpretability is a debugging tool: if your model achieves high accuracy by exploiting a spurious correlation (like learning that photos with green backgrounds are usually "outdoor" scenes), you want to catch that before deployment.

Interpretability methods fall along two axes. **Global** methods explain the model's overall behavior — which features matter most across all predictions, or what patterns each neuron has learned to detect. **Local** methods explain a single prediction — why *this* input received *this* output. A second axis distinguishes **intrinsic** interpretability (models that are transparent by design, like short decision trees or linear models) from **post-hoc** methods that analyze an already-trained model. Saliency maps, for instance, compute gradients of the output with respect to input pixels, highlighting which regions most influenced the prediction. Attention visualization in transformer models shows which input tokens the model "focused on" when producing each output.

The central tension in interpretability is faithfulness versus simplicity. A perfectly faithful explanation would reproduce the model's full computation — but then it would be as complex as the model itself and equally opaque. Useful explanations simplify, and every simplification risks distorting what the model actually does. A saliency map might highlight the right region for the wrong reason; an attention weight might be high on a token that the model ultimately ignores in later layers. Good interpretability practice means using multiple complementary methods, validating explanations against known ground truth, and remaining skeptical of any single explanation technique.
