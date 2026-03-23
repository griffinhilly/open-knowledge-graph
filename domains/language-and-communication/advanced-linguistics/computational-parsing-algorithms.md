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
stage: expert
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

## Questions

```yaml
- question: "An NLP team replaces a CKY chart parser with a neural parser because the neural model scores higher on a benchmark of standard news text. Months later, the system fails badly on technical documents with unusual syntactic constructions. What does this failure most directly illustrate?"
  type: multiple-choice
  options:
    - "CKY is always more accurate than neural parsers because it uses explicit grammar rules that generalize better"
    - "Neural parsers are O(n³) on technical text, causing them to time out on long sentences"
    - "Benchmark accuracy and out-of-distribution robustness are different properties; a faster, higher-scoring parser can still fail in ways a grammar-based parser would not"
    - "The team should have used an Earley parser, which handles arbitrary context-free grammars and therefore generalizes to any text"
  answer: 2
  explanation: "Efficiency and accuracy are separate from robustness to unusual inputs. A neural parser trained on news text may score very highly on that benchmark while failing on constructions outside its training distribution — confidently producing plausible-looking but wrong parses. A chart parser like CKY, by contrast, is theoretically complete for its grammar: if the grammar covers a construction, the parser will find it. The benchmark result measures performance on typical text, not on tail cases. Choosing a parser means understanding which failure modes matter for your application."

- question: "A shift-reduce parser, processing the sentence 'The horse raced past the barn fell,' successfully reduces 'the horse raced past the barn' as a complete verb phrase before encountering 'fell' — and then cannot recover. Why does this happen?"
  type: multiple-choice
  options:
    - "Shift-reduce requires Chomsky Normal Form, and this sentence contains a reduced relative clause that violates CNF"
    - "The O(n³) complexity of shift-reduce causes it to time out on garden-path constructions"
    - "Shift-reduce makes early, irrevocable commitments — once it reduces 'raced past the barn' as a main verb, it cannot reanalyze it as a relative clause modifier"
    - "Shift-reduce processes input right-to-left and therefore misses the main verb 'fell' at the end"
  answer: 2
  explanation: "Shift-reduce parsing is a greedy left-to-right algorithm: at each step it either shifts the next word onto a stack or reduces the top of the stack using a grammar rule, with no backtracking. When it reduces 'the horse raced past the barn' as a complete clause, it commits to that analysis and has no mechanism to revise it when 'fell' arrives. Chart parsers (CKY, Earley) avoid this by maintaining all possible analyses simultaneously until the full sentence is processed. The garden-path effect is not a bug in shift-reduce — it mirrors aspects of how human incremental processing also makes early commitments."

- question: "CKY can parse any context-free grammar as long as the sentence is unambiguous."
  type: true-false
  answer: false
  explanation: "CKY requires the grammar to be in Chomsky Normal Form (CNF), where every rule is either A → BC or A → word. This is not a restriction on ambiguity but on rule structure. Any context-free grammar can be converted to CNF, but CKY cannot directly process arbitrary CFGs — the grammar must be preprocessed into CNF first. Earley parsing, by contrast, handles arbitrary context-free grammars directly without CNF conversion, and also handles ambiguous sentences by returning all possible parse trees."

- question: "An O(n) neural parser will always be less accurate than an O(n³) chart parser, because higher time complexity reflects more thorough examination of the input."
  type: true-false
  answer: false
  explanation: "Efficiency (time complexity) and accuracy are independent properties. An O(n) neural parser can outperform an O(n³) chart parser on typical benchmark text — it has learned patterns from large training corpora that let it make accurate predictions quickly. Complexity bounds describe how computation scales with input length, not how well the output matches the correct parse. In practice, modern neural parsers achieve state-of-the-art accuracy on standard benchmarks despite their speed. However, they fail differently: they are less robust to unusual constructions outside their training distribution, whereas a complete chart parser is bounded by its grammar coverage."

- question: "Explain the core tradeoff between shift-reduce and chart parsing approaches like CKY or Earley. Why is shift-reduce faster, and what does it sacrifice?"
  type: short-answer
  answer: "Shift-reduce is fast because it processes the input greedily from left to right with a single pass, making immediate reduce/shift decisions without revisiting earlier choices. It sacrifices completeness: once it commits to a reduction, it cannot backtrack if that analysis turns out to be wrong when more input arrives. Chart parsers (CKY, Earley) sacrifice speed for completeness: they maintain a chart of all possible partial analyses and never discard alternatives until the full input is seen, guaranteeing they find all valid parses (at O(n³) cost). The tradeoff is early commitment (fast but error-prone on ambiguous/garden-path sentences) versus delayed commitment (thorough but slower)."
  explanation: "This tradeoff mirrors the accuracy/efficiency tradeoff more broadly. Shift-reduce is used in many production NLP systems because it's fast enough and usually correct on typical input. But it embodies a design choice: trade theoretical guarantees for practical speed. Chart parsers are theoretically attractive but computationally heavier. Neural parsers reframe the tradeoff entirely — they learn heuristics from data rather than implementing an explicit algorithm, achieving high speed and accuracy on typical text while failing differently on atypical input."
```

## Explainer

Parsing is the problem of recovering structure from a linear sequence of symbols given a grammar — the same task you do intuitively when you understand a sentence, but made explicit and formal. From your work with lambda calculus for linguistics, you know that meaning composition requires knowing structure: you can't apply the right semantic rules without knowing which phrases combine with which. A **parser** takes a string of words and a grammar, and returns one or more parse trees — the hierarchical structures that make semantic composition possible. The algorithmic question is: how do you find those trees efficiently, especially when the same substring can be parsed multiple ways?

The **CKY algorithm** (Cocke-Kasami-Younger) answers this with **dynamic programming**. It works on grammars in Chomsky Normal Form, where every rule has the shape A → BC or A → word. CKY builds a triangular chart: the cell at row *i*, column *j* stores all the non-terminals that can span from word *i* to word *j* in the input. It fills the chart bottom-up — first single words, then spans of length 2, then 3, and so on — reusing subresults rather than recomputing them. Because each cell combines at most two smaller cells, and there are O(n²) cells each requiring O(n) combination attempts, total complexity is **O(n³)** in sentence length. For typical sentences this is tractable; for very long sentences it can become slow.

**Earley parsing** takes a top-down, left-to-right approach that handles arbitrary context-free grammars without requiring Chomsky Normal Form. It maintains a chart of **items** — partially matched rules — and processes the input incrementally, predicting what rules might apply, scanning the next word, and completing rules when all their right-hand symbols have been matched. Earley is more flexible than CKY and handles ambiguous and even mildly context-sensitive grammars gracefully, though its worst-case complexity is also O(n³). **Shift-reduce parsing** (used in many practical NLP systems) is faster but makes early commitments: it either shifts the next word onto a stack or reduces the top of the stack by a grammar rule, with no backtracking. These commitments make shift-reduce susceptible to **garden-path errors** — the same temporary ambiguities that trip up human readers — and it's no accident that shift-reduce mirrors some aspects of human incremental parsing.

**Neural parsers** — particularly those based on deep learning over word embeddings — learn to produce parse trees from training data without explicit grammar rules. They can achieve high accuracy on standard benchmarks and handle the long-tail of constructions that hand-written grammars miss. But they fail differently from rule-based systems: they can confidently produce structurally plausible but semantically nonsensical parses for unusual inputs, and their errors don't follow the systematic patterns you'd expect from a grammar. The key insight from the misconceptions above is that **efficiency and accuracy are separate axes**: a fast O(n) neural model might outperform a theoretically complete O(n³) chart parser on typical text, but perform worse on the unusual sentences that fall outside its training distribution. Choosing a parser involves understanding which failure modes matter for your application.
