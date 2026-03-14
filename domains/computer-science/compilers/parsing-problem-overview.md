---
id: parsing-problem-overview
title: The Parsing Problem
domain: computer-science
course: compilers
prerequisites:
- id: context-free-grammars-compiler-design
  type: hard
- id: lexical-analyzer-design
  type: hard
builds-toward:
- ll-parsing
- lr-parsing
tags:
- parsing
- syntax-analysis
- problem-formulation
stage: advanced
status: draft
---

# The Parsing Problem

## Core Idea
Syntax analysis (parsing) determines whether a token stream is valid according to a grammar and builds a parse tree or AST. The problem is: given a CFG and input tokens, construct a derivation tree. Not all grammars admit efficient parsing; ambiguous grammars have multiple derivations. Practical parsers require restrictive grammar classes (LL, LR) or disambiguating rules.
