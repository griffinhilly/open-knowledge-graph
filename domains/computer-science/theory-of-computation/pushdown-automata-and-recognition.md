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
