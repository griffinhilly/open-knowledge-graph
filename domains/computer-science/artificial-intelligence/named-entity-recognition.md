---
id: named-entity-recognition
title: Named Entity Recognition (NER)
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: nlp-language-models
  type: hard
- id: neural-networks-intro
  type: hard
- id: sequence-to-sequence-models
  type: soft
tags:
- nlp
- sequence-labeling
- entity-extraction
- information-extraction
stage: advanced
status: draft
---

# Named Entity Recognition (NER)

## Core Idea
Named entity recognition identifies and classifies named entities (people, organizations, locations, dates) in text as a sequence labeling task. BiLSTM-CRF models combine bidirectional context with Markov constraints on valid label transitions; transformer models achieve state-of-the-art performance through contextual embeddings that capture long-range dependencies.

## How It's Best Learned
Implement NER using BiLSTM-CRF and compare with transformer-based models (BERT fine-tuned), observing how architectural differences affect recognition accuracy and speed.

## Questions

```yaml
- question: "A NER system classifies each token independently, selecting the highest-probability label at each position without considering neighboring labels. What critical problem does this create that a CRF layer would prevent?"
  type: multiple-choice
  options:
    - "It cannot process sentences longer than the model's maximum sequence length"
    - "It may produce structurally invalid label sequences, such as I-PER appearing without a preceding B-PER"
    - "It assigns lower confidence scores, making the predictions unreliable for downstream use"
    - "It cannot distinguish between entity types that appear in similar grammatical positions"
  answer: 1
  explanation: "A greedy per-token classifier maximizes local probability at each step but has no mechanism to enforce structural constraints across positions. This allows invalid sequences like O → I-PER (continuation tag with no beginning tag) or B-LOC → I-PER (continuation of one type following the beginning of another). The CRF layer learns a transition matrix over label pairs, scores entire sequences globally, and uses Viterbi decoding to find the most probable valid sequence."

- question: "In 'Washington issued a statement,' a NER system correctly tags 'Washington' as an organization, while in 'Washington crossed the Delaware,' it tags 'Washington' as a person. Which architectural feature of BERT explains this disambiguation?"
  type: multiple-choice
  options:
    - "Byte-pair encoding, which creates distinct subword tokens for words used in different semantic roles"
    - "Contextual embeddings that produce different vector representations for the same token depending on surrounding context"
    - "The CRF transition layer, which knows that person names tend to precede action verbs like 'crossed'"
    - "Attention heads that explicitly attend to the word 'Delaware' and infer that Washington must be a person"
  answer: 1
  explanation: "BERT's key advantage for NER is that its embeddings are contextual — unlike static word embeddings (Word2Vec, GloVe), BERT generates a different vector for 'Washington' based on its full surrounding context. In a political news context, Washington gets one representation; in a historical narrative, it gets another. This context-sensitivity, learned during pretraining on massive corpora, lets the model disambiguate entity type without explicit rules."

- question: "The BIO tagging scheme (Beginning, Inside, Outside) is necessary for NER because without it, a model cannot determine where one multi-word entity ends and another begins."
  type: true-false
  answer: true
  explanation: "Consider 'Steve Jobs' and 'Tim Cook' appearing consecutively. Without B/I markers, both would be labeled PER PER PER PER — indistinguishable from one four-word person name or any other grouping. The B-PER tag marks the start of a new entity, resetting the boundary, while I-PER marks continuation. This scheme also allows adjacent entities of the same type to be correctly segmented."

- question: "A BiLSTM-CRF NER model assigns each token a label based only on that token and its immediate neighbors, making it fundamentally similar to an n-gram classifier."
  type: true-false
  answer: false
  explanation: "The 'Bi' in BiLSTM stands for bidirectional — the model processes the full sentence in both left-to-right and right-to-left directions. Each token's representation is informed by the entire sentence context on both sides, not just local neighbors. This global context is one of the BiLSTM's core advantages over n-gram approaches and is what allows it to resolve long-range dependencies in entity spans."

- question: "Why does adding a CRF layer on top of a BiLSTM improve NER performance, rather than simply taking the highest-probability label at each token position?"
  type: short-answer
  answer: "A CRF scores entire label sequences jointly using a learned transition matrix between adjacent label pairs, then finds the globally optimal valid sequence via Viterbi decoding. Greedy per-position selection can produce locally plausible but globally inconsistent outputs (e.g., I-PER after B-LOC) that the CRF's structural constraints prevent."
  explanation: "The insight is local vs. global optimization. Token-level classification maximizes probability at each step independently, which can produce sequences that violate the structural rules of BIO tagging. The CRF explicitly models label-to-label transitions, penalizing invalid combinations. At inference, Viterbi efficiently finds the highest-scoring sequence across all positions simultaneously — this is analogous to enforcing grammar constraints in parsing rather than choosing words one at a time."
```

## Explainer

Named entity recognition is the task of scanning a sentence and identifying which words refer to real-world entities — and what kind of entity each one is. Given the sentence "Apple was founded by Steve Jobs in Cupertino in 1976," a NER system should tag "Apple" as an organization, "Steve Jobs" as a person, "Cupertino" as a location, and "1976" as a date. This is fundamentally a **sequence labeling** problem: each token in the input receives a label, and the model must decide the correct label for every position in the sequence.

The labeling scheme itself requires care. The standard approach is **BIO tagging** (Beginning, Inside, Outside): the first token of an entity gets a B-tag (e.g., B-PER for the start of a person name), continuation tokens get I-tags (I-PER), and non-entity tokens get O. This lets the model handle multi-word entities like "Steve Jobs" (B-PER I-PER) and distinguish adjacent entities of the same type. Without the B/I distinction, the model could not tell where one entity ends and the next begins.

The classic neural architecture for NER is the **BiLSTM-CRF**. You already know that neural networks can learn contextual representations — the BiLSTM reads the sentence in both directions, giving each token a representation informed by its full context. But sequence labeling has a structural constraint that a standard classifier ignores: adjacent labels are not independent. An I-PER tag should never follow a B-LOC tag, and an I-tag should never appear at the start of a sequence. The **CRF (Conditional Random Field)** layer on top of the BiLSTM learns a transition matrix between label pairs, scoring not just individual tag probabilities but entire label sequences. At inference time, the Viterbi algorithm efficiently finds the highest-scoring global label sequence rather than greedily picking the best tag at each position.

Transformer-based models like BERT have largely surpassed BiLSTM-CRFs by providing richer contextual embeddings. A fine-tuned BERT model for NER feeds its contextualized token representations into a classification head (with or without a CRF layer). The advantage is that BERT's pretraining on massive text corpora gives it deep knowledge of language structure and word usage patterns before it ever sees NER-labeled data. The word "Washington" in "Washington crossed the Delaware" and "Washington issued a statement" gets different contextual embeddings, helping the model distinguish person from organization or location uses. This contextual sensitivity, combined with the attention mechanism's ability to capture long-range dependencies, explains why transformer models achieve state-of-the-art NER performance across most benchmarks.
