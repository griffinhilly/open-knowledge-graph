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
