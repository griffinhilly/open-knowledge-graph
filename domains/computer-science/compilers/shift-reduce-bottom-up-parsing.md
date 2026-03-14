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
status: draft
---

# Shift-Reduce Bottom-Up Parsing

## Core Idea
Bottom-up shift-reduce parsers build parse trees from leaves up, using a stack to accumulate symbols and reduce them when grammar rules match. This approach is more powerful than top-down parsing and handles a wider class of unambiguous grammars.

## How It's Best Learned
Manually build shift-reduce parse trees for example inputs. Implement a simple shift-reduce parser with an explicit stack.

## Common Misconceptions
Only bottom-up parsing is real parsing (top-down is equally valid; choice depends on grammar and application). Shift-reduce parsers are always faster (table size and construction complexity are trade-offs).
