---
id: computational-parsing-algorithms
title: Computational Parsing Algorithms and Complexity
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: lambda-calculus-for-linguistics
  type: soft
tags:
- parsing
- algorithms
- computational
stage: advanced
status: draft
---

# Computational Parsing Algorithms and Complexity

## Core Idea
Computational parsing algorithms (CKY, Earley, shift-reduce) recover syntactic structure from sequences of words, taking as input a grammar and a sentence. Algorithms differ in complexity, coverage, and efficiency—CKY is O(n³) in sentence length for context-free grammars, while neural parsers learn patterns without explicit grammar rules. Modern statistical and neural approaches achieve high accuracy on benchmark corpora but sometimes fail in linguistically unexpected ways.

## How It's Best Learned
Implement or trace through a parsing algorithm on sample sentences, observing complexity and derivation paths. Compare predictions of traditional and neural parsers on ambiguous or difficult sentences.

## Common Misconceptions
- More efficient algorithms do not necessarily parse more accurately; efficiency and accuracy trade off.
- Neural parsers do not simulate human parsing; they achieve different biases and error patterns.

## Explainer

Parsing is the problem of recovering structure from a linear sequence of symbols given a grammar — the same task you do intuitively when you understand a sentence, but made explicit and formal. From your work with lambda calculus for linguistics, you know that meaning composition requires knowing structure: you can't apply the right semantic rules without knowing which phrases combine with which. A **parser** takes a string of words and a grammar, and returns one or more parse trees — the hierarchical structures that make semantic composition possible. The algorithmic question is: how do you find those trees efficiently, especially when the same substring can be parsed multiple ways?

The **CKY algorithm** (Cocke-Kasami-Younger) answers this with **dynamic programming**. It works on grammars in Chomsky Normal Form, where every rule has the shape A → BC or A → word. CKY builds a triangular chart: the cell at row *i*, column *j* stores all the non-terminals that can span from word *i* to word *j* in the input. It fills the chart bottom-up — first single words, then spans of length 2, then 3, and so on — reusing subresults rather than recomputing them. Because each cell combines at most two smaller cells, and there are O(n²) cells each requiring O(n) combination attempts, total complexity is **O(n³)** in sentence length. For typical sentences this is tractable; for very long sentences it can become slow.

**Earley parsing** takes a top-down, left-to-right approach that handles arbitrary context-free grammars without requiring Chomsky Normal Form. It maintains a chart of **items** — partially matched rules — and processes the input incrementally, predicting what rules might apply, scanning the next word, and completing rules when all their right-hand symbols have been matched. Earley is more flexible than CKY and handles ambiguous and even mildly context-sensitive grammars gracefully, though its worst-case complexity is also O(n³). **Shift-reduce parsing** (used in many practical NLP systems) is faster but makes early commitments: it either shifts the next word onto a stack or reduces the top of the stack by a grammar rule, with no backtracking. These commitments make shift-reduce susceptible to **garden-path errors** — the same temporary ambiguities that trip up human readers — and it's no accident that shift-reduce mirrors some aspects of human incremental parsing.

**Neural parsers** — particularly those based on deep learning over word embeddings — learn to produce parse trees from training data without explicit grammar rules. They can achieve high accuracy on standard benchmarks and handle the long-tail of constructions that hand-written grammars miss. But they fail differently from rule-based systems: they can confidently produce structurally plausible but semantically nonsensical parses for unusual inputs, and their errors don't follow the systematic patterns you'd expect from a grammar. The key insight from the misconceptions above is that **efficiency and accuracy are separate axes**: a fast O(n) neural model might outperform a theoretically complete O(n³) chart parser on typical text, but perform worse on the unusual sentences that fall outside its training distribution. Choosing a parser involves understanding which failure modes matter for your application.
