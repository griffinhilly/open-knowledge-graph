---
id: nlp-language-models
title: Language Models and Neural Language Modeling
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: transformer-architecture
  type: hard
tags:
- nlp
- language-models
- deep-learning
stage: advanced
status: draft
---

# Language Models and Neural Language Modeling

## Core Idea
Language models compute P(next_token|context) autoregressively. Neural LMs use RNNs or Transformers. Large pre-trained models (GPT, BERT) learn via self-supervised tasks: next-token (decoder) or masked token (encoder) prediction.

## Explainer

A **language model** answers one deceptively simple question: given a sequence of words (or tokens), what comes next? Formally, it estimates the conditional probability P(next token | preceding context). This is the foundation of virtually all modern NLP — from autocomplete to machine translation to chatbots. Building on your understanding of transformer architecture, language models are the training framework that turns raw neural network architectures into systems that understand and generate language.

The dominant training approach is **self-supervised learning**, meaning the model learns from unlabeled text by predicting parts of its own input. There are two main paradigms. **Autoregressive models** (like GPT) are trained to predict the next token given all previous tokens — they read left to right and generate text one token at a time. **Masked language models** (like BERT) randomly hide tokens in the input and train the network to fill in the blanks, allowing the model to use context from both directions. The distinction matters: autoregressive models excel at text generation, while masked models excel at understanding tasks like classification and question answering.

What makes modern **neural language models** so powerful is scale. Early statistical language models used n-gram counts — the probability of a word given the previous two or three words. These models could not capture long-range dependencies ("The cat that the dog that the boy owned chased ran away" — what ran away?). Transformer-based language models, with their self-attention mechanism, can attend to any position in the context window, capturing dependencies across hundreds or thousands of tokens. When trained on billions of words, these models develop remarkable emergent abilities: they learn grammar, facts about the world, reasoning patterns, and even some capacity for novel problem-solving — all from the simple objective of predicting the next token.

The practical workflow for using language models follows a **pre-train then fine-tune** paradigm. A large model is first pre-trained on massive text corpora (books, web pages, code) to learn general language understanding. This pre-trained model is then **fine-tuned** on a smaller, task-specific dataset — sentiment classification, summarization, or dialogue — adapting its general knowledge to a specific application. This transfer learning approach is why a single architecture like the transformer can power dozens of different NLP applications, and why understanding language models is the gateway to the rest of modern NLP.
