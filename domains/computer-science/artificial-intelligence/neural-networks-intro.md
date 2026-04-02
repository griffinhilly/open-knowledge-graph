---
id: neural-networks-intro
title: Neural Network Fundamentals
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: linear-regression-ml
  type: hard
- id: vectors-in-rn
  type: soft
- id: matrices-intro
  type: soft
- id: matrix-operations
  type: soft
- id: partial-derivatives
  type: soft
- id: derivatives-of-exponential-functions
  type: soft
- id: vectors-in-rn-operations
  type: soft
tags:
- neural-networks
- deep-learning
- function-approximation
stage: advanced
status: validated
---

# Neural Network Fundamentals

## Core Idea
Neural networks compose non-linear functions (neurons) across layers. Each neuron computes a weighted sum plus bias through an activation function. Universal approximation theorem states sufficiently wide networks approximate any continuous function.

## Questions

```yaml
- question: "What is the primary role of an activation function in a neural network neuron?"
  type: multiple-choice
  options: ["To normalize the weighted sum so it always falls between 0 and 1", "To introduce non-linearity, allowing the network to learn non-linear relationships", "To initialize the weights before training begins", "To compute the gradient during backpropagation"]
  answer: 1
  explanation: "Without a non-linear activation function, stacking multiple layers of neurons produces only a linear transformation — equivalent to a single linear layer regardless of depth. The activation function (e.g., ReLU, sigmoid, tanh) breaks this linearity, enabling the network to represent and learn complex, non-linear mappings from inputs to outputs."

- question: "A deep neural network with many layers but mainly linear activation functions can approximate any continuous function, given enough neurons."
  type: true-false
  answer: false
  explanation: "The composition of any number of linear functions is itself a linear function. No matter how many layers you stack, a purely linear network collapses to a single matrix multiplication (and bias addition). The universal approximation theorem requires non-linear activations. Depth without non-linearity adds no representational power."

- question: "In a single neuron, what computation is performed before the activation function is applied?"
  type: short-answer
  answer: "The neuron computes a weighted sum of all its inputs plus a bias term: z = w₁x₁ + w₂x₂ + ... + wₙxₙ + b. This is a linear combination of the input vector and the weight vector, shifted by b. The activation function f is then applied to z to produce the neuron's output."
  explanation: "This pre-activation value z is a dot product of the weight vector and the input vector plus bias. The weights determine how much each input contributes; the bias shifts the activation threshold. Understanding this as a linear regression followed by a non-linear squashing function helps connect neural networks to the linear models that are their prerequisites."
```

## Explainer

You have already worked with linear regression, which fits a single linear function — a weighted sum of inputs — to data. Neural networks extend this idea dramatically: instead of one linear transformation, they stack many layers of simple units (neurons), each with its own weights, and crucially, each followed by a non-linear transformation. This stacking of non-linearities is what makes neural networks capable of approximating extraordinarily complex functions.

A single neuron does something familiar: it computes a weighted sum of its inputs plus a bias, exactly like linear regression. For inputs x₁, x₂, ..., xₙ with weights w₁, w₂, ..., wₙ and bias b, the pre-activation value is z = w₁x₁ + ... + wₙxₙ + b. So far this is just linear regression. The key addition is the activation function f, applied to z: the neuron's output is f(z). Common choices are ReLU (f(z) = max(0, z)), sigmoid (f(z) = 1/(1 + e^{-z})), and tanh. These functions are non-linear, and that non-linearity is everything.

Why does non-linearity matter so much? Because the composition of linear functions is always linear. If you stacked ten layers with no activation functions, the whole network would be equivalent to a single matrix multiplication — as limited as linear regression. Once you introduce non-linear activations, the network can bend, curve, and fold the input space in ways a single linear function cannot. The universal approximation theorem makes this precise: a sufficiently wide single hidden layer can approximate any continuous function on a compact domain to arbitrary accuracy. Deeper networks with more layers can approximate the same functions with fewer neurons — this is why depth is valuable.

Networks are organized into layers: an input layer that receives the raw features, one or more hidden layers where the actual computation and representation learning happens, and an output layer that produces the prediction. Each layer transforms its inputs into a new representation, and as you go deeper, these representations become increasingly abstract. In a network trained on images, early layers might detect edges, later layers shapes, and the final layers might represent concepts like "cat" or "chair."

Training a neural network means finding the weight values that minimize prediction error on training data. This is done by computing the gradient of the loss with respect to every weight — which requires calculus, specifically the chain rule applied repeatedly through the layers (the backpropagation algorithm). This is why derivatives and partial derivatives are prerequisites: without the ability to compute how the loss changes with respect to each weight, you cannot update the weights in the right direction. The connection to linear regression is also direct: a neural network with no hidden layers and a linear activation is exactly linear regression.
