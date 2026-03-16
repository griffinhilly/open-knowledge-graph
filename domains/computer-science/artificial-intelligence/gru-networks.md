---
id: gru-networks
title: Gated Recurrent Units (GRU)
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: recurrent-neural-networks
  type: hard
- id: lstm-gated-networks
  type: hard
builds-toward:
- sequence-modeling
- temporal-modeling
tags:
- gru
- gated-recurrent-unit
- rnn
stage: advanced
status: draft
---

# Gated Recurrent Units (GRU)

## Core Idea
Gated Recurrent Units (GRU) simplify LSTMs by combining forget and input gates into a single update gate, reducing parameters while maintaining gradient flow. GRUs have 3 gates vs. LSTMs' 4, making them faster to train with comparable performance. GRUs are preferred when computational efficiency matters.

## Explainer

From your study of recurrent neural networks and LSTMs, you know the fundamental problem: vanilla RNNs struggle to learn long-range dependencies because gradients either vanish or explode as they are backpropagated through many time steps. LSTMs solved this with a gating mechanism — separate gates control what information to forget, what new information to store, and what to output, all protecting a cell state that can carry information across long sequences without degradation. **Gated Recurrent Units (GRUs)** achieve the same goal with a simpler architecture, reducing the gate count from four operations to three by merging the forget and input gates into a single **update gate**.

The GRU has two gates: the **update gate** z and the **reset gate** r. The update gate decides how much of the previous hidden state to keep versus how much to replace with new candidate information — it simultaneously handles what the LSTM splits into separate forget and input gates. When z is close to 1, the unit preserves the old hidden state almost entirely (like an LSTM keeping its cell state unchanged). When z is close to 0, the unit mostly adopts the new candidate state. The **reset gate** controls how much of the previous hidden state flows into the computation of the candidate state. When r is close to 0, the unit acts as if it is reading the first element of a sequence — it ignores history and computes a candidate based primarily on the current input. When r is close to 1, the candidate state incorporates the full previous hidden state, behaving more like a standard RNN.

The mathematical formulation makes the simplification clear. At each time step, the GRU computes: z = σ(W_z·[h_{t-1}, x_t]), r = σ(W_r·[h_{t-1}, x_t]), h̃ = tanh(W·[r⊙h_{t-1}, x_t]), and finally h_t = (1−z)⊙h_{t-1} + z⊙h̃. That last equation is the key insight: the new hidden state is a linear interpolation between the old hidden state and the candidate, controlled by the update gate. This linear interpolation creates a direct pathway for gradients to flow backward through time (similar to the LSTM's cell state highway), which is what prevents the vanishing gradient problem. Notice there is no separate cell state — the GRU maintains only the hidden state h, whereas the LSTM maintains both a cell state c and a hidden state h.

In practice, GRUs and LSTMs perform comparably on most sequence tasks. The GRU's advantage is computational: with fewer parameters (roughly 75% of an LSTM's parameter count for the same hidden size), GRUs train faster and require less memory. This makes them attractive for applications with limited compute budgets, real-time requirements, or smaller datasets where the extra LSTM parameters might lead to overfitting. The LSTM's advantage tends to emerge on tasks requiring very precise, independent control over what to store versus what to output — the separate output gate gives LSTMs slightly more expressive control. Neither architecture dominates universally; the choice is often made empirically by trying both on the specific task at hand. Both have largely been supplanted by transformer-based attention mechanisms for many sequence tasks, though GRUs remain popular in settings where sequence lengths are moderate and computational efficiency is paramount.
