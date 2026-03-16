---
id: ll-parsing
title: LL Parsing and Predictive Parsing
domain: computer-science
course: compilers
prerequisites:
- id: parsing-problem-overview
  type: hard
- id: stacks-data-structure
  type: hard
builds-toward:
- parser-generators
tags:
- top-down-parsing
- recursive-descent
- predictive-parsing
stage: advanced
status: draft
---

# LL Parsing and Predictive Parsing

## Core Idea
LL(k) parsing is top-down, deterministic parsing using k lookahead tokens. An LL(1) parser uses a single lookahead token to predict which production rule to apply. It can be implemented as a recursive descent parser (function per nonterminal) or via a table-driven parser. LL grammars must be non-left-recursive and free of ambiguity, limiting expressiveness but enabling simple implementation.

## Explainer

You already know from the parsing problem overview that a parser's job is to take a flat sequence of tokens and recover the tree structure implied by a grammar. **LL parsing** is the most intuitive approach: it reads the input **L**eft-to-right and constructs a **L**eftmost derivation, building the parse tree from the root down toward the leaves. Think of it as making predictions — you look at the next token and decide which grammar rule to expand, then commit to that choice and move forward.

The "k" in LL(k) tells you how many tokens ahead the parser peeks before making its prediction. In practice, **LL(1)** — one token of lookahead — is the workhorse. Consider parsing an if-statement: when the parser sees the token `if`, it knows immediately to apply the if-statement production rule. No other rule could start with `if`. This works because LL(1) grammars are designed so that for every nonterminal, the possible productions have disjoint **FIRST sets** — the set of tokens that can begin each alternative. When FIRST sets overlap, the parser cannot decide which rule to apply with a single token, and the grammar is not LL(1).

There are two common implementation strategies, both of which use the stack data structure you already know. A **recursive descent parser** turns each grammar nonterminal into a function. The function for `Expression` calls the function for `Term`, which calls the function for `Factor`, and so on — the call stack itself acts as the parsing stack. Alternatively, a **table-driven parser** uses an explicit stack and a parsing table indexed by (current nonterminal, lookahead token). Each table entry tells the parser which production to apply. Both approaches are equivalent in power; recursive descent is easier to write by hand, while table-driven parsers are easier to generate automatically.

The main limitation of LL parsing is that the grammar must be **non-left-recursive**. A rule like `Expr → Expr + Term` sends a recursive descent parser into an infinite loop — it keeps calling the `Expr` function without consuming any input. The standard fix is **left-factoring** and rewriting left recursion into right recursion (e.g., `Expr → Term Expr'`, `Expr' → + Term Expr' | ε`). This transformation preserves the language but changes the parse tree shape, which matters when you later attach semantic actions. Despite these restrictions, LL parsing remains widely used because it is simple to implement, produces clear error messages (you always know what the parser expected), and maps naturally to hand-written parsers for languages designed with top-down parsing in mind.
