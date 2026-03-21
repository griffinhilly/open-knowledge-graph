---
id: fine-tuning-pretrained-models
title: Fine-Tuning Pretrained Models
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: transfer-learning-neural
  type: hard
- id: backpropagation
  type: hard
- id: hyperparameter-optimization
  type: soft
- id: gradient-descent-optimization
  type: soft
tags:
- transfer-learning
- optimization
- adaptation
- feature-learning
stage: advanced
status: draft
---

# Fine-Tuning Pretrained Models

## Core Idea
Fine-tuning adapts a pretrained model to a new task by continuing training on task-specific data, often with a lower learning rate to avoid catastrophically forgetting learned features. The number of layers to fine-tune balances adaptation (more layers) with regularization (fewer layers); layer-wise learning rates (lower for early layers) are effective for training stability.

## How It's Best Learned
Compare different fine-tuning strategies: frozen base layers only, unfrozen with low learning rate, and layer-wise varying learning rates, measuring final accuracy and computational cost.

## Questions

```yaml
- question: "You have a small dataset of 500 medical X-ray images and want to fine-tune an ImageNet-pretrained ResNet. Which strategy is most appropriate?"
  type: multiple-choice
  options:
    - "Full fine-tuning with a standard learning rate, since the large model capacity is needed for medical images"
    - "Feature extraction (freeze all pretrained layers, train only the new head) to avoid overfitting with limited data"
    - "Train from scratch with random initialization to ensure the model learns medical-specific features"
    - "Use discriminative learning rates with the highest rate on early layers since medical features differ most there"
  answer: 1
  explanation: "With a small dataset, the main risk is overfitting. Feature extraction freezes the pretrained weights (which already encode powerful general features like edges and shapes) and trains only the small classification head — minimizing the number of parameters to optimize and preventing overfitting. Full fine-tuning with a standard learning rate risks catastrophic forgetting and overfitting on 500 examples. Training from scratch would require far more data. Discriminative learning rates have it backwards — early layers are most universal and need the smallest rates."

- question: "In discriminative (layer-wise) fine-tuning, early layers receive smaller learning rates than later layers. Why?"
  type: multiple-choice
  options:
    - "Early layers have more parameters and need smaller updates for numerical stability"
    - "Early layers learn universal features (edges, textures) that transfer well and need minimal adjustment"
    - "Early layers are closer to the output and thus more sensitive to gradient updates"
    - "Earlier layers converge faster, so they need smaller learning rates to prevent overshooting"
  answer: 1
  explanation: "Early layers in deep networks learn low-level features (edge detectors, color patterns, textures) that are nearly universal across image tasks. These features are already well-adapted and should change minimally. Later layers encode more task-specific representations that genuinely need to adapt to the new domain. Using small learning rates for early layers preserves the valuable pretrained representations while allowing later layers to adjust. The early layers are also furthest from the loss and receive the smallest gradients naturally — the small learning rate reinforces this stability."

- question: "Fine-tuning a pretrained model with a learning rate close to the original pretraining rate is a safe starting point because the pretrained weights provide a good initialization."
  type: true-false
  answer: false
  explanation: "This is a dangerous misconception. Using a normal (pretraining-scale) learning rate during fine-tuning causes catastrophic forgetting — the useful features encoded in the early layers get overwritten rapidly before the network adapts them coherently to the new task. The correct approach is a learning rate 10× to 100× smaller than pretraining. The pretrained initialization is valuable precisely because it represents well-learned features; a high learning rate destroys that value by making large, uncoordinated updates to all weights simultaneously."

- question: "Feature extraction (freezing all pretrained layers and training only the new head) performs worse than full fine-tuning when the target task is very different from the pretraining domain."
  type: true-false
  answer: true
  explanation: "When the source and target domains differ significantly (e.g., natural photos vs. satellite imagery vs. medical scans), the features in early and mid-level layers may not transfer well. Feature extraction assumes these frozen representations are useful for the new task. If they are not, no amount of training on the new head can compensate — the inputs to the head remain poorly suited. Full fine-tuning (with a low learning rate) allows the network to adapt its representations to the new domain, often substantially improving performance despite the risk of overfitting."

- question: "Why is a much lower learning rate used when fine-tuning a pretrained model compared to training from scratch, and what specific failure mode does it prevent?"
  type: short-answer
  answer: "A low learning rate prevents catastrophic forgetting — the phenomenon where fine-tuning with large weight updates destroys the useful feature representations learned during pretraining. With a standard learning rate, the pretrained weights are overwritten rapidly, effectively erasing the benefit of pretraining. A smaller learning rate (typically 10–100× lower) allows weights to drift gently toward task-specific solutions while preserving the pretrained structure. Training from scratch uses a higher rate because there are no useful weights to preserve."
  explanation: "The key insight is that the pretrained weights encode a rich representation built from vast data. Fine-tuning should refine, not replace, these representations. Catastrophic forgetting is well-documented: if you train a language model on task A, then fine-tune on task B with a large learning rate, performance on task A collapses. The same mechanism applies to vision models. The low learning rate is not primarily about convergence speed — it is about preserving the signal already embedded in the weights."
```

## Explainer

From transfer learning, you know that a neural network trained on a large dataset learns features that are useful far beyond its original task. The early layers of an image classifier trained on ImageNet learn edge detectors, texture recognizers, and color patterns; the middle layers learn parts and shapes; the later layers learn task-specific compositions. **Fine-tuning** is the process of taking such a pretrained model and adapting it to your specific task — say, classifying medical images or identifying bird species — by continuing training on your (typically smaller) dataset.

The simplest approach is **feature extraction**: freeze all the pretrained layers, replace the final classification head with a new one matching your number of classes, and train only that new head. This treats the pretrained network as a fixed feature extractor. It works well when your task is similar to the original and your dataset is small, because you are only optimizing a few parameters and cannot overfit easily. But if your task differs significantly from the pretraining domain (e.g., medical X-rays versus natural photos), the frozen features may not transfer perfectly, and you need to let deeper layers adapt.

Full fine-tuning unfreezes all layers and trains the entire network on your data, but this requires care. The key risk is **catastrophic forgetting**: if you train with a normal learning rate, the useful features in the early layers get overwritten before the network can adapt them to the new task. The solution is to use a **much lower learning rate** than you would for training from scratch — typically 10× to 100× smaller. This lets the weights drift gently toward task-specific solutions without destroying the pretrained representations. Think of it as nudging the network rather than retraining it.

The most sophisticated strategy uses **discriminative (layer-wise) learning rates**, where early layers get the smallest learning rate and later layers get progressively larger ones. The rationale is that early features (edges, textures) are nearly universal and need minimal adjustment, while later features are more task-specific and need more adaptation. A common recipe is to set the last layer's learning rate to some base value and reduce it by a factor of 2-3 for each preceding layer group. Combined with techniques like gradual unfreezing — starting by training only the head, then unfreezing one layer group at a time — this approach consistently achieves strong performance even with very small datasets. The number of layers to fine-tune becomes a regularization knob: fewer unfrozen layers means less capacity to adapt but also less risk of overfitting, making this a balance you tune based on dataset size and domain similarity.
