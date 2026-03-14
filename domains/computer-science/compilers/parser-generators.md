---
id: parser-generators
title: Parser Generators and Yacc/Bison
domain: computer-science
course: compilers
prerequisites:
- id: ll-parsing
  type: soft
- id: lr-parsing
  type: soft
tags:
- parser-generators
- tools
- automating-parsing
stage: advanced
status: draft
---

# Parser Generators and Yacc/Bison

## Core Idea
Parser generators (Yacc, Bison, ANTLR) automatically generate parsers from declarative grammar specifications. A generator reads a context-free grammar, computes parsing tables (LR tables, LL sets), and emits parser code. This automation reduces error-prone manual coding and simplifies grammar changes. Most real-world compilers use parser generators rather than hand-written parsers.
