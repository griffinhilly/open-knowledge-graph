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
status: validated
---

# LR State Machine and Table Construction

## Core Idea
LR state machines are constructed via the canonical collection of LR(0) items. An item is a production with a dot indicating the parser's position. States are sets of items; transitions correspond to grammar symbols. GOTO/ACTION tables encode the state machine for table-driven parsing: GOTO[state, nonterminal] and ACTION[state, lookahead] determine the next move.

## Questions

```yaml
- question: "An LR parser is in a state containing the item 'E → E + · T'. What does this item tell you about the current parse situation?"
  type: multiple-choice
  options:
    - "The parser has finished recognizing E + T and is about to reduce"
    - "The parser has recognized E and +, and is currently expecting something that matches T"
    - "The parser must shift the next input token regardless of what it is"
    - "The parser has recognized E + T but must check lookahead before deciding"
  answer: 1
  explanation: "The dot in an LR(0) item marks how much of the right-hand side has been matched. 'E → E + · T' means the parser has consumed tokens matching 'E' and '+' from the stack, and is now looking for a T. This is a 'shift' configuration — not a reduction, because the dot is not at the end. The parser will shift or further expand to eventually match the T before reducing this production."

- question: "A parser state contains both the complete item 'A → α ·' and the item 'B → β · a γ' (dot before terminal a). What kind of conflict does this represent, and why is it a problem?"
  type: multiple-choice
  options:
    - "A reduce-reduce conflict: two reductions are possible at once"
    - "A shift-reduce conflict: on terminal a, the parser cannot tell whether to reduce A → α or shift a"
    - "A goto conflict: the GOTO table has two entries for the same nonterminal"
    - "No conflict: complete items always take priority over shift items"
  answer: 1
  explanation: "A complete item 'A → α ·' signals a reduce action. An item 'B → β · a γ' signals a shift action on terminal a. If the next input token is a, both actions are valid according to the item set — this is a shift-reduce conflict. The ACTION table cell for (this state, terminal a) would need two entries, which is undefined for LR(0). SLR, LALR, and canonical LR resolve conflicts by restricting which lookaheads trigger reductions."

- question: "The GOTO function in LR table construction applies to nonterminal symbols, while the ACTION table handles terminal symbols and the end-of-input marker."
  type: true-false
  answer: true
  explanation: "This division of labor is fundamental: after a reduction replaces a right-hand side with a nonterminal A on the stack, the parser uses GOTO[current state, A] to find the next state. The ACTION table governs what happens when the parser looks at the next input terminal — shift, reduce, accept, or error. Mixing these up leads to misreading the parse tables."

- question: "Computing the closure of an item set is optional — it can be skipped for efficiency if the grammar is unambiguous."
  type: true-false
  answer: false
  explanation: "Closure is mandatory, not optional. Without it, the state is incomplete: if the dot precedes a nonterminal A, the parser must also track all the productions of A that might begin here — otherwise it won't know what to do when tokens matching A's body arrive. Closure adds all items 'A → · α' for productions of the nonterminal after the dot, repeated until fixed point. Skipping closure produces an incorrect automaton that fails to recognize valid parses."

- question: "Why must closure be computed when constructing each new LR state during the automaton build? What would go wrong if you only kept the 'kernel' items (the ones that actually advance the dot across a symbol)?"
  type: short-answer
  answer: "Kernel items only track the specific position reached by the last symbol transition. But when the dot precedes a nonterminal, the parser might be at the beginning of any production for that nonterminal. Closure adds those 'prediction' items so the automaton knows to shift or expand for any valid start of the nonterminal. Without closure, the state machine would have no items for the interior of nonterminal expansions, causing the parser to fail on valid inputs that require recognizing a nonterminal's body from scratch."
  explanation: "The distinction between kernel items (those that advance the dot) and closure items (those predicting what could begin next) mirrors the Earley/CYK distinction between completion and prediction. LR construction merges both into a single item-set framework; closure is what makes the sets 'complete' in the sense that every possible next configuration is represented."
```

## Explainer

From your study of LR parsing, you know the parser uses a stack of states and makes shift or reduce decisions based on the current state and the next input token. But where do those states and decisions come from? The answer is a systematic construction that turns a context-free grammar into a finite automaton whose states track every possible position the parser could be in mid-parse.

The building block is the **LR(0) item**, which is simply a grammar production with a dot (·) inserted to mark how much of that production has been recognized so far. For the production `E → E + T`, the item `E → E · + T` means the parser has seen something matching `E` and is expecting a `+` next. A **state** in the LR automaton is a set of such items, representing all the productions the parser might currently be in the middle of. The initial state contains the item for the augmented start production (e.g., `S' → · S`) plus its **closure** — every item you get by expanding the nonterminal immediately after the dot. If the dot precedes a nonterminal `A`, you add all items `A → · α` for every production of `A`, then repeat until no new items appear.

**Transitions** between states correspond to grammar symbols. Given a state and a symbol `X` (terminal or nonterminal), the GOTO function collects every item where the dot precedes `X`, advances the dot past `X`, and computes the closure of the result — that is the next state. You build the entire automaton by starting from the initial state, computing GOTO for every symbol, and repeating for each new state discovered. This process always terminates because the number of distinct item sets is finite.

Once the automaton is complete, you read off the **ACTION** and **GOTO parse tables** directly. For a state containing item `A → α · a β` (dot before terminal `a`), the ACTION entry for that state and terminal `a` is "shift to the state GOTO gives for `a`." For a state containing a **complete item** `A → α ·` (dot at the end), the action is "reduce by production `A → α`." For the augmented production's complete item `S' → S ·`, the action is "accept." The GOTO table simply records the state transitions on nonterminals, used after a reduction replaces the right-hand side with a nonterminal on the stack. If any table cell gets two conflicting entries — two reductions, or a shift and a reduce — the grammar has a **conflict** and is not LR(0). Extending to SLR(1), LALR(1), or canonical LR(1) refines which lookaheads trigger reductions, resolving many such conflicts without changing the fundamental construction process.
