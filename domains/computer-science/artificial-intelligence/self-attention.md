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
- transformer-architecture
tags:
- self-attention
- multi-head
- transformer
stage: advanced
status: validated
---

# Self-Attention and Multi-Head Attention

## Core Idea
Self-attention computes a weighted sum of all positions in a sequence, allowing each position to attend to every other position. Multi-head attention runs multiple self-attention operations in parallel, learning different attention patterns. This mechanism is central to Transformers and enables modeling long-range dependencies more effectively than RNNs.

## Questions

```yaml
- question: "Suppose you remove the positional encodings from a Transformer model and train it on a sentence classification task. What is the most fundamental consequence?"
  type: multiple-choice
  options:
    - "The model can no longer compute attention scores because the Q, K, V projections depend on position"
    - "The model treats every permutation of the same words as identical, losing all sensitivity to word order"
    - "Multi-head attention stops working because heads require positional information to specialize"
    - "The model attends only to adjacent tokens, losing the ability to model long-range dependencies"
  answer: 1
  explanation: "Self-attention is permutation-invariant: the computation treats every position symmetrically, so shuffling the input tokens produces the same output (just rearranged). The sentences 'the cat chased the dog' and 'the dog chased the cat' would produce identical representations after self-attention without positional encodings. Positional encodings inject sequence-order information into the token embeddings *before* attention operates, giving the mechanism something to attend to that encodes position. This is why positional encoding is not optional in Transformers — it is a necessary fix for a fundamental property of the attention mechanism itself."

- question: "Why are the raw dot-product attention scores divided by √dₖ before applying the softmax in self-attention?"
  type: multiple-choice
  options:
    - "To normalize scores to the range [0, 1] before softmax can be applied"
    - "To prevent very large dot products from pushing the softmax into a near-zero-gradient region, which would slow training"
    - "To ensure that the output of each attention head has the same variance as the input"
    - "To make attention scores independent of the model dimension, allowing the same architecture to work at any scale"
  answer: 1
  explanation: "When dₖ (the key/query dimension) is large, random dot products have variance proportional to dₖ. Large-magnitude dot products push the softmax toward a near-one-hot distribution — one position gets almost all the weight and the rest get almost nothing. In this regime the softmax gradient is nearly zero, making learning very slow. Dividing by √dₖ keeps the dot products in a range where the softmax gradient remains healthy. This scaling is subtle but critical — without it, multi-head attention with high-dimensional projections trains poorly."

- question: "Self-attention inherently captures the order of tokens in a sequence, which is why Transformers can model word order without needing positional encodings."
  type: true-false
  answer: false
  explanation: "This is the central counterintuitive property of self-attention. The mechanism computes dot products between every pair of positions and takes weighted sums — operations that are completely symmetric with respect to position. If you feed in 'A B C' versus 'C B A,' the self-attention operation (without positional encodings) produces the same output values, just reindexed. Word order information must be injected externally via positional encodings added to the input embeddings. This is a fundamental architectural constraint, not an implementation detail."

- question: "In multi-head attention, different attention heads can specialize in capturing different types of relationships — such as syntactic dependencies and coreference — without any explicit supervision about which head should learn which pattern."
  type: true-false
  answer: true
  explanation: "This specialization emerges naturally from training. Because each head has its own learned Q, K, V projection matrices mapping into a lower-dimensional subspace, different heads learn to attend to different aspects of the input that are useful for the training objective. Empirical studies of trained Transformers have found heads that attend to adjacent words, heads that resolve coreference (e.g., 'it' → 'cat'), and heads that track syntactic roles — even though none of this was prescribed during architecture design. The parallel structure makes this division of labor both possible and computationally efficient."

- question: "Why is self-attention described as having O(n²) computational cost with respect to sequence length, and what does this imply for very long sequences?"
  type: short-answer
  answer: "Self-attention requires computing a score between every pair of positions: position 1 attends to positions 1 through n, position 2 attends to positions 1 through n, and so on. With n positions, this yields n × n = n² score computations. Both the memory required to store the attention matrix and the compute required to fill it scale quadratically with n. For short sequences (sentences of ~512 tokens), this is manageable. For very long sequences (documents, high-resolution images, genomic sequences), it becomes prohibitively expensive — motivating architectures like sparse attention, linear attention, and hierarchical approaches that reduce this cost at the expense of some modeling flexibility."
  explanation: "This quadratic cost is the main limitation of standard self-attention. Unlike RNNs, which process tokens sequentially with O(n) compute but struggle to propagate information across long distances, self-attention directly connects all pairs but pays a quadratic price. This is the fundamental trade-off that drives ongoing research into efficient attention variants."
```

## Explainer

You already understand attention as a mechanism that lets a model focus on relevant parts of an input when producing an output. **Self-attention** applies this idea within a single sequence — every position attends to every other position in the same sequence, computing how relevant each word (or token) is to every other word. In the sentence "The cat sat on the mat because it was tired," self-attention at the position of "it" can learn to attend strongly to "cat," resolving the pronoun reference. No recurrence or convolution is needed — every pair of positions interacts directly regardless of distance.

The mechanism works through three learned projections. Each input position is projected into a **query** vector (what am I looking for?), a **key** vector (what do I contain?), and a **value** vector (what information do I carry?). Attention scores are computed as the dot product of each query with every key, scaled by √dₖ to prevent the softmax from saturating into a one-hot distribution. After softmax, these scores become weights that determine how much each position's value vector contributes to the output at the query position. The entire operation can be written as Attention(Q, K, V) = softmax(QK^T / √dₖ)V, and because it is expressed as matrix multiplications, it is massively parallelizable on GPUs — a critical advantage over the sequential processing that RNNs require.

A single attention head learns one pattern of relevance — perhaps syntactic dependency, or coreference, or positional proximity. But language requires attending to multiple relationships simultaneously. **Multi-head attention** addresses this by running h separate attention operations in parallel, each with its own learned Q, K, V projections into a smaller subspace (dimension dₖ/h). The outputs of all heads are concatenated and linearly projected back to the model dimension. In practice, different heads specialize: one might track subject-verb agreement across long distances while another focuses on adjacent-word relationships. This division of labor emerges naturally from training, without explicit supervision.

Self-attention has a key limitation: it is **permutation-invariant** — the mechanism itself has no notion of word order, since every position interacts with every other position symmetrically. This is why Transformers add positional encodings to the input embeddings, injecting sequence-order information that the attention mechanism can then use. The computational cost is O(n²) in sequence length, since every position attends to every other, which becomes expensive for very long sequences. Despite this quadratic cost, self-attention's ability to directly model relationships between any two positions — without information having to propagate step-by-step through intermediate states — is what makes Transformers so effective at capturing the long-range dependencies that recurrent models struggle with.
