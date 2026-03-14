---
id: ast-node-representation
title: AST Node Representation
domain: computer-science
course: compilers
prerequisites:
- id: abstract-syntax-trees
  type: hard
- id: recursion-basics
  type: hard
builds-toward:
- attribute-grammar-framework
tags:
- ast
- data-structures
- representation
stage: advanced
status: draft
---

# AST Node Representation

## Core Idea
AST nodes must efficiently represent program structure and support traversal, annotation, and transformation. Node representation choices—classes, variant types, tagged unions—affect memory, performance, and pattern matching.

## How It's Best Learned
Implement AST nodes using different strategies (classes vs unions vs tagged pointers). Measure memory and traversal performance differences.

## Common Misconceptions
AST design is obvious (it is actually a key design decision). ASTs should mirror the grammar exactly (often they abstract away syntactic sugar).
