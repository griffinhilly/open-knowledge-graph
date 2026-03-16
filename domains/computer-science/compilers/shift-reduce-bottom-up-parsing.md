---
id: shift-reduce-bottom-up-parsing
title: Shift-Reduce Bottom-Up Parsing
domain: computer-science
course: compilers
prerequisites:
- id: grammar-design-for-compilation
  type: hard
- id: parse-trees-derivations
  type: soft
builds-toward:
- lalr-grammar-construction
- parser-conflict-resolution
tags:
- bottom-up-parsing
- lr-parsing
- shift-reduce
stage: advanced
status: draft
---

# Shift-Reduce Bottom-Up Parsing

## Core Idea
Bottom-up shift-reduce parsers build parse trees from leaves up, using a stack to accumulate symbols and reduce them when grammar rules match. This approach is more powerful than top-down parsing and handles a wider class of unambiguous grammars.

## How It's Best Learned
Manually build shift-reduce parse trees for example inputs. Implement a simple shift-reduce parser with an explicit stack.

## Common Misconceptions
Only bottom-up parsing is real parsing (top-down is equally valid; choice depends on grammar and application). Shift-reduce parsers are always faster (table size and construction complexity are trade-offs).

## Explainer

Top-down parsers start at the root of the parse tree and predict which rules to apply as they read tokens. **Shift-reduce parsing** works in the opposite direction: it starts at the leaves (the input tokens) and works upward, combining tokens into larger grammatical structures until it arrives at the start symbol. If you have worked through parse tree derivations, you know that a rightmost derivation builds the tree by always expanding the rightmost nonterminal. A shift-reduce parser discovers that same derivation, but in reverse — it reads the input left-to-right and reconstructs the rightmost derivation from bottom to top.

The algorithm uses two operations and a stack. **Shift** pushes the next input token onto the stack. **Reduce** recognizes that the top several symbols on the stack match the right-hand side of a grammar rule and replaces them with the left-hand nonterminal. For example, given the grammar rule `Factor → number`, if the stack top is the token `5`, a reduce pops `5` and pushes `Factor`. Consider parsing `3 + 5 * 2` with standard arithmetic grammar. The parser shifts `3`, reduces it to `Factor`, then to `Term`, then to `Expr`. It shifts `+`, shifts `5`, reduces to `Factor`, then to `Term`. It shifts `*`, shifts `2`, reduces to `Factor`. Now the stack top has `Term * Factor`, which reduces to `Term` — and critically, `*` was reduced before `+` because the parser waited, accumulating more context before committing. This is the power of bottom-up parsing: it defers decisions until enough information is available.

The central challenge is the **shift-reduce conflict**: should the parser shift the next token or reduce what is already on the stack? And occasionally, a **reduce-reduce conflict**: two different rules could match the stack top. Resolving these conflicts is what distinguishes the various LR parsing algorithms (LR(0), SLR, LALR, canonical LR). Each uses increasingly sophisticated lookahead and state information to make the right choice. The parser's decisions are encoded in a **parsing table** with two parts: an ACTION table (shift or reduce, given state and lookahead) and a GOTO table (which state to enter after a reduction).

Bottom-up parsing handles a strictly larger class of grammars than top-down LL parsing. Left recursion, which breaks LL parsers, is perfectly natural in shift-reduce parsing — `Expr → Expr + Term` works fine because the parser simply accumulates tokens until it sees enough to reduce. This is why most parser generators (yacc, Bison) produce bottom-up parsers. The trade-off is conceptual complexity: the parsing tables can be large, and understanding why a particular conflict occurs requires tracing through automaton states. But the result is a parser that makes no predictions and no backtracking — every shift and reduce is determined by the current state and lookahead, giving deterministic, linear-time parsing for a wide class of practical grammars.
