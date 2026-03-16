---
id: attention-mechanisms
title: Attention Mechanisms
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: neural-networks-intro
  type: hard
- id: matrix-multiplication
  type: soft
- id: dot-product
  type: soft
- id: linear-transformations
  type: soft
- id: dot-product-definition
  type: soft
- id: matrix-operations
  type: soft
tags:
- deep-learning
- attention
- sequence-models
stage: advanced
status: draft
---

# Attention Mechanisms

## Core Idea
Attention computes weighted combinations of values based on query-key similarity, focusing on relevant input parts. Scaled dot-product attention computes Q·K^T/√d_k before softmax weighting. Multi-head attention applies attention in parallel with different representations.

## Explainer

From your study of neural networks, you know that a standard feedforward layer applies the same learned transformation to every input position independently. This works well for fixed-size inputs, but it creates a fundamental problem for sequences: how does the network at position 5 know what happened at position 1? Recurrent networks addressed this by passing hidden states forward step by step, but this sequential processing is slow and information from distant positions gets diluted through many steps. **Attention mechanisms** solve this by allowing every position to directly look at every other position and decide what is relevant — no sequential bottleneck required.

The core idea is a soft lookup table. Imagine you have a database of key-value pairs and a query. In a traditional lookup, you find the exact matching key and return its value. Attention does a *soft* version: it compares the query to every key, computes a similarity score for each, converts those scores into weights (using softmax so they sum to 1), and returns a weighted combination of all values. The output is dominated by values whose keys best match the query but still incorporates information from all positions. In **scaled dot-product attention**, the similarity between a query q and key k is computed as their dot product (from your linear algebra prerequisites), divided by √d_k to prevent the dot products from growing too large in high dimensions. Large dot products would push softmax into regions where its gradients are extremely small, stalling learning — the scaling factor keeps the gradients healthy.

In matrix form, attention over an entire sequence is computed as Attention(Q, K, V) = softmax(QK^T/√d_k)V. Here Q, K, and V are matrices where each row corresponds to a position in the sequence. The matrix QK^T computes all pairwise similarities at once — entry (i,j) measures how much position i should attend to position j. After softmax normalizes each row into a probability distribution, multiplying by V produces the output: each position's output is a weighted average of all value vectors, with weights determined by query-key compatibility. This entire operation is a matrix multiplication pipeline, making it highly parallelizable on GPUs — a crucial advantage over sequential recurrent processing.

**Multi-head attention** extends this by running several attention operations in parallel, each with its own learned projection matrices for Q, K, and V. Think of each head as asking a different question about the input: one head might attend based on syntactic relationships, another based on semantic similarity, another based on positional proximity. Each head operates on a lower-dimensional projection (d_k/h dimensions per head for h heads), so the total computation is comparable to single-head attention at full dimensionality. The outputs of all heads are concatenated and linearly projected back to the model dimension. This allows the model to simultaneously capture different types of relationships between positions — a capability that proved essential for the transformer architecture's success across language, vision, and beyond.
