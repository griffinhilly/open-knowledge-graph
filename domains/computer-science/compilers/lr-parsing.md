---
id: lr-parsing
title: LR Parsing Fundamentals
domain: computer-science
course: compilers
prerequisites:
- id: parsing-problem-overview
  type: hard
- id: stacks-data-structure
  type: hard
builds-toward:
- lr-state-machine-construction
- shift-reduce-parsing
tags:
- bottom-up-parsing
- shift-reduce
- parsing-tables
stage: advanced
status: draft
---

# LR Parsing Fundamentals

## Core Idea
LR parsing is bottom-up, deterministic parsing that constructs a parse tree by reducing input tokens to the start symbol. An LR parser maintains a stack of states and a lookahead token; each state encodes all possible actions (shift or reduce). LR parsers handle a much larger grammar class than LL, including left-recursive grammars, making them suitable for real programming languages.

## Explainer

If you understand the parsing problem — turning a flat sequence of tokens into a structured tree — then LR parsing is the most powerful deterministic approach to solving it. Where top-down parsers (like recursive descent) try to guess which grammar rule to apply by looking at the first few tokens, **LR parsing** works bottom-up: it reads tokens left to right, accumulates them, and waits until it has enough evidence to recognize which rule produced them. The name "LR" stands for Left-to-right scan, Rightmost derivation — it builds the parse tree from the leaves up to the root.

The core mechanism relies on the stack data structure you already know. An LR parser maintains a **stack of states**, where each state represents a set of partially-recognized grammar rules. At each step, the parser consults a **parsing table** indexed by the current state and the next input token (the lookahead). The table tells it to do one of two things: **shift** (push the current token and a new state onto the stack, then advance to the next token) or **reduce** (pop several items off the stack that match the right-hand side of a grammar rule, and push the left-hand side nonterminal back on). Think of it like assembling a puzzle from individual pieces — you keep picking up pieces (shifting) until you notice a group that forms a recognizable sub-picture (reducing).

Consider parsing the expression `3 + 4 * 5`. The parser shifts `3`, reduces it to an Expression, shifts `+`, shifts `4`, reduces to Expression, shifts `*`, shifts `5`, reduces to Expression. Now it sees `Expression * Expression` on the stack and reduces that to Expression (because `*` binds tighter). Then it sees `Expression + Expression` and reduces that. The parsing table encodes operator precedence and associativity — the parser never has to guess, because the table was precomputed from the grammar to resolve every possible ambiguity deterministically.

The power of LR parsing comes from what it can handle. Top-down parsers choke on **left-recursive grammars** (rules like `Expr → Expr + Term`), which naturally describe left-associative operators. LR parsers handle left recursion effortlessly because they build from the bottom up — they've already parsed the left operand before they need to decide about the rule. This is why parser generators like yacc and bison produce LR parsers: real programming language grammars are full of left recursion and operator precedence rules that would require awkward rewriting for a top-down parser. The tradeoff is that LR parsing tables can be large and the algorithm is harder to implement by hand, which is exactly why we use parser generators to build them automatically.
