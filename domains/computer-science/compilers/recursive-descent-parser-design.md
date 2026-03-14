---
id: recursive-descent-parser-design
title: Recursive Descent Parser Design
domain: computer-science
course: compilers
prerequisites:
- id: grammar-design-for-compilation
  type: hard
- id: recursion-basics
  type: hard
- id: tree-traversals
  type: soft
builds-toward:
- syntax-error-recovery-techniques
tags:
- top-down-parsing
- hand-written
- parser
stage: advanced
status: draft
---

# Recursive Descent Parser Design

## Core Idea
Recursive descent parsing converts grammar rules directly into mutually-recursive functions. This approach is easy to implement and debug, though it works best with left-factored grammars. Understanding RDP reveals the deep connection between grammars and code.

## How It's Best Learned
Write a recursive descent parser by hand for a small language. Implement error recovery and careful lookahead handling.

## Common Misconceptions
LL(1) is the only restriction for RDP (you can use limited lookahead or backtracking). RDP is not used in real compilers (many modern compilers use hand-written RDP).
