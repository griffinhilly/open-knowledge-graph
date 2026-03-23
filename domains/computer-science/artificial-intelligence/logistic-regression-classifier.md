---
id: logistic-regression-classifier
title: Logistic Regression for Classification
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: linear-regression-ml
  type: hard
- id: probability-basics
  type: hard
- id: probability-axioms
  type: soft
- id: derivatives-of-exponential-functions
  type: soft
- id: partial-derivatives
  type: soft
- id: derivatives-of-logarithmic-functions
  type: soft
- id: conditional-probability
  type: soft
- id: probability-rules-for-events
  type: soft
tags:
- supervised-learning
- classification
- probabilistic
stage: advanced
status: validated
---

# Logistic Regression for Classification

## Core Idea
Logistic regression outputs class probabilities via the logistic function applied to linear combinations of features. Cross-entropy loss is minimized via gradient descent. Despite its name, it is a classification algorithm modeling P(y=1|x).

## How It's Best Learned
Implement logistic regression with cross-entropy loss, visualize decision boundaries on 2D data, and compare ROC curves.

## Common Misconceptions
Logistic regression outputs probabilities, not binary labels; thresholding is needed for classification. It assumes linear separability; overlapping classes degrade performance.

## Questions

```yaml
- question: "A logistic regression model outputs 0.73 for a patient in a cancer screening dataset. A colleague says 'the model predicted cancer.' What is missing from this interpretation?"
  type: multiple-choice
  options:
    - "Nothing is missing — 0.73 means the model predicts cancer, since it is greater than 0.5"
    - "The decision threshold: 0.73 is a probability, and classification requires a separate threshold choice. The default 0.5 is not always correct"
    - "The model should output 0 or 1 directly; 0.73 indicates the model is poorly calibrated"
    - "The model must be compared to a baseline before any prediction can be made"
  answer: 1
  explanation: "Logistic regression outputs P(y=1|x) — a probability, not a label. Whether 0.73 maps to 'cancer' depends on the decision threshold you choose. With a threshold of 0.5, yes, 0.73 → 'positive', but in a screening context you might lower the threshold (e.g., 0.3) to catch more true positives at the cost of more false positives. Option A embeds the assumption that 0.5 is always the threshold, which conflates the model's output with a design choice that should be made separately."

- question: "A logistic regression is trained on two features x₁ and x₂. A student claims the decision boundary must be curved because the sigmoid function is nonlinear. Is the student correct?"
  type: multiple-choice
  options:
    - "Yes — the sigmoid introduces nonlinearity, so the boundary is a curve in feature space"
    - "No — the decision boundary is where the linear combination w₁x₁ + w₂x₂ + b = 0, which is always a straight line (or hyperplane), regardless of the sigmoid"
    - "It depends — the boundary is linear only if the two classes are perfectly separable"
    - "Yes — the boundary is nonlinear unless regularization is applied"
  answer: 1
  explanation: "The sigmoid is nonlinear in terms of the output probability, but the decision boundary is the set of points where P(y=1|x) = 0.5, which corresponds to the linear combination equaling zero. That equation defines a straight line in 2D or a hyperplane in higher dimensions — always linear. This is a fundamental limitation of logistic regression: it cannot learn XOR-like patterns without feature engineering. The nonlinearity of the sigmoid shapes the probability surface, not the decision boundary itself."

- question: "Logistic regression directly outputs a binary classification label (0 or 1) for each input."
  type: true-false
  answer: false
  explanation: "Logistic regression outputs a continuous probability P(y=1|x) ∈ (0,1) via the sigmoid function. Converting this to a binary label requires applying a decision threshold — typically 0.5, but this is a separate design choice that trades off precision and recall. The probabilistic output is one of logistic regression's strengths: it encodes the model's confidence, not just its direction."

- question: "Cross-entropy loss penalizes confident wrong predictions more severely than mean squared error, making it better suited for logistic regression training."
  type: true-false
  answer: true
  explanation: "Cross-entropy loss is −[y·log(p) + (1−y)·log(1−p)]. When the model predicts p ≈ 0.99 but the true label is y = 0, the loss is −log(0.01) ≈ 4.6 — enormous. Squared error would give (0.99)² ≈ 0.98, a moderate penalty. Cross-entropy is also derived from maximum likelihood estimation of a Bernoulli distribution and produces well-behaved gradients for sigmoid outputs, whereas squared error on sigmoid outputs can cause vanishing gradients during training."

- question: "Why is mean squared error (MSE) not the standard loss function for logistic regression, even though logistic regression uses a regression-like framework?"
  type: short-answer
  answer: "MSE applied to sigmoid outputs produces a non-convex loss surface with vanishing gradients when the sigmoid is saturated (near 0 or 1), making gradient descent unreliable. Cross-entropy loss is statistically principled — it is the negative log-likelihood of a Bernoulli distribution, which is exactly the distributional assumption behind binary classification. It is convex in the weights, guaranteeing a global optimum, and its gradient simplifies cleanly to (predicted − true) × input, making updates interpretable and efficient."
  explanation: "The historical name 'logistic regression' reflects its origins in regression-like linear modeling, but the task is classification and the appropriate loss function follows from the probabilistic framework. MSE treats the output as if it were a continuous measurement, which is the wrong model. Cross-entropy treats the output as a probability, which is the right model. The mismatch between loss function and output interpretation is not just aesthetic — it leads to slower convergence and can miss the global optimum entirely."
```

## Explainer

You already know how linear regression fits a line to predict a continuous value. Logistic regression starts from the same foundation — a linear combination of features, w₁x₁ + w₂x₂ + ... + b — but asks a different question: instead of "what value?", it asks "which class?" The problem is that a raw linear combination can produce any real number, while a probability must stay between 0 and 1. The **logistic function** (also called the sigmoid), σ(z) = 1/(1 + e⁻ᶻ), solves this by squashing any real-valued input into the (0, 1) range. Feed the linear combination through the sigmoid, and you get P(y = 1 | x) — the model's estimated probability that the input belongs to the positive class.

This probabilistic output is what makes logistic regression fundamentally different from just drawing a dividing line. The model does not output "yes" or "no" directly; it outputs a number like 0.82, meaning "82% chance of class 1." You choose a **decision threshold** (typically 0.5) to convert this probability into a hard prediction, but the threshold is a separate design choice. Moving it up or down trades off precision against recall — something you can visualize with an ROC curve. The decision boundary itself — the set of points where P(y = 1 | x) = 0.5 — is always a straight line (or hyperplane in higher dimensions), because it corresponds to the set of inputs where the linear combination equals zero.

Training logistic regression means finding the weights that make the model's predicted probabilities match the observed labels as closely as possible. The right loss function here is **cross-entropy loss** (also called log loss), not squared error. Cross-entropy penalizes confident wrong predictions severely: if the model says P(y = 1) = 0.99 but the true label is 0, the loss is enormous. This is derived from maximum likelihood estimation — you are maximizing the likelihood of the observed data under the model. Since the sigmoid and logarithm are both differentiable, you can compute gradients of the cross-entropy loss with respect to each weight using the chain rule, and then apply gradient descent to update the weights iteratively.

Despite its simplicity, logistic regression is a powerful and interpretable baseline. Each weight tells you how much a one-unit increase in that feature shifts the log-odds of the positive class. It works well when the true decision boundary is approximately linear, scales efficiently to large datasets, and rarely overfits when properly regularized. Its limitations are equally instructive: because the decision boundary must be linear, logistic regression cannot capture XOR-like patterns or complex nonlinear boundaries without manual feature engineering. This limitation is precisely what motivates the move to neural networks — which you can think of as stacking many logistic-regression-like units together with nonlinearities between them.
