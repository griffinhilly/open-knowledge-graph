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

## Questions

```yaml
- question: "A transformer model, trained only on next-token prediction with no explicit grammatical rules, correctly handles subject-verb agreement across long embedded relative clauses in sentence types that appear rarely in its training data. What would this finding most strongly suggest?"
  type: multiple-choice
  options:
    - "The model has memorized the specific sentences from training data"
    - "Statistical pattern-matching over sufficient data can produce some degree of structural generalization, challenging the claim that LLMs purely match surface patterns"
    - "The model has an innate grammatical faculty equivalent to Universal Grammar"
    - "Long-distance dependencies are not actually processed by the attention mechanism"
  answer: 1
  explanation: "If the model handles novel structural patterns it rarely saw, this pushes back on the 'mere pattern-matching' critique and suggests the statistical objective induces something resembling structural generalization. It does not prove the model has innate grammar (it learned from data, not innateness), nor does it prove it fully understands structure. This is exactly the kind of evidence that makes the debate productive — it shows LLMs do more than memorize surface patterns, without definitively resolving whether they internalize grammar the way humans do."

- question: "What problem with earlier sequential neural architectures does the transformer's attention mechanism directly solve?"
  type: multiple-choice
  options:
    - "Sequential models could not be parallelized during training, making them impossible to scale"
    - "Information from early in a sequence could fade out before the end, making long-range dependencies hard to capture; attention allows direct connections between any two positions"
    - "Sequential models could not process sentences longer than about 20 words"
    - "Attention allows the model to access external knowledge bases that sequential models could not"
  answer: 1
  explanation: "In sequential (RNN/LSTM) architectures, information about word position 1 must be threaded through every subsequent step to reach position 50 — it can effectively decay or be overwritten along the way. The attention mechanism bypasses this: every position computes a weighted combination of all other positions simultaneously. This makes it possible to connect 'knew' directly to 'lawyer' in 'The lawyer who the journalist interviewed knew the senator' without the intervening clause degrading the connection. Parallelization during training is also a benefit, but the conceptual advance is the direct position-to-position connection."

- question: "Large language models are trained on next-token prediction — they learn to predict which word comes next — without being given explicit rules about grammar or meaning."
  type: true-false
  answer: true
  explanation: "This is correct and is what makes LLMs remarkable. The training objective is purely statistical: given the preceding text, assign probabilities to all possible next tokens. No parse trees, no semantic rules, no explicit syntactic categories are provided. Yet from this objective alone, over sufficient data and parameters, LLMs develop representations that support grammatical sentences, stylistic register, factual knowledge, and cross-lingual translation. Whether this statistical learning captures the same kind of knowledge as human grammatical competence is the central open question."

- question: "LLMs' strong performance on language benchmarks demonstrates that human language acquisition does not require innate grammatical knowledge, definitively settling the debate over Universal Grammar."
  type: true-false
  answer: false
  explanation: "The debate remains unresolved. LLMs acquire language behavior from vastly more input than any child — hundreds of billions of words versus perhaps a few million in childhood — so they cannot straightforwardly demonstrate that statistical learning is sufficient given normal human input. Critics also argue that LLMs fail on systematic structural tests in ways that suggest they lack genuine grammatical knowledge. LLMs are the best-performing systems on benchmarks, which is relevant evidence, but 'best performance' on current tests does not settle the deeper theoretical question about what kind of knowledge underlies human language acquisition."

- question: "Why does the transformer's attention mechanism give it an advantage over step-by-step sequential processing for understanding language? Give an example of a sentence type where this advantage is particularly important."
  type: short-answer
  answer: "In sequential architectures, information propagates one step at a time, so connecting a verb to its subject across a long embedded clause requires the model to maintain that information through every intervening word — it can fade or be overwritten. The attention mechanism allows any position to directly attend to any other position in a single step, regardless of distance. Example: in 'The lawyer who the journalist interviewed knew the senator,' the model must connect 'knew' to 'lawyer' as subject-verb pair, skipping over the embedded relative clause 'who the journalist interviewed.' With attention, the model can directly weight 'lawyer' highly when processing 'knew'; with sequential processing, the relationship must survive being threaded through five intervening words."
  explanation: "Long-distance dependencies are a classic challenge for sequential architectures — often called the 'vanishing gradient' problem at its extreme. Attention's parallel structure sidesteps this by making distance in the sequence irrelevant to the directness of the connection, which is why transformers outperform sequential models on language tasks that require integrating information across long spans."
```

## Explainer

You've already studied compositional semantics — the principle that the meaning of a complex expression is built systematically from the meanings of its parts according to grammatical rules — and formal grammars that specify the structural rules languages follow. Neural language models take a radically different approach to the same problem: rather than encoding explicit rules about meaning or structure, they learn statistical patterns from enormous quantities of text and use those patterns to predict what comes next. The contrast between these two approaches — rule-based versus statistical — is one of the most productive tensions in contemporary linguistics.

The core operation of a language model is **next-token prediction**. Given a sequence of words, predict the probability distribution over what comes next. If you train a model on enough text — hundreds of billions of words — it eventually learns that "the president signed the" is much more likely to be followed by "bill" than by "banana." What's remarkable is that this simple objective, iterated across billions of parameters, produces something that implicitly encodes grammatical structure, factual knowledge, and stylistic register. The model never sees an explicit rule about subject-verb agreement, but learns the pattern empirically from millions of examples. This raises a question directly relevant to your compositional semantics background: is the model learning the *rules*, or learning to mimic their surface effects without ever generalizing correctly to novel structures?

The **transformer architecture** is what makes this tractable at scale. Earlier neural models processed sequences step-by-step, which meant information from the beginning of a long sentence could effectively "fade out" by the end. The transformer's **attention mechanism** solves this by allowing every position in a sequence to directly attend to every other position, computing a weighted combination of all positions' representations simultaneously. To process "The lawyer who the journalist interviewed knew the senator," the model can directly connect "knew" with "lawyer" across the embedded relative clause rather than threading through each intervening word one at a time. This parallel processing also makes transformers far faster to train than sequential architectures, enabling the scale that makes modern large language models possible.

**Large language models** (LLMs) trained on internet-scale data display capabilities that surprised even their creators: they solve analogies, translate between languages, answer factual questions, write code, and generate text that is largely grammatical and contextually coherent. This creates a deep challenge for linguistic theory. Chomskyan linguistics argued for an innate **Universal Grammar** — a domain-specific faculty that allows children to acquire any human language despite impoverished input. LLMs acquire humanlike language behavior from vastly more input but no innate structure, suggesting that statistical learning over sufficient data may approximate the results of innate knowledge. Critics counter that LLMs fail in systematic ways that reveal they lack genuine structural understanding — they are pattern-matchers, not grammar-learners. The debate is unresolved, but LLMs are now the best-performing systems on nearly every language benchmark, and their existence has forced a productive reckoning with what linguistic theory actually needs to explain and what counts as evidence for or against internalized grammatical structure.

