---
id: adversarial-examples-robustness
title: Adversarial Examples and Robustness
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: neural-networks-intro
  type: hard
- id: supervised-learning-intro
  type: hard
- id: ai-ethics-fairness-bias
  type: soft
- id: partial-derivatives
  type: soft
- id: optimization-problems
  type: soft
tags:
- adversarial-ml
- robustness
- security
- perturbations
stage: advanced
status: draft
---

# Adversarial Examples and Robustness

## Core Idea
Adversarial examples are inputs crafted to fool neural networks, sometimes by adding imperceptible perturbations; they reveal model brittleness and exist in high-dimensional spaces due to model linearities and feature overfitting. Defenses include adversarial training (training on adversarial examples), certified defenses (provable robustness), and regularization, though robust models often sacrifice clean accuracy.

## How It's Best Learned
Generate adversarial examples using FGSM and PGD attacks on an image classifier, then implement adversarial training and observe robustness improvements and accuracy tradeoffs.

## Questions

```yaml
- question: "A neural network achieves 98% accuracy on a held-out test set. A researcher then applies FGSM to 100 of those correctly classified images and finds the network misclassifies 85 of them. What does this demonstrate?"
  type: multiple-choice
  options:
    - "The test set was too small to give a reliable accuracy estimate"
    - "High test accuracy does not guarantee robustness — the model is brittle against adversarial perturbations"
    - "FGSM produces unrealistic inputs that no real attacker would generate"
    - "The network needs more training epochs to generalize properly"
  answer: 1
  explanation: "This is the core lesson: test accuracy and adversarial robustness measure different properties. The 98% test accuracy reflects how the model performs on natural inputs drawn from the data distribution. Adversarial inputs are specifically crafted to exploit the model's decision boundaries, revealing that high accuracy can coexist with extreme brittleness. A model can be both state-of-the-art on benchmarks and trivially fooled by imperceptible perturbations."

- question: "Why can adding a tiny perturbation of magnitude ε to each dimension of a high-dimensional input reliably fool a neural network, even when no single perturbed pixel is noticeable?"
  type: multiple-choice
  options:
    - "Because the perturbation shifts the input into a different data distribution that the model has never seen"
    - "Because the perturbations accumulate: the total effect on the output can be as large as ε × d, where d is the input dimensionality"
    - "Because neural networks only process a small subset of input dimensions at a time"
    - "Because ε-perturbations happen to target the most important pixels as identified by the gradient"
  answer: 1
  explanation: "The insight behind FGSM is that neural networks behave approximately linearly in high-dimensional spaces. A perturbation of ε per dimension looks tiny locally, but across d ≈ 150,000 dimensions (a typical image), the cumulative dot product with the model's gradient can reach ε × d — a potentially large effect on the output logits. This is why the attack works even when no individual perturbation is perceptible: the damage accumulates across the whole input vector."

- question: "Adversarially trained models typically achieve lower accuracy on clean, unperturbed test images than models trained without adversarial examples."
  type: true-false
  answer: true
  explanation: "This is the robustness-accuracy tradeoff, and it appears to be fundamental rather than a solvable engineering challenge. Adversarial training forces the model to rely on more robust, semantically meaningful features — but those features may not be as predictive as the brittle statistical patterns in pixel values that a standard model learns. The result is a consistent drop of several percentage points on clean accuracy, reflecting a genuine tension between performance on natural inputs and resistance to adversarial perturbations."

- question: "An adversarial perturbation must be visible to the human eye in order to reliably fool a state-of-the-art neural network classifier."
  type: true-false
  answer: false
  explanation: "The alarming finding is that highly effective adversarial perturbations can be imperceptible — invisible to human observers yet reliably causing misclassification. FGSM and PGD construct perturbations bounded in the L∞ or L2 norm to keep changes small per pixel while maximizing the effect on model outputs. The gap between human perception and model perception is precisely what makes adversarial examples so consequential for safety-critical applications."

- question: "Explain why high-dimensional input spaces make neural networks particularly vulnerable to adversarial perturbations, even when those perturbations are small in any single dimension."
  type: short-answer
  answer: "Neural networks behave approximately linearly in high-dimensional spaces. A perturbation of ε per input dimension may be imperceptible, but when the network computes the dot product of this perturbation with its weight vectors across all d dimensions, the total contribution can be as large as ε × d. For images with ~150,000 dimensions, this is enormous. FGSM exploits this by choosing the perturbation direction that maximizes this dot product — adding ε in the direction of the sign of the gradient of the loss with respect to each input pixel. The problem is not a bug that better training can fully fix; it reflects a structural property of high-dimensional geometry."
  explanation: "The key is the distinction between local and global effects. Each perturbation is tiny locally (below human perceptual threshold), but the model's output is a function of all dimensions simultaneously. Accumulation across many dimensions converts a small perturbation into a large change in the output. This is also why robustness doesn't come for free: making a model robust requires it to learn features that are genuinely invariant to these perturbations, which conflicts with maximizing accuracy on clean data."
```

## Explainer

From supervised learning, you know that neural networks learn to map inputs to outputs by finding patterns in training data. A well-trained image classifier might achieve 95% accuracy on test images — but what happens if you take a correctly classified image of a panda and add a tiny, carefully computed perturbation that is invisible to the human eye? The network confidently classifies it as a gibbon. This perturbed input is an **adversarial example**, and its existence reveals something fundamental about how neural networks represent the world.

The key insight is that neural networks, despite their complexity, behave approximately linearly in high-dimensional spaces. Consider a network with input dimension d. Even a tiny perturbation ε applied to each input dimension can accumulate a total effect of ε × d on the output, which can be enormous when d is large (a 224×224 RGB image has d ≈ 150,000 dimensions). The **Fast Gradient Sign Method (FGSM)** exploits this directly: it computes the gradient of the loss with respect to each input pixel, then adds a small perturbation in the direction that maximizes the loss. Because you already understand partial derivatives and optimization, you can see that FGSM is simply one step of gradient ascent on the input space instead of gradient descent on the weight space. Stronger attacks like **Projected Gradient Descent (PGD)** iterate this process multiple times, staying within a small ε-ball around the original input.

Why do adversarial examples matter beyond academic curiosity? They expose a gap between human perception and machine perception. Humans classify images based on semantic features — shapes, textures, objects. Neural networks often rely on subtle statistical patterns in pixel values that happen to correlate with labels in the training data but have no semantic meaning. Adversarial perturbations exploit these brittle features. In safety-critical applications — self-driving cars, medical imaging, security systems — adversarial vulnerability is not just an inconvenience but a potential attack vector.

The primary defense is **adversarial training**: augmenting the training set with adversarial examples generated during training, so the model learns to classify them correctly. This forces the network to rely on more robust features, but it comes at a cost — adversarially trained models typically sacrifice a few percentage points of accuracy on clean (unperturbed) inputs. This robustness-accuracy tradeoff appears to be fundamental, not just a limitation of current methods. Other approaches include **certified defenses** that mathematically prove no perturbation within a given ε-ball can change the prediction, and input preprocessing techniques that attempt to remove perturbations before classification. The field remains an arms race: stronger attacks break existing defenses, motivating new defenses, which in turn face new attacks. The broader lesson is that high test accuracy does not imply genuine understanding, and robustness must be evaluated and engineered as a separate property.
