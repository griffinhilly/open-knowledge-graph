---
id: recurrent-neural-networks
title: Recurrent Neural Networks
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: backpropagation
  type: hard
- id: markov-chains
  type: soft
- id: partial-derivatives
  type: soft
- id: matrix-operations
  type: soft
- id: sequences-and-series-review
  type: soft
tags:
- deep-learning
- sequence-models
- neural-networks
stage: advanced
status: draft
---

# Recurrent Neural Networks

## Core Idea
RNNs process sequences maintaining hidden states updated at each time step. Information propagates temporally enabling sequence modeling. Backpropagation through time (BPTT) unfolds the network across time but suffers from vanishing/exploding gradients.

## Explainer

Standard feedforward neural networks process fixed-size inputs — give them a vector, get an output. But many real-world problems involve **sequences**: words in a sentence, stock prices over time, notes in a melody. The length varies, and the order matters. **Recurrent neural networks** solve this by introducing a loop: the network maintains a **hidden state** that gets updated at each time step, carrying information forward through the sequence. Think of it as the network having a form of memory — at each step, it sees the current input *and* a summary of everything it has seen so far.

At each time step *t*, the RNN computes a new hidden state h(t) = f(W_h · h(t-1) + W_x · x(t) + b), where x(t) is the current input, h(t-1) is the previous hidden state, and W_h and W_x are weight matrices shared across all time steps. This **weight sharing** is crucial — the same parameters process every position in the sequence, which means the network can generalize across positions and handle sequences of any length. If you are comfortable with matrix operations and how backpropagation computes gradients, you already have the tools to understand this computation: it is just a sequence of matrix multiplies and nonlinear activations, chained together through time.

Training an RNN requires **backpropagation through time (BPTT)**: you "unroll" the recurrent loop into a deep feedforward network with one layer per time step, then apply standard backpropagation. The catch is that for a sequence of length T, the gradient must flow backward through T matrix multiplications. This is where the **vanishing gradient problem** strikes — if the weight matrix W_h has eigenvalues less than 1, the gradient shrinks exponentially, making it nearly impossible to learn long-range dependencies. Conversely, eigenvalues greater than 1 cause **exploding gradients**, which can be managed with gradient clipping but still make training unstable. From your study of partial derivatives, you can see why: the chain rule applied across many time steps multiplies many Jacobian terms together, and repeated multiplication drives values toward zero or infinity.

These gradient problems motivated the development of gated architectures like **Long Short-Term Memory (LSTM)** and **Gated Recurrent Units (GRU)**, which use learned gates to control information flow and maintain gradients over longer sequences. While transformers have largely superseded RNNs for many tasks, understanding the recurrent paradigm — how hidden states carry temporal information, why gradient flow through time is challenging, and how gating mechanisms address it — provides essential context for understanding why modern sequence architectures are designed the way they are.
