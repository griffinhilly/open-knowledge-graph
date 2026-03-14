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
