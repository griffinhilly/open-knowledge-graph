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
status: validated
---

# LR Parsing Fundamentals

## Core Idea
LR parsing is bottom-up, deterministic parsing that constructs a parse tree by reducing input tokens to the start symbol. An LR parser maintains a stack of states and a lookahead token; each state encodes all possible actions (shift or reduce). LR parsers handle a much larger grammar class than LL, including left-recursive grammars, making them suitable for real programming languages.

## Questions

```yaml
- question: "A grammar includes the rule: Expr → Expr + Term. A recursive descent (LL) parser encounters this rule and fails to parse. An LR parser handles it correctly. Why?"
  type: multiple-choice
  options:
    - "Recursive descent parsers cannot handle the + operator; LR parsers have built-in support for arithmetic"
    - "Recursive descent parsers guess the rule before reading input, so Expr → Expr + Term causes infinite recursion trying to expand Expr; LR parsers work bottom-up and have already parsed the left operand before deciding about the rule"
    - "LR parsers use a larger lookahead window than recursive descent parsers, which is why they resolve left recursion"
    - "Recursive descent parsers use a stack, which cannot represent left-recursive derivations"
  answer: 1
  explanation: "Left recursion is fatal for top-down parsers. When a recursive descent parser tries to parse Expr, it checks if this context matches Expr → Expr + Term — which immediately requires parsing another Expr, causing infinite recursion before reading any input. LR parsers avoid this because they are bottom-up: they shift tokens onto the stack, accumulating evidence, and reduce only when the right-hand side of a rule is fully assembled on top of the stack. By the time the parser recognizes Expr → Expr + Term, it has already parsed and reduced the left Expr — no recursion involved. This is the primary reason real language parser generators like yacc and bison produce LR parsers rather than LL parsers."

- question: "During LR parsing of an expression, the parser has the state stack [..., Expr, +] and the next input token is a number. What does the parser do?"
  type: multiple-choice
  options:
    - "Reduce immediately — Expr + is enough to recognize a pattern"
    - "Shift the number token onto the stack, because more input is needed before a reduction is possible"
    - "Report an error — a number cannot follow the + operator in this grammar"
    - "Reduce Expr + to a partial expression using a default rule"
  answer: 1
  explanation: "LR parsing is driven entirely by the parsing table, which encodes the correct action for each (state, lookahead) pair. With Expr and + on the stack and a number as lookahead, the parser has not yet assembled enough to complete a rule — it still needs to parse the right operand. The table will specify 'shift': push the number token and transition to a new state. Once enough tokens are shifted and the right-hand side of a rule appears on top of the stack, the table will specify 'reduce.' The shift/reduce decision is never guessed — it is determined deterministically by the precomputed table, which is why LR parsing is called deterministic."

- question: "LR parsers, like recursive descent parsers, predict which grammar rule to apply by examining the next token before any input has been consumed."
  type: true-false
  answer: false
  explanation: "False. This describes top-down parsing (LL), not LR. Recursive descent parsers try to predict which production to expand based on the current lookahead token, before reading the right-hand side. LR parsers are bottom-up: they read tokens left to right, shifting them onto a stack and waiting until the stack contains a complete right-hand side of some grammar rule — then reducing. LR parsers never predict; they accumulate evidence and recognize patterns after the fact. This fundamental difference is what allows LR parsers to handle left recursion and a larger class of grammars."

- question: "LR parsers can handle left-recursive grammar rules (like Expr → Expr + Term) without requiring any rewriting of the grammar."
  type: true-false
  answer: true
  explanation: "True. Left recursion is a natural and convenient way to express left-associative operators (a + b + c groups as (a + b) + c), and LR parsers handle it directly because their bottom-up approach has already reduced the left Expr before encountering the recursive rule. Top-down (LL) parsers require the grammar to be rewritten to eliminate left recursion, often at the cost of obscuring the intended associativity and precedence. This is a major reason why parser generators for real programming languages (yacc, bison, LALR tools) produce LR parsers."

- question: "What does 'bottom-up' mean in the context of LR parsing, and why does this allow LR parsers to handle left-recursive grammars that top-down parsers cannot?"
  type: short-answer
  answer: "Bottom-up parsing means building the parse tree from the leaves (input tokens) up toward the root (the start symbol). An LR parser reads tokens left to right, shifting each token onto a stack. When the top of the stack matches the right-hand side of a grammar rule, the parser reduces — popping those elements and pushing the left-hand side nonterminal. Because the left operand is shifted and reduced before the parser ever needs to decide about a left-recursive rule (like Expr → Expr + Term), there is no infinite regress. A top-down parser works the opposite direction — it starts from the start symbol and tries to derive input tokens — so it must expand Expr immediately when it encounters Expr → Expr + Term, causing infinite recursion before any input is consumed."
  explanation: "The stack is used in both approaches, but to do opposite things: a top-down parser uses the stack to track pending expansions (rules to apply to future input), while an LR parser uses the stack to accumulate already-consumed tokens and partial reductions. This reversal of direction is what enables LR parsers to handle the full class of deterministic context-free languages."
```

## Explainer

If you understand the parsing problem — turning a flat sequence of tokens into a structured tree — then LR parsing is the most powerful deterministic approach to solving it. Where top-down parsers (like recursive descent) try to guess which grammar rule to apply by looking at the first few tokens, **LR parsing** works bottom-up: it reads tokens left to right, accumulates them, and waits until it has enough evidence to recognize which rule produced them. The name "LR" stands for Left-to-right scan, Rightmost derivation — it builds the parse tree from the leaves up to the root.

The core mechanism relies on the stack data structure you already know. An LR parser maintains a **stack of states**, where each state represents a set of partially-recognized grammar rules. At each step, the parser consults a **parsing table** indexed by the current state and the next input token (the lookahead). The table tells it to do one of two things: **shift** (push the current token and a new state onto the stack, then advance to the next token) or **reduce** (pop several items off the stack that match the right-hand side of a grammar rule, and push the left-hand side nonterminal back on). Think of it like assembling a puzzle from individual pieces — you keep picking up pieces (shifting) until you notice a group that forms a recognizable sub-picture (reducing).

Consider parsing the expression `3 + 4 * 5`. The parser shifts `3`, reduces it to an Expression, shifts `+`, shifts `4`, reduces to Expression, shifts `*`, shifts `5`, reduces to Expression. Now it sees `Expression * Expression` on the stack and reduces that to Expression (because `*` binds tighter). Then it sees `Expression + Expression` and reduces that. The parsing table encodes operator precedence and associativity — the parser never has to guess, because the table was precomputed from the grammar to resolve every possible ambiguity deterministically.

The power of LR parsing comes from what it can handle. Top-down parsers choke on **left-recursive grammars** (rules like `Expr → Expr + Term`), which naturally describe left-associative operators. LR parsers handle left recursion effortlessly because they build from the bottom up — they've already parsed the left operand before they need to decide about the rule. This is why parser generators like yacc and bison produce LR parsers: real programming language grammars are full of left recursion and operator precedence rules that would require awkward rewriting for a top-down parser. The tradeoff is that LR parsing tables can be large and the algorithm is harder to implement by hand, which is exactly why we use parser generators to build them automatically.
