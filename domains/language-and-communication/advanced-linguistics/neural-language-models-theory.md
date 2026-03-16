---
id: neural-language-models-theory
title: Neural Language Models and Transformers
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: compositional-semantics
  type: soft
- id: context-free-grammars-formal
  type: soft
tags:
- computational
- neural
- language-models
stage: advanced
status: draft
---

# Neural Language Models and Transformers

## Core Idea
Neural language models use deep learning to assign probabilities to word sequences. The transformer architecture, based on attention mechanisms, processes sequences in parallel by computing weighted combinations of all positions' representations. Large language models trained on billions of words achieve remarkable performance on generation and comprehension tasks, raising questions about the relationship between statistical pattern-matching and human linguistic knowledge.

## Explainer

You've already studied compositional semantics — the principle that the meaning of a complex expression is built systematically from the meanings of its parts according to grammatical rules — and formal grammars that specify the structural rules languages follow. Neural language models take a radically different approach to the same problem: rather than encoding explicit rules about meaning or structure, they learn statistical patterns from enormous quantities of text and use those patterns to predict what comes next. The contrast between these two approaches — rule-based versus statistical — is one of the most productive tensions in contemporary linguistics.

The core operation of a language model is **next-token prediction**. Given a sequence of words, predict the probability distribution over what comes next. If you train a model on enough text — hundreds of billions of words — it eventually learns that "the president signed the" is much more likely to be followed by "bill" than by "banana." What's remarkable is that this simple objective, iterated across billions of parameters, produces something that implicitly encodes grammatical structure, factual knowledge, and stylistic register. The model never sees an explicit rule about subject-verb agreement, but learns the pattern empirically from millions of examples. This raises a question directly relevant to your compositional semantics background: is the model learning the *rules*, or learning to mimic their surface effects without ever generalizing correctly to novel structures?

The **transformer architecture** is what makes this tractable at scale. Earlier neural models processed sequences step-by-step, which meant information from the beginning of a long sentence could effectively "fade out" by the end. The transformer's **attention mechanism** solves this by allowing every position in a sequence to directly attend to every other position, computing a weighted combination of all positions' representations simultaneously. To process "The lawyer who the journalist interviewed knew the senator," the model can directly connect "knew" with "lawyer" across the embedded relative clause rather than threading through each intervening word one at a time. This parallel processing also makes transformers far faster to train than sequential architectures, enabling the scale that makes modern large language models possible.

**Large language models** (LLMs) trained on internet-scale data display capabilities that surprised even their creators: they solve analogies, translate between languages, answer factual questions, write code, and generate text that is largely grammatical and contextually coherent. This creates a deep challenge for linguistic theory. Chomskyan linguistics argued for an innate **Universal Grammar** — a domain-specific faculty that allows children to acquire any human language despite impoverished input. LLMs acquire humanlike language behavior from vastly more input but no innate structure, suggesting that statistical learning over sufficient data may approximate the results of innate knowledge. Critics counter that LLMs fail in systematic ways that reveal they lack genuine structural understanding — they are pattern-matchers, not grammar-learners. The debate is unresolved, but LLMs are now the best-performing systems on nearly every language benchmark, and their existence has forced a productive reckoning with what linguistic theory actually needs to explain and what counts as evidence for or against internalized grammatical structure.

