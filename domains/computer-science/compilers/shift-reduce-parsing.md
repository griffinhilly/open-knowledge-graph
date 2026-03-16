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
status: draft
---

# Shift-Reduce Parsing Mechanics

## Core Idea
Shift-reduce parsing uses two operations on a stack: shift (push the next input token) and reduce (pop a production's right-hand side and push the left-hand side). The parser decides on each step whether to shift or reduce using a state machine and lookahead. Shift-reduce conflicts are resolved by precedence rules or grammar restrictions.

## Explainer

From your study of LR parsing theory, you know that bottom-up parsers build the parse tree from the leaves up to the root, recognizing the right-hand sides of grammar productions in the input and replacing them with their left-hand side nonterminals. Shift-reduce parsing is the concrete mechanism that makes this happen, and it relies on the stack data structure you already understand to keep track of partially recognized productions.

The parser maintains two structures: a **stack** (initially empty) and an **input buffer** (containing the token stream followed by an end marker). At each step, exactly one of two actions occurs. A **shift** takes the next token from the input and pushes it onto the stack. A **reduce** recognizes that the top several symbols on the stack match the right-hand side of some grammar production, pops them off, and pushes the left-hand side nonterminal in their place. For example, if the grammar has the production `E → E + T` and the top of the stack contains `E`, `+`, `T` (with `T` on top), a reduce pops all three and pushes `E`. Parsing succeeds when the input is exhausted and the stack contains only the start symbol.

The hard question is: how does the parser know whether to shift or reduce at each step? This is where the LR state machine comes in. The parser doesn't just track symbols on the stack — it tracks **states** alongside them. Each state encodes how much of each possible production has been seen so far. The parser consults an **action table** indexed by the current state and the next input token (the **lookahead**). The table entry says either "shift and go to state X," "reduce by production Y," "accept," or "error." This table is precomputed from the grammar and encodes all the information the parser needs to make deterministic decisions.

A **shift-reduce conflict** arises when the table construction finds that a particular state-and-lookahead combination could legitimately be either a shift or a reduce. The classic example is the dangling-else problem: after parsing `if E then if E then S`, should the parser shift the incoming `else` (attaching it to the inner `if`) or reduce the inner `if-then` statement (leaving the `else` for the outer `if`)? These conflicts can be resolved by grammar rewriting, by operator precedence declarations that tell the parser generator which choice to make, or by choosing a default (most tools default to shift, which matches the conventional "else binds to nearest if" rule). Understanding when and why these conflicts arise is central to writing grammars that LR parser generators can handle cleanly.
