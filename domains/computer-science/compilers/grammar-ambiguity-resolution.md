---
id: grammar-ambiguity-resolution
title: Grammar Ambiguity and Resolution
domain: computer-science
course: compilers
prerequisites:
- id: context-free-grammars
  type: hard
- id: parser-conflict-resolution
  type: hard
builds-toward:
- lookahead-and-parsing-power
tags:
- parsing
- grammars
- ambiguity
stage: advanced
status: draft
---

# Grammar Ambiguity and Resolution

## Core Idea
Ambiguous grammars produce multiple valid parse trees for the same input, causing unpredictable parsing. Disambiguation uses conflict resolution rules (precedence, associativity) or grammar restructuring to eliminate ambiguity. Detecting and resolving ambiguity is critical for deterministic compilation.

## How It's Best Learned
Take the classic dangling-else problem: parse it with an ambiguous grammar, see why it fails, then restructure the grammar and verify unique parsing.

## Common Misconceptions
Using associativity/precedence directives 'fixes' an ambiguous grammar—they only select one parse tree among many, masking the underlying ambiguity.
