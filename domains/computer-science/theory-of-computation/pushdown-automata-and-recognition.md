---
id: pushdown-automata-and-recognition
title: Pushdown Automata and CFG Recognition
domain: computer-science
course: theory-of-computation
prerequisites:
- id: context-free-grammars-and-languages
  type: hard
builds-toward:
- cfg-pda-equivalence
- closure-properties-context-free
tags:
- pushdown-automata
- pda
- recognition
stage: abstract-reasoning
status: draft
---

# Pushdown Automata and CFG Recognition

## Core Idea
A pushdown automaton (PDA) extends a finite automaton with a stack, allowing it to recognize context-free languages. A PDA's transition depends on the current state, input symbol, and top-of-stack symbol, and can push or pop from the stack. PDAs accept by empty stack or final state.

## Explainer

You already know that context-free grammars generate languages by applying production rules — starting from a start symbol and rewriting nonterminals until only terminals remain. A **pushdown automaton** (PDA) is the machine that *recognizes* those same languages. The key question shifts from "how do I generate this string?" to "given this string, can a machine verify it belongs to the language?" The answer requires more power than a finite automaton, and that extra power comes from exactly one addition: an unbounded stack.

Think of a PDA as a finite automaton that can also scribble notes on a notepad — but only on the top page, and it can only read or remove the top page. At each step, the machine looks at three things: its current state, the next input symbol (or nothing, for an ε-transition), and whatever symbol sits on top of the stack. Based on this triple, it chooses a new state and decides what to push onto or pop from the stack. This stack gives the PDA a form of memory that finite automata lack — specifically, the ability to count and match nested structures. Consider the language {aⁿbⁿ | n ≥ 0}: a PDA pushes a marker for every `a` it reads, then pops one marker for every `b`. If the stack is empty exactly when the input is exhausted, the string is accepted. No finite automaton can do this because it would need infinitely many states to track arbitrarily large n.

PDAs come in two acceptance flavors. **Accept by final state** means the PDA enters a designated accepting state after consuming all input — the stack contents don't matter. **Accept by empty stack** means the PDA has consumed all input and the stack is completely empty — no special accepting state is needed. These two modes are equivalent in power: any language recognized by one type can be recognized by the other, though the constructions to convert between them add extra states and stack symbols. This equivalence is important because some grammars translate more naturally into one acceptance mode than the other.

The deep result connecting PDAs to your prerequisite knowledge is that PDAs recognize exactly the context-free languages — no more, no less. Every context-free grammar can be converted into an equivalent PDA (typically using accept-by-empty-stack, where production rules become push operations), and every PDA can be converted back into a context-free grammar. This equivalence means that the generative view (grammars) and the recognition view (automata) are two perspectives on the same class of languages. Understanding PDAs prepares you for proving this equivalence formally and for exploring which languages lie beyond context-free — those requiring even more powerful machines.
