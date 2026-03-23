---
id: shift-reduce-parsing
title: Shift-Reduce Parsing Mechanics
domain: computer-science
course: compilers
prerequisites:
- id: lr-parsing
  type: hard
- id: stacks-data-structure
  type: hard
builds-toward:
- lr-state-machine-construction
tags:
- parsing-algorithm
- stack-operations
stage: advanced
status: validated
---

# Shift-Reduce Parsing Mechanics

## Core Idea
Shift-reduce parsing uses two operations on a stack: shift (push the next input token) and reduce (pop a production's right-hand side and push the left-hand side). The parser decides on each step whether to shift or reduce using a state machine and lookahead. Shift-reduce conflicts are resolved by precedence rules or grammar restrictions.

## Questions

```yaml
- question: "A shift-reduce parser has 'E + T' on top of its stack with '*' as the next input token. The grammar has the production E → E + T. A student says the parser should immediately reduce because 'E + T' matches the right-hand side. What actually determines whether to shift or reduce?"
  type: multiple-choice
  options:
    - "The length of the string currently on the stack."
    - "The action table entry for the current parser state and the lookahead token '*'."
    - "Whether the next token '*' is an operator."
    - "The depth of the parse tree constructed so far."
  answer: 1
  explanation: "The shift/reduce decision is made by consulting the precomputed action table, indexed by the current parser state and the lookahead token — not by directly inspecting what is on the stack. In this case, if '*' has higher precedence than '+', the table will encode a shift action, deferring the reduction until '*' and its right operand are handled. The table encodes all such precedence and associativity information at parse-table construction time."

- question: "What critical information is encoded in the LR parser state that makes it possible to decide between shifting and reducing without inspecting the entire stack?"
  type: multiple-choice
  options:
    - "The total number of tokens consumed from the input so far."
    - "How far along the parser is in recognizing each possible production right-hand side — its 'item set' representing partial progress on all active productions."
    - "The identity of every grammar nonterminal seen since parsing began."
    - "The depth of the most recently completed reduction."
  answer: 1
  explanation: "Each LR state is an 'item set' summarizing which grammar productions are currently active and how much of each right-hand side has been seen. This compact state representation lets the parser make correct shift/reduce decisions without re-examining the entire stack history. The action table maps (state, lookahead) pairs to actions, encoding this knowledge up front."

- question: "In a shift-reduce parser, the stack tracks both grammar symbols and parser states alongside them simultaneously."
  type: true-false
  answer: true
  explanation: "The LR stack is not just a symbol stack — each entry is a (symbol, state) pair. The state is pushed and popped together with its corresponding symbol, allowing the parser to know at every step what configuration of partial productions it is in the middle of. This is what enables the action table lookup to work correctly."

- question: "A shift-reduce conflict means the grammar is inherently ambiguous and cannot be parsed deterministically by any bottom-up method."
  type: true-false
  answer: false
  explanation: "A shift-reduce conflict means the parser construction found a state where both a shift and a reduce are valid actions for a given lookahead. This can arise even in unambiguous grammars (like the dangling-else case). It can often be resolved by operator precedence declarations, associativity rules, or grammar rewriting — without changing the language being parsed. Most tools default to 'shift' when a conflict is unresolved, which correctly handles the dangling-else by binding 'else' to the nearest 'if'."

- question: "In the dangling-else problem, what shift-reduce conflict arises and how does the conventional resolution — defaulting to shift — enforce the expected semantic behavior?"
  type: short-answer
  answer: "After parsing 'if E then if E then S', the parser can either shift an incoming 'else' (attaching it to the inner if) or reduce the inner 'if-then' statement (leaving the 'else' for the outer if). Both are grammatically valid. Defaulting to shift means the 'else' is attached to the nearest preceding unmatched 'if', which matches the conventional 'else binds to nearest if' rule expected by programmers."
  explanation: "The default-to-shift resolution is not arbitrary — it aligns with the semantic convention of most programming languages. Without it, the grammar would require rewriting into separate 'matched' and 'unmatched' statement categories to eliminate the conflict syntactically."
```

## Explainer

From your study of LR parsing theory, you know that bottom-up parsers build the parse tree from the leaves up to the root, recognizing the right-hand sides of grammar productions in the input and replacing them with their left-hand side nonterminals. Shift-reduce parsing is the concrete mechanism that makes this happen, and it relies on the stack data structure you already understand to keep track of partially recognized productions.

The parser maintains two structures: a **stack** (initially empty) and an **input buffer** (containing the token stream followed by an end marker). At each step, exactly one of two actions occurs. A **shift** takes the next token from the input and pushes it onto the stack. A **reduce** recognizes that the top several symbols on the stack match the right-hand side of some grammar production, pops them off, and pushes the left-hand side nonterminal in their place. For example, if the grammar has the production `E → E + T` and the top of the stack contains `E`, `+`, `T` (with `T` on top), a reduce pops all three and pushes `E`. Parsing succeeds when the input is exhausted and the stack contains only the start symbol.

The hard question is: how does the parser know whether to shift or reduce at each step? This is where the LR state machine comes in. The parser doesn't just track symbols on the stack — it tracks **states** alongside them. Each state encodes how much of each possible production has been seen so far. The parser consults an **action table** indexed by the current state and the next input token (the **lookahead**). The table entry says either "shift and go to state X," "reduce by production Y," "accept," or "error." This table is precomputed from the grammar and encodes all the information the parser needs to make deterministic decisions.

A **shift-reduce conflict** arises when the table construction finds that a particular state-and-lookahead combination could legitimately be either a shift or a reduce. The classic example is the dangling-else problem: after parsing `if E then if E then S`, should the parser shift the incoming `else` (attaching it to the inner `if`) or reduce the inner `if-then` statement (leaving the `else` for the outer `if`)? These conflicts can be resolved by grammar rewriting, by operator precedence declarations that tell the parser generator which choice to make, or by choosing a default (most tools default to shift, which matches the conventional "else binds to nearest if" rule). Understanding when and why these conflicts arise is central to writing grammars that LR parser generators can handle cleanly.
