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

## Questions

```yaml
- question: "A grammar contains the rule: Expr → Expr + Term | Term. When a recursive descent parser attempts to apply this rule, what happens?"
  type: multiple-choice
  options:
    - "The parser generates an ambiguity warning and falls back to the second alternative"
    - "The parser correctly handles it by checking if the next token is '+' before recursing"
    - "The parser enters an infinite loop because it calls the Expr function without consuming any input"
    - "The parser fails immediately with a syntax error because '+' is not in the FIRST set of Expr"
  answer: 2
  explanation: "Left recursion is fatal for recursive descent (and all LL) parsers. The Expr function immediately calls Expr again before consuming any token — an infinite loop that never terminates. This happens because LL parsers build the parse tree top-down from the root: to parse Expr, they immediately try to parse Expr as the first child, which tries to parse Expr again, with no progress on the input. The fix is to rewrite the grammar: Expr → Term Expr', Expr' → + Term Expr' | ε. This eliminates left recursion by making the '+' consumption explicit, but it changes the parse tree shape compared to the original left-associative structure."

- question: "When does an LL(1) parser fail to determine which production to apply for a given nonterminal?"
  type: multiple-choice
  options:
    - "Whenever the nonterminal has more than two alternative productions"
    - "When two or more alternative productions have overlapping FIRST sets — the same token could begin multiple alternatives"
    - "When the lookahead token does not appear in the grammar at all"
    - "Whenever the grammar contains epsilon (empty) productions"
  answer: 1
  explanation: "An LL(1) parser uses a single lookahead token to select among alternative productions. This works only when the FIRST sets of all alternatives for a nonterminal are disjoint — each possible next token uniquely identifies which rule to apply. If two alternatives can both start with the same token, the parser cannot deterministically choose, and the grammar is not LL(1). The number of alternatives (option A) is irrelevant as long as their FIRST sets don't overlap. Epsilon productions (option D) do complicate things via FOLLOW sets, but they don't by themselves make a grammar non-LL(1)."

- question: "In a recursive descent parser, the call stack implicitly serves as the parsing stack, with each grammar nonterminal implemented as a function."
  type: true-false
  answer: true
  explanation: "This is the key insight that makes recursive descent elegant. Each nonterminal becomes a function: the function for Statement might call the function for Expression, which calls the function for Term, and so on. The program's call stack tracks the nesting of these function calls, exactly mirroring the depth of the parse tree being built. When a function returns, it 'pops' a node from the implicit stack. A table-driven LL parser does the same thing but uses an explicit stack data structure and a parsing table, making the process less natural to write by hand but easier to generate automatically."

- question: "An LL(2) parser can handle left-recursive grammars that LL(1) cannot, because it can 'look ahead' past the recursive call to see how the rule eventually terminates."
  type: true-false
  answer: false
  explanation: "No amount of additional lookahead fixes left recursion in an LL parser. Left recursion causes an infinite loop not because the parser lacks information about what comes later, but because parsing the nonterminal immediately requires parsing the same nonterminal again — an infinite descent that never consumes a token. Even LL(k) for arbitrarily large k cannot resolve this structural problem. The only solution is to rewrite the grammar to eliminate left recursion. LL(2) is strictly more powerful than LL(1) for grammars that are non-left-recursive but have overlapping FIRST sets resolvable with two tokens of lookahead — but left recursion is a different kind of problem entirely."

- question: "Why must LL grammars be free of left recursion, and what does the standard transformation to eliminate it cost you?"
  type: short-answer
  answer: "Left recursion causes infinite loops in LL (top-down) parsers because the parser tries to expand a nonterminal by immediately invoking the same nonterminal again, without consuming any input. The standard fix rewrites `A → Aα | β` into `A → β A'` and `A' → α A' | ε`, replacing left recursion with right recursion. The cost is that the resulting parse tree has a different shape: the left-recursive grammar naturally produced left-associative trees (correctly grouping `a + b + c` as `(a + b) + c`), while the right-recursive rewrite produces right-leaning trees. Semantic actions (code generation steps) attached to the grammar must be adjusted to recover the intended associativity."
  explanation: "This is a real practical cost: parser engineers often prefer LR parsing (bottom-up) for expression-heavy languages precisely because LR parsers handle left recursion naturally and preserve the intended tree structure. LL parsing's simplicity comes at the price of requiring grammar transformations that can obscure the original language's structure."
```

## Explainer

You already know from the parsing problem overview that a parser's job is to take a flat sequence of tokens and recover the tree structure implied by a grammar. **LL parsing** is the most intuitive approach: it reads the input **L**eft-to-right and constructs a **L**eftmost derivation, building the parse tree from the root down toward the leaves. Think of it as making predictions — you look at the next token and decide which grammar rule to expand, then commit to that choice and move forward.

The "k" in LL(k) tells you how many tokens ahead the parser peeks before making its prediction. In practice, **LL(1)** — one token of lookahead — is the workhorse. Consider parsing an if-statement: when the parser sees the token `if`, it knows immediately to apply the if-statement production rule. No other rule could start with `if`. This works because LL(1) grammars are designed so that for every nonterminal, the possible productions have disjoint **FIRST sets** — the set of tokens that can begin each alternative. When FIRST sets overlap, the parser cannot decide which rule to apply with a single token, and the grammar is not LL(1).

There are two common implementation strategies, both of which use the stack data structure you already know. A **recursive descent parser** turns each grammar nonterminal into a function. The function for `Expression` calls the function for `Term`, which calls the function for `Factor`, and so on — the call stack itself acts as the parsing stack. Alternatively, a **table-driven parser** uses an explicit stack and a parsing table indexed by (current nonterminal, lookahead token). Each table entry tells the parser which production to apply. Both approaches are equivalent in power; recursive descent is easier to write by hand, while table-driven parsers are easier to generate automatically.

The main limitation of LL parsing is that the grammar must be **non-left-recursive**. A rule like `Expr → Expr + Term` sends a recursive descent parser into an infinite loop — it keeps calling the `Expr` function without consuming any input. The standard fix is **left-factoring** and rewriting left recursion into right recursion (e.g., `Expr → Term Expr'`, `Expr' → + Term Expr' | ε`). This transformation preserves the language but changes the parse tree shape, which matters when you later attach semantic actions. Despite these restrictions, LL parsing remains widely used because it is simple to implement, produces clear error messages (you always know what the parser expected), and maps naturally to hand-written parsers for languages designed with top-down parsing in mind.
