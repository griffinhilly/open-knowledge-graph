---
id: symbol-tables-and-scope
title: Symbol Tables and Scope Resolution
domain: computer-science
course: compilers
prerequisites:
- id: hash-tables
  type: hard
- id: abstract-syntax-trees
  type: hard
builds-toward:
- semantic-analysis
- type-inference-algorithms
tags:
- symbol-table
- scope
- name-resolution
stage: advanced
status: draft
---

# Symbol Tables and Scope Resolution

## Core Idea
A symbol table is a data structure mapping identifiers to their properties (type, storage location, scope). Scoping rules determine which declaration a name reference refers to. Block scoping creates nested symbol tables; a name lookup searches the current scope, then outer scopes (the scope chain). Proper scope handling prevents name collisions and enables separate compilation of modules.
