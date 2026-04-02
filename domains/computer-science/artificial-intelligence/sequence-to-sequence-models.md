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
stage: expert
status: validated
---

# Sequence-to-Sequence Models

## Core Idea
Seq2seq models encode variable-length inputs and decode to variable-length outputs. Attention allows decoders to focus on relevant input parts. Applications include translation, summarization, and question answering. Beam search improves decoding quality.

## Questions

```yaml
- question: "A seq2seq model translates short sentences well but quality degrades sharply on paragraphs. What architectural feature most likely causes this?"
  type: multiple-choice
  options:
    - "The decoder LSTM cannot process more than one output token at a time"
    - "The encoder compresses the entire input into a fixed-size vector, losing information for long inputs"
    - "Beam search becomes computationally intractable for long sequences"
    - "LSTMs cannot maintain hidden state for more than 50 steps"
  answer: 1
  explanation: "The fixed-size context vector is the architectural bottleneck. Regardless of input length, the encoder must compress everything into one dense vector — a short sentence and a long paragraph must both fit into the same dimensionality. For long inputs, details inevitably get lost. This is the exact problem attention mechanisms solve by letting the decoder access all encoder hidden states, not just the final one."

- question: "During decoding, beam search with width k=5 is used instead of greedy decoding. Which best describes what beam search guarantees?"
  type: multiple-choice
  options:
    - "It finds the globally optimal output sequence with probability 1"
    - "It finds an output sequence at least as good as greedy decoding, but the global optimum is not guaranteed"
    - "It samples k diverse outputs randomly, improving expected quality"
    - "It guarantees the highest-probability individual token at every step"
  answer: 1
  explanation: "Beam search maintains the top-k partial sequences at each step and selects the highest-scoring complete sequence. It is strictly better than greedy decoding (k=1) because it considers more candidates, but it does not exhaustively search all possible outputs. The global optimum can still be missed if it was never in the beam. Beam search is a practical approximation, not an exact algorithm."

- question: "In a seq2seq model without attention, the decoder can primarily use information about the first few input tokens because LSTM hidden states decay over time."
  type: true-false
  answer: false
  explanation: "This conflates two issues. In a standard seq2seq model, the decoder uses the encoder's final hidden state — which ideally summarizes the entire input, not just the early tokens. The problem is not that early tokens are forgotten but that the final hidden state is a fixed-size vector that must encode everything, and very long sequences overload this fixed capacity. Attention solves a different problem: it lets the decoder actively query specific positions at each generation step, rather than relying solely on one summary vector."

- question: "With attention, the decoder can place different amounts of focus on different input positions at each generation step, rather than being restricted to a single fixed context vector."
  type: true-false
  answer: true
  explanation: "This is the defining property of attention. At each decoding step, the attention mechanism computes a weighted sum over all encoder hidden states, where the weights are learned based on compatibility between the current decoder state and each encoder state. The resulting context vector is different at each step — when generating a verb in translation, the model attends to the source verb; when generating a noun, it attends to the source noun. This dynamic access is what overcomes the fixed-vector bottleneck."

- question: "Why does the information bottleneck in a standard encoder-decoder model become a problem for long sequences, and how does attention address it?"
  type: short-answer
  answer: "The encoder must compress the entire input into a single fixed-size vector regardless of input length. For short inputs this works well, but long inputs contain more information than a fixed-size vector can represent — early content gets overwritten or diluted. Attention removes the bottleneck by keeping all encoder hidden states available and letting the decoder dynamically query the most relevant ones at each step, forming a different weighted combination depending on what is being generated."
  explanation: "The bottleneck is a capacity problem: a finite-dimensional vector is asked to carry infinite work as input grows. Attention replaces the fixed summary with a learnable lookup — at each decoding step, it computes how relevant each input position is to the current output, then creates a context vector as their weighted average. The encoder still processes the whole input, but nothing is permanently discarded — everything remains accessible."
```

## Explainer

Many important problems involve transforming one sequence into another where the input and output have different lengths. Translating "How are you?" (three words) to "Comment allez-vous ?" (two or three words depending on tokenization), summarizing a paragraph into a sentence, or converting a spoken utterance into a text transcription — none of these fit the fixed-input, fixed-output pattern of standard neural networks. **Sequence-to-sequence (seq2seq) models** solve this by splitting the problem into two halves: an **encoder** that reads the entire input and compresses it into a fixed representation, and a **decoder** that generates the output one token at a time from that representation.

The encoder, typically an LSTM or GRU network you have already studied, processes the input sequence token by token and produces a final hidden state — a dense vector that in principle captures the meaning of the entire input. The decoder is another recurrent network that takes this hidden state as its initial state and generates output tokens autoregressively: at each step, it predicts the next token, feeds that prediction back as input, and continues until it produces a special end-of-sequence token. This architecture elegantly handles variable-length inputs and outputs because the recurrent networks can process sequences of any length, and the hidden state acts as an information bottleneck bridging the two.

The bottleneck, however, is also the weakness. Compressing an entire input paragraph into a single fixed-size vector inevitably loses information, especially for long sequences. This is where **attention mechanisms** — which you have studied as a prerequisite — transform the architecture. Instead of relying solely on the final encoder hidden state, attention lets the decoder look back at *all* encoder hidden states at each generation step and compute a weighted combination of them. When translating a sentence, the decoder generating the French word for "cat" can attend strongly to the English word "cat" in the input, regardless of how far back it appeared. This alignment between input and output positions dramatically improves performance on long sequences.

During generation, the decoder must choose tokens one at a time, but greedily picking the highest-probability token at each step can lead to suboptimal overall sequences. **Beam search** addresses this by maintaining the top-k partial sequences (the "beam") at each step and expanding all of them, keeping only the k highest-scoring candidates. With a beam width of 5, for example, the decoder explores 5 promising hypotheses in parallel and selects the best complete sequence at the end. This is a practical compromise between the intractable exhaustive search over all possible outputs and the myopia of greedy decoding. Seq2seq with attention and beam search was the dominant architecture for machine translation and text generation before transformers, and understanding it is essential groundwork for the attention-only architectures that followed.
