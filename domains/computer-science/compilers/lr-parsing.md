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
status: draft
---

# LR Parsing Fundamentals

## Core Idea
LR parsing is bottom-up, deterministic parsing that constructs a parse tree by reducing input tokens to the start symbol. An LR parser maintains a stack of states and a lookahead token; each state encodes all possible actions (shift or reduce). LR parsers handle a much larger grammar class than LL, including left-recursive grammars, making them suitable for real programming languages.
