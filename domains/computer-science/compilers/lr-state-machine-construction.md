---
id: lr-state-machine-construction
title: LR State Machine and Table Construction
domain: computer-science
course: compilers
prerequisites:
- id: lr-parsing
  type: hard
- id: deterministic-finite-automata
  type: soft
builds-toward:
- parser-generators
tags:
- lr-parsing
- table-construction
- state-machines
stage: advanced
status: draft
---

# LR State Machine and Table Construction

## Core Idea
LR state machines are constructed via the canonical collection of LR(0) items. An item is a production with a dot indicating the parser's position. States are sets of items; transitions correspond to grammar symbols. GOTO/ACTION tables encode the state machine for table-driven parsing: GOTO[state, nonterminal] and ACTION[state, lookahead] determine the next move.

## Explainer

From your study of LR parsing, you know the parser uses a stack of states and makes shift or reduce decisions based on the current state and the next input token. But where do those states and decisions come from? The answer is a systematic construction that turns a context-free grammar into a finite automaton whose states track every possible position the parser could be in mid-parse.

The building block is the **LR(0) item**, which is simply a grammar production with a dot (·) inserted to mark how much of that production has been recognized so far. For the production `E → E + T`, the item `E → E · + T` means the parser has seen something matching `E` and is expecting a `+` next. A **state** in the LR automaton is a set of such items, representing all the productions the parser might currently be in the middle of. The initial state contains the item for the augmented start production (e.g., `S' → · S`) plus its **closure** — every item you get by expanding the nonterminal immediately after the dot. If the dot precedes a nonterminal `A`, you add all items `A → · α` for every production of `A`, then repeat until no new items appear.

**Transitions** between states correspond to grammar symbols. Given a state and a symbol `X` (terminal or nonterminal), the GOTO function collects every item where the dot precedes `X`, advances the dot past `X`, and computes the closure of the result — that is the next state. You build the entire automaton by starting from the initial state, computing GOTO for every symbol, and repeating for each new state discovered. This process always terminates because the number of distinct item sets is finite.

Once the automaton is complete, you read off the **ACTION** and **GOTO parse tables** directly. For a state containing item `A → α · a β` (dot before terminal `a`), the ACTION entry for that state and terminal `a` is "shift to the state GOTO gives for `a`." For a state containing a **complete item** `A → α ·` (dot at the end), the action is "reduce by production `A → α`." For the augmented production's complete item `S' → S ·`, the action is "accept." The GOTO table simply records the state transitions on nonterminals, used after a reduction replaces the right-hand side with a nonterminal on the stack. If any table cell gets two conflicting entries — two reductions, or a shift and a reduce — the grammar has a **conflict** and is not LR(0). Extending to SLR(1), LALR(1), or canonical LR(1) refines which lookaheads trigger reductions, resolving many such conflicts without changing the fundamental construction process.
