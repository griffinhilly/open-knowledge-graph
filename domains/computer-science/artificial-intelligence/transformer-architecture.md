---
id: transformer-architecture
title: Transformer Architecture
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: attention-mechanisms
  type: hard
- id: linear-transformations
  type: soft
- id: matrix-operations
  type: soft
- id: dot-product
  type: soft
- id: matrix-multiplication
  type: soft
tags:
- deep-learning
- attention
- neural-architecture
stage: advanced
status: draft
---

# Transformer Architecture

## Core Idea
Transformers replace RNNs with self-attention and feedforward layers, enabling parallel sequence processing. Positional encodings inject order information. Encoder-decoder structure processes inputs and generates outputs autoregressively without recurrence.

## Explainer

Recurrent networks process sequences one token at a time, maintaining a hidden state that carries information forward. This sequential nature creates two problems: it prevents parallelization (each step waits for the previous one), and information from early tokens must survive through many compression steps to reach the end — a bottleneck that attention mechanisms only partially fix. The **transformer** architecture eliminates recurrence entirely. Every token attends to every other token directly through **self-attention**, meaning that relationships between distant tokens are captured in a single operation rather than being passed through a chain of hidden states.

The core mechanism is **scaled dot-product attention**, which you know from your study of attention mechanisms. Each token is projected into three vectors — a **query** (Q), a **key** (K), and a **value** (V) — using learned linear transformations (the matrix operations from your prerequisites). Attention scores are computed as the dot product of each query with all keys, scaled by √dₖ to prevent the softmax from saturating, then used to weight the values. In **self-attention**, the queries, keys, and values all come from the same sequence, so every token computes a weighted combination of all other tokens in the sequence. This is done in parallel across all positions — no sequential bottleneck. **Multi-head attention** runs several independent attention operations in parallel, each with its own Q/K/V projections, allowing the model to attend to different types of relationships simultaneously (one head might capture syntactic structure while another captures semantic similarity).

Since self-attention treats the input as an unordered set, the model needs explicit information about token order. **Positional encodings** — fixed sinusoidal functions or learned vectors — are added to the input embeddings to provide this. Each transformer layer then applies self-attention followed by a position-wise **feedforward network** (two linear transformations with a nonlinearity between them), with **residual connections** and **layer normalization** around each sub-layer. Stacking multiple such layers creates a deep network where each layer refines the representations produced by the layer below.

The full transformer follows an **encoder-decoder** structure. The encoder processes the input through self-attention layers, producing contextualized representations. The decoder generates output tokens autoregressively: it uses **masked self-attention** (preventing positions from attending to future tokens, since those have not been generated yet) and **cross-attention** (attending to the encoder's output, exactly like the attention in seq2seq models). At inference time, the decoder generates one token at a time, appending each prediction to the input for the next step. Because all attention operations are matrix multiplications over the full sequence, training is massively parallelizable on GPUs — the key practical advantage that enabled scaling to billions of parameters. Transformers now underpin virtually all state-of-the-art language models, from BERT (encoder-only) to GPT (decoder-only) to T5 (encoder-decoder).
