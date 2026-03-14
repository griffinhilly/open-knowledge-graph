---
id: tree-walking-interpreters
title: Tree-Walking Interpreters
domain: computer-science
course: compilers
prerequisites:
- id: abstract-syntax-trees
  type: hard
- id: recursion-basics
  type: hard
builds-toward:
- type-inference-algorithms
tags:
- interpreters
- execution
- ast-traversal
stage: advanced
status: draft
---

# Tree-Walking Interpreters

## Core Idea
A tree-walking interpreter executes a program by recursively traversing its AST, evaluating each node according to language semantics. Evaluation of an expression node typically involves evaluating its children and applying an operation. Tree-walking is simple to implement but slower than compiled execution. It's useful for prototyping languages and understanding semantics.
