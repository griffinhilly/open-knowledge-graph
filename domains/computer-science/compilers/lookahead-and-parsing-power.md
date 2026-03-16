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

## Explainer

From your study of LL and LR parsing, you know that parsers make decisions about which production rule to apply based on the tokens they can see ahead in the input stream. **Lookahead** is precisely this: the number of tokens a parser examines beyond the current position to decide its next action. The amount of lookahead a parser uses directly determines which grammars it can handle — this is what defines grammar classes like LL(1), LL(2), LR(0), LR(1), and so on.

Consider how an LL(1) parser works: it sits at a nonterminal, looks at exactly one token ahead, and must decide which production to expand. If two productions for the same nonterminal could both start with the same token, the parser cannot choose between them — the grammar is not LL(1). For example, if you have productions `A → if expr then stmt` and `A → if expr then stmt else stmt`, the parser sees `if` and cannot tell which rule to use. This is the classic **dangling-else ambiguity**, and it illustrates how limited lookahead restricts the grammars a parser can handle. Increasing to LL(2) lets the parser see two tokens ahead, resolving some ambiguities, but the grammar class is still fundamentally top-down and cannot handle left recursion.

LR parsers gain power from a different mechanism. Rather than predicting which rule to use by looking ahead from the top, LR parsers build up recognized fragments from the bottom and decide only when they have enough context. An LR(1) parser carries one token of lookahead, but because it also encodes the entire left context (everything already parsed) in its state, it can distinguish situations that would be ambiguous to an LL parser. This is why LR(1) grammars are a strict superset of LL(1) grammars — the parser effectively "sees" more context even with the same single token of lookahead. LALR(1) parsers, which you studied in grammar construction, compress the LR(1) state space at the cost of occasionally introducing conflicts that a full LR(1) parser would not have.

The practical takeaway is a hierarchy of parsing power: LL(1) ⊂ LL(k) ⊂ LR(1) ⊂ LR(k), with each step either increasing lookahead or using a more powerful parsing strategy. When designing a language or choosing a parser generator, this hierarchy tells you what is achievable. If your grammar has conflicts under LL(1), you can try refactoring it (left-factoring, removing left recursion) or switch to a more powerful parser class. Understanding where your grammar sits in this hierarchy prevents wasted effort — you will know whether a conflict is fixable by grammar rewriting or whether you need a fundamentally different parsing approach.
