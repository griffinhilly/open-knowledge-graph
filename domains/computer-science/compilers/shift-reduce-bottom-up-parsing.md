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
status: validated
---

# Shift-Reduce Bottom-Up Parsing

## Core Idea
Bottom-up shift-reduce parsers build parse trees from leaves up, using a stack to accumulate symbols and reduce them when grammar rules match. This approach is more powerful than top-down parsing and handles a wider class of unambiguous grammars.

## How It's Best Learned
Manually build shift-reduce parse trees for example inputs. Implement a simple shift-reduce parser with an explicit stack.

## Common Misconceptions
Only bottom-up parsing is real parsing (top-down is equally valid; choice depends on grammar and application). Shift-reduce parsers are always faster (table size and construction complexity are trade-offs).

## Questions

```yaml
- question: "A grammar rule is left-recursive: Expr → Expr + Term. Which parser type handles this correctly, and why?"
  type: multiple-choice
  options:
    - "Top-down (LL) parsers, because they predict rules before consuming input"
    - "Both equally well, since left recursion is handled by all modern parsers"
    - "Bottom-up (LR/shift-reduce) parsers, because they accumulate tokens and defer reduction decisions"
    - "Neither; left-recursive grammars must always be refactored before parsing"
  answer: 2
  explanation: "Left recursion causes LL (top-down) parsers to loop infinitely: when trying to match Expr, the parser predicts Expr → Expr + Term, which immediately requires matching another Expr, ad infinitum. Shift-reduce parsers handle this naturally because they never predict — they simply shift tokens onto the stack and reduce only when the top of the stack matches a rule's right-hand side. When parsing '3 + 5', the parser shifts '3', reduces to Factor, then Term, then Expr. When it shifts '+' and '5' and reduces those, it has 'Expr + Term' on the stack, which matches the left-recursive rule and reduces to Expr. The deferral of decisions is what makes this work."

- question: "During shift-reduce parsing of the expression '3 * 5 + 2', the parser has Expr on the stack and '+' as the next token. What should it do?"
  type: multiple-choice
  options:
    - "Immediately reduce Expr to a higher-level nonterminal"
    - "Shift '+' onto the stack, because reducing now would discard context needed for precedence"
    - "Report a shift-reduce conflict and halt"
    - "Backtrack to try a different reduction sequence"
  answer: 1
  explanation: "This is a shift-reduce conflict: the parser must decide whether to reduce what's on the stack or shift the next token. Resolving it correctly requires knowing operator precedence. In a properly constructed parsing table for standard arithmetic grammar, '+' has lower precedence than '*', so after computing '3 * 5' = a Term, the parser shifts '+' rather than prematurely reducing — it needs to accumulate the right-hand side of the '+' operator. The correct answer demonstrates that shift-reduce parsers use lookahead and state information (not guessing or backtracking) to resolve conflicts deterministically."

- question: "Shift-reduce parsers discover the rightmost derivation of an input, but in reverse order."
  type: true-false
  answer: true
  explanation: "A rightmost derivation expands the rightmost nonterminal at each step, building the parse tree top-down. A shift-reduce parser processes input left-to-right and performs reductions that correspond to the last step of a rightmost derivation first (i.e., the deepest leaves get reduced first). At any point in parsing, the stack contains a prefix of a right-sentential form — a state that could appear in the middle of a rightmost derivation. Reductions peel away the last applied rule, effectively running the derivation backward from the leaves to the root."

- question: "A shift-reduce parser can backtrack when it makes a wrong shift or reduce decision."
  type: true-false
  answer: false
  explanation: "Shift-reduce parsers as implemented by LR parsing algorithms are deterministic — they make exactly one decision (shift or reduce) at each step based on the current parser state and a fixed lookahead token, with no backtracking. The parsing tables (ACTION and GOTO) are constructed to resolve conflicts in advance so that every state/lookahead combination has a unique action. If the grammar has genuine ambiguities that cannot be resolved, the parser reports a conflict at table construction time, not at parse time. This determinism is what gives LR parsing its linear O(n) time complexity."

- question: "Explain why bottom-up (shift-reduce) parsing is described as 'more powerful' than top-down (LL) parsing."
  type: short-answer
  answer: "Bottom-up parsers handle a strictly larger class of grammars because they defer reduction decisions until sufficient context has accumulated on the stack. They naturally handle left-recursive rules (which break LL parsers) and ambiguities in operator associativity and precedence. LL parsers must predict which production to apply based only on the current input token and a small lookahead, which forces grammar transformations (elimination of left recursion, left factoring) that aren't always natural. LR parsers can also use more right-context before committing to a reduction."
  explanation: "The power difference comes from when decisions are made. An LL(k) parser must commit to an expansion by looking at k tokens ahead from the current position. An LR(k) parser can look at k tokens of lookahead *after* accumulating an entire handle on the stack — giving it the full left context (the stack) plus some right context (lookahead). This means LR parsing can distinguish situations that look identical to a top-down parser. In practice, most programming language grammars are LALR(1) — parseable by bottom-up parsers with just 1 token of lookahead — while many require grammar surgery to fit LL(1) constraints."
```

## Explainer

Top-down parsers start at the root of the parse tree and predict which rules to apply as they read tokens. **Shift-reduce parsing** works in the opposite direction: it starts at the leaves (the input tokens) and works upward, combining tokens into larger grammatical structures until it arrives at the start symbol. If you have worked through parse tree derivations, you know that a rightmost derivation builds the tree by always expanding the rightmost nonterminal. A shift-reduce parser discovers that same derivation, but in reverse — it reads the input left-to-right and reconstructs the rightmost derivation from bottom to top.

The algorithm uses two operations and a stack. **Shift** pushes the next input token onto the stack. **Reduce** recognizes that the top several symbols on the stack match the right-hand side of a grammar rule and replaces them with the left-hand nonterminal. For example, given the grammar rule `Factor → number`, if the stack top is the token `5`, a reduce pops `5` and pushes `Factor`. Consider parsing `3 + 5 * 2` with standard arithmetic grammar. The parser shifts `3`, reduces it to `Factor`, then to `Term`, then to `Expr`. It shifts `+`, shifts `5`, reduces to `Factor`, then to `Term`. It shifts `*`, shifts `2`, reduces to `Factor`. Now the stack top has `Term * Factor`, which reduces to `Term` — and critically, `*` was reduced before `+` because the parser waited, accumulating more context before committing. This is the power of bottom-up parsing: it defers decisions until enough information is available.

The central challenge is the **shift-reduce conflict**: should the parser shift the next token or reduce what is already on the stack? And occasionally, a **reduce-reduce conflict**: two different rules could match the stack top. Resolving these conflicts is what distinguishes the various LR parsing algorithms (LR(0), SLR, LALR, canonical LR). Each uses increasingly sophisticated lookahead and state information to make the right choice. The parser's decisions are encoded in a **parsing table** with two parts: an ACTION table (shift or reduce, given state and lookahead) and a GOTO table (which state to enter after a reduction).

Bottom-up parsing handles a strictly larger class of grammars than top-down LL parsing. Left recursion, which breaks LL parsers, is perfectly natural in shift-reduce parsing — `Expr → Expr + Term` works fine because the parser simply accumulates tokens until it sees enough to reduce. This is why most parser generators (yacc, Bison) produce bottom-up parsers. The trade-off is conceptual complexity: the parsing tables can be large, and understanding why a particular conflict occurs requires tracing through automaton states. But the result is a parser that makes no predictions and no backtracking — every shift and reduce is determined by the current state and lookahead, giving deterministic, linear-time parsing for a wide class of practical grammars.
