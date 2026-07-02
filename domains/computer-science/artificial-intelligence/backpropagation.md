---
id: backpropagation
title: Backpropagation Algorithm
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: neural-networks-intro
  type: hard
- id: chain-rule-multivariable
  type: hard
- id: chain-rule
  type: hard
- id: partial-derivatives
  type: soft
- id: linear-transformations
  type: soft
- id: matrix-operations
  type: soft
tags:
- neural-networks
- training-algorithms
- gradient-computation
stage: advanced
status: validated
---

# Backpropagation Algorithm

## Core Idea
Backpropagation computes gradients efficiently via the chain rule in two phases: forward pass computes activations, backward pass propagates error signals layer-by-layer. Complexity is O(n) for n parameters, enabling large-scale neural network training.

## How It's Best Learned
Implement backpropagation from scratch, deriving gradients by hand and verifying with numerical gradients.

## Common Misconceptions
Backpropagation applies to any differentiable computation, not just neural networks. Vanishing/exploding gradients require normalization techniques.

## Questions

```yaml
- question: "In a neural network with L layers, backpropagation computes the gradient of the loss with respect to the weights in layer l. What does it propagate backward through the network to accomplish this?"
  type: multiple-choice
  options: ["The raw activation values from the forward pass", "The predicted output values for each training example", "Error signals (partial derivatives of the loss) from later layers", "The learning rate scaled by the layer index"]
  answer: 2
  explanation: "Backpropagation applies the chain rule: to get ∂L/∂W_l, you need ∂L/∂a_l (the error signal at layer l's output), which depends on error signals from all layers after l. These error signals — not raw activations — are what get propagated backward. The forward pass already computed and stored the activations; the backward pass uses them together with the propagated error signals."

- question: "Backpropagation can primarily be applied to neural networks that use sigmoid activation functions."
  type: true-false
  answer: false
  explanation: "Backpropagation requires only that each operation in the computation graph be differentiable (or sub-differentiable). It applies equally to ReLU, tanh, softmax, and any other differentiable activation. More broadly, backpropagation is just reverse-mode automatic differentiation and works on any differentiable computational graph — not just neural networks."

- question: "What is the vanishing gradient problem, and in what part of the network does it cause the most harm?"
  type: short-answer
  answer: "During backpropagation, gradients are multiplied together as they travel through layers. If each layer's gradient is less than 1 (as commonly happens with saturating activations like sigmoid), the product shrinks exponentially with depth. Early layers receive near-zero gradients and barely learn."
  explanation: "The chain rule means the gradient at layer l is a product of all the local gradients in layers l+1 through L. Sigmoid outputs are bounded in (0,1), and its derivative peaks at 0.25 — repeated multiplication quickly drives signals toward zero. This is why deep networks with sigmoid/tanh struggled before ReLU activations and batch normalization became standard."
```

## Explainer

You already know from neural networks that a model makes predictions by passing inputs through layers of weighted connections and activation functions. Training the model means adjusting those weights so the predictions improve — but with potentially millions of weights across dozens of layers, how do you know which direction to adjust each one? That is the problem backpropagation solves.

The algorithm runs in two phases. In the **forward pass**, inputs flow through the network layer by layer, and you store the intermediate activations at each layer. At the end, you compute the loss — a scalar measuring how wrong the prediction was. In the **backward pass**, you work in reverse: starting from the loss, you use the chain rule to compute the gradient of the loss with respect to each weight. The chain rule says that ∂L/∂w = (∂L/∂a) · (∂a/∂w), where a is the activation that w influences. Because each layer feeds into the next, the error signals propagate back through the network by repeated application of the chain rule. Crucially, the stored activations from the forward pass are needed here — they are part of the local gradient at each layer.

The efficiency of backpropagation comes from the order of computation. A naïve approach to computing ∂L/∂w for every weight would recompute many of the same partial derivatives repeatedly. Backpropagation avoids this by computing error signals once per layer in a single backward sweep, reusing results as they propagate. This gives O(n) time for n parameters — the same cost as a single forward pass — which is why training large networks is computationally feasible.

A common misconception is that backpropagation is specific to neural networks. It is not — it is **reverse-mode automatic differentiation** applied to a particular kind of computation graph. Any software that computes a differentiable function (not just neural nets) can use the same technique. Modern deep learning frameworks like PyTorch build a dynamic computation graph during the forward pass and then traverse it in reverse to compute all gradients automatically.

The main practical hazard is the **vanishing gradient problem**: when gradients pass through many layers, they are repeatedly multiplied by local derivatives. If those derivatives are consistently small (as with saturating activations like sigmoid, whose derivative peaks at 0.25), the product shrinks exponentially. Early layers receive nearly zero gradient and fail to learn. The opposite — **exploding gradients** from derivatives greater than 1 — causes numerical instability. Remedies include ReLU activations (gradient is 1 for positive inputs), batch normalization (keeps activations in healthy ranges), and gradient clipping for recurrent networks.
