---
id: operator-precedence-parsing
title: Operator Precedence Parsing
domain: computer-science
course: compilers
prerequisites:
- id: context-free-grammars
  type: hard
- id: parsing-problem-overview
  type: hard
builds-toward:
- grammar-ambiguity-resolution
tags:
- parsing
- operators
- grammars
stage: advanced
status: draft
---

# Operator Precedence Parsing

## Core Idea
Operator precedence parsing handles expressions by assigning precedence levels to operators and parsing operands recursively at appropriate precedence levels. This eliminates special grammar rules and allows direct parsing of flat operator sequences. Widely used in expression evaluators and scripting languages.

## How It's Best Learned
Implement a simple arithmetic expression parser using precedence climbing, then verify it handles mixed operators (+, *, ^) correctly with proper evaluation order.

## Common Misconceptions
Precedence and associativity are the same thing—they're separate. Right-associativity requires different handling than left-associativity in recursive descent.

## Explainer

When you learned about context-free grammars, you saw how to encode arithmetic expressions using multiple nonterminals — one for each precedence level. A grammar for `+` and `*` might have `Expr → Expr + Term`, `Term → Term * Factor`, `Factor → number | ( Expr )`. This works, but it is verbose: every new operator means another nonterminal and another level of recursion. **Operator precedence parsing** collapses all of that into a single algorithm driven by a table of precedence levels and associativity rules.

The core insight is that an expression like `3 + 4 * 5 + 2` is really a flat sequence of operands and operators, and all you need to decide is where to place the implicit parentheses. The **precedence climbing** (or Pratt parsing) algorithm handles this elegantly. It parses an operand, then enters a loop: as long as the next operator has precedence at or above a threshold (the "minimum precedence"), it consumes the operator and recursively parses the right-hand operand at a higher minimum precedence. For left-associative operators, the recursive call uses `precedence + 1` as its minimum; for right-associative operators, it uses `precedence` unchanged. This one difference in the recursive call is all that separates `2 ^ 3 ^ 4` being parsed as `2 ^ (3 ^ 4)` versus `(2 ^ 3) ^ 4`.

Consider parsing `3 + 4 * 5`. The algorithm reads `3`, then sees `+` with precedence 1 (meeting the initial threshold of 0). It consumes `+`, then recursively parses the right side at minimum precedence 2. Inside that recursive call, it reads `4`, sees `*` with precedence 2 (meeting the threshold), consumes `*`, and parses `5`. Now it checks again — there are no more operators, so it returns `4 * 5`. Back in the outer call, the result is `3 + (4 * 5)`. The precedence threshold naturally caused `*` to bind tighter than `+` without any grammar rewriting.

This technique is remarkably practical. Most hand-written parsers for real programming languages — including early versions of GCC and many scripting language interpreters — use some form of operator precedence parsing for expressions. Adding a new operator is trivial: assign it a precedence level and associativity, and the algorithm handles it automatically. The trade-off is that this approach only works for binary infix operators (plus unary prefix operators with a small extension). Constructs like ternary operators, array indexing, or function calls require special handling outside the precedence loop. But for the expression subset of a language, precedence parsing is hard to beat in simplicity and extensibility.
