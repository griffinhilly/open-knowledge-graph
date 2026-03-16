---
id: lstm-gated-networks
title: LSTM and Gated Recurrent Units
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: recurrent-neural-networks
  type: hard
- id: partial-derivatives
  type: soft
- id: matrix-operations
  type: soft
tags:
- deep-learning
- sequence-models
- gated-networks
stage: advanced
status: draft
---

# LSTM and Gated Recurrent Units

## Core Idea
LSTMs address vanishing gradients via memory cells with input, forget, and output gates controlling information flow. GRUs simplify LSTMs with reset and update gates. Both maintain long-term dependencies better than vanilla RNNs.

## How It's Best Learned
Train an LSTM on language modeling, comparing convergence against vanilla RNN and visualizing gate activation patterns.

## Common Misconceptions
LSTMs do not guarantee prevention of gradient issues; initialization and learning rates matter. More gates do not always improve performance; GRUs often match LSTM results.

## Explainer

Recall from recurrent neural networks that a vanilla RNN processes sequences by passing a hidden state from one time step to the next, applying the same weight matrix at each step. The problem is that during backpropagation through time, gradients are multiplied by this same matrix repeatedly — and if its eigenvalues are less than one, the gradient shrinks exponentially toward zero. After just 10–20 time steps, the gradient signal from early inputs has effectively vanished, making it impossible for the network to learn long-range dependencies like the relationship between a subject at the start of a paragraph and a verb at the end.

The **Long Short-Term Memory (LSTM)** cell solves this by introducing a separate **cell state** — a highway that runs through the entire sequence with only linear interactions. Information on this highway can flow unchanged across many time steps because it is not repeatedly squashed through a nonlinear activation. Three **gates** control what enters and exits the cell state. The **forget gate** looks at the current input and previous hidden state, then outputs a value between 0 and 1 for each dimension of the cell state — 1 means "keep this entirely," 0 means "erase it." The **input gate** decides which new information to write into the cell state, and the **output gate** decides which parts of the cell state to expose as the hidden state for the current time step. Each gate is itself a small neural network (a sigmoid layer), so the LSTM learns when to remember and when to forget.

The **Gated Recurrent Unit (GRU)** simplifies this architecture by merging the cell state and hidden state into a single vector and using only two gates: a **reset gate** that controls how much of the previous hidden state to ignore when computing the candidate update, and an **update gate** that interpolates between the old hidden state and the candidate. The update gate plays the combined role of the LSTM's forget and input gates. Despite having fewer parameters, GRUs often perform comparably to LSTMs on many tasks, and they train faster because there is less computation per time step.

In practice, the choice between LSTM and GRU is empirical. LSTMs tend to have a slight edge on tasks requiring very precise memory control — such as copying sequences or counting nested brackets — because the separate cell state gives them more capacity to hold information without interference. GRUs work well on shorter sequences or when training speed matters. Both architectures share the core insight: instead of forcing all information through a single repeatedly-multiplied hidden state, use learned gates to create controlled pathways for information to persist across time steps. This gating mechanism is what makes sequence modeling on hundreds or thousands of time steps practical.
