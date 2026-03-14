---
id: ll-parsing
title: LL Parsing and Predictive Parsing
domain: computer-science
course: compilers
prerequisites:
- id: parsing-problem-overview
  type: hard
- id: stacks-data-structure
  type: hard
builds-toward:
- parser-generators
tags:
- top-down-parsing
- recursive-descent
- predictive-parsing
stage: advanced
status: draft
---

# LL Parsing and Predictive Parsing

## Core Idea
LL(k) parsing is top-down, deterministic parsing using k lookahead tokens. An LL(1) parser uses a single lookahead token to predict which production rule to apply. It can be implemented as a recursive descent parser (function per nonterminal) or via a table-driven parser. LL grammars must be non-left-recursive and free of ambiguity, limiting expressiveness but enabling simple implementation.
