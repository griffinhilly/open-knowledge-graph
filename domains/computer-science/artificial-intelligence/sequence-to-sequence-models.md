---
id: sequence-to-sequence-models
title: Sequence-to-Sequence Models
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: lstm-gated-networks
  type: hard
- id: attention-mechanisms
  type: hard
tags:
- nlp
- sequence-models
- encoder-decoder
stage: advanced
status: draft
---

# Sequence-to-Sequence Models

## Core Idea
Seq2seq models encode variable-length inputs and decode to variable-length outputs. Attention allows decoders to focus on relevant input parts. Applications include translation, summarization, and question answering. Beam search improves decoding quality.

## Explainer

Many important problems involve transforming one sequence into another where the input and output have different lengths. Translating "How are you?" (three words) to "Comment allez-vous ?" (two or three words depending on tokenization), summarizing a paragraph into a sentence, or converting a spoken utterance into a text transcription — none of these fit the fixed-input, fixed-output pattern of standard neural networks. **Sequence-to-sequence (seq2seq) models** solve this by splitting the problem into two halves: an **encoder** that reads the entire input and compresses it into a fixed representation, and a **decoder** that generates the output one token at a time from that representation.

The encoder, typically an LSTM or GRU network you have already studied, processes the input sequence token by token and produces a final hidden state — a dense vector that in principle captures the meaning of the entire input. The decoder is another recurrent network that takes this hidden state as its initial state and generates output tokens autoregressively: at each step, it predicts the next token, feeds that prediction back as input, and continues until it produces a special end-of-sequence token. This architecture elegantly handles variable-length inputs and outputs because the recurrent networks can process sequences of any length, and the hidden state acts as an information bottleneck bridging the two.

The bottleneck, however, is also the weakness. Compressing an entire input paragraph into a single fixed-size vector inevitably loses information, especially for long sequences. This is where **attention mechanisms** — which you have studied as a prerequisite — transform the architecture. Instead of relying solely on the final encoder hidden state, attention lets the decoder look back at *all* encoder hidden states at each generation step and compute a weighted combination of them. When translating a sentence, the decoder generating the French word for "cat" can attend strongly to the English word "cat" in the input, regardless of how far back it appeared. This alignment between input and output positions dramatically improves performance on long sequences.

During generation, the decoder must choose tokens one at a time, but greedily picking the highest-probability token at each step can lead to suboptimal overall sequences. **Beam search** addresses this by maintaining the top-k partial sequences (the "beam") at each step and expanding all of them, keeping only the k highest-scoring candidates. With a beam width of 5, for example, the decoder explores 5 promising hypotheses in parallel and selects the best complete sequence at the end. This is a practical compromise between the intractable exhaustive search over all possible outputs and the myopia of greedy decoding. Seq2seq with attention and beam search was the dominant architecture for machine translation and text generation before transformers, and understanding it is essential groundwork for the attention-only architectures that followed.
