---
id: self-attention
title: Self-Attention and Multi-Head Attention
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: attention-mechanisms
  type: hard
- id: transformer-architecture
  type: hard
builds-toward:
- transformer-variants
- vision-transformers
tags:
- self-attention
- multi-head
- transformer
stage: advanced
status: draft
---

# Self-Attention and Multi-Head Attention

## Core Idea
Self-attention computes a weighted sum of all positions in a sequence, allowing each position to attend to every other position. Multi-head attention runs multiple self-attention operations in parallel, learning different attention patterns. This mechanism is central to Transformers and enables modeling long-range dependencies more effectively than RNNs.

## Explainer

You already understand attention as a mechanism that lets a model focus on relevant parts of an input when producing an output. **Self-attention** applies this idea within a single sequence — every position attends to every other position in the same sequence, computing how relevant each word (or token) is to every other word. In the sentence "The cat sat on the mat because it was tired," self-attention at the position of "it" can learn to attend strongly to "cat," resolving the pronoun reference. No recurrence or convolution is needed — every pair of positions interacts directly regardless of distance.

The mechanism works through three learned projections. Each input position is projected into a **query** vector (what am I looking for?), a **key** vector (what do I contain?), and a **value** vector (what information do I carry?). Attention scores are computed as the dot product of each query with every key, scaled by √dₖ to prevent the softmax from saturating into a one-hot distribution. After softmax, these scores become weights that determine how much each position's value vector contributes to the output at the query position. The entire operation can be written as Attention(Q, K, V) = softmax(QK^T / √dₖ)V, and because it is expressed as matrix multiplications, it is massively parallelizable on GPUs — a critical advantage over the sequential processing that RNNs require.

A single attention head learns one pattern of relevance — perhaps syntactic dependency, or coreference, or positional proximity. But language requires attending to multiple relationships simultaneously. **Multi-head attention** addresses this by running h separate attention operations in parallel, each with its own learned Q, K, V projections into a smaller subspace (dimension dₖ/h). The outputs of all heads are concatenated and linearly projected back to the model dimension. In practice, different heads specialize: one might track subject-verb agreement across long distances while another focuses on adjacent-word relationships. This division of labor emerges naturally from training, without explicit supervision.

Self-attention has a key limitation: it is **permutation-invariant** — the mechanism itself has no notion of word order, since every position interacts with every other position symmetrically. This is why Transformers add positional encodings to the input embeddings, injecting sequence-order information that the attention mechanism can then use. The computational cost is O(n²) in sequence length, since every position attends to every other, which becomes expensive for very long sequences. Despite this quadratic cost, self-attention's ability to directly model relationships between any two positions — without information having to propagate step-by-step through intermediate states — is what makes Transformers so effective at capturing the long-range dependencies that recurrent models struggle with.
