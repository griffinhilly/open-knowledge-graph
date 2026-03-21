---
id: lookahead-and-parsing-power
title: Lookahead in Parsing and Grammar Classes
domain: computer-science
course: compilers
prerequisites:
- id: ll-parsing
  type: hard
- id: lr-parsing
  type: hard
builds-toward:
- compiler-error-recovery
tags:
- parsing
- theory
- lookahead
stage: advanced
status: draft
---

# Lookahead in Parsing and Grammar Classes

## Core Idea
Different parsers require different lookahead: LL(1) uses 1-token lookahead and is limited to certain grammar classes; LR(1) implicitly encodes more context in parse tables. Understanding lookahead determines parsing algorithm selection and reveals whether a grammar is parseable without backtracking.

## Questions

```yaml
- question: "An LL(1) parser and an LR(1) parser both use exactly one token of lookahead. Why is LR(1) strictly more powerful?"
  type: multiple-choice
  options:
    - "LR(1) parsers read tokens from right to left, gaining more context about the input structure"
    - "LR(1) parsers encode the complete left context (everything already parsed) in their state, so the same single lookahead token carries more disambiguating information in combination with that accumulated context"
    - "LR(1) parsers use a stack of tokens rather than a single lookahead, effectively seeing multiple symbols ahead"
    - "LR(1) parsers can backtrack and try alternative parses when a conflict occurs"
  answer: 1
  explanation: "The key insight is that 'one token of lookahead' means different things for LL and LR parsers. An LL(1) parser decides which production to expand based on: the current nonterminal + one lookahead token. An LR(1) parser decides based on: its current state (which encodes the *entire* left context — all input already parsed) + one lookahead token. The LR state contains far more information than just the current nonterminal, which is why LR(1) grammars strictly include all LL(1) grammars."

- question: "A grammar has an LL(1) conflict because two productions for nonterminal A both can follow the same FIRST token. Which approach will NOT genuinely resolve the conflict?"
  type: multiple-choice
  options:
    - "Left-factor the grammar to share the common prefix in a single production before branching"
    - "Switch to an LR(1) parser generator, since LR(1) can handle this grammar class"
    - "Increase the lookahead to LL(2), which may resolve the conflict if the second token disambiguates"
    - "Use a Yacc/PLY parser, since it automatically resolves all conflicts via default shift/reduce rules"
  answer: 3
  explanation: "Yacc/PLY-style LALR parsers 'resolve' conflicts by applying default rules (prefer shift over reduce, prefer earlier rule over later), which silently produces a parser that may accept incorrect programs. This is not a real fix — it hides the conflict rather than resolving it. Left-factoring (option A) is the correct grammar-rewriting approach. Switching to LR (option B) works if the grammar is LR(1). Increasing to LL(2) (option C) may genuinely resolve some conflicts. Option D is the trap: automatic conflict resolution is not the same as correctly handling the grammar."

- question: "Every grammar that is LL(1) is also LR(1), but not every LR(1) grammar is LL(1)."
  type: true-false
  answer: true
  explanation: "The parsing power hierarchy is strict: LL(1) ⊂ LR(1). Any grammar an LL(1) parser can handle can also be handled by an LR(1) parser. The converse is false: many LR(1) grammars — including those with left recursion — cannot be handled by LL(1) parsers at all, because LL parsers must predict which production to expand before consuming input, while LR parsers defer the decision until the full left context is accumulated."

- question: "An LR(1) parser examines more tokens of lookahead than an LL(1) parser, which is why it can handle more grammars."
  type: true-false
  answer: false
  explanation: "Both LL(1) and LR(1) examine exactly one token of lookahead — the '1' in each name means one token. LR(1)'s greater power comes from its state, not from seeing further ahead. The LR automaton's state encodes the complete left context of the parse, providing far more disambiguating information than just the current nonterminal. The single lookahead token is combined with this rich state to make decisions impossible for a top-down parser seeing only the current nonterminal and one token ahead."

- question: "Why can't an LL parser handle left-recursive grammars, even with increased lookahead?"
  type: short-answer
  answer: "An LL parser works top-down: it selects a production to expand by looking ahead in the input. With a left-recursive production like A → A α | β, expanding A via A → A α immediately requires expanding A again — an infinite loop. The parser consumes no input while recursing, so no amount of lookahead resolves the problem; the issue is structural, not informational. LR parsers avoid this by building bottom-up: they recognize the 'A' subexpression from actual input tokens before deciding it is an A, with no need to predict the recursive structure upfront."
  explanation: "Left recursion is the clearest example of a structural grammar property that prevents LL parsing regardless of lookahead amount. It can be eliminated by grammar transformation (replacing left recursion with right recursion and iteration), but this changes the grammar's structure and can complicate semantic action embedding."
```

## Explainer

From your study of LL and LR parsing, you know that parsers make decisions about which production rule to apply based on the tokens they can see ahead in the input stream. **Lookahead** is precisely this: the number of tokens a parser examines beyond the current position to decide its next action. The amount of lookahead a parser uses directly determines which grammars it can handle — this is what defines grammar classes like LL(1), LL(2), LR(0), LR(1), and so on.

Consider how an LL(1) parser works: it sits at a nonterminal, looks at exactly one token ahead, and must decide which production to expand. If two productions for the same nonterminal could both start with the same token, the parser cannot choose between them — the grammar is not LL(1). For example, if you have productions `A → if expr then stmt` and `A → if expr then stmt else stmt`, the parser sees `if` and cannot tell which rule to use. This is the classic **dangling-else ambiguity**, and it illustrates how limited lookahead restricts the grammars a parser can handle. Increasing to LL(2) lets the parser see two tokens ahead, resolving some ambiguities, but the grammar class is still fundamentally top-down and cannot handle left recursion.

LR parsers gain power from a different mechanism. Rather than predicting which rule to use by looking ahead from the top, LR parsers build up recognized fragments from the bottom and decide only when they have enough context. An LR(1) parser carries one token of lookahead, but because it also encodes the entire left context (everything already parsed) in its state, it can distinguish situations that would be ambiguous to an LL parser. This is why LR(1) grammars are a strict superset of LL(1) grammars — the parser effectively "sees" more context even with the same single token of lookahead. LALR(1) parsers, which you studied in grammar construction, compress the LR(1) state space at the cost of occasionally introducing conflicts that a full LR(1) parser would not have.

The practical takeaway is a hierarchy of parsing power: LL(1) ⊂ LL(k) ⊂ LR(1) ⊂ LR(k), with each step either increasing lookahead or using a more powerful parsing strategy. When designing a language or choosing a parser generator, this hierarchy tells you what is achievable. If your grammar has conflicts under LL(1), you can try refactoring it (left-factoring, removing left recursion) or switch to a more powerful parser class. Understanding where your grammar sits in this hierarchy prevents wasted effort — you will know whether a conflict is fixable by grammar rewriting or whether you need a fundamentally different parsing approach.
