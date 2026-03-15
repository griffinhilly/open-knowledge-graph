---
id: context-free-grammars-formal
title: Context-Free Grammars
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: pushdown-automata-formal
  type: hard
- id: set-fundamentals
  type: soft
- id: recursion-on-finite-structures
  type: soft
builds-toward:
- linear-bounded-automata
tags:
- formal-languages
- grammars
- context-free-languages
- parsing
stage: formal-systems
status: draft
---

# Context-Free Grammars

## Core Idea
A context-free grammar (CFG) generates strings through production rules that replace a single nonterminal with a string of terminals and nonterminals, regardless of surrounding context. The language of all derivable strings is a context-free language (CFL), and the class of CFLs is exactly the class recognized by nondeterministic pushdown automata. Every CFG can be converted to Chomsky normal form, where each production is either A -> BC or A -> a, enabling the CYK parsing algorithm. The pumping lemma for context-free languages proves that certain languages (e.g., {a^n b^n c^n}) are not context-free.

## How It's Best Learned
Write grammars for familiar languages — arithmetic expressions, matched parentheses, palindromes — and draw derivation (parse) trees. Then convert a grammar to Chomsky normal form step by step, and apply the CFL pumping lemma to prove {a^n b^n c^n} is not context-free. This builds intuition for where the stack-based model breaks down.

## Common Misconceptions
- Ambiguity is a property of a grammar, not the language — some CFLs have both ambiguous and unambiguous grammars, but inherently ambiguous CFLs exist where every grammar is ambiguous.
- Context-free grammars cannot express cross-serial dependencies like {a^n b^n c^n}, which is why natural language syntax sometimes requires mildly context-sensitive formalisms.
