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
status: validated
---

# Transformer Architecture

## Core Idea
Transformers replace RNNs with self-attention and feedforward layers, enabling parallel sequence processing. Positional encodings inject order information. Encoder-decoder structure processes inputs and generates outputs autoregressively without recurrence.

## Questions

```yaml
- question: "Why did the transformer architecture enable scaling language models to hundreds of billions of parameters when LSTM-based architectures could not practically reach that scale?"
  type: multiple-choice
  options:
    - "Transformers have fewer parameters per layer than LSTMs, allowing deeper networks at equivalent computational cost"
    - "All token relationships in a transformer are computed as matrix multiplications that execute in parallel on GPUs, eliminating the sequential bottleneck that forced RNNs to process one token at a time during training"
    - "Transformers use residual connections which prevent vanishing gradients, while LSTMs lack this mechanism entirely"
    - "Transformers can handle variable-length inputs natively, while RNNs require fixed-length padding that wastes computation"
  answer: 1
  explanation: "The parallelization advantage is the core reason transformers enabled modern large-scale training. In an RNN/LSTM, computing the hidden state at position t requires the hidden state at t-1, which requires t-2, and so on — the entire forward pass is a sequential chain. On a GPU with thousands of cores, most cores sit idle during this sequential computation. In a transformer, the attention scores for all position pairs are computed simultaneously as a single large matrix multiplication, and all positions can be processed at once. This makes training 10–100× faster on modern hardware, which is what made scaling to billions of parameters practical."

- question: "If positional encodings were completely removed from a transformer — with all other components unchanged — what would happen to the model's behavior?"
  type: multiple-choice
  options:
    - "The model would fail entirely, since attention requires positional offsets to compute similarity scores"
    - "The model would treat any permutation of the same tokens as an identical input, losing all sensitivity to word order"
    - "Only the cross-attention layers would be affected; self-attention layers would still capture order through learned weights"
    - "The model would effectively become a bag-of-words model with no sequential structure at all"
  answer: 1
  explanation: "Self-attention computes scores as dot products between query and key vectors — a permutation-invariant operation. If you feed the tokens 'dog bites man' and 'man bites dog' without positional encodings, the same set of Q/K/V vectors is produced (just in different order), and the attention output at each position is the same weighted combination of value vectors regardless of order. Option D is tempting but slightly wrong — the model can still represent relationships between tokens, it just cannot tell which came first. Positional encodings break this symmetry by giving each position a unique vector that is added to the token embedding before any computation."

- question: "In a well-trained transformer, different attention heads within the same multi-head attention layer can specialize to capture different types of relationships simultaneously."
  type: true-false
  answer: true
  explanation: "This is one of the key motivations for multi-head attention. Each head has its own learned Q, K, and V projection matrices, so each head can learn to attend to different relationship types. Empirical analysis of trained transformers has found that certain heads reliably track syntactic dependencies (subject-verb agreement), others track coreference (which pronoun refers to which entity), others capture positional patterns (attending to the previous token), and others capture semantic similarity. Running multiple heads in parallel and concatenating their outputs allows the model to build richer representations than any single attention pattern could provide."

- question: "During transformer training, all sequence positions can be processed simultaneously because self-attention does not maintain or read from any sequential hidden state."
  type: true-false
  answer: true
  explanation: "This is the fundamental architectural insight. Unlike RNNs where position t depends on position t-1 through the hidden state, self-attention at position t computes a weighted combination of all other positions' value vectors in a single operation. No position's computation depends on any other position's completion — the entire self-attention and feedforward computation for all positions can proceed in parallel. The decoder introduces a constraint (masked self-attention prevents attending to future positions during training, to simulate left-to-right generation), but even this masking is implemented as a matrix operation that runs in parallel over all positions."

- question: "Explain why self-attention in a transformer requires positional encodings to be explicitly added, whereas an LSTM processes order implicitly without any such mechanism."
  type: short-answer
  answer: "An LSTM processes tokens one at a time in sequence, so the position of each token is encoded implicitly in the order of computation — token 1's hidden state is computed first, token 2's hidden state is computed from token 1's, and so on. Order is built into the recurrence itself. Self-attention, by contrast, treats the input as an unordered set: it computes attention scores as dot products between vectors without any reference to their positions, making the operation completely permutation-invariant. Without positional encodings, the transformer has no way to distinguish 'the cat sat on the mat' from 'the mat sat on the cat.' Positional encodings inject position information by adding a unique vector to each token's embedding, giving the attention mechanism something to distinguish tokens by position when needed."
  explanation: "This tradeoff is fundamental to the transformer design: by making the core operation permutation-invariant (enabling full parallelism), the architecture must separately inject order information. The choice of how to encode positions (sinusoidal, learned, relative, rotary) has been an active research area precisely because the right positional representation significantly affects how well models generalize to sequence lengths not seen during training."
```

## Explainer

Recurrent networks process sequences one token at a time, maintaining a hidden state that carries information forward. This sequential nature creates two problems: it prevents parallelization (each step waits for the previous one), and information from early tokens must survive through many compression steps to reach the end — a bottleneck that attention mechanisms only partially fix. The **transformer** architecture eliminates recurrence entirely. Every token attends to every other token directly through **self-attention**, meaning that relationships between distant tokens are captured in a single operation rather than being passed through a chain of hidden states.

The core mechanism is **scaled dot-product attention**, which you know from your study of attention mechanisms. Each token is projected into three vectors — a **query** (Q), a **key** (K), and a **value** (V) — using learned linear transformations (the matrix operations from your prerequisites). Attention scores are computed as the dot product of each query with all keys, scaled by √dₖ to prevent the softmax from saturating, then used to weight the values. In **self-attention**, the queries, keys, and values all come from the same sequence, so every token computes a weighted combination of all other tokens in the sequence. This is done in parallel across all positions — no sequential bottleneck. **Multi-head attention** runs several independent attention operations in parallel, each with its own Q/K/V projections, allowing the model to attend to different types of relationships simultaneously (one head might capture syntactic structure while another captures semantic similarity).

Since self-attention treats the input as an unordered set, the model needs explicit information about token order. **Positional encodings** — fixed sinusoidal functions or learned vectors — are added to the input embeddings to provide this. Each transformer layer then applies self-attention followed by a position-wise **feedforward network** (two linear transformations with a nonlinearity between them), with **residual connections** and **layer normalization** around each sub-layer. Stacking multiple such layers creates a deep network where each layer refines the representations produced by the layer below.

The full transformer follows an **encoder-decoder** structure. The encoder processes the input through self-attention layers, producing contextualized representations. The decoder generates output tokens autoregressively: it uses **masked self-attention** (preventing positions from attending to future tokens, since those have not been generated yet) and **cross-attention** (attending to the encoder's output, exactly like the attention in seq2seq models). At inference time, the decoder generates one token at a time, appending each prediction to the input for the next step. Because all attention operations are matrix multiplications over the full sequence, training is massively parallelizable on GPUs — the key practical advantage that enabled scaling to billions of parameters. Transformers now underpin virtually all state-of-the-art language models, from BERT (encoder-only) to GPT (decoder-only) to T5 (encoder-decoder).
