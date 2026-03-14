---
id: three-address-intermediate-code
title: Three-Address Intermediate Code
domain: computer-science
course: compilers
prerequisites:
- id: intermediate-code-representation
  type: hard
- id: ast-node-representation
  type: hard
builds-toward:
- quadruple-intermediate-representation
- basic-block-analysis
tags:
- ir
- intermediate-representation
- code-generation
stage: advanced
status: draft
---

# Three-Address Intermediate Code

## Core Idea
Three-address code is a popular intermediate representation where each instruction has at most three operands and one operation. 3AC is linear (easy to optimize sequentially), easy to generate from ASTs, and straightforward to translate to machine code.

## How It's Best Learned
Write a code generator producing 3AC from an AST. Manually optimize 3AC to understand what compilers must do.

## Common Misconceptions
Three-address code is the only intermediate representation (SSA, bytecode, and tree-based IRs exist). All 3AC is equally easy to optimize (SSA form has special properties).
