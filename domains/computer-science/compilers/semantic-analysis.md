---
id: semantic-analysis
title: Semantic Analysis Phase
domain: computer-science
course: compilers
prerequisites:
- id: abstract-syntax-trees
  type: hard
- id: symbol-tables-and-scope
  type: hard
- id: formal-logic-propositions
  type: soft
builds-toward:
- type-inference-algorithms
- intermediate-code-representation
tags:
- semantic-analysis
- type-checking
- language-semantics
stage: advanced
status: draft
---

# Semantic Analysis Phase

## Core Idea
Semantic analysis checks the AST for semantic correctness beyond syntax. It verifies that identifiers are declared before use, types are compatible, function calls have correct arities, and other language rules are obeyed. This phase builds symbol tables, resolves names, and annotates the AST with type information. Errors here (undefined variables, type mismatches) are caught before code generation.
