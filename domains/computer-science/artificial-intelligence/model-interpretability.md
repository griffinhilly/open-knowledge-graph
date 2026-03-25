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
tags:
- interpretability
- explainability
- transparency
stage: advanced
status: validated
---

# Model Interpretability and Explainability

## Core Idea
Model interpretability answers why models make specific predictions, enabling debugging, building trust, and meeting regulatory requirements. Approaches include saliency maps (highlighting important input regions), attention visualization, and feature importance measures. Both global (model-wide) and local (per-prediction) explanations are valuable.

## Questions

```yaml
- question: "A medical AI model achieves 97% accuracy at detecting tumors from X-ray scans. Saliency maps show the model highlights a region in the corner of each image — the same region where a metal ruler used during imaging always appears. What does this scenario most directly illustrate about interpretability?"
  type: multiple-choice
  options:
    - "Saliency maps are fundamentally unreliable and should never be used to explain medical AI decisions"
    - "High accuracy guarantees that the model has learned clinically meaningful features"
    - "Interpretability tools require validation against ground truth — a plausible-looking explanation can still reflect a spurious correlation rather than the model's genuine reasoning"
    - "The model must be retrained on ruler-free images before any explanation can be trusted"
  answer: 2
  explanation: "This is the classic 'clever Hans' failure in interpretability: the model achieves high accuracy by exploiting a spurious artifact (the ruler correlates with how images were labeled) rather than tumor features. The saliency map correctly reveals what the model is doing — but 'correctly revealing a spurious strategy' is not the same as 'the explanation looks clinically valid.' Interpretability tools must be validated against known ground truth (e.g., human expert annotations of which regions are clinically relevant) to confirm they are revealing genuine reasoning. High accuracy alone is insufficient evidence."

- question: "SHAP values are computed to explain why a specific patient's loan application was denied, citing that their debt-to-income ratio was the most influential feature for this decision. This represents which type of interpretability?"
  type: multiple-choice
  options:
    - "Global intrinsic — it uses a transparent model structure that is interpretable by design"
    - "Global post-hoc — it summarizes feature importance across the entire model"
    - "Local post-hoc — it explains a single prediction using a method applied after training"
    - "Local intrinsic — it uses a simple model that is inherently transparent for individual predictions"
  answer: 2
  explanation: "Local methods explain individual predictions ('why did *this* applicant get denied?'), while global methods explain overall model behavior ('which features matter most across all decisions?'). Post-hoc methods are applied to an already-trained model, as opposed to intrinsic methods that use a model transparent by design (like a short decision tree). SHAP applied to explain one specific prediction is local and post-hoc. Understanding this two-axis framework (local/global × intrinsic/post-hoc) helps choose the right tool for the need."

- question: "A perfectly faithful explanation of a neural network's prediction would be at least as difficult to interpret as the model itself."
  type: true-false
  answer: true
  explanation: "This is the core faithfulness-simplicity tradeoff. A perfectly faithful explanation would reproduce every nonlinear transformation, every weight interaction, and every layer computation — which is exactly the model. The model is already opaque, so a faithful explanation is equally opaque. Useful explanations simplify, but every simplification risks distorting what the model actually computed. This tension means 'more interpretable' and 'more faithful' are opposing directions, not the same direction."

- question: "Interpretability methods are most valuable after a model fails in production, since there is no benefit to examining model reasoning on a well-performing system."
  type: true-false
  answer: false
  explanation: "Interpretability is valuable before deployment as a debugging tool — it can reveal that a high-accuracy model has learned spurious correlations (like the ruler example) that will fail on slightly different data distributions. It is also valuable during development for building trust and ensuring alignment with domain knowledge. Post-failure analysis is important, but waiting until failure means the spurious strategy has already caused harm. Regulatory requirements in many jurisdictions also mandate explanations at prediction time, not just post-failure."

- question: "Why is a perfectly faithful explanation of a neural network's prediction inherently self-defeating as a practical tool?"
  type: short-answer
  answer: "A perfectly faithful explanation would have to reproduce the model's full computation — all the weights, nonlinear activations, and layer-by-layer transformations. But that is just the model itself, which is the thing we found opaque in the first place. Practical explanations must simplify the model's behavior into something a human can understand, and every simplification introduces distortion. The more interpretable the explanation, the less it can capture the model's full behavior."
  explanation: "This self-defeating quality is why the field focuses on 'useful approximations' rather than exact explanations. Methods like LIME (local linear approximation), SHAP (Shapley value attribution), and saliency maps all trade faithfulness for comprehensibility. The honest interpretation of any interpretability output is: 'this is how the model appears to behave in this region, under this simplifying assumption' — not 'this is exactly what the model computed.' Good interpretability practice uses multiple complementary methods and validates them against known ground truth."
```

## Explainer

From your introduction to neural networks, you know that deep models can learn powerful mappings from inputs to outputs — but that power comes at a cost. A neural network with millions of parameters produces predictions through a chain of nonlinear transformations that no human can trace by hand. **Model interpretability** is the discipline of opening that black box: understanding not just *what* a model predicts, but *why* it predicts it.

The need for interpretability goes beyond intellectual curiosity. If a medical imaging model flags a scan as cancerous, a doctor needs to know whether it is responding to actual tumor features or to an artifact like a ruler left in the image. If a loan approval model rejects an applicant, regulations in many jurisdictions require an explanation. And during development, interpretability is a debugging tool: if your model achieves high accuracy by exploiting a spurious correlation (like learning that photos with green backgrounds are usually "outdoor" scenes), you want to catch that before deployment.

Interpretability methods fall along two axes. **Global** methods explain the model's overall behavior — which features matter most across all predictions, or what patterns each neuron has learned to detect. **Local** methods explain a single prediction — why *this* input received *this* output. A second axis distinguishes **intrinsic** interpretability (models that are transparent by design, like short decision trees or linear models) from **post-hoc** methods that analyze an already-trained model. Saliency maps, for instance, compute gradients of the output with respect to input pixels, highlighting which regions most influenced the prediction. Attention visualization in transformer models shows which input tokens the model "focused on" when producing each output.

The central tension in interpretability is faithfulness versus simplicity. A perfectly faithful explanation would reproduce the model's full computation — but then it would be as complex as the model itself and equally opaque. Useful explanations simplify, and every simplification risks distorting what the model actually does. A saliency map might highlight the right region for the wrong reason; an attention weight might be high on a token that the model ultimately ignores in later layers. Good interpretability practice means using multiple complementary methods, validating explanations against known ground truth, and remaining skeptical of any single explanation technique.
