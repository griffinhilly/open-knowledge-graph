---
id: loss-functions
title: Loss Functions and Objective Functions
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: neural-networks-intro
  type: hard
- id: gradient-descent-optimization
  type: hard
- id: partial-derivatives
  type: soft
- id: derivatives-of-exponential-functions
  type: soft
builds-toward:
- backpropagation
- optimization-algorithms
tags:
- loss
- objective
- training
stage: advanced
status: draft
---

# Loss Functions and Objective Functions

## Core Idea
Loss functions quantify the error between predicted outputs and actual targets, defining what the model learns to minimize during training. Common choices include mean squared error for regression, cross-entropy for classification, and Huber loss for robustness to outliers. Selecting an appropriate loss function directly shapes model behavior and final performance.

## How It's Best Learned
Implement MSE, cross-entropy, and Huber loss from scratch. Compare convergence on toy datasets; observe how different losses affect learning dynamics.

## Common Misconceptions
Loss and accuracy are distinct metrics; optimizing loss does not guarantee optimal accuracy. Not all problems suit standard losses; domain knowledge may suggest custom objectives.

## Explainer

You already know that a neural network adjusts its weights through gradient descent — but gradient descent needs a direction, and the **loss function** is what provides it. A loss function takes the model's prediction and the true target, and returns a single number measuring how wrong the prediction is. Training then becomes an optimization problem: find the weights that minimize this number across the dataset. The choice of loss function is not a technicality — it defines what "wrong" means, and different definitions lead to fundamentally different model behaviors.

For regression tasks, the most common choice is **mean squared error** (MSE), which computes the average of the squared differences between predictions and targets. Squaring amplifies large errors, so MSE-trained models aggressively penalize big mistakes. This is useful when outliers genuinely matter, but problematic when your data contains noise or extreme values you would rather downweight. **Mean absolute error** (MAE) treats all errors linearly and is more robust to outliers, but its gradient is constant regardless of error size, which can make optimization less smooth. The **Huber loss** blends both: it behaves like MSE for small errors (smooth gradients near the minimum) and like MAE for large errors (bounded influence of outliers), controlled by a threshold parameter delta.

For classification, the standard is **cross-entropy loss**, which measures the divergence between the predicted probability distribution and the true label distribution. If your model predicts a probability of 0.9 for the correct class, the loss is small; if it predicts 0.01, the loss is very large. Cross-entropy has a crucial property: its gradient with respect to the output logits is simply the difference between predicted and true probabilities, which connects directly to the partial derivatives you have studied. This clean gradient signal is why cross-entropy trains faster and more reliably than alternatives like MSE applied to classification outputs.

Understanding the relationship between loss and evaluation metrics is essential. **Loss is what the model optimizes; metrics like accuracy, precision, or F1 are what you care about.** These are not the same thing. A model can decrease its loss while accuracy stays flat, especially when the model is becoming more calibrated in its probability estimates without changing its top prediction. Conversely, a small change in loss near a decision boundary can flip predictions and cause a large jump in accuracy. This disconnect is why you should always monitor both during training. In specialized domains, you may even design custom loss functions — for instance, weighting false negatives more heavily than false positives in medical diagnosis — because the standard losses treat all errors equally, and your problem may not.
